---
id: visual-servoing
title: Visual Servoing and Image-Based Robot Control
domain: engineering
course: robotics-and-autonomous-systems
prerequisites:
- id: robot-vision-fundamentals
  type: hard
- id: jacobian-robot-control
  type: hard
- id: feedback-control-fundamentals
  type: soft
builds-toward:
- simultaneous-localization-and-mapping
tags:
- visual-servoing
- image-based-control
- feature-tracking
- eye-in-hand
- eye-to-hand
- servoing-law
stage: advanced
status: validated
---

# Visual Servoing and Image-Based Robot Control

## Core Idea
Visual servoing uses image features (corners, colors, edges, fiducials) to control the robot's motion. **Image-based visual servoing** defines the control goal directly in image space: bring detected features to desired image positions. **Position-based visual servoing** estimates the 3D position of features and controls the robot in 3D space. **Hybrid servoing** combines both approaches. The image Jacobian (or interaction matrix) L relates camera/end-effector velocity to the rate of change of image features. The control law v = -λ·L^(-1)·e drives the feature error e to zero. Key advantages: no explicit 3D perception or inverse kinematics required (image-based); direct use of the quantities being measured. Key challenges: singularities and local minima in feature space; feature loss when the target moves out of view.

## How It's Best Learned
Implement image-based servoing in simulation (e.g., V-REP, Gazebo with vision). Start simple: detect a red blob or color marker in the image, compute its centroid pixel position (u, v), and write a control law that moves the robot to center the blob in the image. Graduate to point-feature servoing: detect 2D corners using SIFT or ORB, match them to a reference image, and compute the image Jacobian. Move to eye-in-hand configuration: as the camera moves with the end-effector, the feature motion in the image reflects both rotation and translation of the camera, which is richer than eye-to-hand. Verify convergence of the visual servoing loop and observe stability.

## Common Misconceptions
- Image-based visual servoing always reaches the correct 3D pose; it minimizes image feature error, which doesn't guarantee the desired 3D configuration. Local minima and singularities can prevent reaching the target.
- The image Jacobian L is constant throughout the motion; actually L depends on camera motion and changes as the robot moves and features appear at different image locations.
- Fast image processing is needed for servoing stability; with proper control design, image rates of 10-30 Hz are often sufficient because the servoing loop naturally filters high-frequency noise.
- Visual servoing is only useful for fine manipulation; in fact, it is effective from large distances (object visible anywhere in image) down to mm-scale precision.

## Questions

```yaml
- question: "In image-based visual servoing, the control goal is to drive image feature position from current location s(u, v) to desired location s*. The control law is v = -λ·L^(-1)·(s - s*), where L is the image Jacobian. What does the term L^(-1) accomplish?"
  type: multiple-choice
  options:
    - "It inverts the camera distortion to correct the image"
    - "It converts the desired image feature change (s - s*) into camera velocity v required to achieve that change"
    - "It amplifies the error signal to make the servoing faster"
    - "It filters high-frequency noise from the feature measurement"
  answer: 1
  explanation: "The image Jacobian L relates camera velocity v_cam to feature velocity in image space: ds/dt = L · v_cam. Inverting this relationship gives v_cam = L^(-1) · ds/dt. In the control law, the desired feature change is (s* - s) (moving toward the goal), so the required camera velocity is v = -λ · L^(-1) · (s - s*). The negative sign indicates feedback: we move toward the goal by reducing error. L^(-1) is the key: it translates pixel-space error into physical camera motion."

- question: "A robot uses eye-to-hand visual servoing: the camera is fixed on a desk observing the workspace. The robot's end-effector must pick up an object detected in the image at pixel (150, 200). As the robot moves, how does the object's image position change?"
  type: multiple-choice
  options:
    - "The image position changes only if the object moves in 3D space"
    - "The image position changes only if the camera moves (but camera is fixed, so it doesn't change)"
    - "The image position changes due to parallax: as the robot arm moves closer or farther from the camera's viewpoint, object occlusion or perspective changes the apparent position"
    - "The image position doesn't change; the object is stationary"
  answer: 2
  explanation: "In eye-to-hand configuration, the camera observes from a fixed viewpoint. When the robot moves, it doesn't change the camera position. However, if the robot arm (gripper) moves in front of the camera or closer to the camera, the perspective changes. More critically, the object's image position depends on its 3D position relative to the camera. If the object is on a table and the robot approaches, the image perspective can shift due to parallax. The servoing challenge is that the image Jacobian for eye-to-hand includes the perspective effects of the arm motion relative to the fixed camera, which couples position and orientation in complex ways."

- question: "In eye-in-hand visual servoing, the camera is mounted on the robot's end-effector. As the robot moves to grasp an object, the camera motion directly moves the image features. The image Jacobian for this configuration includes:"
  type: multiple-choice
  options:
    - "Only the translational velocity of the camera, ignoring rotation"
    - "Only the rotational velocity of the camera, ignoring translation"
    - "Both translational and rotational velocity of the camera, since features move in the image due to both camera translation and rotation"
    - "Neither; the image Jacobian is undefined for eye-in-hand servoing"
  answer: 2
  explanation: "Eye-in-hand servoing is richer than eye-to-hand because the camera rotates with the gripper. A feature at 3D position P experiences image motion due to: (1) camera translation: if the camera moves forward, points in the scene appear to shift backward in the image (opposite direction, perspective effect). (2) Camera rotation: if the camera rotates, points rotate in the image. The image Jacobian L must account for both, making it a 2×6 matrix (2 image coordinates × 6-DOF camera velocity: 3 translation + 3 rotation). This richer coupling actually simplifies some servoing tasks because the camera can reach singularities less easily."

- question: "During image-based visual servoing, if all detected features suddenly disappear from the image (the object leaves the field of view), the control law v = -λ·L^(-1)·e can no longer compute robot velocity because e is undefined. How is this problem typically handled?"
  type: multiple-choice
  options:
    - "Stop the robot immediately and sound an alarm"
    - "Use the last known feature velocity to continue moving in a dead-reckoning mode"
    - "Predict the feature position based on past motion using a Kalman filter, allowing servoing to continue through temporary occlusions"
    - "Switch to a different control mode (e.g., position-based control using 3D pose estimation) that doesn't depend on image features"
  answer: 3
  explanation: "Predictive approaches (Kalman filtering) can extend servoing through brief occlusions, but they accumulate drift. More robust approaches avoid feature loss by: (1) using multiple features (if one disappears, others remain), (2) monitoring feature visibility and slowing the robot before it exits the field of view, or (3) switching to complementary sensing modes when vision fails. In autonomous servoing, systems often combine vision with other sensors (position control, force feedback) to maintain robustness. Complete feature loss is a fundamental limitation: without visual measurement, the controller has no feedback and must default to open-loop motion or stop."

- question: "The image-based visual servoing control law v = -λ·L^(-1)·(s - s*) drives the image feature error to zero. What is guaranteed to be true when the feature error reaches zero?"
  type: multiple-choice
  options:
    - "The robot has reached the desired 3D position and can grasp the object"
    - "The image feature is at the desired pixel location, but the robot's 3D position may differ from the desired position due to local minima or singularities in feature space"
    - "The camera and the object are in the same reference frame"
    - "All aspects of the robot's pose have been correctly adjusted"
  answer: 1
  explanation: "Image-based visual servoing minimizes image feature error, not 3D pose error. When image error reaches zero, the feature is at the desired image location. However, this doesn't guarantee the correct 3D pose. Example: the camera could be at any position along the ray passing through the feature pixel and the camera center—by moving along this ray (forward or backward), the feature stays at the same image position. This ambiguity is the fundamental limitation of monocular image-based servoing. Position-based servoing (using depth or 3D pose estimation) avoids this by explicitly controlling 3D position, but at the cost of requiring accurate 3D perception."

- question: "Explain why the image Jacobian L becomes ill-conditioned (high condition number) near servoing singularities, and what this means for control stability."
  type: short-answer
  answer: "Near a singularity, the robot loses degrees of freedom: some Cartesian motions become unachievable, so the image Jacobian loses rank. When L is nearly singular, L^(-1) amplifies small measurement noise and errors into large camera velocity commands. A small error in feature detection gets magnified, causing jerky, unstable control. The condition number κ = σ_max / σ_min characterizes this: high condition number means the Jacobian is ill-conditioned, and control becomes sensitive to noise. Practically, this means servoing near singularities is difficult and unreliable. Motion planning in visual servoing should detect and avoid singularities, or use pseudo-inverse methods (e.g., J^+ = J^T(JJ^T + λ²I)^(-1)) that regularize the inversion and reduce noise sensitivity at the cost of slightly reduced performance."
  explanation: "Regularization (Tikhonov damping with parameter λ) is the standard solution: J^+ = J^T(JJ^T + λ²I)^(-1) doesn't truly invert J but computes a least-squares solution that is numerically stable even when J is singular. This is especially important in visual servoing where noise in feature detection is unavoidable."
```

## Explainer

Imagine a robot arm with a camera mounted on its gripper (eye-in-hand configuration) observing an object to be grasped. You could approach this problem using forward kinematics, inverse kinematics, and pose estimation: (1) detect the object, (2) estimate its 3D position, (3) compute a grasp pose, (4) solve inverse kinematics, (5) move the robot. Each step introduces measurement error and computational load. Visual servoing takes a more direct approach: use the image features themselves as the control feedback.

**Image-based visual servoing** specifies the goal directly in image space. For example: "move the robot until the object's image center is at pixel (320, 240) (image center)." The error in image space is e = s - s*, where s is the current feature position and s* is the desired position (both in pixel coordinates). A control law v = -λ·L^(-1)·e computes the camera velocity v (translation and rotation) required to drive the feature error to zero. The image Jacobian L is the key: it relates camera motion to feature motion in the image. Mathematically, ds/dt = L·v_camera, so v_camera = L^(-1)·ds/dt. By feedback, we compute v = -λ·L^(-1)·e, where e = s - s* is the error we want to drive to zero.

The image Jacobian depends on the feature type and camera configuration. For a point feature (x, y) in image coordinates and an eye-in-hand camera with 6-DOF velocity (v_x, v_y, v_z, ω_x, ω_y, ω_z), the Jacobian is 2×6. Each column represents how the feature moves when the camera moves in one direction. For example, if the camera translates forward (v_z > 0) toward an object, the object appears to move backward in the image (negative image velocity), creating a perspective effect.

**Eye-in-hand vs. eye-to-hand configuration** affects the Jacobian significantly. In **eye-in-hand**, the camera moves with the end-effector, so its motion directly affects the image. In **eye-to-hand**, the camera is fixed on the workspace, and the robot moves relative to the camera. Eye-in-hand is generally preferred because the Jacobian is simpler and richer (rotation provides additional constraints that help avoid singularities). However, eye-to-hand is sometimes used in manufacturing when a single camera observes multiple robots or when occlusion by the arm is unacceptable.

The control law is simple: compute the image Jacobian L (which depends on current 3D geometry and feature depth), measure the feature error e in the image, and command robot velocity v = -λ·L^(-1)·e. The proportional gain λ determines the control speed. A small λ gives slow, stable convergence; a large λ gives fast but potentially oscillatory response. As the robot moves, the features change position in the image, reducing the error. When error reaches zero, the features are at the desired image positions, and (ideally) the robot has reached the desired configuration.

**Key advantages** of visual servoing: (1) **Direct measurement**: you measure image features, not something computed from them, so measurement noise is minimized. (2) **No 3D perception required**: you don't need to estimate the object's 3D position; you control in the image space where measurement is direct. (3) **Scalable**: from large distances (grasp a part across the table) to mm precision (inserting a plug), the same algorithm applies. (4) **Robust to calibration errors**: small errors in camera calibration or robot kinematics affect the Jacobian but don't prevent convergence—the feedback loop self-corrects.

**Key challenges**: (1) **Singularities**: the image Jacobian can become singular in certain configurations, losing control authority. (2) **Local minima**: if the feature appears in multiple places (e.g., a repetitive pattern), the servoing may converge to the wrong instance. (3) **Feature loss**: if the object leaves the field of view or is occluded, control fails. (4) **Computation**: computing the image Jacobian L and its inverse requires real-time geometric calculations.

**Practical implementation** combines image-based servoing with other sensing modalities: force feedback (to detect contact), position control (for robustness), and trajectory planning (to avoid singularities). Advanced systems use **hybrid servoing**: some DOFs controlled in image space (precise visual positioning), others controlled in 3D space (e.g., height above the table) or with force feedback (contact force during insertion). This hybrid approach leverages the strengths of visual servoing (precision in the image plane) while maintaining robustness in other dimensions.

Visual servoing is a mature technology used extensively in industrial manipulation, assembly, medical robotics, and autonomous systems. Its elegance lies in using the visual measurement directly for control, closing a tight sensorimotor feedback loop.
