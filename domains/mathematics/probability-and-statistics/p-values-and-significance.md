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
status: validated
---

# P-values and Statistical Significance

## Core Idea
The p-value is the probability of observing data as extreme as ours (or more extreme) if H₀ were true. A result is 'statistically significant' if p < α (typically 0.05). Small p-values suggest data are inconsistent with H₀.

## How It's Best Learned
Calculate p-values for simple test statistics. Simulate null distributions to understand p-value as tail probability. Compare p-values to critical values. Recognize that significance ≠ importance.

## Common Misconceptions
Interpreting p-value as probability H₀ is true (backward; p-value is P(data|H₀)). Thinking p > 0.05 means H₀ is true. Confusing statistical significance with practical significance. Using p-value as a measure of effect size.

## Questions

```yaml
- question: "A researcher gets p = 0.03 and concludes: 'There is only a 3% chance that the null hypothesis is true.' What is wrong with this interpretation?"
  type: multiple-choice
  options:
    - "Nothing — a p-value of 0.03 is defined as the probability H₀ is true"
    - "The p-value of 0.03 means there is a 97% chance the alternative hypothesis is true"
    - "The p-value is P(data this extreme | H₀ true), not P(H₀ is true | this data)"
    - "The threshold should be 0.01 for any valid conclusion about H₀"
  answer: 2
  explanation: "This is the most common p-value misconception. The p-value conditions on H₀ being true and asks how extreme the data would be — it is P(data | H₀). To get P(H₀ | data), you would need Bayes' theorem and a prior probability for H₀, which frequentist hypothesis testing deliberately avoids. A p-value of 0.03 means: if H₀ were true, there would be a 3% chance of seeing data this extreme or more so. It says nothing directly about the probability that H₀ is true."

- question: "A study with n = 1,000,000 participants finds a statistically significant result (p < 0.001) showing that a new drug reduces blood pressure by an average of 0.1 mmHg. What is the most accurate conclusion?"
  type: multiple-choice
  options:
    - "The drug has a large, clinically meaningful effect"
    - "The study is definitive proof of the drug's effectiveness"
    - "The result is statistically significant but the effect may be too small to be clinically relevant"
    - "With p < 0.001, the null hypothesis must be false"
  answer: 2
  explanation: "With a very large sample, even a tiny effect will produce a very small p-value — statistical significance is partly a function of sample size. A 0.1 mmHg reduction in blood pressure is almost certainly clinically meaningless (normal variation in a single reading can be 10–20 mmHg). Statistical significance tells you the effect is distinguishable from zero; it says nothing about whether the effect is large enough to matter. Effect size measures (not p-values) determine practical significance."

- question: "A p-value of 0.03 means that, if the null hypothesis were true, data as extreme as observed would occur only 3% of the time."
  type: true-false
  answer: true
  explanation: "This is the correct definition of a p-value. It is the tail probability of observing data at least as extreme as what was observed, computed under the assumption that H₀ is true. A p-value of 0.03 tells you the data sit in the outer 3% of the null distribution — they are relatively unlikely under H₀, which is why small p-values prompt rejection of H₀."

- question: "A p-value of 0.40 is evidence that the null hypothesis is true."
  type: true-false
  answer: false
  explanation: "Absence of evidence is not evidence of absence. A large p-value means the data are not sufficiently extreme to reject H₀ at your chosen threshold — that is all. It does not mean H₀ is true, and it does not mean the effect is zero. A study with too small a sample may fail to achieve significance even when a real effect exists (this is low statistical power). The correct interpretation of p = 0.40 is: 'we cannot reject H₀' — not 'H₀ is confirmed.'"

- question: "Explain why a very small p-value does not necessarily imply that a research finding is practically important."
  type: short-answer
  answer: "P-values depend on both effect size and sample size. With a large enough sample, even a trivially small effect will produce an arbitrarily small p-value, because large samples reduce sampling variability and make the test very sensitive to any departure from H₀. Statistical significance just means the data are inconsistent with H₀ — it does not indicate the size or real-world relevance of the effect. Practical importance requires effect size measures (Cohen's d, r², etc.) that quantify how large the effect is, not how detectable it is."
  explanation: "The p-value answers 'is this effect detectable?' not 'is this effect large?' These are different questions. A drug that reduces blood pressure by 0.01 mmHg in a study of one million patients will produce p < 0.001, yet the drug is useless clinically. A therapy that reduces depression scores by 15 points might fail significance in a study of 10 patients, yet the effect could be enormous. Always pair p-values with effect sizes."
```

## Explainer

The **p-value** answers a very specific question: "If the null hypothesis were true, how likely would we be to see data at least as extreme as what we observed?" Notice the direction of conditioning — you are computing a probability about data, not about hypotheses. From your study of the hypothesis test framework, you know that H₀ defines a probability model. The p-value is a tail probability from that model: it measures how far out in the tail your observed test statistic sits. A p-value of 0.03 means "if H₀ were true, there would only be a 3% chance of getting data this extreme or more so." It does not mean H₀ has a 3% chance of being true.

The **significance threshold** α (usually 0.05) is a pre-set decision boundary, not a magical cutoff. Choosing α = 0.05 means you are willing to reject H₀ by mistake 5% of the time when it is actually true — this is exactly the Type I error rate. When p < α, you reject H₀ not because you have proven it false, but because the data are sufficiently inconsistent with it under your pre-agreed standard. The comparison p < α only makes sense if α was set before seeing the data; choosing α after computing p defeats the entire logic of the procedure.

One of the most durable misconceptions is treating p > 0.05 as evidence that H₀ is true. It is not. A large p-value means only that the data are not sufficiently extreme to reject H₀ at your threshold — absence of evidence is not evidence of absence. A study with a small sample may fail to reach significance not because the effect is zero but because it lacks the sensitivity to detect it. This is the distinction between failing to reject and accepting the null hypothesis.

**Statistical significance** and **practical significance** are entirely different things. A p-value can be arbitrarily small if the sample is large enough, even when the true effect is negligible in magnitude. Conversely, a practically important effect can fail significance thresholds in an underpowered study. The p-value measures how surprising the data are, not how large the effect is. Effect size measures (Cohen's d, r², odds ratio) tell you whether the effect matters in the real world. Always report both, and remember that the p-value is a statement about the evidence in your particular sample, not a permanent fact about nature.


