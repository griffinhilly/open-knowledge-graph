---
id: alcohol-oxidation-to-carbonyls
title: Oxidation of Alcohols to Aldehydes and Ketones
domain: chemistry
course: organic-chemistry
prerequisites:
- id: oxidation-reactions-organic
  type: soft
- id: nomenclature-oxygenated-compounds
  type: soft
builds-toward:
- carbonyl-reduction-to-alcohols
tags:
- oxidation
- alcohol
- aldehyde
- ketone
stage: formal-systems
status: validated
---

# Oxidation of Alcohols to Aldehydes and Ketones

## Core Idea
Primary alcohols are oxidized to aldehydes and further to carboxylic acids; secondary alcohols are oxidized to ketones; tertiary alcohols are not oxidized under standard conditions. Common oxidizing agents include Jones oxidation (Cr(VI) in H₂SO₄), Dess-Martin periodinane (DMP), and Swern oxidation, each with different functional group tolerance and selectivity.

## How It's Best Learned
Predict oxidation products for primary, secondary, and tertiary alcohols. Compare the selectivity and functional group compatibility of different oxidants to determine which is appropriate for a given substrate.

## Common Misconceptions
- Assuming all strong oxidizing agents produce identical results; DMP and Swern are milder and tolerate more acid-labile functional groups than Jones.
- Forgetting that primary alcohols can be over-oxidized to carboxylic acids under harsh conditions; controlled conditions favor the aldehyde.

## Questions

```yaml
- question: "A chemist needs to convert a primary alcohol to an aldehyde and must avoid any carboxylic acid product. Which reagent and conditions should they choose?"
  type: multiple-choice
  options:
    - "Jones oxidation (CrO₃ in aqueous H₂SO₄) — a powerful, reliable oxidant"
    - "PCC (pyridinium chlorochromate) in anhydrous CH₂Cl₂ — mild, non-aqueous conditions"
    - "Acidic potassium permanganate — strong oxidant for difficult substrates"
    - "Concentrated H₂SO₄ — dehydrates the alcohol to an alkene instead"
  answer: 1
  explanation: "PCC in anhydrous CH₂Cl₂ stops cleanly at the aldehyde because there is no water present to facilitate further oxidation of the aldehyde intermediate to a carboxylic acid. Jones oxidation is powerful but aqueous and acidic — the aldehyde is immediately over-oxidized to the carboxylic acid under those conditions. Acidic KMnO₄ similarly over-oxidizes. Concentrated H₂SO₄ is not an oxidant for this purpose. DMP and Swern oxidation are equally valid choices to PCC for this goal."

- question: "Why does oxidation of a secondary alcohol stop at the ketone stage, while oxidation of a primary alcohol can proceed further to a carboxylic acid?"
  type: multiple-choice
  options:
    - "Ketones are thermodynamically more stable products and resist further reaction"
    - "The ketone's carbonyl carbon has no remaining C–H bond, so there is no hydrogen to remove in a subsequent oxidation step"
    - "Secondary alcohols react more slowly with oxidizing agents than primary alcohols"
    - "Ketones immediately form stable hydrates that protect them from further oxidation"
  answer: 1
  explanation: "Oxidation of carbon involves removing hydrogen from the C–OH unit. An aldehyde (product of primary alcohol oxidation) still has one C–H at the carbonyl carbon — this is the handle for a second oxidation to carboxylic acid. A ketone has NO hydrogen on the carbonyl carbon (both bonds go to carbon substituents), so there is structurally nothing left to remove. The reaction simply cannot proceed further. Thermodynamic stability and reaction rate are not the correct mechanistic explanation."

- question: "A tertiary alcohol such as 2-methyl-2-propanol can be oxidized to a ketone if a sufficiently strong oxidizing agent is used."
  type: true-false
  answer: false
  explanation: "Tertiary alcohols have zero hydrogen atoms on the carbon bonded to the –OH group. Oxidation of a C–OH unit requires removing that C–H hydrogen to form the C=O double bond. With no such hydrogen available, the reaction simply cannot occur. No amount of oxidant strength overcomes this structural limitation under standard conditions. Tertiary alcohols resist oxidation unless the molecule undergoes degradation via entirely different mechanisms."

- question: "Under mild, anhydrous conditions such as PCC in dichloromethane, a primary alcohol is oxidized selectively to the aldehyde without further oxidation to the carboxylic acid."
  type: true-false
  answer: true
  explanation: "The key to stopping at the aldehyde is removing water from the system. In aqueous acidic conditions (Jones oxidation), the aldehyde intermediate is in equilibrium with its hydrate (geminal diol), which is then oxidized to the carboxylic acid. PCC in anhydrous CH₂Cl₂ eliminates this pathway: without water, no hydrate forms, and the aldehyde is the terminal product. DMP and Swern oxidation work by the same logic — mild, non-aqueous conditions prevent over-oxidation."

- question: "A student treats 2-methyl-2-propanol (a tertiary alcohol) with Jones oxidation conditions and observes no carbonyl product. Explain why."
  type: short-answer
  answer: "2-Methyl-2-propanol is a tertiary alcohol — the carbon bearing the –OH group has three carbon substituents and zero hydrogens. Oxidation of an alcohol to a carbonyl compound proceeds by removing a hydrogen from that carbon along with the –OH hydrogen to form the C=O double bond. With no C–H bond available at the carbinol carbon, there is nothing to abstract, and the oxidation cannot occur under standard conditions regardless of oxidant strength."
  explanation: "This question tests whether students understand that the structural classification of an alcohol (primary/secondary/tertiary) is not just a naming convention but directly determines what chemistry is possible. The number of hydrogens on the carbinol carbon controls oxidation reactivity. Jones oxidation is a strong enough oxidant that it would readily react if there were a C–H bond present — its failure here confirms the structural argument, not an issue of reagent potency."
```

## Explainer

From your study of oxidation reactions in organic chemistry, you know that oxidation of carbon involves increasing its bonds to oxygen (or other electronegative atoms) or decreasing its bonds to hydrogen. Alcohol oxidation is the most direct application of this principle: you are removing hydrogen atoms from the C–OH unit and forming a new C=O double bond. The classification of the alcohol — primary, secondary, or tertiary — determines what product is possible, because it determines how many hydrogens are available on the carbon bearing the –OH group.

A **primary alcohol** (RCH₂OH) has two hydrogens on the carbon bonded to oxygen. Removing one hydrogen from that carbon and one from the –OH gives an **aldehyde** (RCHO), which still has one C–H bond remaining at the carbonyl carbon. This remaining hydrogen makes the aldehyde vulnerable to further oxidation — a second round removes it to yield a **carboxylic acid** (RCOOH). A **secondary alcohol** (R₂CHOH) has only one hydrogen on the carbinol carbon, so oxidation produces a **ketone** (R₂C=O) and stops there, because there is no remaining C–H bond at the carbonyl to remove. A **tertiary alcohol** (R₃COH) has zero hydrogens on the carbinol carbon, so there is nothing to remove — tertiary alcohols resist oxidation under standard conditions.

The challenge with primary alcohols is controlling the reaction. If you use a powerful oxidant like chromic acid (**Jones oxidation** — CrO₃ in aqueous H₂SO₄), the aldehyde intermediate is immediately oxidized further to the carboxylic acid in the aqueous, acidic environment. When you specifically need the aldehyde, you turn to milder, non-aqueous oxidants. **Pyridinium chlorochromate (PCC)** in anhydrous CH₂Cl₂ stops cleanly at the aldehyde because there is no water to facilitate further oxidation. **Dess-Martin periodinane (DMP)** and the **Swern oxidation** (using oxalyl chloride and DMSO) are modern alternatives that work under mild, neutral conditions and tolerate acid-sensitive functional groups elsewhere in the molecule. Choosing the right oxidant is less about memorizing reagents and more about understanding what conditions enable or prevent over-oxidation.
