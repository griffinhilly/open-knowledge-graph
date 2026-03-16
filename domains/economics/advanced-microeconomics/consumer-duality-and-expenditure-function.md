---
id: consumer-duality-and-expenditure-function
title: 'Consumer Duality: Expenditure and Indirect Utility Functions'
domain: economics
course: advanced-microeconomics
prerequisites:
- id: consumer-theory-utility
  type: hard
- id: consumer-optimum
  type: hard
- id: lagrange-multipliers
  type: hard
- id: partial-derivatives
  type: soft
- id: constrained-optimization-lagrange
  type: hard
builds-toward:
- hicksian-demand-functions
- compensating-and-equivalent-variation
tags:
- consumer-theory
- duality
- optimization
stage: advanced
status: draft
---

# Consumer Duality: Expenditure and Indirect Utility Functions

## Core Idea
Consumer duality states that utility maximization (fixing income, maximizing utility) and expenditure minimization (fixing utility, minimizing spending) yield the same optimal bundle. Marshallian demand and indirect utility come from the utility problem; Hicksian demand and expenditure function come from the expenditure problem. Shephard's lemma and Roy's identity connect these dual approaches.

## Explainer

You already know the consumer's problem from introductory theory: given income *m* and prices *p*, choose the bundle that maximizes utility subject to the budget constraint. This is the **primal problem**, and its solution gives you **Marshallian (ordinary) demand functions** — quantities demanded as functions of prices and income. Plugging the optimal bundle back into the utility function gives the **indirect utility function** V(p, m), which tells you the maximum utility achievable at given prices and income. So far, this is review. Duality asks: what if we flip the problem?

The **dual problem** fixes a target utility level ū and asks: what is the minimum expenditure needed to reach ū at prices *p*? This is expenditure minimization subject to a utility constraint, and it is the mirror image of the primal. Its solution gives **Hicksian (compensated) demand functions** — quantities demanded as functions of prices and a utility target rather than income. The minimum cost of reaching ū is the **expenditure function** e(p, ū). The deep insight of duality is that these two problems are not merely analogous — they produce the *same* optimal bundle. At the optimum, the consumer who maximizes utility with income *m* reaches utility ū, and the consumer who minimizes expenditure to reach ū spends exactly *m*.

This equivalence generates powerful mathematical connections. **Shephard's lemma** states that the partial derivative of the expenditure function with respect to the price of good *i* gives the Hicksian demand for good *i*. This is remarkably useful because the expenditure function is often easier to work with than solving the Hicksian demand directly. **Roy's identity** does the analogous job for the primal: the Marshallian demand for good *i* equals the negative ratio of partial derivatives of the indirect utility function with respect to price *i* and income. These identities mean that if you know *either* the indirect utility function *or* the expenditure function, you can recover all demand functions without re-solving optimization problems.

Why does this matter beyond mathematical elegance? Hicksian demand isolates the **pure substitution effect** of a price change by holding utility constant, which is exactly what you need for welfare analysis. Marshallian demand mixes substitution and income effects together, making it harder to measure how much a price change actually hurts a consumer. The duality framework — and the tools of compensating and equivalent variation that build on it — lets you decompose price changes cleanly, measure welfare changes in money units, and evaluate policies with precision that Marshallian demand alone cannot provide.
