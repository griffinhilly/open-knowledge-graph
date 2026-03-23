---
id: continuous-random-variables-basics
title: Continuous Random Variables
domain: mathematics
course: probability-and-statistics
prerequisites:
- id: sample-spaces-and-events
  type: hard
builds-toward:
- probability-density-functions
- expected-value
tags:
- random-variables
- probability
stage: formal-systems
status: validated
---

# Continuous Random Variables

## Core Idea
A continuous random variable takes values in a continuum (like an interval). Since there are uncountably many possible values, probabilities apply to intervals, not individual points. Heights, weights, and times are common continuous random variables.

## Questions

```yaml
- question: "A continuous random variable X has PDF f(x). What is P(X = 1.5)?"
  type: multiple-choice
  options:
    - "f(1.5) — the PDF evaluated at that point gives the probability"
    - "f(1.5) × Δx for some small interval Δx around 1.5"
    - "0 — the probability of any single specific value is exactly zero"
    - "It depends on whether f(1.5) is greater than or less than 1"
  answer: 2
  explanation: "For any continuous random variable, P(X = x) = ∫_x^x f(t) dt = 0 for every specific value x, because an integral over a single point has zero width. The PDF f(x) is a density, not a probability — it can even exceed 1. Probability for a continuous variable is computed by integrating f over an interval, never by evaluating f at a point."

- question: "A probability density function has the value f(x) = 3 at some point x. Is this possible?"
  type: multiple-choice
  options:
    - "Impossible — density values must be at most 1 since probabilities cannot exceed 1"
    - "Possible — f(x) is a density, not a probability; it can exceed 1 as long as its integral over the domain equals 1"
    - "Possible, but only if the variable's domain is wider than the interval [0, 3]"
    - "Impossible — a value of 3 would make P(X = x) = 3, violating probability axioms"
  answer: 1
  explanation: "A PDF value at a point is a rate of probability accumulation (a density), not a probability. f(x) = 3 means probability is densely packed near x. For example, f(x) = 3 on [0, 1/3] and 0 elsewhere integrates to 1 and is a valid PDF. The constraint is that ∫f(x)dx = 1 over the whole domain, not that f(x) ≤ 1 pointwise."

- question: "For a continuous random variable X, P(X < 5) = P(X ≤ 5), because boundary points have probability zero."
  type: true-false
  answer: true
  explanation: "Since P(X = 5) = 0 for any continuous random variable, the events {X < 5} and {X ≤ 5} differ only by this zero-probability point. Adding or removing a single point does not change the integral of the PDF over the region, so the two probabilities are equal. This contrasts with discrete distributions, where boundary points often carry positive probability."

- question: "If the probability density function f(x) is large at a point x, then x is a likely outcome of the random variable X."
  type: true-false
  answer: false
  explanation: "No specific value x is a 'likely outcome' for a continuous random variable — P(X = x) = 0 for every x, regardless of f(x). A large f(x) means probability is concentrated in a small neighborhood of x (i.e., P(X ∈ [x−ε, x+ε]) is large relative to 2ε), but the probability of the exact value is still zero. 'Likely' in the continuous setting means likely to fall in a region near x, never likely to equal x exactly."

- question: "Why is it impossible to assign positive probabilities to individual values of a continuous random variable, and what replaces point probabilities?"
  type: short-answer
  answer: "A continuous random variable takes values in an uncountably infinite set (an interval). If each individual value had a positive probability p > 0, summing over infinitely many values would make the total probability infinite — violating the requirement that total probability equals 1. Mathematically, P(X = x) = ∫_x^x f(t) dt = 0. What replaces point probabilities is integration: P(a ≤ X ≤ b) = ∫_a^b f(x) dx. Probability is assigned to intervals, and the PDF f(x) describes how densely probability is packed per unit length."
  explanation: "This is the fundamental conceptual shift from discrete to continuous probability. In the discrete case, you sum; in the continuous case, you integrate. The PDF plays a role analogous to the probability mass function, but it is a density — its values are not probabilities and can exceed 1."
```

## Explainer

In your study of sample spaces and events, you learned that probability is assigned to subsets of outcomes. For a die roll or a coin flip, the sample space has finitely many points and you can assign a positive probability to each one. A **continuous random variable** introduces an entirely different situation: its values fill an entire interval (or all of ℝ), meaning there are uncountably infinitely many possible outcomes. You cannot assign a positive probability to each individual point — if you tried, the total probability would exceed 1 (and in fact be infinite). Instead, the mathematics forces P(X = x) = 0 for every single value x.

This doesn't mean probability has disappeared — it means probability lives on intervals, not points. Asking "what is the probability that a randomly chosen person is exactly 170.000… cm tall?" is the wrong question; the right question is "what is the probability that their height falls between 169 and 171 cm?" This shift from point probabilities to interval probabilities is the defining feature of continuous random variables. The tool for computing these interval probabilities is the **probability density function (PDF)**, written f(x). The probability that X falls in an interval [a, b] is the integral of f over that interval: P(a ≤ X ≤ b) = ∫_a^b f(x) dx. The density f(x) itself is not a probability — it can exceed 1 — but its integral over any region gives a probability.

To connect this to familiar ground: the cumulative distribution function F(x) = P(X ≤ x) still makes sense for continuous variables, and it's related to the density by differentiation: f(x) = F'(x) wherever the derivative exists. So F is the "running total" of probability from −∞ up to x, and f is the rate at which probability accumulates. For a uniform distribution on [0, 1] — the simplest continuous distribution — f(x) = 1 everywhere on [0, 1] and 0 outside, meaning probability accumulates at a constant rate. P(X ∈ [0.2, 0.5]) = 0.3, exactly the length of the interval.

Continuity also changes how we describe outcomes. Since any individual outcome has probability zero, the events {X < x} and {X ≤ x} have the same probability — the boundary point contributes nothing. This means you can freely use strict or non-strict inequalities without changing probabilities, a simplification that has no counterpart in discrete probability. Understanding this is essential before you work with densities, expected values for continuous variables, and the normal distribution — all of which build on the integral-based framework introduced here.
