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
- id: consumer-duality-and-expenditure-function
  type: hard
builds-toward:
- welfare-analysis-advanced
tags:
- welfare-analysis
- consumer-theory
- policy
stage: expert
status: validated
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

## Questions

```yaml
- question: "A government raises the price of electricity and wants to calculate how much cash to give low-income households to make them exactly as well off as before the price increase. Which welfare measure should it use?"
  type: multiple-choice
  options:
    - "Equivalent variation, because EV measures the income change at original prices that achieves the same utility as the price change"
    - "Consumer surplus change, because it is the simplest measure and is always accurate for policy analysis"
    - "Compensating variation, because CV measures the income change at new prices needed to restore the consumer to original utility"
    - "Equivalent variation, because EV is always larger than CV for a price increase, giving a more generous estimate"
  answer: 2
  explanation: "Compensating variation (CV) is defined precisely as the income adjustment needed after the price change to restore the consumer to their original utility level — evaluated at the new prices. This is exactly what the government wants: how much to pay at the new higher electricity price to make consumers whole. EV asks a different question (what would consumers pay at old prices to prevent the change?) and uses new utility as its reference point — not useful for computing actual compensation after the fact."

- question: "Why do compensating variation and equivalent variation typically give different numerical values for the same price change?"
  type: multiple-choice
  options:
    - "CV and EV use different discount rates to convert future utility into present income equivalents"
    - "CV uses the Hicksian demand curve at the original utility level while EV uses the Hicksian demand curve at the new utility level, and these curves differ whenever there are income effects"
    - "CV measures gains while EV measures losses, so they differ in sign but not in magnitude"
    - "CV is computed at original prices while EV is computed at new prices, so they capture different segments of the Marshallian demand curve"
  answer: 1
  explanation: "Both CV and EV are areas under Hicksian (compensated) demand curves — but different ones. CV uses the Hicksian demand curve holding utility at u₀ (original utility); EV uses the curve holding utility at u₁ (new utility). These two curves are separated by the income effect: when income effects are non-zero (normal or inferior goods), the two Hicksian curves differ, and so do CV and EV. Only when income effects are zero (quasilinear preferences) do the two Hicksian curves coincide and CV = EV = consumer surplus change."

- question: "For a price increase on a normal good, the ordering EV < consumer surplus loss < CV holds."
  type: true-false
  answer: true
  explanation: "This is a standard result in welfare economics. For a normal good facing a price increase, the Hicksian demand curve at the original (higher) utility lies to the right of the Marshallian demand curve, which lies to the right of the Hicksian curve at the new (lower) utility. The area under each curve between old and new prices gives CV > CS change > EV. CV must compensate at the new higher prices (the consumer needs more income to restore lost utility), while EV is evaluated at old prices where the consumer had greater purchasing power."

- question: "CV and EV equal the change in consumer surplus when income effects are large, making most three measures equivalent in practice for most goods."
  type: true-false
  answer: false
  explanation: "This is exactly backward. CV, EV, and consumer surplus converge when income effects are *zero* — specifically, when preferences are quasilinear (utility linear in income). In that case, the Marshallian and both Hicksian demand curves coincide. When income effects are large (goods that constitute a significant share of the consumer's budget), CV, EV, and CS diverge substantially — and it is precisely in those cases that using consumer surplus instead of CV or EV leads to seriously misleading welfare conclusions."

- question: "Explain why CV, EV, and consumer surplus all give the same answer when consumer preferences are quasilinear, but diverge for other preference structures."
  type: short-answer
  answer: "With quasilinear preferences, utility is linear in income (e.g., u = v(x) + m), meaning the marginal utility of income is constant — there is no income effect. The Marshallian demand for the good depends only on price, not income. Both Hicksian demand curves (at u₀ and u₁) coincide with the Marshallian demand curve because holding utility constant is identical to holding income constant when there are no income effects. Since all three curves are identical, the area under any of them between old and new prices is the same, so CV = EV = consumer surplus change."
  explanation: "For goods with income effects, the Marshallian demand curve shifts as income changes, causing it to diverge from the Hicksian curves. CV, computed at original (higher) utility, uses a Hicksian curve further from the origin; EV uses a Hicksian curve closer to the origin. The Marshallian curve lies between them. The divergence grows with the size of the income effect — large for necessities that dominate the budget, negligible for goods with small expenditure shares."
```

## Explainer

From consumer surplus, you know how to measure welfare using the area between the demand curve and the market price. And from the Slutsky equation, you know that a price change has two distinct effects: a substitution effect (the relative price change holding utility constant) and an income effect (the change in purchasing power). The problem with ordinary consumer surplus is that it ignores this decomposition — it uses the **Marshallian demand curve**, which blends both effects together. When income effects are significant, consumer surplus gives an imprecise answer to the question "how much better or worse off is this consumer?" **Compensating variation** and **equivalent variation** solve this by anchoring welfare measurement to a specific utility level.

**Compensating variation (CV)** asks: after a price change has occurred, how much money must we give to (or take from) the consumer to restore them to their **original utility level**? Imagine the price of gasoline doubles. You move to a new, lower indifference curve. CV is the dollar amount that, if handed to you at the new prices, would put you back on your original indifference curve. Formally, CV = e(p₁, u₀) − m, where e is the **expenditure function** (the minimum cost of achieving utility u at prices p), p₁ is the new price vector, u₀ is the original utility, and m is actual income. If the price increase hurts you, CV is positive — it is the compensation you need.

**Equivalent variation (EV)** asks the reverse question: before the price change occurs, how much money would you be willing to give up to **avoid** the change, leaving you at the **new utility level**? EV = m − e(p₀, u₁), where p₀ is the original price and u₁ is the new utility. For a harmful price increase, EV is the amount you would pay at original prices to prevent the increase. EV is anchored to the new utility level and evaluated at old prices, while CV is anchored to the old utility level and evaluated at new prices. The distinction matters because each measure uses a different **Hicksian (compensated) demand curve** — one holding utility at u₀, the other at u₁.

For a normal good facing a price increase, EV < consumer surplus change < CV. The three measures converge when income effects are zero (quasilinear preferences), because the Marshallian and both Hicksian demand curves coincide. In practice, CV is the natural measure for evaluating a policy that *has been implemented* — it tells you the compensation needed to make losers whole. EV is natural for evaluating a *proposed* policy — it tells you the maximum amount people would pay to see it enacted (or to prevent it). This distinction makes CV and EV indispensable tools in cost-benefit analysis, where the choice of welfare measure can change whether a project passes or fails the test of improving social welfare.
