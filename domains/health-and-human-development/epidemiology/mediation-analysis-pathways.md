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
