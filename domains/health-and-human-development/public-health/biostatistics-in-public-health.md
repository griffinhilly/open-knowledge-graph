---
id: biostatistics-in-public-health
title: Biostatistics in Public Health
domain: health-and-human-development
course: public-health
prerequisites:
- id: disease-frequency-measures
  type: hard
- id: measures-of-association
  type: hard
- id: statistical-methods-analytical
  type: soft
- id: health-literacy-and-communication
  type: soft
builds-toward:
- screening-and-early-detection
tags:
- biostatistics
- confidence-intervals
- hypothesis-testing
- regression
- p-values
stage: advanced
status: validated
---
# Biostatistics in Public Health

## Core Idea
Biostatistics provides the quantitative methods for designing studies, analyzing data, and drawing valid inferences in public health. Key concepts include hypothesis testing (null vs. alternative hypothesis, Type I and Type II errors), confidence intervals (the range of plausible values for a population parameter), and p-values (the probability of observed data given the null hypothesis). Logistic regression models binary outcomes adjusting for multiple confounders; survival analysis handles time-to-event data with censoring, common in cohort studies. Power and sample size calculations are conducted before studies begin to ensure adequate precision to detect meaningful effect sizes.

## How It's Best Learned
Work through the analysis of a cohort study dataset: compute crude and adjusted relative risks, calculate 95% confidence intervals, interpret p-values in context, and distinguish statistical significance from clinical or public health significance.

## Common Misconceptions
- A p-value is not the probability that the null hypothesis is true; it is the probability of data as extreme as observed, assuming the null is true.
- Statistical significance is not the same as practical importance; large studies can detect trivially small effects.
- Confounding adjustment via regression requires correct model specification; including a collider instead of a confounder introduces bias rather than removing it.

## Questions

```yaml
- question: "A study finds p = 0.03. Which interpretation is correct?"
  type: multiple-choice
  options:
    - "There is a 3% chance that the null hypothesis is true"
    - "There is a 97% chance that the finding reflects a real effect"
    - "If the null hypothesis were true, there is a 3% probability of observing data at least this extreme"
    - "The effect is large enough to be clinically meaningful"
  answer: 2
  explanation: "The p-value is a conditional probability: P(data this extreme | H₀ is true). It is not the probability that H₀ is true, and it says nothing about whether an effect is practically important. Options A and B commit the 'inverse probability fallacy' — they flip the conditioning. A p-value of 0.03 tells you that the observed data would be surprising if the null were true, but it does not tell you the probability that the null is or isn't true. Clinical significance is a separate judgment requiring knowledge of effect size and context."

- question: "A cohort study of 600,000 people finds that a dietary exposure is associated with a 2% higher risk of hypertension (RR = 1.02, 95% CI: 1.01–1.03, p < 0.0001). What is the most accurate interpretation?"
  type: multiple-choice
  options:
    - "The finding is highly significant and the exposure is an important public health target"
    - "The finding is statistically significant but the effect size is small enough that its public health importance depends on exposure prevalence and other factors"
    - "The narrow confidence interval confirms a large effect"
    - "The low p-value means the result is almost certainly not due to chance, so the exposure must be important"
  answer: 1
  explanation: "This scenario illustrates the critical distinction between statistical and practical significance. With 600,000 participants, the study has enormous power to detect tiny effects — even effects too small to matter for public health. A 2% increased risk (RR = 1.02) with a narrow CI means the study is precise about a small effect. Whether that effect matters depends on how prevalent the exposure is, what interventions exist, and what competing health priorities exist. Large studies routinely detect trivially small effects with p < 0.0001."

- question: "A p-value of 0.03 means there is a 3% chance that the null hypothesis is true."
  type: true-false
  answer: false
  explanation: "This is the most common misinterpretation of p-values. The p-value gives you P(data this extreme | H₀ true) — a probability of the data given the hypothesis, not the probability of the hypothesis given the data. Computing P(H₀ true | data) requires prior probabilities, which frequentist hypothesis testing does not incorporate. The correct statement is: 'If the null hypothesis were true, there would be a 3% probability of observing results as extreme as these by chance.'"

- question: "Including a collider variable in a regression model can introduce bias rather than remove it."
  type: true-false
  answer: true
  explanation: "A collider is a variable caused by both the exposure and the outcome (rather than causing them). Conditioning on a collider — including it as a covariate in a model — opens a spurious association between the exposure and outcome that does not reflect a real causal pathway. This is opposite to what happens with a true confounder (which causes both exposure and outcome, and should be controlled). The distinction between confounders and colliders requires causal reasoning — typically using directed acyclic graphs (DAGs) — not statistical criteria alone."

- question: "Why do researchers report 95% confidence intervals in addition to (or instead of) p-values when presenting study results?"
  type: short-answer
  answer: "Confidence intervals convey two pieces of information p-values alone cannot: the estimated effect size and the precision of that estimate. A 95% CI gives the range of population parameter values consistent with the observed data. A wide CI signals an imprecise estimate; a narrow CI around a small effect distinguishes 'precisely estimated small effect' from 'imprecisely estimated large effect.' P-values only indicate whether the null can be rejected at a threshold — they do not communicate effect magnitude."
  explanation: "Consider two studies: one finds RR = 3.0 with 95% CI (0.5–18) and another finds RR = 1.1 with 95% CI (1.09–1.11). The first is statistically non-significant (CI crosses 1.0) but suggests a possibly large effect measured imprecisely. The second is highly significant but shows a trivially small effect measured with great precision. Neither story is told by p-values alone. The CI also allows readers to judge clinical significance directly: if the entire CI lies in the 'clinically unimportant' zone, the finding is practically irrelevant regardless of p-value."
```

## Explainer

You already know how to compute rates, risks, and measures of association from your prerequisite work. Biostatistics in public health asks a harder question: how do you know whether the association you computed reflects something real in the population, or whether it could have arisen by chance, bias, or confounding? The statistical framework you are now learning is designed to answer the first of these concerns—chance—while the epidemiologic concepts of bias and confounding address the rest.

**Hypothesis testing** formalizes the logic of ruling out chance. You begin with a **null hypothesis** (H₀)—typically, that there is no association between exposure and outcome—and ask: if H₀ were true, how probable would it be to observe data at least as extreme as what I found? That probability is the **p-value**. A small p-value (conventionally < 0.05) means the data are unlikely under H₀, providing evidence against it. The critical misconception to avoid: a p-value is *not* the probability that H₀ is true, nor is it the probability that the finding is real. It is a probability of data given a hypothesis—a subtle but crucial distinction. **Type I error** (false positive) occurs when you reject a true H₀; the significance threshold α directly sets this rate. **Type II error** (false negative) occurs when you fail to reject a false H₀; its complement is statistical power. Power is why sample size calculations are done before a study: a study too small to detect a true effect is not just uninformative—it is potentially harmful, because it produces false null results that can delay public health action.

**Confidence intervals** convey more information than p-values and should be your primary reporting tool. A 95% CI gives the range of population parameter values consistent with the observed data—it quantifies both the estimated effect size and the precision of that estimate. A wide CI means your study is imprecise; a narrow CI around a small effect means your study is precise but the effect is small. Crucially, statistical significance and public health importance can come apart: a study with 500,000 participants might find a relative risk of 1.02 with a 95% CI of 1.01–1.03 (highly statistically significant) for an exposure that is practically inconsequential.

**Logistic regression** is the workhorse for binary outcomes (disease yes/no) when you need to control for multiple confounders simultaneously. From your study of measures of association, you know that crude associations can be distorted by factors that are related to both exposure and outcome. Logistic regression produces adjusted **odds ratios** that estimate the exposure-outcome relationship at fixed values of covariates. **Survival analysis** (Kaplan-Meier curves, Cox proportional hazards models) extends this logic to time-to-event data with **censoring**—participants who are lost to follow-up or have not yet experienced the event by study end. The power of these methods depends entirely on correct model specification: including genuine confounders removes bias, but including a **collider** (a variable caused by both exposure and outcome) opens a spurious pathway and *introduces* bias. Knowing which variables belong in a model requires a causal framework—the directed acyclic graphs (DAGs) you will encounter in advanced epidemiology—not statistical instinct alone.
