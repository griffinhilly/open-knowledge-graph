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
stage: expert
status: draft
---

# Virial Theorem

## Core Idea
The virial theorem relates the average kinetic energy ⟨K⟩ to the average potential energy ⟨V⟩ for power-law interactions V ∝ r^n: 2⟨K⟩ = n⟨V⟩. For gravity (n=−1), this gives 2⟨K⟩ + ⟨V⟩ = 0, connecting gravitational binding to temperature. For the ideal gas (no interactions), it implies the equipartition theorem.

## Questions

```yaml
- question: "A young star is contracting under gravity and radiating energy into space. According to the virial theorem, what happens to the star's core temperature as it contracts and loses total energy?"
  type: multiple-choice
  options:
    - "It cools down, because energy is being radiated away and the star has less energy available for heat"
    - "It stays constant, because energy radiated out is exactly compensated by gravitational contraction energy"
    - "It increases, because the virial theorem for gravity gives 2⟨K⟩ = −⟨V⟩, so as ⟨V⟩ becomes more negative, kinetic energy — and hence temperature — must increase"
    - "It depends entirely on whether the star is in hydrostatic equilibrium"
  answer: 2
  explanation: "For gravity (n = −1), the virial theorem gives 2⟨K⟩ = −⟨V⟩. As the star contracts, gravitational potential energy ⟨V⟩ becomes more negative. By the virial theorem, ⟨K⟩ = −⟨V⟩/2 must increase — and since kinetic energy is proportional to temperature, the star heats up even as it loses total energy. Half the liberated gravitational energy is radiated away; the other half heats the gas. This 'negative heat capacity' is counterintuitive but follows directly from the virial theorem."

- question: "For an ideal gas (no interparticle interactions), the virial theorem reduces to which standard result?"
  type: multiple-choice
  options:
    - "The van der Waals equation of state, which corrects for molecular interactions"
    - "The Carnot efficiency limit for heat engines"
    - "The equipartition theorem: each translational degree of freedom carries (1/2)k_BT of kinetic energy"
    - "The Boltzmann H-theorem describing entropy increase"
  answer: 2
  explanation: "For an ideal gas, there are no pairwise interactions — all virial coefficients B_k = 0. The only forces are from the container walls. Applying the virial theorem to these wall interactions recovers the equipartition result: total kinetic energy ⟨K⟩ = (3/2)Nk_BT for a monatomic gas in three dimensions. The virial expansion P = nk_BT(1 + B₂n + …) then provides correction terms for real gases, where each virial coefficient encodes k-body interaction contributions."

- question: "For a gravitationally bound system in equilibrium, the total energy E equals the negative of the time-averaged kinetic energy: E = −⟨K⟩."
  type: true-false
  answer: true
  explanation: "From the virial theorem with n = −1: 2⟨K⟩ = −⟨V⟩, so ⟨V⟩ = −2⟨K⟩. Total energy E = ⟨K⟩ + ⟨V⟩ = ⟨K⟩ − 2⟨K⟩ = −⟨K⟩. Since ⟨K⟩ > 0, E < 0 — gravitationally bound systems always have negative total energy. This also implies negative heat capacity: adding energy (making E less negative) decreases ⟨K⟩ and therefore cools the system, while removing energy increases ⟨K⟩ and heats it."

- question: "When a cloud of gas collapses under gravity, it cools because it radiates most of the released gravitational potential energy into space."
  type: true-false
  answer: false
  explanation: "By the virial theorem (n = −1): 2⟨K⟩ = −⟨V⟩. As the cloud collapses, ⟨V⟩ becomes more negative, so ⟨K⟩ — and thus temperature — increases. Roughly half the released gravitational potential energy is radiated away, but the other half goes into heating the gas. This is why collapsing gas clouds heat up rather than cooling, and why proto-stellar nebulae eventually ignite as stars. Losing energy → getting hotter is the signature of gravitational negative heat capacity."

- question: "Explain in your own words why gravitationally bound systems have 'negative heat capacity' — why removing energy from such a system causes it to heat up."
  type: short-answer
  answer: "The virial theorem for gravity requires 2⟨K⟩ = −⟨V⟩ in equilibrium. Total energy is E = ⟨K⟩ + ⟨V⟩ = ⟨K⟩ − 2⟨K⟩ = −⟨K⟩. If the system radiates energy (E decreases, becomes more negative), then −⟨K⟩ must decrease, meaning ⟨K⟩ must increase. Since temperature is proportional to kinetic energy, the system heats up when it loses energy. This is the opposite of ordinary systems like an ideal gas, where adding energy increases temperature. The virial theorem's constraint — that gravity forces kinetic and potential energies to maintain a fixed ratio — is what produces this counterintuitive behavior."
  explanation: "The result has profound astrophysical consequences: stars heat up as they radiate and contract, proto-stellar clouds ignite as they collapse, and gravitationally bound clusters cannot 'cool' in the ordinary sense. It also explains the stability of stars: as they radiate, they contract and heat their cores, eventually reaching pressures sufficient to sustain fusion — a self-regulating process driven by the virial theorem."
```

## Explainer

The virial theorem is a powerful and general result connecting the time-averaged kinetic and potential energies of a system in stable equilibrium. Its breadth is remarkable: it applies equally to a planetary system, a gas of interacting molecules, a self-gravitating star, and a galaxy cluster. From your work with the partition function, you've seen how statistical averages encode thermodynamic quantities; the virial theorem provides an energy relation at a higher level of abstraction, connecting averages without requiring the full partition function or microstate enumeration.

The classical derivation starts from Newton's second law applied to all particles and forms the time average of the quantity G = Σᵢ rᵢ · pᵢ (the "virial"). In a bounded, stable system, the time average of dG/dt is zero. Working through the algebra yields **2⟨K⟩ = −Σᵢ ⟨rᵢ · Fᵢ⟩**, where the right side is the total virial of the forces. For a power-law pair potential V(r) ∝ r^n, the force scales as r^{n−1}, and the virial evaluates to n⟨V⟩, giving the compact result 2⟨K⟩ = n⟨V⟩.

The gravitational case (n = −1) has profound astrophysical consequences. The theorem gives 2⟨K⟩ = −⟨V⟩, so the total energy E = ⟨K⟩ + ⟨V⟩ = −⟨K⟩. As a self-gravitating gas cloud collapses under its own gravity, it loses total energy (half radiated away), while the kinetic energy — and hence temperature — *increases*: stars heat up as they collapse. This "gravitational thermodynamics" is deeply counterintuitive but follows directly from the virial theorem. It also means that gravitationally bound systems have **negative heat capacity**: adding energy causes them to cool, while removing energy causes them to heat up.

In statistical mechanics, the virial theorem is the foundation of the **virial expansion** for non-ideal gases: P = nk_BT(1 + B₂(T)n + B₃(T)n² + …), where each virial coefficient B_k encodes k-body interaction contributions. For the ideal gas, all B_k = 0 and the virial theorem reduces to the statement that 2⟨K⟩ = 3Nk_BT — exactly the equipartition result. The second virial coefficient B₂ for a van der Waals gas captures the competition between the attractive well and the repulsive hard core of molecular interactions, connecting microscopic pair potentials to measurable deviations from ideal gas behavior.
