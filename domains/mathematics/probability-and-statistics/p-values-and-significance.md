---
id: p-values-and-significance
title: P-values and Statistical Significance
domain: mathematics
course: probability-and-statistics
prerequisites:
- id: hypothesis-test-framework
  type: hard
builds-toward:
- type-i-type-ii-errors-tradeoff
- effect-size-in-hypothesis-tests
tags:
- hypothesis-testing
- p-value
- significance
stage: formal-systems
status: draft
---

# P-values and Statistical Significance

## Core Idea
The p-value is the probability of observing data as extreme as ours (or more extreme) if H₀ were true. A result is 'statistically significant' if p < α (typically 0.05). Small p-values suggest data are inconsistent with H₀.

## How It's Best Learned
Calculate p-values for simple test statistics. Simulate null distributions to understand p-value as tail probability. Compare p-values to critical values. Recognize that significance ≠ importance.

## Common Misconceptions
Interpreting p-value as probability H₀ is true (backward; p-value is P(data|H₀)). Thinking p > 0.05 means H₀ is true. Confusing statistical significance with practical significance. Using p-value as a measure of effect size.

## Explainer

The **p-value** answers a very specific question: "If the null hypothesis were true, how likely would we be to see data at least as extreme as what we observed?" Notice the direction of conditioning — you are computing a probability about data, not about hypotheses. From your study of the hypothesis test framework, you know that H₀ defines a probability model. The p-value is a tail probability from that model: it measures how far out in the tail your observed test statistic sits. A p-value of 0.03 means "if H₀ were true, there would only be a 3% chance of getting data this extreme or more so." It does not mean H₀ has a 3% chance of being true.

The **significance threshold** α (usually 0.05) is a pre-set decision boundary, not a magical cutoff. Choosing α = 0.05 means you are willing to reject H₀ by mistake 5% of the time when it is actually true — this is exactly the Type I error rate. When p < α, you reject H₀ not because you have proven it false, but because the data are sufficiently inconsistent with it under your pre-agreed standard. The comparison p < α only makes sense if α was set before seeing the data; choosing α after computing p defeats the entire logic of the procedure.

One of the most durable misconceptions is treating p > 0.05 as evidence that H₀ is true. It is not. A large p-value means only that the data are not sufficiently extreme to reject H₀ at your threshold — absence of evidence is not evidence of absence. A study with a small sample may fail to reach significance not because the effect is zero but because it lacks the sensitivity to detect it. This is the distinction between failing to reject and accepting the null hypothesis.

**Statistical significance** and **practical significance** are entirely different things. A p-value can be arbitrarily small if the sample is large enough, even when the true effect is negligible in magnitude. Conversely, a practically important effect can fail significance thresholds in an underpowered study. The p-value measures how surprising the data are, not how large the effect is. Effect size measures (Cohen's d, r², odds ratio) tell you whether the effect matters in the real world. Always report both, and remember that the p-value is a statement about the evidence in your particular sample, not a permanent fact about nature.


