---
id: regularization-theory
title: Regularization Theory (Tikhonov, Spectral)
domain: computer-science
course: machine-learning-theory
prerequisites:
- id: regularization-techniques
  type: hard
- id: eigenvalues-and-eigenvectors
  type: hard
- id: representer-theorem
  type: soft
- id: bias-complexity-tradeoff-formal
  type: soft
tags:
- regularization
- inverse-problems
- tikhonov
- spectral-methods
stage: expert
status: validated
---

# Regularization Theory (Tikhonov, Spectral)

## Core Idea
Regularization theory provides the mathematical framework for solving ill-posed inverse problems — problems where the solution does not depend continuously on the data. In machine learning, learning from finite samples is ill-posed: small changes in the training data can cause large changes in the learned function. Tikhonov regularization stabilizes the problem by adding a squared-norm penalty, shrinking the solution toward zero. Spectral regularization generalizes this by applying a filter function to the eigenvalues of the kernel matrix, controlling which frequency components of the solution are retained. Both approaches can be understood through the bias-variance lens: the regularization parameter trades off approximation error against estimation stability.

## Questions

```yaml
- question: "Tikhonov regularization solves min_f (1/n)||y - Kf||^2 + lambda||f||^2, where K is the kernel matrix. In the eigendecomposition of K with eigenvalues sigma_i, what does the regularization parameter lambda do to each eigencomponent of the solution?"
  type: multiple-choice
  options:
    - "It sets eigencomponents with sigma_i < lambda to exactly zero, acting as a hard threshold"
    - "It shrinks each eigencomponent by a factor of sigma_i / (sigma_i + lambda), attenuating small eigenvalues more than large ones"
    - "It adds lambda to each eigenvalue uniformly, shifting the entire spectrum"
    - "It inverts the effect of eigenvalue decay, amplifying small eigenvalues to prevent information loss"
  answer: 1
  explanation: "The Tikhonov solution in the eigendecomposition is alpha_i = sigma_i / (sigma_i^2 + lambda) * (u_i^T y) / sigma_i = 1/(sigma_i + lambda) * (u_i^T y), or more precisely the filter factor is sigma_i / (sigma_i + lambda). For eigencomponents where sigma_i >> lambda, the filter is approximately 1 (no shrinkage). For sigma_i << lambda, the filter is approximately sigma_i/lambda, heavily attenuated. This is soft thresholding — all components are retained but small eigenvalues (corresponding to high-frequency, noisy directions) are suppressed. Option A describes truncated SVD (hard spectral regularization), which is a different spectral method."

- question: "Increasing the Tikhonov regularization parameter lambda always increases the bias of the solution."
  type: true-false
  answer: true
  explanation: "Larger lambda applies stronger shrinkage, pushing the solution toward zero (or toward the prior). This means the regularized solution deviates more from the unregularized solution, which would have lower approximation error if data were infinite. The bias introduced is the price of stabilization — the regularized solution is more biased but less sensitive to noise in the training data. In the limit lambda -> infinity, the solution is zero (maximum bias, zero variance). In the limit lambda -> 0, the solution approaches the unregularized one (minimum bias, maximum variance and instability). The optimal lambda balances these extremes."

- question: "Spectral regularization methods (Tikhonov, truncated SVD, Landweber iteration) all operate by modifying the eigenvalues of the kernel matrix, but they differ in the shape of the filter function."
  type: true-false
  answer: true
  explanation: "All spectral regularization methods can be characterized by a filter function g_lambda(sigma) applied to the eigenvalues sigma of the kernel matrix. Tikhonov uses g(sigma) = sigma/(sigma + lambda), a smooth decay. Truncated SVD uses g(sigma) = 1 if sigma > threshold, 0 otherwise — a hard cutoff. Landweber iteration (iterative regularization) uses g(sigma) = 1 - (1 - sigma)^t, which gradually includes more eigencomponents as iterations t increase. Each filter shape makes different tradeoffs between bias and stability, and the unifying eigenvalue perspective reveals them as a single family of methods parameterized by the filter function."

- question: "Explain why learning from finite data is an ill-posed inverse problem and how Tikhonov regularization makes it well-posed."
  type: short-answer
  answer: "Learning from data is inverse because we observe outputs (labels) and must infer the function that produced them — the reverse of evaluation. It is ill-posed in Hadamard's sense: the solution does not depend continuously on the data. Concretely, small perturbations to the training labels can cause arbitrarily large changes in the learned function, especially along directions corresponding to small eigenvalues of the kernel matrix (where the inverse amplifies noise enormously). Tikhonov regularization adds lambda*||f||^2 to the objective, which prevents the solution from amplifying small-eigenvalue components. The resulting filter sigma/(sigma + lambda) damps the contribution of small eigenvalues, bounding the sensitivity of the solution to data perturbations. This makes the problem well-posed: the regularized solution depends continuously on the data, with the continuity constant controlled by lambda."
  explanation: "The analogy to matrix inversion is direct: inverting a near-singular matrix amplifies small singular values into enormous components. Adding lambda*I (Tikhonov regularization of the normal equations) makes the matrix well-conditioned. The same principle applies in function space."
```

## Explainer

Regularization in machine learning is often presented as a practical trick to prevent overfitting — add a penalty to the loss and tune its strength. Regularization theory reveals the deeper mathematical reason this works: learning from finite data is an ill-posed inverse problem, and regularization is the principled way to restore well-posedness.

An inverse problem is well-posed (in Hadamard's sense) if a solution exists, is unique, and depends continuously on the data. Learning from finite samples violates the third condition: the mapping from training data to learned function is discontinuous. Small perturbations to the labels can cause the learned function to change dramatically, especially when the model is flexible. In the spectral view, the kernel matrix K has eigenvalues that decay toward zero. The unregularized solution involves dividing by these eigenvalues (inverting K), which amplifies noise in the directions corresponding to small eigenvalues — exactly the high-frequency, fine-grained components where the signal-to-noise ratio is worst.

Tikhonov regularization adds lambda * ||f||^2 to the loss, changing the effective inversion from K^{-1} to (K + lambda * I)^{-1} * K. In the eigendecomposition, each eigencomponent is multiplied by the filter factor sigma_i / (sigma_i + lambda) instead of being divided by sigma_i. When sigma_i is large (strong signal directions), the filter is close to 1 — the information is preserved. When sigma_i is small (noisy directions), the filter suppresses the component toward zero. The regularization parameter lambda sets the threshold: eigencomponents above lambda pass through; those below lambda are attenuated. This is a smooth, principled tradeoff between retaining signal and suppressing noise.

Spectral regularization generalizes this idea. Any method that applies a filter function g_lambda(sigma) to the eigenvalues of the kernel matrix is a spectral regularizer. Tikhonov uses g(sigma) = sigma/(sigma + lambda). Truncated SVD uses a hard cutoff: g(sigma) = 1 for sigma above a threshold, 0 below. Early stopping in iterative methods like gradient descent is also a spectral regularizer: after t iterations, the implicit filter is g(sigma) = 1 - (1 - eta*sigma)^t, which gradually incorporates more eigencomponents as training proceeds. This unifying eigenvalue perspective reveals that many seemingly different regularization strategies — norm penalties, truncation, early stopping — are all performing the same fundamental operation: controlling which spectral components of the solution are retained, trading bias for stability in a way that depends on the eigenstructure of the problem.
