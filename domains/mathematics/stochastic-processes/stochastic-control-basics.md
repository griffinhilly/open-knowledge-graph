---
id: stochastic-control-basics
title: Stochastic Control Basics
domain: mathematics
course: stochastic-processes
prerequisites:
- id: stochastic-differential-equations
  type: hard
- id: itos-formula
  type: hard
- id: optimal-stopping
  type: soft
tags:
- stochastic-control
- hjb-equation
- dynamic-programming
- optimal-control
stage: expert
status: validated
---

# Stochastic Control Basics

## Core Idea
Stochastic control optimizes a controlled diffusion dX = μ(X,u)dt + σ(X,u)dW, where the control u(t) is chosen adaptively to minimize an expected cost J(u) = E[∫₀ᵀ L(X,u)dt + g(X(T))]. The Hamilton-Jacobi-Bellman (HJB) equation ∂V/∂t + min_u{L(x,u) + μ(x,u)∂V/∂x + (1/2)σ²(x,u)∂²V/∂x²} = 0 characterizes the value function V(x,t), and the optimal control u* is the minimizer in the HJB equation. This is the stochastic extension of classical optimal control theory.

## Questions

```yaml
- question: "The HJB equation extends the deterministic Hamilton-Jacobi equation by adding the term (1/2)σ²∂²V/∂x². This second-order term arises from:"
  type: multiple-choice
  options:
    - "The uncertainty in the initial condition"
    - "The Itô correction — applying Itô's formula to V(X(t),t) produces a second-order term from the quadratic variation of X"
    - "Numerical discretization error in the dynamic programming equation"
    - "The convexity of the cost functional J(u)"
  answer: 1
  explanation: "The HJB equation is derived by applying Itô's formula to the value function V(X(t),t) and requiring that the resulting process (after subtracting the running cost) be a supermartingale for all controls and a martingale for the optimal control. The (1/2)σ² ∂²V/∂x² term comes from Itô's formula — specifically from (dX)² = σ²dt. In the deterministic case (σ = 0), this term vanishes and the HJB equation reduces to the Hamilton-Jacobi equation of classical mechanics and optimal control."

- question: "A verification theorem states: if a smooth function V solves the HJB equation with terminal condition V(x,T) = g(x), and the control u*(x,t) = argmin of the HJB minimization is admissible, then V is the value function and u* is optimal. Why is this called 'verification' rather than 'derivation'?"
  type: multiple-choice
  options:
    - "Because the HJB equation may not have a smooth solution, so assuming smoothness is a hypothesis that must be verified"
    - "Because the derivation of HJB involves non-rigorous infinitesimal arguments that need verification"
    - "Both — the HJB equation is derived heuristically, and its solution may not be smooth enough for the argument to work without additional verification"
    - "Because the optimal control might not exist even when V exists"
  answer: 2
  explanation: "The derivation of HJB uses the dynamic programming principle (an infinitesimal Bellman equation), which is heuristic. The verification theorem reverses the logic: start with a candidate V that solves HJB, then prove rigorously (via Itô's formula) that it equals the value function. The catch is that HJB may only have viscosity solutions (not C² smooth), in which case the classical verification theorem doesn't apply and the weaker theory of viscosity solutions is needed. In practice, many important problems have smooth solutions and the verification approach works directly."

- question: "In the Merton portfolio problem, an investor with power utility U(x) = x^γ/γ (γ < 1) chooses what fraction π of wealth to invest in a risky asset. The optimal fraction turns out to be constant: π* = (μ-r)/((1-γ)σ²). Explain why this is remarkable."
  type: short-answer
  answer: "The optimal allocation is constant — it doesn't depend on wealth, time, or the state of the market. Despite the problem being a stochastic control problem with a continuous-time objective and random dynamics, the solution has the same structure as a static mean-variance optimization: invest a fixed fraction proportional to the Sharpe ratio (μ-r)/σ and inversely proportional to risk aversion (1-γ). This myopic property is special to power/log utility and GBM dynamics. With stochastic volatility, mean-reverting returns, or non-CRRA utility, the optimal fraction becomes state-dependent and the problem is genuinely dynamic."
  explanation: "The Merton fraction π* = (μ-r)/((1-γ)σ²) separates into the Sharpe ratio (μ-r)/σ² (how attractive the risky asset is) and 1/(1-γ) (how risk-tolerant the investor is). For γ → 0 (log utility), π* = (μ-r)/σ². The constancy of π* means the value function has a separable form V(w,t) = (w^γ/γ)f(t), which reduces the HJB PDE to an ODE for f(t) — the problem is exactly solvable."
```

## Explainer

**Stochastic control** extends classical optimal control to systems driven by noise. The controlled process dX = μ(X,u)dt + σ(X,u)dW evolves differently depending on the control u(t), which the decision-maker chooses adaptively based on current information. The goal is to choose u to minimize the expected total cost J(u) = E[∫₀ᵀ L(X(t), u(t))dt + g(X(T))], where L is the running cost and g is the terminal cost. The control u can affect the drift (steering), the diffusion (risk management), or both.

The **dynamic programming principle** leads to the **Hamilton-Jacobi-Bellman (HJB) equation**. Define the value function V(x,t) = inf_u E[∫ₜᵀ L + g | X(t) = x] — the optimal cost-to-go from state x at time t. The HJB equation is ∂V/∂t + min_u{L(x,u) + μ(x,u)V_x + (1/2)σ²(x,u)V_{xx}} = 0 with terminal condition V(x,T) = g(x). This PDE encapsulates Bellman's principle of optimality: the optimal policy from (x,t) must be optimal for every sub-problem starting at any future state. The minimizer u*(x,t) = argmin{...} gives the optimal feedback control — a rule specifying the control as a function of the current state and time.

The derivation uses Itô's formula. If V is smooth, apply Itô to V(X(t),t): dV = (V_t + μV_x + (1/2)σ²V_{xx})dt + σV_x dW. For the process V(X(t),t) + ∫₀ᵗ L(X(s),u(s))ds to be a martingale under the optimal control (and a submartingale under any control), the drift must satisfy V_t + L + μV_x + (1/2)σ²V_{xx} ≥ 0 for all u and = 0 for u = u*. Minimizing over u gives the HJB equation. The **verification theorem** makes this rigorous: if a smooth V solves HJB and the resulting u* is admissible, then V is indeed the value function and u* is optimal.

The **Merton problem** (optimal investment and consumption) is the most famous application. An investor with wealth W following dW = (rW + π(μ-r)W - c)dt + πσW dW chooses the risky asset fraction π(t) and consumption rate c(t) to maximize E[∫₀ᵀ U(c)dt]. With power utility U(c) = c^γ/γ and GBM dynamics, the HJB equation admits an explicit solution: the optimal investment fraction π* = (μ-r)/((1-γ)σ²) is constant (the Merton fraction), and consumption is proportional to wealth. This elegant result — a dynamic stochastic problem with a static-looking solution — is special to the CRRA utility/GBM combination. Real-world extensions (stochastic volatility, transaction costs, portfolio constraints) make the HJB equation genuinely nonlinear and require numerical methods.
