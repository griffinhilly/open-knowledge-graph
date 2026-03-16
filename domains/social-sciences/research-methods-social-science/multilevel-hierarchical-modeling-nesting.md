---
id: multilevel-hierarchical-modeling-nesting
title: 'Multilevel Modeling: Data Nested in Structure'
domain: social-sciences
course: research-methods-social-science
prerequisites:
- id: multilevel-modeling-hierarchical
  type: hard
- id: regression-diagnostics-assumption-violations
  type: soft
- id: normal-distribution-theory
  type: hard
- id: probability-distributions
  type: hard
- id: conditional-distributions-of-random-variables
  type: soft
builds-toward:
- causal-inference-from-observation
tags:
- multilevel
- hierarchical
- nested-data
- random-effects
stage: advanced
status: draft
---

# Multilevel Modeling: Data Nested in Structure

## Core Idea
Social data are often nested: individuals within classrooms, employees within firms, observations within time periods. Ignoring nesting violates independence assumptions and biases standard errors. Multilevel models explicitly model variation at each level, allowing research on both within-group and between-group processes.

## Explainer

You've already learned regression and its assumption of independent errors — that knowing one observation's residual tells you nothing about another's. This assumption is routinely violated in social research. Students in the same classroom share a teacher, a physical environment, and a peer culture. Employees in the same firm share a management style and corporate culture. Observations on the same country across years share unmeasured country characteristics. When data have this nested structure, residuals within groups correlate — two students in the same classroom are more similar to each other than to two students in different classrooms. Standard regression treats this as noise when it is actually signal.

The core problem has two faces. First, if you ignore clustering, your standard errors are too small. Observations within a cluster are not independent pieces of evidence — ten students from the same classroom give you less information than ten students from ten different classrooms. OLS doesn't know this and treats them as fully independent, producing overconfident estimates and too-small p-values. Second, ignoring clustering means you cannot ask the theoretically interesting cross-level questions: does class size (a Level-2 characteristic) moderate the effect of individual tutoring (a Level-1 effect)? These **cross-level interactions** are central to sociological and educational research, and they are invisible to single-level models.

**Multilevel models** — also called hierarchical linear models or mixed-effects models — solve this by explicitly modeling variation at each level. The model has a separate equation for each level. At Level 1, you model individual outcomes as a function of individual predictors, but allow the intercept (and possibly slopes) to vary across groups. At Level 2, you model that variation as a function of group-level predictors. The Level-2 equation is literally a model of the Level-1 parameters. For example: student test scores are predicted by hours of study (Level 1), but the *intercept* of that relationship (baseline performance) varies across classrooms depending on teacher experience (Level 2). The **random effects** are the Level-2 variances — how much groups differ from the grand mean in ways not explained by your Level-2 predictors.

A critical conceptual distinction is between **fixed effects** (the average relationship across all groups) and **random effects** (group-specific deviations from that average). When you have the full population of groups (all 50 US states, all divisions of your company), you use fixed effects — you're estimating each group's specific value. When your groups are a sample from a larger population (50 schools sampled from thousands), you use random effects — you're estimating the *variance* of the group distribution, not each group's precise value. This distinction connects to your knowledge of probability distributions: random effects are modeled as draws from a normal distribution with mean zero and variance that the model estimates. The model borrows strength across groups — **partial pooling** — producing estimates that are more stable than group-by-group analysis while more accurate than treating all groups as identical.
