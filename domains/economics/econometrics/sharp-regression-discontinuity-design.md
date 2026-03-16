---
id: sharp-regression-discontinuity-design
title: Sharp Regression Discontinuity Design
domain: economics
course: econometrics
prerequisites:
- id: regression-discontinuity
  type: hard
- id: causal-inference-econometrics
  type: hard
builds-toward:
- fuzzy-regression-discontinuity-design
tags:
- causal-inference
- regression-discontinuity
- local-treatment
stage: formal-systems
status: draft
---

# Sharp Regression Discontinuity Design

## Core Idea
In sharp RDD, treatment is a deterministic function of a running variable cᵢ, with discontinuous assignment at threshold c*. The causal effect is the discontinuity in E[Y|cᵢ] at c*. Nonparametric local regression near the cutoff or global polynomial fitting identifies this effect under continuity of potential outcomes.

## Explainer

From your study of regression discontinuity and causal inference, you know the central problem of causal estimation: the treated and control groups differ systematically, so comparing outcomes directly confounds the treatment effect with selection differences. Sharp RDD is one of the most compelling designs for circumventing this problem, and its logic is elegant: find a threshold where assignment to treatment flips from 0 to 1 in a discontinuous jump, and use the continuity of everything else to identify the causal effect right at that threshold.

The canonical example is a scholarship program: students who score at or above a threshold exam score receive the scholarship; those just below do not. The key identifying assumption is that students cannot precisely control their score to land just above the cutoff — near the threshold, the treatment assignment is essentially as good as random. A student who scores 74.8 and misses the cutoff is nearly identical in all background characteristics to a student who scores 75.2 and receives the scholarship. Any discontinuous jump in outcomes (graduation rates, earnings) at exactly the cutoff is therefore attributable to the scholarship itself, not to pre-existing differences between recipients and non-recipients.

The **running variable** (also called the forcing variable or assignment variable) is the continuous measure that determines treatment. The **cutoff** is the threshold c* where assignment jumps. The critical identifying assumption is **continuity of potential outcomes**: in the absence of treatment, the expected outcome would be a smooth function of the running variable at the cutoff. This means any sharp jump in the observed outcome must be caused by the treatment. Formally, the estimand is a **Local Average Treatment Effect (LATE)**: the effect of treatment on individuals right at the threshold, not the average effect in the full population.

Estimation proceeds by fitting regression models on either side of the cutoff and measuring the discontinuous gap at c*. The practical challenge is **bandwidth selection**: observations far from the cutoff use different regions of the running variable distribution and are less comparable. Narrower bandwidths improve comparability at the cost of smaller samples. Modern practice uses **local linear regression** (fitting linear regressions in a narrow window around the cutoff) with data-driven bandwidth selection methods like the Imbens-Kalyanaraman or CCT bandwidth selectors. Global polynomial fitting is generally discouraged because high-degree polynomials produce unstable estimates near the edges of the sample.

**Validity checks** are essential in any RDD application. The most important is a **density test** (McCrary test): if individuals can manipulate the running variable to land just above the cutoff, you will see a suspicious spike in the density of the running variable just above c*. If manipulation is present, the local-randomization argument fails. A second check is **placebo tests**: verify that pre-determined covariates (age, gender, baseline characteristics) show no discontinuity at the cutoff. If observable covariates jump discontinuously, unobservable ones likely do too, undermining the identification assumption. When these checks pass, sharp RDD delivers among the most credible causal estimates available from observational data.
