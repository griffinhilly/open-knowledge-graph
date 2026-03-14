---
id: random-variables-intro
title: Random Variables and Probability Distributions
domain: mathematics
course: probability-and-statistics
prerequisites:
- id: probability-axioms
  type: hard
- id: function-notation-review
  type: soft
builds-toward:
- expected-value
- binomial-distribution
- poisson-distribution
- continuous-random-variables
tags:
- random-variable
- probability-distribution
- PMF
- discrete
- probability-mass-function
stage: formal-systems
status: validated
---

# Random Variables and Probability Distributions

## Core Idea
A random variable X is a function that assigns a numerical value to each outcome in a sample space, transforming qualitative outcomes into numbers we can analyze mathematically. A discrete random variable takes countably many values, and its probability mass function (PMF) P(X = x) gives the probability at each value, satisfying ΣP(X = x) = 1. Listing all values and their probabilities constitutes a complete probability distribution.

## How It's Best Learned
Start with simple examples: let X = number of heads in 3 coin flips. Build the PMF from scratch by counting outcomes. Then graph the distribution as a probability histogram. Connect back to sample spaces to show how the random variable compresses outcome information.

## Common Misconceptions
- Thinking a random variable is a variable in the algebraic sense — it is actually a function.
- Confusing PMF values (probabilities) with the variable values themselves.
- Not recognizing that probabilities must sum to 1 and each must be between 0 and 1.
