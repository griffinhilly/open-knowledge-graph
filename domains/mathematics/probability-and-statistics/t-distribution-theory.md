---
id: t-distribution-theory
title: 'T-Distribution: Theory and Inference'
domain: mathematics
course: probability-and-statistics
prerequisites:
- id: standard-normal-z-scores-theory
  type: hard
builds-toward:
- t-test-for-means
- confidence-intervals-means
tags:
- t-distribution
stage: formal-systems
status: validated
---

# T-Distribution: Theory and Inference

## Core Idea
T(k) has heavier tails than N(0,1) and is used when population SD is unknown. Arises when replacing σ with sample s. As k→∞, T(k)→N(0,1). More conservative than z-test, reflecting additional uncertainty from estimating σ.

## Questions

```yaml
- question: "Why does the t-distribution have heavier tails than the standard normal distribution?"
  type: multiple-choice
  options:
    - "The t-distribution uses a smaller sample size, so each observation has more influence"
    - "Replacing σ with the sample standard deviation s introduces a second source of randomness in the denominator, making extreme values of the ratio more likely"
    - "The t-distribution is designed to be more conservative by artificially inflating the variance"
    - "The t-distribution uses degrees of freedom instead of a fixed variance, which spreads the distribution out"
  answer: 1
  explanation: "The z-score (X̄ − μ)/(σ/√n) has a random numerator and a fixed denominator (σ is known). The t-statistic (X̄ − μ)/(s/√n) has a random numerator AND a random denominator (s fluctuates across samples). When the denominator occasionally takes small values, the ratio can be very large. This extra variability in the denominator, which follows a chi-squared distribution scaled by σ², pushes probability mass into the tails. Option D gestures toward the right idea but 'degrees of freedom replacing fixed variance' is not quite the mechanism."

- question: "A researcher tests a hypothesis about a population mean. The population is normally distributed, but σ is unknown and n = 15. Which test statistic is appropriate?"
  type: multiple-choice
  options:
    - "Z, because the population is normally distributed"
    - "Z, because n = 15 is large enough to invoke the central limit theorem"
    - "T with 14 degrees of freedom, because σ must be estimated from the sample"
    - "T with 15 degrees of freedom, because the sample size determines the degrees of freedom"
  answer: 2
  explanation: "The t-statistic is required whenever σ is unknown and must be estimated by s — regardless of whether the population is normal. The degrees of freedom equal n − 1 = 14, not n, because estimating s from the data uses up one degree of freedom (the sample mean is subtracted in the calculation of s). Option A is the common misconception: normality of the population allows exact t-inference, but doesn't let you use z when σ is unknown. Option B is wrong: the CLT approximation might justify z for large samples, but n = 15 is not large."

- question: "A 95% confidence interval for a mean constructed with the t-distribution will always be wider than one constructed with the z-distribution using the same data."
  type: true-false
  answer: true
  explanation: "T-critical values are always larger than the corresponding z-critical values (for example, t* ≈ 2.145 vs z* ≈ 1.96 for 95% confidence with 14 df). Since the interval half-width is critical value × standard error, a wider critical value produces a wider interval. This conservatism is appropriate: it reflects the added uncertainty from estimating σ. As degrees of freedom grow, t* → z*, and the intervals converge — reflecting that s becomes an increasingly reliable estimate of σ with larger samples."

- question: "When the sample size is large enough, the t-distribution becomes indistinguishable from the standard normal, so there is no practical reason to use t over z for large samples."
  type: true-false
  answer: false
  explanation: "While T(k) → N(0,1) as k → ∞, and the two are indeed very close for large k, there is a principled reason to prefer t: it is the exact correct distribution when σ is estimated, at any sample size. Using z when σ is unknown underclaims uncertainty, producing slightly anti-conservative (narrow) intervals and slightly liberal hypothesis tests. The t-distribution is not an approximation that happens to converge — it is the exact sampling distribution of the standardized mean when σ is replaced by s."

- question: "Why does replacing the known population standard deviation σ with the sample standard deviation s require switching from the z-distribution to the t-distribution?"
  type: short-answer
  answer: "When σ is known, the denominator σ/√n is a fixed constant, so the only randomness in the z-statistic comes from the numerator X̄. When σ is replaced by s, the denominator s/√n is itself a random variable that fluctuates across samples. This second source of randomness means the ratio no longer follows a standard normal distribution. Instead, it follows a t-distribution, which formally arises as the ratio of a standard normal to the square root of an independent chi-squared variable divided by its degrees of freedom."
  explanation: "The chi-squared connection comes from the fact that (n−1)s²/σ² ~ χ²(n−1). The extra randomness in the denominator inflates the tails relative to the normal. As n grows, s converges to σ and its own variability shrinks — the extra randomness in the denominator vanishes, which is why t → z as the degrees of freedom grow. The t-distribution is the honest acknowledgment that estimating σ carries a cost in inferential precision."
```

## Explainer

You already know the z-score: if X̄ is a sample mean drawn from a normal population with known σ, then Z = (X̄ − μ)/(σ/√n) follows a standard normal distribution. The z-score is exact. But in practice, σ is almost never known — you must estimate it from the data using the sample standard deviation s. The natural question is: what distribution does (X̄ − μ)/(s/√n) follow? The answer is the **t-distribution with k = n−1 degrees of freedom**, and understanding why requires seeing what changed when σ was replaced by s.

When you substitute s for σ, you introduce a second source of randomness. The numerator (X̄ − μ) is still random, but now the denominator (s/√n) is also random — s fluctuates across samples. The t-statistic is a ratio of a normal to a scaled **chi-squared** random variable: formally, T(k) = Z/√(χ²(k)/k) where Z ~ N(0,1) and χ²(k) is independent of Z. The chi-squared distribution in the denominator comes from the fact that (n−1)s²/σ² ~ χ²(n−1). Because you're dividing by something that itself varies, the tails of the resulting distribution are heavier than the standard normal — the occasional small values of the denominator produce large values of the ratio more often than the normal predicts.

The degrees of freedom parameter k controls exactly how heavy those tails are. With k=1 (the Cauchy distribution as a limiting case), the tails are so heavy the mean doesn't even exist. As k increases, the extra uncertainty from estimating σ matters less — after all, with a large sample, s is a very good estimate of σ and its own variability becomes negligible. This is why **T(k) → N(0,1) as k→∞**: when the denominator's randomness vanishes, the t-statistic is indistinguishable from a z-score. In practice, many textbooks treat k > 30 as "close enough to normal," though the exact boundary depends on how conservative you need to be.

The practical consequence is that **t-based inference is always more conservative than z-based inference**: t-critical values are larger than z-critical values for the same confidence level, so t-confidence intervals are wider and t-tests require more extreme statistics to reject the null. This conservatism is appropriate — you are acknowledging that you don't know σ precisely. The t-distribution is not a compromise or an approximation to something better; it is the exact correct distribution for this inferential situation, and the fact that it converges to the normal as n grows confirms that the extra conservatism gracefully disappears as the evidence accumulates.
