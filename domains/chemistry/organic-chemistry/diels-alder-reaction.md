---
id: diels-alder-reaction
title: The Diels-Alder Reaction
domain: chemistry
course: organic-chemistry
prerequisites:
- id: conjugated-dienes
  type: hard
builds-toward:
- retrosynthetic-analysis
tags:
- Diels-Alder
- cycloaddition
- pericyclic
- diene
- dienophile
- endo rule
- stereochemistry
- concerted
stage: formal-systems
status: draft
---
# The Diels-Alder Reaction

## Core Idea
The Diels-Alder reaction is a [4+2] cycloaddition in which a conjugated diene (4 pi electrons, in the s-cis conformation) reacts with a dienophile (2 pi electrons, typically bearing electron-withdrawing groups) to form a six-membered ring in a single concerted step with no intermediates. Because the mechanism is concerted and suprafacial, all stereorelationships in the starting materials are preserved in the product: cis substituents on the dienophile remain cis in the ring. The endo rule predicts that the major product places electron-withdrawing groups on the dienophile in the endo orientation (pointing toward the diene pi system) due to favorable secondary orbital interactions in the transition state.

## How It's Best Learned
Build the reaction from orbital symmetry: show HOMO(diene)-LUMO(dienophile) overlap and verify the suprafacial geometry. Practice predicting regiochemistry (1-substituted dienes + monosubstituted dienophiles give "ortho" and "para" products). Draw the endo and exo transition states explicitly and identify secondary orbital overlap to justify the endo rule.

## Common Misconceptions
- The diene must be in the s-cis conformation to react; s-trans dienes are unreactive in Diels-Alder reactions, which is why cyclopentadiene (locked s-cis) is exceptionally reactive.
- The endo rule predicts the kinetic product, not always the thermodynamic product — at high temperatures the exo product may dominate.
- The Diels-Alder reaction is reversible (retro-Diels-Alder) at high temperatures; this is not a side reaction but a fundamentally different equilibrium regime.

## Explainer

From your study of conjugated dienes, you know that alternating single and double bonds create an extended π system where electrons are delocalized across multiple carbons. The Diels-Alder reaction harnesses this delocalization in a remarkably elegant way: a **conjugated diene** (contributing 4 π electrons) reacts with a **dienophile** (contributing 2 π electrons) to form a new six-membered ring with one remaining double bond — a **[4+2] cycloaddition**. Two new σ bonds form simultaneously in a single concerted step, with no intermediates and no carbocations or anions along the way. This makes the Diels-Alder one of the most powerful ring-forming reactions in organic chemistry.

For the reaction to work, the diene must adopt the **s-cis conformation** — the two double bonds rotated so they point toward the same side, creating a crescent shape that can wrap around the dienophile. Dienes locked in the s-trans conformation (like a rigid trans-decalin fragment) simply cannot reach both ends of the dienophile simultaneously and are unreactive. This is why cyclopentadiene, which is permanently locked in the s-cis geometry, is one of the most reactive Diels-Alder dienes. The dienophile is typically an alkene bearing **electron-withdrawing groups** (EWGs) like carbonyls, nitriles, or nitro groups, which lower its LUMO energy and improve orbital overlap with the diene's HOMO. The better the HOMO(diene)–LUMO(dienophile) energy match, the faster the reaction proceeds.

Because the reaction is **concerted and suprafacial** — both new bonds form on the same face of each component — all stereochemical relationships in the starting materials are faithfully preserved in the product. If two substituents on the dienophile are cis to each other, they remain cis in the cyclohexene product. If they are trans, they stay trans. This stereochemical predictability is one reason the Diels-Alder is so valuable in synthesis. On top of this syn-addition stereochemistry, the **endo rule** adds another layer of selectivity: the major product places the dienophile's electron-withdrawing groups in the endo orientation (tucked underneath the newly forming ring, pointing toward the diene π system). This preference arises from stabilizing **secondary orbital interactions** in the transition state — overlap between the EWG's π orbitals and the diene's π system that does not form a bond but lowers the transition state energy.

When planning a Diels-Alder reaction, think backwards: look at a six-membered ring in your target molecule, identify the double bond that would remain after the cycloaddition, and mentally break the ring at the two bonds across from it. The two fragments you get are the diene and dienophile. This **retrosynthetic disconnection** is a cornerstone of synthesis planning. In the forward direction, electron-rich dienes paired with electron-poor dienophiles react fastest ("normal electron demand"), though inverse electron demand Diels-Alder reactions (electron-poor diene, electron-rich dienophile) are also important in advanced synthesis. The reaction is thermally allowed and typically requires only moderate heating — no catalysts, no radicals, no strong acids or bases — which contributes to its exceptional functional group tolerance.
