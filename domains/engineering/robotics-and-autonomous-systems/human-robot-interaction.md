---
id: human-robot-interaction
title: Human-Robot Interaction and Collaborative Robots
domain: engineering
course: robotics-and-autonomous-systems
prerequisites:
- id: behavior-based-robotics
  type: soft
builds-toward: []
tags:
- human-robot-collaboration
- safety
- force-control
- user-interface
- human-factors
stage: advanced
status: validated
---

# Human-Robot Interaction and Collaborative Robots

## Core Idea
Collaborative robots (cobots) work alongside humans in shared workspaces, requiring fundamentally different safety, control, and interface design than traditional industrial robots that are isolated behind fences. Safety in HRI is ensured through force/torque limits (robots stop if forces exceed thresholds to prevent injury), compliant motion control (forces are bounded), quick emergency stop systems, and speed/power limits. Beyond safety, effective HRI requires intuitive interfaces (demonstrative learning, gesture recognition, natural language commands), understanding human intent (learning from human corrections), and predicting human actions to avoid collisions. HRI is an interdisciplinary field spanning robotics, ergonomics, cognitive science, and HCI. Applications include manufacturing (assembly, inspection), healthcare (surgery assistance, rehabilitation), and domestic service (care robots, household assistants). The challenge is building robots that are safe, predictable, and easy for non-experts to operate and supervise.

## Questions

```yaml
- question: "A collaborative robot arm works alongside a human assembling electronics. To prevent injury if the robot hits the human, the designers implement a force limit: if the robot applies force > F_max = 80 N to any contact, motors instantly cut power. Is this sufficient for safe human-robot collaboration?"
  type: multiple-choice
  options:
    - "Yes, 80 N is enough to stop the robot before significant injury"
    - "No, because the robot has momentum and cutting power doesn't stop it instantly; it will coast and apply additional force before decelerating"
    - "Yes, if the force limit is combined with slow speeds (< 0.5 m/s)"
    - "No, because 80 N is arbitrary and different body parts have different injury thresholds"
  answer: 1
  explanation: "Force limiting alone is insufficient. A robot arm with mass and velocity has momentum. When power is cut, it continues moving and applying force for several milliseconds while decelerating due to friction and damping. Total force applied = F_contact + F_momentum. For 1 kg arm moving at 1 m/s, momentum p = 1 kg⋅m/s, and if contact time is 10 ms, the momentum applies ~100 N additional force. Total injury potential is higher than static force limits suggest. Effective safety combines force limits (stop when forces get too high) with speed limits (reduce momentum available) and soft materials (spread force over larger contact area, reducing peak pressure). These combined measures prevent serious injury. Pure force limiting without speed/momentum control is dangerously incomplete."

- question: "A cobot learns to perform assembly tasks from human demonstration. The human shows the robot how to insert a part by guiding the robot's end-effector through the insertion. The robot records these motions and learns a policy that reproduces similar motions. However, the robot rigidly follows the recorded path, ignoring variations in part placement (parts arrive at slightly different heights). Why is this problematic and what control strategy would improve generalization?"
  type: multiple-choice
  options:
    - "The robot should learn multiple paths and choose randomly between them"
    - "The robot should use impedance control: instead of strictly following position, allow forces to apply and adjust position based on contact. If the part resists insertion, forces feedback, and the robot adapts (compliance) rather than pushing harder"
    - "The robot should use vision feedback to detect part position and replan"
    - "The problem is with imitation learning; the robot should use only classical motion planning"
  answer: 1
  explanation: "Stiff position control (teach-playback) is brittle — it works only if conditions exactly match the demonstration. Impedance control (also called compliance or force control) treats the robot as a virtual spring: the robot has a desired position (from the learned task) but applies force proportional to position error: F = K(x_desired - x_actual). If the part is lower than expected, the robot's end-effector contacts it sooner, creating feedback force that modulates motion. The robot naturally adapts to variations while still pursuing the learned task. This is why assembly robots use impedance control — it makes the robot reactive and forgiving of variation, mimicking human compliance (when a human inserts a part and feels resistance, they adapt, not rigidly push)."

- question: "A robot is trained to predict human gaze direction to anticipate what the human will touch next, enabling the robot to move out of the way or prepare to assist. This prediction reduces collision risk and improves task coordination. However, predicting human intent from limited cues (gaze alone) is unreliable. What is the design consequence?"
  type: multiple-choice
  options:
    - "The robot should not attempt intent prediction; it's too risky"
    - "The robot should predict intent but be conservative: if unsure, assume the human will reach toward the robot, and move away proactively"
    - "The robot should predict intent and trust the prediction; false positives are acceptable"
    - "Intent prediction is impossible and should be replaced with communication-based coordination"
  answer: 1
  explanation: "Intent prediction is valuable but imperfect. Conservative design (false-positive bias) is safer: if prediction is uncertain about human intent, assume the worst (human moving toward robot) and move away. This avoids collisions at the cost of over-reactivity (unnecessary moves). Trusting predictions blindly is risky — false negatives (failing to predict a collision) can cause injury. In safety-critical HRI, conservative bias is standard: when unsure, prioritize safety over efficiency. This is similar to defensive driving — assume the worst and you're rarely surprised."

- question: "In human-robot collaboration, what trade-off exists between robot speed and safety, and how do standards like ISO/TS 15066 address this?"
  type: true-false
  answer: true
  explanation: "Correct. Faster robots are more efficient but carry more energy and momentum, creating injury risk if collisions occur. ISO/TS 15066 specifies power and force limits based on robot velocity and contact area. Lower-speed collaborative zones allow higher forces because momentum is lower. Barrier-free collaborative robots (working in the same space without guards) must operate slowly enough that impact force is within safe limits. This couples velocity directly to safety limits. Designers choose operating speed based on the required throughput and acceptable safety margin."

- question: "Explain the key safety requirements for collaborative robots and why traditional industrial robot safety standards (fenced areas, interlocks) are insufficient for collaborative workspaces."
  type: short-answer
  answer: "Traditional industrial robots are caged because they are stiff, fast, and heavy — collisions cause serious injury. Cobots need to share workspaces with humans, so physical barriers are not feasible. Safety is achieved through: (1) Force/torque limiting — bounded interaction forces prevent injury, (2) Speed limiting in collaborative zones — reduces momentum and impact energy, (3) Soft materials — distribute contact force over larger area, reducing peak pressure, (4) Compliant control (impedance, force-control) — robots yield to contact rather than pushing harder, (5) Monitoring and stops — detect collisions and stop rapidly, (6) Design for safety — accessible emergency stops, clear operational modes. Traditional standards assume the robot cannot reach humans (fence + interlocks); collaborative standards assume contact can occur and design the robot's interaction forces to be safe (ISO/TS 15066: max 220 N force on human hand, max 140 W power). This requires active control and mechanical design, not just barriers."
  explanation: "This shift from physical separation to force-limited interaction is why collaborative robots are a distinct category. Traditional industrial arms can be 500 N impact forces; cobots are designed to be <220 N. This changes hardware (lighter, compliant designs), software (force control loops, compliance), and operational procedures (speed limits, no hard tools). The safety model is fundamentally different — prevention of injury through controlled interaction, not prevention of contact through physical barriers."
```

## Explainer

For decades, industrial robots operated in cages, separated from human workers by fences and interlocks. Robots were fast, powerful, and dangerous — a collision could break bones or cause crush injuries. Humans entered only when the robot was safely parked and locked. But this model doesn't scale to factories with space constraints, flexible manufacturing, and tasks requiring human judgment and dexterity alongside robotic precision. Collaborative robots (cobots) promise to change this: robots working alongside humans, sharing workspaces, and collaborating on tasks.

**Safety as a Core Design Principle:** Collaborative robots cannot achieve safety through physical separation — the whole point is shared workspaces. Safety must be built into the robot's interaction with humans. ISO/TS 15066 and related standards specify maximum force and power limits for different types of contact. For a collision with the robot's arm: max 220 N. For sustained contact with the hand: max 140 W power. These limits are determined from biomechanics studies of human injury thresholds. Exceeding them can cause bruising, fractures, or severe trauma. Cobots are designed mechanically and controlled to respect these limits.

**Mechanical Compliance:** Cobots use lighter materials, smaller actuators, and flexible joints compared to traditional industrial robots. Some designs include series elastic actuators (SEA): a spring between the motor and the end-effector allows force measurement and compliance. Others use purely software compliance via impedance control. The goal is that a cobot "feels soft" when touched — it yields, not rigidly resists.

**Control Strategies for Safety:** Force-limiting control is central. The robot monitors forces and torques at the end-effector and joints. If forces exceed safe limits, power is cut or reduced immediately. The reaction is fast (millisecond-scale) but not instantaneous — momentum carries the robot forward briefly. To prevent injury, safe cobots also limit speed in collaborative zones. A robot moving at 0.2 m/s has much less momentum than one moving at 2 m/s; limiting speed reduces injury risk. Modern cobots often operate in collaborative zones at 0.25-0.5 m/s, much slower than traditional robots (1-2 m/s) but sufficient for many assembly tasks.

**Impedance Control for Collaboration:** Cobots often use impedance control: the robot behaves like a virtual spring with controlled stiffness. The robot has a desired trajectory (from a learned task or programmed path), but if forces develop (e.g., a human pushes the robot's arm), the robot yields according to compliance laws. This makes the cobot "feel" responsive to human interaction — if a human guides the cobot's arm, it follows naturally. If a part resists insertion, the robot's force feedback causes it to adjust position or reduce pushing force. Impedance control is why cobots are sometimes called compliant — they don't rigidly push through resistance; they adapt.

**Intent Prediction and Situation Awareness:** Cobots can improve safety and efficiency by predicting human intent. If the robot knows the human will reach toward location A, it can move out of the way or prepare to assist. Intent prediction uses human gaze direction, hand position, activity recognition (what task is being performed), and learned patterns of human behavior. However, predictions are imperfect. Conservative safety design responds to prediction uncertainty by assuming the worst: if the robot doesn't confidently predict the human's action, it assumes the human might reach toward the robot and moves away. This causes over-reactivity but prevents collisions.

**Design Principles for HRI Safety:**
1. **Accessibility of emergency stops**: Red buttons, clearly visible, reachable from any position
2. **Operational modes**: Clear distinction between teach/demo mode (robot moves slowly) and run mode (faster but still limited), with mode indication
3. **Predictability**: Robots move in anticipated directions, accelerate/decelerate smoothly (no jerky motion)
4. **Communication**: LED indicators show robot status; sounds signal robot motion
5. **Speed limits**: Velocity capped in collaborative zones; faster speeds only in human-free areas
6. **Force limits**: Active monitoring and control ensure interaction forces stay safe

**Applications and Limitations:** Cobots excel at assembly, inspection, loading/unloading, and collaborative tasks. They're increasingly used in healthcare (surgery assistance where the cobot constrains motion to safe bounds) and manufacturing. But they're slower than traditional robots and less powerful, limiting applications requiring high speed or force. A car assembly line with multiple fast-moving tasks may be impractical for cobots. A small electronics assembly line with flexible routing and quality inspection is ideal.

**The Future:** As cobots become more dexterous and intelligent (better sensing, learning), collaborative applications will expand. Autonomous cobots that understand context (which part goes where, what the human needs next) and communicate (via gestures, AR, natural language) will blur the line between tool and teammate. But the safety-first design philosophy — force limits, compliance, predictability — will remain central.

