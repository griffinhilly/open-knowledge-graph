---
id: oxidation-reactions-organic
title: Oxidation Reactions in Organic Chemistry
domain: chemistry
course: organic-chemistry
prerequisites:
- id: alcohol-reactions
  type: hard
- id: carbonyl-chemistry-intro
  type: soft
builds-toward:
- retrosynthetic-analysis
tags:
- oxidation
- PCC
- Jones reagent
- KMnO4
- Swern
- alcohol oxidation
- selectivity
stage: formal-systems
status: draft
---
# Oxidation Reactions in Organic Chemistry

## Core Idea
Oxidation of alcohols is the reverse of carbonyl reduction: primary alcohols can be oxidized to aldehydes or further to carboxylic acids, while secondary alcohols yield ketones. Tertiary alcohols resist oxidation because there is no hydrogen on the carbon bearing the OH. The reagent choice controls the oxidation level: PCC (pyridinium chlorochromate) and Swern oxidation stop at the aldehyde stage for primary alcohols, while Jones reagent (CrO3/H2SO4) and KMnO4 push primary alcohols all the way to carboxylic acids. Recognizing oxidation-state changes at carbon — counting bonds to oxygen and other electronegative atoms — is essential for planning synthetic sequences.

## How It's Best Learned
Assign oxidation states to carbon in an alcohol, aldehyde, and carboxylic acid to see the progression. Then match each transformation to the appropriate reagent. Work practice problems where you must select PCC vs Jones reagent based on the desired product. Draw the chromate ester mechanism for PCC oxidation to understand why a beta-hydrogen is required.

## Common Misconceptions
- Ketones cannot be oxidized further under normal conditions (no C-H to remove); attempting to oxidize a ketone with strong oxidant cleaves the molecule, which is a different reaction (Baeyer-Villiger).
- PCC stopping at the aldehyde is not because it is "weaker" — it works in anhydrous conditions (CH2Cl2) so the aldehyde cannot form a hydrate that would be further oxidized.
- KMnO4 can cleave alkenes (oxidative cleavage) in addition to oxidizing alcohols; the reaction conditions (cold, dilute vs hot, concentrated) determine the outcome.

## Explainer

From your study of alcohol reactions, you know that the hydroxyl group is a versatile functional group — it can be protonated, converted to a leaving group, or, as we explore here, oxidized to a higher oxidation state. **Oxidation** in organic chemistry means increasing the number of bonds between carbon and electronegative atoms (usually oxygen) or decreasing the number of C–H bonds. Think of it as climbing a ladder: a primary alcohol (one C–O bond) can step up to an aldehyde (two C–O bonds via a C=O), and then step up again to a carboxylic acid (three C–O bonds). A secondary alcohol climbs one rung to a ketone, but then the ladder ends — there is no C–H left on the carbonyl carbon to remove, so ketones resist further oxidation under normal conditions. Tertiary alcohols cannot even reach the first rung because they lack a hydrogen on the carbon bearing the OH.

The key practical skill is **reagent selection**. PCC (pyridinium chlorochromate) and Swern oxidation are the "controlled" reagents — they oxidize primary alcohols to aldehydes and stop there. Why do they stop? PCC works in anhydrous dichloromethane, and the aldehyde product cannot form the hydrate intermediate that would allow a second oxidation. Swern oxidation uses DMSO and oxalyl chloride at low temperature, activating the alcohol through a sulfonium intermediate and avoiding over-oxidation entirely. By contrast, **Jones reagent** (chromium trioxide in aqueous sulfuric acid) and hot concentrated KMnO4 are aggressive — the aqueous conditions allow the aldehyde to hydrate, exposing a new C–H bond that gets oxidized, pushing primary alcohols all the way to carboxylic acids.

A useful mental model is to think about the oxidation state of carbon as a number. Count bonds to electronegative atoms (O, N, halogen) as +1 each and bonds to hydrogen as −1 each. An alcohol carbon might be at oxidation state 0, an aldehyde at +1, and a carboxylic acid at +2. Each step up the ladder requires removing one C–H bond and forming one new C–O bond. When you see a synthesis problem asking you to convert a primary alcohol to an aldehyde, you know you need a selective, mild oxidant. When the target is a carboxylic acid, reach for Jones reagent or KMnO4. This oxidation-state bookkeeping becomes essential in retrosynthetic analysis, where you work backward from a target molecule and ask: what was the oxidation state of this carbon in my starting material, and which reagent gets me from there to here?

One subtlety worth noting: these reagent choices reflect a broader principle in organic synthesis — **selectivity is controlled by reaction conditions, not just reagent strength**. PCC is not inherently weaker than Jones reagent; it operates under conditions (anhydrous solvent) that prevent the side reaction leading to over-oxidation. This distinction between reagent reactivity and reaction conditions will appear repeatedly as you encounter more complex synthetic transformations.
