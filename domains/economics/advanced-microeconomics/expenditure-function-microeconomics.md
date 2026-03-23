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
stage: formal-systems
status: validated
---

# The Expenditure Function

## Core Idea
The expenditure function e(p, u) gives the minimum income needed to achieve utility level u at prices p. It is the dual problem to utility maximization: solve min_x p·x subject to u(x) ≥ u. The expenditure function is homogeneous of degree 1 in prices and non-decreasing in u. It is the fundamental dual object in consumer theory.

## How It's Best Learned
Derive expenditure functions for standard preferences: perfect complements, perfect substitutes, Cobb-Douglas. Verify homogeneity and check relationship with indirect utility. Compare to Marshallian demands.

## Common Misconceptions
Confusing expenditure function with expenditure itself. Thinking the expenditure function is convex in prices (it is convex). Not recognizing it is the dual of the utility function.

## Questions

```yaml
- question: "All prices in an economy double while a consumer's target utility level remains unchanged. What happens to the value of the expenditure function e(p, u)?"
  type: multiple-choice
  options:
    - "It stays the same — the consumer can achieve the same utility with the same bundle"
    - "It more than doubles — the consumer must substitute toward goods that got relatively less expensive"
    - "It exactly doubles — because the expenditure function is homogeneous of degree 1 in prices"
    - "It depends on the specific utility function"
  answer: 2
  explanation: "The expenditure function is homogeneous of degree 1 in prices: e(λp, u) = λ · e(p, u) for any scalar λ > 0. When all prices double (λ = 2), minimum expenditure exactly doubles. Intuitively, the optimal bundle does not change when all prices double proportionally (relative prices are unchanged), so the cost of that bundle simply doubles. Option D is the tempting wrong answer — while the specific value of e depends on the utility function, the homogeneity property holds for all well-behaved utility functions."

- question: "Which of the following correctly describes the expenditure function e(p, u)?"
  type: multiple-choice
  options:
    - "The total amount a consumer actually spends given income m and prices p"
    - "The maximum utility achievable with income m at prices p"
    - "The minimum income needed to reach utility level u at prices p"
    - "The marginal cost of increasing utility by one unit at prices p"
  answer: 2
  explanation: "The expenditure function answers the question: 'What is the least I must spend to achieve exactly utility u, given prices p?' It is defined as e(p, u) = min_x {p·x : u(x) ≥ u}. Option A confuses the function (a mapping from prices and utility to a number) with actual realized expenditure. Option B describes the indirect utility function — the dual object. Option D is not a standard concept in this context."

- question: "The expenditure function e(p, u) and the indirect utility function v(p, m) contain exactly the same information about consumer preferences."
  type: true-false
  answer: true
  explanation: "These two functions are inverses of each other: e(p, v(p, m)) = m and v(p, e(p, u)) = u. The primal problem (maximize utility given income) and the dual problem (minimize expenditure given utility) yield the same underlying preference structure, just represented from opposite perspectives. Any welfare question you can answer with one representation you can answer with the other — the choice between them is purely a matter of mathematical convenience."

- question: "Because achieving higher utility always requires more spending, the expenditure function is convex in u."
  type: true-false
  answer: false
  explanation: "The expenditure function is non-decreasing in u (higher utility targets require at least as much spending), but the relevant convexity property is concavity in prices, not convexity in utility. The concavity in prices reflects the consumer's ability to substitute toward relatively cheaper goods when a price rises, which means expenditure does not rise as fast as a proportional price increase would suggest. The confusion between 'non-decreasing' and 'convex' is a common error."

- question: "How does the expenditure function differ from simply 'the amount a consumer spends,' and what is its duality relationship with the indirect utility function?"
  type: short-answer
  answer: "The expenditure function e(p, u) is not a number but a function that maps any combination of prices and a target utility level to the minimum cost of achieving that utility. Actual expenditure is a single number for a specific situation. The duality relationship is that e and the indirect utility function v are inverses: e(p, v(p, m)) = m (spending the minimum to reach the utility you'd get from income m costs exactly m) and v(p, e(p, u)) = u (using the minimum expenditure to achieve u gives you exactly utility u)."
  explanation: "This duality means the expenditure-minimization and utility-maximization problems are two sides of the same coin. Any result derived from one can be translated to the other. In practice, the expenditure function is easier to use for welfare analysis and for cleanly separating income and substitution effects via Hicksian demand."
```

## Explainer

From consumer theory, you know the standard problem: a consumer maximizes utility u(x) subject to a budget constraint p·x ≤ m, producing Marshallian demands and the indirect utility function v(p, m). The **expenditure function** flips this problem on its head. Instead of asking "what is the most utility I can achieve with income m?", it asks "what is the least I must spend to achieve utility level u?" This inversion — from maximization to minimization — is the foundation of duality in consumer theory.

Formally, the expenditure function e(p, u) solves min_x p·x subject to u(x) ≥ u. You are minimizing a linear objective (total spending) subject to a nonlinear constraint (achieving at least utility u). Since you already understand indifference curves, the geometry is straightforward: you are finding the lowest budget line that still touches the indifference curve corresponding to utility u. The point of tangency gives the optimal bundle, and the cost of that bundle is the value of the expenditure function.

The expenditure function has several important properties that follow directly from the optimization. It is **non-decreasing in u** — achieving higher utility requires at least as much spending. It is **non-decreasing in each price** — when goods become more expensive, the minimum cost of reaching any utility level cannot fall. It is **homogeneous of degree 1 in prices** — if all prices double, the minimum expenditure exactly doubles, because the optimal bundle does not change when relative prices are unchanged. It is also **concave in prices**, which reflects the consumer's ability to substitute toward relatively cheaper goods when one price rises. This concavity is crucial for deriving the law of demand.

The real power of the expenditure function is its role as a bridge between two ways of analyzing consumer behavior. The standard (primal) approach starts from utility maximization and gives you Marshallian demands and indirect utility. The dual approach starts from expenditure minimization and gives you Hicksian demands and the expenditure function. These two approaches contain exactly the same information: e(p, v(p, m)) = m and v(p, e(p, u)) = u — the expenditure function and indirect utility function are inverses of each other. This duality means you can move freely between the two representations, choosing whichever is more convenient for the problem at hand. As you will see when you study Hicksian demand, this flexibility is essential for cleanly decomposing price effects into substitution and income components.
