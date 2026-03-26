---
id: linearization-of-nonlinear-systems
title: Linearization of Nonlinear Systems
domain: mathematics
course: differential-equations
prerequisites:
- id: stability-classification
  type: hard
- id: partial-derivatives
  type: hard
- id: eulers-method
  type: soft
builds-toward: []
tags:
- nonlinear
- approximation
- local-analysis
stage: advanced
status: validated
---
# Linearization of Nonlinear Systems

## Core Idea
For a nonlinear system y' = f(y), linearize near an equilibrium y* by computing the Jacobian matrix J = ∇f(y*). The linearized system y' ≈ J(y - y*) reveals local stability; if J has eigenvalues with Re(λ) ≠ 0, the nonlinear equilibrium inherits the stability of the linearized system.

## Questions

```yaml
- question: "You compute the Jacobian J of a nonlinear system at an equilibrium y* and find that J has eigenvalues λ = ±3i (pure imaginary, zero real part). What can you conclude about the stability of y*?"
  type: multiple-choice
  options:
    - "The equilibrium is a stable center, because the linearization gives a center and the classification carries over"
    - "The equilibrium is unstable, because imaginary eigenvalues indicate sustained oscillations that grow without bound"
    - "Linearization is inconclusive — higher-order terms in the Taylor expansion determine whether the nonlinear equilibrium is a center, stable spiral, or unstable spiral"
    - "The equilibrium is a saddle point, because the eigenvalues have equal and opposite magnitudes"
  answer: 2
  explanation: "Pure imaginary eigenvalues (zero real part) mean the equilibrium is non-hyperbolic — the linearization gives a center (closed orbits), but the nonlinear system could behave quite differently. Higher-order terms can tip the system into a stable spiral (spiraling inward), unstable spiral (spiraling outward), or genuine center. The Hartman-Grobman theorem that makes linearization valid requires all eigenvalues to have nonzero real part. When Re(λ) = 0, the linearization cannot determine nonlinear stability — additional analysis (Lyapunov functions, Poincaré index, higher-order terms) is required."

- question: "Which condition must be satisfied for the Jacobian linearization to correctly predict the qualitative stability behavior of the nonlinear equilibrium?"
  type: multiple-choice
  options:
    - "The Jacobian must be a 2×2 matrix — linearization only works for 2-dimensional systems"
    - "All eigenvalues of the Jacobian must have negative real parts — the equilibrium must be stable"
    - "The equilibrium must be hyperbolic — all eigenvalues of the Jacobian must have nonzero real parts"
    - "The nonlinear terms must be globally small relative to the linear terms throughout the entire phase plane"
  answer: 2
  explanation: "Hyperbolicity — Re(λ) ≠ 0 for all eigenvalues — is the essential condition for the Hartman-Grobman theorem. When satisfied, the nonlinear system near y* is topologically equivalent to the linearized system, so stable nodes, unstable nodes, saddles, and spirals all carry over from the linearization. The condition is local (applies near the equilibrium), not global, so the size of nonlinear terms far from y* is irrelevant. The condition says nothing about the sign of the real parts — saddles and sources (positive real parts) are also hyperbolic, and linearization correctly identifies them as unstable."

- question: "Linearization of a nonlinear system at an equilibrium tells us about the global behavior of the system — whether most solutions throughout the phase plane eventually converge to that equilibrium."
  type: true-false
  answer: false
  explanation: "Linearization is strictly a local technique. It approximates the nonlinear vector field near a specific equilibrium using the first-order Taylor expansion (the Jacobian), and the resulting stability classification applies only in a neighborhood of that equilibrium. A system can have a locally stable equilibrium (all nearby solutions converge to it) while having other equilibria that are unstable, or even globally divergent behavior far from y*. Global stability analysis requires different tools — Lyapunov functions, invariant sets, or phase portrait construction."

- question: "If the Jacobian at an equilibrium of a nonlinear system has one positive and one negative real eigenvalue (a saddle in the linearization), the nonlinear system also behaves like a saddle near that equilibrium."
  type: true-false
  answer: true
  explanation: "Saddle points are hyperbolic (both eigenvalues have nonzero real parts, one positive and one negative), so the Hartman-Grobman theorem applies. The nonlinear system near this equilibrium is topologically equivalent to the linearized saddle: there are stable and unstable manifolds along which solutions approach or leave the equilibrium, and generic nearby trajectories are deflected away. The saddle classification carries over from the linearization exactly, unlike the center case where pure imaginary eigenvalues make the classification inconclusive."

- question: "Why is the hyperbolicity condition — that all eigenvalues of the Jacobian have nonzero real part — essential for linearization to determine the stability of the nonlinear equilibrium?"
  type: short-answer
  answer: "The Hartman-Grobman theorem guarantees that a hyperbolic equilibrium of a nonlinear system is topologically equivalent to its linearization — the qualitative behavior (stable/unstable node, saddle, stable/unstable spiral) carries over exactly. When an eigenvalue has zero real part, this topological equivalence breaks down: the linearization gives a center (closed orbits), but the nonlinear higher-order terms can perturb this into a stable spiral, unstable spiral, or genuine center depending on their sign and magnitude. Linearization discards these higher-order terms, so it cannot determine which case applies. The hyperbolicity condition is precisely what ensures the discarded terms don't change the qualitative picture."
  explanation: "This is the key limitation of linearization as a stability tool. For the vast majority of equilibria in practice — stable nodes, unstable nodes, saddles, spirals — the eigenvalues have nonzero real part and linearization works perfectly. The center case is special and relatively rare, but important to recognize because treating a linearized center as a nonlinear center can produce dramatically wrong predictions about long-term behavior."
```

## Explainer

From stability classification, you can fully analyze linear systems x' = Ax: find the eigenvalues of A, and the signs of their real parts tell you whether the equilibrium at the origin is a stable node, unstable node, saddle, or spiral. Nonlinear systems are far harder in general — their phase portraits can be wildly complicated. But *near* a specific equilibrium, every smooth nonlinear system looks approximately linear, and this approximation is good enough to determine local stability. Linearization is the technique that makes this precise.

The idea comes directly from your work with partial derivatives. If f : Rⁿ → Rⁿ is a smooth vector field and y* is an equilibrium (so f(y*) = 0), then the **Taylor expansion** of f near y* starts: f(y) ≈ f(y*) + J(y − y*) + higher-order terms, where J = ∇f(y*) is the **Jacobian matrix** — the matrix of all first partial derivatives of f, evaluated at y*. Since f(y*) = 0, we get f(y) ≈ J(y − y*). Setting u = y − y* (the displacement from equilibrium), the nonlinear system y' = f(y) becomes approximately the linear system u' = Ju. This linear system you already know how to analyze completely.

The key theorem is that if every eigenvalue of J has a nonzero real part (the equilibrium is **hyperbolic**), then the qualitative behavior of the nonlinear system near y* is topologically the same as the behavior of the linear approximation. A stable node in the linearization means the nonlinear equilibrium is locally asymptotically stable; a saddle in the linearization means the nonlinear equilibrium is unstable; a source means unstable. The classification table from linear systems carries over exactly — stable node, unstable node, saddle, stable spiral, unstable spiral. The only gap is the **center case**: if J has pure imaginary eigenvalues (zero real part), the linear approximation gives a center, but the nonlinear system could be a center, a stable spiral, or an unstable spiral depending on higher-order terms. This is why the hyperbolicity condition Re(λ) ≠ 0 is essential.

In practice, linearization is a three-step process: (1) find the equilibria by solving f(y*) = 0, (2) compute the Jacobian J = ∇f and evaluate it at each equilibrium, (3) find the eigenvalues of J and apply the linear stability classification. For a 2D system dx/dt = P(x, y), dy/dt = Q(x, y), the Jacobian is the 2×2 matrix [[∂P/∂x, ∂P/∂y], [∂Q/∂x, ∂Q/∂y]] evaluated at the equilibrium point. This technique is the standard first tool for analyzing nonlinear systems in applications ranging from population ecology to mechanical engineering to epidemiology.
