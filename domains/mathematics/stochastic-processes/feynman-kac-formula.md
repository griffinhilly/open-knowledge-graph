---
id: feynman-kac-formula
title: Feynman-Kac Formula
domain: mathematics
course: stochastic-processes
prerequisites:
- id: itos-formula
  type: hard
- id: stochastic-differential-equations
  type: hard
- id: heat-equation-pde
  type: soft
tags:
- feynman-kac
- pde-sde-connection
- parabolic-pde
stage: expert
status: validated
---

# Feynman-Kac Formula

## Core Idea
The Feynman-Kac formula connects solutions of parabolic PDEs to expectations of stochastic processes. If u(x,t) solves ∂u/∂t + μ(x)∂u/∂x + (1/2)σ²(x)∂²u/∂x² - r(x)u = 0 with terminal condition u(x,T) = g(x), then u(x,t) = E[exp(-∫ₜᵀ r(X(s))ds) · g(X(T)) | X(t) = x], where dX = μ dt + σ dW. This provides a probabilistic representation of PDE solutions and a PDE representation of stochastic expectations — a deep bridge between analysis and probability.

## Questions

```yaml
- question: "The Feynman-Kac formula represents the solution of a parabolic PDE as an expectation over paths of a diffusion process. This connection allows you to:"
  type: multiple-choice
  options:
    - "Solve any PDE exactly by computing a single stochastic integral"
    - "Either solve PDEs by Monte Carlo simulation of the diffusion, or solve stochastic problems by PDE methods — the bridge works in both directions"
    - "Replace all PDE theory with probability theory, since the stochastic representation is always more efficient"
    - "Only compute the solution at the boundary, not in the interior of the domain"
  answer: 1
  explanation: "The Feynman-Kac bridge works both ways. Given a PDE, you can estimate its solution by simulating many paths of the corresponding diffusion and averaging the payoff — this is the Monte Carlo method, which scales to high dimensions where grid-based PDE solvers fail. Conversely, given a stochastic expectation E[g(X(T))], you can recognize it as the solution of a PDE and apply analytical or numerical PDE techniques. Neither direction dominates — the choice depends on the dimension, regularity, and structure of the problem."

- question: "In the Black-Scholes model, the option price V(S,t) satisfies the PDE ∂V/∂t + rS·∂V/∂S + (1/2)σ²S²·∂²V/∂S² - rV = 0. Via Feynman-Kac, this PDE is equivalent to:"
  type: multiple-choice
  options:
    - "V(S,t) = E[e^{-r(T-t)} payoff(S(T)) | S(t) = S] under the risk-neutral measure, where dS = rS dt + σS dW̃"
    - "V(S,t) = E[payoff(S(T)) | S(t) = S] under the physical measure, where dS = μS dt + σS dW"
    - "V(S,t) = the probability that S(T) > K"
    - "V(S,t) = e^{-rT}·payoff(S₀)"
  answer: 0
  explanation: "The Black-Scholes PDE is exactly in Feynman-Kac form with drift coefficient rS, diffusion σS, discount rate r, and terminal condition g(S) = payoff(S). The Feynman-Kac representation gives V(S,t) = E[e^{-r(T-t)}g(S(T)) | S(t) = S] where S follows dS = rS dt + σS dW̃. This is the risk-neutral pricing formula — the option price equals the discounted expected payoff under the risk-neutral measure. The connection between the PDE and the expectation is precisely the Feynman-Kac formula."

- question: "Explain why the Feynman-Kac formula is especially useful in high-dimensional problems (e.g., options on multiple assets)."
  type: short-answer
  answer: "Grid-based PDE solvers suffer from the curse of dimensionality: a grid with N points per dimension in d dimensions requires N^d total points, making computation intractable for d > 3-4. The Monte Carlo method from the Feynman-Kac representation simulates independent paths of the d-dimensional diffusion and averages the payoff. The convergence rate of Monte Carlo (1/√n for n paths) is independent of dimension — 10,000 paths give roughly the same accuracy whether d = 1 or d = 100. This dimension-independence makes the stochastic representation computationally superior for high-dimensional PDEs."
  explanation: "The Feynman-Kac formula transforms a d-dimensional PDE into an expectation over d-dimensional diffusion paths. While the PDE approach requires discretizing a d-dimensional domain, the Monte Carlo approach samples individual paths. Each path is one-dimensional (a sequence of time steps), regardless of d. This is why Monte Carlo pricing dominates in multi-asset derivatives and why the Feynman-Kac connection is practically important, not just theoretically elegant."
```

## Explainer

The **Feynman-Kac formula** is one of the deepest connections in mathematics: it equates solutions of partial differential equations with expectations of stochastic processes. The formula states that the solution of the parabolic PDE ∂u/∂t + μ(x)∂u/∂x + (1/2)σ²(x)∂²u/∂x² - r(x)u = 0 with terminal condition u(x,T) = g(x) can be represented as u(x,t) = E[exp(-∫ₜᵀ r(X(s))ds) · g(X(T)) | X(t) = x], where X follows the SDE dX = μ(X)dt + σ(X)dW. The PDE coefficients μ, σ determine the dynamics of the process; the terminal condition g determines the payoff; the coefficient r introduces discounting.

The proof in one direction (from stochastic representation to PDE) uses Itô's formula directly. Define u(x,t) = E[e^{-∫r ds} g(X(T)) | X(t) = x] and consider the process M(s) = e^{-∫ₜˢ r du} u(X(s), s) for s ∈ [t,T]. Apply Itô's formula to M: the drift must be zero because M is a martingale (it is a conditional expectation process). Setting the drift to zero yields exactly the PDE. The converse direction (from PDE solution to stochastic representation) reverses this argument: if u solves the PDE, then M(s) = e^{-∫ₜˢ r du} u(X(s), s) has zero drift by Itô's formula, hence is a martingale. Taking expectations at s = T gives u(x,t) = E[e^{-∫r ds} g(X(T)) | X(t) = x].

This bridge works in both directions practically. Given a PDE, you can solve it by simulating diffusion paths and averaging — this is the **Monte Carlo method**, which excels in high dimensions where grid-based PDE solvers fail catastrophically due to the curse of dimensionality. Conversely, given a stochastic expectation, you can write down the corresponding PDE and apply analytical techniques (separation of variables, Green's functions, transform methods) or efficient numerical PDE solvers. The choice depends on the problem structure: low-dimensional problems with smooth coefficients favor PDE methods; high-dimensional problems or problems with complex path-dependent payoffs favor Monte Carlo.

In mathematical finance, the Feynman-Kac formula is the link between the **Black-Scholes PDE** and **risk-neutral pricing**. The Black-Scholes PDE ∂V/∂t + rS(∂V/∂S) + (1/2)σ²S²(∂²V/∂S²) - rV = 0 is in exact Feynman-Kac form with the risk-neutral drift rS, diffusion σS, and discount rate r. The formula gives V(S,t) = E_Q[e^{-r(T-t)} payoff(S_T)], recovering the risk-neutral pricing formula. Richard Feynman arrived at this formula from the physics side (path integrals in quantum mechanics); Mark Kac gave the rigorous mathematical proof. The formula reveals that PDEs and expectations are two languages for the same mathematics — master both, and you can translate freely between them.
