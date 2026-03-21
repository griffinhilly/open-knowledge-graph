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
stage: advanced
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

## Questions

```yaml
- question: "A student needs to convert a primary alcohol to an aldehyde for a synthesis. They choose Jones reagent (CrO₃/H₂SO₄), reasoning it is the most powerful and reliable chromium oxidant. What product do they most likely obtain?"
  type: multiple-choice
  options:
    - "The desired aldehyde — Jones reagent is selective for the first oxidation"
    - "A carboxylic acid — Jones reagent over-oxidizes primary alcohols past the aldehyde stage"
    - "A ketone — Jones reagent rearranges primary alcohols under acidic conditions"
    - "No reaction — Jones reagent only oxidizes secondary alcohols"
  answer: 1
  explanation: "Jones reagent operates in aqueous acidic conditions, which allows the aldehyde product to hydrate into a geminal diol. That diol has a new C–H bond that gets oxidized, pushing the reaction all the way to a carboxylic acid. The student should have used PCC or Swern oxidation — not because they are 'weaker,' but because they work in anhydrous conditions that prevent aldehyde hydration and therefore prevent over-oxidation."

- question: "Why does PCC stop the oxidation of a primary alcohol at the aldehyde stage rather than continuing to the carboxylic acid?"
  type: multiple-choice
  options:
    - "PCC contains less chromium and therefore runs out of oxidizing capacity after the first step"
    - "PCC cannot react with aldehydes or ketones at all"
    - "PCC is used in anhydrous CH₂Cl₂, preventing the aldehyde from forming a hydrate intermediate that would expose a new C–H for oxidation"
    - "The pyridine in PCC acts as a proton scavenger that deactivates the chromium after one oxidation"
  answer: 2
  explanation: "The key is conditions, not intrinsic strength. In anhydrous CH₂Cl₂, the aldehyde product cannot form a geminal diol hydrate, so there is no new C–H bond for further oxidation. Jones reagent, by contrast, operates in aqueous conditions where hydrate formation is possible, enabling the second oxidation to carboxylic acid. This illustrates the broader principle: selectivity is controlled by reaction conditions, not reagent 'strength' alone."

- question: "Tertiary alcohols resist oxidation under normal conditions because they lack a hydrogen atom on the carbon bearing the hydroxyl group."
  type: true-false
  answer: true
  explanation: "Oxidation of an alcohol to a carbonyl requires removal of the C–H bond on the carbon that bears the OH. Primary alcohols have two such hydrogens, secondary alcohols have one, and tertiary alcohols have none — the carbon is fully substituted. With no C–H to remove, the oxidation cannot proceed by the standard chromate ester mechanism. Strong oxidants like hot concentrated KMnO₄ can cleave the C–C bond instead, but this is a different reaction (oxidative cleavage), not simple alcohol oxidation."

- question: "PCC is a weaker oxidant than Jones reagent, which is why it stops at the aldehyde stage when oxidizing primary alcohols."
  type: true-false
  answer: false
  explanation: "This is the central misconception. PCC stops at the aldehyde not because of inherent weakness but because of reaction conditions. PCC is used in anhydrous dichloromethane, which prevents the aldehyde from hydrating into a geminal diol intermediate. Without that hydrate, the second oxidation cannot occur. Jones reagent in aqueous acid allows hydration, enabling over-oxidation. The principle: the same transformation at a different oxidation state becomes accessible because the conditions change what intermediates are available."

- question: "In terms of oxidation-state bookkeeping, explain the progression from a primary alcohol → aldehyde → carboxylic acid. What changes at each step, and why does this progression stop at the carboxylic acid stage?"
  type: short-answer
  answer: "At each step, one C–H bond is broken and one new C–O bond forms, increasing the carbon's oxidation state by approximately +1. A primary alcohol carbon (one C–O bond, two C–H bonds) steps up to an aldehyde (two C–O bonds via C=O, one C–H). The aldehyde then steps up to a carboxylic acid (two C–O bonds plus an OH, no C–H on the carbonyl carbon). The progression stops at the carboxylic acid because the carbonyl carbon no longer has any C–H bonds to remove — the ladder has no more rungs. Further oxidation would require C–C bond cleavage."
  explanation: "This oxidation-state framework is the essential tool for retrosynthetic analysis: working backward from a target, you ask what oxidation state the relevant carbon was in the starting material and which reagent achieves that specific transition. PCC for +1 step (alcohol → aldehyde), Jones for +2 steps (alcohol → carboxylic acid). Recognizing that each oxidation step consumes one C–H bond is what makes tertiary alcohol resistance immediately intuitive — no C–H, no oxidation."
```

## Explainer

From your study of alcohol reactions, you know that the hydroxyl group is a versatile functional group — it can be protonated, converted to a leaving group, or, as we explore here, oxidized to a higher oxidation state. **Oxidation** in organic chemistry means increasing the number of bonds between carbon and electronegative atoms (usually oxygen) or decreasing the number of C–H bonds. Think of it as climbing a ladder: a primary alcohol (one C–O bond) can step up to an aldehyde (two C–O bonds via a C=O), and then step up again to a carboxylic acid (three C–O bonds). A secondary alcohol climbs one rung to a ketone, but then the ladder ends — there is no C–H left on the carbonyl carbon to remove, so ketones resist further oxidation under normal conditions. Tertiary alcohols cannot even reach the first rung because they lack a hydrogen on the carbon bearing the OH.

The key practical skill is **reagent selection**. PCC (pyridinium chlorochromate) and Swern oxidation are the "controlled" reagents — they oxidize primary alcohols to aldehydes and stop there. Why do they stop? PCC works in anhydrous dichloromethane, and the aldehyde product cannot form the hydrate intermediate that would allow a second oxidation. Swern oxidation uses DMSO and oxalyl chloride at low temperature, activating the alcohol through a sulfonium intermediate and avoiding over-oxidation entirely. By contrast, **Jones reagent** (chromium trioxide in aqueous sulfuric acid) and hot concentrated KMnO4 are aggressive — the aqueous conditions allow the aldehyde to hydrate, exposing a new C–H bond that gets oxidized, pushing primary alcohols all the way to carboxylic acids.

A useful mental model is to think about the oxidation state of carbon as a number. Count bonds to electronegative atoms (O, N, halogen) as +1 each and bonds to hydrogen as −1 each. An alcohol carbon might be at oxidation state 0, an aldehyde at +1, and a carboxylic acid at +2. Each step up the ladder requires removing one C–H bond and forming one new C–O bond. When you see a synthesis problem asking you to convert a primary alcohol to an aldehyde, you know you need a selective, mild oxidant. When the target is a carboxylic acid, reach for Jones reagent or KMnO4. This oxidation-state bookkeeping becomes essential in retrosynthetic analysis, where you work backward from a target molecule and ask: what was the oxidation state of this carbon in my starting material, and which reagent gets me from there to here?

One subtlety worth noting: these reagent choices reflect a broader principle in organic synthesis — **selectivity is controlled by reaction conditions, not just reagent strength**. PCC is not inherently weaker than Jones reagent; it operates under conditions (anhydrous solvent) that prevent the side reaction leading to over-oxidation. This distinction between reagent reactivity and reaction conditions will appear repeatedly as you encounter more complex synthetic transformations.
