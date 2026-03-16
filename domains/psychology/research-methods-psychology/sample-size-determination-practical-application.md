---
id: sample-size-determination-practical-application
title: Sample Size Determination in Research Planning
domain: psychology
course: research-methods-psychology
prerequisites:
- id: effect-size-and-power
  type: hard
- id: research-question-formulation-specificity
  type: soft
builds-toward:
- effect-size-reporting-interpretation
tags:
- planning
- sample-size
- power
stage: abstract-reasoning
status: draft
---

# Sample Size Determination in Research Planning

## Core Idea
Sample size must be adequate to detect your hypothesized effect with sufficient statistical power (typically 80% or higher) while controlling false positive rates (alpha = .05). Larger effect sizes require fewer participants; smaller effects require larger samples. Underpowered studies are likely to miss true effects and can produce spurious significant findings through noise; overpowered studies waste resources on unnecessary precision.

## Explainer

From your study of **effect size and statistical power**, you know that power is the probability of detecting a true effect when it exists. Power is a function of four quantities that are mathematically locked together: **sample size (N)**, **effect size (d or f or r)**, **alpha (the false positive threshold)**, and **power (1 - β, the false negative threshold)**. Fix any three of these and the fourth is determined. A **power analysis** is simply solving this equation: given an expected effect size, a desired power level (usually .80), and a chosen alpha (.05), what N do you need?

The most common practical challenge is specifying the expected effect size before the study. Three sources help: prior literature (what effect size did similar studies find?), meta-analyses of the domain (what is the average effect?), and theoretical constraints (is there a smallest effect that would be scientifically or practically meaningful?). The most important rule is to be conservative: small effects require much larger samples than researchers intuitively expect. A small effect by Cohen's conventions (d = 0.2) requires roughly 394 participants per group to achieve 80% power at α = .05. Researchers who budget for 30 participants per group are planning to be underpowered for anything smaller than a large effect.

**Underpowering** has two separate harms that are often conflated. The obvious harm is missing a real effect — a false negative, Type II error. The less obvious harm is that significant results from underpowered studies are *more likely to be false positives*. This is the winner's curse: to reach significance in a noisy small-N study, a random effect estimate must be inflated above the true population value. The published significant findings from underpowered studies therefore tend to overestimate effect sizes, and replication attempts with more appropriate samples fail — which is a major driver of the replication crisis. **Overpowering**, by contrast, is a waste of resources and an ethical issue in studies with invasive procedures or deception, but it does not distort the literature in the same way.

In practice, sample size planning begins with the most specific possible research question — from your prerequisite concept — because the statistical test you plan to use determines which power analysis formula applies. A two-sample t-test, a one-way ANOVA with 4 groups, and a correlation test have different power functions. Tools like G*Power (free software) implement these calculations for dozens of test families. Document your power analysis in your preregistration: your expected effect size and its source, your desired power, your alpha, and your resulting N. This creates accountability for decisions made before data collection, and makes the study's sensitivity (the smallest effect it could realistically detect) transparent to readers.
