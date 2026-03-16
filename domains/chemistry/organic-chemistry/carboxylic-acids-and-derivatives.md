---
id: carboxylic-acids-and-derivatives
title: Carboxylic Acids and Their Derivatives
domain: chemistry
course: organic-chemistry
prerequisites:
- id: carbonyl-chemistry-intro
  type: hard
- id: acid-base-chemistry
  type: hard
- id: nucleophilic-addition-to-carbonyls
  type: soft
builds-toward:
- nucleophilic-acyl-substitution
- amines-structure-and-properties
tags:
- carboxylic acids
- esters
- amides
- acyl chlorides
- anhydrides
- acidity
- reactivity order
stage: formal-systems
status: validated
---
# Carboxylic Acids and Their Derivatives

## Core Idea
Carboxylic acids (RCOOH) and their derivatives — acyl chlorides, anhydrides, esters, and amides — all contain the acyl group (RCO–) but differ in the substituent on the carbonyl. Carboxylic acids are significantly more acidic than alcohols (pKa ≈ 5 vs ≈ 16) due to resonance delocalization of the negative charge across both oxygens in the carboxylate anion. The reactivity order toward nucleophilic acyl substitution is: acyl chlorides > anhydrides > carboxylic acids ≈ esters >> amides, reflecting how easily the leaving group departs. Understanding this hierarchy predicts interconversion routes among derivatives.

## How It's Best Learned
Memorize the reactivity ladder and the structural reason for each rung. Practice drawing interconversions: can you convert an ester to an amide directly? (Yes, under forcing conditions.) Can you convert an amide to an ester directly? (No — must go through acid chloride.) Use retrosynthetic logic.

## Common Misconceptions
- Esters and acids differ by whether a free OH is directly on the carbonyl — this single structural difference dramatically changes pKa and reactivity.
- Amides are the least reactive acyl derivative because nitrogen donates its lone pair into the C=O, reducing carbonyl electrophilicity.
- Carboxylate anion acidity comes from resonance, not from inductive effects alone; both oxygens share the negative charge equally.

## Questions

```yaml
- question: "Which of the following correctly ranks the reactivity of acyl derivatives toward nucleophilic substitution, from most to least reactive?"
  type: multiple-choice
  options:
    - "Amides > esters > carboxylic acids > acyl chlorides"
    - "Acyl chlorides > anhydrides > esters > amides"
    - "Carboxylic acids > esters > anhydrides > acyl chlorides"
    - "Esters > amides > acyl chlorides > anhydrides"
  answer: 1
  explanation: "Reactivity tracks how easily the leaving group departs from the tetrahedral intermediate. Chloride (from acyl chloride) is the best leaving group — it is the conjugate base of a strong acid. Carboxylate (from an anhydride) is next. Alkoxide (from an ester) and hydroxide (from a carboxylic acid) are comparable. Amide nitrogen donates its lone pair into the carbonyl, reducing electrophilicity and making nitrogen a very poor leaving group — so amides are the least reactive."

- question: "Carboxylic acids are more acidic than alcohols primarily because the oxygen in carboxylic acids is more electronegative than the oxygen in alcohols."
  type: true-false
  answer: false
  explanation: "Both functional groups contain oxygen atoms with similar electronegativity — the key difference is resonance. When a carboxylic acid loses a proton, the resulting carboxylate anion delocalizes the negative charge equally across both oxygens through resonance. This charge delocalization strongly stabilizes the conjugate base, making the acid much stronger (pKa ≈ 5) compared to alcohols, where the alkoxide anion has no resonance stabilization and bears the full charge on a single oxygen (pKa ≈ 16)."

- question: "Explain why it is possible to convert an ester directly to an amide, but converting an amide directly to an ester under mild conditions is not practical."
  type: short-answer
  answer: "An ester is more reactive than an amide toward nucleophilic substitution. Treating an ester with an amine (a nucleophile) displaces the alkoxide leaving group to form the amide — this works because alkoxide is a better leaving group than amide nitrogen. Reversing the reaction requires making the amide nitrogen leave, but nitrogen is a very poor leaving group because it donates its lone pair into the carbonyl, and amide hydrolysis requires forcing conditions (strong acid/base, heat). Mild conditions do not provide enough energy to overcome amide stability."
  explanation: "The reactivity hierarchy dictates the direction of these interconversions. You can always move 'down' the reactivity ladder (from more to less reactive) under mild conditions, because a better leaving group is being replaced by a worse one. Moving 'up' the ladder requires activating the less reactive compound first — typically by converting the amide to an acyl chloride using a reagent like thionyl chloride, then reacting the acyl chloride with the alcohol."
```

## Explainer

In your study of carbonyl chemistry, you encountered aldehydes and ketones — carbonyls where the electrophilic carbon is flanked by carbon or hydrogen substituents. Carboxylic acids and their derivatives are a large family of carbonyls where one substituent on the carbonyl carbon is a heteroatom (O, N, or halogen) connected to another group. This single structural feature — the acyl group RCO– attached to a leaving group — makes them reactive in a fundamentally different way from aldehydes and ketones.

The family has a clear hierarchy of members. Starting from most reactive: acyl chlorides (RCOC–Cl), anhydrides (RCOOCOR'), carboxylic acids (RCOOH) and esters (RCOOR'), and finally amides (RCONH₂). All five share the same carbonyl carbon, yet their reactivities span orders of magnitude. The reason is leaving group ability: the ease with which the substituent on the carbonyl can depart as an anion after a nucleophile attacks. Chloride (Cl⁻) is the conjugate base of HCl, a strong acid — it is a superb leaving group. Carboxylate (RCOO⁻) is next. Alkoxide (RO⁻) and hydroxide (HO⁻) are weaker. Amide nitrogen (–NH₂) donates its lone pair into the C=O pi system through resonance, reducing the carbonyl's electrophilicity and making it a very reluctant leaving group. This is why amide bonds are so stable — they are the peptide bonds holding proteins together.

The acidity story is equally important. You know from acid-base chemistry that acid strength depends on the stability of the conjugate base. When acetic acid (CH₃COOH, pKa ≈ 5) loses a proton, the acetate anion distributes the negative charge equally across both oxygens through resonance — you can draw two equivalent resonance structures, and the true structure is a hybrid with equal C–O bond lengths. This delocalization stabilizes the anion enormously. Compare this to ethanol (pKa ≈ 16), where the ethoxide anion carries the full negative charge on a single oxygen with no resonance relief. The factor-of-10¹¹ difference in Ka reflects this resonance stabilization.

Understanding the reactivity ladder has immediate synthetic consequences. You can always convert a more reactive acyl derivative to a less reactive one: treat an acyl chloride with an alcohol to get an ester, or with an amine to get an amide. These reactions work under mild conditions because a better leaving group (Cl⁻) is displaced by a worse one (RO⁻ or RNH⁻). Moving in the other direction — from amide to ester, for example — requires first activating the compound to a more reactive form (usually the acyl chloride), which demands more forcing conditions. Thinking in terms of the reactivity hierarchy gives you a map for planning multistep syntheses involving acyl groups.
