---
id: free-energy-change-spontaneity-work
title: Gibbs Free Energy and Spontaneity Prediction
domain: chemistry
course: general-chemistry
prerequisites:
- id: entropy-disorder-randomness-fundamentals
  type: hard
- id: gibbs-free-energy-spontaneity
  type: soft
builds-toward:
- electrochemistry-basics
tags:
- gibbs-free-energy
- spontaneity
- work
- thermodynamics
stage: advanced
status: draft
---

# Gibbs Free Energy and Spontaneity Prediction

## Core Idea
Gibbs free energy (G = H − TS) combines enthalpy and entropy into a single criterion for spontaneity at constant T and P. ΔG < 0 indicates a spontaneous process; ΔG > 0 is non-spontaneous; ΔG = 0 indicates equilibrium. ΔG = ΔH − TΔS shows how temperature affects spontaneity: high temperature favors entropy-driven processes.

## How It's Best Learned
Calculate ΔG from ΔH and ΔS data; analyze how temperature changes affect spontaneity; relate ΔG to K via ΔG° = −RT ln K.

## Explainer

From your study of entropy, you learned that the universe tends toward greater disorder — the second law of thermodynamics says total entropy (system + surroundings) must increase for a spontaneous process. But tracking entropy changes in both the system and its surroundings for every reaction is cumbersome. **Gibbs free energy** (G) solves this by packaging both considerations — enthalpy (which reflects heat flow to surroundings) and entropy (disorder within the system) — into a single quantity that refers only to the system. The defining relationship is ΔG = ΔH − TΔS, where T is absolute temperature in Kelvin.

The sign of ΔG tells you everything about spontaneity at constant temperature and pressure. When **ΔG < 0**, the process is spontaneous — it can proceed without external input. When **ΔG > 0**, the process is non-spontaneous and requires energy to drive it. When **ΔG = 0**, the system is at equilibrium. The equation reveals four scenarios depending on the signs of ΔH and ΔS. If a reaction is exothermic (ΔH < 0) and increases entropy (ΔS > 0), ΔG is negative at all temperatures — spontaneous always. If endothermic (ΔH > 0) and entropy-decreasing (ΔS < 0), ΔG is positive at all temperatures — never spontaneous. The interesting cases are the mixed ones: an endothermic reaction with positive ΔS becomes spontaneous at high enough temperature (the TΔS term eventually outweighs ΔH), while an exothermic reaction with negative ΔS becomes non-spontaneous at high temperature.

Consider the melting of ice: ΔH is positive (you must add heat) and ΔS is positive (liquid water is more disordered than solid ice). At low temperature, the ΔH term dominates and ΔG > 0 — ice does not melt spontaneously at −10°C. But at temperatures above 273 K (0°C), the TΔS term exceeds ΔH, making ΔG < 0, and ice melts spontaneously. The crossover point where ΔG = 0 is the melting point itself — the temperature at which the two phases coexist in equilibrium. This is the power of the Gibbs equation: it predicts not just whether a process is spontaneous, but at what temperature spontaneity switches on or off.

Gibbs free energy also connects thermodynamics to the maximum useful **work** a system can perform. The magnitude of ΔG equals the maximum non-expansion work (such as electrical work in a battery) obtainable from a process at constant T and P. This is why ΔG appears again in electrochemistry through the relationship ΔG° = −nFE°, linking free energy to cell potential. The connection to equilibrium is equally fundamental: ΔG° = −RT ln K relates the standard free energy change to the equilibrium constant, revealing that a large negative ΔG° corresponds to a large K (products strongly favored). These relationships make Gibbs free energy the single most versatile thermodynamic quantity in chemistry.
