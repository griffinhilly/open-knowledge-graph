---
id: integrated-rate-laws
title: Integrated Rate Laws
domain: chemistry
course: general-chemistry
prerequisites:
- id: chemical-kinetics
  type: hard
- id: exponential-functions-and-graphs
  type: soft
- id: antiderivatives
  type: soft
- id: differential-equations-intro
  type: soft
builds-toward:
- arrhenius-equation
tags:
- zero-order
- first-order
- second-order
- half-life
- integrated-rate-law
- graphical-method
- concentration-vs-time
stage: abstract-reasoning
status: draft
---
# Integrated Rate Laws

## Core Idea
Integrated rate laws relate concentration to time, enabling prediction of how much reactant remains after a given period. For a reaction A → products: zero order gives [A] = [A]₀ − kt (linear in [A] vs t); first order gives ln[A] = ln[A]₀ − kt (linear in ln[A] vs t, half-life t₁/₂ = 0.693/k); second order gives 1/[A] = 1/[A]₀ + kt (linear in 1/[A] vs t). The graphical method determines order experimentally: plot [A], ln[A], and 1/[A] against time, and whichever gives a straight line reveals the order. Half-life for first-order reactions is uniquely concentration-independent.

## How It's Best Learned
Memorize the three integrated forms and their corresponding straight-line plots. Practice determining order from graphical data — the linear plot identifies the order, the slope gives k (with appropriate sign). Work half-life problems for each order and notice how only first-order half-life is constant (radioactive decay is the classic example).

## Common Misconceptions
- Half-life is constant only for first-order reactions. For zero-order reactions, half-life decreases as concentration drops; for second-order, half-life increases as concentration drops.
- The integrated rate law describes concentration change over time for a single reactant. For reactions with multiple reactants, the pseudo-first-order approach (flooding one reactant in excess) is needed to isolate the dependence on one concentration.

## Explainer

From chemical kinetics, you know that rate laws express how reaction speed depends on concentration: rate = k[A]ⁿ, where n is the reaction order. But rate laws in that form tell you the instantaneous speed at a given moment — they don't directly answer the practical question "how much reactant is left after 30 minutes?" That's what **integrated rate laws** answer. They are the mathematical result of integrating the differential rate law over time, converting a statement about speed into a statement about concentration as a function of time.

For a **zero-order** reaction (rate = k, independent of concentration), integration gives [A] = [A]₀ − kt. Concentration decreases linearly with time, like a faucet draining at a constant rate regardless of how much water remains. The half-life is t₁/₂ = [A]₀/2k — it depends on starting concentration, so each successive half-life is shorter. For a **first-order** reaction (rate = k[A]), integration gives ln[A] = ln[A]₀ − kt, or equivalently [A] = [A]₀e⁻ᵏᵗ. This is exponential decay — the same mathematics that governs radioactive decay, which is why radioactive half-life is constant: t₁/₂ = 0.693/k, independent of how much material remains. For a **second-order** reaction (rate = k[A]²), integration gives 1/[A] = 1/[A]₀ + kt. The reaction slows dramatically as concentration drops, and the half-life t₁/₂ = 1/(k[A]₀) increases with each successive halving.

The **graphical method** is the experimental technique for determining reaction order. You measure concentration at several time points, then make three plots: [A] vs t, ln[A] vs t, and 1/[A] vs t. Whichever plot gives a straight line reveals the order — linear in [A] means zero-order, linear in ln[A] means first-order, linear in 1/[A] means second-order. The slope of the straight-line plot gives you the rate constant k (negative slope for zero and first order, positive for second order). This is why the integrated rate laws are written in y = mx + b form: they are designed to be linearized for graphical analysis.

A practical detail worth internalizing: first-order kinetics are by far the most common in chemistry and biology. Drug metabolism, radioactive decay, and many decomposition reactions follow first-order kinetics. The constant half-life property makes first-order processes especially intuitive — if a drug's half-life is 4 hours, then after 4 hours half remains, after 8 hours a quarter remains, after 12 hours an eighth remains, regardless of the initial dose. When a reaction involves multiple reactants, the **pseudo-first-order** technique simplifies analysis: flood one reactant in large excess so its concentration barely changes, and the rate law reduces to a first-order dependence on the other reactant.
