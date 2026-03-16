---
id: causal-inference-in-epidemiology
title: Causal Inference in Epidemiology
domain: health-and-human-development
course: public-health
prerequisites:
- id: epidemiology-foundations
  type: hard
- id: confounding-epidemiology
  type: hard
builds-toward:
- mediation-analysis-epidemiology
- instrumental-variables-epidemiology
tags:
- causal-inference
- confounding
- dags
- bias-adjustment
- identification
stage: abstract-reasoning
status: draft
---

# Causal Inference in Epidemiology

## Core Idea
Causal inference in epidemiology moves beyond identifying associations to establishing causal relationships using directed acyclic graphs (DAGs), confounding adjustment, and identification strategies. Hill's criteria provide a framework for evaluating causality from observational data when randomized experiments are infeasible or unethical. Understanding counterfactual thinking and potential outcomes frameworks is essential for valid causal conclusions.

## How It's Best Learned
Work through real epidemiologic studies to identify confounders, draw DAGs, and interpret adjusted versus unadjusted analyses. Practice using sensitivity analysis to test robustness of causal conclusions to residual confounding.

## Common Misconceptions
Assuming all confounding is eliminated through statistical adjustment. Believing correlation proves causation just because confounding is ruled out. Confusing confounding with effect modification.

## Explainer

From your study of epidemiology foundations and confounding, you already understand that an observed association between an exposure and outcome may be distorted by third variables — confounders that are related to both. Causal inference takes the next step: given that you have measured an association and controlled for confounders, how do you decide whether the relationship is actually causal? This question cannot be answered by statistical analysis alone. It requires a conceptual framework for what causation means and what evidence pattern would distinguish a genuine cause from a spurious or confounded relationship.

The **counterfactual framework** provides the clearest definition of causation in epidemiology. A cause is something whose presence changes an outcome relative to what would have happened in its absence — the counterfactual. "Would this person have developed disease if they had not been exposed?" is the causal question. In a randomized trial, random assignment ensures the exposed and unexposed groups are comparable on all other factors, so the counterfactual can be approximated by comparing outcomes across arms. In observational data, we can never directly observe both states (exposed and unexposed) for the same person at the same time — we must construct a comparison group that resembles the counterfactual. This is precisely why confounding and selection bias are so pernicious: they corrupt the comparison group, making it non-representative of what would have happened under the counterfactual condition.

**Directed acyclic graphs (DAGs)** are the primary tool for reasoning clearly about confounding, mediation, and selection bias. A DAG represents variables as nodes and causal relationships as directed arrows — you draw what you believe about the causal structure, then use graph rules to identify which variables must be adjusted for to block non-causal paths. The key insight is that not all associated variables should be adjusted: adjusting for a **mediator** (a variable on the causal pathway from exposure to outcome) removes part of the causal effect you are trying to measure, and adjusting for a **collider** (a variable with arrows from both exposure and outcome pointing into it) can *introduce* spurious associations that did not previously exist. DAGs make these pitfalls explicit by allowing you to trace paths between variables and apply the **backdoor criterion** to identify valid adjustment sets.

**Hill's criteria** — proposed by Austin Bradford Hill in 1965 and still used to evaluate causal claims from observational data — list nine features that strengthen a causal inference: strength of association, consistency across studies, specificity, temporality (cause precedes effect), biological gradient (dose-response), plausibility, coherence with existing knowledge, experimental evidence where available, and analogy. Temporality is the only criterion that is logically necessary — a cause cannot follow its effect — but the others increase or decrease confidence in causal interpretation. Applying them rigorously reveals why even a large, consistent, biologically plausible association (like early evidence linking smoking to lung cancer) required sustained accumulation across multiple lines of evidence before the causal claim was accepted. Causal inference is ultimately a judgment about the totality of evidence, not a single statistical threshold — and learning to make that judgment explicitly, rather than collapsing it into a p-value, is what distinguishes epidemiologic thinking from mere pattern detection.
