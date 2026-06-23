---
id: fuzzy-regression-discontinuity-design
title: Fuzzy Regression Discontinuity Design
domain: economics
course: econometrics
prerequisites:
- id: regression-discontinuity
  type: hard
- id: instrumental-variables
  type: hard
- id: sharp-regression-discontinuity-design
  type: hard
tags:
- causal-inference
- regression-discontinuity
- instrumental-variables
stage: formal-systems
status: validated
---

# Fuzzy Regression Discontinuity Design

## Core Idea
In fuzzy RDD, the probability of treatment jumps discontinuously at the threshold c*, but not from 0 to 1. The running variable serves as an instrument for treatment. The estimand is the LATE (Local Average Treatment Effect) for units near the cutoff whose treatment status is affected by the discontinuity.

## Questions

```yaml
- question: "A scholarship program sends eligibility letters to students scoring above 70. 80% of eligible students accept; 5% of ineligible students receive it through exceptions. A researcher uses fuzzy RDD. What exactly does the estimated effect measure?"
  type: multiple-choice
  options:
    - "The average treatment effect of scholarships on the full population of students"
    - "The effect of receiving the eligibility letter on scholarship take-up (the first stage)"
    - "The effect of the scholarship on outcomes for compliers near the cutoff — those whose treatment status changes based on eligibility"
    - "The raw difference in outcomes between students just above and just below the cutoff"
  answer: 2
  explanation: "Fuzzy RDD estimates the LATE — the Local Average Treatment Effect for 'compliers' near the cutoff: students who take the scholarship when eligible but would not have received it otherwise. It is not the ATE for all students (too broad), not the effect of receiving a letter (that's the first stage), and not the raw outcome gap (that's the reduced form before correcting for incomplete takeup). The IV logic restricts identification to compliers near the threshold."

- question: "What is the fuzzy RDD estimator equal to?"
  type: multiple-choice
  options:
    - "The jump in outcomes at the cutoff divided by the jump in treatment probability at the cutoff"
    - "The jump in treatment probability divided by the jump in outcomes at the cutoff"
    - "The regression coefficient on treatment status in a local linear regression, with no adjustment"
    - "The average difference in outcomes between all treated and untreated units near the cutoff"
  answer: 0
  explanation: "The fuzzy RDD estimator is the reduced-form discontinuity (jump in outcomes) divided by the first-stage discontinuity (jump in treatment probability) — exactly the IV ratio estimator applied locally at the threshold. When the first-stage jump equals 1 (sharp RDD), the denominator is 1 and the estimator collapses to the outcome jump alone, as expected."

- question: "In fuzzy RDD, crossing the threshold serves as an instrumental variable for actual treatment receipt."
  type: true-false
  answer: true
  explanation: "True. The threshold-crossing indicator satisfies IV conditions locally: it is strongly correlated with treatment (relevance — it causes a discontinuous jump in treatment probability), and it only affects outcomes through its effect on treatment take-up (exclusion — units just above and below the cutoff are otherwise comparable). The LATE is estimated via the IV ratio, not directly from the outcome discontinuity alone."

- question: "Fuzzy RDD cannot be used when some units below the threshold still receive treatment, because this violates the design's identifying assumptions."
  type: true-false
  answer: false
  explanation: "False. Some below-threshold units receiving treatment is precisely what defines fuzzy (as opposed to sharp) RDD. The design accommodates imperfect compliance — the threshold need only cause a discontinuous jump in the probability of treatment, not a jump from 0 to 1. The IV framework handles partial compliance by using threshold-crossing as an instrument and focusing estimation on compliers."

- question: "Why does fuzzy RDD estimate the LATE rather than the ATE, and what types of units does this LATE cover?"
  type: short-answer
  answer: "Fuzzy RDD estimates the LATE because the instrument (threshold-crossing) only generates variation in treatment for 'compliers' near the cutoff — units whose treatment status changes based on which side they fall. Always-takers (who receive treatment regardless) and never-takers (who don't, regardless) are unaffected by the instrument, so their treatment effects cannot be identified. The LATE is further restricted to units near the cutoff because that's the only region where the local natural experiment is credible."
  explanation: "This is IV logic applied locally. Just as standard IV estimates LATE for compliers in the instrument's region of variation, fuzzy RDD estimates LATE for compliers in the neighborhood of the cutoff. Sharp RDD is the special case where all units near the cutoff are compliers (treatment jumps from 0 to 1), so LATE = ATE at the cutoff."
```

## Explainer

From your study of sharp RDD, you know the basic idea: if assignment to treatment is determined by whether a running variable crosses a threshold, units just below and just above the cutoff are nearly identical, making the discontinuity a natural experiment. The clean assumption in sharp RDD is that every unit above the threshold receives treatment and every unit below does not — the assignment rule is perfectly enforced. But in many real applications, the threshold only *changes the probability* of treatment — some units above it don't receive treatment, and some below it do. This is the **fuzzy RDD** setting.

The classic example is a scholarship program that automatically sends an eligibility letter to students scoring above a test cutoff. Most students who receive the letter take up the scholarship, but some don't bother, and a few below the cutoff receive it through discretionary decisions by administrators. The running variable (test score) no longer perfectly determines treatment — it only shifts the probability. Near the cutoff, you observe a jump in the fraction treated, but not from 0 to 1. Graphically, if you plot treatment takeup against the running variable, you see a discontinuous *jump* at the threshold, but the treatment probability remains strictly between 0 and 1 on both sides.

Here is where your knowledge of **instrumental variables** becomes essential. Being just above versus just below the cutoff serves as an instrument for actual treatment receipt. Think through the IV conditions: (1) **Relevance**: crossing the threshold increases the probability of treatment — this is the first stage, and it is directly visible as the jump in treatment rate. (2) **Exclusion**: being just above the cutoff only affects outcomes through its effect on treatment take-up, not through any direct channel. The local nature of RDD — comparing only units very close to the cutoff — makes this exclusion assumption far more credible than in a typical IV setup, because units just above and just below are nearly identical in all other respects.

The fuzzy RDD estimand is the **Local Average Treatment Effect**: the effect of treatment for "compliers" near the cutoff — those whose treatment status would change depending on which side of the threshold they fall. This is the same LATE you encountered in IV: compliers are the units who take treatment when nudged by the instrument but would not otherwise. The estimator is the ratio of the reduced-form discontinuity (the jump in outcomes at the threshold) to the first-stage discontinuity (the jump in treatment probability). This is exactly the IV ratio estimator, implemented locally. When the first-stage jump is 1 — when everyone above takes up and no one below does — fuzzy and sharp RDD coincide, and the LATE equals the ATE for compliers at the cutoff.
