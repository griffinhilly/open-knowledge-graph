---
id: distribution-theory-pdes
title: Distribution Theory and Generalized Functions
domain: mathematics
course: partial-differential-equations
prerequisites:
- id: fundamental-solutions-pdes
  type: hard
- id: lebesgue-integral
  type: hard
- id: dirac-delta-function
  type: soft
tags: [pde, distribution, generalized-function, schwartz, test-function]
stage: expert
status: validated
---
# Distribution Theory and Generalized Functions

## Core Idea
Distribution theory, developed by Laurent Schwartz, provides a rigorous framework for objects like the Dirac delta function that are not ordinary functions. A distribution is a continuous linear functional on a space of smooth test functions. Every locally integrable function defines a distribution, but distributions also include singular objects (delta functions, their derivatives) that arise naturally as fundamental solutions and weak limits. Within distribution theory, every distribution has derivatives of all orders, every constant-coefficient PDE has a fundamental solution, and operations like convolution and Fourier transform extend naturally.

## Questions
```yaml
- question: "In distribution theory, the derivative of a distribution T is defined by:"
  type: multiple-choice
  options:
    - "⟨T', φ⟩ = -⟨T, φ'⟩ for all test functions φ"
    - "⟨T', φ⟩ = ⟨T, φ'⟩ for all test functions φ"
    - "T'(x) = lim_{h→0} (T(x+h) - T(x))/h"
    - "⟨T', φ⟩ = d/dx ⟨T, φ⟩"
  answer: 0
  explanation: "The derivative is defined by transferring the derivative to the test function with a sign change, generalizing integration by parts: ∫f'φ dx = -∫fφ' dx. This definition ensures that every distribution has derivatives of all orders."
- question: "The Dirac delta distribution δ is defined as a function that is infinite at the origin and zero elsewhere."
  type: true-false
  answer: false
  explanation: "The delta distribution is NOT a function at all. It is a continuous linear functional defined by ⟨δ, φ⟩ = φ(0) for all test functions φ. The informal description 'infinite at the origin' is a useful heuristic but mathematically incorrect—no function (even in the Lebesgue sense) has this property while integrating to 1."
- question: "What does the Malgrange-Ehrenpreis theorem guarantee?"
  type: short-answer
  answer: "Every constant-coefficient linear partial differential operator has a fundamental solution (distribution solving LΦ = δ)"
  explanation: "This is a foundational existence theorem in distribution theory. While the fundamental solution may not be a classical function (it could be a genuine distribution), its existence means every constant-coefficient PDE Lu = f with f a distribution has a solution u = Φ * f."
- question: "The space of test functions D(ℝⁿ) consists of:"
  type: multiple-choice
  options:
    - "C^∞ functions with compact support"
    - "All continuous functions"
    - "L² functions"
    - "Schwartz class functions (rapid decrease)"
  answer: 0
  explanation: "Test functions are infinitely differentiable functions that vanish outside a bounded set. The Schwartz space S(ℝⁿ) of rapidly decreasing functions is a larger space that also supports a distribution theory (tempered distributions), which is better suited for Fourier analysis."
```

## Explainer
Distribution theory resolves a fundamental tension in PDE theory: many important objects—point sources, shock waves, fundamental solutions—are not ordinary functions, yet they appear naturally and must be manipulated rigorously. Before Schwartz's theory (1950s), mathematicians used delta functions and their derivatives informally, relying on physical intuition without a solid mathematical foundation. Distribution theory provides this foundation by shifting the focus from values at points to the action on test functions.

A distribution T on ℝⁿ is a continuous linear functional on the space D(ℝⁿ) = C_c^∞(ℝⁿ) of smooth, compactly supported test functions. Every locally integrable function f defines a distribution via ⟨T_f, φ⟩ = ∫fφ dx, but the space of distributions is much larger. The Dirac delta ⟨δ, φ⟩ = φ(0), the derivative of the Heaviside function ⟨H', φ⟩ = -⟨H, φ'⟩ = φ(0) = ⟨δ, φ⟩, and even more singular objects like the principal value distribution PV(1/x) are all well-defined distributions. The key insight is that derivatives are defined by duality: ⟨D^α T, φ⟩ = (-1)^|α| ⟨T, D^α φ⟩, transferring derivatives to the infinitely differentiable test function.

The Schwartz space S(ℝⁿ) of rapidly decreasing functions (smooth functions whose derivatives all decay faster than any polynomial) gives rise to tempered distributions S'(ℝⁿ), which is the natural setting for Fourier analysis. The Fourier transform extends to a bijection on S'(ℝⁿ), allowing one to take the Fourier transform of polynomials, delta functions, and other non-integrable objects. This is essential for PDE theory: the Fourier transform of the fundamental solution of the Laplacian in 3D, which grows at infinity, is well-defined as a tempered distribution.

Distribution theory provides the rigorous underpinning for weak solutions of PDEs. A weak solution of Lu = f is a distribution u satisfying the equation in the distributional sense. The regularity theory then asks: when is a distributional solution actually a classical function? The Weyl lemma (every distribution satisfying Δu = 0 is a smooth function) shows that elliptic regularity forces distributional solutions to be smooth—a striking result that demonstrates the power of the distributional framework. For hyperbolic equations, distributional solutions can genuinely be non-smooth (shock waves), and distribution theory provides the correct setting for studying these singularities.
