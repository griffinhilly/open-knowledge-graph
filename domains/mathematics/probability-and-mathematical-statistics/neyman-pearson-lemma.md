---
id: neyman-pearson-lemma
title: Neyman-Pearson Lemma
domain: mathematics
course: probability-and-mathematical-statistics
prerequisites:
- id: maximum-likelihood-estimation-theory
  type: hard
- id: type-i-and-type-ii-errors
  type: soft
builds-toward:
- likelihood-ratio-tests
- uniformly-most-powerful-tests
tags:
- neyman-pearson
- hypothesis-testing
- statistics
stage: advanced
status: validated
---

# Neyman-Pearson Lemma

## Core Idea
For testing H₀: θ = θ₀ vs H₁: θ = θ₁, the most powerful test rejects H₀ when L(θ₁|X)/L(θ₀|X) > k for some k determined by the significance level. The Neyman-Pearson lemma characterizes the optimal test in terms of likelihood ratios. This is the foundation for constructing best hypothesis tests.

## Questions

```yaml
- question: "Two analysts both test H₀: μ = 0 vs H₁: μ = 5 at α = 0.05. Analyst A uses the likelihood ratio test. Analyst B invents a different test that also maintains exactly 5% false positives. Which test has higher power?"
  type: multiple-choice
  options:
    - "Analyst B's test — novel approaches can outperform classical methods"
    - "Analyst A's test — the Neyman-Pearson lemma guarantees no test of size α can have higher power"
    - "They are equally powerful, since both maintain α = 0.05"
    - "It depends on the sample size — the lemma only applies asymptotically"
  answer: 1
  explanation: "The Neyman-Pearson lemma is not a rule of thumb — it is a proof. Among all tests that keep Type I error at exactly α, the likelihood ratio test is most powerful: it minimizes Type II error (maximizes the probability of correctly rejecting H₀ when H₁ is true). No other test of the same size can do better. Analyst B's test is either equivalent to the LR test in its rejection region or strictly less powerful."

- question: "When testing H₀: p = 0.5 vs H₁: p = 0.7 in n = 10 coin flips, the Neyman-Pearson optimal rejection region is 'reject when the number of heads k ≥ c.' Why does this follow from the likelihood ratio?"
  type: multiple-choice
  options:
    - "The sample mean is always the optimal test statistic for binomial hypotheses"
    - "The likelihood ratio L(0.7|k)/L(0.5|k) is a monotonically increasing function of k, so large k is the strongest evidence for H₁"
    - "Head counts are sufficient statistics, and sufficient statistics always define optimal rejection regions"
    - "The p-value formula for binomial tests is defined in terms of head counts by convention"
  answer: 1
  explanation: "The likelihood ratio L(0.7|k)/L(0.5|k) = (0.7/0.5)^k · (0.3/0.5)^(10−k) increases as k increases — more heads make H₁ more plausible relative to H₀. The NP lemma says to reject when this ratio exceeds threshold k, which here reduces to rejecting when the head count exceeds some critical value c. The optimal test statistic and rejection region emerge naturally from maximizing the likelihood ratio, not from convention."

- question: "The Neyman-Pearson lemma applies only to simple vs. simple hypothesis tests where both H₀ and H₁ specify a single parameter value."
  type: true-false
  answer: true
  explanation: "The basic NP lemma is stated for simple hypotheses: H₀: θ = θ₀ vs H₁: θ = θ₁. The extension to composite alternatives — where H₁ covers a range of values — leads to the concept of Uniformly Most Powerful (UMP) tests, which are most powerful against every value in the alternative simultaneously. Not all testing problems admit a UMP test. Understanding the NP lemma as the simple-case foundation is essential before extending it."

- question: "Reducing the significance level α (from 0.05 to 0.01, say) while keeping everything else constant will increase the power of a Neyman-Pearson test."
  type: true-false
  answer: false
  explanation: "Power and significance level are in fundamental tension. Reducing α tightens the rejection region — you require stronger evidence to reject H₀. This means you will correctly detect H₁ less often: Type II error increases and power decreases. The Neyman-Pearson framework makes this tradeoff explicit: fixing α is the constraint, and the lemma maximizes power *given* that constraint. You cannot decrease α and increase power simultaneously without additional information (such as a larger sample)."

- question: "Why is the likelihood ratio — rather than some other function of the data — the key quantity in the Neyman-Pearson lemma?"
  type: short-answer
  answer: "The likelihood ratio L(θ₁|X)/L(θ₀|X) directly measures how much better the data supports H₁ compared to H₀. Rejecting H₀ when this ratio is large concentrates the rejection region on exactly those outcomes most consistent with H₁, maximizing the probability of correct rejection while using the full α budget of Type I error. Any other rejection region would either miss some of the most H₁-consistent outcomes or include some H₀-consistent ones."
  explanation: "The likelihood ratio is the sufficient statistic for the binary comparison between two simple hypotheses — it captures everything in the data relevant to distinguishing θ₀ from θ₁. Ranking outcomes by their likelihood ratio gives the ordering that maximizes power: the outcomes most likely under H₁ relative to H₀ should be rejected first. The NP lemma formalizes this intuition into a proof of optimality."
```

## Explainer

From your study of Type I and Type II errors, you know there is a fundamental tradeoff: any test that reduces false positives (Type I errors, controlled by significance level α) tends to increase false negatives (Type II errors). The question the Neyman-Pearson lemma answers is: *given* that you've fixed α, what is the most powerful test — the one that minimizes Type II errors, or equivalently maximizes the probability of correctly rejecting H₀ when H₁ is true?

The answer hinges on the **likelihood ratio**. You know from maximum likelihood estimation that L(θ | X) measures how well parameter θ explains the data X. The ratio L(θ₁ | X) / L(θ₀ | X) compares how much better the data supports H₁ versus H₀. When this ratio is large, the data is much more consistent with H₁ — strong evidence to reject H₀. The lemma says: reject when this ratio exceeds some threshold k, where k is chosen to make the Type I error exactly α. This is the **Neyman-Pearson test**, and the lemma proves it is **most powerful** among all tests of size α.

A concrete example: testing whether a coin is fair (H₀: p = 0.5) versus biased (H₁: p = 0.7) after n = 10 flips. If you observe k heads, L(0.7 | k) / L(0.5 | k) = (0.7/0.5)^k · (0.3/0.5)^(10−k). This ratio increases in k — more heads is stronger evidence for p = 0.7. The NP test rejects when k ≥ c for some critical value c. Note the structure: the optimal rejection region is simply "enough heads" — the test statistic is just the number of heads, a natural sufficient statistic. This connection between NP tests and sufficient statistics is deep and recurring.

The lemma's importance extends beyond the simple case. For **simple vs. simple** hypotheses (both θ₀ and θ₁ are single values), NP gives the uniquely optimal test. For composite hypotheses (θ₁ ranges over a set), this extends to the concept of **Uniformly Most Powerful** (UMP) tests — tests that are simultaneously most powerful against every value in the alternative. Not all testing problems admit a UMP test, but when they do, the NP framework reveals why. Understanding the NP lemma is therefore not just about one test; it is the benchmark that defines what "optimal" means in hypothesis testing and anchors all subsequent developments in the theory.
