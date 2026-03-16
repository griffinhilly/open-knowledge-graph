---
id: compensating-and-equivalent-variation
title: 'Compensating and Equivalent Variation: Welfare Measurement'
domain: economics
course: advanced-microeconomics
prerequisites:
- id: consumer-surplus-microeconomics
  type: hard
- id: slutsky-equation
  type: hard
- id: indifference-curves
  type: soft
builds-toward:
- welfare-analysis-advanced
tags:
- welfare-analysis
- consumer-theory
- policy
stage: advanced
status: draft
---

# Compensating and Equivalent Variation: Welfare Measurement

## Core Idea
Compensating Variation (CV) measures the income change needed after a price change to restore original utility, while Equivalent Variation (EV) measures the income change before a price change to make the consumer indifferent to the actual change. Both are theoretically superior to consumer surplus because they account for income effects and are calculated using expenditure functions: CV = e(p₁, u₀) - m and EV = m - e(p₀, u₁).

## How It's Best Learned
Draw budget lines and indifference curves before/after a price change. Identify the original bundle, new bundle, and hypothetical bundles where CV and EV apply. Calculate using expenditure functions for standard preferences like Cobb-Douglas.

## Common Misconceptions
- CV and EV are not consumer surplus; they account for income effects that consumer surplus ignores.
- Choose CV for evaluating actual policy changes; use EV for hypothetical changes.
- CV and EV diverge more when income effects are larger.

## Explainer

From consumer surplus, you know how to measure welfare using the area between the demand curve and the market price. And from the Slutsky equation, you know that a price change has two distinct effects: a substitution effect (the relative price change holding utility constant) and an income effect (the change in purchasing power). The problem with ordinary consumer surplus is that it ignores this decomposition — it uses the **Marshallian demand curve**, which blends both effects together. When income effects are significant, consumer surplus gives an imprecise answer to the question "how much better or worse off is this consumer?" **Compensating variation** and **equivalent variation** solve this by anchoring welfare measurement to a specific utility level.

**Compensating variation (CV)** asks: after a price change has occurred, how much money must we give to (or take from) the consumer to restore them to their **original utility level**? Imagine the price of gasoline doubles. You move to a new, lower indifference curve. CV is the dollar amount that, if handed to you at the new prices, would put you back on your original indifference curve. Formally, CV = e(p₁, u₀) − m, where e is the **expenditure function** (the minimum cost of achieving utility u at prices p), p₁ is the new price vector, u₀ is the original utility, and m is actual income. If the price increase hurts you, CV is positive — it is the compensation you need.

**Equivalent variation (EV)** asks the reverse question: before the price change occurs, how much money would you be willing to give up to **avoid** the change, leaving you at the **new utility level**? EV = m − e(p₀, u₁), where p₀ is the original price and u₁ is the new utility. For a harmful price increase, EV is the amount you would pay at original prices to prevent the increase. EV is anchored to the new utility level and evaluated at old prices, while CV is anchored to the old utility level and evaluated at new prices. The distinction matters because each measure uses a different **Hicksian (compensated) demand curve** — one holding utility at u₀, the other at u₁.

For a normal good facing a price increase, EV < consumer surplus change < CV. The three measures converge when income effects are zero (quasilinear preferences), because the Marshallian and both Hicksian demand curves coincide. In practice, CV is the natural measure for evaluating a policy that *has been implemented* — it tells you the compensation needed to make losers whole. EV is natural for evaluating a *proposed* policy — it tells you the maximum amount people would pay to see it enacted (or to prevent it). This distinction makes CV and EV indispensable tools in cost-benefit analysis, where the choice of welfare measure can change whether a project passes or fails the test of improving social welfare.
