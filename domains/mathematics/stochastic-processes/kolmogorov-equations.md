---
id: kolmogorov-equations
title: Kolmogorov Forward and Backward Equations
domain: mathematics
course: stochastic-processes
prerequisites:
- id: stochastic-differential-equations
  type: hard
- id: itos-formula
  type: hard
- id: heat-equation-pde
  type: soft
tags:
- kolmogorov-equations
- fokker-planck
- transition-density
- parabolic-pde
stage: expert
status: validated
---

# Kolmogorov Forward and Backward Equations

## Core Idea
The Kolmogorov equations describe how the transition density p(x,t; y,T) of a diffusion dX = μ(X)dt + σ(X)dW evolves. The backward equation ∂p/∂t + μ(x)∂p/∂x + (1/2)σ²(x)∂²p/∂x² = 0 acts on the initial variables (x,t). The forward equation (Fokker-Planck) ∂p/∂T = -(∂/∂y)[μ(y)p] + (1/2)(∂²/∂y²)[σ²(y)p] acts on the final variables (y,T). Together they characterize the full probabilistic evolution of diffusion processes.

## Questions

```yaml
- question: "The Kolmogorov backward equation acts on the initial point (x,t), while the forward equation acts on the terminal point (y,T). Which equation would you use to find the stationary (equilibrium) density of a diffusion?"
  type: multiple-choice
  options:
    - "The backward equation, since stationarity is a condition on initial states"
    - "The forward equation (Fokker-Planck), since setting ∂p/∂T = 0 gives the equation for the time-independent equilibrium density"
    - "Neither — stationary densities require ergodic theory, not Kolmogorov equations"
    - "Both equations simultaneously, since stationarity constrains both initial and final conditions"
  answer: 1
  explanation: "The stationary density π(y) satisfies the time-independent Fokker-Planck equation: 0 = -(d/dy)[μ(y)π(y)] + (1/2)(d²/dy²)[σ²(y)π(y)]. This is an ODE that can often be solved explicitly — for example, the OU process dX = -θX dt + σ dW has stationary density proportional to exp(-θx²/σ²), which is Gaussian N(0, σ²/2θ). The backward equation is the wrong tool here because the stationary density describes the long-run distribution of the terminal state, not a function of the initial state."

- question: "The Fokker-Planck (forward) equation for the process dX = dW (pure Brownian motion, no drift) is:"
  type: multiple-choice
  options:
    - "∂p/∂T = (1/2)∂²p/∂y², the heat equation"
    - "∂p/∂T = ∂p/∂y, the transport equation"
    - "∂p/∂T = -∂²p/∂y², the backward heat equation"
    - "∂p/∂T = p, exponential growth"
  answer: 0
  explanation: "With μ = 0 and σ = 1, the Fokker-Planck equation becomes ∂p/∂T = (1/2)∂²p/∂y². This is the classical heat equation. The fundamental solution (starting from p(y,0) = δ(y-x)) is the Gaussian kernel p(y,T) = (2πT)^{-1/2}exp(-(y-x)²/(2T)), which is exactly the transition density of Brownian motion. The connection between Brownian motion and the heat equation — heat diffuses like probability diffuses — was one of the key insights of early 20th century mathematical physics."

- question: "Explain the physical/probabilistic interpretation of the two terms in the Fokker-Planck equation ∂p/∂T = -(∂/∂y)[μp] + (1/2)(∂²/∂y²)[σ²p]."
  type: short-answer
  answer: "The first term -(∂/∂y)[μp] is the transport (advection) term: it describes how the drift μ(y) shifts probability mass in the direction of the drift. If all particles have the same drift, probability is carried along like fluid in a flow. The second term (1/2)(∂²/∂y²)[σ²p] is the diffusion term: it describes how noise spreads probability mass, smearing concentrated distributions into broader ones. The balance between transport and diffusion determines the evolving shape of the density. In steady state (∂p/∂T = 0), the inward transport from mean reversion exactly balances the outward diffusion from noise."
  explanation: "This interpretation parallels the convection-diffusion equation in physics. The transport term preserves the total mass (probability) while moving it; the diffusion term also preserves total mass while spreading it. Their interplay determines whether the process converges to a stationary distribution (when drift dominates at large |y|) or diffuses to infinity (when drift is too weak)."
```

## Explainer

The **Kolmogorov equations** describe how the probability density of a diffusion process evolves in time. For the process dX = μ(X)dt + σ(X)dW with transition density p(x,t; y,T) = P(X(T) ∈ dy | X(t) = x)/dy, there are two complementary PDEs. The **backward equation** ∂p/∂t + μ(x)∂p/∂x + (1/2)σ²(x)∂²p/∂x² = 0 treats the terminal point (y,T) as fixed and differentiates with respect to the initial point (x,t). The **forward equation** (Fokker-Planck) ∂p/∂T = -(∂/∂y)[μ(y)p] + (1/2)(∂²/∂y²)[σ²(y)p] treats the initial point (x,t) as fixed and differentiates with respect to the terminal point (y,T).

The backward equation is a direct consequence of Itô's formula and the Feynman-Kac connection. If u(x,t) = E[g(X(T)) | X(t) = x], then u satisfies ∂u/∂t + μ(x)∂u/∂x + (1/2)σ²(x)∂²u/∂x² = 0 — this is the backward equation with g as terminal data. The transition density is the special case where g is a delta function: u(x,t) = p(x,t; y,T). The backward equation's differential operator L = μ∂/∂x + (1/2)σ²∂²/∂x² is called the **infinitesimal generator** of the diffusion, and it encodes how the process moves locally.

The **forward equation** describes how an entire distribution evolves. If at time t the process has density ρ(y,t), then ρ evolves by ∂ρ/∂t = -(∂/∂y)[μ(y)ρ] + (1/2)(∂²/∂y²)[σ²(y)ρ]. The operator on the right is the formal adjoint L* of the generator L. The two terms have clear physical meanings: -(∂/∂y)[μρ] is advection (drift carries probability in the direction of μ), and (1/2)(∂²/∂y²)[σ²ρ] is diffusion (noise spreads probability). For Brownian motion (μ=0, σ=1), the forward equation reduces to the heat equation ∂ρ/∂t = (1/2)∂²ρ/∂y² — the connection between probability diffusion and heat diffusion that Einstein exploited in his 1905 paper.

**Stationary distributions** are found by setting ∂ρ/∂T = 0 in the forward equation, yielding the ODE 0 = -(d/dy)[μ(y)π(y)] + (1/2)(d²/dy²)[σ²(y)π(y)]. For the Ornstein-Uhlenbeck process (μ(y) = -θy, σ = const), this gives π(y) ∝ exp(-θy²/σ²), confirming the Gaussian stationary distribution. More generally, one-dimensional diffusions with σ(y) > 0 have explicit stationary densities via the formula π(y) ∝ (1/σ²(y))exp(2∫μ(y)/σ²(y) dy), provided this integrates to a finite total. The Kolmogorov equations thus provide a complete toolkit for analyzing the transient and long-run behavior of diffusion processes.
