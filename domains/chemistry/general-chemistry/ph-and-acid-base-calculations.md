---
id: ph-and-acid-base-calculations
title: pH and Acid-Base Calculations
domain: chemistry
course: general-chemistry
prerequisites:
- id: acid-base-chemistry
  type: hard
- id: chemical-equilibrium
  type: hard
- id: logarithms-intro
  type: soft
- id: logarithm-properties
  type: soft
- id: buffer-chemistry-le-chatelier-application
  type: soft
tags:
- pH
- pOH
- Ka
- Kb
- buffer
- Henderson-Hasselbalch
- titration
- Kw
stage: formal-systems
status: validated
---
# pH and Acid-Base Calculations

## Core Idea
pH = −log[H⁺] and pOH = −log[OH⁻]; in aqueous solution at 25°C, pH + pOH = 14 because Kw = [H⁺][OH⁻] = 1.0 × 10⁻¹⁴. Ka and Kb quantify weak acid and base strength; for conjugate pairs, Ka × Kb = Kw. Buffer solutions (weak acid + conjugate base) resist pH change upon addition of small amounts of acid or base; the Henderson-Hasselbalch equation pH = pKa + log([A⁻]/[HA]) describes buffer pH and is most accurate when both components are present in appreciable amounts.

## How It's Best Learned
Build problem-solving fluency across four solution types: strong acid/base (direct from concentration), weak acid/base (ICE table with Ka/Kb), buffers (Henderson-Hasselbalch), and salt solutions (assess hydrolysis of conjugate ion). Relate pH values to real contexts: blood (7.4), stomach acid (1-2), ocean acidification.

## Common Misconceptions
- pH 7 is neutral only at 25°C — Kw increases with temperature, so the neutral pH is slightly below 7 at physiological temperature.
- Buffers do not prevent pH changes entirely — they resist change but are overwhelmed by large additions of acid or base that exhaust one buffer component.

## Questions

```yaml
- question: "You dissolve sodium acetate (NaC₂H₃O₂) in water. Without calculating, which best describes the resulting solution?"
  type: multiple-choice
  options:
    - "Acidic, because sodium ions are weakly acidic"
    - "Basic, because acetate ions accept a proton from water to form OH⁻"
    - "Neutral, because Na⁺ and C₂H₃O₂⁻ charges cancel"
    - "Acidic, because acetic acid is a weak acid"
  answer: 1
  explanation: "Sodium ion is a spectator (conjugate of the strong base NaOH). Acetate is the conjugate base of the weak acid acetic acid; it undergoes hydrolysis: C₂H₃O₂⁻ + H₂O → HC₂H₃O₂ + OH⁻, making the solution basic. This is the salt hydrolysis concept — a salt of a weak acid and strong base produces a basic solution."

- question: "Adding a small amount of strong acid to a buffer solution does not change its pH at all."
  type: true-false
  answer: false
  explanation: "Buffers resist pH change but do not prevent it entirely. The Henderson-Hasselbalch equation shows that adding acid consumes conjugate base ([A⁻] decreases, [HA] increases), shifting the ratio and slightly lowering pH. The buffer absorbs the shock — it just cannot prevent every change. A buffer is overwhelmed entirely when one component is exhausted."

- question: "Acetic acid has Ka = 1.8 × 10⁻⁵. What is the Kb for acetate ion, and what relationship makes this calculation possible?"
  type: short-answer
  answer: "Kb = Kw / Ka = (1.0 × 10⁻¹⁴) / (1.8 × 10⁻⁵) ≈ 5.6 × 10⁻¹⁰. The relationship Ka × Kb = Kw holds for any conjugate acid-base pair."
  explanation: "For conjugate acid-base pairs, Ka × Kb = Kw because the two equilibria — HA ⇌ H⁺ + A⁻ and A⁻ + H₂O ⇌ HA + OH⁻ — sum to the water autoionization equilibrium H₂O ⇌ H⁺ + OH⁻ with constant Kw. This relationship is a direct consequence of Hess's law applied to equilibria."
```

## Explainer

The pH scale compresses an enormous range of hydrogen ion concentrations into a manageable 0–14 range using logarithms: pH = −log[H⁺]. Because it is a negative log, low [H⁺] gives high pH (basic) and high [H⁺] gives low pH (acidic). At 25°C, pure water has [H⁺] = [OH⁻] = 1.0 × 10⁻⁷ M, giving pH = pOH = 7 and pH + pOH = 14. This 14 comes from pKw = −log(Kw) = −log(1.0 × 10⁻¹⁴). If temperature changes, Kw changes, and the neutral point shifts — blood at body temperature (~37°C) has a neutral pH slightly below 7, though the physiological pH 7.4 is still considered "normal" and basic relative to that neutral point.

For strong acids and bases, calculating pH is direct: a 0.010 M HCl solution has [H⁺] = 0.010 M, so pH = −log(0.010) = 2. For weak acids and bases, the equilibrium is partial. An ICE table (Initial, Change, Equilibrium) lets you set up the Ka expression and solve for [H⁺]. For a weak acid HA with initial concentration C and acid dissociation constant Ka, the equilibrium [H⁺] ≈ √(Ka × C) when Ka << C. The smaller Ka is, the weaker the acid and the less it dissociates — acetic acid (Ka = 1.8 × 10⁻⁵) is far weaker than hydrochloric acid (essentially complete dissociation).

Conjugate pairs are linked by Ka × Kb = Kw. This means if you know the Ka of a weak acid, you can compute the Kb of its conjugate base. A strong acid (large Ka) has a conjugate base with a tiny Kb — the conjugate base of a strong acid barely accepts protons at all (e.g., Cl⁻ in HCl). Conversely, a weak acid's conjugate base has a meaningful Kb, which is why dissolving sodium acetate in water produces a basic solution: the acetate ion hydrolyzes.

Buffers exploit this conjugate-pair relationship to stabilize pH. A buffer contains both the weak acid HA and its conjugate base A⁻, usually in comparable amounts. When a small amount of strong acid is added, it reacts with A⁻ to form more HA — the system absorbs the proton without a large pH shift. When base is added, it converts HA to A⁻. The Henderson-Hasselbalch equation, pH = pKa + log([A⁻]/[HA]), captures this: when [A⁻] = [HA], log(1) = 0 and pH = pKa exactly. Effective buffers operate within about one pH unit of the pKa, where both components are present in significant amounts. Outside that range, the buffer capacity becomes too small to resist change.

The four main calculation types — strong acid/base, weak acid/base (ICE table), buffer (Henderson-Hasselbalch), and salt hydrolysis — build directly on equilibrium concepts. Recognizing which type of problem you face before calculating is the most valuable skill; the arithmetic is secondary.
