---
id: mott-insulators
title: Mott Insulators
domain: physics
course: condensed-matter-physics
prerequisites:
- id: hubbard-model
  type: hard
- id: metals-insulators-semiconductors
  type: hard
tags:
- mott-insulator
- correlation-driven
- metal-insulator-transition
- charge-gap
stage: expert
status: validated
---

# Mott Insulators

## Core Idea
A Mott insulator is a material that band theory predicts should be metallic (partially filled band) but is insulating due to strong electron-electron Coulomb repulsion. When the on-site repulsion U exceeds the bandwidth W, it becomes energetically prohibitive for electrons to hop between sites (each hop creates a doubly-occupied site costing energy U), and the system develops a charge gap despite the absence of a band gap. The Mott metal-insulator transition (MIT) can be driven by changing U/W through pressure, temperature, or chemical doping. Mott insulators are the parent compounds of many exotic materials, including cuprate high-T_c superconductors, colossal magnetoresistance manganites, and frustrated quantum magnets.

## Questions

```yaml
- question: "NiO has a partially filled d-band (Ni²⁺ has 8 d-electrons in a 10-state d-shell). Band theory predicts it is a metal. Experiment shows it is an insulator with a gap of ~4 eV. What is the resolution?"
  type: multiple-choice
  options:
    - "Band theory is wrong about the number of d-electrons"
    - "The strong Coulomb repulsion U ~ 8 eV between d-electrons on the same Ni site far exceeds the d-band width W ~ 3 eV. Electrons are prevented from hopping because double occupation costs too much energy. This Mott mechanism opens a correlation-driven gap between the lower Hubbard band (singly occupied states) and the upper Hubbard band (doubly occupied states), making NiO an insulator"
    - "Crystal field splitting opens a band gap"
    - "The oxygen atoms in NiO donate electrons that fill the d-band"
  answer: 1
  explanation: "This is the textbook Mott insulator. In band theory, the d-band is split by the crystal field but remains partially filled — a metal. The Mott picture splits each d-state into two Hubbard bands: the lower Hubbard band (occupied, energy ~ε_d) and the upper Hubbard band (empty, energy ~ε_d + U). The gap between them is of order U - W. This was one of the earliest and most striking failures of independent-electron band theory, and it established that electron-electron interactions can qualitatively change the electronic ground state."

- question: "The Mott transition can be driven by pressure in V₂O₃, which transitions from an antiferromagnetic insulator to a paramagnetic metal. Why does pressure favor the metallic state?"
  type: multiple-choice
  options:
    - "Pressure destroys the crystal structure"
    - "Pressure decreases interatomic distances, increasing orbital overlap and thus the hopping integral t (and bandwidth W). When W becomes comparable to U, the kinetic energy gain from delocalization overcomes the Coulomb cost of double occupation, and the Mott gap closes. The Mott criterion (U/W ~ 1 for the transition) is reached from the insulating side by increasing W"
    - "Pressure increases the Coulomb repulsion U"
    - "Pressure aligns the electron spins, making the material metallic"
  answer: 1
  explanation: "V₂O₃ is the canonical system for studying the Mott transition. At ambient pressure, it is an antiferromagnetic insulator below 150 K. Applying ~25 kbar of pressure (or doping with Cr or Ti) drives it metallic. The transition is first-order at low temperatures (with a volume collapse — the metallic phase is denser) and ends at a critical point above which a smooth crossover connects the insulating and metallic phases. The entire phase diagram is governed by the ratio U/W."

- question: "Mott insulators are often antiferromagnetic. However, Mott insulating behavior is not the same as antiferromagnetic ordering — the charge gap (Mott physics) and spin order (magnetism) are distinct phenomena."
  type: true-false
  answer: true
  explanation: "The Mott gap arises from Coulomb repulsion suppressing charge fluctuations and exists even without magnetic order. The antiferromagnetism is a secondary consequence: once charges are localized (one electron per site), the residual exchange coupling J = 4t²/U between neighboring spins produces magnetic order. The Mott gap typically persists above the Neel temperature — the material remains insulating even when the spins are disordered (paramagnetic Mott insulator). In frustrated lattices (triangular, kagome), the magnetic ordering can be completely suppressed by geometric frustration, producing a Mott insulator with no long-range magnetic order — a quantum spin liquid candidate."

- question: "Explain the difference between a Mott insulator and a band insulator, and describe how you could experimentally distinguish them."
  type: short-answer
  answer: "A band insulator has a gap due to the crystal potential (all bands fully occupied, gap between valence and conduction bands). A Mott insulator has a gap due to electron-electron interactions (partially filled band split into upper and lower Hubbard bands). Key experimental differences: (1) A Mott insulator has magnetic moments (from unpaired localized electrons) and shows Curie-Weiss susceptibility, while a band insulator is diamagnetic. (2) The Mott gap can be closed by pressure (increasing bandwidth) or doping (introducing mobile carriers), while a band gap is robust against these. (3) Spectroscopy (photoemission + inverse photoemission) shows spectral weight transfer between Hubbard bands as doping or temperature changes — a hallmark of correlated behavior absent in band insulators. (4) DFT calculations predict a metal — the disagreement between DFT and experiment is itself a diagnostic of Mott physics."
  explanation: "The classification has expanded beyond Mott vs. band: charge-transfer insulators (gap is between oxygen p-band and transition metal upper Hubbard band, as in many cuprates), Slater insulators (gap opens only with antiferromagnetic order), and topological Mott insulators (interaction-driven topological phases) are all variations on the theme."
```

## Explainer

The concept of the **Mott insulator** represents one of the most important failures — and subsequent triumphs — of theoretical condensed matter physics. Standard band theory, which treats electrons as independent particles moving in a periodic potential, predicts that any material with a partially filled band should be metallic. Yet many transition metal oxides, rare earth compounds, and organic conductors with partially filled bands are insulating. Nevill Mott explained this in the 1940s-60s: when the electron-electron Coulomb repulsion U is large enough compared to the bandwidth W, electrons become localized to avoid the energetic cost of sharing a site, and a **correlation-driven gap** opens.

The simplest picture uses the **Hubbard model** at half-filling. Each site has one electron. To conduct, an electron must hop to a neighboring site, creating a doubly-occupied site at cost U. If U >> W (the bandwidth from hopping), this cost is prohibitive and the electrons are stuck — each one pinned to its site. The single band splits into two **Hubbard bands**: the lower Hubbard band (removing an electron from a singly-occupied site, creating a hole) and the upper Hubbard band (adding an electron to create double occupancy). The gap between them is approximately U - W, and it is a many-body correlation gap, not a single-particle band gap.

The **Mott metal-insulator transition** occurs when U/W passes through a critical value of order 1. This can be tuned by pressure (increasing t and W by squeezing atoms closer), by temperature (thermal fluctuations can delocalize electrons), by doping (removing or adding electrons from the half-filled configuration), or by chemical substitution (changing U or t). The transition in V_2O_3, the canonical Mott system, is first-order at low temperatures (with hysteresis and a volume collapse) and ends at a critical point around 400 K, above which a continuous crossover replaces the sharp transition. Dynamical mean-field theory (DMFT) provides the modern theoretical framework for the Mott transition, capturing the competition between coherent quasiparticle formation and local moment physics.

Mott insulators are far more than an intellectual curiosity — they are the parent compounds of some of the most technologically important and scientifically puzzling materials. The **cuprate high-T_c superconductors** (La_{2-x}Sr_xCuO_4, YBa_2Cu_3O_7) are doped Mott insulators: the parent compound is an antiferromagnetic Mott insulator, and doping with holes produces d-wave superconductivity at temperatures up to 130 K. **Colossal magnetoresistance** manganites are Mott systems where magnetic field-driven delocalization produces enormous resistance changes. **Frustrated Mott insulators** on triangular and kagome lattices, where antiferromagnetic order is geometrically incompatible, are candidates for **quantum spin liquid** states — exotic phases with fractionalized excitations and topological order. Understanding Mott physics is thus central to the search for new quantum materials.
