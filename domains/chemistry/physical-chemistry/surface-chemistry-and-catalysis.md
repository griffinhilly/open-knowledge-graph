---
id: surface-chemistry-and-catalysis
title: Surface Chemistry and Heterogeneous Catalysis
domain: chemistry
course: physical-chemistry
prerequisites:
- id: langmuir-adsorption-model
  type: hard
- id: reaction-mechanisms-overview
  type: soft
- id: transition-state-theory
  type: soft
tags:
- heterogeneous-catalysis
- Langmuir-Hinshelwood
- Eley-Rideal
- Mars-van-Krevelen
- turnover-frequency
- surface-science
stage: advanced
status: validated
---

# Surface Chemistry and Heterogeneous Catalysis

## Core Idea
Heterogeneous catalysis involves reactions between molecules adsorbed on (or reacting with) a solid surface. Three primary mechanisms are the Langmuir-Hinshelwood mechanism (both reactants adsorb and react on the surface), the Eley-Rideal mechanism (one reactant adsorbs, the other reacts from the gas phase), and the Mars-van Krevelen mechanism (lattice oxygen participates in the reaction). The Sabatier principle states that optimal catalysts bind adsorbates with intermediate strength — too weak and coverage is too low; too strong and products cannot desorb. Volcano plots (activity vs adsorption energy) embody this principle and guide rational catalyst design.

## How It's Best Learned
Study the ammonia synthesis mechanism (Haber process) as an example: N₂ dissociative adsorption is rate-limiting, iron is near the volcano peak, and promoters shift the binding energy. Then analyze an industrial oxidation reaction using Mars-van Krevelen.

## Common Misconceptions
- Thinking a catalyst that binds the substrate very strongly must be very active; strong binding blocks desorption of products.
- Confusing turnover frequency (TOF, rate per active site) with overall activity; two catalysts can have the same TOF but different total activities due to different surface areas.

## Questions

```yaml
- question: "A research team tests a series of transition metals for a catalytic reaction and finds that osmium (which binds the substrate very strongly) shows very low activity despite high surface coverage of the reactant. How does the Sabatier principle explain this?"
  type: multiple-choice
  options:
    - "Osmium has too few surface atoms to provide adequate active sites for the reaction"
    - "Osmium's strong binding prevents product desorption, leaving active sites permanently blocked"
    - "Osmium binds the substrate too weakly, so surface coverage remains negligible"
    - "Osmium does not participate in the Langmuir-Hinshelwood mechanism and thus cannot catalyze the reaction"
  answer: 1
  explanation: "The Sabatier principle states that optimal catalysts bind adsorbates with intermediate strength. Osmium sits on the right (strong-binding) side of the volcano plot. While it adsorbs and activates the substrate readily — which is why coverage is high — the products also bind strongly and cannot desorb, leaving active sites permanently occupied. The rate-limiting step becomes product release, not substrate activation. This is the opposite failure mode from weak binding (left of volcano), where the substrate barely sticks. Strong binding sounds beneficial but poisons the catalyst."

- question: "In the industrial oxidation of SO₂ to SO₃ on vanadium oxide, an oxygen atom from the catalyst lattice is incorporated into the SO₃ product, leaving an oxygen vacancy that is subsequently refilled by gas-phase O₂. Which heterogeneous catalysis mechanism does this describe?"
  type: multiple-choice
  options:
    - "Langmuir-Hinshelwood — both SO₂ and O₂ adsorb on the surface and then react with each other"
    - "Eley-Rideal — SO₂ adsorbs on the surface and then reacts with gas-phase O₂ directly"
    - "Mars-van Krevelen — a lattice atom from the catalyst itself participates in the reaction"
    - "Sabatier mechanism — the reaction proceeds through a surface intermediate of optimal binding strength"
  answer: 2
  explanation: "Mars-van Krevelen is distinctive because the catalyst is a reactant, not merely a surface. Lattice oxygen from vanadium oxide becomes part of the product (SO₃), leaving a vacancy, which is then re-oxidized by gas-phase O₂. This differs from LH (both reactants adsorb first, then react on the surface) and ER (one adsorbs, the other reacts from the gas phase without adsorbing). 'Sabatier mechanism' is not a named mechanism — the Sabatier principle is a design guideline about optimal binding strength, not a description of how reactants meet."

- question: "A catalyst on the weak-binding (left) side of a volcano plot can in principle be improved by adding electron-donating promoters or alloying with a more reactive metal."
  type: true-false
  answer: true
  explanation: "True. If a catalyst is on the weak-binding side, low surface coverage is the limiting factor — reactants barely stick, so few are available to react. Electron-donating promoters strengthen the metal–adsorbate bond, increasing coverage and moving the catalyst toward the volcano peak. Alloying with a more reactive metal has the same effect. This is the practical payoff of the Sabatier principle and volcano framework: knowing which side of the peak you're on reveals the direction to push binding energy for improvement."

- question: "Two heterogeneous catalysts with identical turnover frequencies (TOF) will necessarily show the same catalytic activity per gram of material."
  type: true-false
  answer: false
  explanation: "False. Turnover frequency measures rate per active site — it is a measure of intrinsic site quality. Activity per gram also depends on the number of active sites, which is determined by surface area and active site density. A catalyst with the same TOF but 10× higher BET surface area (e.g., from smaller particle size) will produce 10× more product per gram per second. TOF separates these two contributions: a catalyst can have excellent intrinsic activity (high TOF) but poor industrial performance due to low surface area, or vice versa. Conflating TOF with overall activity is a common source of error in comparing catalysts."

- question: "Explain why volcano plots peak at intermediate binding energy rather than at the maximum binding strength, using the distinction between adsorption and desorption steps."
  type: short-answer
  answer: "At very low binding energy, reactants barely adsorb and surface coverage is negligible — almost no molecules are available on the surface to react. Activity is low because the catalyst cannot hold onto its reactants. At very high binding energy, reactants adsorb strongly and coverage is high, but products also bind strongly and cannot desorb, permanently blocking active sites. Activity is again low because the catalyst cannot release its products. Peak activity occurs at the intermediate binding energy where there is sufficient coverage to drive the reaction AND products desorb quickly enough to regenerate active sites for the next cycle. The volcano reflects a fundamental kinetic competition between activation and regeneration."
  explanation: "The volcano shape is an empirical confirmation that catalysis requires cycle completion — after each reaction, the product must leave so a new reactant can take its place. Both extremes break the catalytic cycle in different ways: weak binding breaks it at the adsorption step, strong binding breaks it at the desorption step. The Sabatier principle names the optimum; volcano plots locate it experimentally for different metal–adsorbate systems."
```

## Explainer

From the Langmuir adsorption model, you understand how gas molecules stick to a surface and how surface coverage depends on pressure and binding energy. Heterogeneous catalysis builds directly on this foundation: reactions happen *on* the surface, so understanding adsorption is understanding the first step of catalysis. The surface provides an alternative reaction pathway with a lower activation energy than the uncatalyzed gas-phase reaction — exactly the same idea as transition state theory applied to homogeneous catalysis, but now the transition state is stabilized by bonding interactions with the solid surface.

The three major mechanisms describe different ways reactants meet on or near the surface. In the **Langmuir-Hinshelwood mechanism**, both reactants adsorb onto the surface, diffuse until they find each other, and react. This is the most common mechanism and explains, for example, CO oxidation on platinum: both CO and O₂ adsorb, O₂ dissociates into adsorbed oxygen atoms, and adsorbed CO reacts with an adjacent adsorbed O atom to form CO₂, which desorbs. In the **Eley-Rideal mechanism**, one reactant adsorbs while the other reacts directly from the gas phase upon collision with the adsorbed species — rarer, but observed in some hydrogenation reactions. The **Mars-van Krevelen mechanism** is distinctive: a lattice atom from the catalyst itself (usually oxygen) participates in the reaction, leaving a vacancy that is later refilled by gas-phase oxygen. This mechanism dominates many industrial oxidation processes, such as the conversion of SO₂ to SO₃ on vanadium oxide catalysts.

The **Sabatier principle** provides the central design insight for choosing catalysts. If the surface binds reactants too weakly, coverage is negligible and few molecules are available to react. If the surface binds too strongly, products cannot desorb and the active sites remain permanently blocked. The optimum lies in between — strong enough to activate the reactant bonds, weak enough to release the products. When you plot catalytic activity against adsorption strength for a series of metals, you get a **volcano plot**: activity rises on the left (increasing binding stabilizes the transition state), peaks at the optimal binding energy, and falls on the right (product poisoning). Iron sits near the peak of the volcano for ammonia synthesis, which is why Fritz Haber and Carl Bosch chose it — not the most reactive metal, not the least, but the one that balances adsorption and desorption just right.

This framework makes catalyst design semi-rational rather than purely empirical. If your current catalyst is on the left side of the volcano (too weak binding), you can alloy it with a more reactive metal or add electron-donating promoters to strengthen adsorption. If it is on the right side (too strong), you can dilute it with an inert metal or modify the support to weaken binding. **Turnover frequency** (TOF) — the number of reaction cycles per active site per second — is the proper measure of intrinsic catalytic activity, separating the quality of each active site from the total number of sites available. Two catalysts may have identical TOFs but vastly different industrial performance if one has a much higher surface area, exposing more active sites per gram of material.
