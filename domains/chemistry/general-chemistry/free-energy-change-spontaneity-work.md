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
stage: formal-systems
status: validated
---

# Gibbs Free Energy and Spontaneity Prediction

## Core Idea
Gibbs free energy (G = H − TS) combines enthalpy and entropy into a single criterion for spontaneity at constant T and P. ΔG < 0 indicates a spontaneous process; ΔG > 0 is non-spontaneous; ΔG = 0 indicates equilibrium. ΔG = ΔH − TΔS shows how temperature affects spontaneity: high temperature favors entropy-driven processes.

## How It's Best Learned
Calculate ΔG from ΔH and ΔS data; analyze how temperature changes affect spontaneity; relate ΔG to K via ΔG° = −RT ln K.

## Questions

```yaml
- question: "A reaction has ΔH = +80 kJ/mol and ΔS = +200 J/mol·K. Under what temperature condition does this reaction become spontaneous?"
  type: multiple-choice
  options:
    - "Never — the positive ΔH means the reaction always requires energy input, so ΔG is always positive"
    - "Always — the positive ΔS guarantees spontaneity regardless of temperature"
    - "Only at temperatures above 400 K, where TΔS exceeds ΔH and makes ΔG negative"
    - "Only at very low temperatures, where entropic effects are minimal and enthalpy drives the process"
  answer: 2
  explanation: "ΔG = ΔH − TΔS. Setting ΔG = 0 gives the crossover temperature: T = ΔH/ΔS = 80,000 J/mol ÷ 200 J/mol·K = 400 K. Below 400 K, ΔH dominates and ΔG > 0 (non-spontaneous). Above 400 K, TΔS > ΔH and ΔG < 0 (spontaneous). Option A is the critical misconception: endothermic does not mean non-spontaneous. When ΔS is positive, sufficiently high temperature can always drive a reaction spontaneous regardless of ΔH. Ice melting (ΔH > 0, ΔS > 0) is the everyday example — non-spontaneous below 0°C, spontaneous above it."

- question: "Methane combustion has a large negative ΔG° at room temperature. A student concludes that methane must ignite spontaneously when exposed to air at room temperature. What is wrong with this reasoning?"
  type: multiple-choice
  options:
    - "Nothing — ΔG° < 0 always means a reaction proceeds spontaneously at a measurable rate"
    - "ΔG° predicts thermodynamic favorability (the destination), not kinetic accessibility (the rate); a large activation energy can prevent a thermodynamically spontaneous reaction from proceeding measurably"
    - "Methane combustion actually has ΔG° > 0 at room temperature because oxygen is a co-reactant"
    - "ΔG° only applies under standard conditions; at atmospheric pressure the reaction is non-spontaneous"
  answer: 1
  explanation: "Thermodynamics and kinetics are distinct. ΔG° tells you about the relative stability of products vs. reactants — the 'destination.' A large negative ΔG° means products are much more stable than reactants, so the system will tend toward products *if it can get there*. But if there is a large activation energy barrier, the reaction proceeds immeasurably slowly despite being thermodynamically favorable. Methane is thermodynamically unstable in air but kinetically stable at room temperature — a spark (activation energy) is needed to overcome the barrier and initiate combustion."

- question: "For an endothermic reaction (ΔH > 0) with a positive entropy change (ΔS > 0), there exists a specific temperature below which the reaction is non-spontaneous and above which it is spontaneous."
  type: true-false
  answer: true
  explanation: "Yes. ΔG = ΔH − TΔS. When ΔH > 0 and ΔS > 0, these terms oppose each other: ΔH drives ΔG positive (non-spontaneous) while TΔS drives it negative (spontaneous). At low T, TΔS < ΔH and ΔG > 0. At high T, TΔS > ΔH and ΔG < 0. The crossover is at T = ΔH/ΔS — exactly the equilibrium temperature. For ice melting, this crossover is 273 K (0°C): non-spontaneous below, spontaneous above. The Gibbs equation predicts not just whether a process is spontaneous but at what temperature spontaneity switches on."

- question: "When ΔG = 0 for a reaction, no reaction is occurring — forward and reverse processes have both stopped at equilibrium."
  type: true-false
  answer: false
  explanation: "ΔG = 0 means the system is at equilibrium, but equilibrium is a dynamic state, not a static one. At the molecular level, forward and reverse reactions are both occurring continuously at equal rates, so there is no net change in concentration. The Gibbs equation connects to the equilibrium constant K via ΔG° = −RT ln K: when ΔG = 0 under the actual conditions, the reaction quotient Q equals K — the system has reached the concentration ratio where forward and reverse rates balance. 'No reaction' and 'equilibrium' are fundamentally different concepts."

- question: "Why does temperature act as a lever that can switch a reaction from non-spontaneous to spontaneous? Which types of reactions are temperature-sensitive in this way, and which are not?"
  type: short-answer
  answer: "Temperature appears in ΔG = ΔH − TΔS as the coefficient of the entropy term, amplifying or shrinking the entropy contribution. When ΔH and ΔS have the same sign, temperature determines which term dominates: for ΔH > 0, ΔS > 0 (endothermic, entropy-increasing), there is a crossover T = ΔH/ΔS above which the reaction becomes spontaneous; for ΔH < 0, ΔS < 0 (exothermic, entropy-decreasing), there is a crossover above which the reaction becomes non-spontaneous. These mixed-sign cases are temperature-sensitive. The temperature-insensitive cases are when ΔH and ΔS have opposite signs: ΔH < 0 and ΔS > 0 gives ΔG < 0 at all temperatures (always spontaneous); ΔH > 0 and ΔS < 0 gives ΔG > 0 at all temperatures (never spontaneous)."
  explanation: "This four-case analysis is one of the most useful frameworks in thermodynamics. Once you know the signs of ΔH and ΔS, you can predict qualitative spontaneity behavior across all temperatures without calculating ΔG numerically. The mixed-sign cases — where temperature is the controlling variable — are the most interesting chemically and include many biologically important processes like protein folding and nucleic acid hybridization."
```

## Explainer

From your study of entropy, you learned that the universe tends toward greater disorder — the second law of thermodynamics says total entropy (system + surroundings) must increase for a spontaneous process. But tracking entropy changes in both the system and its surroundings for every reaction is cumbersome. **Gibbs free energy** (G) solves this by packaging both considerations — enthalpy (which reflects heat flow to surroundings) and entropy (disorder within the system) — into a single quantity that refers only to the system. The defining relationship is ΔG = ΔH − TΔS, where T is absolute temperature in Kelvin.

The sign of ΔG tells you everything about spontaneity at constant temperature and pressure. When **ΔG < 0**, the process is spontaneous — it can proceed without external input. When **ΔG > 0**, the process is non-spontaneous and requires energy to drive it. When **ΔG = 0**, the system is at equilibrium. The equation reveals four scenarios depending on the signs of ΔH and ΔS. If a reaction is exothermic (ΔH < 0) and increases entropy (ΔS > 0), ΔG is negative at all temperatures — spontaneous always. If endothermic (ΔH > 0) and entropy-decreasing (ΔS < 0), ΔG is positive at all temperatures — never spontaneous. The interesting cases are the mixed ones: an endothermic reaction with positive ΔS becomes spontaneous at high enough temperature (the TΔS term eventually outweighs ΔH), while an exothermic reaction with negative ΔS becomes non-spontaneous at high temperature.

Consider the melting of ice: ΔH is positive (you must add heat) and ΔS is positive (liquid water is more disordered than solid ice). At low temperature, the ΔH term dominates and ΔG > 0 — ice does not melt spontaneously at −10°C. But at temperatures above 273 K (0°C), the TΔS term exceeds ΔH, making ΔG < 0, and ice melts spontaneously. The crossover point where ΔG = 0 is the melting point itself — the temperature at which the two phases coexist in equilibrium. This is the power of the Gibbs equation: it predicts not just whether a process is spontaneous, but at what temperature spontaneity switches on or off.

Gibbs free energy also connects thermodynamics to the maximum useful **work** a system can perform. The magnitude of ΔG equals the maximum non-expansion work (such as electrical work in a battery) obtainable from a process at constant T and P. This is why ΔG appears again in electrochemistry through the relationship ΔG° = −nFE°, linking free energy to cell potential. The connection to equilibrium is equally fundamental: ΔG° = −RT ln K relates the standard free energy change to the equilibrium constant, revealing that a large negative ΔG° corresponds to a large K (products strongly favored). These relationships make Gibbs free energy the single most versatile thermodynamic quantity in chemistry.
