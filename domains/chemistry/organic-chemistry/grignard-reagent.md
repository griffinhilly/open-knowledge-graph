---
id: grignard-reagent
title: Grignard Reagents
domain: chemistry
course: organic-chemistry
prerequisites:
- id: carbonyl-chemistry-intro
  type: hard
- id: covalent-bonding
  type: soft
builds-toward:
- retrosynthetic-analysis
tags:
- Grignard
- organometallic
- RMgX
- nucleophilic addition
- carbon-carbon bond
- moisture sensitivity
stage: formal-systems
status: draft
---
# Grignard Reagents

## Core Idea
A Grignard reagent (RMgX) is formed by reacting an alkyl or aryl halide with magnesium metal in anhydrous ether solvent. The resulting carbon-magnesium bond is highly polar, making the carbon strongly nucleophilic — effectively a stabilized carbanion. Grignard reagents react with aldehydes to give secondary alcohols, with ketones to give tertiary alcohols, with formaldehyde to give primary alcohols, with CO2 to give carboxylic acids, and with epoxides to give alcohols with an extended carbon chain. Because the C-Mg bond reacts instantly with water, all glassware and solvents must be rigorously dry — even atmospheric moisture will destroy the reagent.

## How It's Best Learned
Practice the full synthetic sequence: formation of RMgX, then nucleophilic addition to a carbonyl, then aqueous acid workup. For each carbonyl substrate, predict the alcohol product class. Draw the mechanism showing the carbanion-like carbon attacking the electrophilic carbonyl carbon. Work retrosynthesis problems where you must identify the Grignard and carbonyl fragments that combine to give a target alcohol.

## Common Misconceptions
- Grignard reagents are not compatible with protic functional groups (OH, NH, COOH) in the same molecule — the reagent would be destroyed by protonolysis before it could react with the carbonyl.
- The ether solvent is not inert — it stabilizes the Grignard reagent through coordination to magnesium. Without ether, the reagent often does not form.
- Grignard addition to esters does not stop at the ketone stage; two equivalents of RMgX add to give a tertiary alcohol because the initial tetrahedral intermediate collapses to a ketone that reacts again.

## Explainer

From your study of covalent bonding and carbonyl chemistry, you know that the C=O bond is strongly polarized — the carbon is electrophilic (δ⁺) and the oxygen is nucleophilic (δ⁻). To form a new carbon-carbon bond at that electrophilic carbon, you need a carbon nucleophile — a carbon atom that carries significant negative character. That is exactly what a **Grignard reagent** provides. When you react an alkyl or aryl halide (like CH₃Br) with magnesium metal in dry diethyl ether, you get CH₃MgBr — a species where the carbon-magnesium bond is so polar (magnesium is far less electronegative than carbon) that the carbon effectively behaves as a **carbanion** (C⁻), one of the strongest nucleophiles in organic chemistry.

The synthetic power of Grignard reagents comes from their ability to add to different carbonyl substrates, each giving a predictable alcohol product. Think of it as a simple table: RMgX + formaldehyde (H₂C=O) → primary alcohol (RCH₂OH); RMgX + any other aldehyde (R'CHO) → secondary alcohol (RR'CHOH); RMgX + ketone (R'₂C=O) → tertiary alcohol (RR'₂COH). The mechanism is the same each time — the nucleophilic carbon of the Grignard attacks the electrophilic carbonyl carbon, pushing the π electrons onto oxygen to form a magnesium alkoxide, which is then protonated during an acidic aqueous workup to yield the free alcohol. You can also react Grignard reagents with CO₂ to make carboxylic acids and with epoxides to extend the carbon chain by two atoms.

The single most critical practical requirement is **rigorous exclusion of water and protic solvents**. The C–Mg bond is so reactive that even traces of water will destroy the reagent by simple protonolysis: RMgBr + H₂O → RH + Mg(OH)Br. This means every piece of glassware must be oven-dried, the ether solvent must be anhydrous, and the reaction must be performed under an inert atmosphere (nitrogen or argon). It also means you cannot have an –OH, –NH, or –COOH group anywhere in the same molecule as the C–Mg bond — those protons are just as acidic as water from the Grignard's perspective and will destroy the reagent internally.

Once you internalize the Grignard pattern, retrosynthetic analysis becomes much more powerful. Whenever you see a target alcohol, you can mentally disconnect the C–C bond adjacent to the hydroxyl group and ask: "Which Grignard and which carbonyl would combine to make this?" A secondary alcohol like 2-pentanol can be made from ethylmagnesium bromide + propanal, or from propylmagnesium bromide + acetaldehyde — two different disconnections, both valid. This flexibility in retrosynthetic planning is what makes the Grignard reaction one of the most important carbon-carbon bond-forming tools in the organic chemist's repertoire.
