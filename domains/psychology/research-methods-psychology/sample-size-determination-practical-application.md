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
stage: formal-systems
status: validated
---

# Sample Size Determination in Research Planning

## Core Idea
Sample size must be adequate to detect your hypothesized effect with sufficient statistical power (typically 80% or higher) while controlling false positive rates (alpha = .05). Larger effect sizes require fewer participants; smaller effects require larger samples. Underpowered studies are likely to miss true effects and can produce spurious significant findings through noise; overpowered studies waste resources on unnecessary precision.

## Questions

```yaml
- question: "A researcher runs an underpowered study (N=25 per group) and finds a statistically significant result at p < .05. What is the most accurate interpretation?"
  type: multiple-choice
  options:
    - "The result is reliable — statistical significance is the same regardless of sample size"
    - "The result is likely a true positive and probably represents the true effect size accurately"
    - "The significant result is likely real, but the effect size estimate is probably inflated compared to the true population effect"
    - "The result is certainly a false positive because the study was underpowered"
  answer: 2
  explanation: "This is the 'winner's curse.' To reach significance in an underpowered study, a random effect estimate must be larger than average — only inflated estimates cross the significance threshold when N is too small. So significant results from underpowered studies systematically overestimate effect sizes. The result may or may not be a true positive, but if it is, the published estimate is likely exaggerated. Replication attempts with adequate power then fail to find effects of that magnitude, contributing to the replication crisis."

- question: "A researcher expects a small effect (d = 0.2) and recruits 30 participants per group. Which outcome is most likely?"
  type: multiple-choice
  options:
    - "Adequate power to detect the effect because d = 0.2 is a real effect that alpha = .05 should catch"
    - "The study is severely underpowered — detecting d = 0.2 at 80% power requires roughly 394 participants per group"
    - "The study is slightly underpowered but will probably reach significance if the true effect exists"
    - "Power is adequate because the researcher can always increase N after seeing a trend in the data"
  answer: 1
  explanation: "A small effect by Cohen's conventions (d = 0.2) requires ~394 participants per group to achieve 80% power at α = .05. With only 30 per group, power is roughly 11% — the study will miss the effect nine times out of ten. Researchers dramatically underestimate how large samples need to be for small effects. Adding participants after seeing a trend (optional stopping) inflates the false positive rate and is not a valid remedy."

- question: "An underpowered study that finds a statistically significant result is more likely to accurately estimate the true effect size than an adequately powered study."
  type: true-false
  answer: false
  explanation: "The opposite is true. To reach statistical significance when sample size is small, a random effect estimate must be inflated above the population value. This is the winner's curse: the significant result 'won' the noise lottery, producing an estimate that exceeds the truth. Adequately powered studies find significance for typical estimates near the true effect size, not just for outlier estimates. This is why the literature systematically overestimates effects when built from underpowered studies."

- question: "Conducting a power analysis requires you to specify the expected effect size before collecting data."
  type: true-false
  answer: true
  explanation: "True. Power is a function of four quantities: N, effect size, alpha, and power (1-β). A power analysis solves for N given the other three, so you must commit to an expected effect size in advance. This forces researchers to engage with prior literature and meta-analyses, and creates accountability through preregistration. Researchers who skip this step typically collect whatever N is convenient, which is almost always too small for the effect sizes their designs can realistically detect."

- question: "Why do statistically significant results from underpowered studies often fail to replicate in later, adequately powered studies?"
  type: short-answer
  answer: "Underpowered studies produce significant results only when their random effect estimates happen to be inflated above the true population value — the winner's curse. The published significant finding therefore overstates the true effect. When a larger, adequately powered study looks for an effect of the published magnitude, it doesn't find one at that size, even if the underlying effect is real and smaller. This systematic inflation of published effect sizes is a major cause of replication failures."
  explanation: "This connects underpowering to the replication crisis. It's not just that underpowered studies miss effects (Type II error) — it's that the ones they do catch are biased upward. The entire published literature on a topic can become an overestimate of reality when it is built from underpowered studies, making it look like science is inconsistent when the real problem is systematic bias at the study design stage."
```

## Explainer

From your study of **effect size and statistical power**, you know that power is the probability of detecting a true effect when it exists. Power is a function of four quantities that are mathematically locked together: **sample size (N)**, **effect size (d or f or r)**, **alpha (the false positive threshold)**, and **power (1 - β, the false negative threshold)**. Fix any three of these and the fourth is determined. A **power analysis** is simply solving this equation: given an expected effect size, a desired power level (usually .80), and a chosen alpha (.05), what N do you need?

The most common practical challenge is specifying the expected effect size before the study. Three sources help: prior literature (what effect size did similar studies find?), meta-analyses of the domain (what is the average effect?), and theoretical constraints (is there a smallest effect that would be scientifically or practically meaningful?). The most important rule is to be conservative: small effects require much larger samples than researchers intuitively expect. A small effect by Cohen's conventions (d = 0.2) requires roughly 394 participants per group to achieve 80% power at α = .05. Researchers who budget for 30 participants per group are planning to be underpowered for anything smaller than a large effect.

**Underpowering** has two separate harms that are often conflated. The obvious harm is missing a real effect — a false negative, Type II error. The less obvious harm is that significant results from underpowered studies are *more likely to be false positives*. This is the winner's curse: to reach significance in a noisy small-N study, a random effect estimate must be inflated above the true population value. The published significant findings from underpowered studies therefore tend to overestimate effect sizes, and replication attempts with more appropriate samples fail — which is a major driver of the replication crisis. **Overpowering**, by contrast, is a waste of resources and an ethical issue in studies with invasive procedures or deception, but it does not distort the literature in the same way.

In practice, sample size planning begins with the most specific possible research question — from your prerequisite concept — because the statistical test you plan to use determines which power analysis formula applies. A two-sample t-test, a one-way ANOVA with 4 groups, and a correlation test have different power functions. Tools like G*Power (free software) implement these calculations for dozens of test families. Document your power analysis in your preregistration: your expected effect size and its source, your desired power, your alpha, and your resulting N. This creates accountability for decisions made before data collection, and makes the study's sensitivity (the smallest effect it could realistically detect) transparent to readers.
