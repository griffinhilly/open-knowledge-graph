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
stage: formal-systems
status: draft
---

# Force Between Parallel Current-Carrying Wires

## Core Idea
Parallel wires attract if currents are in the same direction and repel if opposite. The force per unit length is F/L = μ₀I₁I₂/(2πd), where d is separation. This arises because each wire creates a magnetic field that exerts force on current in the other. The interaction demonstrates that magnetic forces between currents are fundamental.

## Explainer

This result is built from two things you already know: the Biot-Savart law tells you the magnetic field produced by a current-carrying wire, and the force law F = IL × B tells you the force on a current in that field. Put them together for two wires and you get the interaction. Start with wire 1 carrying current I₁. By Biot-Savart (or equivalently Ampère's law), wire 1 creates a magnetic field B₁ = μ₀I₁/(2πd) at a distance d, circling around the wire according to the right-hand rule. Wire 2, sitting in that field and carrying its own current I₂, then feels a force per unit length F/L = I₂B₁ = μ₀I₁I₂/(2πd). Wire 1 simultaneously feels the same magnitude force from wire 2's field — Newton's third law holds.

The direction is the surprising part: **parallel currents attract, antiparallel currents repel** — the opposite of what happens with charges. Use the right-hand rule to see why. If both currents flow in the +z direction, wire 1's field at the location of wire 2 points in the −ŷ direction (into the page if you're looking along z). The force on wire 2 is F = I₂L × B₁ = I₂(ẑ) × (−ŷ) = I₂(x̂), pointing toward wire 1. Run through the same exercise with antiparallel currents and the force flips outward. An easy mnemonic: currents flowing together "want to merge," currents flowing opposite "push apart."

The formula F/L = μ₀I₁I₂/(2πd) reveals that the force is long-range (it falls off as 1/d, just like the electric field of a line charge) and proportional to both currents. Historically, this relationship was so clean and fundamental that it served as the original definition of the ampere: one ampere was defined as the current in each of two parallel wires one meter apart that produces a force of exactly 2 × 10⁻⁷ N per meter. Modern SI has since redefined the ampere in terms of a fixed numerical value of the elementary charge, but the interaction between parallel wires remains one of the conceptually cleanest results in magnetostatics.

This interaction also shows that magnetism is not fundamentally different from electricity — it is the electromagnetic interaction viewed from a particular arrangement of moving charges. Two current-carrying wires are just two streams of moving charges, and their interaction (attraction or repulsion) arises from the same underlying electromagnetic force. This builds directly toward Ampère's law, which generalizes this picture to arbitrary current distributions, and eventually to the full unified picture of electromagnetism.
