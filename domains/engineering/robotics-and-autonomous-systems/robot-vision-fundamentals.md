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
