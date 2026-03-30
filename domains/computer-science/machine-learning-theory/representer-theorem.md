---
id: representer-theorem
title: Representer Theorem
domain: computer-science
course: machine-learning-theory
prerequisites:
- id: kernel-theory-and-rkhs
  type: hard
- id: regularization-techniques
  type: soft
- id: matrix-multiplication
  type: soft
tags:
- kernel-theory
- optimization
- regularization
stage: expert
status: validated
---

# Representer Theorem

## Core Idea
The representer theorem states that the solution to any regularized empirical risk minimization problem over an RKHS — minimizing a loss plus a monotonically increasing function of the RKHS norm — lies in the span of the kernel functions evaluated at the training points: f*(x) = sum_{i=1}^{n} alpha_i * k(x_i, x). Even though the RKHS may be infinite-dimensional, the optimal function is determined by just n coefficients. This reduces an infinite-dimensional optimization problem to a finite-dimensional one, making kernel methods computationally tractable and explaining why the kernel matrix (Gram matrix) is the central object in kernel algorithms.

## Questions

```yaml
- question: "A kernel method is applied to 500 training points using an RBF kernel (infinite-dimensional RKHS). The representer theorem guarantees the solution has what form?"
  type: multiple-choice
  options:
    - "A function represented by the 500 most important eigenfunctions of the kernel"
    - "A linear combination of exactly 500 kernel functions: f(x) = sum_{i=1}^{500} alpha_i * k(x_i, x), one centered at each training point"
    - "A function that can be expressed with at most 500 parameters in the original input space"
    - "A 500-dimensional feature vector that captures the essential information in the RKHS"
  answer: 1
  explanation: "The representer theorem states that the optimal solution lies in the span of {k(x_1, ·), k(x_2, ·), ..., k(x_n, ·)} — the kernel functions centered at the training points. For n = 500 training points, the solution is f*(x) = sum_{i=1}^{500} alpha_i * k(x_i, x). The 500 coefficients alpha_i are all that need to be determined, reducing the infinite-dimensional optimization to a 500-dimensional one. This is remarkable: the RKHS for the RBF kernel is infinite-dimensional, yet the optimal regularized solution lives in a 500-dimensional subspace determined entirely by the training data."

- question: "The representer theorem applies only to the squared RKHS norm penalty ||f||^2. Other regularizers require different theoretical justification."
  type: true-false
  answer: false
  explanation: "The representer theorem is more general than many expositions suggest. It applies to any regularizer that is a strictly monotonically increasing function of the RKHS norm ||f||, not just the squared norm. This includes ||f||, ||f||^2, ||f||^p for any p > 0, and even non-polynomial increasing functions of the norm. The key requirement is monotonicity: the penalty must increase when the norm increases. This ensures that the component of f orthogonal to the span of the training kernel functions only increases the penalty without reducing the empirical loss, so the optimal solution has zero orthogonal component."

- question: "Without regularization (minimizing only the empirical loss over the RKHS), the representer theorem still guarantees a finite-dimensional solution."
  type: true-false
  answer: false
  explanation: "Without regularization, the representer theorem does not apply in its standard form. The regularization term is what eliminates the component of f orthogonal to the span of training kernel functions — without it, there may be many functions achieving the same minimum loss, some of which have nonzero orthogonal components. The unregularized problem may not have a unique minimum-norm solution, or the solution may not be finite-dimensional. This is one theoretical reason why regularization is essential in kernel methods, beyond just preventing overfitting — it makes the optimization well-posed and finite-dimensional."

- question: "Explain why the representer theorem makes kernel methods computationally tractable despite working in potentially infinite-dimensional function spaces."
  type: short-answer
  answer: "Without the representer theorem, optimizing over an RKHS would require searching an infinite-dimensional space — computationally impossible. The theorem restricts the search to the n-dimensional subspace spanned by kernel functions at the training points, reducing the problem to finding n coefficients alpha_1, ..., alpha_n. The optimization then involves only the n-by-n kernel matrix K_{ij} = k(x_i, x_j), which is finite and computable. For kernel ridge regression, the solution is alpha = (K + lambda*I)^{-1} * y, a standard linear algebra problem. The computational cost is O(n^3) for the matrix inversion, independent of the RKHS dimension. This is the practical miracle of kernel methods: the infinite-dimensional function space collapses to an n-dimensional problem, and the kernel trick means you never need to compute the (possibly infinite-dimensional) feature vectors explicitly."
  explanation: "The O(n^3) cost is also the main limitation of kernel methods for large datasets. Methods like Nystrom approximation and random Fourier features address this by approximating the kernel matrix, but the representer theorem remains the foundational result explaining why exact kernel methods are possible at all."
```

## Explainer

The RKHS framework provides a rich, infinite-dimensional space of functions — but how do you actually optimize over such a space? The representer theorem answers this by showing that regularized optimization in an RKHS automatically produces solutions that live in a finite-dimensional subspace, making the infinite-dimensional problem tractable.

The setup is a regularized empirical risk minimization problem: minimize (1/n) * sum_{i=1}^{n} L(y_i, f(x_i)) + lambda * g(||f||), where L is a loss function, g is a monotonically increasing function (typically g(t) = t^2), and f ranges over the RKHS H_k. The theorem states that the minimizer has the form f*(x) = sum_{i=1}^{n} alpha_i * k(x_i, x). The proof is elegant: decompose any f in the RKHS as f = f_span + f_perp, where f_span lies in the span of {k(x_1, ·), ..., k(x_n, ·)} and f_perp is orthogonal to this subspace. By the reproducing property, f(x_i) = <f, k(x_i, ·)> = <f_span, k(x_i, ·)> — the orthogonal component does not affect any training-point evaluation. So f_perp contributes nothing to the loss but increases the RKHS norm (||f||^2 = ||f_span||^2 + ||f_perp||^2). The regularizer penalizes the larger norm, so the optimal f_perp is zero.

This result transforms kernel learning into linear algebra. Substituting the representer form into the optimization problem, the objective becomes a function of the n-dimensional vector alpha, with all RKHS geometry encoded in the n-by-n kernel matrix K. For kernel ridge regression, the closed-form solution is alpha = (K + lambda * I)^{-1} * y. For SVMs, the representer theorem justifies the dual formulation that depends only on kernel evaluations between training points. The computational cost scales with the number of training points (typically O(n^3) or O(n^2) depending on the algorithm), not with the dimensionality of the RKHS.

The representer theorem also clarifies the role of regularization in kernel methods. Beyond preventing overfitting, regularization is structurally necessary: it is what makes the optimization finite-dimensional. Without the norm penalty, the problem is ill-posed in the infinite-dimensional RKHS — there may be infinitely many functions achieving the same empirical risk, with no reason to prefer one over another. The regularizer selects the minimum-norm solution, which the representer theorem guarantees lies in the finite-dimensional span of the training kernel functions. This deep connection between regularization and tractability is one of the most elegant results in machine learning theory.
