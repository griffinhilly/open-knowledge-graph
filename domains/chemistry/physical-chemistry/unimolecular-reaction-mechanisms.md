---
id: unimolecular-reaction-mechanisms
title: 'Unimolecular Reactions: Lindemann and RRKM Theory'
domain: chemistry
course: physical-chemistry
prerequisites:
- id: transition-state-theory
  type: hard
- id: potential-energy-surfaces
  type: soft
- id: chemical-kinetics
  type: soft
tags:
- Lindemann
- RRKM
- falloff
- pressure-dependence
- energy-randomization
- Rice-Ramsperger-Kassel
stage: advanced
status: validated
---

# Unimolecular Reactions: Lindemann and RRKM Theory

## Core Idea
Unimolecular reactions (e.g., isomerizations, dissociations) require energy activation via collisions even for single-molecule transformations. The Lindemann mechanism explains the observed pressure dependence: at high pressure, activation and deactivation are fast, giving a first-order rate; at low pressure, every activated molecule reacts before being deactivated, giving apparent second-order kinetics. RRKM (Rice-Ramsperger-Kassel-Marcus) theory extends this with a quantum statistical treatment of intramolecular energy redistribution (IVR), expressing the microcanonical rate constant as k(E) = σ·W‡(E−E₀)/(h·ρ(E)), where W‡ is the number of transition-state states and ρ(E) is the reactant density of states.

## How It's Best Learned
Plot rate constant vs pressure for a unimolecular reaction, identifying the high-pressure and low-pressure limits. Then examine how RRKM predicts falloff behavior from molecular parameters (vibrational frequencies, moment of inertia, barrier height).

## Common Misconceptions
- Assuming unimolecular reactions are always first-order; they become second-order at low pressure.
- Thinking IVR is instantaneous; in some molecules, energy stays localized long enough to violate RRKM assumptions.

## Questions

```yaml
- question: "A chemist measures the rate of a gas-phase isomerization at various pressures and finds: rate = k[A][M] at very low pressure, but rate = k[A] at high pressure. What causes the rate law to change?"
  type: multiple-choice
  options:
    - "The reaction mechanism changes from unimolecular to bimolecular at low pressure"
    - "At low pressure, the activation step (collision with M) is rate-limiting; at high pressure, the unimolecular reaction of A* is rate-limiting"
    - "The transition state structure changes at different pressures, altering the stoichiometry"
    - "Low-pressure experiments measure a different reaction because impurities become significant"
  answer: 1
  explanation: "The Lindemann mechanism explains this pressure dependence. At high pressure, collisions are frequent enough to maintain a steady concentration of activated molecules A* — the unimolecular step (A* → products, rate constant k₂) is rate-limiting, giving first-order kinetics in [A]. At low pressure, A* reacts before it can be deactivated, so every activation event directly leads to product. The activation step (A + M → A*, rate constant k₁) is now rate-limiting, and it depends on both [A] and [M], giving apparent second-order kinetics."

- question: "Why does RRKM theory predict the pressure-dependent falloff of unimolecular rate constants more accurately than the simple Lindemann mechanism?"
  type: multiple-choice
  options:
    - "RRKM includes relativistic corrections that Lindemann neglects at high temperatures"
    - "RRKM uses quantum statistical mechanics to account for energy redistribution into the specific reaction coordinate, not just whether total energy exceeds the barrier"
    - "RRKM assumes that all activated molecules react instantaneously, simplifying the rate expression"
    - "RRKM replaces the binary collision model with a field-theoretic treatment of intermolecular forces"
  answer: 1
  explanation: "The Lindemann mechanism treats any molecule with total energy above the barrier as equally likely to react, giving an oversimplified falloff prediction. RRKM theory recognizes that energy must flow into the specific vibrational mode (the reaction coordinate) that leads over the barrier. The rate constant k(E) = σ·W‡(E−E₀)/(h·ρ(E)) expresses this: W‡ counts the quantum states accessible at the transition state (energy channeled into the reaction coordinate), while ρ(E) counts all the ways the reactant molecule can distribute that energy. Molecules with energy spread across many non-reactive modes react slowly; those with energy concentrated in the reaction coordinate react faster. This microcanonical treatment produces quantitatively accurate falloff curves."

- question: "At sufficiently high pressure, the rate constant for a unimolecular reaction becomes independent of pressure and the reaction exhibits clean first-order kinetics."
  type: true-false
  answer: true
  explanation: "At high pressure (the high-pressure limit), collisions are so frequent that activation and deactivation maintain A* in a pseudo-equilibrium with A. Any A* that reacts is quickly replenished. The concentration of A* is proportional to [A], and since the rate-limiting step is the unimolecular decomposition of A*, the overall rate equals k_uni[A] — purely first-order in A and independent of the concentration of the bath gas M."

- question: "According to RRKM theory, once a molecule has accumulated enough total energy to exceed the reaction barrier, it reacts immediately, because intramolecular vibrational energy redistribution (IVR) is essentially instantaneous."
  type: true-false
  answer: false
  explanation: "This is the key assumption RRKM refines relative to the older RRK theory. RRKM explicitly accounts for the rate at which energy flows from non-reactive vibrational modes into the reaction coordinate. While RRKM assumes IVR is fast enough to justify a statistical (microcanonical) treatment, the actual rate k(E) depends on how many transition-state states are accessible — which depends on energy being in the right modes. Moreover, the Explainer notes that in some molecules, energy can remain localized long enough to violate RRKM assumptions entirely — this is an active area of chemical physics research."

- question: "Explain why a unimolecular gas-phase reaction that is first-order at atmospheric pressure becomes second-order at very low pressure."
  type: short-answer
  answer: "At atmospheric pressure, collisions with bath gas molecules (M) are frequent and maintain a steady-state population of activated reactant molecules (A*). The rate-limiting step is the unimolecular conversion A* → products, giving rate = k₂[A*] ∝ [A], i.e., first-order. At very low pressure, collisions are rare: a molecule that gains enough energy from a collision (A + M → A*) reacts before it can collide again and lose that energy. Now the rate-limiting step is the activation collision itself — rate = k₁[A][M] — which depends on both the reactant concentration and the bath gas concentration, giving second-order kinetics. The crossover between the two regimes is the falloff region, the experimental signature of a Lindemann mechanism."
  explanation: "The key is identifying which step is rate-limiting at each pressure limit. At high pressure, deactivation is fast relative to reaction (k₋₁[M] ≫ k₂), so A* equilibrates with A. At low pressure, reaction is fast relative to deactivation (k₂ ≫ k₋₁[M]), so every A* formed immediately proceeds to products."
```

## Explainer

From your study of chemical kinetics, you know that reaction rates depend on concentration, temperature, and activation energy. From transition state theory, you understand that reactions proceed through an activated complex at the top of an energy barrier. But here is a puzzle: if a molecule isomerizes or falls apart on its own — a **unimolecular reaction** — where does the activation energy come from? The molecule cannot simply decide to climb over an energy barrier. The answer, formalized in the **Lindemann mechanism**, is that collisions with other molecules provide the energy, even though the reaction itself involves only one molecule.

The Lindemann mechanism has two steps. First, a reactant molecule A collides with any molecule M and gains enough energy to become an activated species A* (activation step, rate constant k₁). Second, A* either loses its extra energy through another collision with M (deactivation, rate constant k₋₁) or proceeds to products (reaction, rate constant k₂). At **high pressure**, collisions are frequent, so activation and deactivation are both fast and in pseudo-equilibrium. The rate-limiting step is the reaction of A*, giving overall first-order kinetics: rate = k_uni[A]. At **low pressure**, collisions are rare, so every molecule that gets activated reacts before it can be deactivated. The rate-limiting step becomes the activation collision itself, giving second-order kinetics: rate = k₁[A][M]. The transition between these regimes — the **falloff region** — is where the rate constant depends on pressure, and this is the signature experimental fingerprint of a unimolecular reaction.

While the Lindemann mechanism captures the essential physics, it makes a crude prediction of the falloff curve that does not match experiments well. **RRKM theory** (Rice-Ramsperger-Kassel-Marcus) fixes this by treating energy redistribution within the molecule quantum mechanically. The key insight is that a molecule with enough total energy to react may not react immediately because that energy must flow into the specific vibrational mode — the **reaction coordinate** — that leads over the barrier. RRKM theory calculates the microcanonical rate constant k(E) as the ratio of the number of ways energy can be arranged in the transition state (W‡) to the density of states in the reactant (ρ). Molecules with energy concentrated in the reaction coordinate react faster; those with energy spread across many modes must wait for random fluctuations to channel enough energy into the right place.

A concrete example helps ground this. Consider the isomerization of cyclopropane to propene. At atmospheric pressure, this reaction is cleanly first-order — every cyclopropane molecule that gets activated has time to redistribute its energy and cross the barrier before the next collision. But in a low-pressure experiment (a few torr), the rate constant drops because activated molecules are not being replenished fast enough. RRKM theory predicts exactly how k_uni falls off with pressure, using only the molecule's vibrational frequencies and the barrier height as inputs. This quantitative success made RRKM the standard framework for understanding gas-phase reaction dynamics, from combustion chemistry to atmospheric reactions.
