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
tags:
- constraints
- pulleys
- mechanics
stage: formal-systems
status: draft
---

# Pulley Systems and Constraint Forces

## Core Idea
Ideal pulleys redirect forces without losses, maintaining constant tension. Constraint forces (like tension) can be eliminated by using constraint equations relating accelerations of connected masses, reducing the number of equations needed.

## Explainer

From your study of tension forces, you know that a taut string transmits force: pull one end, and the other end pulls back with the same magnitude (for an ideal, massless string). From Newton's second law, you know how to find the acceleration of a single mass under known forces. Pulley problems combine both ideas — and add a new layer of complexity: the accelerations of connected masses are not independent. They are **constrained** by the geometry of the rope. Recognizing and writing down that constraint is the central skill.

An **ideal pulley** is massless and frictionless — it simply changes the direction a rope can exert force without absorbing any of it. Because the rope is ideal (massless, inextensible) and the pulley is frictionless, the tension is the same throughout the rope, regardless of direction changes. This is the key property: a single rope over a single ideal pulley carries one tension value T everywhere. So if mass A hangs on one side and mass B on the other, both experience a tension T in their string — but the *directions* differ. This is what a pulley does: it lets the same tension act in different directions on different objects.

The constraint equation comes from the inextensibility of the rope: the total length of rope doesn't change. For the simplest Atwood machine (two masses hanging over a single pulley), if mass A accelerates upward at a m/s², mass B must accelerate downward at a m/s² — the rope pulled off one side exactly feeds onto the other. Write Newton's second law for each mass separately (T − m_A·g = m_A·a for the rising mass, m_B·g − T = m_B·a for the falling mass), then use the constraint (same magnitude of acceleration) to eliminate one unknown. You have two equations and two unknowns (T and a) — solve the system.

More complex pulley arrangements introduce **mechanical advantage**: multiple rope segments supporting a single load mean each segment carries only a fraction of the load's weight, so less effort force is needed to lift it. But the constraint changes accordingly — if two rope segments support a load, the load moves half as fast as the effort end of the rope. In general, the constraint equation must account for the geometry carefully. The power of the constraint-based approach is that you never need to analyze what the pulley itself is "doing" — you write Newton's second law for each mass, write the geometric constraint relating their accelerations, and the system of equations yields both the tension and the accelerations. The pulley disappears from the algebra, replaced by the constraint it enforces.
