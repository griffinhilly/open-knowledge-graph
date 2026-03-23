---
id: euler-equation-consumption
title: Euler Equation and Intertemporal Substitution
domain: economics
course: advanced-macroeconomics
prerequisites:
- id: household-optimization-consumption-savings
  type: hard
- id: partial-derivatives
  type: soft
- id: chain-rule
  type: soft
- id: lagrange-multipliers
  type: hard
- id: optimization-multivariable-basics
  type: hard
builds-toward:
- new-keynesian-framework
tags:
- euler-equation
- consumption
- substitution
stage: expert
status: validated
---

# Euler Equation and Intertemporal Substitution

## Core Idea
The Euler equation is the first-order condition for optimal consumption over time: the marginal rate of substitution between current and future consumption must equal the intertemporal price (1 plus the real interest rate). This equation shows that consumption growth is determined by the real interest rate and the household's willingness to substitute consumption across time periods. The Euler equation is the backbone of modern macro models, linking macroeconomic outcomes to household preferences and financial conditions.

## Questions

```yaml
- question: "According to the Euler equation with CRRA utility, the real interest rate rises unexpectedly. What does the Euler equation directly predict?"
  type: multiple-choice
  options:
    - "Current consumption falls immediately, because the higher interest rate reduces the present value of future income"
    - "Consumption growth increases — future consumption rises relative to current consumption — but the Euler equation alone does not determine whether current consumption rises or falls"
    - "Both current and future consumption rise proportionally, because households are wealthier when returns to saving are higher"
    - "Consumption is unchanged, because rational households smooth consumption across all interest rate fluctuations"
  answer: 1
  explanation: "The Euler equation c_{t+1}/c_t = [β(1+r)]^(1/σ) governs consumption *growth*, not the consumption *level*. When r rises, the right-hand side increases, meaning households optimally tilt their consumption path toward the future: consumption growth accelerates. Whether current consumption c_t rises or falls depends on the full budget constraint (income, wealth, borrowing limits) — the Euler equation alone is silent on the level. This is the most common source of confusion: students conflate the Euler equation's prediction about the growth rate with a claim about current consumption."

- question: "What does the elasticity of intertemporal substitution (EIS = 1/σ in CRRA utility) measure in the context of the Euler equation?"
  type: multiple-choice
  options:
    - "How much a household's lifetime income changes when the interest rate changes by 1 percentage point"
    - "How responsive the growth rate of consumption is to changes in the real interest rate — households with high EIS strongly tilt consumption toward periods with higher returns"
    - "The fraction of income saved at any given interest rate, holding wealth constant"
    - "The degree of risk aversion, which determines how much consumption volatility the household will tolerate"
  answer: 1
  explanation: "The EIS (= 1/σ) is the elasticity of consumption growth with respect to the gross real interest rate. When EIS is high (σ small), a modest rise in r produces a large tilt toward future consumption — these households are flexible substituters willing to defer gratification for higher returns. When EIS is low (σ large), households have a strong preference for smooth consumption and barely change their consumption growth in response to interest rate variation. Note: σ also governs risk aversion in CRRA utility, but these two interpretations are conceptually distinct — EIS governs deterministic intertemporal substitution, while risk aversion governs responses to uncertainty about consumption levels."

- question: "The Euler equation determines the optimal *level* of consumption in each period, given the household's budget constraint and preferences."
  type: true-false
  answer: false
  explanation: "The Euler equation is a first-order condition that pins down the *ratio* of consumption across periods — the rate of growth — not the absolute level. The equation u'(c_t) = β(1+r)u'(c_{t+1}) says the marginal utility of consuming a dollar today must equal the discounted marginal utility of saving and consuming that dollar tomorrow. It is the intertemporal optimality condition. The absolute level of consumption in any period is determined by combining the Euler equation with the household's lifetime budget constraint (which pins down total spending given total resources). The Euler equation provides one equation in two unknowns (c_t and c_{t+1}); the budget constraint provides the second."

- question: "The Euler equation holds under uncertainty, where the relevant condition becomes: the marginal utility of consuming today equals the discounted expected marginal utility of consuming tomorrow."
  type: true-false
  answer: true
  explanation: "The stochastic Euler equation is: u'(c_t) = β(1+r) E_t[u'(c_{t+1})], where E_t is the expectation conditional on information available at time t. This extends naturally from the deterministic case: the household equates the certain marginal utility of consuming today with the *expected* discounted marginal utility of saving and consuming tomorrow (uncertain because future income, prices, or interest rates may vary). This stochastic version is the workhorse of modern macroeconomics and asset pricing, where it can be combined with asset return data to test whether household consumption behavior is consistent with rational optimization."

- question: "Explain the role of the elasticity of intertemporal substitution (1/σ) in the Euler equation, and contrast the consumption behavior of a household with σ = 0.1 versus one with σ = 10 when the real interest rate rises."
  type: short-answer
  answer: "The EIS (1/σ) measures how much the growth rate of consumption responds to a change in the real interest rate. In the CRRA Euler equation, c_{t+1}/c_t = [β(1+r)]^(1/σ). A household with σ = 0.1 (EIS = 10) responds very strongly: a modest increase in r dramatically increases the consumption growth rate, meaning the household sharply tilts consumption toward the future to take advantage of higher returns. A household with σ = 10 (EIS = 0.1) barely changes its consumption growth rate in response to the same interest rate increase — it has a strong preference for smooth consumption across time. The first household acts like a flexible financial optimizer; the second behaves closer to a rule-of-thumb consumer with near-rigid consumption smoothing."
  explanation: "This parameter has enormous macroeconomic implications. If σ is small (high EIS), monetary policy — which works partly through the real interest rate — powerfully affects consumption timing. If σ is large (low EIS), the intertemporal substitution channel of monetary policy is weak. Empirical estimates of σ are debated, but most macroeconomic models assume σ around 1–2 (EIS of 0.5–1), implying moderate responsiveness of consumption growth to interest rates."
```

## Explainer

From your work on household optimization and Lagrange multipliers, you know how to set up a constrained maximization problem and derive first-order conditions. The **Euler equation** is what you get when you apply that machinery to a household choosing how much to consume today versus tomorrow, subject to a budget constraint that allows saving and borrowing at the real interest rate r. The household maximizes lifetime utility — say, u(c₁) + β·u(c₂) for two periods, where β is the discount factor reflecting impatience — subject to the constraint that the present value of consumption equals the present value of income.

Taking the first-order conditions with respect to consumption in each period and combining them yields the Euler equation: u'(c_t) = β·(1+r)·u'(c_{t+1}). In words, the **marginal utility of consuming one more dollar today** must equal the **discounted marginal utility of saving that dollar, earning interest, and consuming it tomorrow**. If the left side were larger — consuming today gives more marginal utility than the best use of the money tomorrow — the household should consume more today and save less. If the right side were larger, the household should save more. At the optimum, the household is indifferent at the margin between consuming now and consuming later, which is exactly what the equation says.

The Euler equation reveals what drives **consumption growth**. With the common CRRA utility function u(c) = c^(1-σ)/(1-σ), the equation simplifies to c_{t+1}/c_t = [β·(1+r)]^(1/σ). This says consumption grows when the real interest rate exceeds the household's rate of time preference (embedded in β), and the **elasticity of intertemporal substitution** (1/σ) controls how responsive consumption growth is to interest rate changes. When σ is small, households willingly shift consumption across time in response to interest rate incentives — they are flexible substituters. When σ is large, households strongly prefer smooth consumption and barely respond to interest rate changes. This single parameter governs how aggressively households tilt their consumption path toward the future when returns to saving are high.

What makes the Euler equation so powerful in macroeconomics is that it holds in every period and under uncertainty (with expectations operators), providing a tight discipline on consumption dynamics without requiring you to solve for the entire consumption path at once. It says nothing directly about the level of consumption — that comes from the budget constraint — but it pins down the rate of change. This is why the Euler equation appears in virtually every modern macro model: the New Keynesian IS curve is a linearized Euler equation, the Ramsey growth model's dynamics are driven by it, and asset pricing models use it to link consumption growth to expected returns. Once you internalize that households optimize at the margin between present and future consumption, the Euler equation becomes the workhorse condition connecting interest rates, patience, risk aversion, and macroeconomic dynamics.
