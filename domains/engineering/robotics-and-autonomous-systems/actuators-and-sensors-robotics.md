---
id: actuators-and-sensors-robotics
title: Actuators and Sensors in Robotics
domain: engineering
course: robotics-and-autonomous-systems
prerequisites:
- id: pid-control-robotics
  type: soft
- id: dynamics-robot-manipulators
  type: soft
builds-toward:
- robot-vision-fundamentals
- lidar-and-point-clouds
tags:
- actuators
- motors
- sensors
- encoders
- force-torque
- joint-feedback
- actuation
stage: advanced
status: validated
---

# Actuators and Sensors in Robotics

## Core Idea
Robots require actuators to move (electric motors, hydraulic cylinders, pneumatic actuators) and sensors to perceive their state (encoders for joint angles, force-torque sensors for contact forces, IMUs for acceleration). Actuator choice determines speed, force, precision, and energy consumption. Sensor noise and bandwidth limit the feedback quality in control loops. Understanding actuator dynamics (motor lag, saturation limits) and sensor characteristics (noise, drift, latency) is essential for realistic controller design. Common configurations: brushless DC motors with gearboxes and encoders for industrial arms, hydraulic servos for heavy loads, stepper motors for precise positioning.

## How It's Best Learned
Examine a real robot arm and identify its actuators and sensors. Measure the stall torque and no-load speed of a brushless DC motor and verify the motor constant (torque per ampere). Build a simple DC motor controller and measure encoder readings as the motor spins—observe quantization and noise. For force-torque sensing, learn the principles of strain gauges (Wheatstone bridge) and how six-axis F/T sensors are calibrated. Understand motor gearbox ratios and how they trade speed for torque.

## Common Misconceptions
- Higher actuator speed always allows faster robot motion; without adequate gearing, high-speed motors cannot produce the required torque for load manipulation.
- Sensors are perfect measurements; all real sensors have noise, bias, and latency that must be accounted for in control.
- Encoder noise is random and averaging helps; in reality, quantization noise from low-resolution encoders is deterministic and can cause control limit cycling.
- Force-torque sensors are always accurate if well-calibrated; temperature drift, thermal effects, and load-dependent stiffness cause systematic errors.

## Questions

```yaml
- question: "A brushless DC motor has a motor constant K_t = 0.1 N·m/A and is geared with a 100:1 gearbox (output torque = 100 × motor torque). If the motor can deliver a peak current of 10 A, what is the maximum torque at the gearbox output?"
  type: multiple-choice
  options:
    - "1 N·m (motor torque only)"
    - "10 N·m (motor torque with current)"
    - "100 N·m (motor torque with gearbox)"
    - "1000 N·m (motor torque with gearbox and current)"
  answer: 3
  explanation: "Quantization in feedback systems is particularly problematic for PID control because the integral term can accumulate error and build up commands that oscillate at the quantization frequency. This is why encoder selection is important for precision robot control: a coarse encoder (256 CPR) may oscillate noticeably, while a fine encoder (16,000+ CPR) effectively eliminates quantization issues within the control bandwidth."

- question: "A servo hydraulic actuator used for a high-load robotic manipulator has response time of 50 ms (the time from command input to 90% of peak output). When computing a feedforward controller that predicts the required command for a desired trajectory, this actuator lag must be accounted for. True or false?"
  type: true-false
  answer: true
  explanation: "This trade-off is fundamental. You cannot have both high speed and high torque from a small motor. Robots exploit this by using high-ratio gearboxes to compress the motor's power into low-speed, high-torque outputs suitable for manipulation. Without gearboxes, robot joints would need enormous motors to produce adequate torque, making robots heavy, expensive, and inefficient."
```

## Explainer

A robot is a mechanical system powered by actuators and controlled by sensors. The actuator converts electrical or hydraulic energy into motion; the sensor measures the resulting state. The closed-loop controller uses sensor readings to adjust the actuator commands, maintaining desired behavior despite disturbances. Understanding both sides is critical for robust robot design.

**Actuators** for robots fall into three categories: **electric motors** (brushless DC, stepper, synchronous), **hydraulic cylinders and servos**, and **pneumatic cylinders**. Electric motors are the most common for industrial arms: brushless DC motors are efficient, controllable, and have no mechanical commutation noise. They are controlled by electronic drive circuits that regulate current, producing proportional torque. The motor constant K_t (torque per ampere) and back-EMF constant K_e (voltage per angular velocity) characterize the motor. For a given desired output torque and speed, you choose the motor size and add a gearbox to trade speed for torque. A high-ratio gearbox (50:1, 100:1) produces high joint torques with a small motor, but at the cost of lower joint speed. The gearbox also introduces **backlash** (play between gear teeth), which limits control precision. High-precision robots use harmonic drives or strain-wave gears, which have very low backlash and compact design, at higher cost.

**Sensors** provide feedback to the controller. The most critical sensor is the **joint angle sensor**. **Incremental encoders** count pulses as a shaft rotates, providing relative position; they require a homing procedure to establish absolute reference. **Absolute encoders** (multi-turn, CANopen, SSI) directly output absolute position, eliminating the need for homing. Encoder resolution (counts per revolution) determines measurement granularity: a coarse 256-CPR encoder provides 1.4° resolution; a fine 16,000-CPR encoder provides 0.022° resolution. Higher resolution enables finer control but requires faster microcontroller sampling.

**Force-torque sensors** (F/T sensors) measure contact forces and torques between the robot and the environment. They are based on strain gauges: small resistive elements that change value when stressed. A **Wheatstone bridge** amplifies strain-induced resistance changes into measurable voltage. Six strain gauges arranged in a load cell structure measure all six components (F_x, F_y, F_z, T_x, T_y, T_z). F/T sensors require careful **calibration**: a transformation matrix maps raw gauge voltages to forces, accounting for thermal effects, cross-coupling (one axis affecting another), and the sensor's own weight. Thermal drift over hours of operation can introduce systematic errors of a few percent.

**Accelerometers** and **inertial measurement units (IMUs)** measure acceleration and rotation rates. These are useful for fall detection, impact sensing, or open-loop motion estimation when encoders are unavailable (e.g., for a free-falling object). IMUs suffer from drift: integrating acceleration twice to get position accumulates errors that grow over time.

In practice, a robot joint has multiple sensors: an encoder for position feedback (primary control), an F/T sensor for contact sensing (force control, safety), possibly a current sensor for motor current monitoring (fault detection). Each sensor has **noise and latency**: an encoder at 100 Hz updates may have 10 ms latency; an F/T sensor may have ±1-2% noise. The controller must account for these limitations. Aggressive feedback gains (to improve tracking) amplify measurement noise; conversely, conservative gains reduce noise but slow response. The design process balances these competing objectives.

**Actuator saturation** and **rate limits** are also critical. A motor has a maximum torque (stall torque) and maximum speed (no-load speed). In control, commands must respect these limits; violating them causes the actuator to saturate and the controller to lose authority. Advanced controllers use **anti-windup** logic (stopping integrator action during saturation) to prevent this problem. The combination of accurate sensors, powerful actuators, and intelligent control enables robots to perform precise, safe, and efficient tasks.
