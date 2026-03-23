---
id: langmuir-adsorption-model
title: 'Adsorption Isotherms: Langmuir and BET Models'
domain: chemistry
course: physical-chemistry
prerequisites:
- id: chemical-equilibrium
  type: hard
- id: intermolecular-forces
  type: soft
- id: statistical-mechanics-foundations
  type: soft
builds-toward:
- surface-chemistry-and-catalysis
tags:
- adsorption
- Langmuir
- BET
- surface-coverage
- chemisorption
- physisorption
- isotherm
stage: formal-systems
status: validated
---

# Adsorption Isotherms: Langmuir and BET Models

## Core Idea
Adsorption isotherms describe how the amount of gas adsorbed on a surface varies with pressure at constant temperature. The Langmuir model assumes monolayer adsorption on equivalent, non-interacting sites at equilibrium: θ = Kp/(1+Kp), where θ is fractional surface coverage and K is the adsorption equilibrium constant. The BET (Brunauer-Emmett-Teller) model generalizes this to multilayer physisorption and is used to measure surface areas of porous materials. Chemisorption involves covalent bond formation (strong, irreversible) while physisorption involves weak van der Waals interactions (weak, reversible). The coverage-pressure relationship determines catalyst activity and selectivity in heterogeneous catalysis.

## How It's Best Learned
Fit the Langmuir equation to experimental isotherm data for CO on Pd or N₂ on silica. Extract K, compute ΔG_ads, and check linearity of the Langmuir linearization plot (p/n vs p). Compare BET plots for microporous vs mesoporous materials.

## Common Misconceptions
- Assuming the Langmuir model is always accurate; it fails for heterogeneous surfaces and when adsorbate-adsorbate interactions matter.
- Confusing adsorption (surface process) with absorption (bulk process).

## Questions

```yaml
- question: "A catalyst surface is exposed to increasing reactant pressure. At low pressures, the reaction rate doubles when pressure doubles. At very high pressures, further increases in pressure have no effect on the rate. What explains this transition?"
  type: multiple-choice
  options:
    - "At high pressures, the reactant molecules begin to repel each other on the surface, blocking adsorption"
    - "The surface sites become fully occupied (θ → 1), so all available sites are already used and adding more gas cannot increase the rate"
    - "High pressure causes desorption to dominate over adsorption, reversing the equilibrium"
    - "The reaction shifts from chemisorption to physisorption at high pressure, which is slower"
  answer: 1
  explanation: "This is the hallmark of Langmuir saturation behavior. At low pressure (Kp ≪ 1), θ ≈ Kp and rate ∝ θ ∝ p — first-order in pressure. At high pressure (Kp ≫ 1), θ → 1 — essentially all sites are occupied and adding more gas finds no empty sites, so rate becomes independent of pressure (zero-order). The surface has a fixed number of sites; once saturated, it cannot adsorb more. This is the direct physical meaning of the denominator (1 + Kp) in the Langmuir equation."

- question: "Which combination of assumptions is essential to the Langmuir adsorption model?"
  type: multiple-choice
  options:
    - "Multilayer adsorption, heterogeneous surface sites, and strong adsorbate-adsorbate interactions"
    - "Monolayer coverage only, equivalent and independent binding sites, and dynamic equilibrium between adsorption and desorption"
    - "Physisorption only, uniform temperature across the surface, and irreversible binding"
    - "Covalent bonding to the surface, sites with varying binding energies, and no desorption at equilibrium"
  answer: 1
  explanation: "The three core Langmuir assumptions are: (1) monolayer — each site holds at most one molecule, no stacking; (2) equivalent sites — every site has the same binding energy; and (3) dynamic equilibrium — adsorption and desorption occur at equal rates. Violating any of these sends you toward a different isotherm model. The BET model relaxes (1) to allow multilayers. The Freundlich isotherm is used for heterogeneous surfaces."

- question: "At low gas pressure, the Langmuir isotherm predicts that fractional surface coverage θ increases approximately linearly with pressure."
  type: true-false
  answer: true
  explanation: "At low pressure where Kp ≪ 1, the denominator (1 + Kp) ≈ 1, so θ = Kp/(1+Kp) ≈ Kp. Coverage is directly proportional to pressure — linear behavior. This is also called the Henry's law region of the isotherm. Physically, nearly all sites are empty, so every molecule that hits the surface finds an empty site, and coverage grows in direct proportion to the number of collisions (which is ∝ p)."

- question: "The BET model assumes adsorption is complete after one monolayer forms, at which point the isotherm levels off just like the Langmuir model."
  type: true-false
  answer: false
  explanation: "The BET model explicitly allows multilayer adsorption — this is its whole purpose and what distinguishes it from Langmuir. Once the first monolayer forms, additional molecules can adsorb on top of it through weaker van der Waals forces, with the second and subsequent layers behaving like condensation of the bulk liquid. The BET isotherm therefore does not level off but continues to rise with pressure, eventually diverging near the saturation vapor pressure. The Langmuir model levels off; BET does not."

- question: "The Langmuir adsorption equation θ = Kp/(1+Kp) is mathematically identical to the Michaelis-Menten enzyme kinetics equation v = Vmax[S]/(Km+[S]). What does this structural similarity reveal about the two systems?"
  type: short-answer
  answer: "Both equations describe reversible, saturable binding to a fixed number of equivalent, independent sites at equilibrium. In both cases, the denominator (1+Kp or Km+[S]) arises from the competition between occupied and unoccupied sites; the numerator reflects occupancy. The similarity reveals that the mathematics of surface adsorption and enzyme-substrate binding are governed by the same equilibrium logic: a fixed number of sites, reversible occupancy, and saturation when all sites are filled. The equilibrium constant K (adsorption) and 1/Km (enzyme affinity) play analogous roles."
  explanation: "This mathematical equivalence is not a coincidence — it reflects the same underlying physics of bimolecular reversible binding. Henri and Michaelis-Menten derived their equation independently of Langmuir, but both derived it from the same equilibrium condition: rate of binding = rate of unbinding. Recognizing this connection helps you transfer intuition across domains: enzyme inhibition curves, receptor binding studies, and adsorption isotherms all follow the same hyperbolic saturation form."
```

## Explainer

From chemical equilibrium, you know that a dynamic balance exists between forward and reverse reactions, and that the equilibrium position depends on thermodynamic quantities like ΔG and temperature. Adsorption applies this equilibrium concept to surfaces: gas molecules land on a solid surface (adsorb) and leave it (desorb), and at equilibrium, the rates of these two processes are equal. The **adsorption isotherm** describes how the amount of adsorbed gas depends on pressure at a fixed temperature — it is the surface-chemistry analog of a titration curve or a binding curve.

The **Langmuir model** is the simplest and most elegant treatment. It assumes the surface has a fixed number of equivalent, independent binding sites. Each site is either empty or occupied by exactly one molecule — no stacking allowed (monolayer coverage only). Adsorption is the forward reaction (gas molecule + empty site → occupied site) and desorption is the reverse. At equilibrium, the fractional surface coverage θ follows the equation θ = Kp/(1 + Kp), where K is the adsorption equilibrium constant and p is the gas pressure. At low pressure (Kp ≪ 1), θ increases linearly with pressure — every molecule that hits the surface finds an empty site. At high pressure (Kp ≫ 1), θ approaches 1 — the surface is saturated, and adding more gas has no effect. The characteristic shape is a curve that rises steeply and then levels off, much like enzyme saturation kinetics (Michaelis-Menten), which follows identical mathematics.

The **BET model** (Brunauer-Emmett-Teller) extends Langmuir to **multilayer adsorption**. In many real systems, once a monolayer forms, additional layers of gas molecules can stack on top through weaker van der Waals interactions. The BET isotherm accounts for this by allowing each adsorbed molecule to serve as a site for the next layer, with the first-layer binding energy differing from subsequent layers (which approximate the heat of liquefaction). The BET equation is widely used experimentally to measure the surface area of porous materials like catalysts and adsorbents: by fitting experimental data to the BET isotherm, you extract the monolayer capacity, which directly gives the surface area when multiplied by the cross-sectional area of the adsorbate molecule.

Understanding the distinction between **chemisorption** and **physisorption** helps you know which model applies. Chemisorption involves forming real chemical bonds between the adsorbate and surface (high binding energy, ~40–400 kJ/mol), is specific to particular surface-adsorbate pairs, and typically forms only a monolayer — Langmuir conditions. Physisorption involves weak van der Waals forces (~5–40 kJ/mol), is nonspecific, and readily forms multilayers — BET conditions. In heterogeneous catalysis, the reactant first chemisorbs (activating bonds), reacts on the surface, and then the product desorbs. The Langmuir isotherm directly enters catalytic rate laws: if the rate depends on surface coverage, and coverage depends on pressure through the Langmuir equation, you can derive rate expressions that transition from first-order (low pressure, θ ∝ p) to zero-order (high pressure, θ ≈ 1) behavior.
