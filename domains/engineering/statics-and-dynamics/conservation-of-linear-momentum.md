---
id: conservation-of-linear-momentum
title: Conservation of Linear Momentum in Systems
domain: engineering
course: statics-and-dynamics
prerequisites:
- id: linear-momentum-impulse-systems
  type: hard
- id: newtons-three-laws-mechanics
  type: soft
builds-toward:
- systems-of-particles-mechanics
tags:
- momentum
- conservation-laws
- systems
stage: formal-systems
status: validated
---

# Conservation of Linear Momentum in Systems

## Core Idea
When no external forces act on a system (or sum to zero), total linear momentum remains constant. This conservation law follows directly from Newton's third law and is far more powerful than tracking individual particle motions—it solves collision and explosion problems without knowing details of internal forces.

## Questions

```yaml
- question: "Two cars collide and exert enormous forces on each other for 0.1 seconds. A student claims 'momentum cannot be conserved because the collision forces are so large.' What is the student getting wrong?"
  type: multiple-choice
  options:
    - "The student is correct — large internal forces always violate momentum conservation"
    - "The collision forces are internal to the two-car system; Newton's third law guarantees they cancel in pairs and don't change the system's total momentum"
    - "Momentum is only conserved when forces are small and act over long time periods"
    - "The student should apply energy conservation instead, since momentum doesn't apply to contact forces"
  answer: 1
  explanation: "The size of internal forces is irrelevant to conservation. Newton's third law guarantees that every internal force has an equal and opposite reaction force within the system — they cancel in pairs when summed. Only external forces can change the total system momentum. The collision forces between the two cars are enormous but internal to the two-car system, so they cancel and total momentum is conserved (subject to external impulses like friction being negligible during the brief collision)."

- question: "A stationary grenade explodes into three fragments. What is the total momentum of all three fragments immediately after the explosion?"
  type: multiple-choice
  options:
    - "Impossible to determine without knowing the explosion force magnitude and direction"
    - "Greater than zero, since the explosion adds kinetic energy and thus momentum to the system"
    - "Zero, because the grenade was at rest and external impulses during the brief explosion are negligible"
    - "Equal to the impulse of the explosive force times the duration of the explosion"
  answer: 2
  explanation: "Before the explosion, the system (the grenade) has zero momentum. The explosion forces are entirely internal to the system — the explosive gases push the fragments, but those are all parts of the same system. External forces (gravity, air) act for such a short time that their impulse mg·Δt ≈ 0. Therefore total momentum after = total momentum before = 0. The three fragments' momenta must vector-sum to zero. This is the 'explosion run in reverse' principle."

- question: "If you analyze only one object in a two-object collision — say, just Ball A — the contact force from Ball B is an internal force to your analysis and can be ignored."
  type: true-false
  answer: false
  explanation: "The contact force is internal only if BOTH balls are included in the system. If your system boundary contains only Ball A, then the force from Ball B acts on your system from outside — it is external, it produces an impulse, and it changes Ball A's momentum. This is why analyzing the full two-ball system is powerful: the contact forces become internal and cancel, leaving only any external impulses. Shrinking the system boundary makes those forces external and must be included."

- question: "Conservation of linear momentum can hold in one coordinate direction even when it fails in another direction due to an external force."
  type: true-false
  answer: true
  explanation: "Conservation is directional and applies independently in x, y, and z. A hockey puck sliding across frictionless ice and struck by a glancing blow in the x-direction conserves momentum in the y-direction (no external y-impulse) even though y-direction momentum is not conserved in x. This independence is frequently the key to solving 2D collision problems: if the ball can only leave in one direction, that constraint gives you an equation for one component that's independent of the others."

- question: "Explain why the choice of system boundary is critical when applying conservation of momentum, and how choosing the right boundary simplifies a seemingly complex problem."
  type: short-answer
  answer: "The system boundary determines which forces are internal (and therefore cancel by Newton's third law) and which are external (and must be tracked as impulses). Internal forces always cancel in pairs and cannot change total momentum. By choosing a boundary where all large interaction forces are internal and external impulses are negligible, you convert a problem involving unknown contact forces into a simple bookkeeping equation: total momentum before = total momentum after."
  explanation: "This is the strategic insight that makes conservation laws powerful. In a billiard ball collision, the contact forces peak at thousands of newtons and vary in complex ways during the millisecond impact. You never need to model them — just include both balls in your system, confirm that external impulses are negligible during the brief collision, and write one vector equation. The complexity of the internal mechanics is completely bypassed. The art of mechanics problems is often choosing the right system."
```

## Explainer

From your work with impulse and momentum, you know that the change in a single particle's momentum equals the net impulse applied to it: ΔL = ∫F_net dt. Now extend that thinking to a **system** of particles. Any two particles within the system exert forces on each other — but Newton's third law guarantees those internal forces are equal in magnitude and opposite in direction. When you add up all the momenta changes across the entire system, the internal forces cancel in pairs. Only the **external forces** — forces from outside the system boundary — can change the total momentum. If the external forces sum to zero (or if the time interval is so short that their impulse is negligible), the total momentum before equals the total momentum after.

This is powerful because it lets you bypass the internal force details entirely. In a collision between two billiard balls, enormous contact forces act for a few milliseconds — forces that are difficult to measure or model. You never need to know them. You only need to identify the system (both balls), confirm that external impulses are negligible during the collision (gravity acts, but the collision is so brief that mg·Δt ≈ 0), and then write **m₁v₁ + m₂v₂ = m₁v₁' + m₂v₂'**. The same logic applies to explosions run in reverse: a stationary artillery shell that bursts into fragments must have zero total momentum after the explosion because it had zero momentum before.

Conservation is **directional**: it applies independently in x, y, and z. A hockey puck sliding across frictionless ice and struck by a glancing blow conserves momentum in the direction perpendicular to the impulse, even if it does not conserve momentum in the direction of the impulse. This independence is frequently the key to solving two-dimensional collision problems: one direction may be constrained (a ball bouncing off a wall can only leave horizontally), giving you an equation that pins down one component of the unknown velocity.

Watch the system boundary carefully. Include all objects that interact internally; exclude everything whose forces you want to ignore as external. If friction is present and acts for a nontrivial time, it is an external impulse and momentum is not conserved. If the problem asks you to analyze only part of the collision — say, one of the two colliding objects — then the contact force between them is external to that subsystem and must be included. The beauty of conservation is that it rewards choosing the right system: pick the boundary where external impulses vanish, and a complicated interaction collapses into a simple bookkeeping equation.


