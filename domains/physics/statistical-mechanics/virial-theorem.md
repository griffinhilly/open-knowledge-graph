---
id: virial-theorem
title: Virial Theorem
domain: physics
course: statistical-mechanics
prerequisites:
- id: partition-function-definition
  type: hard
tags:
- theorem
- energy-relations
- interactions
stage: advanced
status: draft
---

# Virial Theorem

## Core Idea
The virial theorem relates the average kinetic energy ⟨K⟩ to the average potential energy ⟨V⟩ for power-law interactions V ∝ r^n: 2⟨K⟩ = n⟨V⟩. For gravity (n=−1), this gives 2⟨K⟩ + ⟨V⟩ = 0, connecting gravitational binding to temperature. For the ideal gas (no interactions), it implies the equipartition theorem.

## Explainer

The virial theorem is a powerful and general result connecting the time-averaged kinetic and potential energies of a system in stable equilibrium. Its breadth is remarkable: it applies equally to a planetary system, a gas of interacting molecules, a self-gravitating star, and a galaxy cluster. From your work with the partition function, you've seen how statistical averages encode thermodynamic quantities; the virial theorem provides an energy relation at a higher level of abstraction, connecting averages without requiring the full partition function or microstate enumeration.

The classical derivation starts from Newton's second law applied to all particles and forms the time average of the quantity G = Σᵢ rᵢ · pᵢ (the "virial"). In a bounded, stable system, the time average of dG/dt is zero. Working through the algebra yields **2⟨K⟩ = −Σᵢ ⟨rᵢ · Fᵢ⟩**, where the right side is the total virial of the forces. For a power-law pair potential V(r) ∝ r^n, the force scales as r^{n−1}, and the virial evaluates to n⟨V⟩, giving the compact result 2⟨K⟩ = n⟨V⟩.

The gravitational case (n = −1) has profound astrophysical consequences. The theorem gives 2⟨K⟩ = −⟨V⟩, so the total energy E = ⟨K⟩ + ⟨V⟩ = −⟨K⟩. As a self-gravitating gas cloud collapses under its own gravity, it loses total energy (half radiated away), while the kinetic energy — and hence temperature — *increases*: stars heat up as they collapse. This "gravitational thermodynamics" is deeply counterintuitive but follows directly from the virial theorem. It also means that gravitationally bound systems have **negative heat capacity**: adding energy causes them to cool, while removing energy causes them to heat up.

In statistical mechanics, the virial theorem is the foundation of the **virial expansion** for non-ideal gases: P = nk_BT(1 + B₂(T)n + B₃(T)n² + …), where each virial coefficient B_k encodes k-body interaction contributions. For the ideal gas, all B_k = 0 and the virial theorem reduces to the statement that 2⟨K⟩ = 3Nk_BT — exactly the equipartition result. The second virial coefficient B₂ for a van der Waals gas captures the competition between the attractive well and the repulsive hard core of molecular interactions, connecting microscopic pair potentials to measurable deviations from ideal gas behavior.
