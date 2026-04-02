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

