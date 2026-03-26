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
status: validated
---

# Tension Forces in Strings and Cables

## Core Idea
Tension is the pulling force exerted by a rope or string, acting along its length. In an ideal massless inextensible string, tension is constant throughout and acts to accelerate both connected objects as if they were a single system.

## How It's Best Learned
Analyze systems with pulleys and multiple masses. Use free-body diagrams for each object separately, then apply constraints that relate their accelerations through the rope geometry.

## Common Misconceptions
Tension is not always equal to an object's weight. In a pulley system, the tension in a rope changes if the rope passes over a pulley with friction or if the pulley has significant mass.

## Questions

```yaml
- question: "Two masses hang over a frictionless, massless pulley: mass A (3 kg) on the left and mass B (5 kg) on the right. The tension T in the rope is:"
  type: multiple-choice
  options:
    - "Equal to 5 × 9.8 = 49 N, the weight of the heavier mass"
    - "Equal to 3 × 9.8 = 29.4 N, the weight of the lighter mass"
    - "Equal to (3 × 5 × 2 × 9.8) / (3 + 5) = 36.75 N, less than either weight"
    - "Equal to (3 + 5) × 9.8 / 2 = 39.2 N, the average of both weights"
  answer: 2
  explanation: "From the Atwood machine equations: T = 2·m_A·m_B·g / (m_A + m_B) = 2×3×5×9.8/8 = 36.75 N. This is less than either weight (29.4 N and 49 N). The tension cannot equal the heavier weight — if it did, the heavier mass would be in equilibrium and wouldn't accelerate. The rope must be pulling each mass partially against gravity while also allowing them to accelerate, so T ends up between the two weights but less than either one separately."

- question: "Why is tension constant throughout an ideal massless string, even when different forces are applied to each end?"
  type: multiple-choice
  options:
    - "Because strings are made of elastic material that distributes force evenly"
    - "Because Newton's Third Law requires forces to be equal and opposite at every point"
    - "Because any segment of a massless string has zero mass, so the net force on it must be zero, meaning both ends pull with equal force"
    - "Because the string is inextensible, preventing any variation in force along its length"
  answer: 2
  explanation: "Apply Newton's Second Law to any small segment of the string: F_net = m_segment × a. For a massless string, m_segment = 0, so F_net = 0 regardless of acceleration. This means the force pulling one end of any segment must exactly equal the force pulling the other end — the tension is the same on both sides of any cross-section. Inextensibility (option D) constrains acceleration, not force distribution. Newton's Third Law (option B) applies to force pairs between objects, not to internal force distribution along a rope."

- question: "In an ideal (massless, inextensible) string, the tension is the same at every point along the string."
  type: true-false
  answer: true
  explanation: "This follows directly from Newton's Second Law applied to any segment: zero mass means zero net force, so the tension forces at both ends of any segment must be equal. This idealization is what makes rope problems tractable — you can refer to 'the tension T' as a single value rather than tracking how it varies along the length. When the idealization breaks down (massive rope, frictional pulley), tension is no longer uniform."

- question: "The tension in the rope of a pulley system generally equals the weight of the heavier object."
  type: true-false
  answer: false
  explanation: "Tension in a pulley system is strictly less than the weight of either object when both are accelerating. If the tension equaled the heavier weight, that object would experience zero net force and wouldn't accelerate — contradicting the assumption that the system moves. Tension represents the force the rope exerts, which must be less than the heavier weight (to allow downward acceleration) and greater than the lighter weight (to pull it upward). The formula T = 2·m_A·m_B·g / (m_A + m_B) confirms this."

- question: "Why can a string only pull its endpoints toward each other and never push them apart, and how does this asymmetry affect how you draw free-body diagrams?"
  type: short-answer
  answer: "Strings transmit tension — a pulling force — because their structure only allows them to resist being stretched. When pulled taut, the intermolecular bonds along the string carry the load. When compressed, the string simply goes slack and transmits no force. This asymmetry means tension arrows on free-body diagrams always point away from the object (toward the string), never toward the object. A ball on a string hanging from a ceiling has a tension arrow pointing upward along the rope from the ball; the same string cannot push the ball downward."
  explanation: "This directional rule — tension always pulls, never pushes, always away from the object — is the single most important discipline in drawing tension free-body diagrams. Confusing the direction of tension (pointing toward the ceiling versus toward the ball) is the most common error in setting up Newton's Second Law equations for string-connected systems. Rigid rods can push and pull; strings can only pull."
```

## Explainer

From Newton's Third Law you know that contact forces come in pairs, and from your study of normal force you know how surfaces transmit pushes perpendicular to their face. **Tension** is the complementary contact force: strings and cables transmit *pulls* along their length. A string can only pull its two endpoints toward each other — it cannot push them apart. This is the fundamental asymmetry between strings (which only pull) and rigid rods (which can both push and pull). If you try to push with a string, it goes slack and transmits no force.

The two simplifying assumptions — **massless** and **inextensible** — define the ideal string and make tension problems tractable. A massless string has no weight of its own to support and no inertia of its own to accelerate. This means every cross-section of the string must transmit the same force: if one end pulls with tension T, the whole string pulls with tension T. You can verify this with Newton's Second Law applied to any segment of the string: net force = (mass of segment) × acceleration = 0 × a = 0, so the forces on both ends of any segment must be equal and opposite — the tension is constant throughout. An inextensible string doesn't stretch, so the speed and acceleration of both endpoints are constrained to be equal (for a straight string) or related by the geometry (for strings over pulleys).

In free-body diagrams, tension forces always point *away from* the object and *along* the string. For a ball hanging from a ceiling by a rope: draw the tension arrow pointing upward along the rope from the ball toward the ceiling. The rope is also pulling the ceiling downward — those are Newton's Third Law partners — but they act on the ceiling, not the ball, so they don't appear on the ball's free-body diagram.

**Pulley problems** show the power of these idealizations. Connect mass A (hanging on the left) to mass B (hanging on the right) over a frictionless, massless pulley. The string tension is the same throughout — call it T. Write Newton's Second Law for each mass separately: for A (taking down as positive), m_A·g − T = m_A·a. For B (taking up as positive), T − m_B·g = m_B·a. The constraint that the string doesn't stretch means both masses have the same magnitude of acceleration a. Now you have two equations and two unknowns (T and a). Solving: a = (m_A − m_B)g / (m_A + m_B), and T = 2m_A·m_B·g / (m_A + m_B). Notice that T is less than either weight — the rope can't be pulling A up as hard as A's full weight, or A wouldn't accelerate down.

When the idealizations break down — a rope with significant mass, a pulley with friction or rotational inertia — tension is no longer constant along the rope. A massive rope on a table must support the weight of the rope below it, so tension increases with height. A frictional pulley creates different tensions on its two sides, which is how a capstan (winch) works: a small force on one side can hold a large load on the other. These complications require the same conceptual framework — Newton's Second Law applied to each element — extended to handle the additional physics.
