---
id: ferromagnetism-microscopic-view
title: 'Ferromagnetism: Microscopic Theory'
domain: physics
course: electrodynamics
prerequisites:
- id: magnetic-susceptibility-and-permeability
  type: hard
- id: mean-field-theory-statmech
  type: soft
builds-toward:
- magnetization-and-temperature
tags:
- ferromagnetism
- exchange-interaction
- domain-structure
stage: expert
status: validated
---

# Ferromagnetism: Microscopic Theory

## Core Idea
Ferromagnetism arises from exchange interaction between neighboring spins, creating aligned domains. Mean field theory explains spontaneous magnetization below the Curie temperature and the approach to saturation with applied field.

## Questions

```yaml
- question: "A student argues that ferromagnetism arises because adjacent magnetic dipoles attract and align each other, just as bar magnets do when placed nearby. What is wrong with this explanation?"
  type: multiple-choice
  options:
    - "Nothing — classical dipole-dipole interaction is the correct mechanism for ferromagnetism"
    - "Classical dipole-dipole coupling is thousands of times too weak to maintain spin alignment against thermal fluctuations at room temperature; the actual mechanism is quantum mechanical exchange interaction"
    - "The classical model is approximately correct but fails to account for domain structure"
    - "Dipoles would repel rather than attract in the geometry required for ferromagnetic alignment"
  answer: 1
  explanation: "Classical magnetic dipole-dipole coupling is far too weak to produce ferromagnetic order at any practical temperature. The actual mechanism is the quantum mechanical exchange interaction, arising from the Pauli exclusion principle: parallel spins keep electrons spatially separated on average, reducing Coulomb repulsion. This quantum effect is orders of magnitude stronger than classical dipole coupling and correctly predicts observed Curie temperatures. The student's classical picture is the most common misconception about ferromagnetism's microscopic origin."

- question: "A bulk iron sample at room temperature shows no net magnetic field. What is the most accurate explanation?"
  type: multiple-choice
  options:
    - "The exchange interaction averages to zero across the sample at room temperature"
    - "Iron is only ferromagnetic below its Curie temperature, and room temperature exceeds it"
    - "The sample is divided into magnetic domains, each fully magnetized internally but oriented in different directions, so the net external field cancels"
    - "Individual atomic moments are randomly oriented because thermal fluctuations override the exchange interaction at room temperature"
  answer: 2
  explanation: "A bulk iron sample consists of many magnetic domains, each region fully magnetized by the exchange interaction, but with neighboring domains pointing in different directions so the bulk net magnetization is near zero. Domain structure arises from the competition between exchange energy (favoring large aligned regions) and magnetostatic energy (favoring small regions to reduce the external dipole field). Option B is wrong — iron's Curie temperature is ~1043 K, far above room temperature. Option D describes paramagnets, not ferromagnets."

- question: "Above the Curie temperature, a ferromagnet becomes paramagnetic because the exchange interaction disappears."
  type: true-false
  answer: false
  explanation: "The exchange interaction is a quantum mechanical effect tied to the electronic structure of the material; it does not simply disappear above T_C. What changes is the balance between the exchange coupling and thermal fluctuations. Above T_C, thermal energy kT becomes large enough to randomize spin orientations despite the exchange coupling, destroying long-range magnetic order. The interaction is still present — it simply loses the competition with thermal disorder."

- question: "Hysteresis in a ferromagnet — where the magnetization depends on the history of applied fields — arises from domain wall pinning at crystal defects."
  type: true-false
  answer: true
  explanation: "When an external field is applied, favorably oriented domains grow by domain wall motion at the expense of unfavorably oriented ones. Domain walls can become pinned at grain boundaries, dislocations, impurities, and other crystal defects. Pinning means wall motion requires energy to overcome barriers, causing magnetization to lag behind changes in the applied field. When the field is removed, walls do not fully return to their original positions, leaving residual magnetization. This irreversibility is hysteresis."

- question: "Why do magnetic domains form in a ferromagnetic material, given that exchange interaction alone would favor complete alignment of all spins?"
  type: short-answer
  answer: "Exchange interaction alone would favor a single uniformly magnetized domain, but a large uniformly magnetized body generates a large external magnetic dipole field with high magnetostatic energy. The system minimizes total energy — exchange plus magnetostatic — by breaking into smaller domains pointing in different directions, which cancel each other's external fields. Domain walls separating adjacent domains have their own energy cost from the exchange and anisotropy energies needed to rotate spins through the transition region. The equilibrium domain structure reflects a balance between these competing energy terms."
  explanation: "Ferromagnetism is fundamentally a competition between two energy scales: exchange (favoring large aligned regions) and magnetostatic (favoring small regions to reduce external field energy). Neither wins completely, producing a domain mosaic. This competition also explains why applied fields gradually realign domains (domain wall motion), why pinning produces hysteresis, and why permanent magnets retain magnetization after the applied field is removed."
```

## Explainer

From your study of magnetic susceptibility and permeability, you know that ferromagnets are unusual: they acquire a large magnetization in an applied field and retain much of it when the field is removed. Ordinary **paramagnets** — where each atom's magnetic moment aligns independently with an external field — lose all magnetization immediately when the field turns off, because thermal fluctuations randomize the moments. Ferromagnetism requires something much stronger: a direct interaction between neighboring spins that makes them prefer to align parallel to each other even with no external field. The origin of this interaction is entirely quantum mechanical.

That interaction is the **exchange interaction**, arising from the Pauli exclusion principle and the antisymmetry of the electronic wavefunction. When electrons in neighboring atoms have parallel spins, the Pauli principle forces their spatial wavefunctions to be antisymmetric — keeping the electrons further apart on average and reducing their Coulomb repulsion energy. In ferromagnetic metals like iron, cobalt, and nickel, this energetic preference for spatial separation (and thus parallel spin alignment) is strong enough to dominate over thermal randomization at room temperature. The exchange coupling is written as −J **S**_i · **S**_j per pair, where J > 0 for ferromagnets; the minimum energy configuration is parallel alignment (S_i · S_j maximum). This quantum force is thousands of times stronger than classical dipole-dipole coupling between magnetic moments, which is far too weak to maintain ferromagnetic order at any practical temperature.

**Mean field theory** captures the collective behavior by replacing the complicated many-body problem with a tractable self-consistent one: each spin is assumed to feel an effective field H_eff proportional to the average magnetization M of all its neighbors. If M is large, H_eff is large, which drives further alignment, which sustains M — a self-reinforcing feedback. Solving the self-consistency equation gives a nonzero solution for M below the **Curie temperature** T_C, even at zero applied field. Above T_C, thermal energy kT overwhelms the exchange coupling and the spontaneous magnetization vanishes discontinuously — the material becomes a paramagnet. For iron, T_C ≈ 1043 K; a kitchen magnet placed in a hot flame loses its magnetism above this threshold.

Real ferromagnets are subdivided into **magnetic domains** — microscopic regions of uniform spin alignment, with neighboring domains pointing in different directions. A bulk sample thus appears unmagnetized even though each domain is fully magnetized internally. Domains form because, while exchange interaction favors large uniformly-magnetized regions, magnetostatic energy (the cost of maintaining a large external dipole field) favors smaller regions. Domain walls — thin transition layers where magnetization rotates from one domain's direction to another's — have an energy cost per unit area determined by the balance between exchange and anisotropy energies. When an external field is applied, domains aligned with the field grow at the expense of unfavorably oriented domains, primarily by domain wall motion. Irreversibilities in this motion — pinning of walls at grain boundaries, impurities, and defects — produce **hysteresis**: the magnetization curve depends on the history of applied fields, which is why permanent magnets retain their magnetization and why magnetic recording media can store bits.
