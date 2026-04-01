---
id: aerial-robotics-uav
title: Aerial Robotics and Unmanned Aerial Vehicles
domain: engineering
course: robotics-and-autonomous-systems
prerequisites:
- id: motion-planning-algorithms
  type: soft
builds-toward: []
tags:
- uav
- quadrotor
- aerial-robotics
- flight-control
- trajectory-planning
- autonomous-flight
stage: advanced
status: validated
---

# Aerial Robotics and Unmanned Aerial Vehicles

## Core Idea
Aerial robots (UAVs, drones) add an extra dimension (altitude) to motion planning and control, requiring active stabilization to counteract gravity, aerodynamic effects, and wind. Multirotor drones (quadrotors, hexacopters) are underactuated: they have 6 degrees of freedom (position x,y,z and orientation roll,pitch,yaw) but only 4 control inputs (individual rotor speeds), requiring coordinated control of multiple motors to achieve desired motions. The standard control architecture uses cascaded loops: inner attitude controller stabilizes roll and pitch (keeping the drone level), middle controller commands velocity and yaw, outer position controller generates velocity commands toward goals. Trajectory planning for aerial robots must account for actuation limits (maximum tilt angles, acceleration bounds) and aerodynamic constraints (hover power, forward speed limits). Applications include aerial photography, environmental monitoring, search-and-rescue, infrastructure inspection, and autonomous air mobility. Key challenges include weight constraints limiting onboard computing, power consumption limiting flight time to 15-45 minutes, GPS unavailability indoors, and collision avoidance in dynamic airspace.

## Questions

```yaml
- question: "A quadrotor drone has 4 rotors producing thrust T1, T2, T3, T4 (measured in Newtons). The drone has mass m. To hover, the sum of thrusts must equal weight: T1 + T2 + T3 + T4 = m*g. Now the drone needs to accelerate forward (positive x direction). Which rotor thrust configuration achieves this?"
  type: multiple-choice
  options:
    - "Increase all rotor thrusts equally to increase weight"
    - "Increase front rotors, decrease rear rotors. This tilts the drone forward, and the vertical component of net thrust still equals weight, but horizontal component pushes forward"
    - "Increase rear rotors, decrease front rotors to push backward"
    - "Increase front rotors only; rear rotors stay constant"
  answer: 1
  explanation: "Quadrotors achieve acceleration by tilting. Increasing front rotors (T1, T2) and decreasing rear rotors (T3, T4) tilts the drone forward. The motor torques create roll and pitch moment, tilting the fuselage. The total upward thrust is reduced if front rotors are increased and rear are decreased equally, causing the drone to fall. To maintain altitude while tilting, the controller adjusts all thrusts such that the vertical component of net thrust still equals weight (preventing descent) while the horizontal component (front thrust > rear thrust) accelerates forward. The control law is complex: translating desired acceleration to motor commands requires solving for thrust vector and rotating it to achieve desired tilt angles."

- question: "A quadrotor controller uses nested loops: innermost loop controls attitude (roll, pitch, yaw) at 200 Hz. Middle loop controls horizontal velocity. Outer loop controls position. Why is this hierarchical structure necessary?"
  type: multiple-choice
  options:
    - "Hierarchical loops are more efficient computationally"
    - "The attitude controller must be fast because the drone is unstable without active stabilization. Roll/pitch drift quickly if not corrected. Inner fast loops stabilize attitude; outer slow loops control higher-level motion"
    - "Quadrotors are inherently stable and don't need attitude control; hierarchical loops are optional"
    - "Hierarchical loops reduce the number of sensors needed"
  answer: 1
  explanation: "A quadrotor is inherently unstable in roll and pitch — without active control, it tips over. The attitude controller must run fast (200 Hz) to sense and correct tilt within milliseconds. Once attitude is stabilized, the drone can execute position or velocity commands. Cascaded control is a standard control systems technique: inner loops stabilize lower-level dynamics (attitude dynamics are fast, ~0.1-1 Hz natural frequency), outer loops command higher-level objectives (position control is slower). This separation is necessary because attitude dynamics are fast but unstable, while position dynamics are slower and naturally stable (once tilted, the drone accelerates until tilting back reduces acceleration)."

- question: "A drone flying indoors cannot rely on GPS (signals are too weak). It uses onboard camera + optical flow (measuring movement of visual features between frames) to estimate velocity. However, optical flow can fail (featureless white walls, poor lighting). How should the control system handle optical flow dropout?"
  type: multiple-choice
  options:
    - "Switch to dead reckoning using accelerometers and gyroscopes; no sensor fusion needed"
    - "Fuse optical flow with inertial measurement (accelerometer, gyroscope) via Kalman filter. When optical flow drops out, IMU estimates continue velocity/position (with growing error) until optical flow recovers"
    - "Stop the drone and wait for optical flow to recover"
    - "Use only GPS and ignore optical flow entirely"
  answer: 1
  explanation: "Sensor fusion (Kalman filtering) is standard in drone control. Optical flow is accurate when features are visible but sparse or noisy in poor lighting. IMU accelerometers are noisy and prone to drift without external reference. A Kalman filter combines both: optical flow constrains drift, IMU fills gaps when optical flow is unavailable. When optical flow drops (white wall), the filter relies on IMU estimates and integrates acceleration to maintain position estimate (with growing uncertainty). When features reappear, optical flow re-constrains the estimate, correcting accumulated drift. Dead reckoning (IMU alone) works briefly (seconds) but accumulates error quickly; sensor fusion extends the window of usefulness."

- question: "A quadrotor must carry a camera payload that adds weight but not additional rotor thrust capacity. Which aspect of drone performance is most negatively impacted?"
  type: multiple-choice
  options:
    - "Maximum horizontal speed"
    - "Maximum altitude (absolute ceiling slightly increases)"
    - "Hover time (battery depletes faster at same thrust-to-weight ratio)"
    - "Attitude stabilization quality"
  answer: 2
  explanation: "Adding mass with fixed rotor thrust reduces the thrust-to-weight ratio (T/m). At hover, the drone must produce thrust T = m*g. With larger m, the rotors must operate at higher percentage of maximum thrust, leaving less margin for maneuvers and control authority. More critically, the power required to hover is P = T*v = m*g*v_hover (where v_hover is the induced velocity through the rotors). Heavier drones require more power to hover, draining the battery faster. Hover time is proportional to T/m — it directly decreases. Absolute ceiling (where T_max = m*g*cos(tilt)) actually improves slightly because the drone tips more to accelerate, but practically, you lose hover time (can't stay aloft as long) and responsiveness."

- question: "Describe the control architecture for a quadrotor UAV, explaining why attitude control is the innermost (fastest) loop and how higher-level controllers (position, trajectory planning) interact with it."
  type: short-answer
  answer: "Quadrotor control uses cascaded (hierarchical) loops: Innermost (200 Hz): Attitude controller stabilizes roll, pitch, yaw using gyroscope feedback. This is the fastest loop because attitude is unstable without control; the drone tips if this loop fails. The controller computes motor thrust commands to produce desired roll/pitch angles. Middle (20-50 Hz): Velocity controller commands desired horizontal velocity and vertical acceleration. It generates desired roll/pitch angles for the attitude controller. Outer (5-20 Hz): Position/trajectory controller commands desired position or follows a trajectory. It generates velocity commands for the velocity controller. This cascade works because attitude control is much faster than velocity control, which is faster than position control. At each level, the controller assumes the lower level has achieved its setpoint (e.g., position controller assumes velocity commands are executed with no lag). This decoupling simplifies design. Trajectory planning occurs at the planning level and generates dynamically-feasible trajectories respecting actuator limits (max tilt angle, acceleration)."
  explanation: "This hierarchical structure is universal in aerial robotics. The separation of timescales (fast stabilization, slow positioning) is not just convenient but necessary. Without fast attitude control, the drone cannot maintain controlled flight. The cascaded approach decomposes the problem: stabilize the platform first (attitude), then execute maneuvers (velocity), then reach goals (position). It's analogous to balancing on a unicycle while riding to a destination — you must first stabilize your balance continuously, then route toward the target."
```

## Explainer

Aerial robots add a compelling dimension to robotics: flying through three-dimensional space without relying on fixed structures or ground contact. This opens applications (aerial photography, infrastructure inspection, environmental monitoring, search-and-rescue) impossible for ground robots. But aerial flight introduces challenges absent in ground robotics: active stabilization against gravity, aerodynamic effects, power consumption limits, and the continuous risk of crashes.

**Quadrotor Fundamentals:** The most common aerial platform is the quadrotor (or quadcopter): four motors arranged symmetrically with propellers that push air downward. Each rotor produces thrust proportional to the square of blade speed. The four rotor speeds are independently controllable, providing 4 control inputs. The drone has 6 degrees of freedom (position x,y,z and orientation roll,pitch,yaw), making it **underactuated** — fewer control inputs than DOF. This seemingly limiting, but it's a feature: the drone cannot independently control position and orientation; they're coupled through dynamics.

To move forward, the drone doesn't push with a forward thruster — it tilts forward and relies on gravity and upward thrust to accelerate. Tilting forward requires increasing front rotor speed and decreasing rear rotor speed. The resulting forces are: net upward thrust (supporting weight, less by tilting forward), net forward force (front high thrust minus rear low thrust), and roll moment (rolling the fuselage forward). Controlling a quadrotor requires carefully coordinating all four rotor speeds to achieve desired position and attitude.

**Cascaded Control Architecture:** Manually commanding rotor speeds would be overwhelming. Instead, control is hierarchical:

**Level 1 (Attitude Control, ~200 Hz):** The innermost loop stabilizes roll and pitch (keeping the drone level) using gyroscope feedback. If the drone tilts due to wind or perturbation, the controller commands increased thrust on the low side and decreased thrust on the high side to level it. Roll and pitch dynamics are relatively fast (~100 Hz) and unstable without control. This loop must run fast and responsively.

**Level 2 (Velocity Control, ~20-50 Hz):** Given desired velocity (vx, vy, vz), this controller generates desired roll and pitch angles and vertical acceleration, sending them to the attitude controller. If the drone should move forward at 2 m/s but is moving forward at 1 m/s, it commands a tilt angle that produces the required forward acceleration.

**Level 3 (Position/Trajectory Control, ~5-20 Hz):** Given a goal position or trajectory, this controller generates velocity commands. It measures current position (from sensors like GPS, optical flow, SLAM) and computes velocity commands that reduce position error.

The advantage of this hierarchy: each level operates at an appropriate timescale and abstracts complexity. The attitude controller doesn't worry about position; it focuses on stabilization. The position controller assumes velocity commands are executed (relying on the velocity and attitude controllers). This decomposition is necessary because attitude dynamics are unstable and fast; position dynamics are stable but slow. You can't control both independently — they must be coordinated.

**Power and Flight Time:** A quadrotor hovers by producing upward thrust equal to its weight. The power required is P = T*w = m*g*w, where w is the induced velocity through the rotor disk (related to disk loading). Heavier drones require more power; typical quadrotors can hover for 15-45 minutes on a battery. This is a severe constraint for many applications. Adding payload reduces hover time proportionally. Thrust-to-weight ratio (T/m) is critical: a typical drone has T/m ≈ 2-3, allowing fast acceleration and maneuvering. Heavily loaded drones have T/m ≈ 1, barely hovering, no maneuver margin. Wind is also problematic: a 10 m/s wind gust can push a lightweight drone meters off course. GPS-denied indoor flight requires onboard cameras and vision-based control (optical flow, SLAM) to estimate position without external signals.

**Trajectory Planning and Constraints:** Motion planning for aerial robots must account for underactuation. The drone cannot move purely vertically without tilting; it cannot tilt arbitrarily (max tilt angle ~45-60°); it cannot accelerate infinitely (motors saturate). Trajectory planning generates dynamically-feasible paths respecting these limits. A simple approach: compute position and velocity references at each time step such that desired acceleration doesn't require tilt exceeding limits. For aggressive maneuvers (racing drones), more sophisticated optimization (minimum-time trajectories subject to dynamics constraints) is used.

**Modern Applications and Advances:** Quadrotors are ubiquitous: consumer drones (DJI, Parrot), delivery drones (Amazon Prime Air, Wing), autonomous air taxis. Recent advances include: (1) Visual inertial odometry (VIO): fusing camera images with IMU to estimate position without GPS, enabling consistent autonomous flight indoors; (2) Obstacle avoidance: onboard lidar or stereo cameras detecting and avoiding obstacles in real-time; (3) Swarming: multiple drones coordinating via local communication and decentralized control; (4) Hybrid designs: combining fixed-wing (efficient forward flight) with multirotor (hover) capabilities. The challenge remains power: a commercial quadrotor's 30-minute flight time is too short for many applications (wind power inspection, agricultural spraying). Battery density hasn't improved proportionally to motor efficiency, so long-endurance flight is a bottleneck. Solar, tethered, and longer-range fixed-wing designs address this but trade maneuverability for endurance.

