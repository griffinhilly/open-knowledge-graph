---
id: random-variables-intro
title: Random Variables
domain: mathematics
course: probability-and-statistics
prerequisites:
- id: probability-axioms
  type: hard
- id: sample-spaces-and-events
  type: soft
builds-toward:
- discrete-random-variables
- continuous-random-variables
- expected-value-and-variance
tags:
- random-variable
- distribution
- function
stage: formal-systems
status: draft
---

# Random Variables

## Core Idea
A random variable is a function that assigns a numerical value to each outcome in a sample space. The distribution of a random variable specifies the probability of each value it can take. Random variables transform abstract sample spaces into numerical quantities that we can analyze mathematically, and their distributions completely characterize their probabilistic behavior.

## Explainer

You already know from sample spaces and events that a probability experiment produces outcomes, and from the probability axioms that events — subsets of those outcomes — get assigned probabilities. A **random variable** is the next layer of abstraction: instead of working directly with events like "heads appeared" or "the die showed an even number," we assign a number to each outcome and then work with those numbers. Technically, a random variable X is a function X: Ω → ℝ, where Ω is the sample space. The word "random" reflects that the input is uncertain; the word "variable" reflects that it takes numerical values.

The simplest example: flip a fair coin. The sample space is Ω = {H, T}. Define X(H) = 1 and X(T) = 0. Now X is a random variable — it maps each outcome to a number. The **distribution** of X tells us P(X = 1) = 1/2 and P(X = 0) = 1/2. Notice that we've translated an abstract event ("heads occurred") into a number ("X = 1"), and the probability axioms you already know apply directly to these numerical events. Any statement about X can be unpacked back into statements about events: {X = 1} is just the event {H} ⊆ Ω.

Why introduce this layer? Because numbers support arithmetic in a way that abstract events don't. Once outcomes become numbers, you can ask questions like "what is the average value of X?" or "how spread out are X's values?" — concepts that have no direct analogue for non-numerical events. The distribution is the complete probabilistic summary: for a discrete random variable, it lists every possible value along with its probability. Two random variables with the same distribution behave identically in every probabilistic sense, even if their underlying sample spaces look completely different.

The distribution satisfies the probability axioms automatically. The probabilities of all possible values of X must sum to 1, because the events {X = x} for distinct values x form a partition of Ω — the outcome must produce *some* value. This connection back to the axioms you know ensures the entire probability theory carries over cleanly. Random variables are the standard language of probability from here forward: discrete and continuous types build on this foundation, and expected value and variance are the two key numerical summaries of any distribution.

