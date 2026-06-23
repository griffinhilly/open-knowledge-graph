---
id: collision-theory-advanced-kinetics
title: Collision Theory of Reaction Rates
domain: chemistry
course: physical-chemistry
prerequisites:
- id: kinetic-theory-of-gases
  type: hard
- id: arrhenius-equation
  type: soft
- id: maxwell-boltzmann-distribution
  type: soft
- id: collisions-elastic-inelastic
  type: soft
- id: reaction-rate-and-factors-affecting-rate
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

## Questions

```yaml
- question: "The steric factor p in the collision theory rate constant is always ≤ 1. Which statement best explains why?"
  type: multiple-choice
  options:
    - "Molecules are approximately spherical, so all orientations are equally reactive."
    - "Only collisions with favorable relative geometry can lead to bond rearrangement, so most collisions are unproductive even above the energy threshold."
    - "Temperature limits the fraction of molecules with enough kinetic energy to react."
    - "The reactive cross-section equals the geometric cross-section for most molecules."
  answer: 1
  explanation: "Energy above E_a is necessary but not sufficient. For a reaction to occur, the attacking atom or group must approach the correct site on the target molecule — a geometric constraint captured by p. For small, symmetric molecules p ≈ 1, but for complex molecules where a specific bond must be attacked, p can be many orders of magnitude smaller than 1."

- question: "According to collision theory, raising the temperature increases the reaction rate solely because more collisions occur per unit time."
  type: true-false
  answer: false
  explanation: "Temperature does increase collision frequency, but only as Z ∝ T^(1/2) — a weak effect. The dominant contribution is through the Boltzmann factor exp(−E_a/RT): as T rises, the fraction of collisions with energy exceeding E_a grows exponentially. This exponential term is why even small temperature increases can dramatically accelerate reactions."

- question: "Collision theory predicts a pre-exponential factor A from first principles, yet experimental A values for complex bimolecular reactions are often far smaller than the collision-theory prediction. What physical quantity accounts for this discrepancy, and what does it represent?"
  type: short-answer
  answer: "The steric factor p (0 < p ≤ 1). It represents the fraction of collisions that have the correct relative orientation of reactants for the transition to products. A_experimental = p × A_collision theory. For reactions requiring precise alignment — such as an SN2 backside attack — p can be ≪ 1, explaining the large gap between predicted and observed pre-exponential factors."
  explanation: "Collision theory counts all collisions above E_a regardless of approach geometry. Introducing p as a correction factor salvages the Arrhenius form but exposes collision theory's key limitation: it does not model the orientational requirements from a potential energy surface. Transition state theory handles this more rigorously."
```

## Explainer

Collision theory asks a simple but profound question: how often do molecules collide, and of those collisions, which ones actually produce a reaction? From kinetic theory you already know that gas-phase molecules move with a distribution of speeds (the Maxwell–Boltzmann distribution) and collide billions of times per second. The challenge is connecting collision frequency to the macroscopic rate constant k.

Three conditions must be satisfied for a bimolecular collision to produce a reaction. First, the relative kinetic energy along the line of centers must exceed the activation energy E_a — only the fastest-moving fraction of molecules clears this bar, captured by the Boltzmann factor exp(−E_a/RT). Second, the molecules must actually encounter each other, which depends on their sizes (the collision cross-section σ, with units of area) and relative speed. Combining these gives the collision frequency Z, which scales as σ × (T/μ)^(1/2) × exp(−E_a/RT), where μ is the reduced mass. Third — and this is where collision theory goes beyond simple kinetic theory — the molecules must approach with the correct relative orientation. The steric factor p (between 0 and 1) captures this geometric requirement: p = 1 means every sufficiently energetic collision reacts, while p ≪ 1 means only a tiny fraction of energetic collisions have the right geometry.

Putting these together gives the collision-theory rate constant: k = p · σ · (8kT/πμ)^(1/2) · N_A · exp(−E_a/RT). The first three factors make up the collision-theory pre-exponential A, which you can calculate from molecular parameters. This is a genuine achievement: collision theory provides a physical interpretation for the empirical Arrhenius A factor. When you compare predicted and experimental A values, the ratio gives p directly — a window into the geometric selectivity of the reaction.

Collision theory works well for simple gas-phase reactions between small molecules (p ≈ 1) and correctly recovers the Arrhenius temperature dependence. It breaks down in two important regimes: for very light atoms where quantum tunneling through the barrier is significant (the theory assumes classical over-barrier passage), and for complex molecules where p is so small that geometric modeling is essential. These failures motivate the more rigorous transition state theory, which replaces the steric factor with a partition function ratio evaluated at the saddle point of the potential energy surface.

A useful intuition: think of each molecule as carrying a reaction "target" of effective area p·σ. Only a direct hit on that target, with enough kinetic energy, scores a reaction. Collision theory is the ballistic model of chemistry — it counts bullets and targets, but does not describe what happens at the moment of impact. Transition state theory addresses that gap.
