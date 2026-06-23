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
- id: statistical-distribution-molecular-energies
  type: soft
tags:
- pre-exponential
- collision
- theory
- kinetics
stage: advanced
status: validated
---

# Pre-exponential Factor and Collision Theory

## Core Idea
The pre-exponential factor A encodes the frequency and orientational requirements for successful collisions between reactant molecules. Collision theory predicts A from collision cross-sections, relative velocities, and steric factors. Comparing theoretical A values to experimental values reveals whether the reaction proceeds via a simple bimolecular collision or requires specific molecular orientations. Deviations indicate reaction complexity.

## Questions

```yaml
- question: "An experimentally measured pre-exponential factor A is 10,000 times smaller than the value predicted by collision theory for the same reaction. What is the most likely physical interpretation?"
  type: multiple-choice
  options:
    - "The activation energy was incorrectly measured, causing a systematic error in A"
    - "The reaction requires a very specific molecular orientation, so only a tiny fraction of geometrically possible collisions lead to reaction"
    - "Collision theory overestimates A at low temperatures because the Maxwell-Boltzmann distribution shifts"
    - "The collision cross-section is much larger than assumed, reducing the predicted collision frequency"
  answer: 1
  explanation: "When A_exp ≪ A_theory, the explanation is a severe steric requirement: the steric factor p = A_exp / A_theory ≪ 1. Only a tiny fraction of collisions have the correct geometric orientation for the reaction to proceed (e.g., an SN2 nucleophile must approach from the back side). p can be as small as 10⁻⁵ for highly orientation-specific reactions. The activation energy is determined separately from the slope of ln k vs 1/T and doesn't affect the comparison of A values."

- question: "A reaction between an ion and a dipolar molecule is found to have A_exp approximately 100 times LARGER than the hard-sphere collision theory prediction. Which explanation is most consistent with this observation?"
  type: multiple-choice
  options:
    - "There must be an error in the experimental measurement"
    - "The steric factor must exceed 1, which is impossible since p is always between 0 and 1"
    - "Long-range electrostatic attraction funnels reactants together more efficiently than hard-sphere geometry predicts"
    - "The reaction proceeds through a unimolecular mechanism rather than a bimolecular collision"
  answer: 2
  explanation: "When A_exp > A_theory, collision theory has broken down — its hard-sphere model underestimates how often productive encounters occur. Ion-dipole or strong hydrogen-bond interactions extend the effective range of interaction well beyond what hard-sphere contact assumes, so reactants find each other more often than the geometric cross-section would predict. Option B (p > 1) sounds like a logical fix but reveals a misunderstanding: p is defined as the ratio A_exp / A_theory and can exceed 1, but a p > 1 signals that the model assumptions are wrong, not that more than all collisions react."

- question: "The steric factor p can seldom exceed 1 because it represents the fraction of collisions with the correct orientation, and fractions can seldom be greater than 1."
  type: true-false
  answer: false
  explanation: "While p is conceptually defined as a fraction of 'correctly oriented' collisions and should be between 0 and 1 in the simple collision theory framework, experimentally derived p values (computed as A_exp / A_theory) can exceed 1. This occurs when long-range attractive forces (ion-dipole, hydrogen bonding) cause reactants to encounter each other more frequently than hard-sphere geometry predicts. A p > 1 is a diagnostic signal that collision theory's hard-sphere model is inadequate for that reaction."

- question: "The steric factor p and the activation energy Ea are independent parameters — a reaction can have a small steric factor (p ≪ 1) but still proceed rapidly at high temperatures."
  type: true-false
  answer: true
  explanation: "The Arrhenius equation separates these two effects: k = A·exp(−Ea/RT), where A = p·σ·⟨v_rel⟩·Nₐ. The steric factor p reduces A (the pre-exponential factor) regardless of temperature, but the exponential term exp(−Ea/RT) captures the fraction of collisions with sufficient energy. A reaction with p = 10⁻⁵ (very specific orientation needed) but low Ea can still be fast at high temperatures because the energy barrier is small. Conversely, a reaction with p ≈ 1 but very high Ea will be slow at low temperatures. The two factors are physically distinct and thermodynamically independent."

- question: "What physical phenomenon does the steric factor p represent, and how does the ratio A_experimental / A_theoretical diagnose the mechanism of a chemical reaction?"
  type: short-answer
  answer: "The steric factor p represents the fraction of collisions that have the correct molecular orientation for reaction to occur. Even if two molecules collide with enough energy to overcome the activation barrier, the reaction only proceeds if the reacting functional groups are properly aligned. A reaction with p ≈ 1 (like K + Br₂) can react from almost any approach angle; an SN2 reaction with p ~ 10⁻⁵ requires precise back-side attack. The ratio A_exp / A_theory reveals mechanism: when the ratio ≈ 1, simple hard-sphere collision adequately describes the reaction; when it is much less than 1, severe geometric constraints operate; when it exceeds 1, long-range attractive forces or a complex mechanism (like pre-association) makes the hard-sphere model insufficient, motivating more sophisticated treatments like transition state theory."
  explanation: "This comparison is the practical payoff of collision theory. Transition state theory, which replaced the steric factor with a full statistical mechanical treatment of the activated complex, was developed precisely because large deviations in A_exp / A_theory signaled that the simple 'billiard ball collision' picture was missing important physics."
```

## Explainer

From your study of the Arrhenius equation k = A·exp(−Ea/RT), you know that the exponential factor captures what fraction of collisions have enough energy to overcome the activation barrier. But what determines A, the pre-exponential factor that sits in front? Collision theory gives a physical answer: A represents how often molecules collide in the right way, independent of whether they have enough energy.

**Collision theory** starts from the kinetic theory of gases. Two molecules approaching each other will collide if their centers pass within a distance d₁₂ = (d₁ + d₂)/2, defining a **collision cross-section** σ = πd₁₂². The collision frequency Z — the total number of collisions per unit volume per unit time — depends on this cross-section, the number densities of the reactants, and their average relative velocity, which itself depends on temperature and the **reduced mass** μ of the colliding pair. For a bimolecular reaction A + B, the collision rate is Z_AB = N_A·N_B·σ·⟨v_rel⟩, where ⟨v_rel⟩ = √(8k_BT/πμ). This gives the maximum possible rate if every collision led to reaction.

The critical refinement is the **steric factor** p, a number between 0 and 1 that accounts for the fact that molecules must collide in the correct orientation for bonds to break and form. A reaction like K + Br₂ → KBr + Br has a steric factor near 1 because the electron transfer can happen at almost any approach angle. But a reaction requiring a specific geometric alignment — say, an SN2 attack where the nucleophile must approach the carbon from the back side — has p ≪ 1, sometimes as small as 10⁻⁵. The pre-exponential factor in collision theory is then A = p·σ·⟨v_rel⟩·N_A, combining geometry, molecular size, and thermal velocity into a single number with units of L·mol⁻¹·s⁻¹ for a bimolecular reaction.

Comparing the collision-theory prediction of A to the experimentally measured value is diagnostic. When A_exp ≈ A_theory, the reaction behaves like a simple hard-sphere collision — no unusual orientational demands. When A_exp ≪ A_theory, the steric requirements are severe, indicating the reaction needs a very specific molecular arrangement. When A_exp > A_theory, collision theory has broken down entirely, often because long-range attractive forces (ion-dipole, hydrogen bonding) funnel reactants together more effectively than hard-sphere geometry predicts, or because the reaction proceeds through a long-lived complex rather than a single direct collision. These deviations are precisely what motivates the more sophisticated transition state theory, which replaces the crude steric factor with a full statistical mechanical treatment of the activated complex.
