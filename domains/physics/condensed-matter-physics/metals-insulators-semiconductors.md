---
id: metals-insulators-semiconductors
title: Metals, Insulators, and Semiconductors
domain: physics
course: condensed-matter-physics
prerequisites:
- id: band-structure-density-of-states
  type: hard
- id: fermi-dirac-statistics
  type: hard
tags:
- metal
- insulator
- semiconductor
- band-gap
- fermi-level
stage: expert
status: validated
---

# Metals, Insulators, and Semiconductors

## Core Idea
Band theory classifies solids by the filling of their energy bands. In metals, the Fermi level lies within a band, so there are empty states immediately above E_F available for conduction. In insulators, all bands below a large gap (> ~4 eV) are completely filled and all above are empty — no states are available at accessible energies. Semiconductors are insulators with small gaps (< ~3 eV) where thermal excitation or doping can promote electrons across the gap, creating mobile carriers. This classification explains why copper conducts, diamond does not, and silicon can be made to do either.

## Questions

```yaml
- question: "A material has an even number of electrons per unit cell. Is it necessarily an insulator?"
  type: multiple-choice
  options:
    - "Yes — an even electron count always means completely filled bands"
    - "No — bands from different zones can overlap in energy (band overlap), leaving both partially filled even with an even electron count, as in divalent metals like magnesium and calcium"
    - "No — an even number of electrons always makes a metal"
    - "It depends only on the crystal structure, not the electron count"
  answer: 1
  explanation: "An even electron count is necessary but not sufficient for an insulator. If the valence and conduction bands overlap in energy (which depends on the band structure and Brillouin zone geometry), both are partially filled even though the total electron count would fill bands completely if there were a gap. This is precisely what happens in divalent metals like Mg, Ca, and Zn — band overlap makes them metallic despite having two electrons per atom. Conversely, an odd electron count in a simple band picture must produce a metal (odd filling cannot completely fill a band)."

- question: "At room temperature, silicon has a resistivity ~10^3 Ω·m while copper has ~10^-8 Ω·m — a difference of 11 orders of magnitude. What is the fundamental band-theory explanation?"
  type: multiple-choice
  options:
    - "Silicon atoms are heavier and scatter electrons more"
    - "Copper has partially filled bands with a high density of carriers at E_F, while silicon's 1.1 eV gap means only ~10^10 cm^-3 thermally excited carriers versus copper's ~10^23 cm^-3"
    - "Silicon has a stronger crystal potential"
    - "Copper has more electrons per atom"
  answer: 1
  explanation: "The carrier density difference is the dominant factor. Copper's Fermi level sits in the middle of a band, providing ~10^23 conduction electrons per cm^3. Silicon's 1.1 eV gap means the carrier density at 300K follows n ∝ exp(-E_g/2k_BT) ≈ 10^10 cm^-3 — thirteen orders of magnitude fewer carriers. Even though silicon's carriers may have comparable mobility to copper's, the enormous density difference determines the conductivity ratio."

- question: "Diamond (5.5 eV gap) is an insulator, silicon (1.1 eV) and germanium (0.67 eV) are semiconductors, and tin (alpha-Sn, 0 eV gap) is a semimetal. All four are Group IV elements with the same crystal structure. The gap decreases monotonically with atomic number."
  type: true-false
  answer: true
  explanation: "All four crystallize in the diamond structure. Going down Group IV, atoms get larger and the bond lengths increase. Larger inter-atomic spacing means more orbital overlap between bonding and antibonding states (the bands get wider), and the gap between them shrinks. By tin, the gap has closed entirely, producing a semimetal with overlapping bands. This trend — gap shrinks with increasing atomic size in isostructural materials — is a general principle that reflects the connection between orbital overlap and band width."

- question: "Explain the physical distinction between a semimetal and a semiconductor with zero gap."
  type: short-answer
  answer: "A semiconductor with exactly zero gap (like a gapless semiconductor or zero-gap semiconductor) has the valence band maximum and conduction band minimum touching at the same energy but not overlapping — the density of states vanishes at the Fermi level. A semimetal has band overlap: the bottom of one band dips below the top of another, so both bands are partially occupied and there are carriers of both electron and hole character even at T = 0, with a small but nonzero density of states at E_F. Examples of semimetals include bismuth and graphite. The distinction matters because semimetals always have carriers (metallic-like, though with low density), while a zero-gap semiconductor has zero carriers at T = 0."
  explanation: "Graphene is the most famous zero-gap semiconductor: its conduction and valence bands touch at the Dirac points, but do not overlap, and the density of states vanishes linearly at the Fermi energy."
```

## Explainer

The most consequential prediction of band theory is the division of crystalline solids into three categories based on how their energy bands are filled. In a **metal**, the Fermi level cuts through one or more bands, leaving partially filled states at the Fermi energy. These electrons can be accelerated by an arbitrarily small electric field, producing electrical conduction. The high density of states at E_F also gives metals their characteristic large electronic specific heat and Pauli paramagnetism.

In an **insulator**, all occupied bands are completely filled and separated from the empty bands by a large energy gap E_g. Since a completely filled band carries no net current (for every electron moving right, there is one moving left), an applied field cannot accelerate the electrons — you would need to excite an electron across the gap. For diamond (E_g = 5.5 eV), room-temperature thermal energy k_BT ~ 0.025 eV is utterly inadequate to excite any appreciable number of electrons across the gap, so the conductivity is essentially zero.

**Semiconductors** are the intermediate case: the gap is small enough (roughly 0.1 to 3 eV) that some electrons are thermally excited across it at room temperature, or the gap can be overcome by doping. The intrinsic carrier density scales as n_i proportional to exp(-E_g / 2k_BT), which is exponentially sensitive to both the gap size and the temperature. For silicon at 300K, n_i is approximately 10^{10} cm^{-3} — small compared to a metal's 10^{23}, but enough to make silicon a useful conductor under the right conditions. The ability to control this carrier density through doping is what makes semiconductors the foundation of modern electronics.

The boundary between "insulator" and "semiconductor" is not sharp — it is a matter of gap size and practical utility rather than a fundamental physical distinction. Materials with gaps larger than about 3-4 eV are usually called insulators, smaller gaps semiconductors. **Semimetals** (like bismuth and graphite) represent a fourth category where the gap is actually negative: bands overlap slightly, creating small pockets of both electrons and holes even at zero temperature. The richness of this classification — and its exceptions, including Mott insulators where strong electron-electron interactions open gaps that band theory misses — is what makes condensed matter physics endlessly interesting.
