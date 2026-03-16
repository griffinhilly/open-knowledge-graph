---
id: alcohol-reactions
title: Reactions of Alcohols
domain: chemistry
course: organic-chemistry
prerequisites:
- id: alcohols-and-ethers
  type: hard
- id: sn1-reaction
  type: hard
- id: e2-elimination
  type: soft
- id: e1-elimination
  type: soft
builds-toward:
- carbonyl-chemistry-intro
tags:
- alcohols
- oxidation
- dehydration
- tosylate
- SOCl2
- PBr3
- PCC
stage: formal-systems
status: validated
---

# Reactions of Alcohols

## Core Idea
Alcohols are versatile synthetic intermediates that undergo four major reaction types. Dehydration (acid catalyst, heat) converts them to alkenes via E1 (tertiary) or E2 (secondary) mechanisms, following Zaitsev's rule. Conversion to alkyl halides uses SOCl₂ (gives inversion via SN2 with chloride) or PBr₃. Oxidation with PCC (mild) converts primary alcohols to aldehydes and secondary to ketones; stronger oxidants (KMnO₄, CrO₃) carry primary alcohols through to carboxylic acids. Tertiary alcohols resist oxidation because no alpha C–H bond is present. Conversion to tosylates activates the –OH as a leaving group for subsequent SN2 reactions.

## How It's Best Learned
Organize reactions in a grid: substrate class (1°, 2°, 3°) on one axis, reagent on the other, product in each cell. Practice retrosynthetic thinking: given a target molecule, which alcohol starting material and which reaction would give it?

## Common Misconceptions
- PCC stops oxidation at the aldehyde because it is used in anhydrous conditions that prevent hydration to the gem-diol, which would be further oxidized.
- Tertiary alcohol dehydration proceeds by E1, not E2, because the carbocation is especially stable — a strong non-nucleophilic base is not needed.
- SOCl₂ with pyridine gives retention of configuration (via chlorosulfite intermediate attacked by Cl⁻ intramolecularly); without pyridine the result can differ.

## Explainer

You already know that alcohols contain a hydroxyl group (–OH) bonded to an sp³ carbon, and you understand SN1, SN2, E1, and E2 mechanisms. The challenge with alcohols is that hydroxide (HO⁻) is a terrible leaving group — it is a strong base and simply will not depart on its own. Every major reaction class of alcohols is, at its core, a strategy for solving this leaving-group problem.

**Dehydration** is the elimination pathway. Adding a strong acid (H₂SO₄, H₃PO₄) protonates the –OH to give –OH₂⁺, converting it into water — an excellent leaving group. For tertiary alcohols, water departs first to form a carbocation (E1), which then loses a proton from the adjacent carbon to form the alkene. Zaitsev's rule predicts the more substituted alkene as the major product. Secondary alcohols can follow E1 or E2 depending on conditions, while primary alcohols typically require harsher conditions and may rearrange. The key mental model: protonate the oxygen, then apply the elimination mechanism appropriate to the substrate class.

**Conversion to alkyl halides** uses reagents that replace –OH with a halide while bypassing the poor leaving-group problem. SOCl₂ (thionyl chloride) converts alcohols to alkyl chlorides: it first forms a chlorosulfite ester intermediate, activating the oxygen as a leaving group, and then chloride attacks via SN2, giving inversion of configuration at the carbon. PBr₃ works analogously for bromides. These reagents are preferred over simply adding HBr or HCl because they give cleaner stereochemical outcomes and avoid the carbocation rearrangements that plague acid-catalyzed methods with secondary substrates. Converting the alcohol to a **tosylate** (by reacting with TsCl) is another activation strategy — the tosylate group is an outstanding leaving group that can then be displaced by any nucleophile via SN2.

**Oxidation** adjusts the oxidation state of the carbon bearing the –OH. Primary alcohols can be oxidized to aldehydes or all the way to carboxylic acids; secondary alcohols are oxidized to ketones; tertiary alcohols resist oxidation entirely because there is no hydrogen on the carbon bearing the hydroxyl to be removed. The reagent choice controls the outcome: **PCC** (pyridinium chlorochromate) in anhydrous CH₂Cl₂ stops at the aldehyde because without water, the aldehyde cannot hydrate to a gem-diol that would be further oxidized. Stronger oxidants like Jones reagent (CrO₃/H₂SO₄) or KMnO₄ push primary alcohols all the way to the carboxylic acid. The practical takeaway is a decision tree: identify the alcohol class, choose the reagent, predict the product.
