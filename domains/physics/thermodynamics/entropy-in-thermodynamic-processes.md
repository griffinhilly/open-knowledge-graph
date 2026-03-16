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
status: validated
---

# Entropy Changes in Thermodynamic Processes

## Core Idea
Entropy changes are calculated using ΔS = ∫dQ_rev/T along any reversible path connecting the initial and final states, since S is a state function. For isothermal processes: ΔS = Q/T. For adiabatic reversible processes: ΔS = 0 (isentropic). Heating at constant pressure from T₁ to T₂: ΔS = nCp ln(T₂/T₁). For irreversible processes, one must find an equivalent reversible path. In any irreversible process, the entropy generated is strictly positive.

## How It's Best Learned
Calculate ΔS for heat flowing from a hot reservoir into a cold object. Sum the entropy changes of both: the hot reservoir loses |Q|/T_H and the cold object gains |Q|/T_C. Since T_C < T_H, the net entropy increases.

## Common Misconceptions
- You cannot use ΔS = Q/T for an irreversible process at a fixed temperature — you must find a reversible path between the same endpoints.
- ΔS = 0 for a reversible adiabatic process, but not for all adiabatic processes — an irreversible adiabatic process generates entropy.

## Explainer

From your study of entropy and thermodynamic processes, you know that entropy S is a state function — it depends only on the current state of the system, not on how it got there. This is the crucial fact that makes entropy changes calculable. Even if the actual process is irreversible (and most real processes are), you can compute ΔS by finding *any* reversible path connecting the same initial and final states, then integrating dQ_rev/T along that path. The answer will be the same regardless of which reversible path you choose, because S is a state function.

For an **isothermal process** (T constant), the integral simplifies to ΔS = Q/T, because T can come out of the integral. This applies to isothermal compression or expansion of an ideal gas, or to phase transitions at constant temperature and pressure. Be careful: Q here is the actual heat exchanged during the reversible version of the process. For a **reversible adiabatic** (isentropic) process, Q = 0 at every step by definition, so ΔS = 0. These processes move along lines of constant entropy in the P-V or T-S diagram. For heating at constant pressure from T₁ to T₂, dQ_rev = nC_p dT, giving ΔS = nC_p ln(T₂/T₁). The logarithm reflects the diminishing return on adding heat at higher temperatures — each joule added to a hot system increases its entropy less than the same joule added to a cold one.

The most important skill is handling irreversible processes. The key rule: **never use ΔS = Q_irrev/T** for an irreversible process, even if temperature is constant. The Q that appears in the Clausius inequality dS ≥ dQ/T is the actual heat exchanged — for irreversible processes, dS > dQ/T, not equality. Instead, identify the initial and final states, construct any convenient reversible path between them, and integrate dQ_rev/T along that path. For example, free expansion of an ideal gas into a vacuum: Q = 0, W = 0, so T and U don't change. The actual process is irreversible. But the reversible path between the same two states (same T, different V) is an isothermal expansion, giving ΔS = nR ln(V₂/V₁) > 0. The entropy increased even though no heat flowed in the actual process.

The second law says that in any irreversible process, the **total entropy of system plus surroundings increases**. When heat Q flows from a hot reservoir at T_H into a cold body at T_C, the hot reservoir loses Q/T_H and the cold body gains Q/T_C. Since T_C < T_H, the gain exceeds the loss, and the universe's entropy increases by Q(1/T_C − 1/T_H) > 0. This entropy production is unavoidable in any spontaneous, irreversible process — it is the thermodynamic signature of irreversibility itself. Only in the idealized reversible limit does entropy production vanish, and that limit is never quite reached in practice.
