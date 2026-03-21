---
id: generalized-method-of-moments
title: Generalized Method of Moments (GMM)
domain: economics
course: econometrics
prerequisites:
- id: maximum-likelihood-econometrics
  type: soft
- id: instrumental-variables
  type: hard
- id: probability-theory
  type: hard
- id: linear-algebra
  type: hard
- id: expected-value-theory
  type: soft
builds-toward:
- dynamic-panel-arellano-bond-estimator
tags:
- estimation
- gmm
- moment-conditions
stage: advanced
status: draft
---

# Generalized Method of Moments (GMM)

## Core Idea
GMM exploits moment conditions E[f(Yᵢ, θ)] = 0 to estimate θ by minimizing a quadratic form in sample moments. It generalizes OLS, IV, and MLE; yields efficient estimators when moment conditions are correctly specified. The Hansen J-test checks overidentification.

## Questions

```yaml
- question: "A researcher estimates a model with 3 parameters using 3 moment conditions (just-identified). She then discovers 2 additional valid instruments, giving her 5 moment conditions. What is the correct next step to improve efficiency?"
  type: multiple-choice
  options:
    - "Discard the extra instruments — additional moment conditions do not improve GMM estimates"
    - "Use the additional moments with an initial weighting matrix, then re-estimate using the inverse variance of the moments as the optimal weighting matrix"
    - "Switch to OLS, which is always more efficient than GMM with more than k moment conditions"
    - "Use the identity matrix as the permanent weighting matrix, since it treats all moments equally and avoids estimation error in W"
  answer: 1
  explanation: "Additional valid moment conditions contain information that can improve efficiency. The two-step procedure implements this: (1) estimate with an initial (e.g., identity) weighting matrix to get a consistent θ̂; (2) compute the sample variance of the moment conditions at θ̂; (3) invert it to form the optimal W; (4) re-estimate. The optimal W downweights noisy moments and upweights precisely estimated ones. Discarding valid instruments throws away information; the identity matrix is suboptimal unless moments happen to have equal variance."

- question: "A researcher estimates a dynamic panel model using two-step GMM with 12 instruments and 4 parameters. The Hansen J-statistic is 21.3 with 8 degrees of freedom (p = 0.006). What is the most appropriate conclusion?"
  type: multiple-choice
  options:
    - "The model is well-specified — a large J-statistic signals that the moment conditions are highly informative"
    - "At least one moment condition appears to be misspecified — some instruments may be invalid or the functional form may be incorrect"
    - "The sample size is too small; GMM requires n > 1000 for valid inference"
    - "The estimator is inefficient; a different initial weighting matrix would reduce the J-statistic to an acceptable level"
  answer: 1
  explanation: "The J-statistic tests whether all overidentifying restrictions hold simultaneously at the GMM estimates. Under correct specification, J ~ χ²(q) where q = number of moment conditions minus number of parameters = 12 - 4 = 8. A value of 21.3 with p = 0.006 strongly rejects the null that all moments are correctly specified. This is a signal that one or more instruments are invalid (correlated with the error) or that the functional form is misspecified. Passing the J-test is necessary but not sufficient; failing it is a clear warning of misspecification."

- question: "In a just-identified GMM problem (same number of moment conditions as parameters), the researcher must use a two-step iterative procedure to compute the optimal weighting matrix and obtain estimates."
  type: true-false
  answer: false
  explanation: "When just-identified, there are exactly as many equations (sample moments = 0) as unknowns (parameters), so you can solve the system directly — setting g(θ) = 0 exactly. No weighting matrix is needed or meaningful because there is only one solution regardless of W. The two-step procedure is necessary only when overidentified, because then you cannot satisfy all moments simultaneously and must choose how to weight the residual."

- question: "OLS can be interpreted as a special case of GMM in which the moment conditions are the sample orthogonality conditions between regressors and residuals."
  type: true-false
  answer: true
  explanation: "The OLS first-order conditions require (1/n)Σ Xᵢ(Yᵢ - Xᵢ'β) = 0 — the sample analogs of E[Xᵢεᵢ] = 0. These are exactly GMM moment conditions with f(Yᵢ, β) = Xᵢ(Yᵢ - Xᵢ'β). When the number of regressors equals the number of moment conditions (just-identified), GMM reduces exactly to OLS. IV is also a GMM special case with instrument orthogonality conditions. This unification is the core appeal of the GMM framework."

- question: "Why does having more moment conditions than parameters in GMM create both an opportunity and a testable restriction, and how does the Hansen J-test exploit the latter?"
  type: short-answer
  answer: "Opportunity: each additional valid moment condition contains information about θ that can improve estimation precision. By choosing the weighting matrix to exploit the most informative moments, the researcher achieves greater efficiency than any just-identified estimator. Testable restriction: if the model is correctly specified, all moment conditions should hold simultaneously — but with more conditions than parameters, there is no θ that sets all sample moments to exactly zero. At the GMM optimum, the weighted residual g(θ̂)'Ŵg(θ̂) is small but nonzero. The Hansen J-statistic scales this residual by the sample size: nJ ~ χ²(q) under the null of correct specification, where q = (number of moment conditions) - (number of parameters). A large J indicates the moment conditions are in systematic conflict with each other, signaling that at least one is misspecified."
  explanation: "The J-test is the overidentification test: it asks whether the 'extra' moment conditions, beyond what is needed for identification, are consistent with the same θ. Passing provides some evidence of instrument validity; failing is diagnostic of misspecification. Importantly, the J-test cannot detect if all instruments are invalid in the same direction — it only detects internal inconsistency among the moment conditions."
```

## Explainer

You've encountered several estimation strategies already: OLS minimizes squared residuals, MLE maximizes the likelihood of the observed data, and IV uses instruments to isolate exogenous variation. GMM unifies all of these into a single framework built around the idea of **moment conditions**. A moment condition is a population statement of the form E[f(Yᵢ, θ)] = 0, where f is some function of the data and the parameters, and the expectation equals zero when evaluated at the true θ. OLS, for example, rests on the moment condition E[Xᵢ(Yᵢ - Xᵢ'β)] = 0 — the orthogonality of regressors and errors. IV adds the instrument orthogonality condition E[Zᵢ(Yᵢ - Xᵢ'β)] = 0. Both are special cases of the GMM framework.

The GMM estimator works by replacing the population expectation E[f(Yᵢ, θ)] with its sample analog (1/n)Σf(Yᵢ, θ), then choosing θ to make this sample moment vector as close to zero as possible. When you have exactly as many moment conditions as parameters — just-identified — you can set the sample moments exactly to zero and solve directly. This gives the IV estimator as a special case. When you have more moment conditions than parameters — **overidentified** — you can't satisfy all moments simultaneously, so you minimize a weighted sum of squared moments: the **GMM objective function** g(θ)'Wg(θ), where g(θ) is the vector of sample moments and W is a weighting matrix.

The choice of W matters enormously for efficiency. The **optimal weighting matrix** is the inverse of the variance of the moment conditions — intuitively, you should downweight moments that are noisy and upweight those that are precisely estimated. Implementing this requires two-step GMM: estimate θ with an initial W (often the identity matrix), compute the sample variance of the moments at those estimates, invert it to get the optimal W, and re-estimate. The resulting **two-step GMM estimator** is asymptotically efficient among all GMM estimators using those moment conditions.

Overidentification creates a testable restriction: if the model is correctly specified, all the moment conditions should hold simultaneously. The **Hansen J-statistic** measures how well the overidentifying restrictions are satisfied at the GMM estimates. A large J-statistic — relative to a chi-squared distribution with degrees of freedom equal to the number of overidentifying restrictions — suggests at least one moment condition is misspecified, meaning some instruments may be invalid or the functional form is wrong. Passing the J-test is necessary but not sufficient for validity; failing it is a clear signal of misspecification. In practice, GMM is particularly useful in rational expectations models (where theory delivers moment conditions directly) and in dynamic panel models where the Arellano-Bond estimator uses lagged levels as instruments for differenced equations.
