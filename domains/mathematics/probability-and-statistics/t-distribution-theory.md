---
id: t-distribution-theory
title: 'T-Distribution: Theory and Inference'
domain: mathematics
course: probability-and-statistics
prerequisites:
- id: t-distribution
  type: soft
- id: standard-normal-z-scores-theory
  type: hard
builds-toward:
- t-test-for-means
- confidence-intervals-means
tags:
- t-distribution
stage: formal-systems
status: draft
---

# T-Distribution: Theory and Inference

## Core Idea
T(k) has heavier tails than N(0,1) and is used when population SD is unknown. Arises when replacing σ with sample s. As k→∞, T(k)→N(0,1). More conservative than z-test, reflecting additional uncertainty from estimating σ.

## Explainer

You already know the z-score: if X̄ is a sample mean drawn from a normal population with known σ, then Z = (X̄ − μ)/(σ/√n) follows a standard normal distribution. The z-score is exact. But in practice, σ is almost never known — you must estimate it from the data using the sample standard deviation s. The natural question is: what distribution does (X̄ − μ)/(s/√n) follow? The answer is the **t-distribution with k = n−1 degrees of freedom**, and understanding why requires seeing what changed when σ was replaced by s.

When you substitute s for σ, you introduce a second source of randomness. The numerator (X̄ − μ) is still random, but now the denominator (s/√n) is also random — s fluctuates across samples. The t-statistic is a ratio of a normal to a scaled **chi-squared** random variable: formally, T(k) = Z/√(χ²(k)/k) where Z ~ N(0,1) and χ²(k) is independent of Z. The chi-squared distribution in the denominator comes from the fact that (n−1)s²/σ² ~ χ²(n−1). Because you're dividing by something that itself varies, the tails of the resulting distribution are heavier than the standard normal — the occasional small values of the denominator produce large values of the ratio more often than the normal predicts.

The degrees of freedom parameter k controls exactly how heavy those tails are. With k=1 (the Cauchy distribution as a limiting case), the tails are so heavy the mean doesn't even exist. As k increases, the extra uncertainty from estimating σ matters less — after all, with a large sample, s is a very good estimate of σ and its own variability becomes negligible. This is why **T(k) → N(0,1) as k→∞**: when the denominator's randomness vanishes, the t-statistic is indistinguishable from a z-score. In practice, many textbooks treat k > 30 as "close enough to normal," though the exact boundary depends on how conservative you need to be.

The practical consequence is that **t-based inference is always more conservative than z-based inference**: t-critical values are larger than z-critical values for the same confidence level, so t-confidence intervals are wider and t-tests require more extreme statistics to reject the null. This conservatism is appropriate — you are acknowledging that you don't know σ precisely. The t-distribution is not a compromise or an approximation to something better; it is the exact correct distribution for this inferential situation, and the fact that it converges to the normal as n grows confirms that the extra conservatism gracefully disappears as the evidence accumulates.
