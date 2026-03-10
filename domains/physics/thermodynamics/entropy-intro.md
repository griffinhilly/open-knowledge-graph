---
id: entropy-intro
title: Entropy
domain: physics
course: thermodynamics
prerequisites:
- id: second-law-of-thermodynamics
  type: hard
builds-toward:
- entropy-in-thermodynamic-processes
- statistical-interpretation-of-entropy
tags:
- entropy
- disorder
- irreversibility
- state-function
- Clausius
stage: formal-systems
status: draft
---

# Entropy

## Core Idea
Entropy (S) is a state function that quantifies the degree of disorder or the number of available microstates in a system. For a reversible process, the change in entropy is dS = δQ_rev/T. Entropy is additive and extensive. For irreversible processes, the entropy generated is always positive (ΔS_universe > 0), making entropy increase the arrow of time. At equilibrium, entropy is maximized. The units of entropy are J/K.

## How It's Best Learned
Compute entropy changes for simple reversible processes: isothermal expansion, heating at constant pressure. Then verify that combining two irreversible processes (e.g., heat flow across a finite temperature difference) always yields ΔS_universe > 0.

## Common Misconceptions
- Entropy is not simply 'disorder' in a qualitative sense — it has a precise mathematical definition tied to heat exchange and temperature.
- Entropy can decrease in a subsystem (e.g., a refrigerator cools its interior); only the total entropy of system plus surroundings must increase.
- High entropy does not mean high energy — entropy and energy are independent state variables.
