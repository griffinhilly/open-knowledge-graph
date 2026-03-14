---
id: kirchhoffs-rules
title: Kirchhoff's Rules
domain: physics
course: electricity-and-magnetism
prerequisites:
- id: dc-circuits-series-parallel
  type: hard
- id: conservation-of-energy
  type: soft
- id: systems-elimination
  type: soft
builds-toward:
- rc-circuits
- rl-circuits
tags:
- kirchhoff
- junction-rule
- loop-rule
- circuit-analysis
stage: formal-systems
status: validated
---

# Kirchhoff's Rules

## Core Idea
Kirchhoff's Junction Rule states that the algebraic sum of currents entering any node equals zero (charge conservation). The Loop Rule states that the sum of all potential differences around any closed loop is zero (energy conservation). Together they provide a systematic method to solve any DC circuit, regardless of complexity, by setting up a system of linear equations — one per independent loop — for unknown currents.

## How It's Best Learned
Label all currents with assumed directions before applying the rules — wrong assumed direction will give a negative answer, which is physically meaningful. Practice with 2-loop circuits before 3-loop ones. Connect the Loop Rule explicitly to energy conservation.

## Common Misconceptions
- If you assume a current direction and get a negative value, the current flows opposite to your assumption — this is correct, not an error.
- Both rules must be applied; neither alone is sufficient.
- The number of independent loop equations equals the number of loops minus the number of junctions plus one.
