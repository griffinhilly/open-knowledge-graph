---
id: weak-acid-ionization
title: Weak Acid Ionization
domain: chemistry
course: general-chemistry
prerequisites:
- id: chemical-equilibrium
  type: hard
- id: acid-base-chemistry
  type: hard
- id: logarithms-intro
  type: soft
builds-toward:
- weak-base-ionization
- polyprotic-acids
- buffer-solutions
tags:
- Ka
- acid-ionization-constant
- percent-ionization
- ICE-table
- weak-acid
- small-x-approximation
stage: advanced
status: draft
---
# Weak Acid Ionization

## Core Idea
A weak acid does not fully ionize in water — it establishes equilibrium between the undissociated acid (HA) and its ions (H⁺ and A⁻). The acid ionization constant Ka = [H⁺][A⁻]/[HA] quantifies the extent of ionization; smaller Ka means a weaker acid. Percent ionization = ([H⁺]eq/[HA]₀) × 100 increases as the initial acid concentration decreases (dilution shifts the equilibrium toward products). ICE tables (Initial, Change, Equilibrium) provide a systematic method for calculating equilibrium concentrations and pH. When Ka is very small relative to the initial concentration (Ka/C₀ < 0.05), the 'small x approximation' simplifies the algebra.

## How It's Best Learned
Master the ICE table setup: write the equilibrium expression, define x as the amount ionized, substitute into Ka, and solve. Always check the 5% rule for the small-x approximation — if x > 5% of the initial concentration, use the quadratic formula instead. Compare percent ionization at different concentrations to build intuition about equilibrium shifts.

## Common Misconceptions
- A weak acid with a large initial concentration can still produce a low pH (high [H⁺]). Weak does not mean dilute — it means the fraction that ionizes is small, but that fraction of a large concentration can still be substantial.
- The small-x approximation is a mathematical shortcut, not a chemical principle. When it fails (error > 5%), the full quadratic must be solved to get an accurate answer.

## Questions

```yaml
- question: "A 1.0 M acetic acid solution (Ka = 1.8 × 10⁻⁵) has a percent ionization of about 1.3%. If this solution is diluted to 0.001 M, what happens to the percent ionization?"
  type: multiple-choice
  options:
    - "It decreases to about 0.13% — dilution spreads the same ions over more volume"
    - "It stays at 1.3% — the Ka is fixed so the fraction ionized cannot change"
    - "It increases to about 13% — dilution shifts equilibrium toward the products side"
    - "It increases to 100% — at sufficiently low concentration, weak acids fully ionize"
  answer: 2
  explanation: "This is the key counterintuitive result of weak acid equilibria. Dilution decreases the concentration of all species, and Le Chatelier's principle predicts the system shifts toward the side with more particles (ionized products: H⁺ + A⁻ vs. undissociated HA) to partially restore the lost concentration. The result: a *larger fraction* of acid molecules ionize, even though the absolute [H⁺] decreases. At 1.0 M, only 1.3% ionizes; at 0.001 M, about 13% ionizes. The Ka is constant (not the percent ionization), so as C₀ decreases, [H⁺]eq/C₀ — the percent ionization — must increase."

- question: "You are setting up an ICE table for 0.10 M acetic acid (Ka = 1.8 × 10⁻⁵). Using the small-x approximation, you find x = 1.34 × 10⁻³ M. Should you accept this approximation?"
  type: multiple-choice
  options:
    - "No — always use the quadratic formula for accuracy"
    - "Yes — x/C₀ = 1.34 × 10⁻³ / 0.10 = 1.34%, which is well below the 5% threshold"
    - "No — the approximation is only valid when Ka > 10⁻³"
    - "Yes — the approximation is always valid for acetic acid regardless of concentration"
  answer: 1
  explanation: "The 5% rule checks whether the approximation introduces unacceptable error: if x/C₀ < 0.05 (5%), the approximation is valid. Here, 1.34 × 10⁻³ / 0.10 = 0.0134 = 1.34%, comfortably below 5%. The approximation (0.10 − x ≈ 0.10) is justified. Option D is wrong because the approximation fails for dilute solutions of the same acid — at 0.001 M acetic acid, x/C₀ ≈ 13%, requiring the quadratic. The validity of the approximation depends on the ratio Ka/C₀, not on the acid identity alone."

- question: "Diluting a weak acid decreases both the absolute [H⁺] concentration and the percent ionization."
  type: true-false
  answer: false
  explanation: "Dilution decreases the absolute [H⁺] (fewer moles of H⁺ per liter) but increases the percent ionization (a larger fraction of acid molecules have donated a proton). These two effects move in opposite directions. The absolute [H⁺] decreases because even though more molecules ionize proportionally, the total acid concentration has dropped so much that the absolute count falls. The percent ionization increases because Le Chatelier's principle drives the equilibrium toward the products side (more particles) when the solution is diluted. For strong acids, dilution does decrease both — because strong acids are always 100% ionized regardless of concentration."

- question: "A 'weak acid' is simply a dilute solution of an acid — calling it 'weak' means there isn't much acid present."
  type: true-false
  answer: false
  explanation: "'Weak' refers to the degree of ionization, not the concentration. A weak acid is one that only partially ionizes in water — it establishes an equilibrium between HA and H⁺ + A⁻ with Ka << 1. A strong acid (like HCl) ionizes essentially completely regardless of concentration. You can have a concentrated weak acid (e.g., 5 M acetic acid) or a dilute strong acid (e.g., 0.001 M HCl) — the weakness/strength describes the acid's intrinsic tendency to donate protons, quantified by Ka. This distinction matters because pH calculations for weak vs. strong acids require completely different methods."

- question: "Explain why percent ionization increases as a weak acid solution is diluted, even though the absolute [H⁺] decreases."
  type: short-answer
  answer: "Percent ionization is [H⁺]eq / C₀ × 100. When the solution is diluted, C₀ decreases faster than [H⁺]eq does, because the equilibrium shifts right (toward more ionization) in response to dilution. Le Chatelier's principle predicts this shift: dilution reduces the concentration of all species, but the products side (H⁺ + A⁻) has more particles, so shifting toward products partially counteracts the dilution. The equilibrium constant Ka is fixed, so as C₀ falls, a larger fraction of the remaining acid must ionize to satisfy Ka. The absolute [H⁺] does fall (numerator decreases), but the denominator C₀ decreases proportionally more, raising the ratio."
  explanation: "A mathematical way to see this: Ka = [H⁺][A⁻]/[HA] ≈ x²/(C₀ − x) ≈ x²/C₀. Solving: x ≈ √(Ka·C₀). Percent ionization = x/C₀ ≈ √(Ka·C₀)/C₀ = √(Ka/C₀). As C₀ decreases, √(Ka/C₀) increases — percent ionization scales with 1/√C₀. So halving the concentration increases percent ionization by a factor of √2 ≈ 1.41. This is why weak and strong acids behave differently on dilution: for a strong acid (x = C₀ always), percent ionization is always 100% regardless of concentration."
```

## Explainer

From your work with chemical equilibrium, you know that reversible reactions settle into a state where the forward and reverse rates are equal, described by an equilibrium constant. Weak acid ionization is a specific application of that framework. When a weak acid HA dissolves in water, it partially dissociates: HA ⇌ H⁺ + A⁻. Unlike a strong acid (which ionizes completely), a weak acid reaches equilibrium with most molecules still in the undissociated HA form. The **acid ionization constant** Ka = [H⁺][A⁻]/[HA] tells you where that equilibrium lies. A Ka of 1.8 × 10⁻⁵ (acetic acid) means the equilibrium heavily favors HA — only a small fraction of molecules release a proton at any given moment.

The **ICE table** is the systematic method for solving these problems. You set up three rows — Initial, Change, Equilibrium — for each species. If you start with 0.10 M acetic acid and no products, the initial row is [HA] = 0.10, [H⁺] = 0, [A⁻] = 0. Define x as the amount that ionizes: the change row becomes −x, +x, +x, and the equilibrium row is 0.10 − x, x, x. Substituting into the Ka expression gives 1.8 × 10⁻⁵ = x²/(0.10 − x). This is where the **small-x approximation** becomes useful: if x is very small compared to 0.10, then 0.10 − x ≈ 0.10, and the equation simplifies to x² = 1.8 × 10⁻⁶, giving x = 1.3 × 10⁻³ M. Since 1.3 × 10⁻³ is only 1.3% of 0.10, the approximation is valid (under the 5% threshold). The pH is −log(1.3 × 10⁻³) ≈ 2.9.

**Percent ionization** — the fraction of original acid molecules that have donated a proton — reveals an important and initially surprising behavior. If you dilute the same acetic acid to 0.001 M, the percent ionization jumps from 1.3% to about 13%. This follows directly from Le Chatelier's principle, which you encountered in equilibrium: dilution decreases the concentration of all species, but the system responds by shifting toward the side with more particles (the products side, which has two ions versus one undissociated molecule). So weaker concentration means a larger *fraction* ionizes, even though the absolute [H⁺] decreases. This is why pH does not scale linearly with dilution for weak acids the way it does for strong acids.

When the small-x approximation fails — typically for acids with relatively large Ka or very dilute solutions where x is a significant fraction of the initial concentration — you must solve the full quadratic equation: Ka = x²/(C₀ − x), which rearranges to x² + Ka·x − Ka·C₀ = 0. Apply the quadratic formula, discard the negative root (concentrations cannot be negative), and you have an exact answer. The 5% rule is the quick diagnostic: calculate x with the approximation, divide by C₀, and if the result exceeds 5%, redo with the quadratic. Building the habit of checking this threshold prevents the most common error students make — blindly trusting an approximation that does not hold.
