---
id: spontaneity-and-gibbs-free-energy-intro
title: Spontaneity and ΔG
domain: chemistry
course: general-chemistry
prerequisites:
- id: entropy-and-disorder
  type: hard
- id: thermochemistry-enthalpy
  type: hard
builds-toward:
- gibbs-free-energy-spontaneity
- electrochemistry-basics
tags:
- spontaneity
- Gibbs free energy
- ΔG
stage: advanced
status: draft
---

# Spontaneity and ΔG

## Core Idea
The Gibbs free energy change (ΔG = ΔH - TΔS) combines enthalpy and entropy to predict spontaneity. A negative ΔG indicates a spontaneous process; positive ΔG indicates non-spontaneous.

## Explainer

You have already learned two separate ways to think about whether a reaction "wants" to happen. From thermochemistry, you know that exothermic reactions (negative ΔH) release energy and tend to be favorable. From entropy, you know that processes increasing disorder (positive ΔS) also tend to be favorable. But these two drives can conflict — an endothermic reaction can be spontaneous if it creates enough disorder, and a highly ordered product can form if enough energy is released. **Gibbs free energy** is the single quantity that settles this tug-of-war.

The equation **ΔG = ΔH − TΔS** combines both factors into one number. Think of it as a balance sheet: ΔH represents the enthalpy "cost" or "payment" of the reaction, while TΔS represents the entropy contribution scaled by temperature. When ΔG is negative, the combination of energy release and entropy increase (or one overwhelming the other) makes the process spontaneous — it can proceed without external input. When ΔG is positive, the process is non-spontaneous as written, though the reverse reaction would be spontaneous.

The temperature term is crucial and often underappreciated. Notice that T multiplies ΔS, not ΔH. This means entropy becomes more influential at higher temperatures. Consider ice melting: ΔH is positive (you must add heat to break hydrogen bonds) and ΔS is positive (liquid water is more disordered than ice). At low temperatures, the positive ΔH dominates and ΔG is positive — ice does not melt. At high temperatures, TΔS overwhelms ΔH and ΔG becomes negative — ice melts spontaneously. The crossover temperature where ΔG = 0 is exactly the melting point: T = ΔH/ΔS. This framework lets you predict not just *whether* a process is spontaneous but *at what temperature* it becomes spontaneous.

There are four possible sign combinations for ΔH and ΔS, and understanding them provides a powerful diagnostic tool. If ΔH is negative and ΔS is positive, ΔG is always negative — the reaction is spontaneous at every temperature (combustion reactions are a classic example). If ΔH is positive and ΔS is negative, ΔG is always positive — the reaction is never spontaneous under standard conditions. The interesting cases are the mixed signs, where temperature acts as the switch. Recognizing which case you are in lets you immediately predict how temperature will affect spontaneity without doing any arithmetic.
