---
id: capacitor-field-energy-storage
title: Energy Storage in Capacitor Fields
domain: physics
course: electricity-and-magnetism
prerequisites:
- id: parallel-plate-capacitor
  type: hard
- id: electric-potential-energy
  type: hard
builds-toward:
- electromagnetic-field-energy
tags:
- energy
- capacitors
- field energy
stage: formal-systems
status: validated
---

# Energy Storage in Capacitor Fields

## Core Idea
Energy is stored in the electric field of a charged capacitor: U = (1/2)CV² = (1/2)QV = Q²/(2C). The energy comes from work done separating charges and is distributed throughout the field region. The energy density is u = (1/2)ε₀E², which integrates to give total stored energy.

## How It's Best Learned
Calculate stored energy using all three formulas and verify consistency. Derive energy density by considering work to assemble charge incrementally.

## Common Misconceptions
- Energy is stored 'in the plates' rather than in the field between them.
- Energy density is uniform for non-uniform fields (only true when E is uniform).
- Confusing stored energy with power (different units: joules vs watts).

## Questions

```yaml
- question: "A capacitor with capacitance C is charged to voltage V. The voltage is then doubled to 2V. What happens to the stored energy?"
  type: multiple-choice
  options:
    - "It doubles, since energy is proportional to voltage"
    - "It quadruples, since U = ½CV² and voltage is squared"
    - "It stays the same — only capacitance affects stored energy"
    - "It halves — higher voltage means the same charge is stored more efficiently"
  answer: 1
  explanation: "U = ½CV², so doubling V gives U_new = ½C(2V)² = 4 × ½CV² — the energy quadruples. The quadratic dependence on voltage is why high-voltage capacitors store dramatically more energy than low-voltage ones of the same capacitance. This is not intuitive if you think of energy as simply proportional to voltage, which is the common error."

- question: "Where does the energy in a charged parallel-plate capacitor actually reside?"
  type: multiple-choice
  options:
    - "In the charges accumulated on the metal plates"
    - "In the connecting wires, as electrical current flowing between plates"
    - "In the electric field distributed throughout the volume between the plates"
    - "Equally split between the surface charges and the space between the plates"
  answer: 2
  explanation: "The energy density u = ½ε₀E² is distributed throughout the volume where the electric field exists — the space between the plates. The plates carry charges that maintain the field, but the energy resides in the field itself. This field-centric view becomes essential for understanding electromagnetic waves, where energy propagates through empty space with no charges involved at all."

- question: "The energy stored in a capacitor is ½QV rather than QV because the voltage builds gradually from zero as charge is added."
  type: true-false
  answer: true
  explanation: "The first charge element is moved against essentially no field — little work required. Each subsequent element must fight the growing field established by earlier charge. The average voltage during the charging process is V/2 (not V), so total work = Q × (V/2) = ½QV. The factor of ½ is the signature of any energy-storage process where the 'back-pressure' increases linearly as the store fills — springs follow the same logic: F = kx increases linearly, giving stored energy ½kx²."

- question: "The energy density formula u = ½ε₀E² applies mainly to parallel-plate capacitors where the electric field is uniform."
  type: true-false
  answer: false
  explanation: "The formula u = ½ε₀E² is a universal result for the energy density of any electric field in free space — not limited to uniform fields or parallel-plate geometry. For a nonuniform field (like that of a point charge), you integrate u over all space to find total stored energy. The parallel-plate case is simply the special situation where the field is uniform, making the integral trivial (u times volume). The generality of the formula is what makes it fundamental to electromagnetism."

- question: "Explain why the energy stored in a capacitor is ½QV rather than QV, and what the factor of one-half tells you about energy-storage processes more generally."
  type: short-answer
  answer: "When charging begins, there is no field and the first charge moves easily. As charge accumulates, the electric field grows and each subsequent charge element must be pushed against a stronger opposing field, requiring more work. The voltage ramps linearly from 0 to V during charging, so the average voltage is V/2. Total work = charge × average voltage = Q × (V/2) = ½QV. The factor of ½ appears in any storage process where the 'resistance' grows linearly with the stored quantity — a spring stores ½kx² for the same reason."
  explanation: "This principle generalizes broadly. The quadratic energy-storage relationship (U ∝ V² for a capacitor, U ∝ x² for a spring, U ∝ I² for an inductor) always arises when the quantity being stored builds up the very force opposing further storage. In all these cases, the average 'back-pressure' during filling is half the final value, giving the factor of ½. Recognizing this pattern unifies capacitor, spring, and inductor energy storage under a single physical principle."
```

## Explainer

When you charge a capacitor, you do work moving charge from one plate to the other against a growing electric field. The first charge element moves easily — there is no field yet — but each subsequent element must fight the field already established by the charge before it. The total work done to separate charge Q across voltage V is U = ½QV, not QV, because the voltage builds gradually from zero. This factor of one-half is the signature of any energy-storage process where the "resistance" increases as you fill the store.

The three formulas — **U = ½CV² = ½QV = Q²/(2C)** — are all equivalent, related through Q = CV. Which form to use depends on what you know. If you're given voltage and capacitance, use ½CV². If charge is specified, Q²/(2C) avoids substitution errors. All three express the same physical energy stored in the system. Importantly, doubling the voltage quadruples the stored energy (since U ∝ V²), which is why high-voltage capacitors store dramatically more energy than low-voltage ones of the same capacitance.

The deeper insight is *where* the energy lives. From the perspective of parallel-plate geometry, the electric field between the plates is uniform: E = V/d. Substituting Q = CV and C = ε₀A/d into U = Q²/(2C) and dividing by the volume Ad between the plates gives the **energy density**: u = ½ε₀E². This result says energy is stored in the field itself, distributed throughout the volume where the field exists — not concentrated on the charges at the plates. This field-centric view becomes essential when you extend to electromagnetic waves, where energy propagates through space with no charges involved at all.

The energy density u = ½ε₀E² holds not just for parallel-plate capacitors but for any electric field in free space. To find total energy in a nonuniform field, you integrate u over all space. For the uniform capacitor field this integral is trivial — u times volume — but for a point charge or a more complex geometry the field varies with position and the integral must be computed explicitly. This connection between the formula you derived for capacitors and the general electromagnetic field energy is one of the most satisfying unifications in electromagnetism.
