---
id: hessian-matrix-second-derivative-test
title: The Hessian Matrix and Second Derivative Test
domain: mathematics
course: multivariable-calculus
prerequisites:
- id: critical-points-extrema-saddle
  type: hard
- id: higher-order-partials
  type: hard
builds-toward:
- unconstrained-optimization
tags:
- hessian
- second-derivative-test
- eigenvalues
stage: formal-systems
status: draft
---

# The Hessian Matrix and Second Derivative Test

## Core Idea
The Hessian matrix H = [[f_xx, f_xy], [f_yx, f_yy]] contains all second partial derivatives. At a critical point, the determinant det(H) and trace tr(H) determine whether it is a local max (det > 0, f_xx > 0), local min (det > 0, f_xx < 0), or saddle point (det < 0).

## Questions

```yaml
- question: "At a critical point of f(x, y), you compute det(H) = −3. What can you conclude?"
  type: multiple-choice
  options:
    - "Local minimum, because the negative value indicates downward curvature"
    - "Local maximum, because the Hessian determinant is negative"
    - "Saddle point, because the Hessian has eigenvalues of opposite signs"
    - "The test is inconclusive — you need higher-order information"
  answer: 2
  explanation: "det(H) < 0 means the Hessian has one positive and one negative eigenvalue — the function curves upward in some directions and downward in others. This is definitively a saddle point. A negative determinant rules out both local minima (which require all positive eigenvalues) and local maxima (all negative). The inconclusive case is det(H) = 0, where an eigenvalue is zero."

- question: "At a critical point, f_xx = 4, f_yy = 2, and f_xy = 3. A student claims this must be a local minimum because f_xx > 0. Is the student correct?"
  type: multiple-choice
  options:
    - "Yes — f_xx > 0 confirms upward curvature, guaranteeing a local minimum"
    - "No — you must also verify f_yy > 0 to confirm a local minimum"
    - "No — det(H) = (4)(2) − (3)² = −1 < 0, so this is a saddle point"
    - "No — you need to compute both eigenvalues explicitly before concluding anything"
  answer: 2
  explanation: "det(H) = f_xx · f_yy − (f_xy)² = 8 − 9 = −1 < 0, so this is a saddle point. The student's error is the key misconception: f_xx > 0 only tells you the curvature in the x-direction is upward. A function can curve upward along x but downward in some other direction — that's a saddle. You need det(H) > 0 AND f_xx > 0 together to conclude local minimum."

- question: "A saddle point occurs when the Hessian matrix has eigenvalues of opposite signs, which is equivalent to det(H) < 0."
  type: true-false
  answer: true
  explanation: "At a saddle point, the function increases along some directions through the critical point and decreases along others. The Hessian captures this: one positive eigenvalue (upward curvature) and one negative eigenvalue (downward curvature). Since det(H) = λ₁ · λ₂, opposite-sign eigenvalues produce det(H) < 0. This is the test condition for a saddle point."

- question: "If the Hessian determinant equals zero at a critical point, the point must be a saddle point."
  type: true-false
  answer: false
  explanation: "det(H) = 0 means at least one eigenvalue is zero — the test is inconclusive. The critical point could be a local minimum, a local maximum, or a saddle — you cannot determine which from the Hessian alone. Higher-order analysis or direct examination of the function's behavior is required. Confusing the inconclusive case (det = 0) with the saddle case (det < 0) is a common error."

- question: "Why is checking f_xx > 0 alone insufficient to classify a critical point of a two-variable function as a local minimum?"
  type: short-answer
  answer: "f_xx > 0 only tells you the function curves upward in the x-direction at that point. A function of two variables can curve upward along x and downward along some other direction — making the point a saddle, not a minimum. To guarantee a local minimum, the function must curve upward in every direction simultaneously, which requires the Hessian to be positive definite. This is captured by det(H) > 0 AND f_xx > 0 together."
  explanation: "The single-variable test works because there is only one direction. In two or more variables, upward curvature must hold along every direction through the critical point. The Hessian encodes curvature in all directions via its eigenvalues, and positive definiteness (all eigenvalues > 0) is the correct generalization of f''(c) > 0. Checking just f_xx is equivalent to checking curvature only along the x-axis and ignoring all others."
```

## Explainer

You already know how to find critical points of a multivariable function: set ∇f = 0 and solve. A critical point could be a local minimum, a local maximum, or a saddle point. In single-variable calculus, the second derivative test resolves this cleanly: f''(c) > 0 means the function curves upward, giving a local minimum; f''(c) < 0 means downward curvature, giving a local maximum. The **Hessian matrix** extends this idea to higher dimensions, packaging all second-order information into a matrix that captures curvature in every direction simultaneously.

For f: R² → R, the Hessian is H = [[f_xx, f_xy], [f_yx, f_yy]]. Since Clairaut's theorem guarantees f_xy = f_yx under continuity, H is symmetric. The question at a critical point is: does f curve upward in every direction (local min), downward in every direction (local max), or upward in some directions and downward in others (saddle)? That question is exactly whether H is **positive definite**, **negative definite**, or **indefinite** — which is determined by the signs of its eigenvalues. Positive definite means all eigenvalues are positive (upward curvature in every direction); negative definite means all eigenvalues are negative; indefinite means mixed signs.

For the 2×2 Hessian, the eigenvalue structure reduces to two computable numbers: det(H) = f_xx · f_yy − (f_xy)² and f_xx. If det(H) > 0 and f_xx > 0, the Hessian is positive definite: both eigenvalues are positive, the function curves upward in every direction from the critical point, and you have a **local minimum**. If det(H) > 0 and f_xx < 0, the Hessian is negative definite: both eigenvalues are negative, downward curvature everywhere, giving a **local maximum**. If det(H) < 0, the eigenvalues have opposite signs, giving a **saddle point** — one direction curves up, another down. When det(H) = 0, an eigenvalue is zero and the test is inconclusive.

The geometric intuition for saddle points is worth dwelling on. At a saddle the function increases along some paths through the critical point and decreases along others — like the center of a mountain pass, which is a local maximum along the ridge but a local minimum along the crossing direction. The Hessian test at such a point has one positive and one negative eigenvalue, hence negative determinant. In optimization applications, saddle points are critical to identify because gradient descent can stall near them, mistaking them for minima. For higher-dimensional functions, the full spectrum of the Hessian — not just its determinant — governs the classification, making eigenvalue analysis the natural tool.
