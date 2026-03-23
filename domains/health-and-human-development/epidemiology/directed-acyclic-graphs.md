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
stage: expert
status: draft
---

# Directed Acyclic Graphs for Causal Modeling

## Core Idea
A directed acyclic graph (DAG) is a visual representation of causal assumptions about the relationships among variables. DAGs help identify minimal sufficient sets of confounders to adjust for to block backdoor paths (non-causal paths from exposure to outcome). DAGs clarify whether a variable is a confounder, mediator, or collider, preventing unnecessary or harmful adjustment.

## Questions

```yaml
- question: "A study examines whether a drug (D) causes recovery (R). Both D and R independently increase the likelihood of hospitalization (H): D → H ← R. A researcher adjusts for H to control for 'health severity.' What is the consequence?"
  type: multiple-choice
  options:
    - "This correctly removes confounding by health severity, improving the estimate"
    - "This introduces a spurious association between D and R by conditioning on a collider"
    - "This blocks a mediating pathway, causing underestimation of the drug's total effect"
    - "This has no effect because H is downstream of both D and R"
  answer: 1
  explanation: "H is a collider — arrows point INTO it from both D and R. Colliders do not create open paths between their causes by default. But conditioning on H opens a spurious non-causal path between D and R, introducing bias that wasn't there before. Among hospitalized patients, the absence of the drug becomes evidence for the disease (since something must explain the hospitalization), creating an artificial negative association. Adjusting for a collider makes the estimate worse, not better — this is the counterintuitive core of collider bias."

- question: "A researcher wants to estimate the total effect of exercise (E) on cardiovascular disease (CVD), where part of the effect runs through reduced blood pressure: E → BP → CVD. She includes blood pressure (BP) in her regression. What does her model estimate?"
  type: multiple-choice
  options:
    - "The total causal effect of exercise on CVD"
    - "The direct effect of exercise on CVD not mediated through blood pressure"
    - "The effect of blood pressure on CVD, controlling for exercise"
    - "An unbiased total effect estimate with reduced variance from the extra covariate"
  answer: 1
  explanation: "BP is a mediator on the causal path E → BP → CVD. Adjusting for a mediator blocks the indirect pathway, so the model captures only the direct effect of E on CVD via routes that do not go through BP. To estimate the total effect of exercise, BP should NOT be adjusted for. This is one of the most common mistakes in observational epidemiology: including every 'relevant' variable without asking whether a variable is a mediator, confounder, or collider in the DAG."

- question: "In a DAG analysis, adjusting for more variables always provides a better causal estimate because each additional covariate removes another source of potential confounding."
  type: true-false
  answer: false
  explanation: "This is the central error DAGs are designed to prevent. Adjusting for a collider opens a spurious non-causal path, introducing bias. Adjusting for a mediator blocks the causal path you want to estimate. The correct adjustment set depends on the causal structure — the DAG — not on maximizing the number of covariates. 'Adjust for everything' is not a valid causal inference strategy; it can actively worsen estimates."

- question: "The backdoor criterion identifies adjustment sets that block all non-causal paths from exposure to outcome while leaving causal paths intact."
  type: true-false
  answer: true
  explanation: "The backdoor criterion requires: (1) no variable in the adjustment set is a descendant of the exposure, and (2) the set blocks every backdoor path — every non-causal path entering the exposure node from behind (indicating a common cause). When a set satisfies these criteria, adjusting for it gives the causal effect without blocking causal paths or opening collider paths. Multiple valid adjustment sets may exist for the same DAG, and the DAG helps you choose the most practical one."

- question: "What makes a collider different from a confounder in a DAG, and why does conditioning on a collider cause bias rather than remove it?"
  type: short-answer
  answer: "A confounder has arrows pointing OUT to both exposure and outcome (a common cause), creating an open non-causal path that conditioning blocks. A collider has arrows pointing IN from both exposure and outcome (or their ancestors) — a common effect. No path passes through a collider by default; the path is already closed. Conditioning on a collider opens this previously closed path, creating a spurious association between its causes. The intuition: among patients selected by being hospitalized (a collider of disease and drug exposure), knowing a patient wasn't given the drug makes the disease more likely — producing a spurious drug-disease correlation that doesn't exist in the full population."
  explanation: "Collider bias is the hardest DAG concept for students to internalize because conditioning normally removes associations rather than creating them. The key is that for confounders the path is open and conditioning closes it; for colliders the path is closed and conditioning opens it — exactly the opposite."
```

## Explainer

You already understand confounding intuitively: a third variable that is associated with both the exposure and the outcome can make a non-causal association look causal (or vice versa). The trouble is that deciding what to adjust for in a study — which variables to include in a regression, which to stratify on — has historically been treated as an art guided by subject-matter intuition. **Directed acyclic graphs (DAGs)** make the causal assumptions explicit and then let formal rules determine the correct adjustment strategy.

A DAG is a graph where nodes represent variables and directed arrows (edges) represent direct causal effects. The "acyclic" constraint means no variable can be its own ancestor — there are no feedback loops, which forces you to think of the causal structure as unfolding over time. When you draw a DAG, you are not describing statistical associations; you are committing to a causal story about the world. The power is that given that story, an algorithm can tell you exactly which variables to condition on to estimate a causal effect without bias.

The three key variable types in a DAG define the logic. A **confounder** creates a non-causal path between exposure and outcome — it is a common cause of both. You need to block this path, usually by conditioning on the confounder. A **mediator** lies on the causal path from exposure to outcome (exposure → mediator → outcome). Adjusting for a mediator blocks the very effect you are trying to estimate — so you should *not* adjust for it when you want the total effect. A **collider** is a variable caused by two other variables (exposure → collider ← outcome). Colliders are the most counterintuitive: you should never condition on a collider, because doing so opens a spurious association between its causes, introducing bias where there was none. This is the "collider bias" or "selection bias" problem that has generated considerable rethinking of observational study design.

The **backdoor criterion** formalizes when adjustment is sufficient. A set of variables S satisfies the backdoor criterion if (1) no variable in S is a descendant of the exposure and (2) S blocks every "backdoor path" — every non-causal path from exposure to outcome that starts with an arrow pointing *into* the exposure (indicating a common cause). If you can find such a set S, adjusting for S gives you the causal effect. The practical implication is that you can often find *multiple* sufficient adjustment sets, and the DAG helps you choose the smallest or most easily measured one. DAGs do not tell you whether your causal assumptions are correct — that requires domain knowledge and study design — but they make those assumptions transparent and testable in principle, which is a major advance over the implicit and inconsistent practice of "just control for everything."
