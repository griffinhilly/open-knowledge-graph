---
id: conditional-distributions-theory
title: Conditional Distributions of Random Variables
domain: mathematics
course: probability-and-statistics
prerequisites:
- id: joint-marginal-distributions
  type: hard
builds-toward:
- conditional-expectation
tags:
- conditional-distribution
stage: formal-systems
status: draft
---

# Conditional Distributions of Random Variables

## Core Idea
Conditional distribution of Y given X=x: p_{Y|X}(y|x)=p(x,y)/p_X(x) (discrete) or f_{Y|X}(y|x)=f(x,y)/f_X(x) (continuous). Shows how Y's distribution changes given information about X. When independent, conditional equals marginal.

## Questions

```yaml
- question: "The joint PDF of (X, Y) is f(x, y) = 2 for 0 < x < y < 1. A student wants the conditional distribution of Y given X = 0.3. Which approach is correct?"
  type: multiple-choice
  options:
    - "Use f(0.3, y) directly as the conditional PDF for all valid y"
    - "Compute f_{Y|X}(y | 0.3) = f(0.3, y) / f_X(0.3), normalizing the slice at X = 0.3 to integrate to 1"
    - "Restrict the marginal f_Y(y) to values near y = 0.3"
    - "The conditional distribution equals the joint because a conditional is just a restriction"
  answer: 1
  explanation: "The conditional PDF is f_{Y|X}(y|x) = f(x,y) / f_X(x). You take the joint density evaluated at the fixed x-value (the 'slice'), then divide by the marginal f_X(x) to normalize it into a proper distribution that integrates to 1 over y. Using f(0.3, y) unnormalized (option A) gives a function that does not integrate to 1 — it is proportional to the conditional but not a valid PDF. The marginal f_Y(y) (option C) ignores the conditioning information entirely."

- question: "X and Y are independent random variables. Which of the following is always true about their conditional distribution?"
  type: multiple-choice
  options:
    - "The conditional distribution f_{Y|X}(y|x) equals the joint distribution f(x,y)"
    - "The conditional distribution f_{Y|X}(y|x) equals the marginal f_Y(y) for every x"
    - "The conditional distribution f_{Y|X}(y|x) equals the marginal f_X(x)"
    - "Conditioning on X = x always reduces the variance of Y"
  answer: 1
  explanation: "Independence means knowing X provides zero information about Y. Formally, the joint factors as f(x,y) = f_X(x)·f_Y(y), so f_{Y|X}(y|x) = f(x,y)/f_X(x) = f_Y(y). The conditional equals the marginal — conditioning changed nothing. This is the cleanest characterization of independence in terms of conditional distributions: two variables are independent if and only if every conditional distribution equals the corresponding marginal."

- question: "The conditional PDF f_{Y|X}(y|x) must integrate to 1 over all y for each fixed value of x."
  type: true-false
  answer: true
  explanation: "A conditional distribution is a proper probability distribution in its own right — it describes the behavior of Y in the restricted world where X = x is certain. Like any PDF, it must integrate to 1. The division by f_X(x) in the formula f(x,y)/f_X(x) is exactly what ensures this normalization: it converts the unnormalized joint 'slice' at x into a valid distribution. Without this normalization, you have a function proportional to the conditional but not a probability distribution."

- question: "The conditional distribution of Y given X = x is simply the joint distribution restricted to the region where X is near x, with no need for renormalization."
  type: true-false
  answer: false
  explanation: "Restriction alone does not produce a probability distribution. The 'slice' f(x,y) for fixed x does not integrate to 1 over y — its total mass depends on how probable that x-value is (captured by f_X(x)). Dividing by f_X(x) renormalizes the slice into a proper distribution that accounts for the fact that we are now working in the conditional world where X = x is certain. Skipping normalization gives a function with the right shape but the wrong total mass."

- question: "Explain geometrically what the formula f_{Y|X}(y|x) = f(x,y) / f_X(x) is doing."
  type: short-answer
  answer: "The joint density f(x,y) defines a surface over the (x,y) plane. Fixing X = x means taking a vertical slice through this surface — you get a one-dimensional curve over y showing how the joint density behaves at that x. This curve is proportional to the conditional distribution of Y given X = x, but it doesn't integrate to 1 because the joint density is spread across all x values. Dividing by f_X(x) — the total 'mass' of that slice — rescales it into a proper PDF."
  explanation: "Geometrically, you are zooming into the cross-section of the joint density at x and renormalizing so that this cross-section represents a complete probability story for Y in the restricted world where X = x is given. The marginal f_X(x) is the height of the joint surface when integrated over y — it tells you 'how much' of the joint density lives at this x-value. Dividing by it removes that overall scale factor, leaving only the shape of Y's distribution given X = x."
```

## Explainer

Your prerequisite — **joint and marginal distributions** — gives you two things: the joint distribution p(x, y) or f(x, y) that describes X and Y together, and the marginal p_X(x) or f_X(x) that describes X alone after "integrating out" Y. A **conditional distribution** answers a natural next question: once you learn that X = x, how does the distribution of Y change? You have new information — how do you update your picture of Y?

The formula is a direct extension of conditional probability from events to distributions. In the discrete case, the **conditional PMF** is p_{Y|X}(y|x) = p(x, y) / p_X(x). This is exactly Bayes' rule applied to events: P(Y=y | X=x) = P(X=x, Y=y) / P(X=x). In the continuous case, the **conditional PDF** is f_{Y|X}(y|x) = f(x, y) / f_X(x). The operation has a clean geometric meaning: you take a "slice" of the joint distribution at the fixed value X = x (looking at all possible y-values with that x), then normalize it to integrate to 1. The result is a proper probability distribution over Y.

A concrete example makes this vivid. Suppose X is a person's height and Y is their weight, with some joint distribution f(x, y). The marginal f_Y(y) is the weight distribution of the entire population. But if someone tells you the person is 6 feet tall, the conditional distribution f_{Y|X}(y | x = 6) is the weight distribution restricted to 6-foot-tall people — a different, narrower distribution with a higher mean. You are not just restricting Ω to people who are 6 feet; you are looking at the cross-section of the joint density at x = 6 and renormalizing it.

The connection to **independence** is the cleanest possible: X and Y are independent if and only if f_{Y|X}(y|x) = f_Y(y) for all x. Knowing X gives zero information about Y — the conditional equals the marginal. This is equivalent to the joint factoring as a product: f(x, y) = f_X(x) · f_Y(y), and dividing by f_X(x) recovers f_Y(y). Conditional distributions are the foundational object for conditional expectation, Bayesian inference, and regression — in every case, the central question is: how does the distribution of one quantity shift when you condition on the value of another?
