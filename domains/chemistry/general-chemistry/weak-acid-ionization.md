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
stage: abstract-reasoning
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

## Explainer

From your work with chemical equilibrium, you know that reversible reactions settle into a state where the forward and reverse rates are equal, described by an equilibrium constant. Weak acid ionization is a specific application of that framework. When a weak acid HA dissolves in water, it partially dissociates: HA ⇌ H⁺ + A⁻. Unlike a strong acid (which ionizes completely), a weak acid reaches equilibrium with most molecules still in the undissociated HA form. The **acid ionization constant** Ka = [H⁺][A⁻]/[HA] tells you where that equilibrium lies. A Ka of 1.8 × 10⁻⁵ (acetic acid) means the equilibrium heavily favors HA — only a small fraction of molecules release a proton at any given moment.

The **ICE table** is the systematic method for solving these problems. You set up three rows — Initial, Change, Equilibrium — for each species. If you start with 0.10 M acetic acid and no products, the initial row is [HA] = 0.10, [H⁺] = 0, [A⁻] = 0. Define x as the amount that ionizes: the change row becomes −x, +x, +x, and the equilibrium row is 0.10 − x, x, x. Substituting into the Ka expression gives 1.8 × 10⁻⁵ = x²/(0.10 − x). This is where the **small-x approximation** becomes useful: if x is very small compared to 0.10, then 0.10 − x ≈ 0.10, and the equation simplifies to x² = 1.8 × 10⁻⁶, giving x = 1.3 × 10⁻³ M. Since 1.3 × 10⁻³ is only 1.3% of 0.10, the approximation is valid (under the 5% threshold). The pH is −log(1.3 × 10⁻³) ≈ 2.9.

**Percent ionization** — the fraction of original acid molecules that have donated a proton — reveals an important and initially surprising behavior. If you dilute the same acetic acid to 0.001 M, the percent ionization jumps from 1.3% to about 13%. This follows directly from Le Chatelier's principle, which you encountered in equilibrium: dilution decreases the concentration of all species, but the system responds by shifting toward the side with more particles (the products side, which has two ions versus one undissociated molecule). So weaker concentration means a larger *fraction* ionizes, even though the absolute [H⁺] decreases. This is why pH does not scale linearly with dilution for weak acids the way it does for strong acids.

When the small-x approximation fails — typically for acids with relatively large Ka or very dilute solutions where x is a significant fraction of the initial concentration — you must solve the full quadratic equation: Ka = x²/(C₀ − x), which rearranges to x² + Ka·x − Ka·C₀ = 0. Apply the quadratic formula, discard the negative root (concentrations cannot be negative), and you have an exact answer. The 5% rule is the quick diagnostic: calculate x with the approximation, divide by C₀, and if the result exceeds 5%, redo with the quadratic. Building the habit of checking this threshold prevents the most common error students make — blindly trusting an approximation that does not hold.
