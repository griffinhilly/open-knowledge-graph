---
id: optimal-stopping
title: Optimal Stopping Theory
domain: mathematics
course: stochastic-processes
prerequisites:
- id: martingales-introduction
  type: hard
- id: brownian-motion
  type: hard
- id: stochastic-differential-equations
  type: soft
tags:
- optimal-stopping
- free-boundary
- american-options
- snell-envelope
stage: expert
status: validated
---

# Optimal Stopping Theory

## Core Idea
Optimal stopping asks: given a stochastic process X(t) and a payoff function g(X(t)), when should you stop to maximize the expected reward? The solution is characterized by the Snell envelope — the smallest supermartingale dominating the payoff process — and the optimal stopping time is the first time the process hits the boundary of the "continuation region." In continuous time, this leads to a free-boundary problem where the stopping boundary itself must be determined as part of the solution.

## Questions

```yaml
- question: "In the discrete-time optimal stopping problem with finite horizon N, the value function V_n(x) = sup_{τ≥n} E[g(X_τ) | X_n = x] satisfies the backward recursion:"
  type: multiple-choice
  options:
    - "V_n(x) = E[g(X_{n+1}) | X_n = x] for all n"
    - "V_n(x) = max{g(x), E[V_{n+1}(X_{n+1}) | X_n = x]} — stop now or continue, whichever is better"
    - "V_n(x) = g(x) + E[V_{n+1}(X_{n+1}) | X_n = x] — accumulate the payoff"
    - "V_n(x) = min{g(x), E[V_{n+1}(X_{n+1}) | X_n = x]} — minimize expected loss"
  answer: 1
  explanation: "At each time n, you face a choice: stop now (receive g(x)) or continue (receive the expected value of optimal future decisions, E[V_{n+1}(X_{n+1})]). You choose whichever is larger. This dynamic programming recursion, working backward from V_N(x) = g(x), defines the value function at every time and state. The optimal stopping region is {x : V_n(x) = g(x)} — the set of states where stopping is immediately optimal. The continuation region is {x : V_n(x) > g(x)} — where waiting has positive value."

- question: "The Snell envelope of a payoff process g(X_n) is the smallest supermartingale that dominates g(X_n) for all n. This concept connects optimal stopping to:"
  type: multiple-choice
  options:
    - "Doob's martingale convergence theorem"
    - "The Doob-Meyer decomposition — the value process decomposes into a martingale minus an increasing process that captures the 'cost of waiting'"
    - "The optional stopping theorem applied in reverse"
    - "The law of large numbers for martingales"
  answer: 1
  explanation: "The Snell envelope V_n is a supermartingale (since V_n ≥ E[V_{n+1} | ℱ_n] and V_n ≥ g(X_n)). The Doob-Meyer decomposition writes V_n = M_n - A_n where M is a martingale and A is a predictable non-decreasing process with A_0 = 0. The increasing process A represents the cumulative 'penalty for not stopping' — it increases precisely at times when continuation is strictly suboptimal but the optimal policy would not yet stop. At the optimal stopping time τ*, V_{τ*} = g(X_{τ*}) and A has not yet increased, so the martingale M captures the full value."

- question: "An American put option on a stock following GBM gives the holder the right to sell at strike K at any time before maturity T. Why can't the American put be priced by the Black-Scholes formula for European options?"
  type: short-answer
  answer: "The European put price assumes exercise only at maturity T. The American put allows early exercise, and this option to stop early has positive value — it is optimal to exercise when the stock falls far enough below K, because the time value of waiting cannot compensate for the immediate payoff K - S. The American put price is the solution to an optimal stopping problem: V(S,t) = sup_τ E_Q[e^{-r(τ-t)}(K-S_τ)⁺ | S_t = S], which leads to a free-boundary problem. The exercise boundary S*(t) — the stock price below which immediate exercise is optimal — must be found as part of the solution. No closed-form formula exists; the price is computed numerically (binomial trees, finite differences, or Monte Carlo with regression)."
  explanation: "The free boundary S*(t) divides the (S,t) plane into a continuation region (hold the option) and a stopping region (exercise). In the continuation region, V satisfies the Black-Scholes PDE; in the stopping region, V = K - S. The boundary S*(t) is determined by smooth-pasting conditions: V and ∂V/∂S are continuous across the boundary. This is fundamentally harder than the European case because the domain of the PDE is itself unknown."

- question: "In the secretary problem (observe candidates sequentially, must hire immediately or lose them), the optimal strategy is to observe the first n/e candidates (approximately 37%) and then hire the next candidate who is better than all previously seen."
  type: true-false
  answer: true
  explanation: "The secretary problem is the most famous discrete optimal stopping problem. With n candidates, the optimal strategy is to reject the first k* ≈ n/e candidates (using them as a 'learning sample'), then accept the first subsequent candidate who is the best so far. This strategy selects the overall best candidate with probability approximately 1/e ≈ 36.8%. The threshold n/e arises from optimizing the trade-off between gathering information (rejecting early candidates) and acting before the best candidate passes. The problem illustrates how optimal stopping often involves a phase transition between exploration and exploitation."
```

## Explainer

**Optimal stopping** is the mathematical theory of deciding when to act. Given a stochastic process X(t) and a payoff g(X(t)) received upon stopping, the problem is to choose the stopping time τ that maximizes E[g(X(τ))]. The classic examples are selling an asset (stop when the price is "high enough"), exercising an option (stop when the intrinsic value justifies giving up future optionality), and the secretary problem (stop when the current candidate is likely the best). The theory draws on martingales, dynamic programming, and free-boundary problems.

In discrete time with finite horizon, the solution is given by **backward induction**. Define V_N(x) = g(x) (at the terminal time, you must stop). For earlier times, V_n(x) = max{g(x), E[V_{n+1}(X_{n+1}) | X_n = x]} — the maximum of stopping now versus the expected value of continuing optimally. The **optimal stopping time** is τ* = min{n : V_n(X_n) = g(X_n)} — the first time the value function equals the immediate payoff, meaning there is nothing to gain from waiting. The value process V_n(X_n) is the **Snell envelope** — the smallest supermartingale that dominates the payoff process g(X_n).

In continuous time, optimal stopping for diffusions leads to **free-boundary problems**. For the process dX = μ dt + σ dW with payoff g(x) and discount rate r, the value function V(x) satisfies the equation LV - rV = 0 in the continuation region C = {x : V(x) > g(x)}, where L is the generator of X, and V(x) = g(x) in the stopping region S = {x : V(x) = g(x)}. The boundary ∂C between the two regions is free — it must be determined as part of the solution. The **smooth-pasting condition** V'(x*) = g'(x*) at the free boundary x* is the additional equation that pins down the boundary location.

The most important financial application is **American option pricing**. An American put on a stock following GBM with strike K has value V(S,t) = sup_τ E_Q[e^{-r(τ-t)}(K-S_τ)⁺]. This is a free-boundary problem: in the continuation region {S > S*(t)}, V satisfies the Black-Scholes PDE; in the stopping region {S ≤ S*(t)}, V = K - S. The exercise boundary S*(t) is a decreasing function of time (as maturity approaches, the threshold for exercising drops because there is less future optionality). Unlike European options, no closed-form formula exists for American options — they are computed by binomial trees, finite difference methods, or least-squares Monte Carlo (the Longstaff-Schwartz algorithm). The optimal stopping framework unifies these computational approaches with a rigorous mathematical foundation.
