---
id: sensitivity-analysis
title: Sensitivity Analysis
domain: biology
course: systems-biology
prerequisites:
- id: ode-models-in-biology
  type: hard
- id: parameter-estimation-in-biological-models
  type: hard
builds-toward:
- systems-pharmacology
tags:
- sensitivity-analysis
- local-sensitivity
- global-sensitivity
- Sobol-indices
- metabolic-control-analysis
stage: expert
status: validated
---
# Sensitivity Analysis

## Core Idea
Sensitivity analysis determines how changes in model parameters or inputs affect model outputs, identifying which parameters most strongly influence the system's behavior. Local sensitivity analysis computes partial derivatives of outputs with respect to individual parameters near a specific operating point. Global sensitivity analysis (Sobol indices, Morris screening) explores the full parameter space, accounting for interactions between parameters and nonlinear effects. In metabolic systems, metabolic control analysis (MCA) formalizes sensitivity as flux control coefficients and elasticity coefficients. Sensitivity analysis guides experimental design (measure the parameters that matter most), identifies drug targets (the most sensitive nodes in disease networks), and reveals which model predictions are robust versus parameter-dependent.

## Questions

```yaml
- question: "A model has 20 parameters. Local sensitivity analysis shows that the output is insensitive to parameter k7 at the current parameter values. Can you conclude k7 is universally unimportant?"
  type: multiple-choice
  options:
    - "Yes — if the output is insensitive at the current values, it will be insensitive everywhere"
    - "No — local sensitivity is computed at a single point in parameter space and can change dramatically at different parameter values; a parameter that is unimportant near one operating point may become critical in another regime"
    - "Yes — parameters are either important or not, regardless of their values"
    - "No — but only because local sensitivity analysis has computational errors"
  answer: 1
  explanation: "Local sensitivity is the partial derivative at a specific point — it describes the behavior in the immediate neighborhood of the current parameter values. Nonlinear systems can have very different sensitivity structures in different regions of parameter space. A parameter might be insensitive near steady state but critically important during a transient response, or unimportant at low concentrations but rate-limiting at high concentrations. Global sensitivity analysis addresses this by sampling across the entire plausible parameter range and computing variance-based indices (like Sobol indices) that capture importance across the full parameter space."

- question: "In metabolic control analysis, the sum of all flux control coefficients for a given flux equals 1 (the summation theorem). This means control of a pathway is always distributed across multiple enzymes."
  type: true-false
  answer: true
  explanation: "The summation theorem (sum of all flux control coefficients = 1) is one of the foundational results of metabolic control analysis. It means that if one enzyme has a high control coefficient (close to 1), all other enzymes must have coefficients close to 0 — but the total must sum to 1. In practice, control is typically distributed: several enzymes each contribute partial control, and no single enzyme is 'the' rate-limiting step. This overturned the classical concept of a single rate-limiting enzyme per pathway and has important implications for metabolic engineering (overexpressing one enzyme rarely increases flux proportionally because other enzymes share control)."

- question: "Why is global sensitivity analysis preferred over local sensitivity analysis for complex biological models with uncertain parameters?"
  type: short-answer
  answer: "Complex biological models have uncertain parameters (estimated from noisy data, not measured directly), so there is no single 'correct' operating point at which to evaluate local sensitivities. Global sensitivity analysis samples across the entire plausible parameter range and quantifies each parameter's contribution to output variance, accounting for nonlinear effects and parameter interactions that local analysis misses. Sobol indices decompose the total output variance into contributions from individual parameters (first-order) and parameter interactions (higher-order), providing a complete picture of which parameters and parameter combinations drive model uncertainty. This information directly guides experimental prioritization: measure the parameters with the highest Sobol indices first."
  explanation: "Morris screening (elementary effects method) provides a computationally cheaper alternative for high-dimensional models by classifying parameters as negligible, linear, or nonlinear/interacting. It serves as a useful first pass before the more computationally expensive variance-based Sobol analysis."
```

## Explainer

Every systems biology model, whether an ODE model of signaling dynamics or an FBA model of metabolism, depends on parameters whose values are uncertain. Sensitivity analysis asks: which of these uncertain parameters actually matter for the model's predictions? If the model output barely changes when a parameter varies over its plausible range, that parameter can be fixed at a nominal value without loss. If the output changes dramatically, that parameter is a priority for experimental measurement — and a potential point of biological control or therapeutic intervention.

**Local sensitivity analysis** is the simplest approach: compute the partial derivative of the output with respect to each parameter at the current operating point. For an ODE model, this can be done analytically (solving the sensitivity equations alongside the state equations) or numerically (perturbing each parameter by a small amount and observing the output change). The result is a sensitivity coefficient for each parameter that quantifies its local influence. In metabolic systems, this concept is formalized as **metabolic control analysis** (MCA), where the flux control coefficient C_i^J measures how much a fractional change in enzyme i's activity changes the flux J. The summation theorem (all flux control coefficients sum to 1) reveals that metabolic control is shared among enzymes, demolishing the concept of a single rate-limiting step.

**Global sensitivity analysis** goes further by exploring the entire plausible parameter range. **Sobol indices** decompose the total variance of the model output into contributions from individual parameters (first-order indices) and from interactions between parameters (higher-order indices). A parameter with a high first-order Sobol index drives substantial output uncertainty on its own; a parameter with a high total-order index (including interactions) may not matter individually but strongly modulates the effect of other parameters. **Morris screening** provides a cheaper alternative: it samples the parameter space with a design that estimates, for each parameter, the mean and variance of its elementary effect — classifying parameters as negligible (small mean, small variance), linearly important (large mean, small variance), or nonlinearly important or interacting (large variance).

The practical payoff of sensitivity analysis is threefold. For **experimental design**, it prioritizes which parameters to measure: invest limited experimental resources in the parameters that most influence model predictions. For **drug target identification**, the most sensitive nodes in a disease network model are the most promising therapeutic targets — perturbations at these nodes produce the largest phenotypic effects. For **model robustness assessment**, outputs that are insensitive to most parameters are reliable predictions even with uncertain parameter values, while outputs that are highly sensitive to poorly constrained parameters should be interpreted cautiously. Sensitivity analysis transforms a model from a black box into a transparent tool that communicates not just what it predicts, but how confident those predictions are and what drives the uncertainty.
