---
id: directed-acyclic-graphs
title: Directed Acyclic Graphs for Causal Modeling
domain: health-and-human-development
course: epidemiology
prerequisites:
- id: epidemiology-foundations
  type: hard
- id: confounding-epidemiology
  type: soft
builds-toward:
- counterfactual-framework
- sensitivity-analysis-epidemiology
tags:
- causal-inference
- dag
- graphical-models
- confounder-selection
stage: advanced
status: draft
---

# Directed Acyclic Graphs for Causal Modeling

## Core Idea
A directed acyclic graph (DAG) is a visual representation of causal assumptions about the relationships among variables. DAGs help identify minimal sufficient sets of confounders to adjust for to block backdoor paths (non-causal paths from exposure to outcome). DAGs clarify whether a variable is a confounder, mediator, or collider, preventing unnecessary or harmful adjustment.
