---
id: counterfactual-framework
title: Counterfactual Framework and Potential Outcomes
domain: health-and-human-development
course: epidemiology
prerequisites:
- id: directed-acyclic-graphs
  type: hard
- id: epidemiology-foundations
  type: soft
builds-toward:
- sensitivity-analysis-epidemiology
tags:
- causal-inference
- potential-outcomes
- rubin-causal-model
stage: advanced
status: draft
---

# Counterfactual Framework and Potential Outcomes

## Core Idea
The counterfactual framework defines causal effects as contrasts between potential outcomes under different exposure levels, observed for the same individual in hypothetical scenarios. The fundamental problem of causal inference is that only one potential outcome is observed per person; valid causal inference requires assumptions about missing counterfactuals (e.g., consistency, positivity, exchangeability).

## Explainer

From your study of directed acyclic graphs (DAGs), you already understand that causation has a direction and that confounding arises when common causes of both exposure and outcome distort an observed association. The **counterfactual framework** takes this further: it defines what a causal effect actually *means* for a single individual. The claim "smoking caused her lung cancer" is a counterfactual claim — it asserts that if, contrary to fact, she had not smoked, she would not have developed cancer. Causation is always a comparison between what happened and what *would have happened* under a different world.

The formal notation makes this precise. Write **Y(1)** for the outcome a person would experience if exposed (treatment = 1) and **Y(0)** for the outcome they would experience if unexposed (treatment = 0). These are called **potential outcomes** — not observed outcomes, but outcomes that would be realized under each possible treatment state. The **individual causal effect** is Y(1) − Y(0): did the treatment change this person's outcome? This is the exact quantity we care about. But here is the inescapable problem: every person receives one treatment. If a patient takes the drug, we observe Y(1) and never learn Y(0). If they don't take it, we observe Y(0) and never learn Y(1). One of the two potential outcomes is always a **counterfactual** — literally counter to the observed fact. This is the **fundamental problem of causal inference**.

Because we cannot observe both potential outcomes for the same person, we cannot directly measure individual causal effects. The solution is to shift the estimand: instead of the individual effect, we target the **average treatment effect (ATE)** — E[Y(1) − Y(0)] — averaged across a population. This is estimable if the treated and untreated groups are *exchangeable*: statistically comparable in their potential outcomes, so that the untreated group's observed Y(0) can stand in for the treated group's counterfactual Y(0). Randomization achieves this mechanically; observational studies must achieve it through design and modeling.

Three key assumptions underpin valid counterfactual inference. **Consistency** requires that the potential outcome Y(a) for treatment a is precisely what you observe when treatment a is received — there is one well-defined version of each treatment level, not ambiguous variations. **Positivity** (also called the overlap assumption) requires that every subgroup defined by measured covariates has some positive probability of receiving each treatment level; if certain people *never* receive the treatment, we cannot estimate the effect for them. **Exchangeability** (no unmeasured confounding) is the most demanding: it requires that, conditional on measured covariates, treatment assignment is independent of the potential outcomes — no hidden common causes remain.

The connection to your DAG prerequisite is direct. A DAG encodes the assumed causal structure of the data-generating process. Exchangeability conditional on covariates Z translates to the DAG condition that blocking all backdoor paths from exposure to outcome is achievable by conditioning on Z. The three assumptions are not mere statistical niceties; they are substantive claims about the world that must be justified on scientific grounds. Sensitivity analysis — the topic this builds toward — is specifically the practice of asking how badly your conclusions break down if exchangeability is violated.

## How It's Best Learned
Work through simple numerical examples: two identical people who differ only in treatment received, calculate what the ATE would be if you could observe both potential outcomes, then see how the naive observational comparison can diverge. This makes the fundamental problem concrete and the need for assumptions intuitive.
