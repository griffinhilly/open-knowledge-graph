---
id: entropy-in-thermodynamic-processes
title: Entropy Changes in Thermodynamic Processes
domain: physics
course: thermodynamics
prerequisites:
- id: entropy-intro
  type: hard
- id: thermodynamic-processes
  type: hard
builds-toward:
- carnot-efficiency
tags:
- entropy-change
- isothermal
- adiabatic
- reversible
- irreversible
stage: formal-systems
status: draft
---

# Entropy Changes in Thermodynamic Processes

## Core Idea
Entropy changes are calculated using ΔS = ∫dQ_rev/T along any reversible path connecting the initial and final states, since S is a state function. For isothermal processes: ΔS = Q/T. For adiabatic reversible processes: ΔS = 0 (isentropic). Heating at constant pressure from T₁ to T₂: ΔS = nCp ln(T₂/T₁). For irreversible processes, one must find an equivalent reversible path. In any irreversible process, the entropy generated is strictly positive.

## How It's Best Learned
Calculate ΔS for heat flowing from a hot reservoir into a cold object. Sum the entropy changes of both: the hot reservoir loses |Q|/T_H and the cold object gains |Q|/T_C. Since T_C < T_H, the net entropy increases.

## Common Misconceptions
- You cannot use ΔS = Q/T for an irreversible process at a fixed temperature — you must find a reversible path between the same endpoints.
- ΔS = 0 for a reversible adiabatic process, but not for all adiabatic processes — an irreversible adiabatic process generates entropy.
