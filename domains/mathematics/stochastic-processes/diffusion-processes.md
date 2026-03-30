---
id: diffusion-processes
title: Diffusion Processes
domain: mathematics
course: stochastic-processes
prerequisites:
- id: stochastic-differential-equations
  type: hard
- id: kolmogorov-equations
  type: hard
- id: continuous-time-markov-chains
  type: soft
tags:
- diffusion
- generator
- scale-function
- speed-measure
stage: expert
status: validated
---

# Diffusion Processes

## Core Idea
A diffusion process is a continuous-path strong Markov process, typically the solution of an SDE dX = μ(x)dt + σ(x)dW. Its behavior is characterized by the infinitesimal generator Lf = μf' + (1/2)σ²f'', the scale function s(x) = ∫exp(-2∫μ/σ² dy)dx (which determines the direction of drift), and the speed measure m(dx) = 2dx/(σ²(x)s'(x)) (which determines how long the process spends near each point). Together, scale and speed classify every one-dimensional diffusion's boundary behavior and long-run properties.

## Questions

```yaml
- question: "The scale function s(x) of a diffusion dX = μ(x)dt + σ(x)dW transforms the process into a local martingale: s(X(t)) is a local martingale. What does this mean for the original process?"
  type: multiple-choice
  options:
    - "The process X(t) is itself a martingale in disguise"
    - "The drift has been 'factored out' — s maps X to a process with no directional tendency, isolating the effect of volatility"
    - "The process X(t) has zero quadratic variation after the transformation"
    - "The scale function s is constant, meaning X is already a local martingale"
  answer: 1
  explanation: "By Itô's formula, s(X) satisfies ds(X) = s'(X)σ(X)dW (the drift term vanishes by construction of s). This means s(X) is a local martingale — a process with no drift, only diffusion. The scale function 'straightens out' the drift: in the s-coordinate, the process is directionless and moves like a time-changed Brownian motion. The original drift μ(x) is encoded in the nonlinearity of s — regions where s changes rapidly correspond to regions where the drift is strong."

- question: "For the Ornstein-Uhlenbeck process dX = -θX dt + σ dW, the scale function is s(x) = ∫₀ˣ exp(θy²/σ²) dy. Since s(x) → ±∞ as x → ±∞, both boundaries ±∞ are:"
  type: multiple-choice
  options:
    - "Entrance boundaries — the process can start there but never reach them"
    - "Natural boundaries — the process can never reach ±∞, and the boundaries are inaccessible"
    - "Exit boundaries — the process reaches ±∞ in finite time"
    - "Regular boundaries — the process can reach and return from ±∞"
  answer: 1
  explanation: "Feller's boundary classification uses the scale function and speed measure. For the OU process, s(x) → ±∞ and the speed measure integral ∫m(dx) over any neighborhood of ±∞ diverges. This means ±∞ are natural boundaries: the process cannot reach them in finite time (from either direction), and they are completely inaccessible. This is consistent with the OU process being positive recurrent — it always returns to the center and has a stationary Gaussian distribution."

- question: "Explain why one-dimensional diffusions are much more tractable than higher-dimensional ones, and what specific tools are available in one dimension that fail in higher dimensions."
  type: short-answer
  answer: "In one dimension, the scale function s(x) and speed measure m(dx) completely characterize the diffusion: boundary behavior (Feller's classification), hitting probabilities (P(hit a before b | start at x) = (s(x)-s(b))/(s(a)-s(b))), stationary distribution (proportional to m(dx) when boundaries are natural), and Green's functions all have explicit formulas. These rely on the fact that a one-dimensional process must pass through every intermediate point to go from a to b — there's no way to 'go around.' In two or more dimensions, the process can bypass points, the scale function doesn't exist as a scalar function, and classification requires PDE methods (Dirichlet problems) rather than ODE methods."
  explanation: "The one-dimensional theory is a complete theory: every question about a diffusion on an interval can be answered in terms of s and m. The passage from ODE (one dimension) to PDE (higher dimensions) is the fundamental reason the theory becomes harder. Higher-dimensional diffusions are studied primarily through their generators (elliptic operators) and Kolmogorov equations."
```

## Explainer

A **diffusion process** is the continuous-time, continuous-path Markov process that arises as the solution of an SDE dX = μ(x)dt + σ(x)dW with σ(x) > 0. The term "diffusion" refers to both the process and the PDE framework (Fokker-Planck equation) that describes its density evolution. Diffusions are the natural continuous-state extension of continuous-time Markov chains: where CTMCs jump between discrete states with exponential holding times, diffusions move continuously through the real line (or higher-dimensional space) driven by noise.

The **infinitesimal generator** Lf(x) = μ(x)f'(x) + (1/2)σ²(x)f''(x) is the fundamental operator associated with the diffusion. For any sufficiently smooth function f, the process f(X(t)) - ∫₀ᵗ Lf(X(s))ds is a local martingale — the generator L computes the expected instantaneous rate of change of f along the process. The backward Kolmogorov equation ∂u/∂t = Lu governs expectations; the forward (Fokker-Planck) equation ∂ρ/∂t = L*ρ governs the density evolution. The generator is the single object from which all probabilistic and analytical information about the diffusion can be extracted.

In one dimension, the theory is remarkably complete thanks to two functions: the **scale function** s(x) and the **speed measure** m(dx). The scale function s(x) = ∫exp(-2∫₀ˣ μ(y)/σ²(y) dy)dx transforms the diffusion into a local martingale: s(X(t)) has no drift. It determines hitting probabilities — the probability of reaching level a before level b, starting from x, is (s(x)-s(b))/(s(a)-s(b)). The speed measure m(dx) = 2dx/(σ²(x)s'(x)) determines how long the process spends near each point. Together, s and m classify the boundary behavior (Feller's classification into regular, exit, entrance, and natural boundaries) and determine the stationary distribution (proportional to m when it has finite total mass).

**Feller's boundary classification** is the capstone of one-dimensional diffusion theory. Each boundary point is classified as: **regular** (reached in finite time, from which the process can return), **exit** (reached in finite time but not returned from), **entrance** (not reached from the interior but can be a starting point), or **natural** (inaccessible from either direction). For the OU process, both ±∞ are natural boundaries — the mean-reverting drift prevents escape. For Brownian motion with drift μ > 0, +∞ is natural but -∞ is also natural (the drift pushes rightward, but the process is recurrent only if μ = 0). These classifications, computed entirely from the scale function and speed measure, determine the long-run behavior and the need for boundary conditions.
