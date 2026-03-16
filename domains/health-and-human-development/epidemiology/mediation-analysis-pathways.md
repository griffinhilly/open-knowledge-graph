---
id: mediation-analysis-pathways
title: Mediation Analysis and Causal Pathways
domain: health-and-human-development
course: epidemiology
prerequisites:
- id: counterfactual-framework
  type: hard
- id: multivariable-regression-epi
  type: hard
builds-toward:
- social-epidemiology-pathways
tags:
- causal-inference
- mechanisms
- pathways
- indirect-effects
stage: advanced
status: draft
---

# Mediation Analysis and Causal Pathways

## Core Idea
Mediation analysis decomposes the total effect of an exposure on an outcome into direct effects (not through the mediator) and indirect effects (through the mediator). Natural direct and indirect effects can be estimated using counterfactual definitions even when the mediator is affected by confounders influenced by the exposure.

## How It's Best Learned
Start with a simple three-variable example and manually compute direct and indirect effects using regression coefficients. Apply to a real dataset with multiple mediators and visualize the causal pathways.

## Common Misconceptions
- Mediation analysis identifies pathways (it quantifies associations; causal interpretation requires temporal ordering and unconfoundedness). - Controlling for a mediator removes confounding (mediators are downstream of exposure; controlling them may introduce bias). - Indirect effects must be smaller than total effects (with different outcome scales, indirect can exceed total effects).

## Explainer

From your work with the counterfactual framework, you know that causal effects are defined by comparing potential outcomes: what would happen to person i under treatment A=1 versus A=0? Mediation analysis applies this same logic to a three-variable structure—an exposure A, a mediator M, and an outcome Y—and asks: how much of the total effect of A on Y flows through M (the indirect path A→M→Y), and how much bypasses M (the direct path A→Y not through M)?

The motivating intuition is epidemiological. Suppose you find that high educational attainment (A) reduces mortality (Y). That's a total effect—but it doesn't tell you *why*. Does education improve health by increasing income (M), which then provides better healthcare access? Or is there a direct effect through biological stress pathways, independent of income? If most of the effect is mediated by income, then an economic intervention could substitute for education; if there's a large direct effect, you'd need to target education itself. The **natural direct effect (NDE)** is defined as the effect of changing A from 0 to 1 while holding M fixed at the level it would take under A=0. The **natural indirect effect (NIE)** is the effect of changing M from its value under A=0 to its value under A=1, while holding A constant at 1. Total effect = NDE + NIE.

The regression-based product method makes this concrete. In a linear setting, if you fit: M = α₀ + α₁A + ε₁ and Y = β₀ + β₁A + β₂M + ε₂, then the indirect effect is estimated as α₁ × β₂ (the path A→M times the path M→Y) and the direct effect as β₁. This product method and the difference method (compare total effect to direct-only model coefficient) give the same answer in linear models. The complexity arises in non-linear settings (binary outcomes, survival data), where the two methods diverge and the counterfactual definitions of natural direct and indirect effects require careful identification assumptions.

The critical complication—and the point where regression intuitions most frequently break down—is **exposure-induced mediator-outcome confounding**. Suppose A causes a variable L that is both affected by A and confounds the M→Y relationship. For example: smoking (A) causes inflammation (L), which is also a confounder of the BMI (M) → cardiovascular disease (Y) relationship. In this case, conditioning on M in a regression model opens a collider path through L, introducing bias. Standard regression cannot recover natural direct and indirect effects in this scenario. The solution requires weighting methods (marginal structural models) or the **interventional (separable) effects** framework, which avoids "cross-world" counterfactuals. Recognizing when this problem applies—anytime the exposure causally affects anything that also confounds the mediator-outcome relationship—is the practical skill that separates valid from invalid mediation analyses in the applied literature.
