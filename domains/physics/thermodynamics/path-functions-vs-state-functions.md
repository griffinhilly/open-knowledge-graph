---
id: path-functions-vs-state-functions
title: Path Functions and State Functions
domain: physics
course: thermodynamics
prerequisites:
- id: first-law-of-thermodynamics
  type: hard
- id: work-in-thermodynamic-processes
  type: hard
builds-toward:
- exact-and-inexact-differentials
tags:
- thermodynamics
- mathematics
stage: formal-systems
status: draft
---

# Path Functions and State Functions

## Core Idea
State functions like internal energy, entropy, and enthalpy depend only on current state: ∮ dU = 0 around any closed cycle. Path functions like heat Q and work W depend on the route taken: different processes between same initial and final states yield different Q and W, even though ΔU is identical. Only state function differentials are exact.

## How It's Best Learned
Use the first law to derive that ΔU is path-independent by noting ΔU = Q - W and showing ΔU depends only on initial and final temperatures for an ideal gas. Compute Q and W for isothermal versus adiabatic compression between same endpoints; note Q and W differ but ΔU is identical.

## Common Misconceptions
- Treating heat and work as if they were state functions (they are path-dependent).
- Thinking that because Q and W are path-dependent, their sum (ΔU) is also path-dependent (the sum is always path-independent for a state function).
- Confusing 'state function' with 'measurable quantity' (Q and W are measurable but path-dependent).
