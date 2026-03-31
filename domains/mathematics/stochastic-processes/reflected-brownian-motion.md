---
id: reflected-brownian-motion
title: Reflected Brownian Motion
domain: mathematics
course: stochastic-processes
prerequisites:
- id: brownian-motion-stochastic
  type: hard
- id: properties-of-brownian-motion
  type: hard
- id: itos-formula
  type: soft
- id: stochastic-differential-equations
  type: soft
tags:
- reflected-brownian-motion
- skorokhod-problem
- local-time
- boundary-behavior
stage: expert
status: validated
---

# Reflected Brownian Motion

## Core Idea
Reflected Brownian motion (RBM) is a process constrained to stay non-negative by an instantaneous reflection at the origin. It is constructed as |W(t)| (for a standard Brownian motion W) or equivalently as the solution to the Skorokhod reflection problem: X(t) = W(t) + L(t) ≥ 0, where L(t) is the local time at zero — a continuous, non-decreasing process that increases only when X(t) = 0. The local time measures the "time spent at the boundary" in a generalized sense and is central to the study of stochastic processes with reflecting barriers, queueing theory, and free-boundary problems.

## Questions

```yaml
- question: "Let W(t) be standard Brownian motion. Which of the following correctly constructs reflected Brownian motion on [0,∞)?"
  type: multiple-choice
  options:
    - "X(t) = max(W(t), 0), which clips negative excursions to zero"
    - "X(t) = |W(t)|, the absolute value of Brownian motion"
    - "X(t) = W(t)², since squaring ensures non-negativity"
    - "X(t) = W(t) + t, since the drift ensures the process stays positive"
  answer: 1
  explanation: "Reflected Brownian motion on [0,∞) is X(t) = |W(t)|. By the reflection principle, |W(t)| is a continuous semimartingale that stays non-negative and behaves like Brownian motion away from the origin. The 'clipping' option max(W(t), 0) would create a process that stays at zero during negative excursions rather than reflecting, producing a fundamentally different (and non-Markov) process. The absolute value construction is equivalent to the Skorokhod reflection: X(t) = W(t) + L_t^0(W) where L_t^0(W) is the local time of W at zero."

- question: "In the Skorokhod reflection problem, X(t) = W(t) + L(t) where L(t) is the local time at zero. The local time L(t) increases only when X(t) = 0."
  type: true-false
  answer: true
  explanation: "This is the defining property of the Skorokhod construction. The local time L(t) is the minimal non-decreasing process that keeps X(t) ≥ 0. It acts as a 'pushing force' that activates only at the boundary: ∫₀^∞ X(t) dL(t) = 0, meaning L increases only on the set {t : X(t) = 0}. This set has Lebesgue measure zero (X doesn't spend positive time at 0), yet L(t) grows to infinity — it increases on a set that is topologically large (uncountable, dense in the zero set) but measure-theoretically negligible. This subtle behavior is characteristic of local time."

- question: "Tanaka's formula states that |W(t)| = ∫₀ᵗ sgn(W(s)) dW(s) + L_t^0(W). How does this differ from applying the ordinary chain rule to |x|?"
  type: short-answer
  answer: "The ordinary chain rule would give d|W(t)| = sgn(W(t)) dW(t), with no extra term. But |x| is not differentiable at x = 0, and Brownian motion visits 0 often enough that this non-differentiability matters. Tanaka's formula is the Itô formula applied to the convex function |x|: the usual Itô correction term ½f''(x)dt would involve δ₀(W(t))dt — the Dirac delta — which is formally the local time. So L_t^0(W) is the 'Itô correction' accounting for the singularity of |x| at the origin. This shows local time arises naturally from stochastic calculus, not just from the Skorokhod construction."
  explanation: "Tanaka's formula is the prototypical example of a generalized Itô formula for non-smooth functions. The local time term L_t^0 replaces the second-derivative term that would appear if f were smooth. More generally, the Itô-Tanaka formula applies to convex functions f, with the second derivative interpreted as a measure (the second distributional derivative of f), and the local time acting as the occupation density of the process."

- question: "The local time L_t^a(W) of Brownian motion at level a satisfies the occupation times formula: ∫₀ᵗ g(W(s)) ds = ∫_{-∞}^{∞} g(a) L_t^a da for all non-negative Borel functions g. This formula says:"
  type: multiple-choice
  options:
    - "The total time Brownian motion spends in a set A up to time t equals ∫_A L_t^a da"
    - "The local time L_t^a is the probability density of W(t)"
    - "Brownian motion spends equal time at every level"
    - "The occupation times formula holds only for bounded g"
  answer: 0
  explanation: "The occupation times formula is the fundamental identity connecting local time to the time a process spends near each level. Taking g = 1_A, the left side is the Lebesgue measure of {s ∈ [0,t] : W(s) ∈ A} — the occupation time of the set A. The right side is ∫_A L_t^a da. So L_t^a is the density of the occupation measure with respect to Lebesgue measure on ℝ. It is not a probability density (it is not normalized), and Brownian motion does not spend equal time at every level (L_t^a is random and depends on a). The formula holds for all non-negative measurable g."

- question: "In queueing theory, reflected Brownian motion arises as the heavy-traffic limit of the queue length process in a GI/GI/1 queue. Why does reflection appear?"
  type: short-answer
  answer: "In a single-server queue, the workload cannot go negative — when the queue empties, the server idles rather than accumulating 'negative work.' The net input process (arrivals minus service) behaves like a random walk and, after diffusion scaling in heavy traffic, converges to Brownian motion with negative drift. The non-negativity constraint on the queue length corresponds to reflection at zero: when the Brownian approximation would go negative, it is pushed back to zero by the local time, which represents the cumulative idle time of the server. This is exactly the Skorokhod reflection, making RBM the canonical heavy-traffic model."
  explanation: "This connection, established by Kingman, Iglehart, and Whitt, is one of the most important applications of reflected Brownian motion. The heavy-traffic scaling (arrival rate approaching service rate) produces a diffusion limit, and the physical constraint of non-negative queue length forces reflection. Multidimensional RBM (in the orthant ℝ₊ⁿ) models networks of queues, where the reflection directions encode the routing structure."
```

## Explainer

**Reflected Brownian motion** (RBM) is Brownian motion constrained to a domain — most commonly the half-line [0,∞) — by instantaneous elastic reflection at the boundary. The simplest construction takes a standard Brownian motion W(t) and defines X(t) = |W(t)|. By Lévy's theorem, this is equivalent to X(t) = W(t) + L_t^0(W), where L_t^0(W) is the local time of W at zero — a continuous, non-decreasing process that increases only on the (Lebesgue-null) set of times when W(t) = 0. The local time "pushes" the process away from zero just enough to maintain non-negativity.

The **Skorokhod reflection problem** provides the general framework. Given a continuous function w(t) with w(0) ≥ 0, find a pair (x, l) such that x(t) = w(t) + l(t) ≥ 0, where l is non-decreasing with l(0) = 0 and l increases only when x(t) = 0 (formally, ∫₀^∞ x(t) dl(t) = 0). The unique solution is x(t) = w(t) - min(0, inf_{s ≤ t} w(s)) and l(t) = -min(0, inf_{s ≤ t} w(s)) = max_{s ≤ t}(-w(s))⁺. When w is a Brownian path, x is reflected Brownian motion and l is the local time at zero. The Skorokhod map w ↦ x is continuous in the sup-norm topology, which makes it a powerful tool for proving weak convergence of reflected processes (if w_n → w, then the reflected processes converge too).

**Local time** is one of the most subtle objects in stochastic calculus. The local time L_t^a(W) at level a measures how much time Brownian motion spends near a up to time t — but "time spent at a point" has Lebesgue measure zero for a continuous process, so local time captures something finer. It is defined through the **occupation times formula**: ∫₀ᵗ g(W(s))ds = ∫_{-∞}^∞ g(a) L_t^a da. The local time is the Radon-Nikodym derivative of the occupation measure (time spent in each region) with respect to Lebesgue measure. As a function of a, L_t^a(W) is a.s. continuous (jointly in t and a for Brownian motion). As a function of t, L_t^a is non-decreasing and grows on the (topologically large but measure-zero) set of times when W visits a.

**Tanaka's formula** connects local time to stochastic calculus: |W(t)| = ∫₀ᵗ sgn(W(s)) dW(s) + L_t^0(W). This is the Itô formula applied to the non-smooth function f(x) = |x|. The local time term replaces the ½f''(x)dt correction that would appear for smooth f — since |x|'' = 2δ₀(x) in the distributional sense, the correction is ½ · 2 · "δ₀(W(t))dt" = dL_t^0. Tanaka's formula generalizes to convex functions (the Itô-Tanaka formula) and to semimartingales, making local time a bridge between non-smooth analysis and stochastic calculus.

Reflected Brownian motion has deep applications in **queueing theory** and **mathematical finance**. In heavy-traffic queueing, the workload in a GI/GI/1 queue converges (after diffusion scaling) to RBM with drift — the non-negativity of the queue length forces the reflection, and the local time represents cumulative server idle time. Harrison's program extends this to queueing networks, where multidimensional RBM in the positive orthant models interacting queues with reflection directions determined by the routing structure. In finance, RBM appears in models with regulated prices (currency bands, interest rate floors) and in the study of barriers and knockouts in exotic option pricing, where the boundary behavior of diffusions at barriers determines payoff structures.
