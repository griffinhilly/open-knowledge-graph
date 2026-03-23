---
id: gauss-markov-theorem-ols
title: Gauss-Markov Theorem and OLS Efficiency
domain: economics
course: econometrics
prerequisites:
- id: least-squares-regression-fundamentals
  type: hard
- id: ols-assumptions
  type: hard
- id: linear-algebra
  type: soft
builds-toward:
- estimator-consistency-unbiasedness
tags:
- efficiency
- ols
- theorem
stage: advanced
status: validated
---

# Gauss-Markov Theorem and OLS Efficiency

## Core Idea
Under the Gauss-Markov assumptions (linearity, zero-mean errors, homoskedasticity, no autocorrelation, no perfect multicollinearity), OLS is the Best Linear Unbiased Estimator (BLUE)—it has the smallest variance among all linear unbiased estimators. This fundamental result justifies OLS as the primary estimation method in applied econometrics.

## Questions

```yaml
- question: "A researcher estimating a wage equation discovers the error variance is much larger for high-wage workers than for low-wage workers. Which consequence for OLS is most accurate?"
  type: multiple-choice
  options:
    - "OLS estimates are biased because the zero-mean-error assumption is violated"
    - "OLS estimates are unbiased but no longer have minimum variance among linear unbiased estimators; GLS weights observations by inverse error variance and would be more efficient"
    - "OLS estimates are inconsistent and should be replaced with instrumental variables"
    - "The results are unaffected because heteroskedasticity only matters when errors are also autocorrelated"
  answer: 1
  explanation: "Heteroskedasticity violates the homoskedasticity assumption (Var(uᵢ) = σ² for all i), but it does NOT violate exogeneity (Cov(X, u) = 0). Because exogeneity still holds, OLS remains unbiased — the expected value of the estimates still equals the true parameters. However, OLS is no longer efficient: it treats all observations equally, while GLS exploits the fact that low-variance observations contain more information per unit. GLS minimizes a weighted sum of squared residuals, giving higher weight to observations with lower error variance, and achieves strictly lower variance than OLS. Only a violation of exogeneity (option A/C logic) causes bias."

- question: "An econometrician claims to have found a nonlinear unbiased estimator with strictly lower variance than OLS under all Gauss-Markov conditions. What does this imply about the Gauss-Markov theorem?"
  type: multiple-choice
  options:
    - "It disproves the theorem — no such estimator should exist if the proof is correct"
    - "It is entirely consistent with the theorem — Gauss-Markov only guarantees OLS is best among linear unbiased estimators, and a nonlinear estimator may achieve lower variance"
    - "The estimator must be biased — the theorem guarantees OLS has minimum variance among all unbiased estimators, linear or not"
    - "This is impossible; the theorem covers all estimators regardless of their functional form"
  answer: 1
  explanation: "The 'B' in BLUE stands for 'Best among linear unbiased estimators.' This is a crucial qualifier. The theorem makes no claim that OLS beats nonlinear estimators. In fact, nonlinear estimators can often achieve lower variance — for example, if errors are non-normal, maximum likelihood estimation (a nonlinear procedure) can be strictly more efficient than OLS. The Gauss-Markov theorem is a restricted optimality result: OLS wins the race within the class of linear unbiased estimators. Students often over-read BLUE as claiming universal optimality."

- question: "Under the Gauss-Markov assumptions, OLS is the most efficient estimator among all unbiased estimators — linear or nonlinear."
  type: true-false
  answer: false
  explanation: "Gauss-Markov guarantees OLS is Best Linear Unbiased — minimum variance within the class of linear unbiased estimators only. Nonlinear unbiased estimators (such as maximum likelihood under non-normal errors) can achieve lower variance than OLS while remaining unbiased. The restriction to linear estimators is essential to the theorem's claim; without it the result does not hold."

- question: "If the exogeneity assumption fails — for instance, because a relevant variable is omitted that is correlated with an included regressor — OLS is still unbiased but loses its efficiency advantage over GLS."
  type: true-false
  answer: false
  explanation: "Endogeneity (Cov(X, u) ≠ 0) causes OLS to be biased, not merely inefficient. This is a qualitatively more serious problem than heteroskedasticity or autocorrelation, which cause inefficiency while preserving unbiasedness. When exogeneity fails, E[β̂_OLS] ≠ β — the estimator is systematically wrong in expectation, and no amount of additional data will fix this. This is why instrumental variables are needed to address endogeneity: GLS addresses inefficiency but cannot fix bias caused by correlation between regressors and errors."

- question: "The Gauss-Markov theorem says OLS is 'best' — but best in what restricted sense, and what are the boundaries of that claim?"
  type: short-answer
  answer: "OLS is Best Linear Unbiased (BLUE): it has the lowest variance among all estimators that are (1) linear functions of the observed outcome Y, and (2) unbiased (expected value equals the true parameter). The claim is bounded in two important ways. First, it applies only within the linear class — nonlinear estimators like maximum likelihood can achieve lower variance. Second, all five Gauss-Markov assumptions must hold: if homoskedasticity fails, GLS (a different linear unbiased estimator) beats OLS on variance; if exogeneity fails, OLS is not even unbiased, let alone efficient, and the theorem no longer applies at all."
  explanation: "The key is understanding BLUE as a restricted optimality claim, not an absolute one. Students often treat 'best' as universal superiority, missing that (a) the comparison class is limited to linear estimators, and (b) the result is conditional on all five assumptions holding. Each assumption plays a specific role in the proof — linearity defines the class, unbiasedness requires exogeneity, and efficiency requires homoskedasticity and no autocorrelation."
```

## Explainer

When you learned least-squares regression, you learned how OLS works mechanically — it minimizes the sum of squared residuals to find coefficients. The Gauss-Markov theorem answers a different and deeper question: *why should you use OLS?* Given that infinitely many estimators could produce an estimate of a regression coefficient, the theorem says OLS is the best among a specific class — linear and unbiased — as long as five assumptions hold.

Let's unpack what **BLUE** actually means. "Linear" means the estimator is a linear function of the observed outcomes Y. "Unbiased" means the expected value of the estimate equals the true parameter: E[β̂] = β. Many estimators are unbiased — you could just pick one observation's Y/X ratio, and on average it might equal β. But unbiased isn't enough; you also want precision. "Best" means lowest variance among all linear unbiased estimators. The Gauss-Markov theorem says OLS achieves this minimum variance — no other estimator in this class is more efficient.

The five **Gauss-Markov assumptions** are conditions on the data-generating process, not on the sample. Linearity means the true model is linear in parameters (not necessarily in variables — you can include X² and still satisfy linearity). Zero-mean errors means Cov(X, u) = 0 — errors are uncorrelated with regressors, which is the exogeneity condition. **Homoskedasticity** means all errors have the same variance: Var(uᵢ) = σ² for all i. **No autocorrelation** means Cov(uᵢ, uⱼ) = 0 for i ≠ j. No perfect multicollinearity means the regressors aren't exact linear combinations of each other. Each assumption plays a specific role in the proof — violate one and a competing estimator can beat OLS.

What happens when assumptions fail is as instructive as when they hold. If errors are **heteroskedastic** (unequal variance), OLS is still unbiased but is no longer efficient — Generalized Least Squares (GLS), which weights observations by the inverse of their error variance, produces lower-variance estimates. If errors are **autocorrelated**, the same logic applies. If the zero-mean/exogeneity assumption fails — as in simultaneous equations or omitted variable bias — OLS is not even unbiased, let alone efficient, and instrumental variables become necessary. The Gauss-Markov theorem thus serves as a diagnostic framework: identify which assumption is violated, and the right alternative estimator follows directly from that diagnosis.

