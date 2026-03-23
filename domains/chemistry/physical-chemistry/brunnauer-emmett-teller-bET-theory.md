---
id: brunnauer-emmett-teller-bET-theory
title: BET Theory and Multilayer Adsorption
domain: chemistry
course: physical-chemistry
prerequisites:
- id: langmuir-adsorption-model
  type: hard
- id: adsorption-thermodynamics-entropy
  type: hard
tags:
- bet
- adsorption
- multilayer
- surface-area
stage: advanced
status: validated
---

# BET Theory and Multilayer Adsorption

## Core Idea
The Brunauer-Emmett-Teller (BET) theory extends the Langmuir model to multilayer adsorption by assuming each adsorbed layer exhibits properties of bulk liquid (except the first layer, which binds to surface). This allows calculation of surface area from nitrogen adsorption isotherms, a standard characterization technique for porous materials and catalysts. BET surface area differs from geometric surface area when pores are present.

## Questions

```yaml
- question: "According to BET theory, what adsorption energy governs molecules in the second and higher layers?"
  type: multiple-choice
  options:
    - "The same surface adsorption energy as the first layer — BET treats all layers identically"
    - "Zero — molecules in upper layers are unbound and float above the surface"
    - "The energy of liquefaction — they interact with previously adsorbed molecules, not the surface itself"
    - "A gradually decreasing fraction of the first-layer energy, diminishing with each successive layer"
  answer: 2
  explanation: "This is BET theory's central distinguishing assumption. The first adsorbed layer binds directly to surface sites with a characteristic surface-molecule energy. All subsequent layers bind to already-adsorbed molecules with the energy of liquefaction — essentially the condensation enthalpy of the gas. BET extends Langmuir's site-based logic by treating each occupied first-layer site as a new 'surface' for the next layer, with bulk-liquid energetics beyond that point."

- question: "BET surface area measurements are unreliable for microporous materials like zeolites. What is the best explanation for this limitation?"
  type: multiple-choice
  options:
    - "Zeolites adsorb nitrogen so strongly that saturation occurs before an isotherm can be measured"
    - "BET assumes multilayer adsorption on a flat surface, but micropores are narrower than a few molecular diameters, preventing layered stacking"
    - "Zeolites are too dense for nitrogen gas to penetrate, so no adsorption occurs in the pores"
    - "The BET linear range requires P/P₀ between 0.35 and 0.7, a range zeolites never reach"
  answer: 1
  explanation: "BET theory assumes adsorption proceeds as stacked layers on an essentially flat surface. In micropores — cavities only 1–2 nm wide — the pore walls are so close together that pore filling occurs via capillary condensation, not layered adsorption. You cannot physically stack layers of nitrogen molecules when the pore is only a few molecular diameters across. BET still returns a number, but it is physically meaningless as 'surface area' in these materials."

- question: "BET theory assumes the first adsorbed layer has a stronger binding energy than all subsequent layers."
  type: true-false
  answer: true
  explanation: "The first layer is held by the surface-specific interaction energy — the same energy Langmuir modeled. All subsequent layers are held only by the energy of liquefaction (molecule-to-molecule interaction), which is weaker than the surface-molecule interaction when the BET constant C > 1. C quantifies this difference: when C >> 1, the first layer is tightly held and the isotherm has a pronounced knee at monolayer completion."

- question: "A material with a higher BET surface area necessarily has a larger geometric surface area visible under an optical microscope."
  type: true-false
  answer: false
  explanation: "BET surface area includes all surface accessible to nitrogen gas molecules, including internal pore walls of micropores and mesopores. A material can have tiny geometric surface area but enormous BET surface area if it is highly porous — activated carbon, for example, can reach 1000–3000 m²/g while appearing as dense black granules. The entire purpose of BET analysis is to quantify the internal pore surface where catalysis and adsorption actually occur, not the external geometric surface."

- question: "Why can't the Langmuir model describe adsorption isotherms at pressures approaching saturation (high P/P₀), and how does BET address this limitation?"
  type: short-answer
  answer: "The Langmuir model assumes a monolayer maximum: once every surface site is occupied, no further adsorption occurs and the isotherm levels off to a plateau. In reality, adsorption continues to increase at high P/P₀ as molecules begin to stack on top of already-adsorbed molecules. BET extends Langmuir by allowing each first-layer site to act as a substrate for further adsorption, with additional layers held by the energy of liquefaction. This lets BET describe the continued rise in adsorbed quantity at higher pressures, producing the characteristic Type II isotherm shape seen for most real materials."
  explanation: "Langmuir was designed for chemisorption where a true monolayer saturates. BET was specifically developed for physisorption at low temperatures (like N₂ at 77 K) where van der Waals forces drive multilayer buildup. Understanding which model applies requires knowing whether the adsorption is chemisorption (strong, selective, monolayer) or physisorption (weak, non-specific, multilayer)."
```

## Explainer

From the Langmuir adsorption model, you understand how gas molecules bind to a surface: each surface site can hold one molecule, and coverage increases with pressure until a monolayer saturates the surface. But real adsorption isotherms often do not level off cleanly at a monolayer — instead, the amount adsorbed keeps rising as molecules begin to stack on top of already-adsorbed molecules. The **BET theory** (Brunauer, Emmett, and Teller, 1938) extends the Langmuir framework to account for this **multilayer adsorption**, and it has become the standard method for measuring surface areas of catalysts, adsorbents, and porous materials.

The central assumption of BET theory is that the first layer of molecules adsorbs onto the surface with a characteristic energy of adsorption (related to the molecule-surface interaction), while each subsequent layer adsorbs with the energy of **liquefaction** — essentially, molecules in the second layer and beyond are sticking to other adsorbed molecules, not to the surface itself. This is a natural extension of Langmuir's site-based thinking: the first layer fills by the same equilibrium logic, but now each occupied site can serve as a new "surface" for the next layer. The result is the BET equation, which relates the amount adsorbed to the relative pressure P/P₀ (where P₀ is the saturation vapor pressure) and two parameters: the monolayer capacity (Vm) and the BET constant C, which reflects the strength of the surface-molecule interaction relative to molecule-molecule interactions.

In practice, you measure an adsorption isotherm by exposing your material to nitrogen gas at 77 K (liquid nitrogen temperature) and recording how much gas adsorbs at each pressure. The BET equation is then linearized: plotting P/[V(P₀ − P)] versus P/P₀ gives a straight line in the relative pressure range of roughly 0.05 to 0.35. The slope and intercept yield Vm and C. From Vm — the volume of gas needed to form exactly one complete monolayer — you calculate the **BET surface area** by multiplying the number of adsorbed molecules by the cross-sectional area of a single nitrogen molecule (0.162 nm²). This procedure is so standardized that "BET surface area" is essentially synonymous with surface area measurement in materials science.

The BET model has important limitations inherited from and beyond its Langmuir ancestry. It assumes a uniform, flat surface (no pore-size effects on layering), treats all layers beyond the first as identical to bulk liquid, and breaks down at very low pressures (where surface heterogeneity matters) and very high pressures (where capillary condensation in pores dominates). For microporous materials like zeolites, where pore widths are comparable to molecular diameters, the BET surface area can be physically misleading — it reports a number, but the concept of layered adsorption does not apply in pores only a few molecules wide. Despite these caveats, BET analysis remains indispensable because it provides a reproducible, comparable measure of available surface across vastly different materials.
