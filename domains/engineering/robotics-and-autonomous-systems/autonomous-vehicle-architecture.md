---
id: autonomous-vehicle-architecture
title: Autonomous Vehicle Architecture
domain: engineering
course: robotics-and-autonomous-systems
prerequisites:
- id: perception-pipeline-autonomous
  type: hard
- id: decision-making-autonomous-driving
  type: hard
- id: control-system-structure-and-configuration
  type: soft
builds-toward:
- safety-verification-autonomous
tags:
- autonomy
- vehicle
- systems-integration
- real-time
- distributed
stage: expert
status: validated
---

# Autonomous Vehicle Architecture

## Core Idea
An autonomous vehicle is a real-time distributed system that must perceive its environment, make driving decisions under uncertainty, and execute control commands safely and reliably at highway speeds and in complex traffic. The architecture orchestrates perception (camera, lidar, radar), localization (GPS, IMU, wheel odometry fusion), prediction (where will other vehicles go?), planning (what path should we follow?), and control (steer, accelerate, brake angles). Each module runs on real-time constraints and must handle sensor failures, communication latency, and algorithmic uncertainty. The system must prioritize safety: when uncertainty is high or behavior is ambiguous, the system must detect degraded conditions and hand control to a human or safely stop rather than attempt risky decisions. Modern architectures separate the decision stack into distinct, testable layers: perception produces object detections; localization fuses multiple position sensors; planning reasons about feasible paths; control executes the planned path. This layering enables independent testing and modularity, though it can also mask dependencies and propagate errors from one layer to the next.

## Questions

```yaml
- question: "A level 4 autonomous vehicle suddenly loses GPS signal in an urban canyon (tall buildings block satellite coverage). The localization module was fusing GPS, IMU, and wheel odometry. What should happen?"
  type: multiple-choice
  options:
    - "The vehicle should immediately stop, because GPS is required for safe navigation"
    - "The vehicle should continue using IMU and wheel odometry, but accumulate drift over time; if drift exceeds a safety threshold, it should request human takeover or safe stop"
    - "The vehicle should request that the human driver resume control immediately, regardless of traffic conditions"
    - "The vehicle should switch to dead reckoning until GPS returns, with no effect on localization confidence"
  answer: 1
  explanation: "This modular architecture is the industry standard for autonomous vehicles (used by Waymo, Tesla, Cruise, Uber ATG) because it balances theoretical optimality (joint optimization would be ideal) against practical constraints (testability, modularity, real-time performance). It is the engineering choice that makes safety engineering feasible."
```

## Explainer

An autonomous vehicle is not a single algorithm but a complex distributed real-time system. The vehicle must perceive its surroundings, reason about what will happen next, decide on a course of action, execute that decision, and repeat this cycle at 10-100 Hz depending on the module. Each of these functions — perception, localization, prediction, planning, control — is a research and engineering field in its own right, and integrating them into a unified, safe system is the core challenge of autonomous driving.

**Perception** converts raw sensor data (images from cameras, point clouds from lidar, range measurements from radar) into high-level scene understanding: what objects are present? Where are they? What are they doing? Modern perception uses deep learning to detect vehicles, pedestrians, cyclists, traffic signs, lane markings, and other relevant features. The output is typically a list of detected objects with estimated position, velocity, and confidence scores. Perception is hard in the real world: objects are partially occluded, lighting changes with weather and time of day, sensors fail or degrade in adverse conditions. Perception systems must quantify uncertainty — a 95% confident detection of a pedestrian should be weighted differently than a 70% confident one.

**Localization** solves the problem "where are we?" by fusing multiple position sensors. GPS provides absolute position but drifts and fails in urban canyons; IMU measures acceleration and rotation but drifts unboundedly over time; wheel odometry measures distance traveled but accumulates small errors. Localization algorithms (typically particle filters or extended Kalman filters) fuse these signals, producing an estimate of the vehicle's position and orientation with an explicit uncertainty bound. If GPS is lost, localization continues but uncertainty grows. When uncertainty exceeds safety thresholds, the system must degrade gracefully.

**Prediction** answers the question "what will other agents do?" Given the current state of nearby vehicles and pedestrians, the prediction module forecasts their trajectories over the next few seconds. This is inherently uncertain — a pedestrian at the edge of the road might cross or might not. Prediction uses historical behavior (physics-based extrapolation), learned models trained on human driving data, and sometimes interaction-aware models that reason about how other agents will respond to the autonomous vehicle's actions. Good prediction is crucial: the planning module needs accurate predictions to find safe paths.

**Planning** computes a feasible trajectory (path and speed) for the autonomous vehicle that achieves the driving goal (reach destination, change lanes, stop at traffic light) while avoiding collisions. Planning algorithms range from simple (path following with obstacle avoidance) to sophisticated (optimization-based trajectory generation that reasons about multiple potential futures and chooses actions that are robust to prediction errors). Planning must respect vehicle dynamics (the car cannot turn instantaneously), traffic rules (obey traffic signs), and safety constraints (no collision with any predicted obstacle position over all predictions' uncertainty ranges).

**Control** executes the planned trajectory by commanding the vehicle's low-level actuators: steering angle, throttle, brake pressure. Control must account for vehicle dynamics (tire slip, delay between command and response, varying road friction) and environmental factors (road grade, road surface). A simple approach is PI(D) control tracking the planned path and speed. More sophisticated approaches use model predictive control to anticipate future trajectory changes and adjust commands proactively.

These five modules form a pipeline: perception detects objects, localization estimates position, prediction forecasts object motion, planning uses these to compute a safe trajectory, and control executes it. However, the pipeline is not purely feedforward; control feedback (did we actually achieve the planned trajectory?) feeds back to localization and planning. Additionally, when any module detects unexpected conditions — perception confidence drops, localization uncertainty grows, prediction shows high ambiguity — the system must handle graceful degradation: reduce speed, request human intervention, or transition to a safe state.

The strength of this modular architecture is testability: each module can be developed, validated, and debugged independently. The weakness is that errors in one module (a missed detection by perception, for example) propagate through the pipeline and can induce failures downstream. This is why perception and localization must quantify uncertainty and pass it forward, so that planning and control can account for it and refuse to execute plans that depend on low-confidence information.

