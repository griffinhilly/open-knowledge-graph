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
  explanation: "Motor torque τ = K_t × I = 0.1 × 10 = 1 N·m. With a 100:1 gearbox, output torque = 100 × 1 = 100 N·m. The full calculation: τ_out = gearbox_ratio × K_t × I = 100 × 0.1 × 10 = 100 N·m. Wait, let me recalculate: 100 × 1 = 100 N·m, so the answer is 100. But if the question is asking for 1000 N·m as the maximum achievable, that would require a different setup. Let me verify the correct answer is 100 N·m, which corresponds to option (c)."
  answer: 2
  explanation: "Motor torque τ_motor = K_t × I = 0.1 N·m/A × 10 A = 1 N·m. Gearbox output torque = 100 × 1 = 100 N·m. This is the maximum torque available at the joint."

- question: "An incremental rotary encoder mounted on a robot joint has 1024 counts per revolution (CPR). If the joint rotates at 10 revolutions per second, what is the encoder update frequency (counts per second)?"
  type: multiple-choice
  options:
    - "1024 Hz"
    - "10 Hz (rotations per second)"
    - "10,240 Hz"
    - "1024 CPM (counts per minute)"
  answer: 2
  explanation: "Encoder output rate = CPR × rotations per second = 1024 counts/rev × 10 rev/s = 10,240 counts/s = 10,240 Hz. This is the raw quadrature pulse rate. When decoded by a microcontroller, this represents the joint angular velocity."

- question: "A six-axis force-torque (F/T) sensor mounted at a robot's wrist measures the contact forces and moments applied by the environment. Why is calibration of the F/T sensor critical?"
  type: multiple-choice
  options:
    - "To correct for the gravitational force due to the sensor's own weight, which biases the measurements"
    - "To establish the relationship between raw sensor outputs (strain gauge voltages) and forces/torques, accounting for sensor cross-coupling and sensitivity variation"
    - "To ensure the sensor is mounted perfectly vertically"
    - "To eliminate measurement noise, which cannot be calibrated away"
  answer: 1
  explanation: "F/T sensors use strain gauges to measure deformation in a load cell structure. Different gauges respond to different force/torque components, but coupling exists: a force in one direction produces small signals in other channels. Calibration establishes a 6×6 transformation matrix that maps raw gauge voltages to true forces and torques. Additionally, the sensor's own weight (gravity) biases the measurements and must be subtracted. Calibration is a one-time procedure (performed before deployment) that gives accurate readings throughout the sensor's operational life, assuming it is not physically damaged."

- question: "In a robot joint controlled with an incremental encoder and PID control, position measurement has quantization error: the encoder can only report discrete positions separated by 360°/1024 ≈ 0.35°. This quantization error causes control oscillations (limit cycling) around the setpoint. Why does this occur, and how can it be mitigated?"
  type: short-answer
  answer: "Quantization error creates a sawtooth-like measurement signal: as the joint rotates smoothly, the encoder output steps between discrete counts. The PID controller sees the error alternating between +(0.35°/2) and -(0.35°/2) in a pattern, causing the control signal to oscillate. This limit cycling is deterministic, not random noise. Mitigation: (1) increase encoder resolution (more counts per revolution), (2) apply low-pass filtering to the measured position (though this adds lag), or (3) use a higher-resolution sensor like an absolute encoder or analog position potentiometer. For critical applications, dual-encoder or multi-turn encoders can reduce quantization relative to useful signal bandwidth."
  explanation: "Quantization in feedback systems is particularly problematic for PID control because the integral term can accumulate error and build up commands that oscillate at the quantization frequency. This is why encoder selection is important for precision robot control: a coarse encoder (256 CPR) may oscillate noticeably, while a fine encoder (16,000+ CPR) effectively eliminates quantization issues within the control bandwidth."

- question: "A servo hydraulic actuator used for a high-load robotic manipulator has response time of 50 ms (the time from command input to 90% of peak output). When computing a feedforward controller that predicts the required command for a desired trajectory, this actuator lag must be accounted for. True or false?"
  type: true-false
  answer: true
  explanation: "Correct. A 50 ms lag is significant relative to typical robot control loop rates (10-100 Hz). If you command a torque at time t, the actuator doesn't produce it until t + 50 ms. During this delay, the actual robot motion lags the desired trajectory. A model-based controller that accounts for this delay can precompute the command at time (t - 50 ms) to arrive at the actuator at the right time, improving tracking accuracy. Ignoring actuator lag results in systematic tracking error and potentially instability if the lag is comparable to the control loop period."

- question: "Explain the trade-off between motor speed and motor torque when using a gearbox for robot joint actuation."
  type: short-answer
  answer: "A gearbox trades speed for torque. A 100:1 gearbox reduces the motor shaft speed by 100 but multiplies the output torque by 100. For a given motor size, the output power (τ·ω) is conserved (minus friction losses). A high-speed, low-torque motor becomes a low-speed, high-torque joint. For robot arms, gearboxes are essential: they reduce the required motor size and power while providing the high torque needed for load manipulation. The trade-off is that gearboxes introduce backlash (play in the gears) and friction, which degrade control precision unless carefully designed. Modern robots use planetary gearboxes (compact, low-backlash) or harmonic drives (very low-backlash, high-ratio) to minimize these issues."
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
