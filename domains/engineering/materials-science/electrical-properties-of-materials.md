---
id: electrical-properties-of-materials
title: Electrical Properties of Materials
domain: engineering
course: materials-science
prerequisites:
- id: band-theory-intro
  type: hard
- id: crystal-structure-basics
  type: soft
- id: electron-configuration
  type: soft
- id: electric-current-and-resistance
  type: soft
- id: electron-configuration-aufbau-principle
  type: soft
tags:
- conductivity
- semiconductors
- band-gap
- dielectrics
- superconductivity
stage: formal-systems
status: validated
---

# Electrical Properties of Materials

## Core Idea
Electrical conductivity in solids is explained by band theory: the energy gap between the valence band (occupied) and conduction band (empty) determines whether a material is a conductor (overlapping bands), semiconductor (small gap, ~1 eV), or insulator (large gap, >5 eV). In metals, conductivity decreases with temperature as phonon scattering increases; in semiconductors, conductivity increases with temperature as more carriers are thermally excited across the gap. Doping introduces donor or acceptor levels near band edges, enabling the n-type and p-type semiconductors essential to transistors and photovoltaics. Dielectric materials store electrical energy in polarized bonds and are rated by dielectric constant and breakdown strength.

## How It's Best Learned
Compare resistivity vs. temperature plots for a metal, intrinsic semiconductor, and insulator to see contrasting trends. Trace how adding phosphorus (donor) to silicon shifts the Fermi level and increases electron carrier concentration.

## Common Misconceptions
- Semiconductors are not simply 'partial' conductors — their conduction mechanism (thermally excited carriers across a band gap) is fundamentally different from metallic conduction.
- Resistivity and resistance are different: resistivity is a material property independent of geometry; resistance depends on both material and dimensions.

## Explainer

From band theory, you know that electrons in a crystal occupy allowed energy bands, with gaps of forbidden energies between them. The electrical behavior of a material is almost entirely determined by what happens at two bands: the **valence band** (the highest fully-occupied band at absolute zero) and the **conduction band** (the next available band above it). Current flows only when electrons can move through an applied electric field — and they can only do that if there are empty states nearby to move into. In a metal, the valence band is partially filled (or overlaps the conduction band), so electrons at the Fermi level have empty states immediately accessible: metals conduct easily. In an insulator, the valence band is completely full and the band gap is large (>5 eV), so thermal energy at room temperature cannot excite electrons across it: insulators don't conduct. Semiconductors occupy the middle ground — the gap is small enough (~1 eV for silicon) that some electrons can be thermally promoted to the conduction band, leaving behind mobile holes in the valence band.

The contrasting temperature behaviors of metals and semiconductors make intuitive sense once you understand the mechanism. In a metal, more electrons are always available to conduct (the band is already partially filled), but increasing temperature creates more lattice vibrations (**phonons**) that scatter electrons, reducing their mean free path — so conductivity *decreases* with temperature. In a semiconductor, the scattering effect also exists, but the dominant factor at moderate temperatures is the exponential increase in thermally-excited carriers as temperature rises. More carriers crossing the band gap more than compensates for increased scattering, so semiconductor conductivity *increases* with temperature. This signature difference is a practical diagnostic: a material whose resistance rises with temperature is metallic; one whose resistance falls is semiconducting.

**Doping** is the deliberate introduction of impurity atoms to control carrier concentration. Substituting a pentavalent atom (phosphorus, arsenic) into a silicon lattice provides an extra electron that is only loosely bound — its energy level sits just below the conduction band. At room temperature, this electron is easily excited into the conduction band, creating an n-type semiconductor with excess electron carriers. Substituting a trivalent atom (boron) creates an acceptor level just above the valence band; electrons from the valence band easily fill it, creating holes — mobile positive carriers — and producing p-type material. Doping allows carrier concentration to be controlled over many orders of magnitude, which is what makes transistors and photovoltaic cells possible. The p-n junction formed by joining n-type and p-type regions creates the built-in electric field that drives photocurrent in solar cells and rectifies current in diodes.

**Dielectric** materials are insulators with large band gaps, but their engineering value lies in their response to electric fields: the bound electrons polarize, storing energy capacitively. The **dielectric constant** (relative permittivity) quantifies how much more charge a capacitor can store with the dielectric present compared to vacuum. **Dielectric strength** is the maximum field before breakdown — when enough electrons are promoted across the gap to create a conducting path. High-k dielectrics (large dielectric constant) are used in capacitors and gate oxides in MOSFETs; high dielectric strength materials are used in high-voltage insulation. The interplay between band gap, polarizability, and thermal stability determines which insulating material is right for which application.
