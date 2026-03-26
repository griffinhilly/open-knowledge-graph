---
id: thermal-properties-of-materials
title: Thermal Properties of Materials
domain: engineering
course: materials-science
prerequisites:
- id: heat-transfer-conduction
  type: hard
- id: crystal-structure-basics
  type: soft
- id: thermal-expansion
  type: soft
- id: specific-heat-capacity
  type: soft
- id: heat-capacity-calorimetry
  type: soft
builds-toward:
- heat-treatment-of-steels
tags:
- thermal-conductivity
- thermal-expansion
- heat-capacity
- thermal-properties
stage: formal-systems
status: validated
---

# Thermal Properties of Materials

## Core Idea
Thermal properties — heat capacity, thermal conductivity, and thermal expansion coefficient — govern how materials respond to temperature changes and heat flow. Heat capacity reflects the energy stored in atomic vibrations (phonons); for most solids above room temperature, it approaches 3R per mole of atoms (Dulong-Petit law). Thermal conductivity in metals is dominated by electron transport; in ceramics and polymers, by phonon transport, making them better insulators. The thermal expansion coefficient quantifies lattice dilation and must be matched between joined dissimilar materials to avoid thermal stress cracking. These properties drive materials selection for heat sinks, thermal barrier coatings, and precision instruments.

## How It's Best Learned
Compare thermal conductivity values across metals, ceramics, and polymers and explain the differences in terms of dominant heat carriers. Calculate thermal stress in a bimetallic strip from the expansion coefficient mismatch.

## Common Misconceptions
- Diamond has the highest thermal conductivity of any material (higher than copper) because of its exceptionally stiff covalent bonds enabling efficient phonon transport, despite being an electrical insulator.
- A lower thermal expansion coefficient is not always desirable — it depends on the application and whether the material must be matched to a substrate.

## Questions

```yaml
- question: "An engineer selects a material for a heat sink that must rapidly conduct heat away from a processor. She considers copper, alumina (Al₂O₃ ceramic), and polyethylene. Which should she choose, and why?"
  type: multiple-choice
  options:
    - "Alumina — ceramics are denser and absorb heat more effectively than metals"
    - "Polyethylene — polymers have high specific heat so they store the most energy per kilogram"
    - "Copper — metals have free electrons that serve as efficient heat carriers, giving thermal conductivity orders of magnitude higher than ceramics or polymers"
    - "Alumina — it has a higher melting point than copper, so it survives high processor temperatures better"
  answer: 2
  explanation: "Thermal conductivity depends on the dominant heat carrier. In metals, free electrons carry thermal energy (the same electrons that carry electrical current), giving copper ~400 W/m·K. Ceramics like alumina rely on phonon transport — quantized lattice vibrations that scatter more readily than electrons — giving ~30 W/m·K. Polyethylene relies on even weaker phonon coupling through van der Waals chains, giving ~0.5 W/m·K. For a heat sink the goal is high conductivity to move heat fast, not high heat capacity to store it."

- question: "A steel shaft is fitted with a ceramic sleeve in a precision instrument. After repeated thermal cycling, cracks appear at the steel-ceramic interface. What is the most direct cause?"
  type: multiple-choice
  options:
    - "The ceramic fatigues more quickly than steel because it is less ductile"
    - "Steel has a higher thermal conductivity, so it heats and cools faster than the ceramic, creating a temperature gradient"
    - "Steel and ceramics have different thermal expansion coefficients — when heated, each tries to expand by a different amount but is constrained by the other, generating shear stress at the interface"
    - "Ceramics have higher heat capacity than steel, so they store more thermal energy and retain stress after cycling"
  answer: 2
  explanation: "Thermal stress at a bonded interface arises from expansion coefficient mismatch: σ ≈ E · Δα · ΔT. Steel has a thermal expansion coefficient of ~12 × 10⁻⁶ /°C; many structural ceramics are ~6-8 × 10⁻⁶ /°C. When the assembly heats up, steel wants to expand about twice as much but is constrained by the bonded ceramic. The resulting interfacial shear stress accumulates with each thermal cycle until it exceeds the bond or material strength. This is why matching thermal expansion coefficients is a critical design constraint in solder joints, turbine coatings, and glass-to-metal seals."

- question: "Diamond has higher thermal conductivity than copper despite being an electrical insulator, because its extremely stiff covalent bonds allow phonons to propagate very rapidly with minimal scattering."
  type: true-false
  answer: true
  explanation: "This is the most important exception to the 'metals are the best thermal conductors' rule. Diamond's thermal conductivity (~2000 W/m·K) is roughly five times higher than copper's (~400 W/m·K). Because diamond has no free electrons, its only heat carrier is phonons. However, the C-C covalent bond is among the stiffest in nature, and the low atomic mass of carbon produces phonons with very high velocity and long mean free path (little scattering). These two effects combine to give diamond exceptional phonon-mediated thermal conductivity — demonstrating that the mechanism (electron vs. phonon) does not predetermine the result; the quality of the phonon transport is what matters."

- question: "Materials with high thermal conductivity typically also have high electrical conductivity, because both properties rely on the same microscopic carriers."
  type: true-false
  answer: false
  explanation: "The Wiedemann-Franz law states that thermal and electrical conductivity track together in metals — because in metals, the same free electrons carry both. But this relationship breaks down for non-metals. Diamond is the definitive counterexample: it has the highest thermal conductivity of any known material but is an excellent electrical insulator with essentially zero free electrons. Its thermal conductivity comes from phonons, not electrons. The general rule (metals conduct both well; insulators conduct neither well) has real exceptions because the two properties have different microscopic mechanisms."

- question: "Why do ceramics and polymers generally have much lower thermal conductivity than metals, and what physical mechanism is responsible for the difference?"
  type: short-answer
  answer: "In metals, free electrons are the dominant heat carriers. Electrons move rapidly through the lattice and can transport thermal energy efficiently across macroscopic distances, giving metals thermal conductivities typically in the range of 10–400 W/m·K. Ceramics and polymers are electrical insulators with no free electrons, so they must rely on phonons — quantized lattice vibrations — as their only heat carriers. Phonons scatter at grain boundaries, defects, and lattice irregularities more readily than electrons, and their group velocities are generally lower. This makes phonon transport much less efficient, giving ceramics typically 1–30 W/m·K and polymers below 1 W/m·K. Diamond is the exception: its exceptionally stiff bonds and low atomic mass create unusually fast, long-range phonons despite having no free electrons."
  explanation: "Understanding the carrier type (electrons vs. phonons) is the key to predicting and designing thermal behavior across material classes. It explains why a metal heat sink outperforms a ceramic one of identical geometry, and why strategies to improve ceramic thermal conductivity focus on reducing phonon scattering (e.g., single-crystal growth, reducing defect density)."
```

## Explainer

From your study of heat conduction, you know that temperature gradients drive heat flow, and from specific heat capacity, you know that different materials store different amounts of thermal energy per degree of temperature rise. Thermal properties of materials extend this picture by connecting macroscopic thermal behavior to atomic-scale physics — and the atomic picture explains why metals, ceramics, and polymers behave so differently from one another.

**Heat capacity** (or specific heat, J/kg·K) measures how much energy a material absorbs per unit mass per degree of temperature increase. In a solid, thermal energy is stored in atomic vibrations — the atoms oscillate around their equilibrium positions, and each vibrational mode stores energy. The **Dulong-Petit law** predicts that at sufficiently high temperatures, each atom contributes 3kT of energy regardless of what element it is, giving a molar heat capacity of 3R ≈ 25 J/mol·K. This is why most metals have similar molar heat capacities. The practical specific heat (per kg) differs because atomic mass varies — lighter atoms mean more atoms per kilogram, so materials like aluminum have higher specific heat per kilogram than heavier metals like lead, even though both approach 3R per mole.

**Thermal conductivity** (W/m·K) measures how efficiently a material transports heat. This is where material classes diverge dramatically. In metals, free electrons are the dominant heat carriers — the same electrons that carry electrical current also carry thermal energy, which is why electrical and thermal conductivity track together in metals (Wiedemann-Franz law). In ceramics and crystalline insulators, there are no free electrons, so heat must be carried by **phonons** — quantized lattice vibrations. Phonon transport is less efficient than electron transport, making ceramics and polymers thermal insulators relative to metals. Diamond is the striking exception: its extremely stiff covalent bonds and lightweight carbon atoms create phonons that travel exceptionally fast and scatter very little, giving thermal conductivity ~5× higher than copper despite being an electrical insulator.

**Thermal expansion** arises from an asymmetry in interatomic potential: atoms are easier to push apart than to push together, so as they vibrate more vigorously at higher temperature, their average separation increases. Materials with deep, steep potential wells (strong, stiff bonds) expand less — ceramics and refractory metals have low thermal expansion coefficients; polymers with weak van der Waals forces expand dramatically. The engineering consequence is **thermal stress**: when two bonded materials with different expansion coefficients are heated or cooled, each wants to expand or contract by a different amount but is constrained by the other. The resulting stress is σ = E · Δα · ΔT, where Δα is the mismatch in expansion coefficients and E is the elastic modulus. This drives the design of solder joints in electronics, ceramic coatings on metal turbine blades, and glass-to-metal seals in vacuum systems — all of which require careful matching of expansion coefficients to survive thermal cycling without cracking.
