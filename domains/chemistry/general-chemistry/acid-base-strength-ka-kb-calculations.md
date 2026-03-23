---
id: acid-base-strength-ka-kb-calculations
title: 'Acid and Base Strength: Ka, Kb, and Ionization'
domain: chemistry
course: general-chemistry
prerequisites:
- id: weak-acid-ionization
  type: soft
- id: weak-base-ionization
  type: soft
- id: pH-and-acid-base-calculations
  type: hard
- id: logarithm-properties
  type: hard
- id: logarithms-intro
  type: hard
- id: exponential-functions-and-graphs
  type: soft
builds-toward:
- buffer-chemistry-le-chatelier-application
tags:
- acid-strength
- base-strength
- ka
- kb
- ionization
stage: formal-systems
status: validated
---

# Acid and Base Strength: Ka, Kb, and Ionization

## Core Idea
Acid strength is quantified by Ka (acid dissociation constant); base strength by Kb (base dissociation constant). Larger Ka or Kb indicates stronger acid or base. Strong acids and bases ionize completely; weak acids and bases establish equilibrium. Conjugate acid-base pairs are related by Ka × Kb = Kw = 1.0 × 10⁻¹⁴ at 25°C.

## Questions

```yaml
- question: "The Ka of acetic acid (CH₃COOH) is 1.8 × 10⁻⁵. What is the Kb of its conjugate base, acetate ion (CH₃COO⁻)?"
  type: multiple-choice
  options: ["1.8 × 10⁻⁵", "5.6 × 10⁻¹⁰", "1.8 × 10⁻¹⁴", "1.0 × 10⁻⁷"]
  answer: 1
  explanation: "For a conjugate acid-base pair, Ka × Kb = Kw = 1.0 × 10⁻¹⁴. So Kb = Kw / Ka = (1.0 × 10⁻¹⁴) / (1.8 × 10⁻⁵) ≈ 5.6 × 10⁻¹⁰. This relationship shows that the stronger the acid, the weaker its conjugate base — acetic acid is a weak acid, so acetate is a moderately weak base."

- question: "A solution of a weak acid with a larger Ka value will always have a lower pH than an equal-concentration solution of a weak acid with a smaller Ka."
  type: true-false
  answer: true
  explanation: "For two weak acids at the same initial concentration, a larger Ka means a greater degree of ionization — more H⁺ ions in solution — which produces a lower pH. For example, a 0.1 M solution of an acid with Ka = 10⁻³ will be more acidic than a 0.1 M solution of an acid with Ka = 10⁻⁵. (This would be false if concentrations were different, which is a common source of confusion.)"

- question: "Why does a weak acid with Ka = 10⁻⁵ not fully ionize, even though the ionization reaction is spontaneous?"
  type: short-answer
  answer: "The ionization establishes an equilibrium. As H⁺ and A⁻ accumulate, the reverse reaction (recombination) becomes more favorable, and the system reaches a balance where only a small fraction of HA has dissociated. Ka quantifies where that balance lies."
  explanation: "Ka is an equilibrium constant. A value much less than 1 means the equilibrium strongly favors the undissociated form HA. The reaction does proceed forward, but it also proceeds in reverse — and for weak acids, the reverse reaction is fast enough to keep most of the acid intact at equilibrium. This is fundamentally different from strong acids, where the reverse reaction is negligible."
```

## Explainer

Acid strength is not a binary property — it exists on a continuous spectrum captured by the acid dissociation constant Ka. When a weak acid HA dissolves in water, it partially ionizes: HA ⇌ H⁺ + A⁻. The Ka is the equilibrium constant for this reaction: Ka = [H⁺][A⁻] / [HA]. A large Ka means the equilibrium lies far to the right — most of the acid has donated its proton and the acid is strong. A small Ka means the equilibrium lies left — most of the acid remains intact, and only a small fraction has ionized. Strong acids like HCl and HNO₃ have Ka values so large that ionization is essentially complete; weak acids like acetic acid (Ka ≈ 1.8 × 10⁻⁵) ionize only partially.

Working with Ka numerically usually means using logarithms, since Ka values span many orders of magnitude. The pKa = −log(Ka) compresses this range into a more convenient scale: a lower pKa corresponds to a stronger acid (more ionization). For example, acetic acid has pKa ≈ 4.74, while hydrofluoric acid has pKa ≈ 3.17, confirming HF is the stronger acid of the two. When calculating the pH of a weak acid solution, you set up an ICE table (Initial, Change, Equilibrium) and solve the equilibrium expression — often using the approximation that x ≪ initial concentration when Ka is small.

The conjugate base relationship is a critical organizing principle. Every acid HA has a conjugate base A⁻ formed when it donates its proton. The Ka of the acid and the Kb of its conjugate base are linked by Ka × Kb = Kw = 1.0 × 10⁻¹⁴ at 25°C. This means a strong acid (large Ka) always has a weak conjugate base (small Kb), and vice versa. Acetic acid's conjugate base, acetate, has Kb ≈ 5.6 × 10⁻¹⁰ — a weak base, but not negligible. This is why sodium acetate solutions are slightly basic: acetate slowly picks up protons from water.

A common misconception is that Ka directly tells you the pH of a solution without considering concentration. Ka measures ionization tendency, not the resulting H⁺ concentration in a specific solution. A 0.001 M weak acid will have a higher pH than a 1.0 M solution of the same acid even though Ka is identical. The pH depends on both Ka and the initial concentration, which is why the ICE table approach accounts for both.
