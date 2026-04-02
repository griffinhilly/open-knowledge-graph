---
id: force-between-parallel-current-wires
title: Force Between Parallel Current-Carrying Wires
domain: physics
course: electricity-and-magnetism
prerequisites:
- id: force-on-current-carrying-conductor
  type: hard
- id: biot-savart-law
  type: hard
builds-toward:
- amperes-law
tags:
- magnetism
- forces
- current interaction
stage: expert
status: validated
---

# Force Between Parallel Current-Carrying Wires

## Core Idea
Parallel wires attract if currents are in the same direction and repel if opposite. The force per unit length is F/L = μ₀I₁I₂/(2πd), where d is separation. This arises because each wire creates a magnetic field that exerts force on current in the other. The interaction demonstrates that magnetic forces between currents are fundamental.

## Questions

```yaml
- question: "Two parallel wires carry currents in opposite directions. A student, reasoning by analogy with electric charges, predicts the wires will attract. Is this correct?"
  type: multiple-choice
  options:
    - "Yes — opposite currents attract, just as opposite charges attract"
    - "No — parallel wires with opposite (antiparallel) currents repel each other"
    - "No — opposite currents produce no force because their magnetic fields cancel"
    - "Yes, but only if the wires are separated by less than one meter"
  answer: 1
  explanation: "Antiparallel currents repel — the opposite of what the charge analogy would suggest. Use the right-hand rule: if wire 1 carries current in +z and wire 2 carries current in −z, wire 1's field at wire 2's location still points in the same direction, but wire 2's current is reversed, so the force reverses. The charge analogy breaks down entirely here: unlike charges attract because their fields point toward each other; antiparallel currents repel because their interaction involves a cross product of current direction with magnetic field direction."

- question: "Two parallel wires separated by distance d each carry current I. If the current in both wires is doubled and their separation is halved, by what factor does the force per unit length change?"
  type: multiple-choice
  options:
    - "Doubles (×2)"
    - "Quadruples (×4)"
    - "Increases by a factor of 8 (×8)"
    - "Increases by a factor of 16 (×16)"
  answer: 2
  explanation: "F/L = μ₀I₁I₂/(2πd). Doubling both currents multiplies I₁I₂ by 4. Halving the separation multiplies 1/d by 2. Combined effect: 4 × 2 = 8. The force grows with the product of the currents (so doubling both quadruples that factor) and inversely with distance (so halving the gap doubles that factor). The 1/d dependence is linear, not squared — an important distinction from Coulomb's law for point charges."

- question: "Two parallel wires carrying current in the same direction will attract each other."
  type: true-false
  answer: true
  explanation: "Parallel (same-direction) currents attract. Using the right-hand rule: wire 1's field at wire 2's location points perpendicular to the plane containing both wires. The force on wire 2 (F = IL × B) then points toward wire 1. This result — parallel currents attract — is counterintuitive relative to charge behavior but follows directly from the cross-product geometry. It was so fundamental that the original SI definition of the ampere was based on this force."

- question: "The force between two parallel current-carrying wires follows an inverse-square law, falling off as 1/d²."
  type: true-false
  answer: false
  explanation: "The force per unit length falls off as 1/d (linear inverse), not 1/d² (inverse square). F/L = μ₀I₁I₂/(2πd). This is because the magnetic field from an infinite straight wire falls off as 1/d (by Biot-Savart or Ampère's law), and the force is proportional to that field. The 1/r² law applies to point charges (Coulomb's law) and point magnetic dipoles, not to infinite line sources. The 1/d behavior makes parallel wire interactions longer-range than point-charge interactions at comparable distances."

- question: "Explain, using the right-hand rule, why parallel currents attract while antiparallel currents repel."
  type: short-answer
  answer: "Consider two wires both carrying current in the +z direction. By the right-hand rule, wire 1 creates a magnetic field circling counterclockwise around it. At wire 2's location (say, in the +x direction from wire 1), this field points in the −y direction. The force on wire 2 is F = I₂(ẑ) × (−ŷ) = I₂(x̂) — pointing toward wire 1, i.e., attraction. For antiparallel currents, wire 2 carries current in −z, so the force is I₂(−ẑ) × (−ŷ) = −I₂(x̂) — pointing away from wire 1, i.e., repulsion. The key is that the magnetic field direction is fixed by wire 1, but whether the resulting force is attractive or repulsive depends on wire 2's current direction via the cross product."
  explanation: "The right-hand rule for this problem has two applications: first to find the field from wire 1 (curl the fingers in the direction of current, field circles the wire), then to find the force on wire 2 using F = IL × B (point fingers in current direction, curl toward B, thumb points in force direction). The two-step application is what students often confuse, but working through it concretely with specific directions makes the attraction/repulsion result clear."
```

## Explainer

This result is built from two things you already know: the Biot-Savart law tells you the magnetic field produced by a current-carrying wire, and the force law F = IL × B tells you the force on a current in that field. Put them together for two wires and you get the interaction. Start with wire 1 carrying current I₁. By Biot-Savart (or equivalently Ampère's law), wire 1 creates a magnetic field B₁ = μ₀I₁/(2πd) at a distance d, circling around the wire according to the right-hand rule. Wire 2, sitting in that field and carrying its own current I₂, then feels a force per unit length F/L = I₂B₁ = μ₀I₁I₂/(2πd). Wire 1 simultaneously feels the same magnitude force from wire 2's field — Newton's third law holds.

The direction is the surprising part: **parallel currents attract, antiparallel currents repel** — the opposite of what happens with charges. Use the right-hand rule to see why. If both currents flow in the +z direction, wire 1's field at the location of wire 2 points in the −ŷ direction (into the page if you're looking along z). The force on wire 2 is F = I₂L × B₁ = I₂(ẑ) × (−ŷ) = I₂(x̂), pointing toward wire 1. Run through the same exercise with antiparallel currents and the force flips outward. An easy mnemonic: currents flowing together "want to merge," currents flowing opposite "push apart."

The formula F/L = μ₀I₁I₂/(2πd) reveals that the force is long-range (it falls off as 1/d, just like the electric field of a line charge) and proportional to both currents. Historically, this relationship was so clean and fundamental that it served as the original definition of the ampere: one ampere was defined as the current in each of two parallel wires one meter apart that produces a force of exactly 2 × 10⁻⁷ N per meter. Modern SI has since redefined the ampere in terms of a fixed numerical value of the elementary charge, but the interaction between parallel wires remains one of the conceptually cleanest results in magnetostatics.

This interaction also shows that magnetism is not fundamentally different from electricity — it is the electromagnetic interaction viewed from a particular arrangement of moving charges. Two current-carrying wires are just two streams of moving charges, and their interaction (attraction or repulsion) arises from the same underlying electromagnetic force. This builds directly toward Ampère's law, which generalizes this picture to arbitrary current distributions, and eventually to the full unified picture of electromagnetism.
