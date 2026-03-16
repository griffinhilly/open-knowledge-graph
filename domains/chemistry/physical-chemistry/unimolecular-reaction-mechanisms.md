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

## Explainer

From your study of chemical kinetics, you know that reaction rates depend on concentration, temperature, and activation energy. From transition state theory, you understand that reactions proceed through an activated complex at the top of an energy barrier. But here is a puzzle: if a molecule isomerizes or falls apart on its own — a **unimolecular reaction** — where does the activation energy come from? The molecule cannot simply decide to climb over an energy barrier. The answer, formalized in the **Lindemann mechanism**, is that collisions with other molecules provide the energy, even though the reaction itself involves only one molecule.

The Lindemann mechanism has two steps. First, a reactant molecule A collides with any molecule M and gains enough energy to become an activated species A* (activation step, rate constant k₁). Second, A* either loses its extra energy through another collision with M (deactivation, rate constant k₋₁) or proceeds to products (reaction, rate constant k₂). At **high pressure**, collisions are frequent, so activation and deactivation are both fast and in pseudo-equilibrium. The rate-limiting step is the reaction of A*, giving overall first-order kinetics: rate = k_uni[A]. At **low pressure**, collisions are rare, so every molecule that gets activated reacts before it can be deactivated. The rate-limiting step becomes the activation collision itself, giving second-order kinetics: rate = k₁[A][M]. The transition between these regimes — the **falloff region** — is where the rate constant depends on pressure, and this is the signature experimental fingerprint of a unimolecular reaction.

While the Lindemann mechanism captures the essential physics, it makes a crude prediction of the falloff curve that does not match experiments well. **RRKM theory** (Rice-Ramsperger-Kassel-Marcus) fixes this by treating energy redistribution within the molecule quantum mechanically. The key insight is that a molecule with enough total energy to react may not react immediately because that energy must flow into the specific vibrational mode — the **reaction coordinate** — that leads over the barrier. RRKM theory calculates the microcanonical rate constant k(E) as the ratio of the number of ways energy can be arranged in the transition state (W‡) to the density of states in the reactant (ρ). Molecules with energy concentrated in the reaction coordinate react faster; those with energy spread across many modes must wait for random fluctuations to channel enough energy into the right place.

A concrete example helps ground this. Consider the isomerization of cyclopropane to propene. At atmospheric pressure, this reaction is cleanly first-order — every cyclopropane molecule that gets activated has time to redistribute its energy and cross the barrier before the next collision. But in a low-pressure experiment (a few torr), the rate constant drops because activated molecules are not being replenished fast enough. RRKM theory predicts exactly how k_uni falls off with pressure, using only the molecule's vibrational frequencies and the barrier height as inputs. This quantitative success made RRKM the standard framework for understanding gas-phase reaction dynamics, from combustion chemistry to atmospheric reactions.
