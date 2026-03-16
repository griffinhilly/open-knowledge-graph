---
id: discrete-random-variables-basics
title: Discrete Random Variables
domain: mathematics
course: probability-and-statistics
prerequisites:
- id: sample-spaces-and-events
  type: hard
builds-toward:
- probability-mass-functions
- expected-value
tags:
- random-variables
- probability
stage: formal-systems
status: draft
---

# Discrete Random Variables

## Core Idea
A discrete random variable is a function from sample space to the integers or a countable set. It takes on isolated values (like 0, 1, 2, ...) with defined probabilities. Common examples include the number of successes in trials or counts in categories.

## Explainer

From your study of sample spaces and events, you know that an experiment produces outcomes, and probabilities are assigned to events (sets of outcomes). A **random variable** takes this framework one step further: it assigns a number to each outcome, converting qualitative descriptions into numerical values that are easier to analyze. More formally, it is a function X: Ω → ℝ where Ω is the sample space. The word "random" does not mean X is arbitrary — it means X inherits its uncertainty from the randomness of the experiment.

Consider rolling a six-sided die. The sample space is Ω = {1, 2, 3, 4, 5, 6}. The natural random variable is X(ω) = ω (the number showing). But you could equally define Y(ω) = 1 if ω is even and Y(ω) = 0 if ω is odd — this is an **indicator random variable** for the event "even roll." Or Z(ω) = (ω − 3.5)² measures squared deviation from the mean. All three are valid random variables on the same sample space. The point is that random variables let you focus on *numerical summaries* of outcomes rather than the raw outcome space.

A random variable is **discrete** when it takes values in a countable set — typically integers or a finite list. This is the case when the sample space is finite or countably infinite, or when you apply a function that collapses a continuous outcome into discrete counts. The number of heads in 10 coin flips, the number of defective items in a batch, the number of emails arriving per hour — all are discrete because they count things. The key distinction from continuous random variables (which you will encounter later) is that discrete random variables have **gaps** between possible values: there is no outcome where X = 2.7 if X is counting successes.

The probability structure of X is captured by its **probability mass function** (pmf), p(x) = P(X = x), which specifies the probability of each possible value. Because X is a function of the outcome ω, computing P(X = x) means summing the probabilities of all outcomes that map to x: P(X = x) = P({ω ∈ Ω : X(ω) = x}). The set {ω : X(ω) = x} is an event — it lives in the original sample space — so all your existing probability rules (addition, complement, etc.) carry over. Random variables do not replace sample spaces; they sit on top of them, providing a more convenient coordinate system for calculations. This layered structure — outcomes underneath, numerical values on top — is the foundation for expected values, variances, and all the distributional properties you will study next.
