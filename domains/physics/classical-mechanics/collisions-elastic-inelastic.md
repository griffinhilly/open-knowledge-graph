---
id: collisions-elastic-inelastic
title: Elastic and Inelastic Collisions
domain: physics
course: classical-mechanics
prerequisites:
- id: conservation-of-momentum
  type: hard
- id: conservation-of-energy
  type: soft
tags:
- collisions
- elastic
- inelastic
- perfectly-inelastic
stage: formal-systems
status: validated
---

# Elastic and Inelastic Collisions

## Core Idea
In elastic collisions, both momentum and kinetic energy are conserved (e.g., billiard balls at low speed). In perfectly inelastic collisions, objects stick together, momentum is conserved, but kinetic energy is not. In between are partially inelastic collisions. The coefficient of restitution e (ratio of relative speeds after to before) characterizes a collision: e = 1 (elastic), 0 < e < 1 (partially inelastic), e = 0 (perfectly inelastic).

## How It's Best Learned
Solve elastic collisions in 1D using both conservation equations simultaneously. For perfectly inelastic collisions, use a single momentum equation since the objects share a final velocity. Check: can kinetic energy increase in a collision? (No — a coefficient e > 1 would require an explosive.)

## Common Misconceptions
- Thinking elastic means the objects bounce 'hard' — elastic strictly means kinetic energy is conserved, not how hard the impact looks.
- Trying to apply both conservation laws to an inelastic collision: kinetic energy is not conserved, so only momentum conservation applies.

## Questions

```yaml
- question: "Two rubber balls collide and bounce back vigorously. A student says 'That must be elastic — look how hard they bounced!' A lab partner says 'We can't tell without measuring kinetic energy before and after.' Who is right?"
  type: multiple-choice
  options:
    - "The first student — a hard bounce is the definition of an elastic collision"
    - "The lab partner — elastic means kinetic energy is conserved, which cannot be determined from appearance alone"
    - "Both — a vigorous bounce necessarily implies kinetic energy conservation"
    - "Neither — elasticity is determined by the coefficient of restitution, which requires measuring deformation"
  answer: 1
  explanation: "Elastic is a precise technical term: a collision is elastic if and only if kinetic energy is conserved — the objects emerge with the same total KE they had before impact. How vigorous or dramatic the bounce appears is irrelevant. Real rubber balls are actually inelastic; they deform, generate heat, and lose kinetic energy even in a 'hard' bounce. The only way to classify a collision as elastic is to measure KE before and after (or measure e = 1 using relative speeds). The visual appearance of the collision tells you nothing definitive about energy conservation."

- question: "Two clay balls collide and stick together, moving as one mass after the impact. Which quantities are conserved in this collision?"
  type: multiple-choice
  options:
    - "Both momentum and kinetic energy"
    - "Kinetic energy only"
    - "Momentum only"
    - "Neither — the sticking together means energy is destroyed and momentum redistributed"
  answer: 2
  explanation: "This is a perfectly inelastic collision (e = 0). Momentum is always conserved in a collision with no net external force — including perfectly inelastic ones. Kinetic energy is NOT conserved: the objects deform permanently, generating heat and sound, and the combined mass moves slower than either original object was moving (in center-of-mass frame, all kinetic energy in that frame is lost). Note that option D is wrong in a subtle way: total energy IS still conserved globally — kinetic energy converts to internal energy (heat, deformation), it is not destroyed. Only kinetic energy decreases."

- question: "In any collision between two objects with no net external force, total momentum of the system is conserved regardless of whether the collision is elastic, inelastic, or perfectly inelastic."
  type: true-false
  answer: true
  explanation: "Momentum conservation is a consequence of Newton's third law and the absence of net external forces — it does not depend on what happens to kinetic energy. During a collision, the internal forces between the colliding objects are equal and opposite, so they cancel in the momentum sum. This holds whether the collision converts some kinetic energy to heat (inelastic) or none at all (elastic). Momentum conservation is universal across collision types; kinetic energy conservation is the special additional condition that defines elasticity."

- question: "In an inelastic collision, total energy is not conserved — some energy is permanently destroyed during the impact."
  type: true-false
  answer: false
  explanation: "Total energy is always conserved — this is one of the most fundamental principles in physics. What changes in an inelastic collision is the form of energy: kinetic energy converts to internal energy (heat, sound, permanent deformation of the objects). The total energy budget is unchanged; it is redistributed. Saying energy is 'lost' is sloppy shorthand for 'lost from the kinetic budget.' The distinction matters because it determines what tools you can use: for inelastic collisions you cannot apply KE conservation, but total energy conservation still holds and connects kinetic energy loss to thermal energy gain."

- question: "Why can you apply two conservation laws (momentum AND kinetic energy) when solving an elastic collision, but only one (momentum) for a perfectly inelastic collision? What determines this?"
  type: short-answer
  answer: "In an elastic collision, the internal forces between the objects are perfectly conservative — no energy leaves the kinetic budget. Both momentum and KE are unchanged after the collision, giving two independent equations to solve for the two unknown final velocities. In a perfectly inelastic collision, kinetic energy is converted to internal energy (heat, deformation). The amount converted is unknown without additional information about the materials, so KE conservation cannot be written as a constraint on final velocities. Momentum conservation still holds (external forces are absent), giving one equation for one unknown (the shared final velocity of the combined mass). The collision type determines how many usable conservation laws you have."
  explanation: "This is the practical core of the topic. The coefficient of restitution e encodes which case you're in: e = 1 allows both laws, e = 0 (perfectly inelastic) allows only momentum conservation. For intermediate e, you use the restitution condition (v₂' - v₁' = -e(v₂ - v₁)) as your second equation instead of KE conservation, which avoids needing to know the details of energy dissipation."
```

## Explainer

You already know that **momentum is conserved** whenever no net external force acts on a system, and that **kinetic energy is conserved** in isolated systems with only conservative forces. Collisions let you see these two principles operating together — or separately — depending on what happens at the moment of impact.

The key distinction is what happens to kinetic energy *during* the collision. In an **elastic collision**, the objects deform and rebound without any permanent deformation or heat generation — the internal forces are perfectly conservative, so kinetic energy is restored when the objects separate. Billiard balls and atomic collisions approximate this well. In an **inelastic collision**, some kinetic energy is converted into internal energy — heat, sound, deformation — during the collision. That energy doesn't disappear (total energy is always conserved), but it leaves the kinetic budget. In a **perfectly inelastic collision**, the objects stick together and move as one, maximizing the loss of kinetic energy consistent with momentum conservation.

For a **1D elastic collision** between two objects, you have two conservation equations: Σp_before = Σp_after, and ΣKE_before = ΣKE_after. Writing these out: m₁v₁ + m₂v₂ = m₁v₁' + m₂v₂', and ½m₁v₁² + ½m₂v₂² = ½m₁v₁'² + ½m₂v₂'². Two equations, two unknowns (v₁' and v₂'). The kinetic energy equation is quadratic, but it factors conveniently — you can rewrite it as m₁(v₁ - v₁')(v₁ + v₁') = m₂(v₂' - v₂)(v₂' + v₂'), then combine with the momentum equation to get the elegant result: the **relative speed of approach equals the relative speed of separation**, (v₁ - v₂) = -(v₁' - v₂'). This is the elastic collision's signature, and it makes the algebra tractable.

The **coefficient of restitution** *e* generalizes this: it is the ratio of the relative speed after to the relative speed before, *e* = |v₂' - v₁'| / |v₁ - v₂|. For elastic collisions e = 1, for perfectly inelastic e = 0, and real collisions fall in between. Notice that e > 1 would mean the objects speed up during collision — impossible without an internal energy source like an explosion. The coefficient of restitution is the single parameter that characterizes where a real collision sits on the spectrum, and it is directly measurable by dropping a ball and seeing how high it bounces. This is why e is useful in engineering: it captures the collision behavior without requiring you to model all the internal energy losses in detail.
