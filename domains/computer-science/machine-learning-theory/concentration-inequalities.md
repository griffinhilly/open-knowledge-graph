---
id: concentration-inequalities
title: Concentration Inequalities
domain: computer-science
course: machine-learning-theory
prerequisites:
- id: expected-value
  type: hard
- id: random-variables-intro
  type: hard
- id: discrete-random-variables-basics
  type: hard
tags:
- probability
- concentration
- tail-bounds
- hoeffding
stage: expert
status: validated
---

# Concentration Inequalities

## Core Idea
Concentration inequalities quantify how tightly a random variable clusters around its expected value. Unlike the central limit theorem (which gives asymptotic normality), concentration inequalities provide finite-sample, non-asymptotic tail bounds. Hoeffding's inequality bounds the deviation of a sum of bounded independent random variables: P(|mean - E[mean]| >= t) <= 2 * exp(-2nt^2) for variables in [0,1]. McDiarmid's inequality extends this to any function of independent variables with bounded differences. Bernstein's inequality tightens the bound when the variance is small. These are the workhorses of learning theory — every generalization bound, uniform convergence result, and sample complexity argument relies on concentration inequalities.

## Questions

```yaml
- question: "You want to estimate the mean of a distribution in [0,1] to within epsilon = 0.05 with probability at least 0.95 (delta = 0.05). Using Hoeffding's inequality, how many samples do you need?"
  type: multiple-choice
  options:
    - "About 200 samples — solving 2*exp(-2n*0.05^2) = 0.05 gives n = ln(40) / (2*0.0025) ≈ 738"
    - "About 738 samples — solving 2*exp(-2n*0.0025) = 0.05 gives n ≈ 738"
    - "About 50 samples — the rule of thumb is n = 1/epsilon"
    - "About 10,000 samples — Hoeffding bounds require n >= 1/epsilon^2 * 1/delta"
  answer: 1
  explanation: "Hoeffding's inequality states P(|mean - mu| >= epsilon) <= 2*exp(-2n*epsilon^2). Setting 2*exp(-2n*0.0025) <= 0.05, we get exp(-0.005n) <= 0.025, so 0.005n >= ln(40) ≈ 3.69, giving n >= 738. This is a non-asymptotic, distribution-free bound — it holds for ANY distribution on [0,1], not just Gaussians. The O(1/epsilon^2) dependence is the fundamental rate for estimating means from bounded data. Bernstein's inequality can improve this when the variance is much smaller than the range, but Hoeffding is the universal starting point."

- question: "McDiarmid's inequality applies to a function f(X_1, ..., X_n) where changing any single X_i can change f by at most c_i. Why is this more general than Hoeffding's inequality?"
  type: multiple-choice
  options:
    - "McDiarmid handles continuous random variables while Hoeffding only works for discrete ones"
    - "McDiarmid applies to any function of independent variables with bounded sensitivity, not just sums — it covers statistics like the median, maximum, or the empirical risk of a hypothesis, as long as each data point's influence is bounded"
    - "McDiarmid provides tighter bounds for all the same settings where Hoeffding applies"
    - "McDiarmid does not require independence, while Hoeffding does"
  answer: 1
  explanation: "Hoeffding's inequality bounds deviations of sums (or means) of independent bounded variables. McDiarmid's extends this to any function f(X_1, ..., X_n) satisfying the bounded differences property: changing one input changes the output by at most c_i. This covers a much wider class of statistics. For example, the empirical risk of a hypothesis is a function of n training examples, and changing one example changes the risk by at most 1/n (bounded difference c_i = 1/n). McDiarmid's gives P(|f - E[f]| >= t) <= 2*exp(-2t^2 / sum c_i^2), which reduces to Hoeffding when f is a sum. Both require independence."

- question: "Bernstein's inequality is always tighter than Hoeffding's inequality because it incorporates the variance."
  type: true-false
  answer: false
  explanation: "Bernstein's inequality is tighter when the variance sigma^2 is much smaller than the range would suggest. For a variable in [0,1], Hoeffding treats the worst case as sigma^2 = 1/4 (the maximum variance for bounded variables). If the actual variance is 0.01, Bernstein gives a much tighter bound by using sigma^2 = 0.01 instead. However, Bernstein requires knowing or bounding the variance, while Hoeffding only requires knowing the range. When the variance is close to the maximum (sigma^2 ≈ 1/4 for [0,1] variables), Bernstein offers little improvement. So Bernstein dominates Hoeffding in the small-variance regime but offers no advantage when variance is large."

- question: "Concentration inequalities are unnecessary for learning theory because the law of large numbers already guarantees that sample means converge to true means."
  type: true-false
  answer: false
  explanation: "The law of large numbers guarantees convergence in the limit (as n -> infinity) but says nothing about the rate or about finite samples. It tells you the sample mean WILL converge, not how many samples you need for a given accuracy. Learning theory requires finite-sample, quantitative bounds: 'with n = 1000 samples, the error is within 0.05 with probability 0.99.' Only concentration inequalities provide this. Furthermore, learning theory needs UNIFORM convergence (over all hypotheses), which requires even stronger tools than pointwise convergence — the Sauer-Shelah lemma combined with concentration inequalities, not just the law of large numbers."

- question: "Explain why Hoeffding's inequality, rather than the central limit theorem, is the appropriate tool for deriving sample complexity bounds in learning theory."
  type: short-answer
  answer: "The central limit theorem (CLT) says the sample mean is approximately normal for large n, but 'large n' is not quantified — the approximation quality depends on the distribution and has no universal finite-sample guarantee. Hoeffding's inequality gives an exact, non-asymptotic bound that holds for ANY sample size n and ANY distribution on bounded variables: P(|mean - mu| >= t) <= 2*exp(-2nt^2). This is essential for learning theory because: (1) we need a bound that holds for a specific, finite n, not an asymptotic regime; (2) the bound must be distribution-free (PAC learning makes no distributional assumptions); (3) we need an explicit probability bound (the delta in PAC). The CLT provides none of these. Concentration inequalities are the finite-sample, distribution-free replacement for the CLT in learning theory."
  explanation: "The CLT is an asymptotic approximation; concentration inequalities are exact finite-sample bounds. For deriving sample complexity (how many samples suffice for a given epsilon-delta guarantee), only finite-sample bounds are logically valid."
```

## Explainer

Concentration inequalities are the probabilistic engine that powers virtually every result in machine learning theory. They answer a specific question: given n independent samples, how likely is it that the sample statistic deviates from its expected value by more than a given amount? The answers they provide are non-asymptotic (valid for any n, not just large n) and distribution-free (valid for any distribution satisfying the stated conditions), making them the ideal tools for deriving PAC-style guarantees.

Hoeffding's inequality is the workhorse. If X_1, ..., X_n are independent random variables with X_i in [a_i, b_i], then P(|mean(X) - E[mean(X)]| >= t) <= 2 * exp(-2n^2t^2 / sum(b_i - a_i)^2). For variables in [0,1], this simplifies to P(|mean - mu| >= t) <= 2 * exp(-2nt^2). The bound is exponential in n — the probability of a large deviation decreases exponentially with the sample size. This exponential decay is why PAC bounds have logarithmic dependence on 1/delta: to achieve failure probability delta, you need n proportional to log(1/delta), because exp(-cn) = delta gives n = log(1/delta)/c.

McDiarmid's inequality extends Hoeffding to functions beyond simple means. If f(X_1, ..., X_n) satisfies the bounded differences property — changing any single X_i changes f by at most c_i — then P(|f - E[f]| >= t) <= 2 * exp(-2t^2 / sum c_i^2). This is directly applicable to learning theory: the empirical risk of a hypothesis h on a sample (X_1, y_1), ..., (X_n, y_n) is a function with bounded differences (changing one example changes the risk by at most 1/n), so McDiarmid gives the concentration of empirical risk around true risk. This is the foundation of generalization bounds.

Bernstein's inequality refines Hoeffding when the variance is known to be small: P(mean - mu >= t) <= exp(-nt^2 / (2(sigma^2 + t/3))). When sigma^2 << 1/4 (the maximum variance for [0,1] variables), Bernstein's bound is substantially tighter. This matters in learning theory when the best hypothesis has low error — the variance of its indicator variable is approximately p(1-p), which is small when p (the error) is small. Bernstein-based bounds give faster rates (O(1/n) instead of O(1/sqrt(n))) in the low-error regime, capturing the intuition that learning is easier when the target is nearly deterministic. Together, these three inequalities form the probabilistic toolkit that every subsequent topic in this course draws upon.
