---
id: radical-chain-reactions
title: Free Radical Halogenation and Chain Reactions
domain: chemistry
course: organic-chemistry
prerequisites:
- id: alkane-structure-and-properties
  type: hard
- id: bond-energy-and-enthaly
  type: soft
tags:
- free-radical
- halogenation
- selectivity
- chain-reaction
- initiation-propagation-termination
stage: advanced
status: draft
---

# Free Radical Halogenation and Chain Reactions

## Core Idea
Free radical halogenation (e.g., Cl₂, light) replaces alkane C-H bonds with C-X. The reaction proceeds via a chain mechanism: initiation (Cl₂ photolysis → Cl•), propagation (Cl• + RH → R• + HCl, then R• + Cl₂ → RCl + Cl•), and termination (radical coupling). Selectivity favors abstraction at more substituted C-H bonds because more substituted radicals are more stable. Multiple products form unless selectivity is exceptional.

## Explainer

You know from studying alkane structure that C–H bonds are strong and generally unreactive — alkanes are famously inert to most reagents. Radical halogenation is one of the few ways to functionalize these bonds, and it works by a fundamentally different mechanism than the polar reactions you may have encountered. Instead of nucleophiles attacking electrophiles, this reaction proceeds through **free radicals** — species with an unpaired electron that are highly reactive and seek to pair that electron by abstracting atoms from nearby molecules.

The mechanism unfolds in three distinct phases. **Initiation** creates the first radicals: UV light or heat breaks the weak Cl–Cl bond homolytically, producing two chlorine radicals (Cl•). Each Cl• then enters the **propagation** cycle, which is the engine of the reaction. In the first propagation step, Cl• abstracts a hydrogen from the alkane, forming HCl and a carbon radical (R•). In the second propagation step, R• attacks a Cl₂ molecule, forming the alkyl chloride product and regenerating Cl•. This regeneration is what makes it a chain reaction — a single initiation event can produce thousands of product molecules before the chain breaks. **Termination** occurs when two radicals encounter each other and combine, destroying the chain carriers. Because radicals are present at very low concentration, termination is statistically rare compared to propagation.

The selectivity of radical halogenation depends on two factors: the **stability of the carbon radical** formed and the **reactivity of the halogen radical**. Tertiary C–H bonds are abstracted more easily than secondary, which are easier than primary, because more substituted radicals are stabilized by hyperconjugation — the same electronic effect that stabilizes more substituted carbocations. With chlorination, however, the chlorine radical is so reactive that it does not discriminate strongly between C–H bond types. The selectivity ratio for Cl• is roughly 5:4:1 (tertiary:secondary:primary per hydrogen), which means a molecule like propane gives a substantial mixture of 1-chloropropane and 2-chloropropane. Bromine radicals are much less reactive and therefore far more selective (roughly 1600:80:1), so bromination gives predominantly the tertiary or secondary product.

Understanding the energetics through bond dissociation energies — a concept from your prerequisites — clarifies why this selectivity exists. The first propagation step is endothermic for chlorination (Cl• + R–H → HCl + R•) because the C–H bond being broken is stronger than the H–Cl bond being formed. A weaker C–H bond (tertiary) makes this step less endothermic, lowering the activation energy by the Hammond postulate. For bromination, the first propagation step is even more endothermic, so differences in C–H bond strength have a proportionally larger effect on the activation barrier — hence the dramatically higher selectivity. This connection between thermodynamics and kinetic selectivity is a pattern you will encounter repeatedly in organic chemistry.
