---
id: expectation-linearity-counting
title: Linearity of Expectation in Counting
domain: mathematics
course: discrete-math
prerequisites:
- id: expected-value
  type: hard
- id: counting-principles
  type: soft
builds-toward:
- probabilistic-method-counting
tags:
- probability
- counting
- expectation
stage: formal-systems
status: draft
---

# Linearity of Expectation in Counting

## Core Idea
Linearity of expectation states that E[X₁ + X₂ + ... + Xₙ] = E[X₁] + E[X₂] + ... + E[Xₙ], even when variables are dependent. This powerful tool in combinatorics simplifies counting problems by breaking them into indicator random variables and computing expected values.

## Explainer

You already know from your prerequisite that **expected value** is the probability-weighted average of a random variable's possible outcomes. Linearity of expectation says something deceptively simple: the expected value of a sum is always the sum of the expected values — even when the summands are *not* independent. This "even when dependent" clause is what makes it a power tool rather than just a tautology.

The key technique is **indicator random variables**. For any event A, define the indicator Iₐ as 1 if A occurs and 0 otherwise. Then E[Iₐ] = P(A), which is often straightforward to compute. Now suppose you want the expected number of times some thing happens in a complex random process — say, the expected number of fixed points in a random permutation (elements that map to themselves). Direct computation via the full probability distribution is painful. Instead: let Xᵢ = 1 if element i is a fixed point. Then the total number of fixed points is X = X₁ + X₂ + ⋯ + Xₙ, and by linearity E[X] = E[X₁] + ⋯ + E[Xₙ]. Each E[Xᵢ] = P(element i is fixed) = 1/n. So E[X] = n · (1/n) = 1 — regardless of n, a random permutation has on average exactly one fixed point.

The reason linearity holds even for dependent variables comes down to the definition of expectation as an integral (or sum) — linearity of integration is unconditional. This is the key contrast with variance: Var(X + Y) = Var(X) + Var(Y) only when X and Y are independent. Expectation's linearity is genuinely unconditional.

A counting application: you want to know the expected number of edges in a random subgraph where each edge is included independently with probability p. Without linearity, you'd need to sum over all possible subgraphs — combinatorially intractable. With linearity, let Xₑ be the indicator for each edge e. Then E[total edges] = Σₑ E[Xₑ] = Σₑ p = p·|E|. The answer is immediate. The general pattern is always: identify the quantity as a sum of indicators, compute each indicator's expectation separately, then add them up. This technique, combined with your knowledge of counting principles for enumerating the indicators, converts hard combinatorial problems into collections of easy probability calculations.
