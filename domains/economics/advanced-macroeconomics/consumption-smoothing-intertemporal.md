---
id: consumption-smoothing-intertemporal
title: Consumption Smoothing and Permanent Income Hypothesis
domain: economics
course: advanced-macroeconomics
prerequisites:
- id: euler-equation-intertemporal-choice
  type: hard
- id: partial-derivatives
  type: soft
- id: constrained-optimization-lagrange
  type: soft
- id: lagrange-multipliers
  type: soft
tags:
- consumption-smoothing
- permanent-income
- intertemporal-substitution
stage: advanced
status: draft
---

# Consumption Smoothing and Permanent Income Hypothesis

## Core Idea
The permanent income hypothesis asserts that rational agents spread consumption evenly across their lifetime given expected lifetime income. Temporary income shocks have small effects on consumption (high marginal propensity to save), while permanent shocks have large effects. This implies permanent income, not current income, drives consumption.

## Explainer

From the Euler equation you studied previously, you know that an optimizing consumer equates the marginal utility of consuming today with the discounted marginal utility of consuming tomorrow (adjusted for the interest rate). **Consumption smoothing** is the behavioral consequence of this condition: because marginal utility is concave (each additional dollar of consumption is worth less than the last), a consumer who expects to live for many periods is better off spreading resources evenly across time rather than feasting today and starving tomorrow. The Euler equation provides the formal mechanism; consumption smoothing is the intuitive result.

The **permanent income hypothesis** (PIH), developed by Milton Friedman, pushes this logic to its full conclusion. Define **permanent income** as the constant consumption stream that has the same present value as the consumer's actual expected lifetime earnings. A rational, forward-looking consumer sets consumption equal to permanent income in every period. Current income in any single year is irrelevant except insofar as it changes the consumer's estimate of lifetime resources.

Consider a concrete example. Suppose you are a young lawyer earning $80,000 per year who expects to earn $200,000 per year in a decade. The PIH predicts you will borrow against future income now, consuming more than $80,000, because your permanent income — the annuity value of your entire career earnings — is well above your current salary. Conversely, a farmer who receives a one-time bumper crop does not spend the windfall immediately; she recognizes it as a **transitory income shock** and saves most of it, spreading the benefit over many years. The marginal propensity to consume out of transitory income is close to zero, while the marginal propensity to consume out of permanent income is close to one.

This distinction has profound implications for macroeconomic policy. A temporary tax rebate — say, a one-time $1,200 stimulus check — should have a small effect on consumption under the PIH, because rational consumers recognize it as transitory and save most of it. A permanent tax cut, by contrast, raises permanent income and should translate almost fully into higher consumption. Empirically, the truth lies between the textbook PIH and the naive Keynesian model where consumption tracks current income: many households do spend windfalls, likely because of borrowing constraints, uncertainty, or bounded rationality. But the PIH remains the essential benchmark against which all modern consumption theory is measured, and the Euler equation you already know is its mathematical backbone.
