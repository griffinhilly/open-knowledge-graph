---
id: normal-distribution
title: Normal Distribution
domain: mathematics
course: probability-and-statistics
prerequisites:
- id: continuous-random-variables
  type: hard
- id: expected-value-and-variance
  type: soft
- id: bivariate-normal-distribution
  type: soft
builds-toward:
- standard-normal-and-z-scores
- central-limit-theorem
- confidence-intervals-means
tags:
- normal
- gaussian
- bell-curve
stage: formal-systems
status: validated
---
# Normal Distribution

## Core Idea
The normal distribution with mean μ and standard deviation σ has PDF f(x) = (1/(σ√(2π))) × e^(-(x-μ)²/(2σ²)). It is symmetric, bell-shaped, and completely determined by its mean and variance. The normal distribution is ubiquitous in statistics because many naturally occurring phenomena approximate it, and because of the central limit theorem, which states that means of large samples are approximately normal regardless of the original distribution.

## How It's Best Learned
Visualize how mean shifts and standard deviation stretches the bell curve. Use the empirical rule (68-95-99.7). Compare distributions with different μ and σ.

## Common Misconceptions
Assuming all bell-shaped distributions are normal. Thinking the normal distribution can be negative (values are on ℝ, but probabilities decay in tails). Confusing standard deviation with variance.

## Questions

```yaml
- question: "A normal distribution has μ = 100 and σ = 15. Approximately what percentage of values fall between 85 and 115?"
  type: multiple-choice
  options: ["50%", "68%", "95%", "99.7%"]
  answer: 1
  explanation: "85 and 115 are each exactly one standard deviation from the mean (μ ± σ = 100 ± 15). The empirical rule states that approximately 68% of values in a normal distribution fall within one standard deviation of the mean. 95% falls within two, and 99.7% within three."

- question: "Any distribution that looks bell-shaped is a normal distribution."
  type: true-false
  answer: false
  explanation: "Many distributions are bell-shaped but not technically normal. For example, t-distributions are symmetric and bell-shaped but have heavier tails than the normal. A distribution is normal only if it follows the specific exponential formula f(x) = (1/(σ√(2π))) × e^(-(x-μ)²/(2σ²)). Visual resemblance to a bell curve is not sufficient."

- question: "How do the mean and standard deviation together completely determine the shape of a normal distribution?"
  type: short-answer
  answer: "The mean sets the center (location) of the bell curve, while the standard deviation sets its width — larger σ produces a flatter, wider curve and smaller σ produces a taller, narrower one. No other parameters are needed."
  explanation: "Unlike many distributions that require additional shape parameters, the normal distribution is fully specified by just μ and σ. This is one of the reasons it is mathematically tractable and widely used — every normal distribution is just a shifted and scaled version of the standard normal (μ=0, σ=1)."
```

## Explainer

You have already encountered the idea of a continuous random variable — a quantity that can take any value in an interval, described by a probability density function (PDF). The normal distribution is the most important continuous distribution in all of statistics, and understanding why requires looking at both its shape and its origins.

The normal distribution is symmetric and bell-shaped, centered at its mean μ. The spread is controlled by the standard deviation σ: a small σ produces a tall, narrow bell, while a large σ produces a short, wide one. The mean and standard deviation are all you need to specify a normal distribution completely — there are no additional shape parameters. This makes it unusually tractable mathematically.

A practical rule that makes normals easy to reason about is the **empirical rule**: approximately 68% of values fall within one standard deviation of the mean (μ ± σ), about 95% within two, and about 99.7% within three. This rule is worth memorizing because it lets you quickly answer questions like "how unusual is a value 2 standard deviations above average?" without computing integrals. (Answer: only about 2.5% of values are that far above the mean.)

One of the most common misconceptions is treating any bell-shaped distribution as normal. The t-distribution, for instance, is also symmetric and peaked in the middle, but its tails are heavier — extreme values are more likely than the normal predicts. The normal is defined by a specific mathematical formula, not just by its visual shape. That said, the normal is ubiquitous because of the **central limit theorem** (a topic you will encounter soon), which says that the average of a large number of independent random variables is approximately normally distributed, regardless of the original distribution. This is why so many real-world measurements — heights, measurement errors, test scores — approximate the normal.

When you see a normal distribution, always read off μ and σ first. They tell you where the bulk of the data sits and how spread out it is. A score of 130 on a test with μ = 100, σ = 15 is two standard deviations above average — notable but not extraordinary (about 2.3% of people score this high). The same score on a test with μ = 100, σ = 5 would be six standard deviations above average — effectively impossible in a true normal. The same number means very different things depending on the distribution's parameters.
