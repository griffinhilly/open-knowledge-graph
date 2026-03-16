---
id: weak-base-ionization
title: Weak Base Ionization
domain: chemistry
course: general-chemistry
prerequisites:
- id: weak-acid-ionization
  type: hard
- id: logarithms-intro
  type: soft
builds-toward:
- buffer-solutions
tags:
- Kb
- base-ionization-constant
- Kw
- Ka-Kb-relationship
- ICE-table
- weak-base
- hydroxide-ion
stage: abstract-reasoning
status: draft
---
# Weak Base Ionization

## Core Idea
A weak base partially ionizes in water by accepting a proton from H₂O, producing OH⁻ and the conjugate acid. The base ionization constant Kb = [BH⁺][OH⁻]/[B] measures the extent of ionization. For any conjugate acid-base pair, Ka × Kb = Kw = 1.0 × 10⁻¹⁴ at 25°C, linking the strength of a weak acid to the strength of its conjugate base. ICE tables work identically to weak acid problems: define x as the amount of base that reacts, substitute into the Kb expression, and solve for [OH⁻], then convert to pH via pOH = −log[OH⁻] and pH = 14 − pOH.

## How It's Best Learned
Solve weak base ICE table problems in parallel with weak acid problems to see the structural symmetry. Practice using Ka × Kb = Kw to find Kb from a given Ka (or vice versa) — this is essential for predicting whether a salt solution is acidic, basic, or neutral.

## Common Misconceptions
- The conjugate base of a strong acid (e.g., Cl⁻ from HCl) has a Kb so small it is effectively zero — it does not hydrolyze in water. Only conjugate bases of weak acids produce measurably basic solutions.
- pH = 14 − pOH is valid at 25°C. At other temperatures, Kw changes, so the relationship between pH and pOH changes as well.

## Explainer

If you are comfortable solving weak acid equilibrium problems with Ka and ICE tables, weak base ionization is structurally identical — you are just looking at the mirror image of the same process. Instead of an acid donating a proton to water (HA + H₂O → A⁻ + H₃O⁺), a **weak base** accepts a proton from water: B + H₂O → BH⁺ + OH⁻. The base steals a hydrogen from water, producing hydroxide ions that make the solution basic, and a **conjugate acid** (BH⁺) that is the base's protonated form. Ammonia is the classic example: NH₃ + H₂O ⇌ NH₄⁺ + OH⁻.

The equilibrium constant for this process is **Kb**, defined as [BH⁺][OH⁻]/[B]. A larger Kb means the base ionizes more extensively and produces a more basic solution. The ICE table setup is mechanically identical to what you did for weak acids: start with the initial concentration of the base, define *x* as the amount that reacts, and substitute into the Kb expression. The key difference is that you solve for [OH⁻] rather than [H₃O⁺]. To find pH, you first calculate pOH = −log[OH⁻], then use pH = 14 − pOH (at 25°C).

The most powerful relationship in this topic is **Ka × Kb = Kw**. Every conjugate acid-base pair is linked: a strong acid has a very weak conjugate base (tiny Kb), and a weak acid has a conjugate base with a correspondingly larger Kb. This relationship is not just bookkeeping — it is the tool you use to predict whether a salt solution will be acidic, basic, or neutral. When sodium acetate dissolves, the acetate ion is the conjugate base of acetic acid. You can calculate its Kb from Ka of acetic acid using Kb = Kw/Ka, then solve the ICE table to find the pH. This same logic extends to every salt formed from a weak acid or weak base.

Practice building the habit of asking: "What is this ion the conjugate of?" For any weak base problem, identify the conjugate acid, note the Ka × Kb = Kw connection, and then the ICE table machinery you already know does the rest. The symmetry between weak acid and weak base calculations is complete — the only difference is which side of water's autoionization you are working from.
