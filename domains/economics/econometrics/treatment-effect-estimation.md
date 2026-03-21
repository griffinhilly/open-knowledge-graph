---
id: treatment-effect-estimation
title: 'Treatment Effects: ATE, CATE, and Heterogeneous Effects'
domain: economics
course: econometrics
prerequisites:
- id: causal-inference-econometrics
  type: hard
- id: potential-outcomes-framework
  type: hard
- id: conditional-probability
  type: soft
builds-toward:
- matching-estimators-causal-inference
tags:
- causal-inference
- treatment-effects
- heterogeneous
stage: formal-systems
status: draft
---

# Treatment Effects: ATE, CATE, and Heterogeneous Effects

## Core Idea
The Average Treatment Effect (ATE) measures mean causal impact across the population; Conditional Average Treatment Effect (CATE) varies by subgroups; Local Average Treatment Effect (LATE) applies to compliers in instrumental variable settings. Identifying these requires assumptions about confounding and selection mechanisms.

## How It's Best Learned
Contrast ATE, CATE, and LATE with examples; understand which assumptions identify each and when each is relevant.

## Common Misconceptions
ATE and CATE are conceptually different; ATE averages over the population while CATE allows effects to differ by observable characteristics.

## Questions

```yaml
- question: "A researcher uses a draft lottery as an instrument to estimate the earnings effect of military service. The IV estimator identifies which estimand?"
  type: multiple-choice
  options:
    - "ATE — the average effect across all men in the eligible population"
    - "ATT — the effect on men who chose to serve voluntarily"
    - "LATE — the effect on men who served because they were drafted but would not have enlisted voluntarily"
    - "CATE — the effect conditional on observable characteristics like education and age"
  answer: 2
  explanation: "IV identifies LATE — the Local Average Treatment Effect — which is the treatment effect for compliers: people who comply with the instrument's assignment. In the draft lottery, compliers are men who served when drafted but would not have enlisted voluntarily. Always-takers (enlisted regardless) and never-takers (refused regardless) contribute no identifying variation. This LATE may differ substantially from ATE: men who served only because they were drafted may have had very different earnings trajectories than voluntary enlistees. Option A is ATE, which IV does not recover unless the instrument affects everyone."

- question: "A policy analyst wants to evaluate whether a job training program benefited the workers who participated in it. Which estimand is most appropriate?"
  type: multiple-choice
  options:
    - "ATE — the average effect if the program were extended to the entire eligible population"
    - "ATT — the effect on treated units, i.e., those who actually enrolled in the program"
    - "LATE — the effect on compliers with the assignment instrument"
    - "CATE — the subgroup effects conditional on worker characteristics"
  answer: 1
  explanation: "ATT (Average Treatment Effect on the Treated) answers: 'was the program beneficial for participants?' — exactly what this analyst wants. ATE would answer a different question: 'would it benefit the full eligible population, including those who didn't enroll?' ATE and ATT differ when people self-select into treatment based on expected benefit — workers who chose to enroll may have higher expected returns from training than non-enrollees. If that selection exists, ATE ≠ ATT. Specifying ATT clarifies that the target is participants, not a hypothetical universal rollout."

- question: "When a study uses an instrumental variable estimator and reports its main result, the estimate recovers the Average Treatment Effect (ATE) for the full population."
  type: true-false
  answer: false
  explanation: "IV identifies LATE — the treatment effect specifically for compliers, the subgroup whose treatment status is actually changed by the instrument. Unless the instrument affects everyone in the population (full compliance), LATE ≠ ATE. LATE can be larger, smaller, or even opposite in sign to ATE if compliers are a selected subgroup. Reporting an IV estimate as if it were the population ATE is a common and consequential error — always ask: 'who are the compliers for this instrument, and how representative are they?'"

- question: "CATE can be thought of as a function from covariate values to local treatment effects, rather than as a single number."
  type: true-false
  answer: true
  explanation: "CATE(x) = E[Y(1) − Y(0) | X = x] assigns a different expected treatment effect to each covariate vector x. Rather than averaging heterogeneous effects into one number (as ATE does), CATE preserves heterogeneity by conditioning on observable characteristics. For a drug, CATE might reveal the treatment works well for patients over 65 but has no effect for younger patients. This is why CATE estimation often uses machine learning methods (causal forests, meta-learners) that can flexibly model variation across the covariate space."

- question: "Why do most empirical papers report ATT or LATE rather than ATE, even when the policy question seems to call for ATE?"
  type: short-answer
  answer: "Most identification strategies — difference-in-differences, regression discontinuity, instrumental variables — only credibly identify treatment effects for a specific subpopulation, not the full population. DiD estimates the ATT for units that experienced the treatment. IV estimates LATE for compliers. RD estimates a local ATT near the cutoff. Estimating ATE would require identifying the counterfactual for everyone, including those who never received treatment and may be fundamentally different from treated units. Reporting ATT or LATE is honest about what the identification strategy actually delivers, even if ATE is the ultimately desired parameter."
  explanation: "The mismatch between the policy-relevant estimand (often ATE) and the identified estimand (often ATT or LATE) is one of the central tensions in applied econometrics. A drug approved based on a clinical trial's ATT may perform differently when given to the broader population — the people who enrolled in the trial (treated units) may be more motivated or healthier than the general public. Recognizing this gap, and being explicit about it, is what separates careful causal inference from naïve policy extrapolation."
```

## Explainer

From your potential outcomes prerequisite, you know the fundamental setup: every unit i has two potential outcomes — Y(1) if treated and Y(0) if not treated. The individual causal effect is τᵢ = Y(1)ᵢ − Y(0)ᵢ, but you observe only one potential outcome per person. Since individual effects are never identified, empirical work targets averages — and which average matters depends on the policy question being asked.

The **Average Treatment Effect (ATE)** is E[Y(1) − Y(0)] averaged over the full population, treated and untreated alike. This is the right quantity for a universal policy question: if we were to randomly select someone from the population and treat them, what would happen on average? The **Average Treatment Effect on the Treated (ATT)** narrows focus to those who actually received treatment: ATT = E[Y(1) − Y(0) | D = 1]. For a voluntary job training program, ATT tells you the benefit to participants — people who chose to enroll. ATE would additionally include the counterfactual effect on people who didn't enroll, which may be different if selection into treatment was based on expected benefit.

The **Conditional Average Treatment Effect (CATE)** takes heterogeneity seriously. Rather than a single number, CATE maps each covariate vector X to a local treatment effect: τ(x) = E[Y(1) − Y(0) | X = x]. This is the right framework when effects are expected to vary across subgroups — a drug may work better for older patients, a training program may benefit low-educated workers more. In practice, estimating CATE requires data-rich methods: causal forests and other machine learning approaches partition the covariate space to estimate local effects, but they need large samples to be precise. The fundamental tradeoff is between aggregation (ATE is precise but hides heterogeneity) and granularity (CATE reveals heterogeneity but demands more data and stronger assumptions).

The **Local Average Treatment Effect (LATE)** arises in instrumental variables settings. When you use an instrument Z to address selection into treatment, the IV estimator does not recover ATE or ATT — it recovers the effect only for **compliers**: people who take treatment when Z assigns them to treatment and decline when Z does not. Always-takers (who take treatment regardless) and never-takers (who never take it) contribute no identifying variation. LATE can differ substantially from ATE if compliers are unusual. In a military draft lottery study, LATE measures the earnings effect for men who served because they were drafted but would not have enlisted voluntarily — this may not generalize to those who chose to serve.

The practical lesson is to specify the target parameter before analyzing data. "The effect of X on Y" is incomplete. "The ATE if the policy is universally applied" differs from "the ATT — the effect on current participants" which differs from "which subgroups benefit most (CATE)" which differs from "what does this particular instrument identify (LATE)." Most empirical papers report ATT or LATE rather than ATE, because their identification strategy only credibly identifies effects for a specific subpopulation. Being explicit about which estimand you are targeting — and why it matches your policy question — is the hallmark of careful causal inference.
