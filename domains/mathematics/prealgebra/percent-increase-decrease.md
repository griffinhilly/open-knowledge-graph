---
id: percent-increase-decrease
title: Percent Increase and Decrease
domain: mathematics
course: prealgebra
prerequisites:
- id: percent-of-a-number
  type: hard
- id: subtracting-integers
  type: soft
builds-toward:
- simple-interest
- exponential-growth-and-decay
tags:
- percent
- change
- increase
- decrease
- applications
stage: abstract-reasoning
status: validated
---
# Percent Increase and Decrease

## Core Idea
Percent increase and decrease measure how much a quantity has changed relative to its original value. The formula is: percent change = (amount of change / original amount) × 100. A $50 item on sale for $35 has decreased by $15, which is a 30% decrease (15/50 × 100). This concept is essential for understanding markups, discounts, inflation, population growth, and financial returns. It also introduces multiplicative thinking about change — a 10% increase followed by a 10% decrease does not return to the original value.

## How It's Best Learned
Start with concrete scenarios: a store marks up wholesale prices, then puts items on sale. Always emphasize that the percent is relative to the original amount (not the new amount). Practice both directions: given original and new values, find the percent change; given an original value and a percent change, find the new value. Introduce the multiplier approach (a 15% increase means multiply by 1.15) for efficiency.

## Common Misconceptions
- Using the new amount as the denominator instead of the original amount when calculating percent change.
- Thinking a 50% increase followed by a 50% decrease returns to the original (it actually gives 75% of the original).
- Confusing the amount of change with the percent of change.

## Questions

```yaml
- question: "A jacket originally costs $80 and is now on sale for $60. What is the percent decrease?"
  type: multiple-choice
  options: ["20%", "25%", "33%", "75%"]
  answer: 1
  explanation: "Percent decrease = (change ÷ original) × 100 = (20 ÷ 80) × 100 = 25%. The change is $20 and the original (denominator) is $80. A common error is dividing by the new price ($60), which gives approximately 33% — but that uses the wrong base."

- question: "A store increases prices by 20%, then offers a 20% discount. The final price equals the original price."
  type: true-false
  answer: false
  explanation: "The 20% discount applies to the already-increased price, not the original. Multiplier: 1.20 × 0.80 = 0.96, so the final price is 96% of the original — a 4% net decrease. Each percent change uses the current amount as its base, which is why successive percent changes are multiplicative, not additive."

- question: "A population grows from 4,000 to 5,200. What is the percent increase? Then, using the multiplier method, find the population after a further 15% increase."
  type: short-answer
  answer: "30% increase (1,200 ÷ 4,000 × 100). After a further 15%: 5,200 × 1.15 = 5,980."
  explanation: "The multiplier method converts percent change to a factor: a 15% increase means multiply by 1.15 rather than computing 15% of 5,200 separately and adding. This is more efficient and generalizes directly to compound growth problems, where you chain multipliers together."
```

## Explainer

You already know how to find a percent of a number — 30% of 200 is 60. Percent increase and decrease build on this by asking: how large is a change *relative to where you started*? That phrase — "relative to where you started" — is the key, because the original amount is always the denominator.

The formula is: percent change = (amount of change ÷ original amount) × 100. If a shirt drops from $40 to $30, the change is $10 and the original is $40, so the percent decrease is 25%. The most common mistake is dividing by the new amount ($30), which gives approximately 33% — a plausible-sounding number that answers the wrong question. Always ask: "what did we start with?" and put that on the bottom.

You can work the formula in either direction. Given original and new values, find the percent change. Or, given an original value and a percent change, find the new value. For efficiency, use the multiplier shortcut: a 25% decrease means multiply by (1 − 0.25) = 0.75, so $40 × 0.75 = $30 directly. A 15% increase means multiply by 1.15. This one-step approach is faster than finding the change and adding, and it extends naturally to problems with multiple changes.

The multiplier approach also reveals a crucial insight: percent changes are *multiplicative*, not additive. A 20% increase followed by a 20% decrease is NOT zero net change — it is 1.20 × 0.80 = 0.96, a 4% net decrease. This is because the second percent applies to a different base than the first. Understanding this is foundational for the exponential growth and decay models you will encounter next, where every change compounds on top of the previous result.
