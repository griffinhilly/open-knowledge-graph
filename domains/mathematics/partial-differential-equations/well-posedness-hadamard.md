---
id: well-posedness-hadamard
title: Well-Posedness and Hadamard's Conditions
domain: mathematics
course: partial-differential-equations
prerequisites:
- id: pde-classification
  type: hard
- id: existence-uniqueness-ode
  type: soft
tags: [pde, well-posedness, hadamard, existence, uniqueness, stability]
stage: advanced
status: validated
---
# Well-Posedness and Hadamard's Conditions

## Core Idea
Hadamard defined a PDE problem as well-posed if it satisfies three conditions: existence (a solution exists for given data), uniqueness (the solution is the only one), and continuous dependence on data (small changes in the data produce small changes in the solution). A problem failing any condition is ill-posed. Well-posedness determines whether a mathematical model is physically meaningful and computationally tractable. The classification of PDEs is intimately linked to well-posedness: each PDE type has specific data requirements (boundary conditions, initial conditions) that make the problem well-posed.

## Questions
```yaml
- question: "Which of Hadamard's three conditions for well-posedness addresses numerical stability?"
  type: multiple-choice
  options:
    - "Existence"
    - "Uniqueness"
    - "Continuous dependence on data"
    - "All three equally"
  answer: 2
  explanation: "Continuous dependence on data ensures that small perturbations in the input (from measurement errors or numerical rounding) produce only small changes in the solution. Without this property, numerical computation of the solution is unreliable because tiny floating-point errors can produce wildly different outputs."
- question: "The backward heat equation u_t = -kΔu is well-posed as an initial value problem."
  type: true-false
  answer: false
  explanation: "The backward heat equation is the classic example of ill-posedness. While solutions may exist and be unique, they do not depend continuously on the data: Fourier modes e^(kn²t) grow exponentially, amplifying any small perturbation in the initial data without bound. This makes the problem catastrophically unstable."
- question: "Why is the Cauchy problem for Laplace's equation (specifying u and u_n on part of the boundary) ill-posed?"
  type: short-answer
  answer: "It violates continuous dependence: Hadamard showed that arbitrarily small oscillatory boundary data can produce arbitrarily large solutions in the interior"
  explanation: "Hadamard's famous counterexample shows that the Cauchy data u = 0, u_y = sin(nx)/n on y = 0 for Laplace's equation produces the solution sinh(ny)sin(nx)/n², which grows exponentially with n despite the data shrinking to zero. This demonstrates catastrophic instability."
- question: "Prescribing Dirichlet boundary conditions for Laplace's equation on a bounded domain is well-posed."
  type: true-false
  answer: true
  explanation: "The Dirichlet problem for Laplace's equation satisfies all three Hadamard conditions: existence follows from Perron's method or variational arguments, uniqueness from the maximum principle, and continuous dependence from the maximum principle applied to the difference of two solutions."
```

## Explainer
Jacques Hadamard introduced the concept of well-posedness in 1902, identifying the three properties that a PDE problem must have to be physically and computationally meaningful. Existence guarantees that the mathematical model has a solution—that the equations are not internally contradictory. Uniqueness ensures that the model makes definite predictions—the physical situation described determines a single outcome. Continuous dependence on data means the model is robust—since physical measurements always contain errors, the predicted solution must not be arbitrarily sensitive to these errors.

The concept of well-posedness is deeply linked to the classification of PDEs. Each type of equation is well-posed with specific types of auxiliary conditions. Elliptic equations like Laplace's equation are well-posed as boundary value problems (specifying u on all of ∂Ω) but ill-posed as initial value problems. Hyperbolic equations like the wave equation are well-posed as initial value problems (specifying u and u_t at t = 0) but require exactly the right amount of boundary data—too much or too little leads to ill-posedness. Parabolic equations like the heat equation are well-posed forward in time but ill-posed backward.

Hadamard's counterexample for the Cauchy problem of Laplace's equation is a landmark in PDE theory. He showed that specifying u and ∂u/∂n on a portion of the boundary does not determine u continuously throughout the domain: oscillatory data with amplitude 1/n produces solutions that grow like e^n. This is not a technicality—it means that no amount of measurement precision on the boundary can reliably predict the solution in the interior from Cauchy data alone.

Despite Hadamard's original intent that ill-posed problems should be avoided, the 20th century revealed that many important practical problems are ill-posed: inverse problems (determining an internal structure from boundary measurements), data assimilation (combining models with noisy observations), and backward-in-time problems all fail continuous dependence. The theory of regularization, developed by Tikhonov and others, provides systematic methods for extracting useful approximate solutions from ill-posed problems by adding stabilizing constraints. Understanding well-posedness remains essential: it tells us which problems can be solved directly and which require the additional machinery of regularization theory.
