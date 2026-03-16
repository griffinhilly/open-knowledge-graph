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
builds-toward:
- screening-and-early-detection
tags:
- biostatistics
- confidence-intervals
- hypothesis-testing
- regression
- p-values
stage: formal-systems
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

## Explainer

You already know how to compute rates, risks, and measures of association from your prerequisite work. Biostatistics in public health asks a harder question: how do you know whether the association you computed reflects something real in the population, or whether it could have arisen by chance, bias, or confounding? The statistical framework you are now learning is designed to answer the first of these concerns—chance—while the epidemiologic concepts of bias and confounding address the rest.

**Hypothesis testing** formalizes the logic of ruling out chance. You begin with a **null hypothesis** (H₀)—typically, that there is no association between exposure and outcome—and ask: if H₀ were true, how probable would it be to observe data at least as extreme as what I found? That probability is the **p-value**. A small p-value (conventionally < 0.05) means the data are unlikely under H₀, providing evidence against it. The critical misconception to avoid: a p-value is *not* the probability that H₀ is true, nor is it the probability that the finding is real. It is a probability of data given a hypothesis—a subtle but crucial distinction. **Type I error** (false positive) occurs when you reject a true H₀; the significance threshold α directly sets this rate. **Type II error** (false negative) occurs when you fail to reject a false H₀; its complement is statistical power. Power is why sample size calculations are done before a study: a study too small to detect a true effect is not just uninformative—it is potentially harmful, because it produces false null results that can delay public health action.

**Confidence intervals** convey more information than p-values and should be your primary reporting tool. A 95% CI gives the range of population parameter values consistent with the observed data—it quantifies both the estimated effect size and the precision of that estimate. A wide CI means your study is imprecise; a narrow CI around a small effect means your study is precise but the effect is small. Crucially, statistical significance and public health importance can come apart: a study with 500,000 participants might find a relative risk of 1.02 with a 95% CI of 1.01–1.03 (highly statistically significant) for an exposure that is practically inconsequential.

**Logistic regression** is the workhorse for binary outcomes (disease yes/no) when you need to control for multiple confounders simultaneously. From your study of measures of association, you know that crude associations can be distorted by factors that are related to both exposure and outcome. Logistic regression produces adjusted **odds ratios** that estimate the exposure-outcome relationship at fixed values of covariates. **Survival analysis** (Kaplan-Meier curves, Cox proportional hazards models) extends this logic to time-to-event data with **censoring**—participants who are lost to follow-up or have not yet experienced the event by study end. The power of these methods depends entirely on correct model specification: including genuine confounders removes bias, but including a **collider** (a variable caused by both exposure and outcome) opens a spurious pathway and *introduces* bias. Knowing which variables belong in a model requires a causal framework—the directed acyclic graphs (DAGs) you will encounter in advanced epidemiology—not statistical instinct alone.
