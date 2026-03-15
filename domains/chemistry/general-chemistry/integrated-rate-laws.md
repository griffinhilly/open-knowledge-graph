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
