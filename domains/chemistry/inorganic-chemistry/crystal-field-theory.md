---
id: crystal-field-theory
title: Crystal Field Theory
domain: chemistry
course: inorganic-chemistry
prerequisites:
- id: coordination-chemistry-basics
  type: hard
- id: periodic-trends
  type: soft
builds-toward:
- spectrochemical-series
- color-spectroscopy-coordination-compounds
- magnetism-coordination-compounds
- ligand-field-theory
tags:
- crystal field theory
- d-orbital splitting
- octahedral field
- tetrahedral field
- square planar
stage: formal-systems
status: validated
---

# Crystal Field Theory

## Core Idea
Crystal field theory (CFT) explains the electronic structure of transition metal complexes by treating ligands as point charges that create an electrostatic field around the metal ion. This field splits the five degenerate d-orbitals into groups of different energy, and the pattern of splitting depends on the geometry of the complex. The magnitude of this splitting (Δ) determines the color, magnetism, and stability of the complex.

## Questions

```yaml
- question: "In an octahedral crystal field, which d-orbitals are raised to higher energy?"
  type: multiple-choice
  options:
    - "d_xy, d_xz, and d_yz (the t₂g set)"
    - "d_z² and d_x²−y² (the eg set)"
    - "All five d-orbitals are raised equally"
    - "Only d_z² is raised; the other four remain degenerate"
  answer: 1
  explanation: "In an octahedral field, six ligands approach along the x, y, and z axes. The d_z² and d_x²−y² orbitals (eg set) point directly at the ligands and experience strong electrostatic repulsion, raising their energy. The d_xy, d_xz, and d_yz orbitals (t₂g set) point between the ligand axes and experience less repulsion, placing them at lower energy. The energy gap between these two sets is the octahedral crystal field splitting parameter, Δ_oct (or 10Dq)."

- question: "A d⁶ metal ion in an octahedral field can be either high-spin (4 unpaired electrons) or low-spin (0 unpaired electrons). What determines which configuration is adopted?"
  type: multiple-choice
  options:
    - "The atomic number of the metal ion"
    - "The relative magnitudes of the crystal field splitting energy (Δ_oct) and the electron pairing energy (P)"
    - "Whether the complex is charged or neutral"
    - "The principal quantum number of the d-orbitals"
  answer: 1
  explanation: "The competition between Δ_oct and the pairing energy P determines spin state. If Δ_oct > P (strong-field ligands), electrons pair in the lower t₂g set before occupying the higher eg set — producing a low-spin configuration (t₂g⁶ eg⁰, zero unpaired electrons for d⁶). If Δ_oct < P (weak-field ligands), electrons maximize spin by occupying all five d-orbitals singly before pairing — giving a high-spin configuration (t₂g⁴ eg², four unpaired electrons for d⁶). The metal identity matters insofar as it affects Δ_oct (higher oxidation states and heavier metals give larger Δ), but the direct determinant is the Δ vs P comparison."

- question: "Tetrahedral crystal field splitting (Δ_tet) is approximately 4/9 of octahedral splitting (Δ_oct) for the same metal-ligand combination."
  type: true-false
  answer: true
  explanation: "Two factors make tetrahedral splitting smaller: there are only four ligands instead of six (reducing total electrostatic interaction), and the ligands do not point directly at any d-orbital (they approach between the axes). The combined geometric and numerical effect gives Δ_tet ≈ (4/9)Δ_oct. Because tetrahedral splitting is inherently smaller, it almost never exceeds the pairing energy — which is why tetrahedral complexes are nearly always high-spin."

- question: "In crystal field theory, the total energy of the d-electrons in a complex is always lower than in the free (spherically symmetric) ion, regardless of the electron configuration."
  type: true-false
  answer: false
  explanation: "CFT splitting is a redistribution of energy: the t₂g set drops by 0.4Δ_oct per electron while the eg set rises by 0.6Δ_oct per electron (in an octahedral field). The crystal field stabilization energy (CFSE) — the net energy lowering — depends on how electrons distribute. For configurations like d⁵ high-spin (t₂g³ eg²), CFSE is 3(−0.4Δ) + 2(+0.6Δ) = 0 — no net stabilization. For d¹⁰, CFSE is similarly zero. So not all configurations gain stabilization from the crystal field."

- question: "Explain why Cr³⁺ (d³) octahedral complexes are exceptionally kinetically inert, connecting your answer to crystal field stabilization energy."
  type: short-answer
  answer: "Cr³⁺ has the configuration t₂g³ in an octahedral field, with one electron in each of the three lower-energy orbitals. This gives a large CFSE of 3 × (−0.4Δ_oct) = −1.2Δ_oct. For any ligand substitution to occur, the complex must pass through a transition state with different geometry (five-coordinate or seven-coordinate), which necessarily changes the d-orbital splitting pattern and partially loses this CFSE. The large CFSE of t₂g³ means the activation energy for any geometry change is high, making ligand exchange slow — hence kinetic inertness. This is why Cr(III) complexes can be isolated as specific isomers that persist indefinitely at room temperature."
  explanation: "Kinetic inertness is distinct from thermodynamic stability. A complex can be thermodynamically unstable (the products are lower energy) but kinetically inert (the barrier to reaching those products is high). CFSE contributes to this barrier by stabilizing the ground-state geometry relative to any transition-state geometry."
```

## Explainer

In general chemistry, you learned that transition metal complexes display vivid colors and varied magnetic properties, and that these arise from the d-electrons. Crystal field theory provides the first quantitative model for understanding why. The central idea is surprisingly simple: treat the ligands not as bonding partners but as point negative charges arranged around the metal ion. These charges create an electrostatic field that interacts differently with different d-orbitals, breaking their degeneracy.

In a free transition metal ion, all five d-orbitals have the same energy. When six ligands approach along the Cartesian axes to form an octahedral complex, the d-orbitals that point directly at those ligands — d_z² and d_x²−y² (called the eg set) — experience stronger electron-electron repulsion and are pushed to higher energy. The three orbitals that point between the ligand positions — d_xy, d_xz, d_yz (the t₂g set) — experience less repulsion and drop to lower energy. The energy gap between these two sets is the crystal field splitting parameter, Δ_oct. This splitting is not a small perturbation — it dictates the color a complex absorbs (and therefore the color we see), how many unpaired electrons it has (and therefore its magnetic moment), and how readily it undergoes ligand substitution.

The interplay between Δ_oct and the pairing energy P creates the high-spin versus low-spin distinction. Consider a d⁶ ion like Fe²⁺. If the ligands produce a small Δ_oct (weak-field ligands like H₂O), the electrons distribute to maximize unpaired spins: four in t₂g and two in eg, giving four unpaired electrons and a paramagnetic complex. If Δ_oct is large (strong-field ligands like CN⁻), all six electrons pair in the t₂g set, giving zero unpaired electrons and a diamagnetic complex. The same metal ion shows completely different magnetic behavior depending on its ligands — a powerful demonstration that electronic structure in complexes depends on the entire metal-ligand system, not just the metal alone.

Tetrahedral and square planar geometries produce different splitting patterns. In a tetrahedron, the splitting is inverted (the e set is lower, the t₂ set is higher) and much smaller — only about 4/9 of the octahedral value for the same metal and ligands. This smaller splitting means tetrahedral complexes are almost always high-spin. Square planar geometry, favored by d⁸ ions like Pt²⁺ and Pd²⁺ with strong-field ligands, produces an extreme splitting that leaves one orbital far above the rest, naturally accommodating eight electrons in four orbitals with all spins paired. These geometric preferences and their electronic consequences form the foundation for understanding everything from the colors of gemstones to the mechanisms of catalytic reactions.
