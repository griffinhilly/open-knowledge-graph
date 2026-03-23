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
stage: formal-systems
status: validated
---

# Effect Size Reporting and Practical Interpretation

## Core Idea
Effect size quantifies the magnitude of an effect (correlation coefficient, standardized difference between means, odds ratio) independent of sample size. Effect sizes are essential for interpreting the practical importance of statistically significant findings, for power analysis, and for meta-analysis. Reporting effect sizes with confidence intervals provides a complete picture of both magnitude and precision of your findings.

## Questions

```yaml
- question: "A study with n = 50,000 participants finds a statistically significant result (p < 0.001) for a new educational intervention, with Cohen's d = 0.04. What is the most appropriate interpretation?"
  type: multiple-choice
  options:
    - "The intervention has a practically meaningful benefit and should be widely adopted"
    - "The p-value is impressive, so the effect size doesn't matter for policy decisions"
    - "With a very large sample, even a trivially small effect can reach statistical significance — the practical impact appears negligible"
    - "The study is flawed because a significant result should have a larger effect size"
  answer: 2
  explanation: "Statistical significance and practical importance are separate questions. With 50,000 participants, enormous statistical power means even d = 0.04 — far below Cohen's 'small' threshold of 0.2 — will reliably reach significance. But d = 0.04 means the intervention moves the average person only 4% of a standard deviation. For most educational interventions, this is far too small to justify adoption costs. The p-value confirms the effect is real; the effect size tells you it barely matters. Both are needed for an honest interpretation."

- question: "A new therapy shows Cohen's d = 0.3. Is this a clinically meaningful effect?"
  type: multiple-choice
  options:
    - "Yes — d = 0.3 exceeds Cohen's 'small' threshold of 0.2, so it is meaningful by definition"
    - "No — only d ≥ 0.5 ('medium') counts as a meaningful effect worth acting on"
    - "It depends on context: the cost, risk, available alternatives, and what the outcome means determine practical importance"
    - "It cannot be meaningful without also being statistically significant"
  answer: 2
  explanation: "Cohen's conventional thresholds are descriptive benchmarks from the social science literature, not universal standards of importance. A d of 0.3 for an inexpensive, low-risk public health intervention could be highly meaningful — a 30-cent screening that saves lives. The same d = 0.3 for an expensive, intensive clinical program might be disappointing. Context — cost, risk, alternatives, magnitude of the outcome — determines practical importance. The common misconception is treating Cohen's labels as verdicts rather than rough guides."

- question: "A study with a very large sample can produce a statistically significant result even if the true effect size is too small to have any practical importance."
  type: true-false
  answer: true
  explanation: "Statistical significance depends on both effect size and sample size. With N large enough, the standard error becomes tiny, and even a d of 0.01 will produce p < 0.05. This is why p-values alone cannot tell you whether an effect matters. Effect size is the sample-size-independent measure of magnitude — it tells you how big the difference actually is, regardless of how precisely it was measured."

- question: "Cohen's conventional thresholds (small ≈ 0.2, medium ≈ 0.5, large ≈ 0.8) should serve as the primary standard for judging whether a finding has practical importance."
  type: true-false
  answer: false
  explanation: "Cohen himself cautioned against mechanical application of his thresholds. They were derived empirically from average effect sizes across the social science literature — not from any analysis of what matters in practice. A d of 0.3 might be transformative in one context and trivial in another. Practical importance requires asking: given the cost, risk, and available alternatives, is this effect large enough to change decisions? The thresholds are a rough orientation, not a verdict."

- question: "Why are effect sizes — rather than p-values alone — essential for conducting a meta-analysis that synthesizes results across multiple studies?"
  type: short-answer
  answer: "Different studies use different sample sizes, measurement instruments, and raw score scales, making their p-values and raw means incomparable. You cannot meaningfully average p-values (they conflate effect size with sample size) or raw means (a '5-point improvement' on one scale means nothing relative to a '0.3-unit improvement' on another). Effect sizes like Cohen's d standardize across studies by expressing differences in standard deviation units, making results comparable regardless of the original scale. Meta-analysis averages these standardized estimates to estimate the true underlying effect across the literature."
  explanation: "Effect sizes are the currency of cumulative science. Each individual study is a noisy estimate of the true population effect. Meta-analysis reduces this noise by pooling estimates. But pooling only works if the estimates are on a common scale — which standardized effect sizes provide. Missing or misreported effect sizes in individual studies degrade every future meta-analysis that would have included that study, which is why complete effect size reporting is a form of scientific infrastructure."
```

## Explainer

Statistical significance and effect size address fundamentally different questions, and your study of effect size and statistical power introduced the crucial distinction. Significance asks: could this result be due to chance? Effect size asks: how large is the result? With a sufficiently large sample, almost any difference — no matter how trivially small in practice — will reach statistical significance. With a small sample, a substantial and meaningful effect may fail to reach significance. Effect size cuts through this sample-size dependence and gives the magnitude of the phenomenon directly.

The most common effect size measures are **Cohen's d** (for comparing means), **r** or **r²** (for correlations), and **odds ratios** or **risk ratios** (for categorical outcomes). Cohen's d expresses the mean difference between groups in standard deviation units: d = (M₁ − M₂) / SD_pooled. By convention, d ≈ 0.2 is "small," d ≈ 0.5 is "medium," and d ≈ 0.8 is "large" — conventions derived empirically from the social science literature. But these thresholds should not be applied mechanically. A d of 0.3 for a low-cost public health screening program may be highly meaningful; a d of 0.3 for an expensive individualized intervention might be disappointing. **Context, not convention, determines practical importance.** Ask: is this effect large enough to matter given the cost, risk, and alternatives?

Complete reporting combines three elements. The **point estimate** (e.g., d = 0.45) is the sample's best guess at the true population effect. The **95% confidence interval** (e.g., [0.20, 0.70]) gives the plausible range for the population effect and communicates precision: narrow intervals indicate well-estimated effects; wide intervals indicate imprecision, usually due to small samples. The **significance test** indicates whether the effect is distinguishable from zero given sampling variability. All three are needed: significance alone tells you the effect is probably real, but not whether it matters; effect size alone without uncertainty bounds may overstate confidence.

Effect sizes are also the currency of **meta-analysis** — the statistical synthesis of results across multiple studies on the same topic. Because individual studies use different sample sizes and raw score scales, you cannot meaningfully average their p-values or raw means. But you can average their standardized effect sizes. Meta-analysis is how cumulative scientific knowledge gets built in psychology: any single study may be noisy or idiosyncratic, but averaging across many well-designed studies converges on the true underlying effect. Accurate effect size reporting is therefore a form of scientific infrastructure — missing or misreported effect sizes degrade the quality of every future meta-analysis that would otherwise include your work.
