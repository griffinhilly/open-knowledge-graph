---
id: f-element-chemistry
title: f-Element Chemistry (Lanthanides and Actinides)
domain: chemistry
course: inorganic-chemistry
prerequisites:
- id: crystal-field-theory
  type: hard
- id: periodic-trends
  type: hard
- id: coordination-compounds-nomenclature
  type: soft
builds-toward: []
tags:
- lanthanides
- actinides
- f-orbitals
- rare earth
- nuclear chemistry
- lanthanide contraction
stage: expert
status: validated
---

# f-Element Chemistry (Lanthanides and Actinides)

## Core Idea
The f-block elements — lanthanides (4f) and actinides (5f) — have distinctive chemistry governed by the shielded, core-like nature of f-orbitals. Lanthanide chemistry is dominated by the +3 oxidation state, large coordination numbers (8-12), and ionic bonding, with minimal crystal field effects because f-orbitals have negligible overlap with ligands. Actinide chemistry, especially for early actinides (U, Np, Pu), shows greater oxidation state variability and more covalent character due to the more extended 5f orbitals. The lanthanide contraction — the steady decrease in ionic radius across the 4f series — has consequences that ripple through the entire periodic table.

## Questions

```yaml
- question: "Why do lanthanide ions show sharp f-f absorption bands in their electronic spectra, in contrast to the broad d-d bands of transition metal complexes?"
  type: multiple-choice
  options:
    - "Lanthanide f-electrons are in higher-energy orbitals, producing sharper transitions"
    - "The 4f orbitals are shielded by the 5s²5p⁶ outer shells, so the ligand environment has minimal effect on f-electron energies — transitions occur at nearly identical energies regardless of the ligand, producing sharp, atom-like bands"
    - "Lanthanide complexes have higher symmetry than d-block complexes"
    - "The Laporte selection rule does not apply to f-f transitions"
  answer: 1
  explanation: "The 4f orbitals are buried inside the xenon core, shielded by the filled 5s and 5p subshells. Ligands interact primarily with these outer electrons and barely perturb the 4f orbitals. The crystal field splitting of f-orbitals is only ~100 cm⁻¹ (compared to ~10,000-30,000 cm⁻¹ for d-orbitals in transition metals). Because the ligand environment barely affects f-orbital energies, the f-f transitions remain sharp and nearly constant across different complexes — resembling free-ion atomic spectra. This is why lanthanide ions have characteristic colors (Nd³⁺ purple, Er³⁺ pink, Pr³⁺ green) that are virtually independent of their coordination environment."

- question: "The lanthanide contraction causes the third-row transition metals (Hf, Ta, W, etc.) to have nearly identical ionic radii to their second-row counterparts (Zr, Nb, Mo, etc.)."
  type: true-false
  answer: true
  explanation: "As you cross the lanthanide series from La to Lu, each added 4f electron poorly shields the nucleus (f-orbitals have poor radial penetration). The effective nuclear charge experienced by outer electrons increases steadily, shrinking the ionic radius by about 0.01 Å per element — a total contraction of ~0.15 Å across 14 elements. This 'lanthanide contraction' almost exactly cancels the expected size increase from going from the 4d to the 5d transition series. As a result, Zr⁴⁺ and Hf⁴⁺ have nearly identical radii (0.72 vs 0.71 Å), making their chemistry very similar and making hafnium one of the last stable elements to be discovered."

- question: "Unlike lanthanides, early actinides (U, Np, Pu) commonly exhibit multiple stable oxidation states ranging from +3 to +6."
  type: true-false
  answer: true
  explanation: "The 5f orbitals in early actinides are more extended and higher in energy than the 4f orbitals in lanthanides, allowing them to participate more actively in bonding and to be removed in oxidation. Uranium commonly exists as U³⁺, U⁴⁺, U⁵⁺, and U⁶⁺; neptunium and plutonium show similar variability. As you move across the actinide series, the 5f orbitals contract and become more core-like — by americium and beyond, the chemistry resembles the lanthanides with +3 as the dominant oxidation state. The early actinide variability is exploited in nuclear fuel processing (separation of U, Pu, and fission products) and creates complex aqueous chemistry."

- question: "Explain why lanthanide complexes typically have high coordination numbers (8-12) and show little geometric preference, in contrast to transition metal complexes."
  type: short-answer
  answer: "Two factors combine: large ionic radii and negligible crystal field stabilization. Ln³⁺ ions are large (0.86-1.03 Å for the series), accommodating many ligands without excessive steric crowding. Since the 4f orbitals are shielded and barely interact with ligands, crystal field splitting is negligible (~100 cm⁻¹). Without CFSE to stabilize specific geometries (as it does in d-block complexes), the coordination geometry is determined almost entirely by ligand-ligand repulsion and packing efficiency, which for 8-12 ligands produces geometries like square antiprismatic, tricapped trigonal prismatic, or icosahedral — geometries rarely seen in d-block chemistry. The bonding is predominantly ionic/electrostatic, with ligand preferences dictated by HSAB (hard Ln³⁺ prefers hard O and F donors)."
  explanation: "This lack of geometric preference is why lanthanide complexes in solution are conformationally flexible and exchange ligands rapidly. It also explains why lanthanide coordination chemistry developed much later than transition metal coordination chemistry — the absence of strong spectroscopic and structural signatures made characterization more difficult."
```

## Explainer

The f-block elements occupy a unique chemical niche. The lanthanides (Ce through Lu) and actinides (Th through Lr) share the defining feature of progressively filling f-orbitals, but these orbitals behave very differently from the d-orbitals of transition metals. Understanding f-element chemistry requires recognizing both the similarities (they are still metallic elements that form cations and coordination compounds) and the fundamental differences (the f-orbitals are largely spectators in bonding, leading to ionic chemistry with minimal crystal field effects).

The 4f orbitals of the lanthanides are buried inside the xenon core, shielded from the external environment by the filled 5s² and 5p⁶ subshells. Ligands cannot effectively perturb these inner orbitals. Crystal field splitting of 4f levels is roughly 100 cm⁻¹ — two orders of magnitude smaller than for d-orbitals. This has several consequences: f-f electronic transitions produce sharp, atom-like absorption bands that barely change with the ligand environment; there is negligible CFSE, so coordination geometries are determined by size and electrostatics rather than orbital preferences; and magnetic properties follow the free-ion Russell-Saunders coupling scheme (including orbital contributions) rather than the spin-only model that works for first-row transition metals.

The lanthanide contraction — the steady decrease in ionic radius from La³⁺ (1.03 Å) to Lu³⁺ (0.86 Å) — has consequences far beyond the f-block. Each 4f electron added across the series poorly shields the increasing nuclear charge, causing the outer electrons to be drawn inward. This contraction accumulates across 14 elements and exactly cancels the expected size increase in the third transition series. As a result, second-row (4d) and third-row (5d) transition metals in the same group have nearly identical sizes — Zr/Hf, Nb/Ta, Mo/W — making them chemically almost indistinguishable and historically difficult to separate.

Actinide chemistry diverges from lanthanide chemistry in two key ways. First, the 5f orbitals are more extended and higher in energy, allowing them to participate in covalent bonding — especially for the early actinides (Th through Pu). This leads to oxidation state variability: uranium exists as U³⁺ through U⁶⁺, with the uranyl ion UO₂²⁺ being a distinctive linear dioxo cation with strong U-O multiple bonds. Second, the radioactivity of actinides beyond uranium adds both practical challenges (requiring specialized handling) and unique applications (nuclear energy, medical isotopes). The transition from covalent early-actinide chemistry to ionic late-actinide chemistry (Am³⁺ and beyond resemble Ln³⁺) mirrors the contraction of 5f orbitals across the series — a parallel to the lanthanide story at a deeper energy level.
