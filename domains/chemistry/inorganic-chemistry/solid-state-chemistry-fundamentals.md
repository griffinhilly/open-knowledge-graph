---
id: solid-state-chemistry-fundamentals
title: Solid State Chemistry Fundamentals
domain: chemistry
course: inorganic-chemistry
prerequisites:
- id: crystal-field-theory
  type: soft
- id: main-group-chemistry-overview
  type: soft
- id: periodic-trends
  type: hard
builds-toward:
- materials-chemistry-zeolites-mofs
- heterogeneous-catalysis-metal-surfaces
tags:
- crystal structures
- unit cells
- band theory
- defects
- ionic solids
stage: advanced
status: validated
---

# Solid State Chemistry Fundamentals

## Core Idea
Solid state chemistry studies the structure, bonding, and properties of crystalline and amorphous solids. Crystal structures are described by unit cells and space groups; bonding ranges from ionic (NaCl) to covalent (diamond) to metallic (copper). Band theory extends molecular orbital theory to infinite arrays of atoms, explaining why some solids are metals, some are semiconductors, and some are insulators. Defects in crystal lattices — vacancies, interstitials, substitutions — profoundly affect properties like conductivity, color, and catalytic activity.

## Questions

```yaml
- question: "In the rock salt (NaCl) structure, what is the coordination number of each ion?"
  type: multiple-choice
  options:
    - "Na⁺ has coordination number 4, Cl⁻ has coordination number 4"
    - "Na⁺ has coordination number 6, Cl⁻ has coordination number 6"
    - "Na⁺ has coordination number 8, Cl⁻ has coordination number 8"
    - "Na⁺ has coordination number 6, Cl⁻ has coordination number 4"
  answer: 1
  explanation: "In the rock salt structure, each Na⁺ is surrounded by six Cl⁻ ions in an octahedral arrangement, and each Cl⁻ is surrounded by six Na⁺ ions in an octahedral arrangement. Both ions have coordination number 6. This structure is adopted when the radius ratio r⁺/r⁻ falls in the range that stabilizes octahedral coordination (~0.414-0.732). The rock salt structure can be described as two interpenetrating face-centered cubic lattices, one of Na⁺ and one of Cl⁻, offset by half a unit cell edge."

- question: "Band theory explains metallic conductivity by showing that partially filled bands allow electrons to move freely through the solid under an applied electric field."
  type: true-false
  answer: true
  explanation: "When N atoms come together in a solid, each atomic orbital splits into N molecular orbitals forming a near-continuous band. If the band is partially filled (as in metals like sodium, where the 3s band is half-full), there are empty states immediately above the occupied states — electrons can be promoted to these states by an infinitesimally small electric field, enabling conduction. In an insulator, the highest occupied band (valence band) is completely full and separated from the empty band (conduction band) by a large energy gap; electrons cannot be promoted, so no conduction occurs. Semiconductors have a small gap that thermal energy can bridge."

- question: "A perfect crystal with no defects would be a better catalyst than one with vacancies and surface steps."
  type: true-false
  answer: false
  explanation: "Defects are often the catalytically active sites. Surface vacancies, steps, edges, and kinks provide under-coordinated atoms with unsatisfied valences that can bind and activate substrate molecules. A perfect, flat crystal surface has fewer such sites and is generally less reactive. This is why nanoparticles (with high surface-to-volume ratios and many edge/corner atoms) are more catalytically active per atom than bulk materials. In ionic solids, oxygen vacancies create sites for oxide ion migration (important in solid oxide fuel cells) and can trap electrons, creating localized color centers."

- question: "Explain why the band gap determines whether a solid is a metal, semiconductor, or insulator, and describe how doping a semiconductor changes its conductivity."
  type: short-answer
  answer: "The band gap is the energy difference between the top of the valence band (highest occupied states) and the bottom of the conduction band (lowest empty states). Metals have no band gap — their valence and conduction bands overlap or the valence band is partially filled. Insulators have a large band gap (>3 eV) that thermal energy cannot bridge. Semiconductors have a small band gap (0.1-3 eV) where some thermal excitation of electrons into the conduction band occurs. Doping introduces impurity atoms: n-type doping (e.g., phosphorus in silicon) adds extra electrons near the conduction band edge, dramatically increasing conductivity; p-type doping (e.g., boron in silicon) creates holes in the valence band that act as positive charge carriers."
  explanation: "The semiconductor industry is built on the ability to tune conductivity over many orders of magnitude through controlled doping. This is why silicon — with a conveniently sized band gap of 1.1 eV and an easily grown oxide layer — became the foundation of modern electronics."
```

## Explainer

Molecular orbital theory works beautifully for discrete molecules with a countable number of atoms. But what happens when you bring together 10²³ atoms in a solid? The orbitals do not disappear — they multiply. When N atoms combine, each atomic orbital produces N molecular orbitals, so closely spaced in energy that they form a continuous band. Band theory is simply MO theory applied to infinite periodic arrays, and it provides the framework for understanding the electrical, optical, and thermal properties of solids.

Consider metallic sodium. Each atom contributes its 3s orbital. In a solid with N sodium atoms, these N orbitals produce a band of N energy levels. Since each Na contributes one electron, the band is half-filled. Electrons at the top of the occupied levels can easily move into nearby empty levels when an electric field is applied — this is metallic conduction. Now consider diamond: each carbon contributes four orbitals that hybridize and form bonding and antibonding bands (the valence and conduction bands). All bonding levels are filled, all antibonding levels are empty, and the gap between them is 5.5 eV — far too large for thermal excitation. Diamond is an insulator. Silicon has the same structure but a gap of only 1.1 eV, allowing some thermal excitation: a semiconductor.

Crystal structures describe how atoms pack in three dimensions. The simplest ionic structures — rock salt (NaCl), cesium chloride (CsCl), zinc blende (ZnS), fluorite (CaF₂) — are determined primarily by the radius ratio of the cation to the anion, which dictates the coordination number that maximizes electrostatic attraction while avoiding ion-ion repulsion. The rock salt structure (coordination number 6 for both ions) is adopted by hundreds of binary compounds. The perovskite structure (ABX₃, with A in a 12-coordinate site and B in a 6-coordinate octahedral site) is important for understanding materials from calcium titanate to high-temperature superconductors.

Real crystals are never perfect. Point defects — missing atoms (vacancies), extra atoms (interstitials), and foreign atoms (substitutions) — profoundly affect properties. Vacancies in ionic crystals allow ion migration, enabling solid-state ionic conduction. Color centers (electrons trapped at anion vacancies) give crystals like NaCl their characteristic colors when irradiated. Doping semiconductors with controlled impurities creates the p-type and n-type materials that form the basis of transistors and solar cells. In catalysis, surface defects provide the active sites where reactions occur. The chemistry of defects is often more important than the chemistry of the perfect crystal — a lesson that extends throughout materials science.
