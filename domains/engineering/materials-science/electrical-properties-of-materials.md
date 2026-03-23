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

## Questions

```yaml
- question: "A material's electrical resistance increases as it is heated from room temperature to 200°C. What type of material is this most likely to be?"
  type: multiple-choice
  options:
    - "A semiconductor, because thermally excited carriers always reduce resistance"
    - "An insulator, because high temperatures promote electron trapping"
    - "A metal, because increasing temperature creates more phonon scattering that impedes electron flow"
    - "A superconductor, because superconductivity breaks down above a critical temperature"
  answer: 2
  explanation: "In metals, the conduction band is already partially filled — electrons can conduct readily. As temperature rises, increased lattice vibrations (phonons) scatter conduction electrons more frequently, reducing their mean free path and decreasing conductivity (increasing resistance). This is the diagnostic signature of metallic behavior: resistance rises with temperature. Semiconductors behave oppositely — their resistance falls as temperature rises, because the dominant effect is exponential increase in thermally excited carriers across the band gap. Option A describes semiconductor behavior and is the common confusion this question is designed to catch."

- question: "Silicon is doped with phosphorus atoms substituted into the crystal lattice. How does this primarily increase the conductivity of the silicon?"
  type: multiple-choice
  options:
    - "Phosphorus atoms widen the band gap, allowing more electrons to participate in conduction"
    - "Phosphorus provides extra electrons with energy levels just below the conduction band, easily excited into it at room temperature"
    - "Phosphorus replaces silicon-silicon bonds with metallic bonds, increasing electron mobility"
    - "Phosphorus creates holes in the valence band by accepting electrons from silicon atoms"
  answer: 1
  explanation: "Phosphorus has 5 valence electrons; silicon has 4. When phosphorus substitutes into the silicon lattice, 4 electrons form bonds with neighboring silicon atoms, but the 5th is only loosely bound — its energy level sits just below the conduction band. At room temperature, thermal energy is sufficient to excite this electron into the conduction band, creating a free electron carrier. This is n-type doping. The key insight is that doping creates energy levels near the band edge, dramatically reducing the activation energy needed to generate carriers. Option D describes p-type doping (with boron or other trivalent atoms), not phosphorus."

- question: "A material that becomes more electrically conductive as temperature rises is behaving as a semiconductor rather than a metal."
  type: true-false
  answer: true
  explanation: "The contrasting temperature dependence is the clearest diagnostic for distinguishing metals from semiconductors. In semiconductors, the dominant effect of rising temperature is exponential increase in carriers thermally excited across the band gap — which overwhelms the increased phonon scattering that also occurs. In metals, there are already enough carriers (the band is partially filled), so the scattering effect dominates and conductivity decreases. This temperature signature is used in practice to identify and classify materials: if resistance falls when you heat a sample, it's behaving semiconductingly."

- question: "Semiconductors are simply 'weak conductors' that behave like metals with fewer charge carriers — just a less conductive version of the same mechanism."
  type: true-false
  answer: false
  explanation: "The conduction mechanisms are fundamentally different, not just quantitatively different. In a metal, charge carriers (electrons) are always present in partially filled bands and available to conduct at any temperature. In a semiconductor, the valence band is completely full at absolute zero — there are no carriers and it is a perfect insulator. Carriers only appear when electrons are thermally (or photonically) excited across the band gap into the conduction band, leaving behind mobile holes in the valence band. This gap-crossing mechanism explains why semiconductor conductivity is temperature-sensitive and light-sensitive (photovoltaic effect), while metallic conductivity is neither. It also explains why doping with tiny impurity concentrations can change conductivity by many orders of magnitude — something impossible in a true metal."

- question: "Explain why the conductivity of a metal decreases with increasing temperature while the conductivity of a semiconductor increases, even though both effects involve temperature."
  type: short-answer
  answer: "In a metal, the conduction band is already partially filled — there are always free electrons available to carry current. As temperature rises, lattice vibrations (phonons) increase, scattering electrons more frequently and shortening their mean free path. More scattering means lower mobility, lower conductivity. In a semiconductor, the valence band is full and the conduction band is empty at low temperatures — there are no free carriers. As temperature rises, thermal energy excites electrons across the band gap into the conduction band (and creates holes in the valence band). The number of carriers increases exponentially with temperature, which more than compensates for the increased scattering. The net effect is rising conductivity. The key is that metals are carrier-saturated (more temperature just adds scatter), while semiconductors are carrier-starved (more temperature primarily adds carriers)."
  explanation: "This distinction is also why semiconductors can be light-sensitive: photons can supply the energy to excite electrons across the band gap just as thermal energy does, creating carriers and increasing conductivity. Metals don't exhibit photoconductivity for the same reason they don't show thermally activated conductivity — the carriers are already there."
```

## Explainer

From band theory, you know that electrons in a crystal occupy allowed energy bands, with gaps of forbidden energies between them. The electrical behavior of a material is almost entirely determined by what happens at two bands: the **valence band** (the highest fully-occupied band at absolute zero) and the **conduction band** (the next available band above it). Current flows only when electrons can move through an applied electric field — and they can only do that if there are empty states nearby to move into. In a metal, the valence band is partially filled (or overlaps the conduction band), so electrons at the Fermi level have empty states immediately accessible: metals conduct easily. In an insulator, the valence band is completely full and the band gap is large (>5 eV), so thermal energy at room temperature cannot excite electrons across it: insulators don't conduct. Semiconductors occupy the middle ground — the gap is small enough (~1 eV for silicon) that some electrons can be thermally promoted to the conduction band, leaving behind mobile holes in the valence band.

The contrasting temperature behaviors of metals and semiconductors make intuitive sense once you understand the mechanism. In a metal, more electrons are always available to conduct (the band is already partially filled), but increasing temperature creates more lattice vibrations (**phonons**) that scatter electrons, reducing their mean free path — so conductivity *decreases* with temperature. In a semiconductor, the scattering effect also exists, but the dominant factor at moderate temperatures is the exponential increase in thermally-excited carriers as temperature rises. More carriers crossing the band gap more than compensates for increased scattering, so semiconductor conductivity *increases* with temperature. This signature difference is a practical diagnostic: a material whose resistance rises with temperature is metallic; one whose resistance falls is semiconducting.

**Doping** is the deliberate introduction of impurity atoms to control carrier concentration. Substituting a pentavalent atom (phosphorus, arsenic) into a silicon lattice provides an extra electron that is only loosely bound — its energy level sits just below the conduction band. At room temperature, this electron is easily excited into the conduction band, creating an n-type semiconductor with excess electron carriers. Substituting a trivalent atom (boron) creates an acceptor level just above the valence band; electrons from the valence band easily fill it, creating holes — mobile positive carriers — and producing p-type material. Doping allows carrier concentration to be controlled over many orders of magnitude, which is what makes transistors and photovoltaic cells possible. The p-n junction formed by joining n-type and p-type regions creates the built-in electric field that drives photocurrent in solar cells and rectifies current in diodes.

**Dielectric** materials are insulators with large band gaps, but their engineering value lies in their response to electric fields: the bound electrons polarize, storing energy capacitively. The **dielectric constant** (relative permittivity) quantifies how much more charge a capacitor can store with the dielectric present compared to vacuum. **Dielectric strength** is the maximum field before breakdown — when enough electrons are promoted across the gap to create a conducting path. High-k dielectrics (large dielectric constant) are used in capacitors and gate oxides in MOSFETs; high dielectric strength materials are used in high-voltage insulation. The interplay between band gap, polarizability, and thermal stability determines which insulating material is right for which application.
