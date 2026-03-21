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

## Questions

```yaml
- question: "A fair coin is flipped twice. Define X = number of heads. What is the best description of X?"
  type: multiple-choice
  options:
    - "X is one of the outcomes {HH, HT, TH, TT}"
    - "X is a function that assigns the values 0, 1, or 2 to each outcome in the sample space"
    - "X is a probability; its value is between 0 and 1"
    - "X is the same as the event 'at least one head'"
  answer: 1
  explanation: "A random variable is a function from the sample space to numbers, not an outcome, a probability, or an event. X maps HH → 2, HT → 1, TH → 1, TT → 0. It sits on top of the sample space as a numerical summary. Option A confuses X with an element of the sample space. Option C confuses the random variable with a probability value. Option D confuses a random variable with an event."

- question: "Roll a six-sided die. Define Y = 1 if the roll is even, Y = 0 if the roll is odd. What is P(Y = 1)?"
  type: multiple-choice
  options:
    - "1/6, because one specific outcome causes Y = 1"
    - "1/2, because three outcomes (2, 4, 6) map to Y = 1, each with probability 1/6"
    - "2/6, because Y takes two values"
    - "0, because Y is a derived variable, not a primary outcome"
  answer: 1
  explanation: "P(Y = 1) = P({ω : Y(ω) = 1}) = P({2, 4, 6}) = 3/6 = 1/2. Computing a random variable's probability means summing the probabilities of all outcomes in the sample space that map to that value. The set {2, 4, 6} is an event in the original sample space, so standard probability rules apply directly. This illustrates the layered structure: outcomes in Ω, random variable on top, probabilities computed via the original measure."

- question: "Two different random variables can be defined on the same sample space."
  type: true-false
  answer: true
  explanation: "Multiple random variables can be defined on the same sample space — they are just different functions from Ω to ℝ. Rolling a die: X(ω) = ω (the number showing), Y(ω) = 1 if even else 0, and Z(ω) = (ω − 3.5)² are all valid random variables on the same sample space {1,2,3,4,5,6}. This is a key structural point: the sample space is fixed by the experiment; the random variable is a choice of how to summarize it numerically."

- question: "A discrete random variable must always take integer values."
  type: true-false
  answer: false
  explanation: "A discrete random variable must take values in a *countable* set, but that set need not be integers. For example, a random variable could take values {0, 0.5, 1, 1.5, 2, ...} or any other countably infinite set. What makes it discrete is the presence of gaps between possible values and countability, not whether the values are whole numbers. The integers are the most common case, but not the only one."

- question: "What is the difference between an outcome in the sample space and the value of a random variable, and why does the distinction matter?"
  type: short-answer
  answer: "An outcome is an element of the sample space — the raw result of an experiment (e.g., 'HHT'). A random variable assigns a number to each outcome (e.g., 'number of heads = 2'). The distinction matters because multiple outcomes can map to the same value, so computing P(X = x) requires summing probabilities over all outcomes that map to x."
  explanation: "The distinction is especially important when outcomes are not naturally numerical (e.g., survey responses, card draws, genetic sequences). The random variable converts these qualitative outcomes into numbers that can be analyzed with algebra, calculus, and statistics. Without it, calculating 'expected number of heads' would require working directly with outcome strings. With it, you can apply all the machinery of probability theory to numerical values while tracking probabilities back to the original sample space structure."
```

## Explainer

From your study of sample spaces and events, you know that an experiment produces outcomes, and probabilities are assigned to events (sets of outcomes). A **random variable** takes this framework one step further: it assigns a number to each outcome, converting qualitative descriptions into numerical values that are easier to analyze. More formally, it is a function X: Ω → ℝ where Ω is the sample space. The word "random" does not mean X is arbitrary — it means X inherits its uncertainty from the randomness of the experiment.

Consider rolling a six-sided die. The sample space is Ω = {1, 2, 3, 4, 5, 6}. The natural random variable is X(ω) = ω (the number showing). But you could equally define Y(ω) = 1 if ω is even and Y(ω) = 0 if ω is odd — this is an **indicator random variable** for the event "even roll." Or Z(ω) = (ω − 3.5)² measures squared deviation from the mean. All three are valid random variables on the same sample space. The point is that random variables let you focus on *numerical summaries* of outcomes rather than the raw outcome space.

A random variable is **discrete** when it takes values in a countable set — typically integers or a finite list. This is the case when the sample space is finite or countably infinite, or when you apply a function that collapses a continuous outcome into discrete counts. The number of heads in 10 coin flips, the number of defective items in a batch, the number of emails arriving per hour — all are discrete because they count things. The key distinction from continuous random variables (which you will encounter later) is that discrete random variables have **gaps** between possible values: there is no outcome where X = 2.7 if X is counting successes.

The probability structure of X is captured by its **probability mass function** (pmf), p(x) = P(X = x), which specifies the probability of each possible value. Because X is a function of the outcome ω, computing P(X = x) means summing the probabilities of all outcomes that map to x: P(X = x) = P({ω ∈ Ω : X(ω) = x}). The set {ω : X(ω) = x} is an event — it lives in the original sample space — so all your existing probability rules (addition, complement, etc.) carry over. Random variables do not replace sample spaces; they sit on top of them, providing a more convenient coordinate system for calculations. This layered structure — outcomes underneath, numerical values on top — is the foundation for expected values, variances, and all the distributional properties you will study next.
