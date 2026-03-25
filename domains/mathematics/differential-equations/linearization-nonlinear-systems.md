---
id: linearization-nonlinear-systems
title: Linearization of Nonlinear Systems Near Equilibria
domain: mathematics
course: differential-equations
prerequisites:
- id: stability-classification
  type: hard
- id: partial-derivatives
  type: hard
- id: linearization-of-nonlinear-systems
  type: soft
tags:
- linearization
- jacobian
- local-analysis
stage: advanced
status: validated
---
# Linearization of Nonlinear Systems Near Equilibria

## Core Idea
For a nonlinear system dx/dt = f(x) near equilibrium x*, compute the Jacobian J = ∂f/∂x at x*. The linearized system dx/dt ≈ J(x - x*) determines local behavior. If all eigenvalues of J have non-zero real parts, the nonlinear stability matches the linear prediction (Hartman-Grobman theorem). Linearization provides local information when global analysis is infeasible.

## Questions

```yaml
- question: "You linearize a nonlinear system at an equilibrium and find the Jacobian has eigenvalues λ = ±2i (purely imaginary). You conclude the equilibrium is a center. What does the Hartman-Grobman theorem say about this conclusion?"
  type: multiple-choice
  options:
    - "The theorem confirms your conclusion: purely imaginary eigenvalues always produce a center in both the linear and nonlinear system"
    - "The theorem is silent here: purely imaginary eigenvalues make the equilibrium non-hyperbolic, so the theorem does not apply and higher-order terms must determine actual stability"
    - "The theorem says the equilibrium is unstable, because imaginary eigenvalues indicate oscillatory growth"
    - "The theorem guarantees the conclusion is correct only if the system is two-dimensional"
  answer: 1
  explanation: "Hartman-Grobman applies only to hyperbolic equilibria — those where all eigenvalues of the Jacobian have non-zero real parts. Purely imaginary eigenvalues have zero real part, so the equilibrium is non-hyperbolic and the theorem gives no guarantee. A linear center can correspond to a nonlinear center, spiral, or even a node depending on higher-order terms. This is a critical limitation: you cannot trust the linearization at centers."

- question: "What is the Jacobian matrix J = ∂f/∂x, and why is it the correct tool for linearizing a nonlinear system ẋ = f(x) near an equilibrium x*?"
  type: multiple-choice
  options:
    - "The Jacobian is the Hessian matrix of second derivatives, capturing curvature of f near x*"
    - "The Jacobian is the matrix of partial derivatives ∂fᵢ/∂xⱼ evaluated at x*; it is the best linear approximation of f near x*, analogous to the derivative for single-variable functions"
    - "The Jacobian is the matrix whose eigenvalues are the natural frequencies of the system, valid globally"
    - "The Jacobian is only applicable when f is a polynomial function; for other functions, a different linearization tool is needed"
  answer: 1
  explanation: "The Jacobian is the multivariable generalization of the derivative: just as f(x) ≈ f(x*) + f'(x*)(x − x*) for a scalar function, the Taylor expansion of a vector field gives f(x) ≈ f(x*) + J(x − x*). Since f(x*) = 0 at an equilibrium, this reduces the nonlinear system to ẋ ≈ J·u, where u = x − x*. The Jacobian is valid only locally near x*, not globally."

- question: "If the Jacobian of a nonlinear system at an equilibrium has eigenvalues with negative real parts, the equilibrium is definitely a stable spiral or node in the original nonlinear system."
  type: true-false
  answer: false
  explanation: "This is almost right but misses the hyperbolicity condition. Negative real parts guarantee the linearization predicts stability, but Hartman-Grobman requires that the real parts be strictly non-zero (not merely negative). If all eigenvalues have strictly negative real parts, the equilibrium IS hyperbolic and the nonlinear system is indeed locally stable — but the conclusion follows from hyperbolicity, not merely from negativity. The statement as written would be false if one eigenvalue had real part exactly 0, even if others were negative."

- question: "Linearization of a nonlinear system gives valid stability information only locally, near the specific equilibrium where the Jacobian was computed."
  type: true-false
  answer: true
  explanation: "This is the fundamental limitation of linearization. The Jacobian is derived from a first-order Taylor expansion of f around x*, so it approximates f accurately only when x is close to x*. For behavior far from the equilibrium — large-amplitude oscillations, trajectories near other equilibria, global attractors — the linearization says nothing. Global analysis requires other tools (Lyapunov functions, phase plane analysis, numerical simulation)."

- question: "What does it mean for an equilibrium to be 'hyperbolic,' and why is hyperbolicity the condition required for the Hartman-Grobman theorem to guarantee that the linearization correctly predicts qualitative behavior?"
  type: short-answer
  answer: "An equilibrium is hyperbolic if all eigenvalues of the Jacobian J have strictly non-zero real parts — none lie on the imaginary axis. Hyperbolicity guarantees that the linearization is 'structurally stable': small perturbations (including the higher-order terms that make f nonlinear) cannot qualitatively change the phase portrait near x*. When eigenvalues have zero real part (as with centers or degenerate cases), even tiny nonlinear terms can tip the system from stable to unstable or change the topology entirely. Hartman-Grobman needs hyperbolicity precisely because non-hyperbolic cases sit at a boundary where qualitative behavior is structurally fragile."
  explanation: "The practical upshot: trust the linearization when eigenvalues have clear positive or negative real parts (saddles, spirals, nodes). Be suspicious when real parts are zero. Centers (±iω) require Lyapunov methods or higher-order analysis to resolve stability. Zero eigenvalues indicate bifurcations, where the system's behavior changes qualitatively as parameters vary."
```

## Explainer

From your work on stability classification, you know how to fully analyze a linear system ẋ = Ax: find eigenvalues of A, determine whether their real parts are positive, negative, or zero, and classify the equilibrium at the origin as a stable node, unstable node, saddle, spiral, or center. For a nonlinear system ẋ = f(x), the same classification is not directly available — f is not a matrix, and eigenvalues of a nonlinear system are not defined. Linearization closes this gap by approximating f with the best linear approximation near an equilibrium.

The approximation tool is the **Jacobian matrix**: J = ∂f/∂x evaluated at the equilibrium x*. Each entry J_{ij} = ∂fᵢ/∂xⱼ(x*) measures how the i-th component of f changes with the j-th variable, evaluated at the fixed point. This comes directly from your prerequisite on partial derivatives — the Jacobian is the multivariable generalization of the derivative. Near x*, the Taylor expansion of f gives f(x) ≈ f(x*) + J(x − x*), and since f(x*) = 0 at an equilibrium, the system becomes ẋ ≈ J(x − x*). With the substitution u = x − x*, this is the linear system u̇ = Ju, which you already know how to classify.

The **Hartman-Grobman theorem** tells you when this linearization gives reliable local stability information: if all eigenvalues of J have **non-zero real parts** (a condition called hyperbolicity), the qualitative phase portrait of the nonlinear system near x* is topologically equivalent to the portrait of the linearization. In other words, if the linearization says "stable spiral," the nonlinear system really does spiral inward near x*. Hyperbolicity fails at centers (purely imaginary eigenvalues) and at degenerate cases (zero eigenvalues) — in those cases, the linear approximation is ambiguous about stability, and higher-order terms in the Taylor expansion must be examined.

The procedure is: find all equilibria by solving f(x*) = 0, compute J at each equilibrium, find the eigenvalues of each J, classify each equilibrium from the eigenvalues, and note any non-hyperbolic cases requiring further analysis. For a 2D system dx/dt = P(x,y), dy/dt = Q(x,y), the Jacobian is the 2×2 matrix [[∂P/∂x, ∂P/∂y], [∂Q/∂x, ∂Q/∂y]], and the eigenvalues follow from the characteristic polynomial λ² − (trace)λ + det = 0. The trace and determinant of J provide the fastest route to classification: det < 0 means a saddle; det > 0 and trace < 0 means stable; det > 0 and trace > 0 means unstable; the discriminant distinguishes spirals from nodes. Linearization converts a hard nonlinear problem into a sequence of linear ones you already know how to solve.
