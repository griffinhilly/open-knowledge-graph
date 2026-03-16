---
id: dc-circuits-series-parallel
title: 'DC Circuits: Series and Parallel'
domain: physics
course: electricity-and-magnetism
prerequisites:
- id: ohms-law
  type: hard
- id: electric-power
  type: soft
builds-toward:
- kirchhoffs-rules
- rc-circuits
tags:
- dc-circuits
- series
- parallel
- resistors
- EMF
stage: abstract-reasoning
status: validated
---

# DC Circuits: Series and Parallel

## Core Idea
In a series circuit, components share the same current; equivalent resistance is R_eq = ΣRᵢ, and voltage divides among components. In a parallel circuit, components share the same voltage; equivalent resistance follows 1/R_eq = Σ(1/Rᵢ), and current divides. A real battery has an internal resistance r that reduces the terminal voltage below its EMF ε by an amount Ir. Multi-loop circuits with combinations of series and parallel elements are analyzed by successive reduction of equivalent resistances.

## How It's Best Learned
Build intuition by reducing complex resistor networks step by step: identify series pairs and parallel pairs, replace each with equivalent resistors, and repeat until one equivalent resistance remains. Always check limiting cases.

## Common Misconceptions
- Adding more resistors in series increases total resistance; in parallel, it decreases it.
- The terminal voltage of a battery is not equal to its EMF when current flows.
- Current does not 'choose' one path — in parallel branches, all paths carry current.

## Explainer

The fundamental difference between series and parallel comes down to what is shared. In a **series circuit**, the same current flows through every element — there is only one path, so every coulomb of charge must pass through each resistor in turn. The voltage, however, divides: each resistor "uses up" a portion proportional to its resistance, and those portions sum to the total voltage. Adding resistors in series always increases the total resistance because every resistor adds another obstacle to the same current.

In a **parallel circuit**, all elements share the same voltage — each branch connects directly across the same two terminals. But now the current divides among the branches, and each branch draws current independently of the others. Adding a new parallel branch creates an additional path, so total current increases and equivalent resistance decreases. The formula 1/R_eq = Σ(1/Rᵢ) reflects this: each new branch contributes a new term, and the equivalent resistance is always less than the smallest individual resistance.

A real battery introduces a practical complication: **internal resistance** r. No battery is a perfect voltage source — the electrochemical materials inside have finite resistance. When current I flows, the internal resistance drops voltage by Ir, so the **terminal voltage** (what you measure at the battery terminals) is V = ε − Ir, where ε is the EMF (the open-circuit voltage from the chemistry). Under heavy load (large I), terminal voltage sags noticeably below ε. This is why a nearly-dead battery reads close to its nominal voltage with no load but collapses when a motor draws current.

Analyzing a complex resistor network is a process of successive reduction. Look for resistors carrying identical current — that's series, and you can replace them with their sum. Look for resistors sharing identical terminal voltage — that's parallel, and you can replace them with 1/Σ(1/Rᵢ). Repeat until you have one equivalent resistor. The key discipline is checking limiting cases: short-circuiting one branch of a parallel network should drive R_eq toward zero; opening a series branch should drive R_eq toward infinity. If your formula gives the wrong limiting behavior, find the error before solving the full problem.
