---
id: pre-exponential-factor-collision-theory
title: Pre-exponential Factor and Collision Theory
domain: chemistry
course: physical-chemistry
prerequisites:
- id: arrhenius-rate-constants-temperature
  type: hard
- id: molecular-partition-functions
  type: soft
tags:
- pre-exponential
- collision
- theory
- kinetics
stage: advanced
status: draft
---

# Pre-exponential Factor and Collision Theory

## Core Idea
The pre-exponential factor A encodes the frequency and orientational requirements for successful collisions between reactant molecules. Collision theory predicts A from collision cross-sections, relative velocities, and steric factors. Comparing theoretical A values to experimental values reveals whether the reaction proceeds via a simple bimolecular collision or requires specific molecular orientations. Deviations indicate reaction complexity.

## Explainer

From your study of the Arrhenius equation k = A·exp(−Ea/RT), you know that the exponential factor captures what fraction of collisions have enough energy to overcome the activation barrier. But what determines A, the pre-exponential factor that sits in front? Collision theory gives a physical answer: A represents how often molecules collide in the right way, independent of whether they have enough energy.

**Collision theory** starts from the kinetic theory of gases. Two molecules approaching each other will collide if their centers pass within a distance d₁₂ = (d₁ + d₂)/2, defining a **collision cross-section** σ = πd₁₂². The collision frequency Z — the total number of collisions per unit volume per unit time — depends on this cross-section, the number densities of the reactants, and their average relative velocity, which itself depends on temperature and the **reduced mass** μ of the colliding pair. For a bimolecular reaction A + B, the collision rate is Z_AB = N_A·N_B·σ·⟨v_rel⟩, where ⟨v_rel⟩ = √(8k_BT/πμ). This gives the maximum possible rate if every collision led to reaction.

The critical refinement is the **steric factor** p, a number between 0 and 1 that accounts for the fact that molecules must collide in the correct orientation for bonds to break and form. A reaction like K + Br₂ → KBr + Br has a steric factor near 1 because the electron transfer can happen at almost any approach angle. But a reaction requiring a specific geometric alignment — say, an SN2 attack where the nucleophile must approach the carbon from the back side — has p ≪ 1, sometimes as small as 10⁻⁵. The pre-exponential factor in collision theory is then A = p·σ·⟨v_rel⟩·N_A, combining geometry, molecular size, and thermal velocity into a single number with units of L·mol⁻¹·s⁻¹ for a bimolecular reaction.

Comparing the collision-theory prediction of A to the experimentally measured value is diagnostic. When A_exp ≈ A_theory, the reaction behaves like a simple hard-sphere collision — no unusual orientational demands. When A_exp ≪ A_theory, the steric requirements are severe, indicating the reaction needs a very specific molecular arrangement. When A_exp > A_theory, collision theory has broken down entirely, often because long-range attractive forces (ion-dipole, hydrogen bonding) funnel reactants together more effectively than hard-sphere geometry predicts, or because the reaction proceeds through a long-lived complex rather than a single direct collision. These deviations are precisely what motivates the more sophisticated transition state theory, which replaces the crude steric factor with a full statistical mechanical treatment of the activated complex.
