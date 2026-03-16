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
status: draft
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

## Explainer

When you charge a capacitor, you do work moving charge from one plate to the other against a growing electric field. The first charge element moves easily — there is no field yet — but each subsequent element must fight the field already established by the charge before it. The total work done to separate charge Q across voltage V is U = ½QV, not QV, because the voltage builds gradually from zero. This factor of one-half is the signature of any energy-storage process where the "resistance" increases as you fill the store.

The three formulas — **U = ½CV² = ½QV = Q²/(2C)** — are all equivalent, related through Q = CV. Which form to use depends on what you know. If you're given voltage and capacitance, use ½CV². If charge is specified, Q²/(2C) avoids substitution errors. All three express the same physical energy stored in the system. Importantly, doubling the voltage quadruples the stored energy (since U ∝ V²), which is why high-voltage capacitors store dramatically more energy than low-voltage ones of the same capacitance.

The deeper insight is *where* the energy lives. From the perspective of parallel-plate geometry, the electric field between the plates is uniform: E = V/d. Substituting Q = CV and C = ε₀A/d into U = Q²/(2C) and dividing by the volume Ad between the plates gives the **energy density**: u = ½ε₀E². This result says energy is stored in the field itself, distributed throughout the volume where the field exists — not concentrated on the charges at the plates. This field-centric view becomes essential when you extend to electromagnetic waves, where energy propagates through space with no charges involved at all.

The energy density u = ½ε₀E² holds not just for parallel-plate capacitors but for any electric field in free space. To find total energy in a nonuniform field, you integrate u over all space. For the uniform capacitor field this integral is trivial — u times volume — but for a point charge or a more complex geometry the field varies with position and the integral must be computed explicitly. This connection between the formula you derived for capacitors and the general electromagnetic field energy is one of the most satisfying unifications in electromagnetism.
