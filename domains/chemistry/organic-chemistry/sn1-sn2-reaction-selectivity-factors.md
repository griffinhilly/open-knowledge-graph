---
id: sn1-sn2-reaction-selectivity-factors
title: 'SN1 vs SN2 Selectivity: Factors and Competition'
domain: chemistry
course: organic-chemistry
prerequisites:
- id: sn1-reaction
  type: hard
- id: sn2-reaction
  type: hard
- id: nucleophilicity-and-leaving-groups
  type: hard
- id: polar-protic-aprotic-solvents
  type: hard
builds-toward:
- zaitsevs-rule-hofmann-elimination
tags:
- mechanism
- selectivity
- substrate-structure
- nucleophile
- solvent
stage: formal-systems
status: validated
---

# SN1 vs SN2 Selectivity: Factors and Competition

## Core Idea
SN1 occurs on tertiary substrates with weak nucleophiles in polar protic solvents (carbocation forms first). SN2 occurs on primary/secondary substrates with strong nucleophiles in polar aprotic solvents (single transition state, inversion). The selectivity depends on substrate steric hindrance (1° → SN2; 3° → SN1), nucleophile strength/basicity, and solvent polarity. Competing E1/E2 eliminations also occur.

## How It's Best Learned
Sketch transition states for SN1 (carbocation intermediate) and SN2 (back-side attack). Predict products for different substrates/nucleophiles. Consider which factor dominates in each scenario (steric vs electronic).

## Common Misconceptions
SN1 doesn't always mean racemization—some substrate/solvent pairs show modest stereoselectivity. SN2 with a good nucleophile still competes with E2. Secondary substrates can go either SN1 or SN2 depending on solvent and nucleophile strength.

## Questions

```yaml
- question: "Sodium cyanide (CN⁻, a strong nucleophile) is added to (CH₃)₃CBr in DMSO at room temperature. A student predicts SN2 because CN⁻ is a strong nucleophile. What will actually be the major pathway and why?"
  type: multiple-choice
  options:
    - "SN2 — strong nucleophiles always displace leaving groups regardless of substrate structure"
    - "SN1 — the tertiary substrate forms a stabilized carbocation, and steric crowding physically blocks back-side attack even though CN⁻ is strong"
    - "No reaction — polar aprotic solvents destabilize carbocations and prevent SN1 on tertiary substrates"
    - "E2 elimination — CN⁻ preferentially acts as a base on all tertiary substrates"
  answer: 1
  explanation: "Substrate structure is the most important factor. Tertiary substrates have three alkyl groups shielding the electrophilic carbon, physically preventing the back-side attack that SN2 requires — regardless of how strong the nucleophile is. The tertiary carbocation from (CH₃)₃C⁺ is also well-stabilized by hyperconjugation. The student's error is thinking nucleophile strength alone determines mechanism; it cannot overcome the steric barrier. The combination of tertiary substrate + DMSO (which stabilizes ions) means SN1 dominates."

- question: "2-Bromopropane (a secondary substrate) is treated with methanol (a weak nucleophile) in water. Which prediction is best, and what factors lead to it?"
  type: multiple-choice
  options:
    - "SN2 — secondary substrates have moderate steric hindrance and will always go SN2 with any nucleophile"
    - "SN1 — water and methanol are polar protic solvents that stabilize the secondary carbocation intermediate, and the weak nucleophile cannot drive SN2"
    - "No reaction — secondary substrates require a strong nucleophile to react by either mechanism"
    - "E2 elimination — methanol is basic enough to deprotonate and favor elimination on secondary substrates"
  answer: 1
  explanation: "Secondary substrates are the borderline case — you must look beyond substrate structure. Here, two factors point to SN1: the solvent (water/methanol) is polar protic, which stabilizes the secondary carbocation through solvation and weakens nucleophilicity through hydrogen bonding; and methanol is a weak nucleophile that cannot drive SN2 by actively attacking the substrate. Weak nucleophiles favor SN1 because they passively trap a carbocation once it forms rather than forcing a direct displacement."

- question: "A secondary substrate treated with a strong nucleophile (e.g., CN⁻) in a polar aprotic solvent (e.g., DMSO) will predominantly undergo SN1, because secondary carbocations are moderately stable."
  type: true-false
  answer: false
  explanation: "This is a common error. For secondary substrates, the solvent and nucleophile strength matter enormously. A polar aprotic solvent leaves the nucleophile bare and highly reactive (no hydrogen bonding to solvate and weaken it), and a strong nucleophile can drive direct back-side attack. Together, these conditions favor SN2. SN1 on secondary substrates requires polar protic solvents to stabilize the carbocation and a weak nucleophile that cannot force SN2. The substrate alone does not determine the outcome — the combination of all four factors must be evaluated."

- question: "The selectivity between SN1 and SN2 for a given substrate can be shifted by changing the solvent, even without changing the nucleophile or substrate."
  type: true-false
  answer: true
  explanation: "Solvent is a genuine mechanistic lever. Switching from a polar protic solvent (water, methanol) to a polar aprotic solvent (DMSO, DMF, acetone) can shift a secondary substrate from SN1 toward SN2. Polar protic solvents stabilize carbocation intermediates through solvation, favoring SN1; they also hydrogen-bond to nucleophiles, weakening them. Polar aprotic solvents do neither — they leave nucleophiles reactive. So the same substrate and nucleophile can show dramatically different selectivity depending solely on solvent choice."

- question: "Why does tertiary substrate structure favor SN1 over SN2? Provide both a steric and an electronic argument."
  type: short-answer
  answer: "Sterically: three alkyl groups surround the electrophilic carbon in a tertiary substrate, creating a steric barrier that prevents a nucleophile from approaching the back face for the SN2 transition state. Even strong nucleophiles cannot physically reach the carbon for back-side attack. Electronically: when the tertiary substrate ionizes to form a carbocation, the three alkyl groups stabilize the positive charge through hyperconjugation (overlap of adjacent C-H sigma bonds with the empty p orbital) and inductive electron donation. This lowers the activation energy for carbocation formation, making SN1 energetically favorable."
  explanation: "Both effects reinforce each other: the steric crowding blocks SN2, and the electronic stabilization promotes SN1. This is why tertiary substrates almost always go SN1 regardless of nucleophile strength or solvent — the two factors combine to make the SN1 pathway strongly preferred."
```

## Explainer

You have learned the SN1 and SN2 mechanisms individually — now the real challenge is predicting which one wins when both are possible. The answer comes from evaluating four factors: **substrate structure**, **nucleophile strength**, **solvent**, and **leaving group**. No single factor decides the outcome; it is the combination that tips the balance.

**Substrate structure** is the most important factor. Primary substrates strongly favor SN2 because they are sterically unhindered — the nucleophile can easily access the electrophilic carbon from the back side. Tertiary substrates strongly favor SN1 because the resulting carbocation is stabilized by three alkyl groups through hyperconjugation and induction, and because steric crowding blocks the back-side attack required for SN2. Secondary substrates are the borderline case — either mechanism is possible, and you must look at the other factors to decide. Think of it as a tug-of-war: steric crowding pulls toward SN1 (dissociative), while openness pulls toward SN2 (associative).

**Nucleophile strength** breaks ties for secondary substrates and reinforces trends elsewhere. Strong nucleophiles (like hydroxide, cyanide, or iodide) push reactions toward SN2 because they actively attack the substrate — rate depends on nucleophile concentration. Weak nucleophiles (like water or alcohols) favor SN1 because they cannot force the displacement but can readily trap a carbocation once it forms. **Solvent** works in concert: polar aprotic solvents (DMSO, acetone, DMF) favor SN2 by leaving the nucleophile "naked" and reactive, while polar protic solvents (water, alcohols) favor SN1 by stabilizing the carbocation intermediate through solvation and simultaneously weakening nucleophilicity through hydrogen bonding.

The practical decision tree works like this: identify the substrate class first. If it is methyl or primary, predict SN2 (unless the nucleophile is very weak). If it is tertiary, predict SN1. If it is secondary, check the nucleophile — strong nucleophile in a polar aprotic solvent means SN2; weak nucleophile in a polar protic solvent means SN1. But always remember the elephant in the room: **elimination competes with substitution**. Strong bases at elevated temperatures favor E2 over SN2, and high temperatures push SN1 toward E1. A complete prediction considers all four pathways — SN1, SN2, E1, E2 — not just the two substitution mechanisms.
