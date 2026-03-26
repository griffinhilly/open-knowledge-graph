---
id: conditional-distributions-of-random-variables
title: Conditional Distributions
domain: mathematics
course: probability-and-statistics
prerequisites:
- id: marginal-distributions-from-joint
  type: hard
- id: conditional-probability
  type: hard
- id: conditional-distributions-theory
  type: soft
builds-toward:
- conditional-expectation
- bivariate-normal-distribution
tags:
- conditional-distributions
- multivariate
- probability
stage: formal-systems
status: validated
---
# Conditional Distributions

## Core Idea
The conditional distribution of X given Y=y is the distribution of X when Y is fixed: P(X=x|Y=y) = P(X=x,Y=y)/P(Y=y). Conditional distributions capture how one variable's distribution depends on another's value.

## How It's Best Learned
From a joint distribution table, select a column or row and normalize it to sum to 1. For continuous distributions, condition by dividing joint PDF by marginal PDF. Compare conditional distributions for different values.

## Questions

```yaml
- question: "A joint probability table shows P(X=1, Y=2) = 0.12 and P(Y=2) = 0.30. What is P(X=1 | Y=2)?"
  type: multiple-choice
  options:
    - "0.036 — multiply joint by marginal to condition"
    - "0.40 — divide joint probability by the marginal of Y"
    - "2.5 — divide marginal of Y by joint probability"
    - "0.12 — the joint probability already represents the conditional"
  answer: 1
  explanation: "The definition of conditional probability is P(X=x | Y=y) = P(X=x, Y=y) / P(Y=y). Here that's 0.12 / 0.30 = 0.40. Option A reverses the operation (multiplication instead of division). Option D confuses the joint probability with the conditional — the joint has not been normalized to the subpopulation where Y=2."

- question: "You compute the conditional distribution of X given Y=y for three different values of y, and find that all three conditional distributions are identical. What can you conclude?"
  type: multiple-choice
  options:
    - "You made an error — if all conditionals are the same, the joint table must be uniform"
    - "X and Y are independent — knowing the value of Y provides no information about X's distribution"
    - "Y must be a constant random variable taking only one value"
    - "X must be a constant random variable"
  answer: 1
  explanation: "Independence means the conditional distribution of X given Y=y equals the marginal distribution of X for every value y. If all conditional distributions are identical to each other, knowing Y changes nothing about our picture of X — this is precisely the definition of independence. Option A is wrong: the joint can assign unequal probabilities to cells while still having identical conditional distributions (just scale each row by its marginal). Options C and D are unjustified — neither variable need be constant."

- question: "The conditional distribution P(X | Y = y) is typically well-defined for any value y that Y can take."
  type: true-false
  answer: false
  explanation: "The conditional distribution requires dividing by P(Y=y). If P(Y=y) = 0, this division is undefined. In the discrete case, this means conditioning on a value y that has zero probability. In the continuous case, every individual value has probability zero, which is why continuous conditional distributions are defined via density ratios f(x,y)/f_Y(y) — but this still requires f_Y(y) > 0."

- question: "If X and Y are independent random variables, then the conditional distribution of X given Y = y is identical to the marginal distribution of X."
  type: true-false
  answer: true
  explanation: "Independence means P(X=x, Y=y) = P(X=x) × P(Y=y). Dividing both sides by P(Y=y) gives P(X=x | Y=y) = P(X=x). The conditional distribution collapses to the marginal — knowing Y tells you nothing new about X. This is equivalent to saying all 'columns' of the joint table, after normalization, look the same."

- question: "Why must you divide by the marginal probability P(Y=y) when computing the conditional distribution P(X | Y=y), and what does this normalization represent intuitively?"
  type: short-answer
  answer: "Dividing by P(Y=y) rescales the joint probabilities so they sum to 1 within the subpopulation where Y=y. Intuitively, conditioning on Y=y means you zoom in to only those outcomes where Y took value y. Within that restricted population, the relative probabilities of different X values are given by the joint probabilities in that slice — but those slice probabilities don't sum to 1 on their own (they sum to P(Y=y)). Dividing by P(Y=y) restores the sum-to-1 property, making the result a valid probability distribution for X within the Y=y subpopulation."
  explanation: "This normalization is the same operation as in elementary conditional probability P(A|B) = P(A∩B)/P(B) — the denominator ensures the conditional measure is a proper probability. Without it, P(X=x | Y=y) across all x would sum to P(Y=y) instead of 1, which is not a valid probability distribution."
```

## Explainer

You know how to work with joint distributions — probability tables or density functions describing two random variables simultaneously — and you know conditional probability: P(A|B) = P(A∩B)/P(B). Conditional distributions combine these ideas. Instead of asking for the probability of a single event given another event, you ask: what does the entire distribution of X look like when Y is fixed at a specific value?

In the discrete case, the idea is concrete. Suppose (X, Y) has a joint probability table. Fix a particular value y for Y. The **conditional distribution of X given Y = y** is the distribution you get by looking only at the column (or row) of the table where Y = y, then rescaling so the values sum to 1. Formally: P(X = x | Y = y) = P(X = x, Y = y) / P(Y = y). The denominator P(Y = y) is the **marginal probability** of that value of Y, obtained by summing the column — exactly the marginal distribution you know how to compute. Dividing by this sum is the normalization step: you zoom in on the subpopulation where Y = y and rescale to form a valid probability distribution for X within that subpopulation.

In the continuous case, individual values have probability zero, so the formula P(X = x | Y = y) / P(Y = y) would be 0/0. Instead, the **conditional density** is defined as the ratio of densities: f_{X|Y}(x|y) = f_{X,Y}(x, y) / f_Y(y). This is the same logical structure — numerator is joint, denominator is marginal — just expressed in terms of density functions rather than probabilities. To verify it is a valid density: integrate over x, getting ∫ f_{X,Y}(x,y) dx / f_Y(y) = f_Y(y) / f_Y(y) = 1. The normalization works out automatically from the definition of the marginal.

Conditional distributions reveal the **dependence structure** between variables. If X and Y are independent, the conditional distribution of X given Y = y is identical to the marginal distribution of X — knowing Y tells you nothing about X, and every column of the joint table looks the same after normalization. If they are dependent, the shape of the conditional distribution changes as y varies. Comparing f_{X|Y}(x|y) for several values of y shows exactly how Y "informs" X: which values of X become more or less likely as Y shifts. This comparison is the right way to think about dependence, and it directly motivates conditional expectation — the expected value of X given Y = y, which averages the conditional distribution and becomes the central tool in regression and Bayesian inference.
