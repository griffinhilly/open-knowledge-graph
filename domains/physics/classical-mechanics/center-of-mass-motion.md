---
id: center-of-mass-motion
title: Center of Mass Motion
domain: physics
course: classical-mechanics
prerequisites: []
builds-toward:
- reduced-mass-problem
- angular-momentum-of-rigid-body
tags:
- center-of-mass
- dynamics
- systems
- conservation
stage: formal-systems
status: draft
---

# Center of Mass Motion

## Core Idea
The center of mass (CM) of a system moves as if all mass were concentrated there with external forces applied there: M·a_CM = F_external. Internal forces do not affect CM motion, only the motion of individual parts relative to the CM. This theorem greatly simplifies multi-body problems by separating overall motion (CM trajectory) from internal dynamics (orbits about the CM).

## Questions

```yaml
- question: "A firework shell explodes at the peak of its arc. Ignoring air resistance, what happens to the trajectory of the center of mass after the explosion?"
  type: multiple-choice
  options:
    - "The CM stops because internal forces from the explosion act in all directions"
    - "The CM continues on the same parabolic arc as before the explosion"
    - "The CM accelerates downward faster due to the increase in total downward momentum"
    - "The CM follows a new trajectory determined by the direction of the largest fragment"
  answer: 1
  explanation: "The CM theorem states M·a_CM = F_net,external. The explosion's forces are internal — every action has an equal and opposite reaction, so they sum to zero. Only gravity (an external force) acts on the system of fragments, giving a_CM = g downward. The CM continues the same parabola it was already on, completely unaffected by the internal explosion."

- question: "An astronaut floating in empty space pushes off a heavy wrench, sending it flying backward. What happens to the astronaut?"
  type: multiple-choice
  options:
    - "She stays still because she exerted an internal force on a system object"
    - "She moves forward, as the system CM stays fixed while wrench and astronaut move apart"
    - "She stays still because the CM of the astronaut-wrench system doesn't move"
    - "She moves forward, and the system CM also shifts toward her new position"
  answer: 1
  explanation: "With no external forces, the system CM stays fixed. The astronaut and wrench must move in opposite directions to keep the CM stationary. As the wrench moves backward, the astronaut moves forward — total momentum remains zero. Option C confuses 'CM stays fixed' with 'everything stays fixed'; the CM is fixed, but individual parts move in opposite directions around it."

- question: "Internal forces within a system can move the system's center of mass if they are large enough."
  type: true-false
  answer: false
  explanation: "False. By Newton's third law, every internal force has an equal and opposite internal reaction. When summed over the entire system, internal forces always cancel exactly, contributing zero to the net force and therefore zero to the CM acceleration. No matter how large the internal forces (an explosion, a spring releasing, colliding parts), the CM motion is determined solely by external forces."

- question: "Separating CM motion from relative motion simplifies multi-body problems because the two motions are governed by different forces."
  type: true-false
  answer: true
  explanation: "True. The CM motion obeys M·a_CM = F_external — only external forces matter. The relative motion of parts about the CM is governed by internal forces. These two analyses are completely independent. For a binary star with no external forces, the CM travels in a straight line while each star follows an elliptical orbit around the CM. You solve each piece separately with the appropriate tools."

- question: "Why can't an isolated astronaut floating in space propel herself in any direction by moving her body (waving arms, kicking legs)? What would she need to do to actually change her position?"
  type: short-answer
  answer: "With no external forces, the astronaut-system CM is fixed. Any movement of her arms pushes her body in the opposite direction — the CM doesn't translate. She can rearrange her body around the CM but cannot move the CM itself. To change her position, she must interact with an external agent: throw an object away from herself (the reaction force pushes her in the opposite direction) or use a thruster that expels mass."
  explanation: "This follows directly from M·a_CM = F_external with F_external = 0. Internal rearrangements cannot translate the CM. She can change her orientation through internal torques, but translational motion requires ejecting mass or pushing off something external — creating an external reaction force that moves the CM."
```

## Explainer

Imagine a firework exploding in the sky. After the explosion, hundreds of fragments fly outward, spinning and tumbling in all directions. The internal forces of the explosion are enormous — far larger than gravity during the brief detonation. Yet if you track the **center of mass** of all the fragments together, weighting each fragment's position by its mass, that single point traces the same smooth parabolic arc the intact firework would have followed. It ignores the explosion entirely. This is the center of mass theorem: the explosion's internal forces come in equal-and-opposite pairs that cancel out, leaving only gravity — the external force — to govern how the CM moves.

The formal statement is compact: M·**a**_CM = **F**_net,external, where M is the total mass of the system and **F**_net,external is the vector sum of all forces exerted by agents outside the system. This is Newton's second law applied to an imaginary point particle carrying the total mass at the CM location. For the firework, only gravity acts from outside: **F**_ext = M**g** downward, so **a**_CM = **g** downward — a parabola, regardless of how chaotically the fragments fly. Every internal force one fragment exerts on another has an equal-and-opposite reaction (Newton's third law), so internal forces sum to zero and vanish from the CM equation entirely.

The practical power of this theorem is **decomposition**: any multi-body problem splits cleanly into two independent pieces. First, solve the CM motion using only external forces — this is a single-particle problem. Second, analyze the motion of parts relative to the CM — this is governed by internal forces and is independent of external ones. For a binary star system with no external forces, the CM moves in a straight line at constant velocity forever; each star orbits the CM in an ellipse. The two analyses decouple completely, letting you solve each piece with the tools appropriate to it.

The CM theorem and **conservation of momentum** are the same principle from two perspectives. If net external force is zero, M·**a**_CM = 0, so **v**_CM is constant — the total momentum **p** = M**v**_CM is conserved. This is why an isolated system's CM cannot accelerate without external influence: no amount of internal rearrangement can move the CM. An astronaut floating in space cannot propel herself forward by waving her arms — her CM stays fixed. But she can throw a wrench backward, making her CM remain fixed while she and the wrench move in opposite directions to keep **p** = 0. Grasping the CM as the "translation handle" of any system, and understanding that only external forces move it, is one of the most powerful simplifying principles in all of classical mechanics.
