---
id: minimum-description-length
title: Minimum Description Length
domain: computer-science
course: information-theory
prerequisites:
- id: kolmogorov-complexity-algorithmic
  type: hard
- id: source-coding-theorem
  type: hard
- id: kl-divergence
  type: soft
builds-toward:
- information-theory-statistical-inference
tags:
- MDL
- model selection
- description length
- compression
- Occam's razor
- algorithmic probability
stage: expert
status: validated
---

# Minimum Description Length

## Core Idea
The Minimum Description Length (MDL) principle is a practical formalization of Occam's razor: choose the model that minimizes the total description length of the model plus the data encoded relative to that model. MDL = L(M) + L(D|M), where L(M) is the length of the model description and L(D|M) is the length of the data description given the model. This provides a principled model selection criterion that automatically trades off fit and complexity — more complex models can explain data in fewer bits (lower L(D|M)), but require longer descriptions themselves (higher L(M)). MDL is motivated by Kolmogorov complexity and Solomonoff induction (the universal prior 2^(-K(x)) assigns exponentially higher weight to simpler explanations), and is related to the Bayesian information criterion (BIC) and information-theoretic measures like AIC. Unlike likelihood-based approaches, MDL is not asymptotic — it applies to finite samples — and avoids overfitting by penalizing model complexity directly.

## Questions

```yaml
- question: "In MDL, the total description length is L(M) + L(D|M). Why is it insufficient to minimize only L(D|M) (the fit) when selecting a model?"
  type: multiple-choice
  options:
    - "Because L(D|M) is always zero for complex models"
    - "Because minimizing only L(D|M) leads to overfitting — every training set can be perfectly memorized by a sufficiently complex model (e.g., a lookup table), which explains the data with L(D|M) = 0 but does not generalize. MDL penalizes complexity through L(M), forcing a tradeoff."
    - "Because L(D|M) cannot be computed"
    - "Because the data length is fixed and does not vary across models"
  answer: 1
  explanation: "A model that memorizes all N training examples (e.g., storing (x_i, y_i) pairs) can achieve L(D|M) ≈ 0 — perfect fit. But such a model has no predictive power on new data. MDL enforces a tradeoff: the model description L(M) would be huge (it must encode all the lookups), so the total L(M) + L(D|M) is large. A simpler model might have nonzero L(D|M) on the training set (it doesn't fit perfectly), but smaller L(M), yielding lower total description length and better generalization. This is why MDL is a principled solution to model selection: it automatically prevents overfitting without needing a separate validation set."

- question: "MDL is asymptotically equivalent to the Bayesian information criterion (BIC), which penalizes model complexity using n*log(k) where n is the sample size and k is the model's degrees of freedom."
  type: true-false
  answer: true
  explanation: "The connection is deep. BIC = -2*log-likelihood(D|M) + k*log(n), which penalizes model complexity logarithmically in the sample size. For large n, BIC is asymptotically equivalent to MDL when L(M) is taken as the (log) prior on model complexity, and L(D|M) is the (log) likelihood. Both methods balance fit and complexity in a way that is asymptotically optimal for selecting among a finite set of models. MDL generalizes to non-asymptotic settings and to models where the number of parameters is not fixed."

- question: "Explain how MDL connects to Kolmogorov complexity and Solomonoff induction. Why does MDL approximate the theoretical optimum for learning?"
  type: short-answer
  answer: "Kolmogorov complexity K(x) measures the shortest program that generates x. The universal prior 2^(-K(x)) assigns probability to each data sequence inversely proportional to the shortest program length. Solomonoff induction predicts by averaging over all programs consistent with observed data, weighted by this prior — it is theoretically optimal for any computable source (converges to the true distribution). MDL approximates Solomonoff induction by using practical compression schemes (e.g., arithmetic coding) in place of true K(x), which is uncomputable. The description length L(D|M) via arithmetic coding approximates I(D|M) in bits, and choosing M to minimize L(M) + L(D|M) approximates the Solomonoff prior. In this sense, MDL is a computable, practical approximation to theoretically optimal Bayesian prediction using the universal prior."
  explanation: "MDL makes the abstract theory of algorithmic information concrete: instead of computing K(x) (uncomputable), we use compression algorithms; instead of computing the universal prior 2^(-K(x)) (uncomputable), we optimize description length directly. The result is a practical principle that inherits the theoretical optimality of Solomonoff induction while remaining implementable."

- question: "A dataset D of 100 samples is fit with two models: (A) a 2-parameter linear regression with total description L_A = 100 bits, (B) a 10-parameter polynomial regression with total description L_B = 150 bits. Which model does MDL prefer, and why?"
  type: multiple-choice
  options:
    - "Model B, because it has more parameters and higher capacity"
    - "Model A, because it has lower total description length (100 < 150)"
    - "Model B, because the sample size is 100 and polynomial has better expressiveness"
    - "The choice depends on the likelihood values, not the description length"
  answer: 1
  explanation: "MDL directly compares total description lengths: L_A = 100 < L_B = 150, so MDL selects Model A. The total description includes both the model specification (L(M)) and the residuals given the model (L(D|M)). Model B's higher-dimensional parameter space requires more bits to specify, and though it might fit the data more closely (lower L(D|M)), the savings in data description do not outweigh the cost of the model description. This is how MDL automatically prevents overfitting: extra parameters must justify themselves by achieving significant compression of the data."
```

## Explainer

Modern machine learning faces a fundamental challenge: overfitting. A sufficiently complex model can memorize any training data, achieving zero training error while failing on new data. How do you choose model complexity automatically?

The Minimum Description Length principle answers this by formalizing Occam's razor as a compression problem. The description of data D given model M consists of two parts:
1. **Model description L(M)**: How many bits to describe the model itself (its parameters, structure, hyperparameters)?
2. **Data description L(D|M)**: How many bits to describe the data, compressed using the model?

The total is **MDL = L(M) + L(D|M)**. The principle: choose the model that minimizes this total. This balances two competing objectives. A simple model has low L(M) but may not fit the data well, requiring many bits to describe the residuals (high L(D|M)). A complex model has high L(M) but can fit the data closely (low L(D|M)). The optimal model trades off these two costs.

**Practical Implementation**:
- L(M) = cost to encode the model parameters (often proportional to the number of parameters k, scaled by log of precision needed, e.g., k*log(n) bits for n samples).
- L(D|M) = bits needed to encode the prediction errors given the model, often via arithmetic coding or similar compression.

For a dataset with n samples, a 2-parameter linear model might require 10 bits to specify parameters precisely, plus 1000 bits to encode residuals (total 1010). A 10-parameter polynomial might require 50 bits for parameters, plus 800 bits for residuals (total 850). MDL chooses the polynomial. As the polynomial's complexity grows further, L(M) increases rapidly. At some point, the savings in L(D|M) do not compensate — MDL stops and selects the best model.

**Connection to Bayesian Methods**:
MDL is closely related to the Bayesian information criterion (BIC) and Bayesian model selection. A Bayesian assigns a prior to each model and computes the posterior given data. The model with the highest posterior is selected. When the prior is a uniform distribution over models, and we use a data likelihood that corresponds to a compression scheme, MDL emerges naturally. More formally, Bayesian model selection under the "universal prior" 2^(-K(M)) (from Kolmogorov complexity) is equivalent to MDL.

**Comparison to Information Criteria**:
- **AIC** (Akaike Information Criterion) = -2*log-likelihood + 2k. Penalizes complexity by the number of parameters, without sample size dependence. Tends to overfit for finite samples.
- **BIC** = -2*log-likelihood + k*log(n). Penalizes complexity scaled by sample size. Asymptotically equivalent to MDL for large n.
- **MDL** = L(M) + L(D|M). Directly minimizes description length, applies to finite samples, and is not restricted to parametric models.

**Advantages**:
- Avoids overfitting without needing a separate validation set.
- Applies to non-parametric models (decision trees, neural networks) where the number of "parameters" is ambiguous.
- Theoretically justified through Kolmogorov complexity and algorithmic probability.
- Naturally handles model comparison, feature selection, and architecture search.

**Limitations**:
- Requires computing or approximating L(D|M), which depends on the choice of compression scheme (Huffman, arithmetic coding). Different schemes give slightly different results.
- Computationally expensive for some models (requires iterating to find optimal parameter encodings).
- The "true" MDL involves uncomputable Kolmogorov complexity; practical MDL uses approximations.

The principle has been successfully applied to feature selection, model architecture search, clustering, and pattern discovery. It provides a unified framework for learning that, unlike empirical risk minimization, directly encodes the philosophical principle that simpler explanations are preferable — a principle with deep roots in information theory and mathematical foundations of science.
