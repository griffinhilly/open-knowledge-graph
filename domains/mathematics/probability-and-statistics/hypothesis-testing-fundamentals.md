---
id: hypothesis-testing-fundamentals
title: Hypothesis Testing Fundamentals
domain: mathematics
course: probability-and-statistics
prerequisites:
- id: probability-axioms
  type: soft
- id: sampling-distributions
  type: hard
builds-toward:
- type-i-and-type-ii-errors
- z-test-and-t-test-for-means
tags:
- hypothesis-testing
- null-hypothesis
- alternative-hypothesis
stage: formal-systems
status: draft
---

# Hypothesis Testing Fundamentals

## Core Idea
Hypothesis testing is a method for deciding between two competing claims about a population parameter. The null hypothesis (H₀) represents the status quo or 'no effect'; the alternative hypothesis (H₁ or H_a) represents what we're testing for. A test statistic is computed from sample data, and a p-value gives the probability of observing such an extreme statistic if H₀ is true. We reject H₀ when the p-value is smaller than a predetermined significance level α (typically 0.05), but this does not prove H₀ is false—only that the data provide evidence against it.

## How It's Best Learned
Set up hypotheses for realistic scenarios. Interpret p-values correctly: probability of data given H₀, not probability H₀ is true. Distinguish statistical significance from practical significance.

## Common Misconceptions
Thinking p-value is the probability that H₀ is true. Confusing 'fail to reject' with 'accept.' Believing p < α proves the alternative is true. Forgetting that p-values measure evidence, not truth of hypotheses.

## Questions

```yaml
- question: "A researcher gets p = 0.03 with α = 0.05. What is the correct interpretation?"
  type: multiple-choice
  options: ["There is a 3% probability that H₀ is true", "There is a 3% probability that the result occurred by chance if H₀ is true", "The alternative hypothesis is 97% likely to be correct", "H₀ has been proven false"]
  answer: 1
  explanation: "The p-value is P(data this extreme or more | H₀ true). It says nothing about the probability that H₀ is true or false — that would require a Bayesian framework. Options A and C confuse the conditional direction; option D overreaches because statistical tests never prove hypotheses."

- question: "Failing to reject the null hypothesis (p > α) is equivalent to accepting the null hypothesis as true."
  type: true-false
  answer: false
  explanation: "Failing to reject H₀ means only that we did not find sufficient evidence against it — not that H₀ is true. The test may have low power (small sample, small effect size), meaning a real effect existed but the test could not detect it. 'Absence of evidence is not evidence of absence.'"

- question: "Why do statisticians choose a significance level α before collecting data, rather than after seeing the p-value?"
  type: short-answer
  answer: "Setting α in advance prevents p-hacking — the practice of adjusting the threshold after seeing the data to make a result appear significant. Pre-registration keeps the decision rule honest and ensures the false positive rate (Type I error) is controlled at the intended level."
  explanation: "If α were chosen after observing p, a researcher could always pick α just above the observed p-value to claim significance. Prespecifying α is a form of scientific discipline that separates confirmatory testing (fixed rules) from exploratory analysis."
```

## Explainer

Suppose a pharmaceutical company claims their drug reduces blood pressure. You cannot test every patient in the world, so you test a sample. Hypothesis testing gives you a principled framework for deciding whether your sample result is convincing enough to conclude the drug actually works — or whether it could just be random variation.

You start by setting up two competing claims. The **null hypothesis** (H₀) is the conservative, boring claim: "nothing is happening" — the drug has no effect, the coin is fair, the groups are identical. The **alternative hypothesis** (H₁) is what you are trying to demonstrate: "there is an effect." You never directly test H₁; instead, you ask how surprising your data would be *if H₀ were true*. This is where your knowledge of sampling distributions comes in: you know what the distribution of sample statistics looks like under H₀, so you can measure where your actual result falls.

The **p-value** is the probability of observing a test statistic at least as extreme as yours, assuming H₀ is true. A small p-value means your data are unlikely under H₀ — the evidence points against it. When the p-value falls below your pre-chosen threshold α (often 0.05), you reject H₀. Note carefully what this does and does not say: rejecting H₀ is not the same as proving H₁ is true, and a large p-value is not proof that H₀ is true — it just means you did not find enough evidence against it. The phrase is "fail to reject," not "accept."

The most persistent misconception in statistics is reading the p-value backwards: thinking p = 0.03 means "there is a 3% chance H₀ is true." That is wrong. The p-value is a probability about the *data given H₀*, not about H₀ given the data. To put probabilities on hypotheses you need Bayesian methods. What p = 0.03 actually says is: "if H₀ were true, only 3% of experiments like mine would produce results this extreme or more." That is evidence against H₀, but it is not a probability that H₀ is false.

Finally, statistical significance and practical significance are different things. With a very large sample, even a trivially small effect (a drug that lowers blood pressure by 0.001 mmHg) can yield p < 0.05. Always pair your p-value with an effect size or confidence interval to assess whether the result is meaningful in the real world, not just statistically detectable.
