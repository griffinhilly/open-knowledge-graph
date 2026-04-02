---
id: simultaneous-localization-and-mapping
title: Simultaneous Localization and Mapping (SLAM)
domain: engineering
course: robotics-and-autonomous-systems
prerequisites:
- id: kalman-filter-state-estimation
  type: hard
- id: lidar-and-point-clouds
  type: soft
- id: visual-servoing
  type: soft
builds-toward: []
tags:
- slam
- localization
- mapping
- loop-closure
- visual-slam
- lidar-slam
- bundle-adjustment
stage: expert
status: validated
---

# Simultaneous Localization and Mapping (SLAM)

## Core Idea
SLAM solves the chicken-and-egg problem: to build a map, the robot needs to know where it is; to know where it is, it needs a map. The solution is to simultaneously estimate the robot's pose (position and orientation) and the map of the environment, with uncertainty propagation through a Kalman filter or graph optimization. **Visual SLAM** uses camera images; **LiDAR SLAM** uses point cloud registration. A critical component is **loop closure**: when the robot returns to a previously visited location, the detector recognizes it and adds a constraint that corrects accumulated drift. The result is a consistent, driftless map. SLAM enables autonomous navigation, exploration, and 3D reconstruction without pre-built maps.

## How It's Best Learned
Implement a simple monocular visual SLAM from scratch: feature extraction (SIFT/ORB), matching between frames, computing the essential matrix, triangulation of 3D points, pose estimation via PnP, bundle adjustment to refine estimates. Observe how drift accumulates as the robot moves. Add loop closure: when the current frame matches a past frame, add a loop constraint to optimize the full trajectory. Move to using existing SLAM frameworks (ORB-SLAM2 for visual, LOAM or LeGO-LOAM for LiDAR). Run on real sensor data and visualize the reconstructed map and camera trajectory.

## Common Misconceptions
- SLAM produces a perfect map by integrating all sensor observations; in reality, drift and errors are unavoidable without loop closure and global optimization.
- Loop closure can be added to any SLAM system; actually, loop closure requires place recognition (detecting revisited locations), which is non-trivial and often fails in featureless or repetitive environments.
- Visual SLAM works in all lighting conditions; actually, feature-based visual SLAM fails in low light, rain, or motion blur. LiDAR SLAM is more robust to lighting.
- SLAM runs in real-time on standard CPUs; modern SLAM systems require GPU acceleration for real-time performance on high-frame-rate sensors.

## Questions

```yaml
- question: "In a visual SLAM system, the robot moves forward while a camera observes static landmark features. Over time, odometry (integrating motion estimates) accumulates drift. How does SLAM with loop closure correct this drift?"
  type: multiple-choice
  options:
    - "Loop closure detects when the robot returns to a familiar location and immediately resets the pose to the past estimate, erasing the accumulated drift"
    - "Loop closure adds a constraint between the current pose and the previously-visited pose that they should be at the same location, then globally optimizes all poses in the trajectory to satisfy all constraints while minimizing total error"
    - "Loop closure marks the drift as an error and re-runs the entire motion estimation from the beginning with updated parameters"
    - "Loop closure is unnecessary; drift naturally vanishes as the robot continues exploring"
  answer: 1
  explanation: "The complementarity of visual and LiDAR SLAM drives modern sensor fusion approaches: visual SLAM provides rich detail and semantic understanding, LiDAR provides robust metric localization. Multi-sensor SLAM systems leverage both strengths."
```

## Explainer

Imagine a mobile robot exploring an unknown building with only a camera or LiDAR for sensing and encoders tracking wheel rotation (odometry). As the robot moves, it builds a map of observed features. The problem: odometry drifts over time (wheel slip, sensor noise), so the robot loses track of its true location. Without knowing its true position, the map is warped and inconsistent. Conversely, without a map, it's impossible to know where the robot is. This is the SLAM problem: estimate the robot's trajectory and map simultaneously.

**Filtering-based SLAM** (EKF-SLAM, particle filter SLAM) maintains a single state estimate: the robot pose and all landmark positions. The Kalman filter predicts state based on odometry and updates based on sensor observations (feature measurements). As the robot observes landmarks, observations constrain the pose, reducing uncertainty. The key insight is that observations of known landmarks improve localization, and building maps and localizing are tightly coupled. The state vector grows as new landmarks are discovered, making the filter slower over time.

**Graph-based SLAM** is more modern: represent the SLAM problem as a graph where nodes are robot poses (one node per time step or keyframe) and landmarks, and edges are constraints (odometry, sensor observations). The goal is to find the configuration of nodes that best satisfies all constraints in a least-squares sense. Bundle adjustment (in visual SLAM) or pose graph optimization (in general SLAM) solves this. Graph-based methods scale better than filtering as the environment grows.

**Visual SLAM** uses camera images:
1. **Initialization**: From two views, extract matching features, compute the essential matrix, triangulate 3D points.
2. **Pose estimation**: For each new frame, match features to existing 3D points, solve PnP (Perspective-n-Point) to get the camera pose.
3. **Mapping**: If sufficient features are tracked, add the frame as a keyframe and triangulate new 3D points.
4. **Loop closure**: Periodically check if the current frame matches any past keyframes (place recognition). If yes, add a loop constraint to the graph.
5. **Optimization**: Bundle adjustment refines all camera poses and 3D points.

The advantage of keyframes: instead of processing every frame, you selectively add frames that contribute new information (large motion or new areas). This reduces computation and redundancy.

**LiDAR SLAM** uses point cloud registration:
1. **Scan alignment**: Use ICP to align the current scan to the previous scan, estimating the motion.
2. **Pose estimation**: Integrate motion estimates from successive scans.
3. **Mapping**: Accumulate aligned scans into a global map.
4. **Loop closure**: When the current scan matches a past scan (detected via scan similarity), add a loop constraint.
5. **Optimization**: Pose graph optimization corrects the entire trajectory.

LiDAR SLAM is often more robust than visual SLAM because scan-to-scan alignment is a well-defined geometric problem (point cloud registration) with good convergence properties. Visual SLAM must handle feature matching, which can fail in repetitive or featureless environments.

**Loop closure** is the critical component that eliminates drift. The problem is **place recognition**: how do you know you've returned to a previous location? Visual SLAM uses image-based methods (matching visual features), LiDAR SLAM uses scan-based methods (matching point clouds). A detector with high precision (few false positives) is essential—a false loop closure adds a wrong constraint that corrupts the map.

Once a loop closure is detected, the full trajectory is optimized to satisfy all constraints simultaneously. Early poses (which had accumulated drift) are corrected based on late observations. The result is a globally consistent map and trajectory.

**Challenges**:
- **Place recognition**: Robust across viewpoint changes, lighting variations, and perceptual aliasing.
- **Scale ambiguity** (monocular visual SLAM): A single camera can't determine absolute scale; motion is ambiguous between moving forward slowly or backward quickly. Stereo cameras or LiDAR (which provide metric depth) resolve this.
- **Computational efficiency**: Real-time SLAM on mobile robots requires efficient feature detection, matching, and optimization.
- **Dynamic environments**: Moving people, vehicles, or other robots violate the SLAM assumption that the world is static. Robust outlier rejection is needed.

**Applications**: autonomous vehicles, drones, mobile robots in warehouses, hand-held 3D reconstruction devices, and underwater robotics. Modern visual SLAM systems (ORB-SLAM, ORB-SLAM3) can run real-time on modest hardware. LiDAR SLAM is standard in autonomous vehicles and industrial drones.

SLAM is one of the most important problems in robotics, and decades of research have produced mature, practical solutions. The field continues to evolve with deep learning approaches (neural depth estimation, learned place recognition) and tighter sensor fusion integration.
