---
id: entropy-and-gibbs-free-energy
title: Entropy and Gibbs Free Energy
domain: chemistry
course: general-chemistry
prerequisites:
- id: thermochemistry-enthalpy
  type: hard
builds-toward:
- chemical-equilibrium
- electrochemical-cells
tags:
- entropy
- Gibbs-free-energy
- spontaneity
- second-law
- ΔG
- ΔS
- thermodynamics
stage: formal-systems
status: validated
---

# Entropy and Gibbs Free Energy

## Core Idea
A process is thermodynamically spontaneous if the total entropy of the universe increases. Gibbs free energy (G) combines enthalpy and entropy: ΔG = ΔH − TΔS. A reaction is spontaneous at constant temperature and pressure when ΔG < 0. The four ΔH/ΔS sign combinations predict different temperature-dependence behaviors: always spontaneous (−ΔH, +ΔS), never spontaneous (+ΔH, −ΔS), or temperature-dependent. The relationship ΔG° = −RT ln K connects thermodynamics directly to the equilibrium constant.

## How It's Best Learned
Work through all four ΔH/ΔS combinations and predict spontaneity at high vs. low temperature. Calculate ΔG under non-standard conditions using ΔG = ΔG° + RT ln Q and practice interconverting between ΔG°, K, and E°cell.

## Common Misconceptions
- A spontaneous reaction is not necessarily fast — thermodynamics predicts whether a reaction can occur, not how quickly (that is kinetics). Diamond converting to graphite is spontaneous but immeasurably slow.
- Entropy is not simply 'disorder' — it is more precisely a measure of the number of accessible microstates, which generally (but not always) corresponds to what we intuitively call disorder.

## Questions

```yaml
- question: "A reaction has ΔH = +80 kJ/mol and ΔS = +200 J/(mol·K). At which temperature range does this reaction become spontaneous?"
  type: multiple-choice
  options: ["Below 400 K", "Above 400 K", "At any temperature", "Never — a positive ΔH makes it always non-spontaneous"]
  answer: 1
  explanation: "For spontaneity, ΔG = ΔH - TΔS < 0. With positive ΔH and positive ΔS, ΔG < 0 when TΔS > ΔH, i.e., T > ΔH/ΔS. Converting units: 80,000 J/mol ÷ 200 J/(mol·K) = 400 K. Above 400 K, the entropy term dominates and ΔG becomes negative. This is a temperature-dependent case — endothermic but entropy-driven."

- question: "A reaction with ΔG < 0 will occur quickly at room temperature because the negative free energy drives the reaction forward rapidly."
  type: true-false
  answer: false
  explanation: "ΔG predicts whether a reaction is thermodynamically favorable — whether it can release free energy — but says nothing about how fast it proceeds. Reaction rates are governed by kinetics, specifically the activation energy barrier. Diamond converting to graphite has ΔG < 0 at room temperature but proceeds at an immeasurably slow rate because the activation energy is enormous. Spontaneous and fast are independent properties."

- question: "What does the equation ΔG° = −RT ln K reveal about the relationship between thermodynamics and chemical equilibrium?"
  type: short-answer
  answer: "It shows that the standard free energy change directly determines the equilibrium constant: a large negative ΔG° corresponds to a large K (products strongly favored), while a positive ΔG° gives K < 1 (reactants favored). Thermodynamic spontaneity and equilibrium position are the same phenomenon viewed from different angles."
  explanation: "At equilibrium, ΔG = 0 — there is no net free energy available to drive further change. The standard value ΔG° tells you where equilibrium lies under standard conditions. If ΔG° = −20 kJ/mol, then K is large (around 3000 at 298 K), meaning the reaction runs strongly toward products. This bridges thermodynamics with the equilibrium constant you studied in chemical equilibrium, and it reappears in electrochemistry via ΔG° = −nFE°."
```

## Explainer

You learned from thermochemistry that reactions release or absorb heat (enthalpy, ΔH), and you have some intuition that certain processes seem to "want" to happen — gases expand, ice melts above 0°C, salt dissolves in water. But enthalpy alone cannot explain everything: some endothermic processes (like dissolving ammonium nitrate) occur spontaneously. What is the complete criterion for spontaneity? The answer involves entropy.

The second law of thermodynamics states that any spontaneous process increases the total entropy of the universe. But tracking the universe's entropy is impractical. Gibbs free energy (G) repackages this criterion into a single value computed from the system alone: ΔG = ΔH − TΔS. When ΔG < 0, the process increases universal entropy and is spontaneous. When ΔG > 0, it is non-spontaneous in the forward direction. When ΔG = 0, the system is at equilibrium. The formula reveals a competition: enthalpy drives reactions toward lower energy (negative ΔH favors spontaneity) while entropy drives reactions toward greater dispersal of energy and matter (positive ΔS favors spontaneity), and temperature determines which wins.

This yields four cases worth understanding clearly. If ΔH < 0 and ΔS > 0, both terms push toward negative ΔG — spontaneous at every temperature. If ΔH > 0 and ΔS < 0, both push positive — never spontaneous. If ΔH > 0 and ΔS > 0 (endothermic, entropy-increasing), the reaction is spontaneous only above a crossover temperature T = ΔH/ΔS, where the TΔS term overwhelms ΔH. If ΔH < 0 and ΔS < 0 (exothermic, entropy-decreasing), the reaction is spontaneous only below that crossover temperature. Notice the unit trap: ΔH is typically in kJ/mol while ΔS is in J/(mol·K) — you must convert before dividing.

Perhaps the most important conceptual point: ΔG says nothing about rate. Thermodynamics answers "can this reaction release free energy?" — kinetics answers "how fast?" These are entirely separate questions. Diamond is thermodynamically unstable relative to graphite (ΔG < 0 for the conversion at room temperature), yet your diamond ring is in no danger because the activation energy for the conversion is enormous. You need a favorable ΔG for a reaction to be possible, but you need a reasonable kinetic pathway for it to actually occur on a useful timescale.

Finally, ΔG° = −RT ln K directly connects the thermodynamic favorability you compute from ΔH and ΔS to the equilibrium position you learned in chemical equilibrium. A reaction with ΔG° = −40 kJ/mol strongly favors products (K ≈ 10⁷ at 298 K); a reaction with ΔG° = +20 kJ/mol strongly favors reactants (K ≈ 10⁻⁴). This relationship also reappears in electrochemistry: ΔG° = −nFE°, linking free energy to cell voltage. These three expressions — ΔG°, K, and E° — are all measures of the same underlying thermodynamic spontaneity, related by these equations.
