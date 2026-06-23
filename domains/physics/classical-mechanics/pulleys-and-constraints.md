---
id: pulleys-and-constraints
title: Pulley Systems and Constraint Forces
domain: physics
course: classical-mechanics
prerequisites:
- id: tension-forces-mechanics
  type: hard
- id: newtons-second-law
  type: hard
- id: pulleys
  type: soft
tags:
- constraints
- pulleys
- mechanics
stage: formal-systems
status: validated
---

# Pulley Systems and Constraint Forces

## Core Idea
Ideal pulleys redirect forces without losses, maintaining constant tension. Constraint forces (like tension) can be eliminated by using constraint equations relating accelerations of connected masses, reducing the number of equations needed.

## Questions

```yaml
- question: "In a simple Atwood machine, mass A (2 kg) hangs on one side and mass B (5 kg) hangs on the other over a single ideal pulley. After release, what can you immediately conclude from the constraint equation alone, before solving Newton's second law?"
  type: multiple-choice
  options:
    - "Mass B accelerates at 5/2 times the rate of mass A because it is heavier"
    - "Both masses have the same magnitude of acceleration, because rope leaving one side of an inextensible rope feeds directly onto the other"
    - "Mass A does not move because it is lighter"
    - "The system cannot be analyzed without knowing the moment of inertia of the pulley"
  answer: 1
  explanation: "The constraint comes from the inextensibility of the rope: if mass B moves down by some distance, mass A must move up by exactly the same distance, since the total rope length is fixed. Therefore their speeds and acceleration magnitudes are always equal. The masses' weights determine *which* direction each moves and what the common acceleration magnitude *is* — but the constraint tells you the magnitudes are equal before you do any force analysis. This is the central insight: the constraint equation is separate from and precedes Newton's second law."

- question: "In a compound pulley where two rope segments directly support a load of 100 N, you pull the free end of the rope with force F. To hold the load stationary, F must be approximately:"
  type: multiple-choice
  options:
    - "100 N"
    - "50 N"
    - "200 N"
    - "25 N"
  answer: 1
  explanation: "With two rope segments supporting the load, each segment bears half the total load — so each carries a tension of 50 N. Since the tension is the same throughout the rope (ideal pulley), F = 50 N. This is mechanical advantage of 2: you need half the force to support the load. The trade-off encoded in the constraint: to lift the load by 1 meter, you must pull the free end of the rope by 2 meters. Force halved, distance doubled — consistent with conservation of energy."

- question: "In an ideal pulley system, the tension is the same throughout the entire rope, regardless of how many direction changes the rope makes around frictionless pulleys."
  type: true-false
  answer: true
  explanation: "This is the defining property of an ideal pulley: it is massless and frictionless, so it changes the direction a rope exerts force without absorbing any of it. A massless frictionless pulley cannot sustain a net torque, which forces the tension on both sides to be equal. For a single rope passing over any number of ideal pulleys, there is exactly one tension value T throughout the rope. This is what allows the same tension to act in different directions on different objects connected by the rope."

- question: "A compound pulley that provides mechanical advantage (allowing you to lift a heavy load with less force) also allows you to move the load through the same distance as the effort end of the rope."
  type: true-false
  answer: false
  explanation: "This violates conservation of energy. Mechanical advantage trades force for distance: if two rope segments support the load, each segment must shorten by d for the load to rise by d, requiring the effort end to move 2d. In general, with n supporting rope segments, the effort rope moves n times as far as the load. You can lift a heavier object (mechanical advantage), but you must do so by pulling the rope a greater distance. Work input (F × distance pulled) equals work output (load × height raised)."

- question: "Why does the constraint-equation approach make it unnecessary to directly analyze the forces acting on the pulley itself?"
  type: short-answer
  answer: "The constraint equation captures the geometric relationship the pulley enforces (that rope lengths are conserved) without requiring any force analysis of the pulley. You write Newton's second law for each mass using tension T, then use the constraint to relate their accelerations and eliminate unknowns. The pulley disappears from the algebra because it contributes only a constraint (equal tensions, related accelerations) not an independent equation. Solving the system yields T and the accelerations without ever asking 'what net force acts on the pulley?'"
  explanation: "This is the power of the constraint-based method: you replace a complicated three-body problem (mass A + pulley + mass B) with a two-equation system (Newton's second law for each mass) plus one constraint equation (from inextensibility). The pulley is an ideal intermediary — it neither gains kinetic energy nor absorbs work, so it needs no separate equation. The constraint it enforces is simply encoded in the kinematic relationship between the masses."
```

## Explainer

From your study of tension forces, you know that a taut string transmits force: pull one end, and the other end pulls back with the same magnitude (for an ideal, massless string). From Newton's second law, you know how to find the acceleration of a single mass under known forces. Pulley problems combine both ideas — and add a new layer of complexity: the accelerations of connected masses are not independent. They are **constrained** by the geometry of the rope. Recognizing and writing down that constraint is the central skill.

An **ideal pulley** is massless and frictionless — it simply changes the direction a rope can exert force without absorbing any of it. Because the rope is ideal (massless, inextensible) and the pulley is frictionless, the tension is the same throughout the rope, regardless of direction changes. This is the key property: a single rope over a single ideal pulley carries one tension value T everywhere. So if mass A hangs on one side and mass B on the other, both experience a tension T in their string — but the *directions* differ. This is what a pulley does: it lets the same tension act in different directions on different objects.

The constraint equation comes from the inextensibility of the rope: the total length of rope doesn't change. For the simplest Atwood machine (two masses hanging over a single pulley), if mass A accelerates upward at a m/s², mass B must accelerate downward at a m/s² — the rope pulled off one side exactly feeds onto the other. Write Newton's second law for each mass separately (T − m_A·g = m_A·a for the rising mass, m_B·g − T = m_B·a for the falling mass), then use the constraint (same magnitude of acceleration) to eliminate one unknown. You have two equations and two unknowns (T and a) — solve the system.

More complex pulley arrangements introduce **mechanical advantage**: multiple rope segments supporting a single load mean each segment carries only a fraction of the load's weight, so less effort force is needed to lift it. But the constraint changes accordingly — if two rope segments support a load, the load moves half as fast as the effort end of the rope. In general, the constraint equation must account for the geometry carefully. The power of the constraint-based approach is that you never need to analyze what the pulley itself is "doing" — you write Newton's second law for each mass, write the geometric constraint relating their accelerations, and the system of equations yields both the tension and the accelerations. The pulley disappears from the algebra, replaced by the constraint it enforces.
