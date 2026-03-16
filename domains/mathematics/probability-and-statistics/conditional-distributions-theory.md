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

## Explainer

Your prerequisite — **joint and marginal distributions** — gives you two things: the joint distribution p(x, y) or f(x, y) that describes X and Y together, and the marginal p_X(x) or f_X(x) that describes X alone after "integrating out" Y. A **conditional distribution** answers a natural next question: once you learn that X = x, how does the distribution of Y change? You have new information — how do you update your picture of Y?

The formula is a direct extension of conditional probability from events to distributions. In the discrete case, the **conditional PMF** is p_{Y|X}(y|x) = p(x, y) / p_X(x). This is exactly Bayes' rule applied to events: P(Y=y | X=x) = P(X=x, Y=y) / P(X=x). In the continuous case, the **conditional PDF** is f_{Y|X}(y|x) = f(x, y) / f_X(x). The operation has a clean geometric meaning: you take a "slice" of the joint distribution at the fixed value X = x (looking at all possible y-values with that x), then normalize it to integrate to 1. The result is a proper probability distribution over Y.

A concrete example makes this vivid. Suppose X is a person's height and Y is their weight, with some joint distribution f(x, y). The marginal f_Y(y) is the weight distribution of the entire population. But if someone tells you the person is 6 feet tall, the conditional distribution f_{Y|X}(y | x = 6) is the weight distribution restricted to 6-foot-tall people — a different, narrower distribution with a higher mean. You are not just restricting Ω to people who are 6 feet; you are looking at the cross-section of the joint density at x = 6 and renormalizing it.

The connection to **independence** is the cleanest possible: X and Y are independent if and only if f_{Y|X}(y|x) = f_Y(y) for all x. Knowing X gives zero information about Y — the conditional equals the marginal. This is equivalent to the joint factoring as a product: f(x, y) = f_X(x) · f_Y(y), and dividing by f_X(x) recovers f_Y(y). Conditional distributions are the foundational object for conditional expectation, Bayesian inference, and regression — in every case, the central question is: how does the distribution of one quantity shift when you condition on the value of another?
