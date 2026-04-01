---
id: amperes-law
title: Ampère's Law
domain: physics
course: electricity-and-magnetism
prerequisites:
- id: biot-savart-law
  type: hard
- id: dot-product
  type: hard
- id: line-integrals-vector-fields
  type: soft
- id: curl-and-divergence
  type: soft
- id: curl-and-divergence-operators
  type: hard
builds-toward:
- maxwells-equations-overview
- magnetic-flux-and-induction
tags:
- Ampere-law
- solenoid
- toroid
- symmetry
- magnetostatics
stage: formal-systems
status: validated
---

# Ampère's Law

## Core Idea
Ampère's law states that the line integral of B around any closed Amperian loop equals μ₀ times the total current enclosed: ∮ B · dl = μ₀I_enc. It is the magnetic analog of Gauss's law — mathematically equivalent to Biot-Savart for steady currents but far more powerful when symmetry is present. It is used to find B inside a solenoid (B = μ₀nI), a toroid, or near a long straight wire without integration.

## How It's Best Learned
Study the three canonical applications: infinite straight wire, infinite solenoid, and toroid. For each, identify the Amperian loop shape (circle or rectangle) that exploits symmetry to simplify ∮ B · dl before evaluating I_enc.

## Common Misconceptions
- Like Gauss's law for E, Ampère's law is always valid but only simplifies calculation when symmetry exists.
- For a solenoid, B outside is approximately zero, not because of shielding but because of field cancellation from all loops.
- Ampère's law in this form applies only to magnetostatics; Maxwell added the displacement current term to generalize it.

## Questions

```yaml
- question: "You want to find the magnetic field inside an infinite solenoid using Ampère's law. Which Amperian loop shape is most appropriate, and why?"
  type: multiple-choice
  options: ["A circle concentric with the solenoid cross-section, because B is radial", "A rectangular loop with one side inside and one side outside the solenoid, because B is uniform inside and zero outside", "A circular loop outside the solenoid, because all the current is enclosed", "A sphere enclosing the solenoid, to capture the full flux"]
  answer: 1
  explanation: "For a solenoid, B inside is uniform and parallel to the axis; B outside is approximately zero. A rectangular Amperian loop with one long side inside (where B · dl = BL) and one long side outside (where B · dl = 0) lets you write ∮ B · dl = BL = μ₀ n L I, giving B = μ₀nI. A circular loop does not exploit the geometry correctly because B is axial, not azimuthal."

- question: "Ampère's law (∮ B · dl = μ₀I_enc) is only valid when the current distribution has a high degree of symmetry."
  type: true-false
  answer: false
  explanation: "Ampère's law is always valid for steady currents — it is an exact law of magnetostatics, true for any current distribution and any closed loop. The symmetry requirement applies to practical calculation: the integral ∮ B · dl simplifies to BL or B(2πr) only when symmetry guarantees B is constant in magnitude and parallel to dl along the chosen loop. Without symmetry, the integral is too complex to evaluate analytically, so Biot-Savart is used instead."

- question: "Explain the analogy between Ampère's law and Gauss's law, and what condition both laws require for practical use."
  type: short-answer
  answer: "Both laws relate a field integrated over a closed surface or loop to the source enclosed: Gauss's law relates the electric flux through a closed surface to the enclosed charge (∮ E · dA = Q_enc/ε₀), while Ampère's law relates the line integral of B around a closed loop to the enclosed current (∮ B · dl = μ₀I_enc). Both are always mathematically valid, but both simplify to usable algebraic equations only when symmetry makes the field constant and aligned with the integration path or surface."
  explanation: "The structural parallel is deep: Gauss's law uses a closed surface (Gaussian surface) and a volume integral of charge; Ampère's law uses a closed loop (Amperian loop) and a line integral of current. In both cases, the law itself does not depend on symmetry — it is an identity. Symmetry is required to pull the field outside the integral sign, reducing ∮ B · dl to B × (path length) or ∮ E · dA to E × (area)."
```

## Explainer

When you learned the Biot-Savart law, you could calculate the magnetic field from any current distribution — in principle. In practice, the vector integral is demanding: for each infinitesimal current element you compute a cross product, then integrate over the entire current path. Ampère's law offers a dramatically simpler route for symmetric configurations, analogous to the relationship between Coulomb's law and Gauss's law in electrostatics.

Ampère's law states that the line integral of B around any closed loop equals μ₀ times the total current threading through the loop: ∮ B · dl = μ₀I_enc. Like Gauss's law, this is always true — it is an exact statement of magnetostatics, not an approximation. The integral on the left sums up B · dl along the chosen path, and I_enc counts all currents passing through any surface bounded by that loop. The freedom to choose any loop is what makes the law powerful.

The strategy is the same as for Gauss's law: choose an Amperian loop whose geometry matches the symmetry of the current distribution so that B is constant in magnitude and parallel (or perpendicular) to dl everywhere on the loop. For a long straight wire, a circular loop of radius r centered on the wire gives ∮ B · dl = B(2πr), immediately yielding B = μ₀I/(2πr). For an infinite solenoid, a rectangular loop with one side inside and one outside gives BL = μ₀nIL, so B = μ₀nI inside and zero outside — the same result that would require a much harder Biot-Savart integration.

It is worth being precise about what "symmetry is required" means. Ampère's law is not a tool that "only works with symmetry" — it is always correct. The symmetry requirement is about calculation: without it, B is not constant along the loop, the integral cannot be factored, and you cannot extract B analytically. For asymmetric configurations, Biot-Savart remains the tool of choice.

Finally, the version of Ampère's law here (∮ B · dl = μ₀I_enc) applies only to magnetostatics — steady, non-changing currents. Maxwell's great insight was that changing electric fields also produce magnetic fields, and he added a displacement current term (μ₀ε₀ dΦ_E/dt) to generalize the law. This modified form is one of Maxwell's four equations and is the foundation of electromagnetic wave theory.
