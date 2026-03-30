---
id: information-geometry-basics
title: Information Geometry Basics
domain: computer-science
course: information-theory
prerequisites:
- id: fisher-information
  type: hard
- id: kl-divergence
  type: hard
- id: differential-entropy
  type: soft
tags:
- information geometry
- Fisher metric
- Riemannian manifold
- statistical manifold
- dual connections
- Amari
stage: expert
status: validated
---

# Information Geometry Basics

## Core Idea
Information geometry treats families of probability distributions as points on a Riemannian manifold, with the Fisher information matrix as the metric tensor. This geometric perspective reveals that statistical inference is fundamentally a geometric operation: maximum likelihood estimation finds the nearest point on a model manifold, the EM algorithm alternates between two dual projections, and exponential families are flat submanifolds. The dual connection structure (e-connection and m-connection) discovered by Amari captures the asymmetry of KL divergence geometrically. Information geometry unifies concepts from statistics, information theory, and differential geometry, providing deep structural insights into optimization, machine learning, and neural networks.

## Questions

```yaml
- question: "Why is the Fisher information matrix the natural choice of Riemannian metric on a statistical manifold, rather than the Euclidean metric on parameters?"
  type: multiple-choice
  options:
    - "The Euclidean metric is not defined for probability distributions"
    - "The Fisher metric is invariant under reparameterization — changing coordinates (e.g., from probability p to log-odds) does not change the geometric structure, while the Euclidean metric depends on the arbitrary choice of parameterization"
    - "The Fisher metric is always positive definite, while the Euclidean metric is not"
    - "The Euclidean metric requires distributions to have the same support"
  answer: 1
  explanation: "Cencov's theorem proves that the Fisher information matrix is the UNIQUE (up to scaling) Riemannian metric that is invariant under sufficient statistics (Markov morphisms). This means the geometry does not depend on how you parameterize the family — distance between distributions is an intrinsic property. The Euclidean metric d(theta_1, theta_2) = ||theta_1 - theta_2|| depends on the parameterization: distributions that are 'close' in one parameterization may be 'far' in another. The Fisher metric avoids this arbitrariness."

- question: "In information geometry, exponential families are flat manifolds under the e-connection, and mixture families are flat under the m-connection."
  type: true-false
  answer: true
  explanation: "This dually flat structure is a central result of information geometry. Exponential families (Gaussian, Bernoulli, Poisson, etc.) have zero curvature under the e-connection, meaning e-geodesics (exponential interpolations between distributions) are straight lines in natural parameters. Mixture families (convex combinations of distributions) are flat under the m-connection. The KL divergence D_KL(p||q) is the Bregman divergence associated with the e-flat structure, and it naturally decomposes into projections along the two dual connections. This duality explains why EM converges (each step is a dual projection)."

- question: "Explain the Pythagorean theorem in information geometry and how it relates to the projection properties of maximum likelihood estimation."
  type: short-answer
  answer: "In a dually flat manifold, the generalized Pythagorean theorem states: for distributions p, q, r where q is the m-projection (mixture projection) of p onto a submanifold M, D_KL(p || r) = D_KL(p || q) + D_KL(q || r) for any r in M. This is analogous to ||p-r||^2 = ||p-q||^2 + ||q-r||^2 in Euclidean geometry, where q is the orthogonal projection. MLE is an m-projection: the MLE distribution is the point in the model family closest to the empirical distribution in KL divergence. The Pythagorean theorem guarantees that this projection decomposes the total KL divergence into 'model error' (p to q) and 'within-model distance' (q to r), which is the geometric foundation of model selection and goodness-of-fit testing."
  explanation: "The Pythagorean relation requires that q be the projection of p and r be in the flat submanifold — the 'right angle' condition. This generalizes the familiar orthogonal decomposition in linear regression to the nonlinear setting of exponential families, providing geometric insight into why maximum likelihood has good properties."
```

## Explainer

Probability distributions have a natural geometric structure. Consider the set of all Bernoulli distributions parameterized by p in (0,1). In the usual Euclidean view, this is a line segment. But from an information-theoretic perspective, distributions near p = 0 or p = 1 are packed more tightly — small changes in p create large changes in the distribution when p is extreme. The Fisher information I(p) = 1/(p(1-p)) captures this: the "information-theoretic distance" between p and p + dp is sqrt(I(p)) * dp, which is large near the boundaries. Information geometry makes this rigorous by using I(p) as a Riemannian metric.

For a parametric family {f(x; theta) : theta in Theta}, the **Fisher information matrix** g_{ij}(theta) = E[(d/d_theta_i log f)(d/d_theta_j log f)] serves as the metric tensor. The geodesic distance between nearby distributions f(x; theta) and f(x; theta + d_theta) is ds^2 = sum g_{ij} d_theta_i d_theta_j. This distance is invariant under reparameterization — by Cencov's theorem, it is the unique natural metric on statistical manifolds. Two distributions that look close in one parameterization but far in another are correctly measured by the Fisher metric regardless.

The deepest insight of information geometry is the **dual connection structure**. On a standard Riemannian manifold, there is one natural connection (the Levi-Civita connection). On a statistical manifold, there are two: the **e-connection** (exponential) and the **m-connection** (mixture), which are dual with respect to the Fisher metric. Exponential families are flat under the e-connection, meaning their natural parameters form a coordinate system in which e-geodesics are straight lines. Mixture families are flat under the m-connection. KL divergence is the canonical divergence of this dually flat structure, and its asymmetry (D_KL(p||q) != D_KL(q||p)) reflects the dual nature of the two connections.

This geometric framework illuminates algorithms. The EM algorithm alternates between e-projection and m-projection, which is why it converges monotonically. Natural gradient descent (used in training neural networks) follows geodesics in the Fisher metric rather than Euclidean straight lines in parameter space, leading to faster convergence. Variational inference minimizes KL divergence, which is a projection in the information-geometric sense. The field, developed primarily by Shun-ichi Amari, continues to provide structural insights into machine learning, optimization, and the foundations of statistics.
