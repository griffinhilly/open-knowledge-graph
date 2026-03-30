---
id: nanomaterials-synthesis
title: Nanomaterials Synthesis
domain: chemistry
course: materials-chemistry
prerequisites:
- id: crystal-structures-and-unit-cells
  type: hard
- id: chemical-equilibrium
  type: soft
- id: semiconductor-materials-chemistry
  type: soft
builds-toward:
- self-assembly-materials
- thin-film-deposition-cvd-pvd
- catalytic-materials-design
tags:
- nanoparticles
- quantum dots
- nucleation
- surface-to-volume ratio
- size-dependent properties
stage: expert
status: validated
---

# Nanomaterials Synthesis

## Core Idea
Nanomaterials have at least one dimension between 1 and 100 nm, a size regime where properties differ dramatically from both individual molecules and bulk materials. The high surface-to-volume ratio and quantum confinement effects at this scale produce size-dependent optical, electronic, magnetic, and catalytic properties. Synthesis strategies fall into two categories: top-down (breaking bulk material down to nanoscale via milling, lithography, or etching) and bottom-up (building nanoscale structures from molecular precursors via nucleation and growth, sol-gel, or vapor-phase methods). The LaMer model of nucleation and growth provides the framework for synthesizing monodisperse nanoparticles: a burst of nucleation followed by slow, controlled growth produces uniform particles, while continuous nucleation gives polydisperse products.

## Questions

```yaml
- question: "Colloidal gold nanoparticles appear red in solution rather than gold-colored. What causes this size-dependent color change?"
  type: short-answer
  answer: "Gold nanoparticles (10-50 nm) exhibit localized surface plasmon resonance (LSPR): the conduction electrons oscillate collectively in response to incident light, and the resonance frequency depends on particle size, shape, and the surrounding medium. For ~20 nm spherical gold nanoparticles, the plasmon resonance absorbs green light (~520 nm), making the transmitted light appear red. Bulk gold appears gold-colored because the flat surface supports only non-resonant reflection. The nanoscale confinement of electrons changes the optical response qualitatively."
  explanation: "Surface plasmon resonance is one of the most dramatic examples of size-dependent properties. As gold nanoparticles grow from 10 to 100 nm, the absorption peak red-shifts and broadens. Changing shape from spheres to rods splits the resonance into two peaks (transverse and longitudinal modes), allowing tuning across the visible and near-infrared spectrum. This tunable optical response is exploited in biosensors, photothermal therapy, and SERS (surface-enhanced Raman spectroscopy)."

- question: "The LaMer model predicts that monodisperse nanoparticles require a short burst of nucleation followed by a long period of growth without further nucleation."
  type: true-false
  answer: true
  explanation: "In the LaMer model, precursor concentration increases until it exceeds the critical supersaturation threshold, triggering rapid homogeneous nucleation. This burst of nucleation consumes precursor, dropping the concentration below the nucleation threshold but above the growth threshold. All subsequent precursor consumption goes into growing existing nuclei rather than forming new ones. If all nuclei form at roughly the same time and grow at the same rate, the result is monodisperse particles. Continuous or multiple nucleation events produce polydisperse mixtures. Practical synthesis strategies (hot injection, slow precursor addition) are designed to achieve this separation of nucleation and growth."

- question: "CdSe quantum dots emit different colors depending on their size — smaller dots emit blue light, larger dots emit red. What physical phenomenon explains this?"
  type: multiple-choice
  options:
    - "Smaller particles have more surface defects that emit blue light"
    - "Quantum confinement increases the effective band gap as particle size decreases, shifting emission to higher energy (shorter wavelength)"
    - "Smaller particles absorb more blue light and re-emit it"
    - "The crystal structure changes with particle size, altering the band gap"
  answer: 1
  explanation: "When a semiconductor nanocrystal is smaller than the exciton Bohr radius (~5.6 nm for CdSe), the electron and hole wavefunctions are confined within the particle boundaries. This confinement increases the kinetic energy of the carriers, widening the effective band gap beyond the bulk value (1.74 eV for CdSe). Smaller particles = stronger confinement = larger effective band gap = shorter wavelength emission. A 2 nm CdSe dot emits blue (~480 nm); a 6 nm dot emits red (~620 nm). This size-tunable emission, with narrow linewidths, makes quantum dots valuable for displays, bioimaging, and lighting."

- question: "Why does decreasing nanoparticle size dramatically increase catalytic activity per unit mass of material?"
  type: short-answer
  answer: "Catalysis occurs at the surface. As particle size decreases, the fraction of atoms at the surface increases dramatically — for a 2 nm particle, roughly 50% of atoms are surface atoms, compared to a negligible fraction for micron-sized particles. This vastly increases the number of catalytically active sites per unit mass. Additionally, small nanoparticles have a higher proportion of edge, corner, and step sites (low-coordination atoms) that are often the most catalytically active. The electronic structure also changes at small sizes, potentially modifying binding energies of reactants and intermediates."
  explanation: "The surface-to-volume ratio scales as 1/r, so halving the particle diameter doubles the specific surface area. A 3 nm gold nanoparticle supported on TiO2 is an excellent catalyst for CO oxidation, while bulk gold is catalytically inert. This is not just a surface area effect — the electronic properties of nanoscale gold differ from bulk, weakening CO binding and enabling the catalytic cycle. The interplay of geometric (more surface sites) and electronic (modified binding energies) effects makes nanomaterial catalyst design a rich field."
```

## Explainer

Nanomaterials occupy the boundary between molecules and bulk solids — a size regime where neither molecular chemistry nor solid-state physics alone can predict material behavior. At 1-100 nm, a significant fraction of atoms reside at the surface, quantum mechanical confinement effects alter electronic structure, and the equilibrium properties familiar from bulk thermodynamics may not apply. The synthesis of nanomaterials is fundamentally about controlling size, shape, composition, and surface chemistry at this scale.

**Bottom-up synthesis** from molecular precursors is the workhorse of nanomaterials chemistry. The classic approach — colloidal synthesis — dissolves metal or semiconductor precursors in a solvent with surfactant molecules (capping agents), then induces nucleation by changing temperature, adding a reducing agent, or decomposing the precursor. The **LaMer model** frames the key challenge: to get uniform nanoparticles, you need all nuclei to form at the same time (burst nucleation) and then grow at the same rate. Hot-injection synthesis achieves this by rapidly injecting a cold precursor solution into a hot surfactant solution — the sudden supersaturation triggers a burst of nucleation, and subsequent growth at lower temperature produces monodisperse particles. Size is controlled by growth time: quench early for small particles, grow longer for large ones.

**Capping agents** (oleic acid, thiols, phosphine oxides, polymers) play a dual role: they prevent nanoparticles from aggregating by providing steric or electrostatic stabilization, and they control growth kinetics by selectively binding to certain crystal faces. Preferential binding to the {100} faces of a growing nanocrystal while leaving {111} faces exposed leads to anisotropic growth — rods, wires, or plates instead of spheres. The chemistry of the capping agent determines the final shape and, ultimately, the surface chemistry of the nanoparticle.

The **size-dependent properties** that motivate nanomaterial synthesis arise from two main effects. **Quantum confinement** dominates in semiconductor nanocrystals (quantum dots): when the particle is smaller than the exciton Bohr radius, the electronic wavefunctions are confined, increasing the effective band gap. This produces the spectacular size-tunable fluorescence of CdSe, InP, and perovskite quantum dots. **Surface effects** dominate in metal nanoparticles: the high fraction of under-coordinated surface atoms gives rise to surface plasmon resonances (gold, silver), enhanced catalytic activity (Pt, Pd, Au), and superparamagnetic behavior (Fe3O4). Understanding and exploiting these size-dependent phenomena is the core intellectual challenge of nanomaterials chemistry.
