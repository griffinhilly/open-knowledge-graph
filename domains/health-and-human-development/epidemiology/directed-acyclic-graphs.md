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

## Explainer

You already understand confounding intuitively: a third variable that is associated with both the exposure and the outcome can make a non-causal association look causal (or vice versa). The trouble is that deciding what to adjust for in a study — which variables to include in a regression, which to stratify on — has historically been treated as an art guided by subject-matter intuition. **Directed acyclic graphs (DAGs)** make the causal assumptions explicit and then let formal rules determine the correct adjustment strategy.

A DAG is a graph where nodes represent variables and directed arrows (edges) represent direct causal effects. The "acyclic" constraint means no variable can be its own ancestor — there are no feedback loops, which forces you to think of the causal structure as unfolding over time. When you draw a DAG, you are not describing statistical associations; you are committing to a causal story about the world. The power is that given that story, an algorithm can tell you exactly which variables to condition on to estimate a causal effect without bias.

The three key variable types in a DAG define the logic. A **confounder** creates a non-causal path between exposure and outcome — it is a common cause of both. You need to block this path, usually by conditioning on the confounder. A **mediator** lies on the causal path from exposure to outcome (exposure → mediator → outcome). Adjusting for a mediator blocks the very effect you are trying to estimate — so you should *not* adjust for it when you want the total effect. A **collider** is a variable caused by two other variables (exposure → collider ← outcome). Colliders are the most counterintuitive: you should never condition on a collider, because doing so opens a spurious association between its causes, introducing bias where there was none. This is the "collider bias" or "selection bias" problem that has generated considerable rethinking of observational study design.

The **backdoor criterion** formalizes when adjustment is sufficient. A set of variables S satisfies the backdoor criterion if (1) no variable in S is a descendant of the exposure and (2) S blocks every "backdoor path" — every non-causal path from exposure to outcome that starts with an arrow pointing *into* the exposure (indicating a common cause). If you can find such a set S, adjusting for S gives you the causal effect. The practical implication is that you can often find *multiple* sufficient adjustment sets, and the DAG helps you choose the smallest or most easily measured one. DAGs do not tell you whether your causal assumptions are correct — that requires domain knowledge and study design — but they make those assumptions transparent and testable in principle, which is a major advance over the implicit and inconsistent practice of "just control for everything."
