---
id: household-optimization-consumption-savings
title: Household Optimization and Consumption-Savings Decisions
domain: economics
course: advanced-macroeconomics
prerequisites:
- id: dynamic-optimization-macroeconomics
  type: hard
- id: consumer-theory-utility
  type: hard
- id: lagrange-multipliers
  type: soft
- id: constrained-optimization-lagrange
  type: soft
builds-toward:
- euler-equation-consumption
- lifecycle-hypothesis-consumption
tags:
- consumption
- savings
- optimization
stage: advanced
status: draft
---

# Household Optimization and Consumption-Savings Decisions

## Core Idea
Households make consumption and savings decisions over their lifetime by maximizing the present value of utility from consumption. The budget constraint links current and future consumption through interest rates and income flows. Preferences (particularly the elasticity of intertemporal substitution) determine how much households reduce consumption today to increase it in the future when interest rates rise, shaping macroeconomic responses to policy.

## Explainer

From consumer theory, you know that households maximize utility subject to constraints. From dynamic optimization, you know how to extend this reasoning across time using discounted sums and Lagrangian methods. Household optimization over consumption and savings fuses these tools: instead of choosing between two goods at a single point in time, the household chooses between **consuming today versus consuming tomorrow**, treating present and future consumption as two "goods" linked by the interest rate.

The simplest version is a two-period model. A household earns income y₁ today and y₂ tomorrow, and can borrow or save at interest rate r. The **intertemporal budget constraint** says that the present value of lifetime consumption cannot exceed the present value of lifetime income: c₁ + c₂/(1+r) ≤ y₁ + y₂/(1+r). This looks exactly like a standard budget constraint from consumer theory, except the "prices" of present and future consumption are 1 and 1/(1+r) respectively. The household maximizes U(c₁) + βU(c₂) subject to this constraint, where β is the **discount factor** reflecting impatience — how much less the household values future utility compared to present utility.

Applying your Lagrangian technique yields the **consumption Euler equation**: U'(c₁) = β(1+r)U'(c₂). This elegant condition says the household adjusts consumption until the marginal utility sacrificed today exactly equals the discounted marginal utility gained tomorrow, scaled by the gross return on savings. If the interest rate rises, the right side increases, meaning the household needs higher marginal utility today (lower consumption today) and lower marginal utility tomorrow (higher consumption tomorrow) to restore equality. The household saves more. But how much more depends on the **elasticity of intertemporal substitution** (EIS) — a preference parameter measuring the household's willingness to shift consumption across time in response to interest rate changes. High EIS means consumption is very responsive to interest rates; low EIS means the household stubbornly smooths consumption regardless.

The macroeconomic implications are profound. In aggregate, household consumption-savings decisions determine the economy's saving rate, capital accumulation, and interest rate. When a central bank raises interest rates, the consumption Euler equation is the channel through which this policy bites: higher rates increase the return to saving, inducing households to postpone consumption (the **substitution effect**), though they also make savers wealthier (the **income effect** that works in the opposite direction). The relative strength of these effects — governed by the EIS and the distribution of wealth — determines whether monetary policy is powerful or weak. This is why the household optimization problem is not merely a microeconomic exercise but the microfoundation on which all modern macroeconomic models are built.
