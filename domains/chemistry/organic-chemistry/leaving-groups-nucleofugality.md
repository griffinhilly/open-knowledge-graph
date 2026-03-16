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

## Explainer

In every substitution and elimination reaction you will study, a bond must break and a group must depart with the bonding electrons. That departing species is the **leaving group**, and its ability to leave — its **nucleofugality** — is one of the most important factors controlling whether a reaction occurs at all. The core principle is simple: a good leaving group is a **stable species after it departs**. If the leaving group can exist comfortably as an anion or neutral molecule once it carries away the bonding electrons, it leaves easily. If it would form a high-energy, unstable species, it resists departure.

The most reliable predictor of leaving group ability is **basicity**, which you already understand from acid-base chemistry. Good leaving groups are the conjugate bases of strong acids — that is, they are weak bases. Iodide (I⁻), the conjugate base of the strong acid HI (pKa ≈ –10), is an excellent leaving group because it is extremely stable as a free anion. Bromide and chloride are also good, in the order I⁻ > Br⁻ > Cl⁻, following the trend in acid strength of their conjugate acids. Fluoride is a poor leaving group despite being a halide because it is a relatively strong base (HF is a weak acid). At the other extreme, hydroxide (OH⁻) and alkoxide (RO⁻) are terrible leaving groups because they are the conjugate bases of weak acids (water and alcohols).

This basicity relationship has a direct practical consequence: **alcohols cannot undergo SN1, SN2, E1, or E2 reactions directly** because OH⁻ is too poor a leaving group. To make an alcohol reactive, you must first convert the –OH into a better leaving group. The simplest approach is protonation: treating the alcohol with a strong acid converts –OH into –OH₂⁺, and water (H₂O) is an excellent leaving group because it is the conjugate base of H₃O⁺. Alternatively, you can convert the alcohol to a **tosylate** (–OTs) or **mesylate** (–OMs) by reacting with the corresponding sulfonyl chloride. These sulfonate esters are superb leaving groups because the departing anion is stabilized by resonance delocalization of the negative charge across multiple oxygen atoms.

When evaluating a reaction, always check the leaving group first. If the substrate has a good leaving group (halide, tosylate, mesylate, water after protonation), the reaction can proceed. If it has a poor leaving group (OH⁻, OR⁻, NH₂⁻), the reaction will not occur without prior activation. This single check eliminates many impossible reaction pathways and is the first step in the systematic analysis you will use to predict whether a substrate undergoes SN1, SN2, E1, or E2.
