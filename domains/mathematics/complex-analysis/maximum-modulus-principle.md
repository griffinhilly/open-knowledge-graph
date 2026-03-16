---
id: maximum-modulus-principle
title: Maximum Modulus Principle
domain: mathematics
course: complex-analysis
prerequisites:
- id: liouville-theorem
  type: hard
tags:
- maximum-modulus
- rigidity
- interior-points
stage: advanced
status: draft
---

# Maximum Modulus Principle

## Core Idea
If f is holomorphic on a domain D and |f| attains a local maximum at an interior point z₀ ∈ D, then f is constant on D. The maximum of |f| must occur on the boundary. This principle reflects the rigidity of analytic functions: they cannot have isolated peaks or valleys in their magnitude.

## Explainer

To appreciate the Maximum Modulus Principle, start from your prerequisite: Liouville's Theorem says every bounded entire function is constant. The Maximum Modulus Principle is a dramatically stronger version of the same rigidity idea, applicable to bounded domains rather than the entire plane. Its message: a **holomorphic function** cannot have an interior peak in its magnitude |f(z)|. If |f| achieves its largest value anywhere inside a domain, then f must be constant throughout that domain.

The intuition comes from the **mean-value property** of analytic functions, a consequence of Cauchy's integral formula. If f is holomorphic inside a disk centered at z₀, then f(z₀) equals the average of f's values on any circle centered at z₀. Now suppose |f(z₀)| is a local maximum — |f(z₀)| ≥ |f(z)| for all z near z₀. Draw a small circle around z₀. The average of |f| on the circle cannot exceed |f(z₀)| (by the maximum assumption), but f(z₀) is the average of f itself on the circle. For the modulus of an average to equal the maximum modulus, all values on the circle must point in the same direction in the complex plane and share the same magnitude. This forces f to be constant on the circle. Since the circle was arbitrary, f is constant everywhere on D by the identity theorem.

The most useful form for applications is the **boundary maximum**: if f is continuous on a closed bounded domain D̄ and holomorphic on the open interior D, then |f| achieves its maximum on the boundary ∂D, not in the interior (unless f is constant). To bound how large |f| can be inside a region, you only need to examine the boundary — a powerful reduction. For instance, if you know |f(z)| ≤ M on the boundary of a disk, then |f(z)| ≤ M everywhere inside.

The contrast with real analysis is instructive. A real-valued smooth function on an interval can certainly achieve its maximum in the interior — f(x) = −x² peaks at x = 0 on any interval containing it. Holomorphic functions are far more rigid: once a complex function's values are specified on any open set or curve, they are determined everywhere on the connected domain (the identity theorem). The Maximum Modulus Principle is one expression of this global rigidity — local information about where |f| is largest forces a global conclusion about the entire function. The same principle applies to harmonic functions (real and imaginary parts of holomorphic functions) and underlies the maximum principle used throughout partial differential equations.
