---
id: information-theory-statistical-inference
title: Information Theory and Statistical Inference
domain: computer-science
course: information-theory
prerequisites:
- id: kl-divergence
  type: hard
- id: minimum-description-length
  type: hard
- id: fisher-information-theory
  type: hard
builds-toward: []
tags:
- hypothesis testing
- estimation theory
- KL divergence
- information criterion
- Kullback-Leibler
- divergence and statistical distance
stage: expert
status: validated
---

# Information Theory and Statistical Inference

## Core Idea
Information theory provides fundamental limits and optimality principles for statistical inference: estimation and hypothesis testing. The **Kullback-Leibler divergence** D_KL(p||q) quantifies the information lost when approximating true distribution p with model q, and arises naturally in maximum likelihood estimation as the asymptotic objective (minimizing KL divergence). The **Fisher information** I(theta) quantifies the curvature of the likelihood landscape and lower-bounds the variance of any unbiased estimator (Cramer-Rao bound). **Hypothesis testing** can be framed information-theoretically: the error probability decays exponentially with the number of samples, with rate determined by the Chernoff exponent, which involves KL divergence between competing hypotheses. **Information criteria** (AIC, BIC, MDL) trade off model fit and complexity using KL divergence or description length. These principles unify estimation, testing, and model selection under a single information-theoretic framework, revealing that all statistical tasks are fundamentally limited by how much information the data provides about unknowns.

## Questions

```yaml
- question: "The Kullback-Leibler divergence D_KL(p||q) = sum_x p(x) log(p(x)/q(x)) measures information lost when using q to approximate p. Why does maximum likelihood estimation (MLE) asymptotically minimize D_KL(p||q_theta)?"
  type: multiple-choice
  options:
    - "MLE minimizes the likelihood, which is the reciprocal of KL divergence"
    - "MLE maximizes log p_theta(data), and by the law of large numbers, this is equivalent to minimizing D_KL(empirical distribution || p_theta), which bounds D_KL(true p || p_theta)"
    - "MLE is defined to minimize KL divergence by design"
    - "KL divergence and likelihood are not related"
  answer: 1
  explanation: "Given n samples from true distribution p, the empirical distribution p_emp puts mass 1/n on each sample. For large n, p_emp converges to p (by the law of large numbers). The log-likelihood is sum_i log p_theta(x_i) = n * E_emp[log p_theta(x)]. MLE maximizes this, equivalent to maximizing E_emp[log p_theta(x)]. This is equivalent to minimizing D_KL(p_emp || p_theta) = E_emp[log(p_emp(x)/p_theta(x))] = E_emp[log p_emp] - E_emp[log p_theta]. The first term (empirical entropy) doesn't depend on theta, so minimizing KL w.r.t. theta is equivalent to maximizing likelihood. As n increases, p_emp approaches p, so MLE approaches the solution that minimizes D_KL(p || p_theta). This is how information theory unifies MLE as KL divergence minimization."

- question: "The Cramer-Rao bound states that the variance of any unbiased estimator of theta is lower-bounded by 1/F(theta), where F is Fisher information. This bound is information-theoretic: it relates curvature of the likelihood landscape to estimation precision."
  type: true-false
  answer: true
  explanation: "Fisher information F(theta) = E[(d/d_theta log p(X|theta))^2] measures how much the log-likelihood curvature around theta. High curvature means small changes in theta create large changes in the likelihood — the data is sensitive to theta, allowing precise estimation. Low curvature means the likelihood is flat — the data are insensitive to theta, making estimation imprecise. The Cramer-Rao bound formalizes this: no estimator (biased or unbiased) can achieve variance smaller than 1/F(theta), a fundamental limit set by the information in the data. The bound is tight for exponential families and certain other models; maximum likelihood estimation often achieves the bound asymptotically."

- question: "Explain how the error exponent in binary hypothesis testing (Neyman-Pearson setting) is related to the Kullback-Leibler divergence between the two hypotheses."
  type: short-answer
  answer: "In binary hypothesis testing, we have null hypothesis H0 (distribution p) versus alternative H1 (distribution q). A test error occurs when we reject H0 given q, or fail to reject given p. The Chernoff exponent gives the rate at which error probability decays with sample size n: P(error) ~ exp(-n*E*), where E* is the Chernoff information, defined as E* = min_{0 < beta < 1} [beta*D_KL(p||q) + (1-beta)*D_KL(q||p)]. This is a weighted average of the KL divergences between the two hypotheses. When p and q are far apart (large KL divergence), E* is large and errors decay rapidly (strong separation). When p and q are close (small KL), E* is small and errors decay slowly (weak separation). The optimal test (which achieves the Chernoff exponent) uses a likelihood ratio: accept the hypothesis with higher likelihood."
  explanation: "This fundamental result shows that hypothesis testing error is fundamentally limited by how much information the samples provide about which hypothesis is true — quantified by KL divergence. No test can beat the Chernoff exponent; many practical tests (likelihood ratio) achieve it."

- question: "The Akaike Information Criterion (AIC) = -2*log-likelihood + 2*k penalizes model complexity by 2k. In what sense is AIC an 'information criterion'?"
  type: multiple-choice
  options:
    - "AIC measures information content of the model parameters"
    - "AIC approximates the KL divergence between the true distribution and the fitted model, plus a penalty for overfitting. It balances likelihood (KL divergence) and complexity, derived from information theory"
    - "AIC is based on Shannon entropy directly"
    - "AIC has no connection to information theory"
  answer: 1
  explanation: "AIC derives from information theory through the connection between MLE and KL divergence minimization. For large samples, AIC approximately equals n*(minimum KL divergence) + 2k. Minimizing AIC trades off likelihood (KL divergence to true distribution) and model complexity (k). The factor 2 (in 2*k) comes from an information-theoretic calculation: under model misspecification, the penalty for adding one parameter is approximately 2 in likelihood terms. AIC is used when you're comparing models that may be misspecified (none is true). BIC = -2*log-likelihood + k*log(n) is another information-based criterion that emerges from a Bayesian information-theoretic perspective and penalizes complexity more severely (log n >> 2 for large n)."
```

## Explainer

Statistical inference — estimating unknown parameters and testing hypotheses from data — appears to have little to do with information theory. Yet information-theoretic concepts and bounds are fundamental to understanding what inference is possible and how well it can be done.

**Maximum Likelihood and KL Divergence**:
The most common approach to estimation is maximum likelihood: given observed data, find the parameter theta that maximizes the probability of the data. Asymptotically (as the sample size grows), MLE is equivalent to finding the theta that minimizes the Kullback-Leibler divergence D_KL(p_true || p_theta) between the true distribution and the model. This connection is profound: it unifies estimation under the principle of KL divergence minimization. The likelihood function, the score, the Hessian (Fisher information) — all emerge naturally from divergence-theoretic concepts. MLE is asymptotically optimal in several senses: it is consistent (converges to the true parameter), efficient (achieves the Cramer-Rao lower bound asymptotically), and has minimal information loss.

**Fisher Information and Estimation Limits**:
The Fisher information I(theta) = E[(d/d_theta log p(X|theta))^2] quantifies how sensitive the likelihood is to changes in theta. High Fisher information means the data are informative about theta, enabling precise estimation. The Cramer-Rao bound states that no unbiased estimator can have variance lower than 1/I(theta) per sample. This is a fundamental limit imposed by information theory: the amount of information in the data (quantified by Fisher information) directly constrains estimation precision. MLE achieves the Cramer-Rao bound asymptotically for most models, showing that MLE is not just practical but information-theoretically optimal.

**Hypothesis Testing and Error Exponents**:
In the Neyman-Pearson setting, we test H0 (data drawn from p) versus H1 (data drawn from q). The optimal test is the likelihood ratio test: accept H1 if the likelihood ratio p(data|q)/p(data|p) exceeds a threshold. The error probability decays exponentially with sample size n: P(error) ~ exp(-n*E*), where E* is the Chernoff information. For simple hypotheses, E* = min_{0<beta<1} [beta*D_KL(p||q) + (1-beta)*D_KL(q||p)]. When p and q are far apart (large mutual KL divergence), E* is large — errors vanish quickly, strong discrimination. When p and q are close, E* is small — weak discrimination. The rate of error decay is fundamentally set by the KL divergence between hypotheses: information-theoretic separation.

**Information Criteria and Model Selection**:
Comparing models that may be misspecified requires balancing likelihood and complexity. Three major information criteria emerge from information-theoretic principles:
- **AIC** (Akaike): -2*log L + 2k. Minimizes expected KL divergence to the true distribution under repeated sampling.
- **BIC** (Bayesian): -2*log L + k*log(n). Emerges from a Bayesian perspective with uniform model priors; asymptotically selects the true model (if it is in the set).
- **MDL** (Minimum Description Length): L(model) + L(data|model) in bits. Directly minimizes description length under the universal prior 2^(-K(x)).

Each reflects a different information-theoretic principle: AIC minimizes expected future KL divergence; BIC selects the best model asymptotically; MDL directly encodes simplicity as short description. For finite samples or model misspecification, they give different answers. Understanding the information-theoretic foundations helps choose the right criterion for a given problem.

**Convergence and Sample Complexity**:
How many samples do you need to estimate a parameter to a given precision? Information theory answers: at least log(1/epsilon) samples are necessary (where epsilon is the precision), because each sample provides about 1 bit of information. More precisely, the sample complexity depends on the Fisher information: lower information (flatter likelihood landscape) requires more samples. This is why high-dimensional problems are hard: with d parameters, you need at least d information-theoretically just to identify them, and practical estimation requires more.

**Learning Theory Connection**:
Information theory connects to learning theory (generalization bounds, PAC learning). The number of distinguishable hypotheses from a limited dataset is bounded by the mutual information between the hypothesis class and the observed data. This information-theoretic view unifies estimation error (approximation quality) and generalization error (performance on unseen data). A learner can distinguish at most ~sqrt(d) parameters with n samples from a d-dimensional exponential family, because the information in n samples scales as sqrt(n) when maximally distributed across d parameters.

Information theory reveals that estimation, testing, and model selection are all fundamentally constrained by how much information the data provide about unknowns. The field of statistical inference, when viewed through the lens of information theory, is unified: all tasks are limited by Shannon's bounds, and optimal methods minimize KL divergence or maximize mutual information. This perspective has practical implications — it guides algorithm design, explains why certain methods work well, and reveals fundamental limits that no method can overcome.
