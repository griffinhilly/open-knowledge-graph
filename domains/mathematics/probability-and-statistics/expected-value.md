---
id: expected-value
title: Expected Value
domain: mathematics
course: probability-and-statistics
prerequisites:
- id: random-variables-intro
  type: hard
- id: sigma-notation
  type: hard
builds-toward:
- variance-of-random-variables
- binomial-distribution
- poisson-distribution
- sampling-distributions
tags:
- expected-value
- mean
- expectation
- long-run-average
- weighted-average
stage: formal-systems
status: validated
---

# Expected Value

## Core Idea
The expected value E(X) = Σ x · P(X = x) is the long-run average value of a random variable over many repetitions of the experiment. It is a weighted average of all possible values, where each weight is the corresponding probability. E(X) need not be a value the variable can actually take — for a fair die, E(X) = 3.5. Key properties: E(aX + b) = aE(X) + b, and for independent variables, E(X + Y) = E(X) + E(Y).

## How It's Best Learned
Games of chance (lotteries, casino games) make expected value immediately meaningful. Have students compute expected payoffs to determine whether a game is fair. Then connect to the long-run frequency interpretation with simulations.

## Common Misconceptions
- Thinking the expected value will actually occur on a single trial.
- Forgetting to multiply each outcome by its probability — treating it as a simple average.
- Not recognizing that E(X + Y) = E(X) + E(Y) holds even when X and Y are dependent.

## Questions

```yaml
- question: "A game pays $10 if you roll a 6 on a fair die, and $0 otherwise. What is the expected payout?"
  type: multiple-choice
  options: ["$0", "$1.67", "$5.00", "$10.00"]
  answer: 1
  explanation: "E(X) = 10 × (1/6) + 0 × (5/6) = 10/6 ≈ $1.67. This is the long-run average payout per game — not the $10 you could win or the $0 you usually get. Expected value weights each outcome by its probability."

- question: "If the expected value of a random variable is 3.5, you should expect the outcome 3.5 to occur frequently in repeated trials."
  type: true-false
  answer: false
  explanation: "Expected value is a long-run average, not a prediction for individual trials. For a fair six-sided die, E(X) = 3.5, but 3.5 never actually occurs — it is the average you converge to as you roll many times. This is the most common misconception about expected value."

- question: "Why is expected value described as a 'weighted average' rather than a simple average of possible outcomes?"
  type: short-answer
  answer: "Because each possible outcome is weighted by its probability. Outcomes that are more likely contribute more to the expected value than rare outcomes, even if the rare outcomes have large magnitudes."
  explanation: "A simple average treats all outcomes equally. Expected value uses Σ x · P(X = x), so an outcome worth 100 with probability 0.01 contributes only 1, while an outcome worth 5 with probability 0.5 contributes 2.5. The weighting by probability is what makes expected value meaningful as a predictive quantity."
```

## Explainer

Expected value is the foundational concept linking probability to real-world decision-making. Informally, it answers: if you repeated this random experiment a very large number of times, what would the average outcome be? You compute it by multiplying each possible outcome by its probability and summing those products: E(X) = Σ x · P(X = x). Because you already know sigma notation and random variables, you have exactly the tools needed to read and apply this formula.

The "weighted average" framing is key to building intuition. Suppose a lottery ticket costs $2 and pays $100 with probability 0.01 and $0 otherwise. The simple average of possible payouts is ($100 + $0) / 2 = $50, which wildly overstates the ticket's worth. The expected value is $100 × 0.01 + $0 × 0.99 = $1.00 — below the $2 purchase price, so the game is unfair to the buyer. Expected value is the right tool precisely because it weights outcomes by how often they occur.

A critical subtlety: the expected value does not need to be an achievable outcome. A fair die has E(X) = 3.5, but you will never roll a 3.5. E(X) is not a prediction about any single trial; it describes the long-run behavior across many trials. If you rolled the die 6,000 times, the average of all rolls would be very close to 3.5. This long-run-average interpretation is the correct way to understand expected value.

Two properties are especially useful. First, linearity: E(aX + b) = aE(X) + b. This means if you double all payouts and add a $5 bonus, expected value doubles and gains $5. Second, additivity: E(X + Y) = E(X) + E(Y) for any two random variables, even dependent ones. This is surprisingly powerful — it lets you compute the expected total of complex combinations without worrying about how the individual variables relate to each other.

Expected value is a building block for variance, distributions, and statistical inference. When you encounter the binomial distribution or sampling distributions next, you will see expected value used to describe the center of these distributions. In economics and decision theory, it is the foundation of rational choice under uncertainty.
