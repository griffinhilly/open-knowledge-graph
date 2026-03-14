---
id: third-law-absolute-entropy
title: The Third Law of Thermodynamics and Absolute Entropy
domain: physics
course: thermodynamics
prerequisites:
- id: entropy-intro
  type: hard
- id: statistical-interpretation-of-entropy
  type: soft
builds-toward:
- molar-heat-capacities
tags:
- entropy
- third-law
- absolute-values
stage: formal-systems
status: draft
---

# The Third Law of Thermodynamics and Absolute Entropy

## Core Idea
The third law of thermodynamics states that the entropy of a perfect crystal at absolute zero is zero: S(T=0) = 0. This allows the calculation of absolute entropy values S(T) = S(0) + ∫(C_p/T)dT from absolute zero to any temperature, rather than only entropy differences. The third law, combined with statistical mechanics, shows that entropy quantifies the number of accessible microstates and provides a natural definition of absolute entropy.

## How It's Best Learned
Use heat capacity data to integrate S(T) from 0 K to any temperature. Compare calculated absolute entropies with tabulated values.

## Common Misconceptions
- Thinking the third law forbids reaching absolute zero (it forbids reaching it in finite steps, not absolutely).
- Confusing the third law with energy conservation (first law).
- Assuming non-perfect crystals have exactly zero entropy at 0 K (residual entropy can exist).
