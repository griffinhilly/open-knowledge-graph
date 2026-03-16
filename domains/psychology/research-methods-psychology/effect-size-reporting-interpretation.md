---
id: effect-size-reporting-interpretation
title: Effect Size Reporting and Practical Interpretation
domain: psychology
course: research-methods-psychology
prerequisites:
- id: effect-size-and-power
  type: hard
builds-toward:
- type-i-type-ii-error-tradeoffs
tags:
- statistics
- effect-size
- interpretation
stage: abstract-reasoning
status: draft
---

# Effect Size Reporting and Practical Interpretation

## Core Idea
Effect size quantifies the magnitude of an effect (correlation coefficient, standardized difference between means, odds ratio) independent of sample size. Effect sizes are essential for interpreting the practical importance of statistically significant findings, for power analysis, and for meta-analysis. Reporting effect sizes with confidence intervals provides a complete picture of both magnitude and precision of your findings.

## Explainer

Statistical significance and effect size address fundamentally different questions, and your study of effect size and statistical power introduced the crucial distinction. Significance asks: could this result be due to chance? Effect size asks: how large is the result? With a sufficiently large sample, almost any difference — no matter how trivially small in practice — will reach statistical significance. With a small sample, a substantial and meaningful effect may fail to reach significance. Effect size cuts through this sample-size dependence and gives the magnitude of the phenomenon directly.

The most common effect size measures are **Cohen's d** (for comparing means), **r** or **r²** (for correlations), and **odds ratios** or **risk ratios** (for categorical outcomes). Cohen's d expresses the mean difference between groups in standard deviation units: d = (M₁ − M₂) / SD_pooled. By convention, d ≈ 0.2 is "small," d ≈ 0.5 is "medium," and d ≈ 0.8 is "large" — conventions derived empirically from the social science literature. But these thresholds should not be applied mechanically. A d of 0.3 for a low-cost public health screening program may be highly meaningful; a d of 0.3 for an expensive individualized intervention might be disappointing. **Context, not convention, determines practical importance.** Ask: is this effect large enough to matter given the cost, risk, and alternatives?

Complete reporting combines three elements. The **point estimate** (e.g., d = 0.45) is the sample's best guess at the true population effect. The **95% confidence interval** (e.g., [0.20, 0.70]) gives the plausible range for the population effect and communicates precision: narrow intervals indicate well-estimated effects; wide intervals indicate imprecision, usually due to small samples. The **significance test** indicates whether the effect is distinguishable from zero given sampling variability. All three are needed: significance alone tells you the effect is probably real, but not whether it matters; effect size alone without uncertainty bounds may overstate confidence.

Effect sizes are also the currency of **meta-analysis** — the statistical synthesis of results across multiple studies on the same topic. Because individual studies use different sample sizes and raw score scales, you cannot meaningfully average their p-values or raw means. But you can average their standardized effect sizes. Meta-analysis is how cumulative scientific knowledge gets built in psychology: any single study may be noisy or idiosyncratic, but averaging across many well-designed studies converges on the true underlying effect. Accurate effect size reporting is therefore a form of scientific infrastructure — missing or misreported effect sizes degrade the quality of every future meta-analysis that would otherwise include your work.
