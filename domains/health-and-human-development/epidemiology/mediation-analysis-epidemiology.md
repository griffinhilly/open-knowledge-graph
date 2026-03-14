---
id: mediation-analysis-epidemiology
title: Mediation Analysis and Pathways
domain: health-and-human-development
course: epidemiology
prerequisites:
- id: counterfactual-framework
  type: hard
- id: directed-acyclic-graphs
  type: hard
tags:
- causal-pathways
- direct-indirect-effects
- mechanisms
stage: advanced
status: draft
---

# Mediation Analysis and Pathways

## Core Idea
Mediation analysis decomposes a total causal effect into natural direct effects (paths not operating through the mediator) and natural indirect effects (pathways operating through a mediator). Understanding mediation requires carefully specifying the causal pathway and assumes no unmeasured confounding of the mediator-outcome relationship. Modern mediation methods can handle interactions between exposure and mediator, mediator-outcome confounding, and cross-level interactions.

## How It's Best Learned
Draw DAGs for exposure → mediator → outcome; calculate controlled and natural direct/indirect effects using counterfactual definitions.

## Common Misconceptions
Mediation analysis is simply about statistical association and regression adjustment. The indirect effect is always smaller than the total effect (with interactions it can exceed the total).
