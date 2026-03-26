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
stage: expert
status: validated
---

# Mediation Analysis and Causal Pathways

## Core Idea
Mediation analysis decomposes the total effect of an exposure on an outcome into direct effects (not through the mediator) and indirect effects (through the mediator). Natural direct and indirect effects can be estimated using counterfactual definitions even when the mediator is affected by confounders influenced by the exposure.

## How It's Best Learned
Start with a simple three-variable example and manually compute direct and indirect effects using regression coefficients. Apply to a real dataset with multiple mediators and visualize the causal pathways.

## Common Misconceptions
- Mediation analysis identifies pathways (it quantifies associations; causal interpretation requires temporal ordering and unconfoundedness). - Controlling for a mediator removes confounding (mediators are downstream of exposure; controlling them may introduce bias). - Indirect effects must be smaller than total effects (with different outcome scales, indirect can exceed total effects).

## Questions

```yaml
- question: "A researcher estimates the direct effect of exercise (A) on cardiovascular disease (Y) by controlling for BMI (M, the proposed mediator). Exercise also causes inflammation (L), which confounds the BMI→CVD relationship. What is the key problem with simply adding M to the regression?"
  type: multiple-choice
  options:
    - "Adding M causes multicollinearity, inflating standard errors for the direct effect estimate"
    - "Conditioning on M opens a collider path through L, biasing both the direct and indirect effect estimates"
    - "The direct effect cannot be estimated without additional data on physical fitness levels"
    - "Adding M removes the indirect effect cleanly, leaving the direct effect correctly estimated"
  answer: 1
  explanation: "When L is affected by A and also confounds M→Y, conditioning on M in a regression creates a collider-stratification bias — opening a backdoor path through L. This is exposure-induced mediator-outcome confounding, one of the central scenarios where standard regression fails for mediation analysis. The common wrong intuition (option D) assumes that controlling for M is always safe for estimating the direct effect; this only holds when no variable affected by the exposure also confounds the mediator-outcome relationship."

- question: "A linear mediation model estimates: M = 0.4A + ε₁ and Y = 0.3A + 0.5M + ε₂. What is the indirect effect of A on Y through M, using the product method?"
  type: multiple-choice
  options:
    - "0.3 — the direct path coefficient from A to Y"
    - "0.5 — the path coefficient from M to Y"
    - "0.2 — the product of the A→M and M→Y path coefficients"
    - "0.7 — the sum of the direct effect and the mediator coefficient"
  answer: 2
  explanation: "The product method estimates the indirect effect as α₁ × β₂ = 0.4 × 0.5 = 0.2. The direct effect is β₁ = 0.3, and the total effect is 0.5. Option A is the direct effect alone. Option B (0.5) is the M→Y coefficient — the effect of the mediator on the outcome — not the indirect effect (which must also account for how much A moves M). Option D adds two quantities that don't belong together. In linear models, the product method and the difference method yield the same indirect effect."

- question: "Controlling for a mediator in a standard regression model typically removes the indirect effect without introducing bias into the direct effect estimate."
  type: true-false
  answer: false
  explanation: "This is false when exposure-induced mediator-outcome confounding is present — that is, when the exposure causes a variable that also confounds the mediator-outcome relationship. In that case, conditioning on the mediator opens a collider path, introducing bias into both the direct and indirect effect estimates. Standard regression can only recover valid natural direct and indirect effects when all four identification assumptions hold, including no such confounders. The solution requires weighting methods or the interventional effects framework."

- question: "In linear regression models, the product method (α₁ × β₂) and the difference method for estimating indirect effects yield the same answer."
  type: true-false
  answer: true
  explanation: "In linear models, both methods give the same indirect effect estimate. The product method multiplies the A→M path by the M→Y path. The difference method subtracts the direct effect coefficient (from the model including M) from the total effect coefficient (from the model without M). The algebraic equivalence breaks down in non-linear settings — binary outcomes, survival data — where the two methods diverge and the product method is no longer a valid estimate of the natural indirect effect."

- question: "Why does the presence of exposure-induced mediator-outcome confounding invalidate standard regression approaches to mediation analysis, and what does this imply about when mediation analysis is valid?"
  type: short-answer
  answer: "Exposure-induced mediator-outcome confounding occurs when the exposure causes a variable (L) that also confounds the mediator-outcome relationship. Conditioning on the mediator (as required to estimate the direct effect) simultaneously conditions on a collider with respect to L, opening a non-causal path that biases the estimates. This means the standard Baron-Kenny/product method regression approach is invalid anytime the exposure has downstream effects on any M-Y confounder. Valid mediation analysis in this scenario requires weighting methods (marginal structural models) or interventional effects defined without cross-world counterfactuals."
  explanation: "The core issue is that the mediator is not just an intermediate variable — it can be entangled with the confounding structure in ways that make conditioning on it harmful rather than helpful. Recognizing when this applies (any time the exposure causally affects anything that also confounds M→Y) is the practical skill that separates valid from invalid mediation analyses in the applied literature. The general lesson: opening one backdoor path to block confounding can simultaneously open another."
```

## Explainer

From your work with the counterfactual framework, you know that causal effects are defined by comparing potential outcomes: what would happen to person i under treatment A=1 versus A=0? Mediation analysis applies this same logic to a three-variable structure—an exposure A, a mediator M, and an outcome Y—and asks: how much of the total effect of A on Y flows through M (the indirect path A→M→Y), and how much bypasses M (the direct path A→Y not through M)?

The motivating intuition is epidemiological. Suppose you find that high educational attainment (A) reduces mortality (Y). That's a total effect—but it doesn't tell you *why*. Does education improve health by increasing income (M), which then provides better healthcare access? Or is there a direct effect through biological stress pathways, independent of income? If most of the effect is mediated by income, then an economic intervention could substitute for education; if there's a large direct effect, you'd need to target education itself. The **natural direct effect (NDE)** is defined as the effect of changing A from 0 to 1 while holding M fixed at the level it would take under A=0. The **natural indirect effect (NIE)** is the effect of changing M from its value under A=0 to its value under A=1, while holding A constant at 1. Total effect = NDE + NIE.

The regression-based product method makes this concrete. In a linear setting, if you fit: M = α₀ + α₁A + ε₁ and Y = β₀ + β₁A + β₂M + ε₂, then the indirect effect is estimated as α₁ × β₂ (the path A→M times the path M→Y) and the direct effect as β₁. This product method and the difference method (compare total effect to direct-only model coefficient) give the same answer in linear models. The complexity arises in non-linear settings (binary outcomes, survival data), where the two methods diverge and the counterfactual definitions of natural direct and indirect effects require careful identification assumptions.

The critical complication—and the point where regression intuitions most frequently break down—is **exposure-induced mediator-outcome confounding**. Suppose A causes a variable L that is both affected by A and confounds the M→Y relationship. For example: smoking (A) causes inflammation (L), which is also a confounder of the BMI (M) → cardiovascular disease (Y) relationship. In this case, conditioning on M in a regression model opens a collider path through L, introducing bias. Standard regression cannot recover natural direct and indirect effects in this scenario. The solution requires weighting methods (marginal structural models) or the **interventional (separable) effects** framework, which avoids "cross-world" counterfactuals. Recognizing when this problem applies—anytime the exposure causally affects anything that also confounds the mediator-outcome relationship—is the practical skill that separates valid from invalid mediation analyses in the applied literature.
