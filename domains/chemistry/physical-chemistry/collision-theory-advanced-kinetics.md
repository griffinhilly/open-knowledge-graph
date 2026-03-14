---
id: collision-theory-advanced-kinetics
title: Collision Theory of Reaction Rates
domain: chemistry
course: physical-chemistry
prerequisites:
- id: chemical-kinetics
  type: hard
- id: kinetic-theory-of-gases
  type: hard
- id: arrhenius-equation
  type: soft
- id: maxwell-boltzmann-distribution
  type: soft
builds-toward:
- transition-state-theory
- potential-energy-surfaces
tags:
- collision-theory
- steric-factor
- collision-frequency
- reaction-cross-section
- activation-energy
stage: advanced
status: validated
---

# Collision Theory of Reaction Rates

## Core Idea
Collision theory models reaction rates by calculating the frequency of bimolecular collisions with sufficient energy to overcome the activation barrier. The rate constant is k = p·σ·(8kT/πμ)^(1/2)·N_A·exp(−E_a/RT), where σ is the collision cross-section, μ is the reduced mass, and p is the steric factor (fraction of collisions with favorable geometry). Collision theory correctly predicts the Arrhenius temperature dependence and provides a physical interpretation of the pre-exponential factor A. However, it underestimates rates when quantum tunneling is important and overestimates when geometric constraints are severe, motivating the more refined transition state theory.

## How It's Best Learned
Calculate predicted rate constants for simple gas-phase reactions using collision theory, then compare to experimental values. The ratio gives the steric factor p, and examining trends across a series of reactions builds intuition about geometric requirements.

## Common Misconceptions
- Thinking all high-energy collisions lead to reaction — orientation matters (steric factor p < 1).
- Confusing the collision cross-section σ with the molecular diameter; σ is a reactive cross-section that can differ greatly from the geometric one.
