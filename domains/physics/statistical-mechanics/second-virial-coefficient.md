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
stage: advanced
status: draft
---

# Second Virial Coefficient

## Core Idea
The second virial coefficient B₂(T) represents the leading correction to ideal behavior and reflects two-body interactions. It changes sign at the Boyle temperature where it vanishes, and its temperature dependence reveals the balance between repulsive and attractive forces in intermolecular interactions.

## Explainer

The virial expansion writes the pressure of a real gas as a power series in density: PV/NkT = 1 + B₂(T)/V + B₃(T)/V² + …, where each **virial coefficient** captures the effect of increasingly complex multi-particle encounters. The ideal gas result (1) corresponds to particles that never interact. The **second virial coefficient** B₂(T) is the first correction and accounts for two-body interactions — collisions between pairs of molecules. At low enough densities, three-body encounters (B₃) are so rare that they can be ignored, making B₂ the dominant correction in most practical situations.

B₂(T) has a statistical mechanical expression: B₂(T) = −½ ∫ [exp(−u(r)/kT) − 1] 4πr² dr, where u(r) is the pair potential — the interaction energy between two molecules separated by distance r. The integrand, known as the **Mayer f-function** f(r) = exp(−u(r)/kT) − 1, vanishes when molecules don't interact (u = 0) and is nonzero only where they do. At short distances, repulsive interactions (u >> kT) make f(r) ≈ −1, contributing a positive term to B₂. At intermediate distances, attractive interactions (u < 0) make f(r) > 0, contributing a negative term. The sign and magnitude of B₂ reflect which effect dominates.

At high temperatures, kT >> |u(r)|, so the attractive well has negligible effect. The hard-core repulsion dominates, making B₂ > 0 — the gas behaves as if molecules simply exclude each other's volume, so pressure is higher than ideal (PV > NkT). At low temperatures, the attractive well matters: molecules linger near each other, reducing the effective pressure below ideal, making B₂ < 0. The **Boyle temperature** T_B is where B₂(T_B) = 0 — repulsive and attractive corrections exactly cancel, and the gas obeys PV = NkT to first order regardless of density. This is not because the gas is ideal; it is a coincidental cancellation. Real gases like nitrogen have T_B ≈ 327 K and are studied near this temperature to isolate higher-order effects.

The practical value of B₂(T) goes beyond corrections to the ideal gas law. Its temperature dependence is a fingerprint of the intermolecular potential u(r): measuring B₂(T) at many temperatures can be used to infer the shape of u(r) without directly measuring molecular forces. The Lennard-Jones potential u(r) = 4ε[(σ/r)¹² − (σ/r)⁶] — with its characteristic hard-core repulsion and shallow attractive well — was refined historically by fitting its parameters ε and σ to experimental B₂(T) data. The second virial coefficient thus bridges macroscopic thermodynamic measurements and microscopic molecular physics.
