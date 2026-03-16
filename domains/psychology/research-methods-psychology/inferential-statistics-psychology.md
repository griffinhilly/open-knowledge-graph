---
id: inferential-statistics-psychology
title: Inferential Statistics in Psychology
domain: psychology
course: research-methods-psychology
prerequisites:
- id: research-hypothesis-formation
  type: hard
- id: sampling-in-psychology
  type: hard
- id: hypothesis-testing-fundamentals
  type: soft
- id: p-values-and-significance
  type: soft
- id: normal-distribution-intro
  type: soft
- id: t-test-for-means
  type: soft
- id: confidence-intervals-means
  type: soft
- id: correlational-research-design
  type: soft
- id: measurement-scales-psychology
  type: soft
- id: random-assignment
  type: soft
- id: validity-in-measurement
  type: soft
- id: confidence-intervals-framework
  type: soft
- id: hypothesis-testing-framework
  type: hard
builds-toward:
- effect-size-and-power
- replication-and-open-science
tags:
- inferential-statistics
- t-test
- ANOVA
- significance
- p-value
stage: abstract-reasoning
status: validated
---
# Inferential Statistics in Psychology

## Core Idea
Inferential statistics allow researchers to draw conclusions about populations from sample data and to decide whether observed effects are likely due to chance. Core tools include t-tests (comparing two means), ANOVA (comparing three or more means), and chi-square tests (categorical data). The p-value expresses the probability of obtaining results at least as extreme as observed, assuming the null hypothesis is true. A p-value below the significance threshold (typically .05) justifies rejecting the null, though this threshold is arbitrary and widely misunderstood.

## How It's Best Learned
Run a t-test on a small dataset by hand to understand what the test statistic represents. Then use software to analyze a larger dataset and interpret the full output, including confidence intervals.

## Common Misconceptions
- A p-value is not the probability that the null hypothesis is true, nor the probability that the result is due to chance.
- Statistical significance does not imply practical importance — a trivially small effect can be statistically significant with a large enough sample.

## Questions

```yaml
- question: "A researcher finds p = .03 for the effect of a memory training program. Which interpretation is correct?"
  type: multiple-choice
  options: ["There is a 3% probability that the null hypothesis is true", "There is a 97% probability that the training program works", "If the null hypothesis were true, the probability of observing results this extreme or more extreme is 3%", "The training program explains 3% of the variance in memory scores"]
  answer: 2
  explanation: "The p-value is defined as the probability of observing data at least as extreme as the obtained results, *assuming the null hypothesis is true*. It does not tell you the probability that the null is true, the probability the result is a fluke, or the size of the effect. Options A and B describe the 'inverse probability fallacy' — confusing P(data | null) with P(null | data). Option D describes r², a measure of effect size, not a p-value."

- question: "A statistically significant result (p < .05) means the effect is large enough to matter in practical or clinical terms."
  type: true-false
  answer: false
  explanation: "Statistical significance depends on three things: effect size, sample size, and variability. With a large enough sample, even a trivially small effect — one too small to be practically meaningful — will produce p < .05. For example, a study of 50,000 participants might find a statistically significant difference of 0.2 points on a 100-point scale. 'Significant' in statistics means 'unlikely to be due to chance,' not 'important.' Effect size measures (Cohen's d, r², η²) are needed to evaluate practical importance."

- question: "What is the difference between a Type I error and a Type II error in hypothesis testing, and which one does the .05 significance threshold directly control?"
  type: short-answer
  answer: "A Type I error is rejecting the null hypothesis when it is actually true (a false positive). A Type II error is failing to reject the null when it is actually false (a false negative). The .05 significance threshold (α) directly controls the Type I error rate — by setting α = .05, researchers accept a 5% chance of falsely rejecting a true null hypothesis. Type II error rate (β) is controlled separately through study design, primarily by ensuring adequate statistical power (1 - β), which depends on sample size."
  explanation: "This distinction matters because researchers face a trade-off: lowering α to reduce false positives (e.g., α = .01) simultaneously increases the Type II error rate unless sample size is increased. The choice of α = .05 is a convention, not a law of nature — in some fields (particle physics, clinical trials with serious consequences) much stricter thresholds are used. Understanding that the .05 threshold controls only one type of error helps researchers design studies with appropriate power rather than just aiming for p < .05."
```

## Explainer

From your study of hypothesis testing, you know the basic logic: state a null hypothesis (typically that there is no effect), collect data, compute a test statistic, and decide whether the data are surprising enough under the null to reject it. Inferential statistics in psychology applies this framework to real research questions — comparing group means, testing correlations, examining categorical relationships — and introduces the specific tools psychologists use most often.

The three workhorses of inferential statistics in psychology are the **t-test**, **ANOVA**, and the **chi-square test**. The t-test compares two means: is the average memory score in the trained group higher than in the control group, beyond what chance variation would produce? It does this by computing how many standard errors apart the two sample means are. If that distance is large relative to what you'd expect by chance (under the null), you reject the null. ANOVA (Analysis of Variance) extends the same logic to three or more groups — comparing a control, low-dose, and high-dose condition, for example — while controlling the Type I error rate that would inflate if you ran multiple t-tests. The chi-square test addresses categorical outcomes: are observed frequencies of categories (e.g., recovery vs. no recovery across treatment groups) different from what chance predicts?

The **p-value** is the most used and most misunderstood number in psychological research. Its correct definition: the probability of observing data at least as extreme as what you got, *assuming the null hypothesis is true*. This is a conditional probability — P(data | null) — not P(null | data). Psychologists routinely confuse the two, interpreting p = .03 as "there's only a 3% chance the null is true," which is wrong. The p-value says nothing about the probability the null is true; that requires prior probabilities the frequentist framework does not provide. What p = .03 does tell you: if the null were true, results this extreme would occur only 3% of the time by chance.

The significance threshold of **.05** is a convention established by Ronald Fisher in the 1920s and widely adopted in psychology. Setting α = .05 means you accept a 5% risk of rejecting a true null hypothesis (a Type I error, or false positive). Crucially, the .05 threshold says nothing about Type II errors (false negatives — missing a real effect). Controlling Type II errors requires adequate **statistical power**, which depends primarily on sample size. A study with 20 participants may have only 40% power to detect a medium-sized effect, meaning it will miss that effect 60% of the time.

The most important practical lesson: **statistical significance is not practical importance**. Because significance depends on sample size, a study with 50,000 participants can achieve p < .001 for an effect so small it has no real-world consequence. Effect size measures — Cohen's d for mean differences, r² for correlations, η² for ANOVA — quantify the *magnitude* of an effect independently of sample size. A complete inferential report includes both a p-value and an effect size. The growing replication crisis in psychology has made this point urgent: many published findings with p < .05 have failed to replicate, partly because small samples combined with flexible analysis choices artificially inflated apparent significance.
