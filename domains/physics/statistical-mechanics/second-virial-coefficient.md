---
id: second-virial-coefficient
title: Second Virial Coefficient
domain: physics
course: statistical-mechanics
prerequisites:
- id: virial-coefficients-interaction
  type: hard
builds-toward:
- van-der-waals-derivation
tags:
- interactions
- two-body
- non-ideal
stage: expert
status: validated
---

# Second Virial Coefficient

## Core Idea
The second virial coefficient B₂(T) represents the leading correction to ideal behavior and reflects two-body interactions. It changes sign at the Boyle temperature where it vanishes, and its temperature dependence reveals the balance between repulsive and attractive forces in intermolecular interactions.

## Questions

```yaml
- question: "A gas is studied at its Boyle temperature. A chemist concludes that 'the gas behaves ideally at this temperature because intermolecular forces cancel out.' What is wrong with this conclusion?"
  type: multiple-choice
  options:
    - "The Boyle temperature is where B₂ is at its maximum, not zero"
    - "Intermolecular forces do not actually cancel — B₂ = 0 is a coincidental balance of repulsive and attractive contributions to the integral, not an absence of forces"
    - "The gas behaves ideally at all temperatures, not just the Boyle temperature"
    - "At the Boyle temperature, only repulsive forces remain, so the gas is not truly ideal"
  answer: 1
  explanation: "B₂(T_B) = 0 means that the positive contribution from short-range repulsion and the negative contribution from attractive interactions in the integral ∫[exp(−u(r)/kT) − 1] 4πr² dr happen to cancel exactly. Intermolecular forces are still very much present — the Mayer f-function is nonzero at many separations. The gas obeys PV = NkT to first order, but this is a cancellation, not absence of interactions. Higher-order virial terms (B₃, etc.) are still nonzero."

- question: "At low temperatures, B₂(T) is negative. What physical process causes this?"
  type: multiple-choice
  options:
    - "At low temperatures, molecular velocities are too low for molecules to collide, so there is no repulsive contribution"
    - "The hard-core repulsion disappears at low temperatures because kT is small"
    - "The attractive potential well becomes significant relative to kT, causing molecules to linger near each other and reducing pressure below the ideal value"
    - "Low temperatures reduce molecular volume, making the ideal gas approximation more accurate and B₂ smaller"
  answer: 2
  explanation: "B₂(T) = −½ ∫ f(r) 4πr² dr, where f(r) = exp(−u(r)/kT) − 1. At low temperatures, kT is small relative to the depth of the attractive well |ε|, so exp(−u(r)/kT) >> 1 in the attractive region, making f(r) large and positive. This positive integrand dominates the negative contribution from the repulsive core, making B₂ < 0. Physically: molecules slow down, spend more time in each other's attractive well, and the average pressure is reduced below the ideal value."

- question: "A gas with B₂ = 0 at its Boyle temperature has no intermolecular interactions at that temperature."
  type: true-false
  answer: false
  explanation: "B₂ = 0 does not mean the intermolecular potential u(r) is zero. The integral ∫[exp(−u(r)/kT) − 1] 4πr² dr = 0 because the positive contribution from repulsive interactions (short distances) and the negative contribution from attractive interactions (intermediate distances) exactly cancel. The forces are fully operative — this is a mathematical cancellation in the virial coefficient, not an absence of molecular interactions."

- question: "At high temperatures, the second virial coefficient B₂(T) is typically positive because repulsive interactions dominate."
  type: true-false
  answer: true
  explanation: "At high temperatures, kT >> |u(r)| for the attractive well, so the Mayer f-function in the attractive region is approximately zero (the exponential collapses to near 1). Only the hard-core repulsive region contributes significantly: there, u(r) >> kT makes exp(−u(r)/kT) ≈ 0, so f(r) ≈ −1, contributing a positive term to B₂ (since B₂ = −½ ∫ f(r) 4πr² dr). The result is B₂ > 0, meaning pressure exceeds the ideal prediction — molecules effectively exclude each other's volume."

- question: "Why is measuring B₂(T) at many temperatures more useful than a single measurement, and what can be learned from its temperature dependence?"
  type: short-answer
  answer: "B₂(T) as a function of temperature encodes the shape of the intermolecular pair potential u(r). At different temperatures, different regions of u(r) dominate: high-T data constrain the repulsive core, low-T data constrain the attractive well, and T_B constrains where the two contributions balance. By fitting a model potential (such as the Lennard-Jones potential) to B₂(T) data across temperatures, one can extract molecular parameters ε (well depth) and σ (effective diameter) that cannot easily be measured directly."
  explanation: "This is the key bridge B₂(T) provides between macroscopic thermodynamic measurements and microscopic molecular physics. A single B₂ value at one temperature is just a correction factor; a full B₂(T) curve is a fingerprint of the intermolecular potential. This is why Lennard-Jones potential parameters were historically refined by fitting to B₂(T) datasets rather than from direct force measurements."
```

## Explainer

The virial expansion writes the pressure of a real gas as a power series in density: PV/NkT = 1 + B₂(T)/V + B₃(T)/V² + …, where each **virial coefficient** captures the effect of increasingly complex multi-particle encounters. The ideal gas result (1) corresponds to particles that never interact. The **second virial coefficient** B₂(T) is the first correction and accounts for two-body interactions — collisions between pairs of molecules. At low enough densities, three-body encounters (B₃) are so rare that they can be ignored, making B₂ the dominant correction in most practical situations.

B₂(T) has a statistical mechanical expression: B₂(T) = −½ ∫ [exp(−u(r)/kT) − 1] 4πr² dr, where u(r) is the pair potential — the interaction energy between two molecules separated by distance r. The integrand, known as the **Mayer f-function** f(r) = exp(−u(r)/kT) − 1, vanishes when molecules don't interact (u = 0) and is nonzero only where they do. At short distances, repulsive interactions (u >> kT) make f(r) ≈ −1, contributing a positive term to B₂. At intermediate distances, attractive interactions (u < 0) make f(r) > 0, contributing a negative term. The sign and magnitude of B₂ reflect which effect dominates.

At high temperatures, kT >> |u(r)|, so the attractive well has negligible effect. The hard-core repulsion dominates, making B₂ > 0 — the gas behaves as if molecules simply exclude each other's volume, so pressure is higher than ideal (PV > NkT). At low temperatures, the attractive well matters: molecules linger near each other, reducing the effective pressure below ideal, making B₂ < 0. The **Boyle temperature** T_B is where B₂(T_B) = 0 — repulsive and attractive corrections exactly cancel, and the gas obeys PV = NkT to first order regardless of density. This is not because the gas is ideal; it is a coincidental cancellation. Real gases like nitrogen have T_B ≈ 327 K and are studied near this temperature to isolate higher-order effects.

The practical value of B₂(T) goes beyond corrections to the ideal gas law. Its temperature dependence is a fingerprint of the intermolecular potential u(r): measuring B₂(T) at many temperatures can be used to infer the shape of u(r) without directly measuring molecular forces. The Lennard-Jones potential u(r) = 4ε[(σ/r)¹² − (σ/r)⁶] — with its characteristic hard-core repulsion and shallow attractive well — was refined historically by fitting its parameters ε and σ to experimental B₂(T) data. The second virial coefficient thus bridges macroscopic thermodynamic measurements and microscopic molecular physics.
