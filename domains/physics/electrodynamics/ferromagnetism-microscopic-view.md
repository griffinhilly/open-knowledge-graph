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
stage: advanced
status: draft
---

# Ferromagnetism: Microscopic Theory

## Core Idea
Ferromagnetism arises from exchange interaction between neighboring spins, creating aligned domains. Mean field theory explains spontaneous magnetization below the Curie temperature and the approach to saturation with applied field.

## Explainer

From your study of magnetic susceptibility and permeability, you know that ferromagnets are unusual: they acquire a large magnetization in an applied field and retain much of it when the field is removed. Ordinary **paramagnets** — where each atom's magnetic moment aligns independently with an external field — lose all magnetization immediately when the field turns off, because thermal fluctuations randomize the moments. Ferromagnetism requires something much stronger: a direct interaction between neighboring spins that makes them prefer to align parallel to each other even with no external field. The origin of this interaction is entirely quantum mechanical.

That interaction is the **exchange interaction**, arising from the Pauli exclusion principle and the antisymmetry of the electronic wavefunction. When electrons in neighboring atoms have parallel spins, the Pauli principle forces their spatial wavefunctions to be antisymmetric — keeping the electrons further apart on average and reducing their Coulomb repulsion energy. In ferromagnetic metals like iron, cobalt, and nickel, this energetic preference for spatial separation (and thus parallel spin alignment) is strong enough to dominate over thermal randomization at room temperature. The exchange coupling is written as −J **S**_i · **S**_j per pair, where J > 0 for ferromagnets; the minimum energy configuration is parallel alignment (S_i · S_j maximum). This quantum force is thousands of times stronger than classical dipole-dipole coupling between magnetic moments, which is far too weak to maintain ferromagnetic order at any practical temperature.

**Mean field theory** captures the collective behavior by replacing the complicated many-body problem with a tractable self-consistent one: each spin is assumed to feel an effective field H_eff proportional to the average magnetization M of all its neighbors. If M is large, H_eff is large, which drives further alignment, which sustains M — a self-reinforcing feedback. Solving the self-consistency equation gives a nonzero solution for M below the **Curie temperature** T_C, even at zero applied field. Above T_C, thermal energy kT overwhelms the exchange coupling and the spontaneous magnetization vanishes discontinuously — the material becomes a paramagnet. For iron, T_C ≈ 1043 K; a kitchen magnet placed in a hot flame loses its magnetism above this threshold.

Real ferromagnets are subdivided into **magnetic domains** — microscopic regions of uniform spin alignment, with neighboring domains pointing in different directions. A bulk sample thus appears unmagnetized even though each domain is fully magnetized internally. Domains form because, while exchange interaction favors large uniformly-magnetized regions, magnetostatic energy (the cost of maintaining a large external dipole field) favors smaller regions. Domain walls — thin transition layers where magnetization rotates from one domain's direction to another's — have an energy cost per unit area determined by the balance between exchange and anisotropy energies. When an external field is applied, domains aligned with the field grow at the expense of unfavorably oriented domains, primarily by domain wall motion. Irreversibilities in this motion — pinning of walls at grain boundaries, impurities, and defects — produce **hysteresis**: the magnetization curve depends on the history of applied fields, which is why permanent magnets retain their magnetization and why magnetic recording media can store bits.
