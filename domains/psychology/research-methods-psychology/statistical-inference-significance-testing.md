---
id: statistical-inference-significance-testing
title: Inferential Statistics, Hypothesis Testing, and P-Values
domain: psychology
course: research-methods-psychology
prerequisites:
- id: descriptive-analysis-visualization-summary
  type: hard
- id: statistical-power-and-effect-size-determination
  type: hard
- id: t-distribution-theory
  type: soft
- id: hypothesis-test-framework
  type: hard
- id: central-limit-theorem-rigorous
  type: hard
- id: exploratory-vs-confirmatory-analysis-strategies
  type: soft
builds-toward:
- effect-size-practical-significance-reporting
tags:
- hypothesis-testing
- p-values
- statistical-inference
- significance
stage: advanced
status: validated
---
# Inferential Statistics, Hypothesis Testing, and P-Values

## Core Idea
Hypothesis testing infers whether sample evidence supports a hypothesis about the population. The p-value is the probability of observing the sample statistic (or more extreme) if the null hypothesis is true. Alpha (e.g., 0.05) is the maximum acceptable false-positive rate. Statistical significance indicates the result is unlikely under the null; it does not indicate magnitude or importance.

## How It's Best Learned
Interpret p-values and null hypothesis significance tests from published papers. Conduct NHST on a real dataset and report both p and effect size. Discuss the logic and limitations of NHST and alternatives (e.g., Bayesian inference).

## Common Misconceptions
- P < 0.05 proves the hypothesis is true; - Non-significant results are non-findings; - P-values directly measure effect size; - Repeated sampling with p-hacking is acceptable if the hypothesis is 'right'.

## Questions

```yaml
- question: "A pharmaceutical study with 100,000 participants finds that a supplement increases memory test scores by 0.3 points (on a 100-point scale) with p = 0.0001. What is the most accurate interpretation?"
  type: multiple-choice
  options:
    - "The supplement is highly effective — the tiny p-value confirms a strong, practically meaningful benefit"
    - "The result is statistically significant but the effect size is negligible — statistical significance does not establish practical importance"
    - "The p-value of 0.0001 means there is a 0.01% chance the null hypothesis is true"
    - "The result is conclusive because p < 0.05 proves the hypothesis correct"
  answer: 1
  explanation: "Statistical significance and practical importance are entirely separate. With 100,000 participants, even a trivially small effect (0.3 points on a 100-point scale) produces a very small p-value because large samples detect tiny deviations from the null. The p-value only tells you how surprising the result would be if H₀ were true — it says nothing about the size or real-world relevance of the effect. Always report and interpret effect sizes alongside p-values."

- question: "A researcher reports p = 0.03 for a hypothesis test. A journalist writes: 'There is only a 3% chance this result occurred by chance.' What is wrong with this statement?"
  type: multiple-choice
  options:
    - "Nothing — that is exactly what a p-value of 0.03 means"
    - "The journalist should have said 5%, not 3%, since alpha is the relevant threshold"
    - "The p-value is P(data this extreme | H₀ is true), not P(H₀ is true | this data) — the journalist has reversed the conditional probability"
    - "The statement is wrong because p-values cannot be expressed as percentages"
  answer: 2
  explanation: "This is the most common p-value misinterpretation. P = 0.03 means: if the null hypothesis were true, you would see results this extreme or more extreme 3% of the time by chance. It does NOT give the probability that H₀ is true — that requires Bayes' theorem and a prior. The conditional has been reversed: P(data | H₀) ≠ P(H₀ | data)."

- question: "A study that fails to reach p < 0.05 has proven that the effect being studied does not exist."
  type: true-false
  answer: false
  explanation: "Failing to reject H₀ is not the same as accepting H₀. A non-significant result may simply reflect low statistical power — the study may have been too small to detect a real effect. This is the difference between 'evidence of absence' and 'absence of evidence.' A null result is informative only when the study had adequate power to detect an effect of the size that would matter practically."

- question: "Two studies on the same research question can both report p = 0.04 while detecting very different-sized effects."
  type: true-false
  answer: true
  explanation: "The p-value depends on both effect size and sample size. A study with tens of thousands of participants can yield p = 0.04 for a negligible correlation (r = 0.02), while a smaller study yields p = 0.04 for a large effect (r = 0.35). The p-value conflates effect size and sample size into a single threshold crossing — which is precisely why reporting effect sizes (Cohen's d, r, η²) alongside p-values is essential."

- question: "Why is it incorrect to define the p-value as 'the probability that the null hypothesis is true'?"
  type: short-answer
  answer: "The p-value is computed assuming the null hypothesis is true — it is P(data this extreme | H₀). To find P(H₀ | data), you would need Bayes' theorem, which requires a prior probability for H₀. The p-value conditions on H₀ being true; reversing this conditional to ask about P(H₀) requires additional assumptions the NHST framework does not provide."
  explanation: "This distinction has real consequences. Researchers who believe p = 0.05 means H₀ has a 5% chance of being true will systematically overstate their confidence. The correct interpretation demands acknowledging that a significant p-value is compatible with H₀ being true (you could be in the 5% false-positive zone), and a non-significant result is compatible with H₁ being true (you may simply lack power)."
```

## Explainer

You know from the central limit theorem that with a large enough sample, the sampling distribution of the mean is approximately normal regardless of the population distribution. You know from the hypothesis test framework that we set up a null hypothesis (H₀), compute a test statistic, and make a decision. Inferential statistics in psychology operationalizes that framework through the machinery of **null hypothesis significance testing (NHST)** — a procedure for deciding whether to reject H₀ based on sample data, with a controlled probability of being wrong.

The **p-value** is the single most misunderstood quantity in social science. Here is its precise definition: the probability of observing a test statistic at least as extreme as the one you got, *assuming the null hypothesis is true*. P = 0.03 means that if the null were true, you would see a result this extreme or more extreme only 3% of the time by chance. That's it. It does not tell you the probability that H₀ is true. It does not tell you the probability that your result will replicate. It does not tell you the size of the effect. It is a single conditional probability about the data given H₀, and that conditional is easy to flip incorrectly. Saying "there is a 3% chance this result is due to chance" reverses the condition; it would require Bayesian reasoning and a prior on H₀ to compute that probability.

The **alpha level** (α) is your pre-specified threshold for this conditional probability below which you will reject H₀. Setting α = 0.05 means you accept a 5% false-positive rate (Type I error) — you will reject H₀ 5% of the time when it is actually true, in the long run across many studies. This is not a guarantee about any single study. When you reject H₀, you have not proven that H₁ is true; you have shown that the data are unlikely if H₀ were true. Statistical significance and practical importance are entirely separate: a study with 100,000 participants can produce p < 0.0001 for a correlation of r = 0.02, which is statistically significant but explains only 0.04% of the variance. **Effect size** (Cohen's *d*, *r*, *η²*, etc.) is the quantity that measures practical importance — always report it alongside the *p*-value.

Power, which you studied in the prerequisite, connects back here in an important way. **Statistical power** is the probability of correctly rejecting H₀ when H₁ is true — the complement of the Type II error rate (β). Low-powered studies, which are endemic in psychology, have two failure modes: they often miss real effects (false negatives), and when they do find significant results, those results are systematically inflated. This second point — called the **winner's curse** — is counterintuitive but follows from the mathematics: in a low-powered study, the only time you cross the significance threshold is when the estimated effect is large enough by luck, which means your effect size estimate is biased upward. This is one of the structural causes of the replication crisis in psychology. The remedy is not to abandon NHST but to use it correctly: plan sample sizes for adequate power, pre-register hypotheses, report effect sizes and confidence intervals, and treat any single significant p-value as one piece of evidence rather than a definitive conclusion.
