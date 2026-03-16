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

## Explainer

From the Langmuir adsorption model, you understand how gas molecules stick to a surface and how surface coverage depends on pressure and binding energy. Heterogeneous catalysis builds directly on this foundation: reactions happen *on* the surface, so understanding adsorption is understanding the first step of catalysis. The surface provides an alternative reaction pathway with a lower activation energy than the uncatalyzed gas-phase reaction — exactly the same idea as transition state theory applied to homogeneous catalysis, but now the transition state is stabilized by bonding interactions with the solid surface.

The three major mechanisms describe different ways reactants meet on or near the surface. In the **Langmuir-Hinshelwood mechanism**, both reactants adsorb onto the surface, diffuse until they find each other, and react. This is the most common mechanism and explains, for example, CO oxidation on platinum: both CO and O₂ adsorb, O₂ dissociates into adsorbed oxygen atoms, and adsorbed CO reacts with an adjacent adsorbed O atom to form CO₂, which desorbs. In the **Eley-Rideal mechanism**, one reactant adsorbs while the other reacts directly from the gas phase upon collision with the adsorbed species — rarer, but observed in some hydrogenation reactions. The **Mars-van Krevelen mechanism** is distinctive: a lattice atom from the catalyst itself (usually oxygen) participates in the reaction, leaving a vacancy that is later refilled by gas-phase oxygen. This mechanism dominates many industrial oxidation processes, such as the conversion of SO₂ to SO₃ on vanadium oxide catalysts.

The **Sabatier principle** provides the central design insight for choosing catalysts. If the surface binds reactants too weakly, coverage is negligible and few molecules are available to react. If the surface binds too strongly, products cannot desorb and the active sites remain permanently blocked. The optimum lies in between — strong enough to activate the reactant bonds, weak enough to release the products. When you plot catalytic activity against adsorption strength for a series of metals, you get a **volcano plot**: activity rises on the left (increasing binding stabilizes the transition state), peaks at the optimal binding energy, and falls on the right (product poisoning). Iron sits near the peak of the volcano for ammonia synthesis, which is why Fritz Haber and Carl Bosch chose it — not the most reactive metal, not the least, but the one that balances adsorption and desorption just right.

This framework makes catalyst design semi-rational rather than purely empirical. If your current catalyst is on the left side of the volcano (too weak binding), you can alloy it with a more reactive metal or add electron-donating promoters to strengthen adsorption. If it is on the right side (too strong), you can dilute it with an inert metal or modify the support to weaken binding. **Turnover frequency** (TOF) — the number of reaction cycles per active site per second — is the proper measure of intrinsic catalytic activity, separating the quality of each active site from the total number of sites available. Two catalysts may have identical TOFs but vastly different industrial performance if one has a much higher surface area, exposing more active sites per gram of material.
