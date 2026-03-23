---
id: regression-discontinuity-design
title: Regression Discontinuity Design
domain: health-and-human-development
course: epidemiology
prerequisites:
- id: natural-experiments
  type: hard
- id: epidemiologic-study-designs
  type: soft
tags:
- quasi-experimental
- threshold-design
- causal-effects
stage: expert
status: draft
---

# Regression Discontinuity Design

## Core Idea
Regression discontinuity (RD) exploits a known threshold in an assignment rule (e.g., patients above age 65 receive treatment) to estimate causal effects. Comparing individuals just above and below the threshold eliminates confounding from variables varying smoothly near the cutoff, though effects are local to the threshold.

## Questions

```yaml
- question: "A study uses U.S. Medicare eligibility (which begins at age 65) as an RD design to estimate the effect of health insurance on mortality. What is the most accurate characterization of the causal effect this design identifies?"
  type: multiple-choice
  options:
    - "The average causal effect of insurance for the entire U.S. adult population"
    - "The causal effect of insurance specifically for people near age 65 — not necessarily for 40- or 75-year-olds"
    - "The effect only for people who voluntarily enroll in Medicare, not for all eligibles"
    - "An unbiased estimate of the effect only if mortality trends are linear with age"
  answer: 1
  explanation: "RD estimates a local average treatment effect (LATE) at the threshold — here, the causal effect of insurance for near-65-year-olds. Whether this generalizes to other age groups depends on substantive reasoning about treatment effect heterogeneity, not on the design itself. Option A is wrong because RD is explicitly a local estimator. Option C confuses compliance issues in a fuzzy RD with the scope of inference. Option D misunderstands bandwidth and functional-form choices as validity conditions."

- question: "Before relying on an RD estimate, a researcher checks whether baseline health measures (prior hospitalization rates, income) show discontinuities at the threshold. This check is designed to test:"
  type: multiple-choice
  options:
    - "Whether the running variable is measured without error"
    - "Whether the smoothness assumption holds — that no other determinants of the outcome also jump at the cutoff"
    - "Whether the bandwidth around the threshold is large enough for statistical power"
    - "Whether the effect is linear in the running variable"
  answer: 1
  explanation: "The identifying assumption in RD is that all determinants of the outcome vary smoothly at the threshold — any jump in the outcome at the cutoff is attributed to the treatment. If observable covariates also show discontinuities, it suggests confounding variables are themselves discontinuous at the cutoff, compromising the design's validity. This check directly tests the smoothness assumption, not measurement precision, bandwidth, or functional form."

- question: "If people can precisely manipulate their value of the running variable to sort themselves just above or just below the cutoff, the RD design remains valid as long as an outcome discontinuity is still detectable."
  type: true-false
  answer: false
  explanation: "Manipulation of the running variable directly violates the comparability of units near the threshold, which is the design's foundation. If people can sort themselves, those just above and just below the cutoff are no longer similar — they differ systematically by their ability or motivation to manipulate. A McCrary density test detects this by checking for a spike in the running variable's distribution at the cutoff. A detectable outcome discontinuity does not rescue the design if the groups being compared are already systematically different."

- question: "In a regression discontinuity design, the identifying assumption is that all determinants of the outcome vary smoothly at the threshold, so any jump in the outcome at the cutoff is caused by the treatment."
  type: true-false
  answer: true
  explanation: "This is the core identifying assumption of RD. Because everything except treatment assignment is assumed to change smoothly at the cutoff, a sharp discontinuity in the outcome can only be caused by the treatment itself. This is why RD extracts credible causal evidence from arbitrary administrative rules: the cutoff is unrelated to outcomes except through the treatment it triggers."

- question: "Why is a 'fuzzy' RD design analyzed using instrumental variables methods rather than a simple comparison of means above and below the threshold?"
  type: short-answer
  answer: "In a fuzzy RD, crossing the threshold changes the probability of treatment but does not deterministically assign it — some units above the cutoff don't take up treatment and some below do. The threshold acts as an instrument: it affects treatment probability (relevance) but affects outcomes only through treatment (exclusion restriction). IV methods recover the causal effect for 'compliers' — those whose treatment status changes because of the threshold — and scale the reduced-form jump in outcomes by the jump in treatment probability at the cutoff."
  explanation: "A simple comparison of means above and below would conflate compliers and non-compliers, biasing the estimate. IV correctly accounts for imperfect compliance by using the discontinuity in treatment probability as the identifying variation. This connects fuzzy RD directly to the IV framework: the threshold is the instrument, the treatment indicator is the endogenous variable, and the outcome is what you are estimating."
```

## Explainer

From your study of natural experiments, you know that nature and policy sometimes create variation in treatment assignment that is as good as random — not because researchers designed it, but because of arbitrary rules or external events. **Regression discontinuity design** is the most elegant exploitation of a specific type of natural experiment: one where treatment is assigned based on whether a continuous variable (the **running variable**) crosses a known threshold. The design turns the arbitrariness of the cutoff into a source of valid causal inference.

The canonical example is age-based eligibility. Medicare eligibility in the United States triggers at age 65 precisely. Someone who is 64 years and 11 months old is not eligible; someone who just turned 65 is. These two people are, in every meaningful respect, nearly identical — their health, income, education, and prior medical history are distributed almost the same in the population near that boundary. The sharp jump in treatment probability at exactly 65 is therefore arguably unrelated to the factors that would confound a naive comparison between the insured and uninsured. RD compares outcomes just above and just below the threshold to estimate what the insurance itself caused.

The identifying assumption is that all other determinants of the outcome vary **smoothly** at the threshold — meaning any jump in the outcome at the cutoff must be caused by the treatment, not by some other variable also jumping there. In practice, you test this by checking whether observable covariates (baseline health, demographics) show any discontinuities at the cutoff; if they do, the design is compromised. You also check for **manipulation**: if people can precisely sort themselves above or below the cutoff (e.g., if doctors delay a diagnosis to get a patient over a threshold), the groups near the boundary are no longer comparable. The density of the running variable around the cutoff — tested with McCrary's density test — should be smooth. A suspicious spike just above the cutoff suggests sorting.

The critical limitation of RD is that its estimates are **local to the threshold**: the causal effect applies to people whose running variable is close to the cutoff, not to the entire population. In the Medicare example, the effect of insurance is estimated for near-65-year-olds — people who are about to age into eligibility. Whether that estimate generalizes to, say, 45-year-olds or 75-year-olds depends on substantive reasoning about treatment effect heterogeneity, not on the design itself. This local average treatment effect (LATE) is often exactly the policy-relevant quantity — policymakers are frequently asking what happens at the margin — but it must be interpreted carefully. When treatment is only probabilistically rather than deterministically assigned at the threshold (a "fuzzy" RD), instrumental variables methods are used to account for imperfect compliance, and the effect estimate is scaled by the change in the probability of treatment at the cutoff. The elegance of RD is that it extracts credible causal evidence from rules that were never designed for research — but that credibility is entirely contingent on the smoothness assumption holding.
