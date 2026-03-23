---
id: leaving-groups-nucleofugality
title: Leaving Groups and Nucleofugality
domain: chemistry
course: organic-chemistry
prerequisites:
- id: nucleophile-electrophile-definitions
  type: hard
- id: acid-base-strength-ka-kb-calculations
  type: soft
builds-toward:
- sn1-reaction
- sn2-reaction
- e1-elimination
- e2-elimination
tags:
- leaving-group
- basicity
- nucleofugality
- reactivity
stage: formal-systems
status: draft
---

# Leaving Groups and Nucleofugality

## Core Idea
Good leaving groups are weak bases whose conjugate bases are stable anions or neutral molecules. Leaving group ability is inversely related to basicity: strong conjugate bases (OH⁻, alkoxide) are poor leaving groups, while weak bases (halide, tosylate, mesylate, water) are excellent leaving groups. The stability of the departing species determines the ease of bond cleavage.

## How It's Best Learned
Compare basicity (pKa values) of conjugate bases to rank leaving group ability. Understand why halides and sulfonate esters are superior leaving groups compared to hydroxyl or alkoxy groups.

## Common Misconceptions
- Confusing leaving group ability with nucleophilicity; they are separate properties.
- Underestimating how poor hydroxyl is as a leaving group; it typically requires protonation to water to depart.

## Questions

```yaml
- question: "A student attempts an SN2 reaction by treating an alcohol (R-OH) directly with sodium cyanide (NaCN). No substitution product forms. What is the most likely reason?"
  type: multiple-choice
  options:
    - "Cyanide is too weak a nucleophile to attack a carbon bearing an OH group."
    - "OH⁻ is too poor a leaving group to depart; its high basicity makes it resist leaving, and alcohols cannot undergo SN2 without prior activation."
    - "The reaction actually proceeds by SN1 instead of SN2, so no substitution product is detected by the student's method."
    - "NaCN makes the solution basic, which deprotonates the alcohol and prevents water from acting as a leaving group."
  answer: 1
  explanation: "The first check in any substitution analysis is the leaving group. OH⁻ is the conjugate base of water (pKₐ ≈ 15.7), making it a strong base and a terrible leaving group. It will not depart regardless of how good the nucleophile is. To activate an alcohol for SN2, the –OH must first be converted to a better leaving group — either by protonation to give –OH₂⁺ (water, an excellent leaving group) or by conversion to a tosylate or mesylate."

- question: "Rank the following groups from BEST to WORST leaving group ability: F⁻, I⁻, Br⁻, OH⁻"
  type: multiple-choice
  options:
    - "F⁻ > Br⁻ > I⁻ > OH⁻"
    - "OH⁻ > F⁻ > Br⁻ > I⁻"
    - "I⁻ > Br⁻ > F⁻ > OH⁻"
    - "Br⁻ > I⁻ > F⁻ > OH⁻"
  answer: 2
  explanation: "Leaving group ability is inversely related to basicity. The order follows the pKₐ of the conjugate acids: HI (pKₐ ≈ −10) > HBr (pKₐ ≈ −9) > HF (pKₐ ≈ 3.2) > H₂O (pKₐ ≈ 15.7). So I⁻ > Br⁻ >> F⁻ >> OH⁻. Fluoride is surprisingly poor for a halide because HF is a weak acid — F⁻ is a relatively strong base. The common mistake is ranking F⁻ as the best halide leaving group because fluorine is the most electronegative."

- question: "Converting an alcohol to a tosylate ester (–OTs) improves its reactivity in substitution reactions by replacing a poor leaving group with a better one."
  type: true-false
  answer: true
  explanation: "This is exactly right. The tosylate anion (TsO⁻) is the conjugate base of toluenesulfonic acid, a strong acid (pKₐ ≈ −1). The departing anion is stabilized by resonance delocalization of the negative charge across multiple sulfonate oxygen atoms, making TsO⁻ a weak base and excellent leaving group. Crucially, this conversion does not alter the stereochemistry at the carbon bearing the leaving group, preserving the substrate's configuration for subsequent stereospecific reactions."

- question: "A better nucleophile is always also a better leaving group, because both properties reflect the stability of the species."
  type: true-false
  answer: false
  explanation: "Nucleophilicity and leaving group ability are distinct and often inversely correlated in polar aprotic solvents. Nucleophilicity measures how readily a species attacks an electrophile (a kinetic, forward-reaction property). Leaving group ability measures how readily a species departs with bonding electrons (a thermodynamic stability property). Hydroxide (OH⁻) is a good nucleophile but a terrible leaving group. Iodide (I⁻) is both a good nucleophile and a good leaving group. Tosylate is an excellent leaving group but a weak nucleophile. The confusion is one of the most common in organic chemistry."

- question: "Why does protonating an alcohol (R-OH → R-OH₂⁺) dramatically increase its reactivity in substitution reactions, even though the nucleophile still attacks the same carbon?"
  type: short-answer
  answer: "Protonation converts OH⁻ (a strong base, terrible leaving group) into H₂O (a weak base, excellent leaving group). The key factor is the stability of the departing species: water is the conjugate base of H₃O⁺ (pKₐ ≈ −1.7), making it an extremely weak base that departs easily. Before protonation, the carbon-oxygen bond would have to break to release OH⁻, an unstable high-energy anion. After protonation, the same bond breaks to release neutral water, a stable molecule. The nucleophile's job hasn't changed — the leaving group has been transformed from unworkable to excellent."
  explanation: "This question probes whether students understand that leaving group ability determines whether bond cleavage is thermodynamically feasible, not just kinetically fast. The proton does not go to the leaving group's carbon or change which bond the nucleophile attacks — it changes the identity of the leaving species from OH⁻ to H₂O. Since leaving group ability tracks inverse basicity, converting a strong base (OH⁻) to a weak base (H₂O) makes all the difference between zero reactivity and rapid substitution."
```

## Explainer

In every substitution and elimination reaction you will study, a bond must break and a group must depart with the bonding electrons. That departing species is the **leaving group**, and its ability to leave — its **nucleofugality** — is one of the most important factors controlling whether a reaction occurs at all. The core principle is simple: a good leaving group is a **stable species after it departs**. If the leaving group can exist comfortably as an anion or neutral molecule once it carries away the bonding electrons, it leaves easily. If it would form a high-energy, unstable species, it resists departure.

The most reliable predictor of leaving group ability is **basicity**, which you already understand from acid-base chemistry. Good leaving groups are the conjugate bases of strong acids — that is, they are weak bases. Iodide (I⁻), the conjugate base of the strong acid HI (pKa ≈ –10), is an excellent leaving group because it is extremely stable as a free anion. Bromide and chloride are also good, in the order I⁻ > Br⁻ > Cl⁻, following the trend in acid strength of their conjugate acids. Fluoride is a poor leaving group despite being a halide because it is a relatively strong base (HF is a weak acid). At the other extreme, hydroxide (OH⁻) and alkoxide (RO⁻) are terrible leaving groups because they are the conjugate bases of weak acids (water and alcohols).

This basicity relationship has a direct practical consequence: **alcohols cannot undergo SN1, SN2, E1, or E2 reactions directly** because OH⁻ is too poor a leaving group. To make an alcohol reactive, you must first convert the –OH into a better leaving group. The simplest approach is protonation: treating the alcohol with a strong acid converts –OH into –OH₂⁺, and water (H₂O) is an excellent leaving group because it is the conjugate base of H₃O⁺. Alternatively, you can convert the alcohol to a **tosylate** (–OTs) or **mesylate** (–OMs) by reacting with the corresponding sulfonyl chloride. These sulfonate esters are superb leaving groups because the departing anion is stabilized by resonance delocalization of the negative charge across multiple oxygen atoms.

When evaluating a reaction, always check the leaving group first. If the substrate has a good leaving group (halide, tosylate, mesylate, water after protonation), the reaction can proceed. If it has a poor leaving group (OH⁻, OR⁻, NH₂⁻), the reaction will not occur without prior activation. This single check eliminates many impossible reaction pathways and is the first step in the systematic analysis you will use to predict whether a substrate undergoes SN1, SN2, E1, or E2.
