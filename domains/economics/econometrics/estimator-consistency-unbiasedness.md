---
id: estimator-consistency-unbiasedness
title: 'Estimator Properties: Consistency, Unbiasedness, and Efficiency'
domain: economics
course: econometrics
prerequisites:
- id: ols-assumptions
  type: hard
- id: coefficient-interpretation-regression
  type: soft
builds-toward:
- asymptotic-normality-regression
tags:
- statistical-properties
- inference
stage: formal-systems
status: validated
---

# Estimator Properties: Consistency, Unbiasedness, and Efficiency

## Core Idea
Unbiasedness means the estimator's expected value equals the true parameter; consistency means it converges to the true value as sample size grows; efficiency compares variance among unbiased estimators. OLS is unbiased under assumptions MLR 1-4 and consistent under weaker conditions, making these properties central to assessing when OLS is reliable.

## Questions

```yaml
- question: "An estimator β̂ is unbiased (E[β̂] = β) but its variance remains constant at 0.5 regardless of sample size. How should this estimator be classified?"
  type: multiple-choice
  options:
    - "Unbiased and consistent — unbiasedness guarantees that estimates are centered on the true value, which implies convergence"
    - "Consistent but biased — a fixed variance is acceptable for large-sample properties"
    - "Unbiased but inconsistent — without variance shrinking toward zero, the estimator never converges in probability to β"
    - "Efficient, since it is unbiased and has a well-defined variance"
  answer: 2
  explanation: "Unbiasedness (E[β̂] = β) and consistency (plim β̂ = β as n → ∞) are logically independent properties. Unbiasedness says estimates are centered on β on average, but says nothing about how spread out they are as n grows. Consistency requires the sampling distribution to collapse onto β — which means variance must shrink to zero. If variance stays constant at 0.5 forever, collecting more data never narrows the distribution of estimates. This is the canonical counterexample to the misconception that 'unbiased implies consistent.'"

- question: "A researcher runs OLS on a dataset where the key regressor is correlated with the error term. After collecting ten times more observations, what happens to the OLS estimate?"
  type: multiple-choice
  options:
    - "It becomes unbiased, because the larger sample reduces sampling error toward zero"
    - "It becomes more precise — the variance shrinks — but it converges toward a biased limit rather than the true parameter"
    - "It improves toward the true value because consistency holds even under endogeneity"
    - "Sample size has no effect on the estimate when endogeneity is present"
  answer: 1
  explanation: "When E[u | x] ≠ 0 (endogeneity), OLS is neither unbiased nor consistent. More data makes the estimate more precise — variance shrinks — but the estimate converges to a biased limit, not the true β. This is the crucial practical implication of inconsistency: no amount of data can fix a violation of the identifying assumption. The only solutions address the endogeneity directly (instruments, fixed effects, natural experiments). More data with a broken design gives you a very precise wrong answer."

- question: "A consistent estimator should also be unbiased, since convergence to the true value in large samples implies there is no systematic error."
  type: true-false
  answer: false
  explanation: "Consistency and unbiasedness are independent. A consistent estimator can have finite-sample bias that vanishes as n → ∞. The maximum likelihood estimator of variance (dividing by n instead of n−1) is biased in finite samples but consistent. In econometrics, OLS under contemporaneous exogeneity (E[uᵢ | xᵢ] = 0 but not strict exogeneity) is technically biased in finite samples but consistent. The bias is negligible in large samples — which is precisely what makes consistency the operative guarantee in practice."

- question: "Consistency is often considered more practically important than unbiasedness in applied econometrics because it guarantees a useful answer given enough data, while unbiasedness alone makes no such guarantee."
  type: true-false
  answer: true
  explanation: "This is the practical hierarchy in the explainer. Unbiasedness guarantees no systematic error at any sample size, which sounds strong, but if variance doesn't shrink, more data never helps — you remain permanently imprecise. Consistency guarantees convergence: with enough data, you can get as close to the true value as you want. In applied research with large samples, consistency is the operative guarantee. The worst case is inconsistency under endogeneity: collecting more data produces a precise but wrong answer that you cannot distinguish from a correct one."

- question: "In your own words, explain why consistency is often more practically valuable than unbiasedness in applied econometrics, even though unbiasedness sounds like the stronger guarantee."
  type: short-answer
  answer: "Unbiasedness means E[β̂] = β — no systematic error on average — but it says nothing about what happens as you collect more data. An unbiased estimator with non-shrinking variance stays imprecise regardless of sample size. Consistency means that as n → ∞, β̂ converges to the true β — given enough data, you recover the true value. In practice, we work with large samples where the asymptotic guarantee of consistency matters most. An unbiased but inconsistent estimator is useless at scale; a slightly biased but consistent estimator improves reliably and predictably."
  explanation: "The deeper issue is the failure mode of inconsistency: under endogeneity, OLS converges to a wrong limit. More data narrows the distribution around a biased target. No statistical technique can fix a design flaw — only a better identification strategy (instruments, randomization, fixed effects) restores consistency. This is why applied econometrics is fundamentally about identification: getting the consistency condition right is the prerequisite for any valid inference, regardless of sample size."
```

## Explainer

You already know that OLS produces estimates β̂ by minimizing the sum of squared residuals. But a single estimate from a single dataset isn't enough to evaluate an estimator — you need to ask what would happen if you drew many datasets from the same population and ran OLS on each. **Unbiasedness** is a statement about that thought experiment: if E[β̂] = β, the estimator is unbiased, meaning the estimates are centered on the true value across repeated samples. Any individual estimate may be wrong, but there's no systematic pull in one direction.

**Consistency** is a different, and in many ways more practically important, property. An estimator is consistent if it converges in probability to the true parameter as the sample size n grows without bound — written plim(β̂) = β. Think of consistency as saying: "if I had enough data, I'd eventually get the right answer." An unbiased estimator is not necessarily consistent (if its variance doesn't shrink with n), and a consistent estimator is not necessarily unbiased (it can have a small bias in finite samples that disappears asymptotically). The key OLS requirement for consistency is that regressors be contemporaneously exogenous: E[uᵢ | xᵢ] = 0. This is weaker than the full strict exogeneity assumption needed for unbiasedness (MLR 4), which is why OLS remains consistent in some settings where it's technically biased.

**Efficiency** enters when you compare estimators that are all unbiased — which one has the smallest variance? The Gauss-Markov theorem, which you've seen through the OLS assumptions, tells you that OLS is the **Best Linear Unbiased Estimator (BLUE)** under assumptions MLR 1-5. "Best" means minimum variance among all linear unbiased estimators. If errors are also normally distributed (MLR 6), OLS achieves the Cramér-Rao lower bound and is efficient even among nonlinear estimators.

The practical takeaway is a diagnostic hierarchy. When OLS assumptions hold fully, you get unbiasedness and efficiency. When strict exogeneity fails but contemporaneous exogeneity holds, you lose unbiasedness but keep consistency — estimates are wrong in small samples but correct in large ones. When even contemporaneous exogeneity fails (endogeneity), OLS is neither unbiased nor consistent, and no amount of additional data will fix the problem. This is why identifying and addressing endogeneity — through instruments, fixed effects, or natural experiments — is the central challenge of applied econometrics.
