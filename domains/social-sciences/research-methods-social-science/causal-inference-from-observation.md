---
id: causal-inference-from-observation
title: 'Causal Inference from Observational Data: Fundamental Problem'
domain: social-sciences
course: research-methods-social-science
prerequisites:
- id: multilevel-hierarchical-modeling-nesting
  type: hard
- id: causal-inference-observational-data
  type: soft
- id: conditional-probability
  type: soft
builds-toward:
- natural-experiments-identification-strategy
- instrumental-variables-causal-effects
- regression-discontinuity-sharp-fuzzy
- matching-and-weighting-causal-estimation
tags:
- causal-inference
- observational
- confounding
- identification
stage: advanced
status: draft
---

# Causal Inference from Observational Data: Fundamental Problem

## Core Idea
The fundamental problem of causal inference is observing only one potential outcome per unit. Causal claims require assumptions: no unmeasured confounding, common support, consistency. This section reviews the potential outcomes framework and assumptions needed for causal identification from observational data.

## Explainer

The fundamental problem of causal inference arises from a simple impossibility: you cannot observe the same unit in two states simultaneously. To know whether a policy caused an outcome, you would need to see the same person both treated and untreated at the same moment — which is physically impossible. What you observe is called the **factual outcome**; what would have happened under the counterfactual condition is the **potential outcome**. The causal effect for any individual is the difference between these two potential outcomes, but since only one is ever observed, individual-level causal effects are inherently unidentifiable without further assumptions. This is the fundamental problem — not a technical limitation to be engineered around, but a logical constraint on all causal inference.

The **potential outcomes framework** (associated with Rubin) formalizes this logic. Each unit *i* has two potential outcomes: *Y_i(1)* if treated, *Y_i(0)* if not. The treatment effect for unit *i* is *Y_i(1) − Y_i(0)*. Researchers typically estimate the **Average Treatment Effect (ATE)** — the mean of individual effects across the population — or the **Average Treatment Effect on the Treated (ATT)**. But to estimate either, you need a comparison group whose untreated outcomes represent what the treated group's outcomes *would have been* absent treatment. In a randomized experiment, random assignment ensures this by making treatment statistically independent of potential outcomes. In observational data, no such guarantee exists — and the entire project of observational causal inference is constructing credible comparisons in its absence.

The three identification assumptions for causal inference from observational data are: **ignorability** (also called unconfoundedness or no unmeasured confounding), **common support** (or overlap), and **consistency** (or SUTVA). Ignorability means that, conditional on observed covariates, treatment assignment is as-if random — there are no unmeasured variables that jointly predict treatment and outcome. Common support means that every unit has a nonzero probability of receiving each treatment level: you cannot extrapolate causal effects to covariate regions with no counterfactual comparisons. Consistency means that the potential outcome under a given treatment level is well-defined and the same regardless of *how* treatment was received — an assumption violated when treatment is heterogeneous in ways that matter.

Violations of these assumptions are the central concern of observational causal inference. **Unmeasured confounders** — variables that predict both who receives treatment and what outcomes they achieve — bias naive estimates. The classic example: students who attend tutoring programs tend to be more motivated, so the "tutoring effect" estimated by comparing tutored versus untutored students conflates the program's effect with pre-existing motivation differences. Your prior work on conditional probability gives you the formal language: a confounder is a variable *C* such that treatment *T* and outcome *Y* are not independent, but become independent once you condition on *C*. Multilevel models (your hard prerequisite) highlight why this is especially difficult in nested data: individual-level unobservables may correlate at the group level, creating confounding that simple covariate adjustment cannot resolve. The downstream strategies — natural experiments, instrumental variables, regression discontinuity — are all attempts to recover credible causal identification when ignorability cannot be assumed to hold on observables alone.
