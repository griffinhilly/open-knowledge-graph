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
stage: formal-systems
status: draft
---

# Generalized Method of Moments (GMM)

## Core Idea
GMM exploits moment conditions E[f(Yᵢ, θ)] = 0 to estimate θ by minimizing a quadratic form in sample moments. It generalizes OLS, IV, and MLE; yields efficient estimators when moment conditions are correctly specified. The Hansen J-test checks overidentification.

## Explainer

You've encountered several estimation strategies already: OLS minimizes squared residuals, MLE maximizes the likelihood of the observed data, and IV uses instruments to isolate exogenous variation. GMM unifies all of these into a single framework built around the idea of **moment conditions**. A moment condition is a population statement of the form E[f(Yᵢ, θ)] = 0, where f is some function of the data and the parameters, and the expectation equals zero when evaluated at the true θ. OLS, for example, rests on the moment condition E[Xᵢ(Yᵢ - Xᵢ'β)] = 0 — the orthogonality of regressors and errors. IV adds the instrument orthogonality condition E[Zᵢ(Yᵢ - Xᵢ'β)] = 0. Both are special cases of the GMM framework.

The GMM estimator works by replacing the population expectation E[f(Yᵢ, θ)] with its sample analog (1/n)Σf(Yᵢ, θ), then choosing θ to make this sample moment vector as close to zero as possible. When you have exactly as many moment conditions as parameters — just-identified — you can set the sample moments exactly to zero and solve directly. This gives the IV estimator as a special case. When you have more moment conditions than parameters — **overidentified** — you can't satisfy all moments simultaneously, so you minimize a weighted sum of squared moments: the **GMM objective function** g(θ)'Wg(θ), where g(θ) is the vector of sample moments and W is a weighting matrix.

The choice of W matters enormously for efficiency. The **optimal weighting matrix** is the inverse of the variance of the moment conditions — intuitively, you should downweight moments that are noisy and upweight those that are precisely estimated. Implementing this requires two-step GMM: estimate θ with an initial W (often the identity matrix), compute the sample variance of the moments at those estimates, invert it to get the optimal W, and re-estimate. The resulting **two-step GMM estimator** is asymptotically efficient among all GMM estimators using those moment conditions.

Overidentification creates a testable restriction: if the model is correctly specified, all the moment conditions should hold simultaneously. The **Hansen J-statistic** measures how well the overidentifying restrictions are satisfied at the GMM estimates. A large J-statistic — relative to a chi-squared distribution with degrees of freedom equal to the number of overidentifying restrictions — suggests at least one moment condition is misspecified, meaning some instruments may be invalid or the functional form is wrong. Passing the J-test is necessary but not sufficient for validity; failing it is a clear signal of misspecification. In practice, GMM is particularly useful in rational expectations models (where theory delivers moment conditions directly) and in dynamic panel models where the Arellano-Bond estimator uses lagged levels as instruments for differenced equations.
