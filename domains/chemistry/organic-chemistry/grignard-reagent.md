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
status: validated
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

## Questions

```yaml
- question: "A student reacts methylmagnesium bromide (CH₃MgBr) with acetaldehyde (CH₃CHO), then works up with dilute aqueous acid. What is the organic product?"
  type: multiple-choice
  options:
    - "Acetone — the Grignard adds a methyl group to give a ketone product"
    - "2-Propanol — the Grignard's nucleophilic carbon adds to the aldehyde carbonyl, giving a secondary alcohol after workup"
    - "1-Propanol — the reaction proceeds through a formaldehyde intermediate to give a primary alcohol"
    - "Propanal — the Grignard reduces the aldehyde while extending the chain by one carbon"
  answer: 1
  explanation: "RMgX + aldehyde → secondary alcohol. CH₃MgBr adds to CH₃CHO: the nucleophilic carbanion-like carbon attacks the electrophilic carbonyl carbon, forming a magnesium alkoxide with the C skeleton (CH₃)(CH₃)CHOMgBr. Acidic aqueous workup protonates the alkoxide to give 2-propanol (isopropanol), a secondary alcohol. Option A confuses nucleophilic addition with some kind of oxidation; the Grignard does not convert aldehydes to ketones — it adds to them."

- question: "A student wants to synthesize a product using a Grignard reagent, but the substrate molecule also contains a hydroxyl group on the carbon chain. What must the student do before forming the Grignard?"
  type: multiple-choice
  options:
    - "Proceed normally — the hydroxyl group will coordinate to magnesium and improve the reaction's selectivity"
    - "Protect the hydroxyl group, because the -OH proton will instantly destroy the C-Mg bond by protonolysis before any productive reaction can occur"
    - "Use a milder aryl Grignard instead of an alkyl Grignard, since aryl Grignards are less sensitive to protic groups"
    - "Cool the reaction to −78°C to slow the protonolysis so the Grignard reaction can compete kinetically"
  answer: 1
  explanation: "The C-Mg bond is one of the strongest nucleophiles in organic chemistry precisely because it behaves as a carbanion — and carbanions are instantly protonated by any source of acidic hydrogen. A hydroxyl group (pKa ~16) is far more acidic than what the Grignard requires; protonolysis is essentially instantaneous and irreversible. Cooling cannot slow this down. The only solution is to protect the OH group (e.g., as a THP ether or silyl ether) before introducing magnesium, then deprotect at the end. The same applies to NH and COOH groups."

- question: "When a Grignard reagent reacts with an ester, two equivalents of RMgX add to give a tertiary alcohol — the reaction does not stop at the ketone intermediate."
  type: true-false
  answer: true
  explanation: "The first addition of RMgX to an ester gives a tetrahedral intermediate that collapses by expelling the alkoxide leaving group, generating a ketone in situ. This ketone is actually more electrophilic and more reactive toward Grignard addition than the original ester. The still-present Grignard immediately adds again, and after acidic workup the product is a tertiary alcohol bearing two identical R groups from the two equivalents of RMgX. Attempts to stop at the ketone stage by using limiting Grignard typically fail — if a ketone product is desired, other organometallic reagents or lower-reactivity acyl equivalents must be used."

- question: "Diethyl ether is used as the solvent for Grignard reactions because it is chemically inert and does not interact with the reagent."
  type: true-false
  answer: false
  explanation: "Ether is far from inert in Grignard chemistry — it actively stabilizes the reagent through Lewis acid-base coordination. Magnesium is a Lewis acid; the ether oxygen lone pairs act as Lewis bases, coordinating to Mg and solvating the C-Mg bond. This solvation is essential for the reagent to form and remain stable. Without an ethereal solvent, Grignard reagents often cannot be prepared at all. 'Anhydrous and coordinative' is the accurate description. The critical requirement is that ether be rigorously dry (anhydrous), not that it be inert."

- question: "Describe the retrosynthetic logic for designing a Grignard synthesis. Given a target alcohol, how do you identify the required Grignard reagent and carbonyl compound?"
  type: short-answer
  answer: "In retrosynthesis, disconnect the C-C bond that was formed adjacent to the -OH group. The carbon bearing -OH was originally the electrophilic carbonyl carbon; the carbon on the other side of the disconnect came from the Grignard's R group (the carbanion equivalent). The alcohol class tells you which carbonyl substrate was used: a primary alcohol (RCH₂OH, excluding methanol) implies the Grignard added to formaldehyde; a secondary alcohol (RR'CHOH) implies addition to an aldehyde (R'CHO); a tertiary alcohol (RR'R''COH) implies addition to a ketone. Each target can often be disconnected in multiple ways, giving different valid synthetic routes. For example, 2-pentanol (a secondary alcohol) could be made from ethylmagnesium bromide + propanal, or from propylmagnesium bromide + acetaldehyde — either disconnection is valid."
```

## Explainer

From your study of covalent bonding and carbonyl chemistry, you know that the C=O bond is strongly polarized — the carbon is electrophilic (δ⁺) and the oxygen is nucleophilic (δ⁻). To form a new carbon-carbon bond at that electrophilic carbon, you need a carbon nucleophile — a carbon atom that carries significant negative character. That is exactly what a **Grignard reagent** provides. When you react an alkyl or aryl halide (like CH₃Br) with magnesium metal in dry diethyl ether, you get CH₃MgBr — a species where the carbon-magnesium bond is so polar (magnesium is far less electronegative than carbon) that the carbon effectively behaves as a **carbanion** (C⁻), one of the strongest nucleophiles in organic chemistry.

The synthetic power of Grignard reagents comes from their ability to add to different carbonyl substrates, each giving a predictable alcohol product. Think of it as a simple table: RMgX + formaldehyde (H₂C=O) → primary alcohol (RCH₂OH); RMgX + any other aldehyde (R'CHO) → secondary alcohol (RR'CHOH); RMgX + ketone (R'₂C=O) → tertiary alcohol (RR'₂COH). The mechanism is the same each time — the nucleophilic carbon of the Grignard attacks the electrophilic carbonyl carbon, pushing the π electrons onto oxygen to form a magnesium alkoxide, which is then protonated during an acidic aqueous workup to yield the free alcohol. You can also react Grignard reagents with CO₂ to make carboxylic acids and with epoxides to extend the carbon chain by two atoms.

The single most critical practical requirement is **rigorous exclusion of water and protic solvents**. The C–Mg bond is so reactive that even traces of water will destroy the reagent by simple protonolysis: RMgBr + H₂O → RH + Mg(OH)Br. This means every piece of glassware must be oven-dried, the ether solvent must be anhydrous, and the reaction must be performed under an inert atmosphere (nitrogen or argon). It also means you cannot have an –OH, –NH, or –COOH group anywhere in the same molecule as the C–Mg bond — those protons are just as acidic as water from the Grignard's perspective and will destroy the reagent internally.

Once you internalize the Grignard pattern, retrosynthetic analysis becomes much more powerful. Whenever you see a target alcohol, you can mentally disconnect the C–C bond adjacent to the hydroxyl group and ask: "Which Grignard and which carbonyl would combine to make this?" A secondary alcohol like 2-pentanol can be made from ethylmagnesium bromide + propanal, or from propylmagnesium bromide + acetaldehyde — two different disconnections, both valid. This flexibility in retrosynthetic planning is what makes the Grignard reaction one of the most important carbon-carbon bond-forming tools in the organic chemist's repertoire.
