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
status: draft
---

# Unimolecular Reactions: Lindemann and RRKM Theory

## Core Idea
Unimolecular reactions (e.g., isomerizations, dissociations) require energy activation via collisions even for single-molecule transformations. The Lindemann mechanism explains the observed pressure dependence: at high pressure, activation and deactivation are fast, giving a first-order rate; at low pressure, every activated molecule reacts before being deactivated, giving apparent second-order kinetics. RRKM (Rice-Ramsperger-Kassel-Marcus) theory extends this with a quantum statistical treatment of intramolecular energy redistribution (IVR), expressing the microcanonical rate constant as k(E) = σ·W‡(E−E₀)/(h·ρ(E)), where W‡ is the number of transition-state states and ρ(E) is the reactant density of states.

## How It's Best Learned
Plot rate constant vs pressure for a unimolecular reaction, identifying the high-pressure and low-pressure limits. Then examine how RRKM predicts falloff behavior from molecular parameters (vibrational frequencies, moment of inertia, barrier height).

## Common Misconceptions
- Assuming unimolecular reactions are always first-order; they become second-order at low pressure.
- Thinking IVR is instantaneous; in some molecules, energy stays localized long enough to violate RRKM assumptions.
