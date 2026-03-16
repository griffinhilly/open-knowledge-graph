---
id: clausius-inequality
title: The Clausius Inequality
domain: physics
course: thermodynamics
prerequisites:
- id: second-law-of-thermodynamics
  type: hard
- id: entropy-intro
  type: hard
builds-toward:
- third-law-absolute-entropy
- thermodynamic-availability-exergy
tags:
- second-law
- entropy
- irreversibility
stage: formal-systems
status: draft
---

# The Clausius Inequality

## Core Idea
The Clausius inequality states that for any process, dS ≥ đQ/T, with equality holding for reversible processes and strict inequality for irreversible processes. Integrating over a complete cycle gives ∮(đQ/T) ≤ 0, with the integral being zero only for reversible cycles. The Clausius inequality provides a mathematical expression of the second law and establishes entropy as a measure of irreversibility and the spontaneity of processes.

## How It's Best Learned
Prove the Clausius inequality from the Carnot cycle and second law. Apply it to irreversible processes and cycles to verify sign changes.

## Common Misconceptions
- Forgetting the T in the denominator (đQ/T, not just đQ).
- Assuming equality always holds (only for reversible processes).
- Confusing Clausius inequality with entropy change definition.

## Explainer

You know the second law — heat flows spontaneously from hot to cold, and no engine converts all heat to work — and you know entropy as a state function measuring disorder or the number of accessible microstates. The **Clausius inequality** is the quantitative bridge between them: for any process, it tells you whether entropy has increased or decreased and by how much relative to the heat exchanged, giving the second law a precise mathematical form.

The physical reasoning begins with what we know about the most efficient possible cycle. A **Carnot cycle** operating reversibly between temperatures T_H and T_C has efficiency η = 1 − T_C/T_H, which means Q_C/Q_H = T_C/T_H. With careful sign convention (Q_H > 0 absorbed at T_H, Q_C > 0 rejected at T_C), this gives Q_H/T_H − Q_C/T_C = 0. For any *irreversible* cycle between the same temperatures, Carnot's theorem says the efficiency is strictly less: more heat is rejected per unit of heat absorbed, so Q_C/Q_H > T_C/T_H, giving Q_H/T_H − Q_C/T_C < 0. Any real cycle can be approximated by a sum of Carnot sub-cycles, leading to the general statement: **∮ đQ/T ≤ 0** for any cyclic process, with equality if and only if the cycle is entirely reversible.

For a non-cyclic process from state A to state B, combine the actual process with a reversible return path from B to A. The cycle inequality gives ∫_{A→B,actual} đQ/T + ∫_{B→A,rev} đQ/T ≤ 0. The second integral equals −(S_B − S_A) because entropy is a state function and the path is reversible (dS = đQ/T exactly on a reversible path). Rearranging: **S_B − S_A ≥ ∫_A^B đQ/T**, or in differential form **dS ≥ đQ/T**, with equality only on a reversible path. For an isolated system (đQ = 0), this gives dS ≥ 0 — the entropy of an isolated system never decreases. This is the second law in its sharpest form.

The difference σ = ΔS − ∫ đQ/T ≥ 0 is the **entropy generated** internally by irreversibility — friction, heat transfer across a finite temperature difference, turbulence, chemical reactions out of equilibrium. A process with σ = 0 is reversible; any σ > 0 marks irreversibility and represents lost work. In engineering thermodynamics, minimizing entropy generation is the route to maximum efficiency. Practical sources of irreversibility — heat transfer across finite ΔT in a heat exchanger, throttling through a valve, mixing of fluids at different temperatures — each have quantifiable σ values. The Clausius inequality thus converts the qualitative second law ("irreversible processes increase entropy") into a quantitative tool: compute ∫ đQ/T along the process, compare to ΔS, and the gap directly measures how much work was irreversibly destroyed.
