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
stage: expert
status: validated
---

# Causal Inference from Observational Data: Fundamental Problem

## Core Idea
The fundamental problem of causal inference is observing only one potential outcome per unit. Causal claims require assumptions: no unmeasured confounding, common support, consistency. This section reviews the potential outcomes framework and assumptions needed for causal identification from observational data.

## Questions

```yaml
- question: "A study finds that students who attended a tutoring program scored 10 points higher on average than students who did not. What is the primary reason this cannot be interpreted as the causal effect of tutoring?"
  type: multiple-choice
  options:
    - "The sample size is too small to draw reliable conclusions"
    - "Students who sought tutoring may have been more motivated to begin with, confounding the comparison"
    - "The 10-point difference is too small to be practically significant"
    - "The study should have used a different outcome measure than test scores"
  answer: 1
  explanation: "The fundamental problem is confounding: students who seek out tutoring likely differ systematically from those who do not — in motivation, parental support, prior academic history, and other factors that also affect outcomes. The observed difference conflates the tutoring effect with these pre-existing differences. This is why the naive comparison is invalid: the untreated students are not a credible counterfactual for what the treated students' outcomes would have been without treatment. Options A, C, and D are concerns about study design and interpretation, but they do not capture the core identification problem."

- question: "Which statement best describes the 'fundamental problem of causal inference'?"
  type: multiple-choice
  options:
    - "Researchers can never collect enough data to estimate causal effects with precision"
    - "Selection bias always invalidates observational studies, making experiments the only valid approach"
    - "For any given unit at any given time, only one potential outcome — treated or untreated — can ever be observed"
    - "Causal effects can only be estimated when all confounders have been measured and adjusted for"
  answer: 2
  explanation: "The fundamental problem is a logical impossibility, not a data problem: the same unit cannot be observed simultaneously in two treatment conditions. The counterfactual — what would have happened under the other condition — is inherently unobservable. This means individual-level causal effects (Y_i(1) − Y_i(0)) are never directly measurable. All methods of causal inference (experiments, natural experiments, IV, RD, matching) are strategies for constructing credible counterfactuals under assumptions, not for circumventing this constraint. Option D describes one important assumption (ignorability) but is not the definition of the fundamental problem."

- question: "Randomized experiments solve the fundamental problem of causal inference by making treatment assignment statistically independent of potential outcomes."
  type: true-false
  answer: true
  explanation: "Random assignment ensures that, in expectation, the treated and untreated groups have the same distribution of potential outcomes — including unmeasured ones. This is what makes the untreated group a valid counterfactual for the treated group: any pre-existing differences are eliminated by randomization (in expectation). This is the key advantage of experiments over observational studies: they satisfy the ignorability assumption by design rather than relying on it as an untestable claim."

- question: "If researchers carefully measure and control for all relevant background characteristics in an observational study, they can always achieve valid causal identification."
  type: true-false
  answer: false
  explanation: "No amount of covariate adjustment can guarantee causal identification if unmeasured confounders remain. The ignorability assumption — that conditional on observed covariates, treatment is as-if random — is fundamentally untestable: by definition, you cannot check whether unmeasured variables are confounders. A well-measured study can reduce confounding, but it cannot eliminate the logical possibility that some unmeasured variable jointly predicts treatment receipt and outcomes. This is precisely why identification strategies like natural experiments, IV, and regression discontinuity are needed — they seek variation in treatment that is plausibly unrelated to potential outcomes by some external mechanism."

- question: "Why is the fundamental problem of causal inference described as a logical constraint rather than a technical limitation that better methods or bigger data can overcome?"
  type: short-answer
  answer: "Because the problem is not about measurement precision or sample size — it is about the impossibility of observing the same unit in two states simultaneously. No matter how much data you collect, you can only ever see one factual outcome per unit per moment in time. The counterfactual — what would have happened under the other treatment — is not just unmeasured but unmeasurable in principle. Causal inference methods address this by constructing credible comparison groups under assumptions, but those assumptions are always untestable to some degree. Bigger samples narrow confidence intervals but cannot conjure the missing counterfactual."
  explanation: "This is the core epistemological foundation of the potential outcomes framework. Understanding that the constraint is logical (not technical) explains why causal inference requires substantive assumptions — about ignorability, common support, consistency — that go beyond statistics alone. Methods like randomization, natural experiments, and instrumental variables are valued precisely because they make those assumptions more credible, not because they eliminate the fundamental problem."
```

## Explainer

The fundamental problem of causal inference arises from a simple impossibility: you cannot observe the same unit in two states simultaneously. To know whether a policy caused an outcome, you would need to see the same person both treated and untreated at the same moment — which is physically impossible. What you observe is called the **factual outcome**; what would have happened under the counterfactual condition is the **potential outcome**. The causal effect for any individual is the difference between these two potential outcomes, but since only one is ever observed, individual-level causal effects are inherently unidentifiable without further assumptions. This is the fundamental problem — not a technical limitation to be engineered around, but a logical constraint on all causal inference.

The **potential outcomes framework** (associated with Rubin) formalizes this logic. Each unit *i* has two potential outcomes: *Y_i(1)* if treated, *Y_i(0)* if not. The treatment effect for unit *i* is *Y_i(1) − Y_i(0)*. Researchers typically estimate the **Average Treatment Effect (ATE)** — the mean of individual effects across the population — or the **Average Treatment Effect on the Treated (ATT)**. But to estimate either, you need a comparison group whose untreated outcomes represent what the treated group's outcomes *would have been* absent treatment. In a randomized experiment, random assignment ensures this by making treatment statistically independent of potential outcomes. In observational data, no such guarantee exists — and the entire project of observational causal inference is constructing credible comparisons in its absence.

The three identification assumptions for causal inference from observational data are: **ignorability** (also called unconfoundedness or no unmeasured confounding), **common support** (or overlap), and **consistency** (or SUTVA). Ignorability means that, conditional on observed covariates, treatment assignment is as-if random — there are no unmeasured variables that jointly predict treatment and outcome. Common support means that every unit has a nonzero probability of receiving each treatment level: you cannot extrapolate causal effects to covariate regions with no counterfactual comparisons. Consistency means that the potential outcome under a given treatment level is well-defined and the same regardless of *how* treatment was received — an assumption violated when treatment is heterogeneous in ways that matter.

Violations of these assumptions are the central concern of observational causal inference. **Unmeasured confounders** — variables that predict both who receives treatment and what outcomes they achieve — bias naive estimates. The classic example: students who attend tutoring programs tend to be more motivated, so the "tutoring effect" estimated by comparing tutored versus untutored students conflates the program's effect with pre-existing motivation differences. Your prior work on conditional probability gives you the formal language: a confounder is a variable *C* such that treatment *T* and outcome *Y* are not independent, but become independent once you condition on *C*. Multilevel models (your hard prerequisite) highlight why this is especially difficult in nested data: individual-level unobservables may correlate at the group level, creating confounding that simple covariate adjustment cannot resolve. The downstream strategies — natural experiments, instrumental variables, regression discontinuity — are all attempts to recover credible causal identification when ignorability cannot be assumed to hold on observables alone.
