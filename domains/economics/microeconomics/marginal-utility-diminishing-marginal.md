---
id: marginal-utility-diminishing-marginal
title: Marginal Utility and the Law of Diminishing Marginal Utility
domain: economics
course: microeconomics
prerequisites:
- id: demand-curve-individual-consumer
  type: hard
builds-toward:
- consumer-optimum
- indifference-curves
tags:
- utility
- marginal-analysis
- consumer-choice
stage: formal-systems
status: draft
---

# Marginal Utility and the Law of Diminishing Marginal Utility

## Core Idea
Marginal utility is the additional satisfaction gained from consuming one more unit of a good. The law of diminishing marginal utility states that as consumption of a good increases, the marginal utility declines: the 10th slice of pizza gives less satisfaction than the first. This drives downward-sloping demand curves and explains why consumers diversify consumption.

## How It's Best Learned
Rate satisfaction for successive units of a good. Plot it. Observe that the curve is downward-sloping. This explains why you're willing to pay more for the first unit than the fifth.

## Common Misconceptions
- Total utility decreases (it usually increases, but at a decreasing rate; marginal utility is what declines).
- MU being positive means satisfaction is unbounded (MU eventually can go negative when too much causes dissatisfaction).

## Questions

```yaml
- question: "A consumer eats slices of pizza and reports: slice 1 gives 10 utils of satisfaction, slice 2 gives 7 utils, slice 3 gives 4 utils. What is the consumer's total utility after eating all 3 slices?"
  type: multiple-choice
  options:
    - "4 utils — the marginal utility of the last (third) slice"
    - "10 utils — the highest satisfaction reported"
    - "21 utils — the sum of all marginal utilities (10 + 7 + 4)"
    - "7 utils — the average marginal utility across slices"
  answer: 2
  explanation: "Total utility is the cumulative satisfaction from all units consumed — you add up every marginal utility received: 10 + 7 + 4 = 21 utils. The fact that marginal utility is falling does not mean total utility is falling — it means total utility is rising more and more slowly. As long as each slice adds some positive satisfaction (MU > 0), total utility keeps increasing. Confusing marginal utility (the addition from one more unit) with total utility (the cumulative amount) is the central misconception in this topic."

- question: "A student claims: 'After drinking 4 cups of coffee, my total satisfaction from coffee is decreasing because of diminishing marginal utility.' Based on the law of diminishing marginal utility, what is the correct assessment?"
  type: multiple-choice
  options:
    - "The student is correct — total utility always decreases as consumption rises above some point"
    - "The student is confusing the law — total utility decreases only if the marginal utility of the 4th cup is negative (it actually reduces overall satisfaction)"
    - "The law predicts total utility decreases after any 4 units consumed"
    - "Diminishing marginal utility only applies to food and drink, not beverages"
  answer: 1
  explanation: "Diminishing marginal utility means each additional cup adds less satisfaction than the one before — but as long as MU > 0, each cup still adds something positive, so total utility is still rising. Total utility only starts to fall when MU turns negative — when a unit of consumption actually causes net harm (anxiety from too much coffee, nausea from too much food). The student is misapplying the law by equating 'diminishing additions' with 'decreasing total.'"

- question: "The law of diminishing marginal utility states that the more you consume of a good, the less total satisfaction you have from consuming it."
  type: true-false
  answer: false
  explanation: "The law applies to MARGINAL utility — the additional satisfaction from each successive unit — not to total utility. Total utility continues to rise as long as marginal utility is positive (i.e., each additional unit still adds some satisfaction). Total utility only falls when marginal utility becomes negative. Confusing the two is the most common error when learning this concept."

- question: "The downward slope of an individual demand curve is a direct consequence of diminishing marginal utility: as a consumer acquires more units, their willingness to pay for each additional unit falls."
  type: true-false
  answer: true
  explanation: "This is the key link between utility theory and the demand curve you already know. A rational consumer will pay for a unit only up to the satisfaction that unit provides. Since each successive unit yields less marginal utility, the consumer's marginal willingness to pay declines with each unit. The demand curve is essentially marginal utility expressed in dollar terms — the two concepts are the same insight at different levels of abstraction."

- question: "Explain the difference between total utility and marginal utility. Why does total utility continue to rise even as marginal utility diminishes?"
  type: short-answer
  answer: "Total utility is the cumulative satisfaction from all units consumed. Marginal utility is the additional satisfaction from consuming one more unit. As long as each new unit adds any positive amount (MU > 0), total utility keeps increasing — just more slowly. Total utility only falls when MU becomes negative. Diminishing MU means the additions are getting smaller, not that the total is shrinking."
  explanation: "An analogy: imagine filling a bucket with water. Each cup you add increases the water level (total utility rises), but each successive cup might fill the bucket a bit less efficiently (marginal utility diminishes). The bucket keeps filling as long as you keep adding water with positive effect. Only if the water somehow evaporated faster than you added it (negative MU) would the level drop. The total is the accumulation of all the marginals."
```

## Explainer

Your prerequisite — the individual demand curve — shows that consumers are willing to pay less for additional units of a good as they consume more. But why? The answer lies in **utility**: the satisfaction a consumer derives from consumption. **Marginal utility** is the additional satisfaction from consuming one more unit. It answers a simple question: how much better off is this person from getting one more slice of pizza? The first slice when you're hungry delivers enormous satisfaction. The fifth slice when you're already full delivers far less. This is the core intuition behind the entire concept.

The **law of diminishing marginal utility** formalizes this intuition: as consumption of a good increases, holding everything else constant, each successive unit adds less satisfaction than the one before. **Total utility** — the cumulative satisfaction from all units consumed — keeps rising as long as marginal utility is positive. You're still getting *some* satisfaction from that fifth slice, so total utility is still going up. But it's rising more and more slowly. Marginal utility is the slope of the total utility curve; the law says that slope is decreasing. Eventually, if you consumed enough, marginal utility could even turn negative — the fourth cup of coffee in an afternoon might cause anxiety rather than alertness, actually reducing your total satisfaction.

Diminishing marginal utility directly generates the downward-sloping demand curve you already know. A rational consumer is willing to pay for a unit only up to the value of the satisfaction that unit provides. Since each successive unit delivers less marginal utility, the consumer's **marginal willingness to pay** — their maximum acceptable price — falls with each additional unit. The demand curve is simply marginal utility expressed in dollar terms. At low quantities, willingness to pay is high; at high quantities, it is low. This is not a coincidence but a direct consequence of diminishing marginal utility.

Diminishing marginal utility also explains why consumers diversify. If you're allocating spending across multiple goods, concentrating everything on one good drives its marginal utility very low while leaving the marginal utility of other goods very high — you're leaving satisfaction on the table. The consumer optimum you'll study next formalizes this insight as an equalization condition: rational consumers spread spending until the last dollar spent on every good delivers the same marginal utility. Any imbalance — one good delivering more satisfaction per dollar than another — is a signal to reallocate spending, and consumers keep doing so until the margins are equalized.
