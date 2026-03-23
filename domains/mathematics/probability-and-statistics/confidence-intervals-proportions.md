---
id: confidence-intervals-proportions
title: Confidence Intervals for Proportions
domain: mathematics
course: probability-and-statistics
prerequisites:
- id: central-limit-theorem
  type: hard
- id: binomial-distribution
  type: soft
builds-toward:
- hypothesis-testing-fundamentals
tags:
- confidence-interval
- proportion
- binomial
stage: formal-systems
status: validated
---

# Confidence Intervals for Proportions

## Core Idea
A confidence interval for a population proportion p is computed from sample proportion p̂. When the sample size is large enough that both np̂ and n(1-p̂) exceed 10, the sample proportion is approximately normal, and we can use: p̂ ± z* × √(p̂(1-p̂)/n). The margin of error decreases with larger sample size and larger confidence level. For smaller samples, exact binomial methods or continuity corrections provide better coverage.

## How It's Best Learned
Compute confidence intervals for proportions in polling contexts. Understand how sample size affects margin of error. Compare normal approximation to exact binomial.

## Common Misconceptions
Using normal approximation when np̂ or n(1-p̂) < 10. Confusing sample proportion p̂ with population proportion p. Thinking margin of error accounts for all sources of error (sampling only).

## Questions

```yaml
- question: "A poll of 400 voters finds that 52% prefer candidate A. Using z* = 1.96 for a 95% confidence interval, which is closest to the margin of error?"
  type: multiple-choice
  options:
    - "About 1%"
    - "About 2.5%"
    - "About 5%"
    - "About 10%"
  answer: 2
  explanation: "The margin of error is z* × √(p̂(1−p̂)/n) = 1.96 × √(0.52 × 0.48 / 400) = 1.96 × √(0.000624) ≈ 1.96 × 0.02498 ≈ 0.049, or about 5%. Option B (2.5%) would correspond to n = 1600, and option D (10%) to n = 100. This illustrates the key relationship: margin of error scales as 1/√n, so quadrupling n halves the margin of error."

- question: "A researcher has a confidence interval with margin of error 4% (n = 625, 95% CI). To reduce the margin of error to 2%, approximately how many observations are needed?"
  type: multiple-choice
  options:
    - "1250 — double the sample"
    - "2500 — four times the sample"
    - "3125 — five times the sample"
    - "312 — half the sample, since error is inversely proportional to n"
  answer: 1
  explanation: "Margin of error scales as 1/√n. To cut the margin of error in half (from 4% to 2%), you need to multiply n by 4: √(4n) = 2√n, so the margin halves. Starting from n = 625, the new sample size is 625 × 4 = 2500. This 1/√n relationship is one of the most practically important facts in survey statistics — halving the margin of error is expensive, requiring four times as many observations."

- question: "The margin of error for a confidence interval for a proportion is maximized (for a given sample size and confidence level) when the sample proportion p̂ = 0.5."
  type: true-false
  answer: true
  explanation: "The standard error formula is √(p̂(1−p̂)/n). The expression p̂(1−p̂) is a downward-opening parabola in p̂, maximized at p̂ = 0.5, where it equals 0.25. This means the margin of error is largest — and the estimate most uncertain — when the sample is split 50/50. Conservative sample size planning therefore assumes p̂ = 0.5 when the true proportion is unknown, ensuring the sample size is adequate regardless of the actual value."

- question: "A 95% confidence interval from this sample means there is a 95% probability that the true population proportion falls within this specific interval."
  type: true-false
  answer: false
  explanation: "This is the most common misinterpretation of confidence intervals. Once the interval is computed from your sample, the true proportion either is or is not inside it — there is no probability involved for that fixed interval. The correct interpretation is frequentist: if you repeat the sampling procedure many times and compute a 95% CI each time, about 95% of those intervals will contain the true proportion. 'Confidence' describes the procedure, not the probability of any single realized interval."

- question: "Why is the Wald interval unreliable when np̂ < 10, and what alternative should be used?"
  type: short-answer
  answer: "The Wald interval relies on the normal approximation to the binomial: for large n, p̂ is approximately normally distributed. When np̂ < 10 (or n(1−p̂) < 10), there are too few successes (or failures) for this approximation to hold — the binomial distribution is skewed, and the symmetric normal interval has poor coverage, meaning it contains the true proportion less often than the stated confidence level. The alternative is the exact Clopper-Pearson interval, which inverts the exact binomial test and has guaranteed coverage properties, at the cost of being more conservative (wider)."
  explanation: "The condition np̂ ≥ 10 and n(1−p̂) ≥ 10 is the standard check for when the normal approximation is adequate. Below this threshold, the asymmetry of the binomial distribution matters enough that symmetric normal-based intervals systematically miss the true proportion more often than advertised. This is a practical concern in clinical trials with rare events, polls about rare opinions, or any setting with extreme proportions."
```

## Explainer

A proportion is just a mean of 0s and 1s — if you code "success" as 1 and "failure" as 0, then the sample proportion p̂ = (number of successes)/n is the sample mean of those coded values. This observation connects proportions directly to everything you know from the Central Limit Theorem: for large enough n, sample means are approximately normally distributed, so p̂ is approximately normal with mean p (the true population proportion) and variance p(1−p)/n.

The **confidence interval** follows from this normal approximation. Since p̂ is approximately N(p, p(1−p)/n), standardizing gives (p̂ − p)/√(p(1−p)/n) ≈ N(0,1). Rearranging this to isolate p gives an interval centered on p̂: p̂ ± z* × √(p(1−p)/n). The catch is that the true p appears in the standard error formula, but we don't know p (that's what we're trying to estimate). The standard solution is to plug in p̂ for p in the standard error, giving the **Wald interval**: p̂ ± z* × √(p̂(1−p̂)/n). Here z* is the critical value: 1.96 for a 95% confidence level, 2.576 for 99%, and so on — values you can look up from the standard normal table.

The **margin of error** is the ± part: z* × √(p̂(1−p̂)/n). It quantifies the precision of your estimate. Notice that the margin of error shrinks as n grows (proportional to 1/√n) but increases as your confidence level increases (larger z*). To cut the margin of error in half, you need four times as many observations. The margin of error is maximized when p̂ = 0.5 (the most uncertain case), so conservative sample size calculations often assume p̂ = 0.5 when the true proportion is unknown.

The normal approximation breaks down when the sample contains very few successes or failures — specifically when np̂ < 10 or n(1−p̂) < 10. In these cases, the binomial distribution (which you know) is skewed, and the normal approximation produces intervals with poor coverage — they claim 95% but actually contain the truth less often. For small samples, the preferred alternative is the **exact binomial interval** (Clopper-Pearson), which inverts the exact binomial test rather than using a normal approximation. It is more conservative (wider) but has guaranteed coverage properties. In practice, poll results and clinical trial proportions usually have large enough samples that the Wald interval works well, but always check the condition before applying the formula.
