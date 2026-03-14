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
stage: formal-systems
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
