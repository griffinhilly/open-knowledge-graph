---
id: distribution-functions-moments
title: Distribution Functions and Moments
domain: physics
course: statistical-mechanics
prerequisites:
- id: probability-mass-functions-theory
  type: hard
- id: canonical-ensemble
  type: soft
tags:
- probability
- statistics
- fluctuations
stage: advanced
status: draft
---

# Distribution Functions and Moments

## Core Idea
Moments ⟨A^n⟩ and cumulants κ_n characterize the distribution P(A) of a fluctuating quantity. The mean μ = ⟨A⟩, variance σ^2 = ⟨(ΔA)^2⟩, skewness S = ⟨(ΔA)^3⟩/σ^3, and kurtosis K measure different aspects of the distribution. Cumulants are additive for independent variables, simplifying the analysis of sums of fluctuating quantities; they vanish for Gaussian distributions beyond the second cumulant.

## Explainer

From probability theory, you know that a distribution P(A) is fully characterized by all its **moments** ⟨A^n⟩ = ∫ A^n P(A) dA. The first moment is the mean, the second central moment is the variance, and higher moments describe the shape in increasingly refined ways. In statistical mechanics, observables like energy, magnetization, and particle number fluctuate around their equilibrium values; the canonical ensemble gives you the Boltzmann-weighted distribution of these fluctuations. The question is: which combinations of moments are most natural and useful for physics?

The answer is **cumulants** κ_n, defined through the cumulant-generating function K(t) = ln⟨e^{tA}⟩. Differentiating at t = 0 gives κ_1 = ⟨A⟩ (mean), κ_2 = ⟨(ΔA)²⟩ (variance), κ_3 = ⟨(ΔA)³⟩ (skewness numerator), and κ_4 = ⟨(ΔA)⁴⟩ − 3σ⁴ (excess kurtosis). That last expression — the fourth moment minus three times the squared variance — illustrates how cumulants correct for the "trivial" contribution of the Gaussian part of a distribution. The defining advantage of cumulants is **additivity**: for statistically independent variables A = A₁ + A₂ + ··· drawn from independent subsystems, κ_n(A) = κ_n(A₁) + κ_n(A₂) + ···. Raw moments do not have this property. Additivity reflects the physical fact that uncorrelated subsystems contribute independently to fluctuations — their individual statistics simply stack.

The deepest property of cumulants is their relationship to the **Gaussian distribution**: for a Gaussian, all cumulants beyond κ₂ vanish identically. This is the precise mathematical statement of why the Gaussian is "the simplest" distribution — it is completely characterized by just two parameters. Any nonzero higher cumulant is a measure of non-Gaussianity. In the canonical ensemble for large systems, the central limit theorem ensures that the distribution of extensive quantities (like total energy E) becomes approximately Gaussian with corrections of order 1/N. The relative fluctuations ΔE/⟨E⟩ ~ 1/√N vanish in the thermodynamic limit, justifying treating thermodynamic quantities as sharp. Higher cumulants of E, however, encode information about heat capacity fluctuations and correlations.

The practical importance of higher cumulants becomes dramatic near **phase transitions**. While the mean and variance typically vary smoothly with temperature, the kurtosis κ_4/σ⁴ can diverge at a critical point, signaling that large non-Gaussian fluctuations dominate because correlations extend across the whole system. This makes higher cumulants sensitive experimental probes: in heavy-ion collisions aimed at mapping the QCD phase diagram, the kurtosis of net-proton number distributions is predicted to change sign and diverge near a QCD critical point, providing a measurable signature that thermodynamic quantities alone cannot reveal. The additivity property also underlies the **cluster expansion** in statistical mechanics, where the nth cumulant corresponds to an irreducible n-point correlation function — the connected diagrams in a diagrammatic perturbation expansion.
