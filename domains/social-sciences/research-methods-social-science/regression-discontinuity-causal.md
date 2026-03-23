---
id: regression-discontinuity-causal
title: Regression Discontinuity Design
domain: social-sciences
course: research-methods-social-science
prerequisites:
- id: causal-inference-observational-data
  type: hard
- id: linear-regression-social-science
  type: hard
- id: limit-definition-intuitive
  type: soft
- id: linear-regression
  type: hard
- id: limits-continuity-multivariable
  type: soft
tags:
- regression-discontinuity
- threshold-assignment
- local-polynomial
- fuzzy-RD
stage: expert
status: draft
---

# Regression Discontinuity Design

## Core Idea
Applies regression discontinuity methods when assignment to treatment depends on a continuous running variable crossing a threshold. Covers sharp and fuzzy RD designs, local polynomial estimation, bandwidth selection, and internal validity advantages of RD for causal inference.

## How It's Best Learned
Identify RD applications in real policies (test cutoffs, age eligibility), estimate sharp and fuzzy RD models, create RD plots, conduct falsification tests with placebo cutoffs.

## Common Misconceptions
- RD requires very narrow bandwidths around the cutoff
- Fuzzy RD is always weaker than sharp RD
- RD can only use polynomial functional forms

## Questions

```yaml
- question: "A researcher wants to estimate the effect of receiving a merit scholarship on graduation rates. Scholarships are awarded to students who score 70 or above on an entrance exam. She compares graduation rates of students scoring 65–69 vs. 71–75. What is the core identifying assumption that makes this a valid causal estimate?"
  type: multiple-choice
  options:
    - "Students near the cutoff are a representative sample of the full student population"
    - "In the absence of the scholarship, graduation rates would follow a continuous smooth trend as a function of exam score — any jump at 70 reflects the treatment effect"
    - "Students just above and below the cutoff have identical observable characteristics — no confounding is possible near the threshold"
    - "The sample size near the cutoff is large enough to detect a statistically significant effect"
  answer: 1
  explanation: "The identifying assumption in RD is continuity: potential outcomes would be a smooth, continuous function of the running variable at the cutoff in the absence of treatment. Any discrete jump in outcomes at the threshold is then attributable to the treatment. Option C is close but subtly wrong — students near the cutoff are expected to be similar, but 'identical observable characteristics' is too strong and misses the key point. What matters is that there are no other factors that also jump discontinuously at exactly this threshold. The continuity assumption is what allows the smooth trend to serve as a counterfactual."

- question: "A researcher finds that many students report exam scores of exactly 70 on the scholarship entrance exam, with suspiciously few students at 68 and 69. What does this pattern suggest, and why does it threaten the RD design?"
  type: multiple-choice
  options:
    - "The sample is too small near the cutoff — the researcher should use a wider bandwidth to include more observations"
    - "Bunching just above the cutoff suggests score manipulation, violating the continuity assumption by making the groups near the threshold non-comparable"
    - "This is a fuzzy RD situation because not all students with 70+ received the scholarship"
    - "The running variable has measurement error, which is normal and handled by local polynomial estimation"
  answer: 1
  explanation: "Bunching in the running variable distribution just above the cutoff is a classic sign that subjects or administrators are manipulating scores to just exceed the threshold. If students who would otherwise score 68 or 69 are somehow getting their scores adjusted to 70, then the group just above the cutoff is no longer comparable to those just below — they have systematically different characteristics (motivation, connections, resources to obtain score adjustments). This violates the continuity assumption, which requires that who ends up just above vs. just below the cutoff is essentially random near the threshold. Density tests (McCrary test) are a standard falsification check for this."

- question: "RD provides only a local estimate of the treatment effect — specifically, the effect for units near the cutoff — rather than an average treatment effect for the full population."
  type: true-false
  answer: true
  explanation: "This is a genuine limitation of RD that researchers must state clearly. The causal identification in RD relies on the near-randomness of treatment assignment very close to the threshold. The estimated effect is a local average treatment effect (LATE) for units near the cutoff, who may differ systematically from units far from the cutoff. For example, the effect of a scholarship on graduation for students who barely qualified (scores just above 70) may differ substantially from the effect for high-achieving students (scores of 90+). External validity requires careful argument that the local estimate generalizes."

- question: "A fuzzy RD design is invalid because the running variable does not perfectly determine treatment — some people above the cutoff don't take up the treatment, making the design non-experimental."
  type: true-false
  answer: false
  explanation: "Fuzzy RD is a valid research design — it simply combines RD intuition with instrumental variables logic. When the cutoff affects the *probability* of treatment rather than determining it perfectly, the cutoff becomes an instrument for actual treatment receipt. The resulting estimate is still causally identified (as a LATE for compliers near the threshold) as long as the cutoff creates a sharp enough discontinuity in treatment probability and the exclusion restriction holds (the cutoff affects outcomes only through its effect on treatment). Many real policy cutoffs are fuzzy — eligibility doesn't guarantee takeup — and fuzzy RD is the appropriate tool."

- question: "What is the identifying assumption in regression discontinuity design, and why does manipulation of the running variable violate it?"
  type: short-answer
  answer: "The identifying assumption is continuity: in the absence of treatment, potential outcomes would be a smooth function of the running variable at the cutoff. Any jump at the threshold is then attributed to the treatment. Manipulation of the running variable (e.g., students or officials adjusting scores to just exceed the cutoff) violates this because the groups just above and below the threshold are no longer comparable — those who manipulated their way above the cutoff are systematically different from those who couldn't, in ways that affect the outcome independently of treatment."
  explanation: "The continuity assumption works because near-threshold observations are essentially comparable — assignment to just above vs. just below is close to random due to measurement noise. Manipulation breaks this near-randomness: if motivated, well-connected, or resourceful individuals can get just above the threshold while others can't, then the above-threshold group is positively selected on traits correlated with outcomes. The treatment effect estimate would then conflate the true effect with the selection difference. Falsification tests for bunching (the McCrary density test) are a standard check for this threat."
```

## Explainer

You know from your causal inference prerequisites that the central challenge in observational data is confounding: people who receive a treatment are systematically different from those who don't, and those differences — not the treatment itself — may explain the outcome differences we observe. Regression discontinuity design (RDD) exploits a simple but powerful idea: if assignment to treatment is determined by whether a continuous variable crosses a threshold, then people just below the cutoff and just above it are nearly identical in all respects except treatment status. The threshold creates a local natural experiment.

The classic example makes the logic vivid. Students who score just above an admissions cutoff gain entry to a selective school; those who score just below do not. Among students very near the cutoff, admission is essentially random — a few points' difference on a test on one day, attributable to noise rather than meaningful ability differences. By comparing outcomes for students just above versus just below the cutoff, you obtain a clean estimate of the effect of selective school admission, free of the selection bias that would contaminate a comparison of all admitted versus non-admitted students. This is the **sharp RD design**: treatment status jumps discontinuously from 0 to 1 at the **cutoff** (also called the threshold), and the **running variable** (test score, age, income, geographic distance) determines that jump precisely.

Your prerequisites on limits and continuity clarify the identifying assumption: in the absence of treatment, potential outcomes would be a *continuous* function of the running variable at the cutoff. The causal estimate is the discontinuous jump in outcomes at the threshold — whatever can't be explained by the smooth trend in the running variable must be the treatment effect. Visually, you plot the outcome against the running variable on both sides of the cutoff. A smooth curve with a sudden jump at the threshold is the signature of a causal effect. **Local polynomial regression** estimates those smooth trends flexibly on each side, avoiding the distortions introduced by high-degree global polynomials. **Bandwidth selection** involves a bias-variance tradeoff: a narrow bandwidth around the cutoff gives you observations most similar to each other (internal validity) but fewer observations (larger standard errors). Optimal bandwidth selection algorithms balance these concerns formally.

The **fuzzy RD design** applies when the cutoff affects the probability of treatment rather than determining it deterministically — some above the cutoff don't take up the treatment, some below obtain it through other means. Here the discontinuity is in the *probability* of treatment, and you use the cutoff as an instrument for actual treatment receipt, combining RD intuition with instrumental variables logic. The resulting estimate is a local average treatment effect (LATE) for compliers near the threshold. **Falsification tests** are essential for validating any RD design: test whether predetermined covariates (baseline characteristics measured before treatment) show no discontinuity at the real cutoff; test for discontinuities at placebo cutoffs where no effect should exist; check for bunching in the running variable distribution just above the cutoff, which would indicate manipulation of the assignment rule.
