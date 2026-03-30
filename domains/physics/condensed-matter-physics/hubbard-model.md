---
id: hubbard-model
title: Hubbard Model
domain: physics
course: condensed-matter-physics
prerequisites:
- id: tight-binding-model
  type: hard
- id: fermi-liquid-theory
  type: soft
tags:
- hubbard-model
- electron-correlation
- mott-transition
- strongly-correlated
stage: expert
status: validated
---

# Hubbard Model

## Core Idea
The Hubbard model is the simplest model of interacting electrons on a lattice: H = -t sum_{<ij>,sigma} c^dagger_{i,sigma} c_{j,sigma} + U sum_i n_{i,up} n_{i,down}. The first term is nearest-neighbor hopping (kinetic energy, bandwidth W ~ zt), and the second penalizes double occupancy of any site by Coulomb repulsion U. The competition between kinetic energy (which delocalizes electrons) and interaction energy (which localizes them) produces a rich phase diagram including metallic, Mott insulating, antiferromagnetic, and (in some geometries) superconducting phases. At half-filling with U >> t, the model reduces to the Heisenberg antiferromagnet. The Hubbard model is believed to capture the essential physics of high-temperature superconductivity in the cuprates.

## Questions

```yaml
- question: "The Hubbard model with only two parameters (t and U) produces metals, Mott insulators, antiferromagnets, and possibly superconductors. Why is it considered the 'standard model' of strongly correlated electron physics?"
  type: multiple-choice
  options:
    - "Because it can be solved exactly in all cases"
    - "It captures the minimal essential competition: kinetic energy (t) favors delocalization and metallic behavior; on-site repulsion (U) favors localization and magnetic order. This single competition, combined with the geometry of the lattice and the electron filling, is sufficient to produce the major phenomena of correlated-electron physics. Despite its simplicity, the model remains unsolved in 2D and 3D, and understanding its phase diagram is one of the great open problems in theoretical physics"
    - "It includes all the interactions present in real materials"
    - "It was derived directly from the Schrodinger equation for copper oxide materials"
  answer: 1
  explanation: "The Hubbard model is the minimal model that includes both itinerant (band-like) and localized (atomic-like) tendencies of electrons. For U = 0, it reduces to the tight-binding model (free electrons in bands). For t = 0, it gives isolated atoms. The crossover between these limits — and the phases that emerge in between — contains the physics of Mott insulators, magnetic ordering, heavy fermions (in extended versions), and potentially unconventional superconductivity. Its importance parallels the Ising model in statistical mechanics: it is simple enough to define precisely but rich enough to exhibit non-trivial emergent behavior."

- question: "At half-filling (one electron per site on average) with U >> t, why does the Hubbard model become an insulator even though band theory predicts a metal (half-filled band)?"
  type: multiple-choice
  options:
    - "The crystal structure changes at large U"
    - "When U >> t, the energy cost of double occupancy (~U) far exceeds the kinetic energy gain (~t) from hopping. Each site is singly occupied, and electrons cannot hop without creating an energetically costly doubly-occupied site. The electrons are effectively frozen in place — a Mott insulator with a charge gap of order U, despite having a half-filled band that band theory says should be metallic"
    - "The Pauli exclusion principle prevents more than one electron per site"
    - "Disorder localizes the electrons in the strong-coupling limit"
  answer: 1
  explanation: "This is the Mott insulating state — a failure of band theory. Band theory treats electrons as non-interacting and predicts that a half-filled band is metallic. The Hubbard model shows that strong Coulomb repulsion can localize electrons even in a partially filled band, opening a correlation-driven gap. In the Mott insulator, each site has exactly one electron, and the residual exchange coupling (J ~ t²/U, second-order hopping) produces an antiferromagnetic Heisenberg model. This explains why many transition metal oxides (NiO, CoO, V₂O₃) are insulators despite having partially filled d-bands."

- question: "The 2D Hubbard model on a square lattice is widely believed to describe the essential physics of cuprate high-temperature superconductors. Why can't it be solved exactly?"
  type: true-false
  answer: true
  explanation: "The 2D Hubbard model is exactly solvable only in 1D (via the Bethe ansatz) and in infinite dimensions (via dynamical mean-field theory). In 2D — the relevant dimension for cuprate physics — there is no exact solution. The minus sign problem makes quantum Monte Carlo exponentially expensive for fermions away from half-filling. Approximate methods (DMFT, variational Monte Carlo, tensor networks, diagrammatic techniques) give conflicting predictions for the phase diagram, particularly regarding whether the doped Hubbard model supports d-wave superconductivity. This is considered one of the most important unsolved problems in theoretical physics, directly relevant to understanding high-T_c superconductivity."

- question: "In the limit U >> t at half-filling, the Hubbard model reduces to the Heisenberg antiferromagnet with exchange coupling J = 4t²/U. Derive the physical origin of this mapping."
  type: short-answer
  answer: "At half-filling with U >> t, each site is singly occupied and direct hopping is suppressed (it would create a doubly-occupied site costing energy U). However, virtual hopping is allowed in second-order perturbation theory: an electron hops to a neighbor (creating a doublon, energy cost U), then hops back (energy recovered). This virtual process has amplitude t²/U and is only possible when the two neighboring spins are antiparallel (Pauli exclusion forbids hopping to a same-spin site). The effective Hamiltonian for the spin degrees of freedom is H_eff = J Σ_{<ij>} (S_i · S_j - 1/4) with J = 4t²/U > 0, which is the antiferromagnetic Heisenberg model. The factor of 4 comes from the two possible intermediate states (either electron can hop)."
  explanation: "This mapping is a canonical example of 'integrating out high-energy degrees of freedom.' The charge fluctuations (energy scale U) are frozen out, leaving only spin fluctuations (energy scale J = 4t²/U << U). It explains why so many Mott insulators are antiferromagnets and provides the starting point for understanding doped Mott insulators (cuprate superconductors)."
```

## Explainer

The **Hubbard model** is to strongly correlated electron physics what the Ising model is to statistical mechanics: the simplest possible model that captures the essential competition. It was introduced independently by Hubbard, Gutzwiller, and Kanamori in 1963, and it contains just two parameters. The hopping integral **t** measures the amplitude for an electron to tunnel between neighboring sites (kinetic energy, favoring delocalization). The on-site repulsion **U** penalizes having two electrons (with opposite spins) on the same site (interaction energy, favoring localization). The tension between these two tendencies produces the rich physics of correlated electrons.

For **U = 0**, the Hubbard model is just the tight-binding model — non-interacting electrons forming energy bands. Band theory says a half-filled band is metallic. For **U >> t** at half-filling, every site is singly occupied and charge fluctuations are frozen out — the system is a **Mott insulator** with a charge gap of order U. This is the fundamental failure mode of band theory: interactions can make an insulator out of what band theory predicts is a metal. Transition metal oxides like NiO, CoO, and V_2O_3 are Mott insulators, and their insulating behavior puzzled physicists until Mott's insight that Coulomb correlations are responsible.

In the Mott insulating limit (U >> t, half-filling), the remaining degree of freedom is the spin on each site. Virtual hopping processes (electron hops to a neighbor and back, through a high-energy doubly-occupied intermediate state) generate an effective antiferromagnetic exchange J = 4t^2/U between neighboring spins. The half-filled Hubbard model at large U thus maps onto the **Heisenberg antiferromagnet**, explaining why Mott insulators are so often antiferromagnetically ordered. This connection between charge localization and magnetic ordering is one of the central insights of correlated electron physics.

The most exciting and unsolved regime is the **doped Mott insulator**: start from the half-filled Mott state and remove some electrons (or add some holes). The doped holes can move through the antiferromagnetic background, disrupting the magnetic order. In the 2D Hubbard model on a square lattice, there is strong numerical and analytical evidence that the doped system develops **d-wave superconductivity** — the same symmetry observed in cuprate high-T_c superconductors (YBa_2Cu_3O_7, La_{2-x}Sr_xCuO_4, etc.). Whether the Hubbard model rigorously supports superconductivity in 2D, and if so with what T_c, remains one of the great open questions. The model also exhibits stripe phases (interleaved charge and spin order), pseudogap behavior, and other phenomena seen in cuprates. Solving the 2D Hubbard model is simultaneously one of the most important and most difficult problems in theoretical physics.
