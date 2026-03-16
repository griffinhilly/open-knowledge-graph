---
id: current-divider-circuit
title: Current Divider Principle
domain: engineering
course: circuits-and-electronics
prerequisites:
- id: kirchhoff-current-law
  type: hard
builds-toward:
- series-parallel-resistor-analysis
- impedance-admittance-networks
tags:
- circuit-analysis
- resistive-circuits
- fundamental
stage: formal-systems
status: draft
---

# Current Divider Principle

## Core Idea
The current divider principle describes how current distributes through parallel branches: the current through any branch is inversely proportional to its resistance. For parallel resistors R₁ and R₂ with total current I, the current through R₁ is I × (R₂/(R₁+R₂)). This principle shows that current prefers paths of lower resistance and is essential for multi-branch circuit analysis.

## Explainer

From Kirchhoff's Current Law (KCL) you know that at any node, current flowing in equals current flowing out — charge is conserved. When two resistors are connected in parallel between the same two nodes, the total current I entering the junction must split between them. The current divider tells you exactly *how* it splits, without needing to solve a full system of equations.

Here is the derivation. Parallel resistors share the same voltage V across their terminals. By Ohm's law, I₁ = V/R₁ and I₂ = V/R₂. KCL says I = I₁ + I₂. The equivalent resistance of the parallel combination is R_eq = R₁R₂/(R₁+R₂), so V = I·R_eq. Substituting back: I₁ = V/R₁ = I·R_eq/R₁ = I·(R₂/(R₁+R₂)). Notice the result: branch 1's current contains R₂ in the numerator — the *other* branch's resistance. This is the counterintuitive feature beginners often get backwards. The branch with lower resistance carries more current, and its current fraction is determined by the opposing branch's resistance relative to the total.

A useful way to remember this: think of each branch as competing for current. A low-resistance path is "easier" — more current naturally flows through it. If R₁ = 0 (a short circuit), all current flows through branch 1 and none through R₂, because the voltage across both is zero and I₂ = 0/R₂ = 0. If R₁ = ∞ (an open circuit), no current flows through branch 1 and all flows through R₂. The formula captures this full range smoothly.

The principle extends to more than two branches by using **conductance** G = 1/R. The current through any branch is I × (G_branch / G_total), where G_total is the sum of all branch conductances. This form is more natural for multi-branch dividers and generalizes cleanly to AC circuits where you replace conductance with **admittance** Y = 1/Z. Current dividers appear throughout circuit analysis — in transistor biasing networks, current-mirror circuits, and sensor signal conditioning — making this one of the core two-component analysis tools alongside the voltage divider.
