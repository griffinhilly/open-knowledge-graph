---
id: robot-vision-fundamentals
title: Robot Vision Fundamentals
domain: engineering
course: robotics-and-autonomous-systems
prerequisites:
- id: actuators-and-sensors-robotics
  type: soft
builds-toward:
- visual-servoing
- lidar-and-point-clouds
tags:
- computer-vision
- object-detection
- image-features
- robot-perception
- camera-calibration
stage: advanced
status: validated
---

# Robot Vision Fundamentals

## Core Idea
Robots use cameras to perceive and interact with the environment. The camera model relates 3D world coordinates to 2D image pixel coordinates through intrinsic parameters (focal length, principal point) and extrinsic parameters (pose relative to the robot base). Image processing extracts features (corners, edges, colors) that identify objects or landmarks. Object detection localizes targets in images; pose estimation recovers 6-DOF position and orientation from visual features. Vision feedback enables visual servoing (moving the robot to achieve a visual goal) and semantic understanding (recognizing objects and scenes).

## How It's Best Learned
Calibrate a camera using a checkerboard pattern and OpenCV: compute intrinsic matrix K from multiple checkerboard images, then verify accuracy by reprojecting 3D points onto images. Detect features (SIFT, SURF, ORB) in robot workspace images and match them across views to estimate structure. Perform pose estimation using PnP (Perspective-n-Point) on a known object. Implement simple visual servoing: detect a colored object, compute its image position, convert to desired robot motion using the Jacobian.

## Common Misconceptions
- Camera intrinsics are the same for all cameras of the same model; actually, each camera must be individually calibrated due to manufacturing variations.
- High image resolution always improves vision accuracy; beyond a certain point, resolution doesn't help and increases computational load.
- Detected features are perfectly accurate; in reality, feature detection is noisy and requires filtering, outlier rejection, and robust estimation.
- Vision feedback must be high-speed (100+ Hz) for safe robot operation; in practice, 10-30 Hz is often sufficient with proper control design.

## Questions

```yaml
- question: "A camera with focal length f = 1000 pixels and principal point c = (320, 240) is calibrated to have intrinsic matrix K = [[1000, 0, 320], [0, 1000, 240], [0, 0, 1]]. A 3D point at world position P_w = (0.1, 0.05, 1.0) m (1 meter in front of the camera) projects onto the image at:"
  type: multiple-choice
  options:
    - "Image pixel (420, 290)"
    - "Image pixel (220, 190)"
    - "Image pixel (320, 240) (the principal point)"
    - "Insufficient information; need the extrinsic pose of the camera"
  answer: 0
  explanation: "The intrinsic matrix K relates camera frame coordinates to image pixels: p_image = K · P_camera. If the world frame is aligned with the camera frame, then P_camera = (0.1, 0.05, 1.0). Normalized image coordinates: (x, y) = (0.1/1.0, 0.05/1.0) = (0.1, 0.05). Pixel coordinates: p = K · [0.1, 0.05, 1]^T = [1000·0.1 + 320, 1000·0.05 + 240] = [420, 290]. This is the projection formula p_image = K · (P_camera / P_z)."

- question: "Camera calibration computes the intrinsic matrix K and the extrinsic parameters (rotation R and translation t from world to camera). Why is calibration necessary even if the camera's focal length and image resolution are known?"
  type: multiple-choice
  options:
    - "Calibration is not necessary; the focal length and resolution fully specify the camera"
    - "Calibration is needed to compute lens distortion coefficients, which are significant at the edges of the image"
    - "Calibration is needed to find the principal point (image center), which may not be exactly at the image center pixel due to manufacturing variations"
    - "Calibration is needed to determine the extrinsic pose of the camera relative to the robot base"
  answer: 3
  explanation: "All three reasons are valid. The principal point (image center) is usually close to the pixel image center but not exactly, due to manufacturing tolerance. Lens distortion (radial and tangential) is present in most cameras and must be corrected. Most importantly, the extrinsic transformation from world (or robot base) coordinates to camera coordinates must be determined through calibration. Intrinsic parameters alone don't give you the 3D position of detected objects."

- question: "In visual servoing, the goal is to drive a visual feature to a desired image position. If a red ball is detected at pixel (100, 300) but the desired setpoint is (320, 240) (image center), the control error in image space is (220, -60) pixels. How should this error be converted to robot motion?"
  type: multiple-choice
  options:
    - "Move the robot left and up in Cartesian space to directly push the feature toward the desired position"
    - "Compute the image Jacobian J_image relating camera motion to feature motion, then solve for camera velocity: v_camera = J_image^(-1) · error"
    - "Use the error to command the robot to move toward the detected ball in 3D space, without using image geometry"
    - "Increase the proportional gain K_p in the image control law to accelerate the feature to the setpoint"
  answer: 1
  explanation: "The image Jacobian relates how camera motion produces feature motion in the image. If the camera moves by δx_camera, the feature moves by δx_image = J_image · δx_camera. Inverting this relationship gives the camera velocity needed to drive the feature error to zero. This is the foundation of image-based visual servoing. The error is directly in image space (pixels), so the controller directly commands camera motion to reduce pixel error, which implicitly moves the robot to the desired configuration."

- question: "A checkerboard pattern is used to calibrate a camera. The checkerboard is shown to the camera from multiple viewing angles and distances. Why must the checkerboard be shown from different viewpoints?"
  type: true-false
  answer: true
  explanation: "Different viewpoints are necessary to fully constrain the camera parameters. A single image provides only 2D information (pixel coordinates); multiple images from different angles provide geometric relationships that enable estimation of 3D parameters (focal length, principal point, lens distortion). Additionally, viewing from different distances helps constrain radial distortion. A single viewpoint could technically constrain the intrinsic matrix if the checkerboard size is known, but multiple viewpoints improve numerical stability and allow estimation of extrinsic parameters."

- question: "In robot grasping, a camera detects the 3D position of an object using detection and depth estimation. The camera outputs a bounding box in 2D image coordinates and a depth value. To grasp the object, the robot must convert this to 3D world coordinates and plan a gripper approach. Explain the steps."
  type: short-answer
  answer: "Step 1: Convert 2D bounding box center (u, v) to 3D camera frame coordinates using the intrinsic matrix K and depth z: P_camera_x = (u - c_x) · z / f_x, P_camera_y = (v - c_y) · z / f_y, P_camera_z = z. Step 2: Transform from camera frame to robot base frame using extrinsic parameters: P_world = R · P_camera + t, where R and t are the calibrated rotation and translation from camera to base. Step 3: Use inverse kinematics to find the gripper pose (slightly offset above the object) that the robot must achieve. Step 4: Plan a trajectory from the current configuration to the grasp pose, execute, close the gripper, and lift."
  explanation: "This pipeline combines camera geometry, kinematics, and planning. Each step requires accurate calibration and computation. Errors in camera calibration propagate to errors in perceived 3D positions, degrading grasp success. This is why robots in manufacturing are carefully calibrated with hand-eye calibration (determining T_camera_to_base) as a critical setup step."
```

## Explainer

A camera is an optical sensor that captures light reflected from the 3D world and converts it into a 2D image. For a robot to use this image to understand and interact with the environment, the robot must know the geometric relationship between image coordinates and 3D world coordinates. This is the domain of **robot vision**.

The **pinhole camera model** is the foundation. Light from a 3D point P_world passes through a focal point (the camera center) and projects onto an image plane. The intrinsic matrix K maps 3D camera-frame coordinates to 2D image pixels:

p_image = K · P_camera / P_camera_z

where K = [[f_x, 0, c_x], [0, f_y, c_y], [0, 0, 1]] contains the focal length (f_x, f_y in pixels) and the principal point (c_x, c_y) where the optical axis intersects the image plane. The extrinsic parameters (rotation matrix R and translation vector t) transform points from world frame to camera frame:

P_camera = R · P_world + t

**Camera calibration** determines K and optionally (R, t). Using a checkerboard pattern shown from multiple viewpoints, calibration algorithms estimate the intrinsic parameters by fitting the camera model to detected corners in the images. Calibration also estimates **lens distortion**: real cameras have radial distortion (straight lines curve outward or inward) and tangential distortion. These distortions are corrected using polynomial coefficients computed during calibration. After calibration, image coordinates can be undistorted, and the pixel-to-3D projection becomes accurate.

**Object detection** identifies objects of interest in the image. **Classical methods** extract hand-crafted features (SIFT, SURF, ORB) and match them across images or to reference templates. **Deep learning methods** (CNNs like YOLO, Faster R-CNN) directly predict bounding boxes and class labels from raw images, achieving higher accuracy at the cost of computational load. Once an object is detected in 2D (bounding box), **depth estimation** determines how far away it is. This can come from a separate depth sensor (stereo camera, Time-of-Flight sensor) or from monocular depth estimation (a trained neural network).

**Pose estimation** recovers the 6-DOF position and orientation of a known object from its image. **Perspective-n-Point (PnP)** methods use detected feature matches: if you know the 3D object model and can detect and match features in the image, you solve for the pose. For known geometric objects (like a QR code or fiducial marker), you can directly compute pose from the marker's image corners.

**Visual servoing** uses vision feedback to control the robot. **Image-based visual servoing** specifies the control goal in image space: e.g., "move the robot until the detected ball is at the image center." The image Jacobian J_image relates camera motion to feature motion in the image. A proportional controller in image space (error = feature_position - desired_position, command = -K_p · error) drives the feature to the setpoint, which automatically positions the robot correctly. The advantage is that you don't need to explicitly solve inverse kinematics or measure 3D position; you control directly in image space where the error is measured. **Position-based visual servoing** estimates the 3D position and orientation of the target, then uses inverse kinematics to command the robot. This approach is more intuitive but requires accurate 3D perception.

**Hand-eye calibration** is a critical procedure that determines the spatial relationship between the camera and the robot's end-effector. By moving the robot to known poses and observing how the image changes, you can solve for the camera's position and orientation relative to the base or gripper. This enables the robot to coordinate vision with manipulation.

Robot vision is a rich field combining geometry, optimization, machine learning, and control. At its core, it bridges perception (what the camera sees) and action (what the robot does) by establishing the geometric and semantic relationships between images and 3D reality.
