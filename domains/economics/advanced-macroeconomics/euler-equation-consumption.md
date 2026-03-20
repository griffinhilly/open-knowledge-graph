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
stage: advanced
status: draft
---

# Euler Equation and Intertemporal Substitution

## Core Idea
The Euler equation is the first-order condition for optimal consumption over time: the marginal rate of substitution between current and future consumption must equal the intertemporal price (1 plus the real interest rate). This equation shows that consumption growth is determined by the real interest rate and the household's willingness to substitute consumption across time periods. The Euler equation is the backbone of modern macro models, linking macroeconomic outcomes to household preferences and financial conditions.

## Explainer

From your work on household optimization and Lagrange multipliers, you know how to set up a constrained maximization problem and derive first-order conditions. The **Euler equation** is what you get when you apply that machinery to a household choosing how much to consume today versus tomorrow, subject to a budget constraint that allows saving and borrowing at the real interest rate r. The household maximizes lifetime utility — say, u(c₁) + β·u(c₂) for two periods, where β is the discount factor reflecting impatience — subject to the constraint that the present value of consumption equals the present value of income.

Taking the first-order conditions with respect to consumption in each period and combining them yields the Euler equation: u'(c_t) = β·(1+r)·u'(c_{t+1}). In words, the **marginal utility of consuming one more dollar today** must equal the **discounted marginal utility of saving that dollar, earning interest, and consuming it tomorrow**. If the left side were larger — consuming today gives more marginal utility than the best use of the money tomorrow — the household should consume more today and save less. If the right side were larger, the household should save more. At the optimum, the household is indifferent at the margin between consuming now and consuming later, which is exactly what the equation says.

The Euler equation reveals what drives **consumption growth**. With the common CRRA utility function u(c) = c^(1-σ)/(1-σ), the equation simplifies to c_{t+1}/c_t = [β·(1+r)]^(1/σ). This says consumption grows when the real interest rate exceeds the household's rate of time preference (embedded in β), and the **elasticity of intertemporal substitution** (1/σ) controls how responsive consumption growth is to interest rate changes. When σ is small, households willingly shift consumption across time in response to interest rate incentives — they are flexible substituters. When σ is large, households strongly prefer smooth consumption and barely respond to interest rate changes. This single parameter governs how aggressively households tilt their consumption path toward the future when returns to saving are high.

What makes the Euler equation so powerful in macroeconomics is that it holds in every period and under uncertainty (with expectations operators), providing a tight discipline on consumption dynamics without requiring you to solve for the entire consumption path at once. It says nothing directly about the level of consumption — that comes from the budget constraint — but it pins down the rate of change. This is why the Euler equation appears in virtually every modern macro model: the New Keynesian IS curve is a linearized Euler equation, the Ramsey growth model's dynamics are driven by it, and asset pricing models use it to link consumption growth to expected returns. Once you internalize that households optimize at the margin between present and future consumption, the Euler equation becomes the workhorse condition connecting interest rates, patience, risk aversion, and macroeconomic dynamics.
