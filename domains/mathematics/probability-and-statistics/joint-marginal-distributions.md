---
id: joint-marginal-distributions
title: Joint and Marginal Distributions
domain: mathematics
course: probability-and-statistics
prerequisites:
- id: random-variables-definition-types
  type: hard
builds-toward:
- conditional-distributions-of-random-variables
- covariance-between-random-variables
tags:
- joint-distribution
- marginal
stage: formal-systems
status: validated
---

# Joint and Marginal Distributions

## Core Idea
Joint PMF/PDF p(x,y) or f(x,y) specifies the probability of pairs. Marginal distributions sum or integrate out the other variable: p_X(x)=∑_y p(x,y). Two variables are independent iff joint factors into marginals: p(x,y)=p_X(x)p_Y(y).

## Questions

```yaml
- question: "You are given the marginal distributions of X and Y completely. What can you determine about their joint distribution p(x,y)?"
  type: multiple-choice
  options:
    - "The joint is fully determined — the marginals contain all information about the pair"
    - "The joint can be recovered by multiplying the two marginals together"
    - "The joint cannot be fully determined — many different joints share the same marginals"
    - "The joint is determined only when X and Y take the same set of values"
  answer: 2
  explanation: "Marginals tell you what each variable does in isolation — they are the 'shadows' of the joint, obtained by summing out the other variable. But the same marginals are consistent with many different joint distributions: X and Y could be positively correlated, negatively correlated, or independent, all while sharing identical marginals. Option B describes exactly the independence case — if X and Y happen to be independent, then the joint does equal the product of marginals. But assuming independence when it hasn't been established is the key error to avoid."

- question: "For discrete X and Y, you verify that p(x,y) = p_X(x)·p_Y(y) holds for 95% of the pairs (x,y) in the support. What can you conclude?"
  type: multiple-choice
  options:
    - "X and Y are approximately independent"
    - "X and Y are independent for practical purposes"
    - "X and Y are not necessarily independent — independence requires the factoring to hold for all pairs"
    - "X and Y are independent if the 5% of failing pairs have small probability"
  answer: 2
  explanation: "Independence is an all-or-nothing condition: p(x,y) = p_X(x)·p_Y(y) must hold for every pair (x,y) without exception. A single violating pair means the variables are dependent. There is no such thing as 'almost independent' in the formal sense — a distribution either factors exactly or it does not. Options A, B, and D reflect the intuition that 'close enough' should count, but in probability theory, dependence is determined by the structure of the full joint, not by a majority of pairs."

- question: "Summing the joint PMF p(x,y) over all values of y yields the marginal PMF p_X(x)."
  type: true-false
  answer: true
  explanation: "This is the defining operation for computing marginals from a joint distribution. By summing out y, you ask: regardless of what Y is doing, what is the probability that X = x? The result — p_X(x) = Σ_y p(x,y) — is the marginal distribution of X. For continuous variables, the analogous operation is integration: f_X(x) = ∫ f(x,y) dy. The marginal is literally the 'margin' of the joint table — what you'd get by collapsing the table into a single column."

- question: "Two random variables with identical marginal distributions is expected to have the same joint distribution."
  type: true-false
  answer: false
  explanation: "This is the core misconception about marginals. Marginals describe each variable individually; the joint describes how they interact. Two entirely different dependency structures can produce identical marginals. For example, if X and Y are both uniform on {0,1}, you could have: (a) an independent joint where p(0,0)=p(0,1)=p(1,0)=p(1,1)=0.25, or (b) a perfectly correlated joint where p(0,0)=p(1,1)=0.5 and p(0,1)=p(1,0)=0. Both have uniform marginals, but completely different joints."

- question: "Explain why you cannot reconstruct a joint distribution from its marginals alone. What does the joint tell you that the marginals do not?"
  type: short-answer
  answer: "The marginals tell you the individual behavior of each variable separately, but say nothing about how the variables relate to each other. The joint distribution captures the dependency structure — whether high values of X tend to coincide with high or low values of Y, and how strongly. This relationship information is entirely absent from the marginals. To reconstruct the joint, you would need additional information such as the conditional distributions or the full covariance structure."
  explanation: "The gap between 'marginals' and 'joint' is precisely the concept of statistical dependence. If X and Y are independent, the joint is completely determined by the marginals (it's their product). But in all other cases, knowing each variable individually gives you no information about their interaction. This is why joint distributions are the fundamental object in multivariate probability — all correlation, regression, and conditional reasoning stems from the additional information the joint contains beyond what the marginals show."
```

## Explainer

When you studied random variables, each variable described the uncertainty about a single quantity — the outcome of one die roll, one measurement, one coin flip. But most real situations involve multiple uncertain quantities at once: the height and weight of a randomly chosen person, the price and volume of a stock, the test scores of two students. Joint distributions are the framework for handling multiple random variables simultaneously.

The **joint PMF** (for discrete variables) p(x, y) = P(X = x and Y = y) assigns a probability to every pair of values. It's a complete description of the relationship between X and Y — not just what each variable does on its own, but how they interact. Think of it as a table (for finite discrete variables): each cell (x, y) holds the probability of that particular combination. All cells must be non-negative, and they must sum to 1. From this table, you can answer any probability question about X and Y together.

**Marginal distributions** recover the individual behavior of each variable from the joint. To find P(X = x), just sum p(x, y) over all possible values of y — you're "summing out" Y, which is equivalent to asking what X is doing regardless of Y's value. Geometrically, if you imagine the joint distribution as a surface over a grid, the marginal of X is the "shadow" of that surface projected onto the x-axis. For continuous variables, summation becomes integration: f_X(x) = ∫ f(x, y) dy. The marginals tell you each variable's individual distribution, but they don't tell you the relationship *between* them.

**Independence** is the key structural condition. X and Y are independent if and only if the joint distribution factors: p(x, y) = p_X(x) · p_Y(y) for all pairs (x, y). In words: knowing X gives you no information about Y, and vice versa. Equivalently, the joint table looks like the "outer product" of the two marginals — every row is a scalar multiple of every other row. Independence is a very strong condition; most interesting pairs of variables are *not* independent, because they tend to be correlated (height and weight, income and education, etc.).

The payoff of understanding joint and marginal distributions is that they enable everything downstream: conditional distributions (what's the distribution of Y given that X = x?), covariance and correlation (how much do X and Y move together?), and the joint behavior of sums and transformations. When you encounter bivariate Normal distributions, regression models, or multivariate statistics, the joint distribution is always the starting point. The marginals describe what each variable does alone; the joint describes what they do together; the gap between those two descriptions is exactly the information carried by their statistical relationship.
