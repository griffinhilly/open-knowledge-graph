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
status: draft
---

# Continuous Random Variables

## Core Idea
A continuous random variable takes values in a continuum (like an interval). Since there are uncountably many possible values, probabilities apply to intervals, not individual points. Heights, weights, and times are common continuous random variables.

## Explainer

In your study of sample spaces and events, you learned that probability is assigned to subsets of outcomes. For a die roll or a coin flip, the sample space has finitely many points and you can assign a positive probability to each one. A **continuous random variable** introduces an entirely different situation: its values fill an entire interval (or all of ℝ), meaning there are uncountably infinitely many possible outcomes. You cannot assign a positive probability to each individual point — if you tried, the total probability would exceed 1 (and in fact be infinite). Instead, the mathematics forces P(X = x) = 0 for every single value x.

This doesn't mean probability has disappeared — it means probability lives on intervals, not points. Asking "what is the probability that a randomly chosen person is exactly 170.000… cm tall?" is the wrong question; the right question is "what is the probability that their height falls between 169 and 171 cm?" This shift from point probabilities to interval probabilities is the defining feature of continuous random variables. The tool for computing these interval probabilities is the **probability density function (PDF)**, written f(x). The probability that X falls in an interval [a, b] is the integral of f over that interval: P(a ≤ X ≤ b) = ∫_a^b f(x) dx. The density f(x) itself is not a probability — it can exceed 1 — but its integral over any region gives a probability.

To connect this to familiar ground: the cumulative distribution function F(x) = P(X ≤ x) still makes sense for continuous variables, and it's related to the density by differentiation: f(x) = F'(x) wherever the derivative exists. So F is the "running total" of probability from −∞ up to x, and f is the rate at which probability accumulates. For a uniform distribution on [0, 1] — the simplest continuous distribution — f(x) = 1 everywhere on [0, 1] and 0 outside, meaning probability accumulates at a constant rate. P(X ∈ [0.2, 0.5]) = 0.3, exactly the length of the interval.

Continuity also changes how we describe outcomes. Since any individual outcome has probability zero, the events {X < x} and {X ≤ x} have the same probability — the boundary point contributes nothing. This means you can freely use strict or non-strict inequalities without changing probabilities, a simplification that has no counterpart in discrete probability. Understanding this is essential before you work with densities, expected values for continuous variables, and the normal distribution — all of which build on the integral-based framework introduced here.
