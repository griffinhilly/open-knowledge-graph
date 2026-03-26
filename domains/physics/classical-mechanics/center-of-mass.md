---
id: center-of-mass
title: Center of Mass
domain: physics
course: classical-mechanics
prerequisites:
- id: newtons-second-law
  type: hard
- id: vectors-in-two-dimensions
  type: soft
- id: definite-integral-definition
  type: soft
- id: applications-integrals-area-mass
  type: hard
- id: triple-integrals
  type: soft
builds-toward:
- conservation-of-momentum
- rotational-dynamics
- moment-of-inertia
tags:
- center-of-mass
- mass-distribution
- reference-point
stage: formal-systems
status: validated
---

# Center of Mass

## Core Idea
The center of mass (CM) of a system of particles is the mass-weighted average position: r_cm = (Σmᵢrᵢ)/(Σmᵢ). For continuous bodies, r_cm = (∫r dm)/M. Newton's second law for a system states that the net external force equals total mass times the acceleration of the CM: F_net = M·a_cm. Internal forces between parts of the system do not affect the CM motion, making the center of mass the natural reference point for dynamics.

## How It's Best Learned
Compute CM positions for simple discrete systems (two masses on a rod) and verify by balancing the rod at the computed point. Then extend to uniform 2D shapes using symmetry and integration.

## Common Misconceptions
- Thinking the CM must be located inside the object: for a ring or hollow shell, the CM lies at the geometric center where there is no material.
- Confusing the CM (weighted by mass) with the geometric centroid (weighted by volume) when density is nonuniform.

## Questions

```yaml
- question: "An astronaut floating in space throws a wrench from one hand to the other. Ignoring all external forces, what happens to the center of mass of the (astronaut + wrench) system?"
  type: multiple-choice
  options:
    - "It shifts toward the astronaut's body, since she is much heavier than the wrench"
    - "It remains stationary — internal forces between astronaut and wrench cannot change the CM's motion"
    - "It accelerates in the direction the wrench is thrown"
    - "It moves toward the point where the total momentum is zero"
  answer: 1
  explanation: "With no external forces, F_net = 0, so the CM acceleration is zero — the CM stays put (or moves at constant velocity if it was already moving). The throw is an internal interaction: the astronaut pushes the wrench, and the wrench pushes back equally on the astronaut. These internal forces cancel in pairs when summing across the whole system. The individual pieces (astronaut, wrench) each move, but the mass-weighted average position — the CM — does not change. This is a direct consequence of Newton's third law applied to the internal force pairs."

- question: "An artillery shell explodes into three fragments mid-flight. Ignoring air resistance after the explosion, what can you say about the center of mass of the three fragments?"
  type: multiple-choice
  options:
    - "The CM stops because kinetic energy is converted to heat and sound in the explosion"
    - "The CM follows a new trajectory determined by the largest fragment's momentum"
    - "The CM continues along the same parabolic trajectory the intact shell was following, because the explosion forces are internal to the system"
    - "The CM cannot be tracked after the explosion since the fragments are no longer a single rigid object"
  answer: 2
  explanation: "The explosion is an internal event — the forces driving the fragments apart are interactions between parts of the system, so they cancel when computing net external force. The only external force acting is gravity, which was already determining the parabolic trajectory of the intact shell. After the explosion, gravity acts on each fragment, and the net external force on the system is still just the total weight M·g downward. So F_net = M·a_cm is unchanged, and the CM parabola continues exactly as before. This is one of the most elegant applications of CM dynamics."

- question: "The center of mass of a solid object should usually be located at a point inside the object where there is physical material."
  type: true-false
  answer: false
  explanation: "For objects with holes or curved geometry, the CM can lie outside the physical material. The classic example is a ring: its CM is at the geometric center of the ring, where there is no material at all. Similarly, a hollow spherical shell has its CM at its center (empty space). The CM is a mathematical weighted average of mass distribution, not a physical point of the object. This matters for dynamics: a spinning ring rotates around its geometric center (the CM in free space), even though no part of the ring is actually there."

- question: "If the net external force on a system of particles is zero, the center of mass moves at constant velocity — which is equivalent to conservation of total momentum."
  type: true-false
  answer: true
  explanation: "F_net = M·a_cm, so if F_net = 0 then a_cm = 0, meaning the CM moves at constant velocity v_cm. Total momentum is p_total = M·v_cm, so constant v_cm means constant p_total. These are two ways of expressing the same physical fact: with no external forces, the total momentum of the system is conserved. This is why CM dynamics and momentum conservation are not separate principles — they are the same principle viewed from different angles."

- question: "Why do internal forces between parts of a system not affect the center of mass's acceleration, even when those internal forces are very large?"
  type: short-answer
  answer: "By Newton's third law, every internal force has an equal and opposite reaction within the system. If particle A exerts force F on particle B, then B exerts −F on A. When you sum all forces across all particles to find the net force on the system, every action-reaction pair cancels exactly. What remains is only the sum of external forces — forces exerted on the system by the outside world. So F_net(external) = M·a_cm, and the CM responds only to external influences, regardless of how large the internal forces are."
  explanation: "This is what makes the CM such a powerful simplification. A baseball's molecular bonds exert enormous forces on each other internally, yet none of that affects the CM trajectory. An exploding bomb has massive internal forces, yet the CM continues its original path. The CM 'ignores' all internal complexity and responds only to what the outside world does. This is why you can treat complex objects as point masses for translational dynamics."
```

## Explainer

The center of mass is the single most useful simplification in the mechanics of multi-part systems. When you have a complex object — a rigid body, a collection of particles, a system of interacting masses — you often don't need to track every individual part. From your prerequisite in **Newton's second law**, you know that F = ma for a single particle. The center-of-mass theorem extends this: **F_net = M · a_cm**, where F_net is the total *external* force, M is the total mass, and a_cm is the acceleration of the center of mass. Every internal force — the molecular bonds holding a baseball together, the mutual gravitational attraction between Earth and Moon — cancels out in pairs by Newton's third law. Only what the *outside* does to the system matters for CM motion.

To build intuition for the formula r_cm = (Σmᵢrᵢ)/M, think of it as a mass-weighted average — a tug-of-war where each particle pulls the average toward itself in proportion to its mass. Place a 1 kg mass at x = 0 and a 3 kg mass at x = 4 m: the CM sits at (1·0 + 3·4)/4 = 3 m, three-quarters of the way toward the heavier mass. The heavier particle dominates. For a continuous body, the integral r_cm = (∫r dm)/M does the same thing for infinitely many infinitesimal mass elements — your prerequisite in **integration for area and mass** gives you the tools to evaluate this directly by setting up dm = ρ dV and integrating over the body.

The most striking implication concerns trajectory independence from internal motion. Throw a wrench through the air: it tumbles and rotates, but its CM traces a perfect parabolic arc exactly as a single point-mass would. The tumbling is internal redistribution of mass; it does not appear in F_net = M · a_cm because the internal forces sum to zero. Similarly, if an artillery shell explodes mid-flight, the fragments scatter in all directions, but the CM of all the fragments continues along the same parabolic path the intact shell was on — because the explosion is internal. External forces alone (gravity, air resistance) change the CM trajectory.

The CM concept directly sets up everything that follows in this course. **Conservation of momentum** is just F_net = M · a_cm with F_net = 0: if no net external force acts, the CM moves at constant velocity, meaning the total momentum M · v_cm is conserved. When you move to **rotational dynamics** and **moment of inertia**, the CM becomes the natural reference point — an object rotating about its own CM has the simplest equations of motion, and the parallel-axis theorem lets you shift to any parallel axis. Mastering the CM now means you already understand the architecture of multi-body dynamics before you have learned any of its detailed techniques.
