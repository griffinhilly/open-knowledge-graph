---
id: surface-chemistry-adsorption
title: Surface Chemistry and Adsorption
domain: chemistry
course: materials-chemistry
prerequisites:
- id: entropy-and-gibbs-free-energy
  type: hard
- id: chemical-equilibrium
  type: hard
- id: crystal-structures-and-unit-cells
  type: soft
- id: surface-chemistry-and-catalysis
  type: soft
builds-toward:
- catalytic-materials-design
- thin-film-deposition-cvd-pvd
tags:
- adsorption
- Langmuir-isotherm
- BET-isotherm
- surface-energy
- wetting
- chemisorption
- physisorption
stage: expert
status: validated
---

# Surface Chemistry and Adsorption

## Core Idea
Surface chemistry governs how atoms and molecules interact with the boundaries of materials. At a surface, atoms have unsatisfied bonds (dangling bonds), creating excess energy — the surface energy — that drives phenomena from crystal growth to catalysis to corrosion. Adsorption, the accumulation of molecules at a surface, is described quantitatively by isotherms: the Langmuir isotherm models monolayer chemisorption on uniform sites with constant binding energy, while the BET (Brunauer-Emmett-Teller) isotherm extends this to multilayer physisorption and is the standard method for measuring surface areas of porous materials. The distinction between chemisorption (electron sharing, bond formation, typically 40-400 kJ/mol) and physisorption (van der Waals attraction, typically 5-40 kJ/mol) determines whether a surface interaction activates a molecule for reaction or merely concentrates it. Wetting and contact angle connect surface energy to macroscopic behavior — whether a liquid spreads on a solid or beads up.

## Questions

```yaml
- question: "The Langmuir adsorption isotherm assumes: (1) a fixed number of equivalent adsorption sites, (2) each site holds at most one adsorbate molecule, (3) no interactions between adsorbed molecules. Under these assumptions, the fractional surface coverage theta = KP / (1 + KP), where K is the equilibrium constant and P is the gas pressure. At very high pressures, the Langmuir isotherm predicts that surface coverage continues to increase without limit."
  type: true-false
  answer: false
  explanation: "At very high pressures (KP >> 1), the Langmuir isotherm predicts theta approaches 1 — complete monolayer coverage — not unlimited adsorption. This saturation behavior is a defining feature of the Langmuir model: once every site is occupied, additional gas pressure cannot increase coverage. The shape of the isotherm is hyperbolic: rapid initial increase at low pressure (each molecule easily finds an empty site), then a plateau as sites fill up. This saturation distinguishes the Langmuir isotherm from the BET isotherm, which allows multilayer adsorption and shows coverage increasing beyond a monolayer at pressures approaching the saturation vapor pressure."

- question: "The BET method measures the surface area of a porous material by analyzing its nitrogen adsorption isotherm at 77 K. Why is nitrogen at 77 K used rather than, say, water vapor at room temperature?"
  type: short-answer
  answer: "Nitrogen at 77 K (its boiling point) provides physisorption that is reversible, uniform, and well-characterized. At this temperature, N2 molecules physisorb on essentially all surface types with a known cross-sectional area (0.162 nm2 per molecule), enabling straightforward conversion from monolayer capacity to surface area. The interaction is weak enough to be reversible (allowing adsorption-desorption isotherms) but strong enough for measurable coverage. Water vapor is unsuitable because water chemisorbs on many oxide surfaces, forms hydrogen-bonded clusters rather than uniform monolayers, and has an irregular cross-sectional area that varies with surface chemistry — all of which violate BET assumptions."
  explanation: "The BET method transforms an experimental isotherm into a surface area by determining the monolayer capacity (volume of gas needed to cover the surface one molecule deep) and multiplying by the known area per molecule. The BET equation linearizes the multilayer isotherm in the relative pressure range P/P0 = 0.05-0.35, where the model is most reliable. Below this range, micropore filling distorts the isotherm; above it, capillary condensation in mesopores adds non-surface-area contributions. Despite its simplifying assumptions, BET surface area is the universally accepted metric for comparing porous materials — catalysts, adsorbents, battery electrodes, and construction materials."

- question: "A material with a surface energy of 2000 mJ/m2 (e.g., a freshly cleaved metal oxide) is exposed to air. What happens to its surface, and why?"
  type: multiple-choice
  options:
    - "Nothing — high surface energy materials are stable in air"
    - "The surface immediately adsorbs water vapor, hydrocarbons, and other ambient molecules to lower its surface energy, forming a contamination layer within seconds. This is why ultra-high vacuum (UHV) is required for clean surface science experiments"
    - "The surface energy causes the material to spontaneously fracture into smaller pieces"
    - "The surface reconstructs by melting a thin layer at the surface"
  answer: 1
  explanation: "High surface energy is thermodynamically unfavorable — the system lowers its total energy by adsorbing molecules from the environment onto the surface, satisfying dangling bonds and replacing the high-energy solid-vacuum interface with lower-energy solid-adsorbate interfaces. A freshly cleaved metal oxide surface in air acquires a monolayer of water and hydrocarbons within seconds. This is why surface-sensitive techniques (XPS, LEED, STM) require ultra-high vacuum (< 10^-9 mbar): at atmospheric pressure, a surface is bombarded by ~10^23 molecules per cm2 per second, and even at 10^-6 mbar, a monolayer forms in about 1 second. Surface preparation (sputtering, annealing in UHV) is necessary to obtain atomically clean surfaces for study."
```

## Explainer

Every atom in the interior of a crystal is surrounded by neighbors on all sides, with all its bonding capacity satisfied. An atom at the surface, by contrast, has neighbors on one side only — the other side faces vacuum, gas, or liquid. These unsatisfied bonds represent excess energy, the **surface energy** (measured in J/m2 or equivalently N/m). This single quantity drives an enormous range of materials phenomena: crystal shapes (Wulff construction minimizes total surface energy), sintering (particles fuse to reduce surface area), catalysis (surfaces are reactive because of their unsatisfied bonds), and wetting (the balance of surface energies between solid, liquid, and vapor determines contact angle).

**Adsorption** is the process by which molecules from a gas or liquid phase accumulate at a surface. It comes in two fundamentally different types. **Physisorption** involves weak van der Waals forces (5-40 kJ/mol) — the same forces that cause gas condensation. It is reversible, non-specific (occurs on any surface), and can form multilayers. **Chemisorption** involves electron sharing or transfer, forming actual chemical bonds (40-400 kJ/mol). It is often irreversible at low temperatures, specific to particular surface-adsorbate combinations, and limited to a monolayer because it requires direct contact with surface atoms. The distinction matters enormously for catalysis: physisorbed molecules are merely concentrated at the surface; chemisorbed molecules have their bonds weakened or broken, making them available for reaction.

The **Langmuir isotherm** provides the simplest quantitative model: identical, independent sites, one molecule per site, coverage theta = KP/(1+KP). Despite its simplicity, it captures the essential physics of monolayer chemisorption and correctly predicts saturation at high pressure. The **BET isotherm** extends Langmuir to multilayer physisorption by treating each adsorbed molecule as a potential site for the next layer. The BET equation adds one parameter (the ratio of first-layer to multilayer binding energy) and predicts a characteristic S-shaped isotherm that matches experimental nitrogen adsorption data in the relative pressure range 0.05-0.35. From the monolayer capacity extracted by BET analysis and the known cross-sectional area of a nitrogen molecule (0.162 nm2), one obtains the specific surface area — the single most important characterization parameter for porous and nanostructured materials.

**Wetting** connects microscopic surface energetics to macroscopic behavior. Young's equation relates the contact angle of a liquid drop on a solid to three surface energies: solid-vapor, solid-liquid, and liquid-vapor. A contact angle near zero (complete wetting) means the solid-liquid interaction is strongly favorable — the liquid spreads to maximize contact area. A contact angle above 90 degrees (non-wetting) means the solid-liquid interaction is unfavorable relative to the solid-vapor and liquid-vapor interfaces. Surface modification — applying hydrophobic coatings, roughening surfaces, or functionalizing with self-assembled monolayers — manipulates wetting for applications from waterproof textiles to anti-fouling coatings to microfluidic devices. Surface chemistry is the foundation on which catalysis, thin-film deposition, corrosion science, and biomaterials engineering all rest.
