---
id: tension-forces-mechanics
title: Tension Forces in Strings and Cables
domain: physics
course: classical-mechanics
prerequisites:
- id: newtons-third-law
  type: hard
- id: normal-force-contact-forces
  type: soft
builds-toward:
- pulleys-and-constraints
- coupled-oscillator-equations
tags:
- forces
- contact
- tension
stage: formal-systems
status: draft
---

# Tension Forces in Strings and Cables

## Core Idea
Tension is the pulling force exerted by a rope or string, acting along its length. In an ideal massless inextensible string, tension is constant throughout and acts to accelerate both connected objects as if they were a single system.

## How It's Best Learned
Analyze systems with pulleys and multiple masses. Use free-body diagrams for each object separately, then apply constraints that relate their accelerations through the rope geometry.

## Common Misconceptions
Tension is not always equal to an object's weight. In a pulley system, the tension in a rope changes if the rope passes over a pulley with friction or if the pulley has significant mass.

## Explainer

From Newton's Third Law you know that contact forces come in pairs, and from your study of normal force you know how surfaces transmit pushes perpendicular to their face. **Tension** is the complementary contact force: strings and cables transmit *pulls* along their length. A string can only pull its two endpoints toward each other — it cannot push them apart. This is the fundamental asymmetry between strings (which only pull) and rigid rods (which can both push and pull). If you try to push with a string, it goes slack and transmits no force.

The two simplifying assumptions — **massless** and **inextensible** — define the ideal string and make tension problems tractable. A massless string has no weight of its own to support and no inertia of its own to accelerate. This means every cross-section of the string must transmit the same force: if one end pulls with tension T, the whole string pulls with tension T. You can verify this with Newton's Second Law applied to any segment of the string: net force = (mass of segment) × acceleration = 0 × a = 0, so the forces on both ends of any segment must be equal and opposite — the tension is constant throughout. An inextensible string doesn't stretch, so the speed and acceleration of both endpoints are constrained to be equal (for a straight string) or related by the geometry (for strings over pulleys).

In free-body diagrams, tension forces always point *away from* the object and *along* the string. For a ball hanging from a ceiling by a rope: draw the tension arrow pointing upward along the rope from the ball toward the ceiling. The rope is also pulling the ceiling downward — those are Newton's Third Law partners — but they act on the ceiling, not the ball, so they don't appear on the ball's free-body diagram.

**Pulley problems** show the power of these idealizations. Connect mass A (hanging on the left) to mass B (hanging on the right) over a frictionless, massless pulley. The string tension is the same throughout — call it T. Write Newton's Second Law for each mass separately: for A (taking down as positive), m_A·g − T = m_A·a. For B (taking up as positive), T − m_B·g = m_B·a. The constraint that the string doesn't stretch means both masses have the same magnitude of acceleration a. Now you have two equations and two unknowns (T and a). Solving: a = (m_A − m_B)g / (m_A + m_B), and T = 2m_A·m_B·g / (m_A + m_B). Notice that T is less than either weight — the rope can't be pulling A up as hard as A's full weight, or A wouldn't accelerate down.

When the idealizations break down — a rope with significant mass, a pulley with friction or rotational inertia — tension is no longer constant along the rope. A massive rope on a table must support the weight of the rope below it, so tension increases with height. A frictional pulley creates different tensions on its two sides, which is how a capstan (winch) works: a small force on one side can hold a large load on the other. These complications require the same conceptual framework — Newton's Second Law applied to each element — extended to handle the additional physics.
