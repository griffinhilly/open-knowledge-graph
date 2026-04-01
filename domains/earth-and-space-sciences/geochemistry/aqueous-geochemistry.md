---
id: aqueous-geochemistry
title: Aqueous Geochemistry
domain: earth-and-space-sciences
course: geochemistry
prerequisites:
- id: geochemical-thermodynamics
  type: hard
- id: everyday-acids-and-bases
  type: soft
builds-toward:
- redox-geochemistry
- weathering-soil-chemistry
- isotope-hydrology
- environmental-geochemistry
tags:
- aqueous-solutions
- water-chemistry
- speciation
- mineral-dissolution
stage: expert
status: validated
---

# Aqueous Geochemistry

## Core Idea
Aqueous geochemistry describes the chemical behavior of dissolved species in natural waters -- rivers, groundwater, ocean, hydrothermal fluids. Water is the universal geological solvent, mediating mineral dissolution and precipitation, transporting elements, and hosting the reactions that drive weathering, diagenesis, and ore formation. Key concepts include aqueous speciation (how dissolved elements distribute among free ions, complexes, and ion pairs), activity versus concentration (the effective thermodynamic concentration in non-ideal solutions), saturation indices (whether a water will dissolve or precipitate a given mineral), and the master variables pH and pe (or Eh) that control speciation of virtually all dissolved species.

## Questions

```yaml
- question: "Groundwater analysis shows a saturation index (SI) of +0.5 for calcite. What does this indicate about the water's relationship to calcite?"
  type: multiple-choice
  options:
    - "The water is undersaturated and will dissolve calcite"
    - "The water is supersaturated with respect to calcite (SI > 0), meaning it has a thermodynamic driving force to precipitate calcite -- though whether precipitation actually occurs depends on kinetics and nucleation"
    - "The water is exactly at equilibrium with calcite"
    - "The water contains no calcium or carbonate"
  answer: 1
  explanation: "SI = log(IAP/Ksp), where IAP is the ion activity product and Ksp is the solubility product. SI > 0 means IAP > Ksp, so the solution is supersaturated. Thermodynamics predicts precipitation should occur to reduce the dissolved load. However, calcite supersaturation is common in natural waters because precipitation requires nucleation and crystal growth, which may be inhibited by dissolved organic matter, magnesium, or phosphate."

- question: "The concentration of a dissolved ion (in mg/L or molality) is the appropriate quantity to use in equilibrium calculations for natural waters."
  type: true-false
  answer: false
  explanation: "Equilibrium constants are defined in terms of activities, not concentrations. Activity = concentration x activity coefficient, where the activity coefficient accounts for ion-ion interactions in solution. In dilute waters, activities approximate concentrations (activity coefficients near 1). But in saline waters (seawater, brines, hydrothermal fluids), activity coefficients deviate significantly from 1 due to electrostatic interactions. Using concentrations instead of activities in equilibrium calculations produces incorrect speciation and saturation results for any water with significant ionic strength."

- question: "Explain why pH is considered a master variable in aqueous geochemistry."
  type: short-answer
  answer: "pH controls the speciation of virtually every weak acid and base in solution: carbonate species (CO2/HCO3-/CO3 2-), aluminum hydroxide complexes, silica species, phosphate species, and metal-hydroxide complexes all shift their dominant form depending on pH. It also controls mineral solubility -- many minerals (carbonates, hydroxides, sulfides) have pH-dependent solubility that varies by orders of magnitude. Additionally, pH couples to redox through the Nernst equation (H+ appears in most half-reactions). Because pH influences so many equilibria simultaneously, it is the single most diagnostic measurement for characterizing a natural water."
  explanation: "Knowing pH immediately constrains the speciation of carbonate, aluminum, iron, and most other dissolved species -- which is why it is measured first in any water analysis."
```

## Explainer

Water is the medium through which Earth's surface chemistry operates. Rain dissolves atmospheric CO2 to form carbonic acid, which attacks silicate and carbonate minerals. Groundwater carries dissolved ions through aquifers, precipitating minerals in some places and dissolving them in others. Hydrothermal fluids concentrate metals into ore deposits. Seawater maintains a remarkably stable composition through a balance of river inputs, biological uptake, hydrothermal exchange, and sedimentary removal. Understanding all of these processes requires aqueous geochemistry.

The concept of aqueous speciation is central. A dissolved element does not simply exist as a free ion -- it distributes among multiple chemical forms. Dissolved iron, for example, may exist as Fe2+, Fe3+, FeOH+, Fe(OH)2, FeCl+, FeSO4, and organic complexes, with the proportions controlled by pH, redox state, and the concentrations of ligands. The speciation determines the element's behavior: its toxicity, bioavailability, tendency to precipitate, and ability to be transported. Speciation modeling (using codes like PHREEQC, Geochemist's Workbench, or EQ3/6) is the primary computational tool of aqueous geochemistry.

The saturation index (SI) is the practical bridge between thermodynamics and observation. SI = log(IAP/Ksp) compares the actual ion activity product in a water sample to the equilibrium solubility product. SI < 0 means undersaturated (mineral dissolves), SI = 0 means equilibrium, SI > 0 means supersaturated (mineral precipitates). Calculating SI for a suite of minerals reveals which minerals control the water's composition and predicts how the water will react with its geological environment -- will it dissolve the limestone aquifer or deposit scale in the well casing?

The Eh-pH (or pe-pH) diagram is the geochemist's map for redox-sensitive systems. It plots the stability fields of dissolved species and solid phases as functions of oxidation state and acidity, revealing the dominant form of an element under any given conditions. Iron, for example, exists as dissolved Fe2+ in acidic reducing waters, dissolved Fe3+ in acidic oxidizing waters, and insoluble Fe(OH)3 in neutral-to-alkaline oxidizing waters. These diagrams predict what happens when groundwater encounters changing conditions -- entering an oxidizing zone, mixing with different water, or being modified by microbial activity.
