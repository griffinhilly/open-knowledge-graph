---
id: statistical-power-and-effect-size-determination
title: Statistical Power, Effect Size, and Sample Size Planning
domain: psychology
course: research-methods-psychology
prerequisites:
- id: variable-definition-and-operational-measurement
  type: hard
- id: population-sampling-representativeness
  type: hard
- id: effect-size-and-power
  type: hard
- id: normal-distribution
  type: soft
- id: standard-normal-z-scores-theory
  type: hard
builds-toward:
- statistical-inference-significance-testing
tags:
- statistical-power
- effect-size
- sample-size
- design-planning
stage: formal-systems
status: draft
---

# Statistical Power, Effect Size, and Sample Size Planning

## Core Idea
Statistical power is the probability of detecting a true effect. It increases with sample size, effect size magnitude, and alpha level. Effect size quantifies the magnitude of an effect independent of sample size. A-priori power analysis plans sample size to achieve adequate power (typically 0.80). Underpowered studies risk Type II error (missing true effects); overpowered studies waste resources.

## How It's Best Learned
Use power analysis software (G*Power) to compute required sample sizes for typical effect sizes and power levels. Review published papers reporting effect sizes and power. Discuss why small-sample studies are common in psychology and their implications.

## Common Misconceptions
- Statistical significance proves practical significance; - All effect sizes worth studying are large; - Power analysis is only needed for rare or expensive studies; - Larger samples automatically mean valid inferences.

## Explainer

You've already encountered the concept that statistical significance depends on both the size of an effect and the precision of your estimate. **Statistical power** and **effect size** formalize this relationship and turn it into a design tool. Power is the probability that your study will detect a true effect when one exists — in other words, the probability of *not* making a Type II error (false negative). Power depends on three things under your control as a researcher: the effect size you're trying to detect, the sample size you collect, and the significance threshold you set.

**Effect size** is the metric that links statistical results to scientific meaning. It quantifies the magnitude of a difference or relationship in a scale-free way. Common effect size metrics include **Cohen's d** (for mean differences — a d of 0.5 means the group means are half a standard deviation apart), **r** (the correlation coefficient, which is its own effect size measure), and **η²** (proportion of variance explained in ANOVA). Cohen's benchmark guidelines — small (.2), medium (.5), large (.8) for d — are rough calibrations, not laws. What counts as a meaningful effect depends entirely on the domain: a d of 0.2 might be clinically important for a serious disease intervention but trivial for an attitude measure. Effect size connects your result to the world outside the p-value, which is why reporting it is now required by most journals.

**A-priori power analysis** is the practice of calculating required sample size *before* collecting data, given your target power (typically .80), your chosen alpha (.05), and your expected effect size. The mechanics work like this: power increases as sample size increases, because larger samples reduce sampling error, making it easier to distinguish real effects from noise. If you expect a small effect (d = 0.2), you need a much larger sample to reliably detect it than if you expect a large effect (d = 0.8). Underpowered studies — those with power below .80 — not only fail to detect true effects; they also produce unstable effect size estimates, because small samples vary widely. A study with 30% power that happens to find p < .05 likely observed an inflated effect by chance, which then fails to replicate.

The replication crisis in psychology was partly caused by widespread use of underpowered studies with flexible stopping rules — collecting data until p < .05 emerged. Understanding power helps you see exactly why this is problematic: if you stop when you first cross the significance threshold, you've created an implicit multiple-comparison problem (the more you look, the higher the false positive rate) and you've exploited sampling variability rather than estimated a true effect. The remedy is to commit to a sample size before you start, justify it with a power analysis, and pre-register your hypotheses. Power analysis is not a bureaucratic requirement — it is the tool that connects the precision of your measurement to the scientific claims you're entitled to make.
