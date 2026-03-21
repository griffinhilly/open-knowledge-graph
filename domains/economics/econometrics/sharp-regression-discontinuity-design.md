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

## Questions

```yaml
- question: "A researcher uses sharp RDD to study a job training program assigned to workers who score below 50 on a skills test. She finds a significant positive jump in earnings at the cutoff. Her colleague claims this proves the training is effective for all low-skilled workers. What is wrong with this conclusion?"
  type: multiple-choice
  options:
    - "Nothing — RDD identifies the average treatment effect across the full sample"
    - "The estimate only applies to workers right at the threshold score of 50, not to all low-skilled workers; extrapolating to the full population is not supported by the design"
    - "The conclusion is wrong because RDD requires a regression, and regressions cannot prove causality"
    - "The finding is invalid unless the skills test has a normal distribution"
  answer: 1
  explanation: "Sharp RDD identifies a Local Average Treatment Effect (LATE) — the causal effect for individuals right at the cutoff. Workers scoring 20 or 80 may respond to the training very differently from those at 50. The design's credibility comes from local randomization near the threshold, but that local randomization only supports local inference. This is a fundamental limitation of RDD: it is highly credible for the threshold population but silent about treatment effects elsewhere in the running variable distribution."

- question: "In a sharp RDD evaluation of a scholarship program (cutoff: exam score 75), what is the purpose of the McCrary density test?"
  type: multiple-choice
  options:
    - "To verify that the outcome variable (e.g., graduation rates) is continuously distributed near the cutoff"
    - "To detect whether students are manipulating their exam scores to land just above 75, which would invalidate the local randomization assumption"
    - "To select the optimal bandwidth for the local linear regression"
    - "To test whether the scholarship causes a discontinuous jump in earnings"
  answer: 1
  explanation: "The McCrary density test checks for a suspicious spike in the density of the running variable just above the cutoff. If students can manipulate their scores to land just above 75 (by re-taking the exam, getting extra tutoring, or having grades rounded up), then students just above 75 are systematically different from those just below — the local randomization argument fails. Students who successfully manipulate their score are likely higher-ability, more motivated, or better-resourced, creating selection bias. An RDD where manipulation is present cannot be trusted even if a discontinuity in outcomes is observed."

- question: "Sharp RDD identifies the average treatment effect for the entire population of treated individuals."
  type: true-false
  answer: false
  explanation: "Sharp RDD identifies a Local Average Treatment Effect (LATE) — the causal effect specifically for units right at the threshold, where the local randomization argument is valid. Units far from the cutoff are not comparable across the treatment boundary; their assignment is not quasi-random. This is why 'sharp' (deterministic assignment) RDD is highly credible for the threshold population but provides no direct evidence about treatment effects for the broader population. Extrapolating beyond the local neighborhood requires untestable assumptions about effect homogeneity."

- question: "If observable pre-determined covariates (age, gender, baseline test scores) show a discontinuous jump at the RDD cutoff, this is evidence that the identification assumption may be violated."
  type: true-false
  answer: true
  explanation: "This placebo test is one of the most important validity checks in RDD. The identifying assumption is that potential outcomes — and everything that determines them — vary smoothly through the cutoff. Pre-determined covariates that couldn't have been affected by treatment should show no discontinuity. If they jump at the cutoff, it suggests that units just above and just below are systematically different in ways beyond treatment assignment — exactly the selection problem RDD is supposed to eliminate. If observable characteristics show a jump, unobservable ones likely do too."

- question: "Why does sharp RDD only estimate a local average treatment effect at the cutoff, rather than the average treatment effect for the full population? Why does this limitation matter?"
  type: short-answer
  answer: "Sharp RDD's identification relies on the continuity of potential outcomes at the cutoff — in the absence of treatment, the outcome would vary smoothly through the threshold. This assumption is plausible only locally: units right at the cutoff are near-identical in observable and unobservable characteristics, making assignment essentially random. Units far from the cutoff differ systematically (a student scoring 60 is genuinely different from one scoring 90), so comparing their outcomes would confound treatment with pre-existing differences. The limitation matters because the threshold population may not be representative — a job training program might work well for workers right at the skill cutoff but have no effect for workers far below or far above it."
  explanation: "The LATE limitation is inherent to the design's strength: its credibility comes from local quasi-randomization, and that local randomization only permits local inference. This is the fundamental tension in causal identification — more credible designs often purchase their credibility by narrowing the scope of valid inference. RDD is among the most credible observational designs precisely because it doesn't extrapolate; the researcher who correctly respects this limitation is doing good science."
```

## Explainer

From your study of regression discontinuity and causal inference, you know the central problem of causal estimation: the treated and control groups differ systematically, so comparing outcomes directly confounds the treatment effect with selection differences. Sharp RDD is one of the most compelling designs for circumventing this problem, and its logic is elegant: find a threshold where assignment to treatment flips from 0 to 1 in a discontinuous jump, and use the continuity of everything else to identify the causal effect right at that threshold.

The canonical example is a scholarship program: students who score at or above a threshold exam score receive the scholarship; those just below do not. The key identifying assumption is that students cannot precisely control their score to land just above the cutoff — near the threshold, the treatment assignment is essentially as good as random. A student who scores 74.8 and misses the cutoff is nearly identical in all background characteristics to a student who scores 75.2 and receives the scholarship. Any discontinuous jump in outcomes (graduation rates, earnings) at exactly the cutoff is therefore attributable to the scholarship itself, not to pre-existing differences between recipients and non-recipients.

The **running variable** (also called the forcing variable or assignment variable) is the continuous measure that determines treatment. The **cutoff** is the threshold c* where assignment jumps. The critical identifying assumption is **continuity of potential outcomes**: in the absence of treatment, the expected outcome would be a smooth function of the running variable at the cutoff. This means any sharp jump in the observed outcome must be caused by the treatment. Formally, the estimand is a **Local Average Treatment Effect (LATE)**: the effect of treatment on individuals right at the threshold, not the average effect in the full population.

Estimation proceeds by fitting regression models on either side of the cutoff and measuring the discontinuous gap at c*. The practical challenge is **bandwidth selection**: observations far from the cutoff use different regions of the running variable distribution and are less comparable. Narrower bandwidths improve comparability at the cost of smaller samples. Modern practice uses **local linear regression** (fitting linear regressions in a narrow window around the cutoff) with data-driven bandwidth selection methods like the Imbens-Kalyanaraman or CCT bandwidth selectors. Global polynomial fitting is generally discouraged because high-degree polynomials produce unstable estimates near the edges of the sample.

**Validity checks** are essential in any RDD application. The most important is a **density test** (McCrary test): if individuals can manipulate the running variable to land just above the cutoff, you will see a suspicious spike in the density of the running variable just above c*. If manipulation is present, the local-randomization argument fails. A second check is **placebo tests**: verify that pre-determined covariates (age, gender, baseline characteristics) show no discontinuity at the cutoff. If observable covariates jump discontinuously, unobservable ones likely do too, undermining the identification assumption. When these checks pass, sharp RDD delivers among the most credible causal estimates available from observational data.
