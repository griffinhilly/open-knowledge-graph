---
id: expenditure-function-microeconomics
title: The Expenditure Function
domain: economics
course: advanced-microeconomics
prerequisites:
- id: consumer-theory-utility
  type: hard
- id: indifference-curves
  type: hard
builds-toward:
- duality-consumer-theory
- hicksian-demand
tags:
- consumer-theory
- cost-minimization
- duality
stage: abstract-reasoning
status: draft
---

# The Expenditure Function

## Core Idea
The expenditure function e(p, u) gives the minimum income needed to achieve utility level u at prices p. It is the dual problem to utility maximization: solve min_x p·x subject to u(x) ≥ u. The expenditure function is homogeneous of degree 1 in prices and non-decreasing in u. It is the fundamental dual object in consumer theory.

## How It's Best Learned
Derive expenditure functions for standard preferences: perfect complements, perfect substitutes, Cobb-Douglas. Verify homogeneity and check relationship with indirect utility. Compare to Marshallian demands.

## Common Misconceptions
Confusing expenditure function with expenditure itself. Thinking the expenditure function is convex in prices (it is convex). Not recognizing it is the dual of the utility function.

## Explainer

From consumer theory, you know the standard problem: a consumer maximizes utility u(x) subject to a budget constraint p·x ≤ m, producing Marshallian demands and the indirect utility function v(p, m). The **expenditure function** flips this problem on its head. Instead of asking "what is the most utility I can achieve with income m?", it asks "what is the least I must spend to achieve utility level u?" This inversion — from maximization to minimization — is the foundation of duality in consumer theory.

Formally, the expenditure function e(p, u) solves min_x p·x subject to u(x) ≥ u. You are minimizing a linear objective (total spending) subject to a nonlinear constraint (achieving at least utility u). Since you already understand indifference curves, the geometry is straightforward: you are finding the lowest budget line that still touches the indifference curve corresponding to utility u. The point of tangency gives the optimal bundle, and the cost of that bundle is the value of the expenditure function.

The expenditure function has several important properties that follow directly from the optimization. It is **non-decreasing in u** — achieving higher utility requires at least as much spending. It is **non-decreasing in each price** — when goods become more expensive, the minimum cost of reaching any utility level cannot fall. It is **homogeneous of degree 1 in prices** — if all prices double, the minimum expenditure exactly doubles, because the optimal bundle does not change when relative prices are unchanged. It is also **concave in prices**, which reflects the consumer's ability to substitute toward relatively cheaper goods when one price rises. This concavity is crucial for deriving the law of demand.

The real power of the expenditure function is its role as a bridge between two ways of analyzing consumer behavior. The standard (primal) approach starts from utility maximization and gives you Marshallian demands and indirect utility. The dual approach starts from expenditure minimization and gives you Hicksian demands and the expenditure function. These two approaches contain exactly the same information: e(p, v(p, m)) = m and v(p, e(p, u)) = u — the expenditure function and indirect utility function are inverses of each other. This duality means you can move freely between the two representations, choosing whichever is more convenient for the problem at hand. As you will see when you study Hicksian demand, this flexibility is essential for cleanly decomposing price effects into substitution and income components.
