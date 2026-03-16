---
id: closed-graph-theorem
title: Closed Graph Theorem
domain: mathematics
course: measure-theory-and-functional-analysis
prerequisites:
- id: banach-spaces-definition
  type: hard
tags:
- functional-analysis
stage: abstract-reasoning
status: draft
---

# Closed Graph Theorem

## Core Idea
The closed graph theorem states that a linear operator T: X → Y between Banach spaces is continuous if and only if its graph {(x, T(x)) : x ∈ X} is closed in X × Y. This provides a powerful criterion for continuity without explicit bound verification.

## Explainer

From your study of Banach spaces, you know that a Banach space is a complete normed vector space — complete meaning every Cauchy sequence converges. Continuity of a linear operator T: X → Y means small inputs produce small outputs, equivalently that T is **bounded**: there exists a constant C such that ‖T(x)‖ ≤ C‖x‖ for all x. Proving this directly often requires knowing the bound C explicitly. The closed graph theorem provides an indirect route: instead of bounding T, check a topological property of its graph.

The **graph** of T is the set of input-output pairs Γ(T) = {(x, T(x)) : x ∈ X}, living in the product space X × Y. Saying the graph is **closed** means: whenever a sequence (xₙ, T(xₙ)) converges to some pair (x, y) in X × Y, then y = T(x). In plain English — if inputs converge and outputs converge, the limit of the outputs must equal T applied to the limit of the inputs. This is weaker than continuity, because it requires *both* sequences to converge as a hypothesis; continuity only requires input convergence. For arbitrary maps these notions differ, but for linear operators between Banach spaces they collapse to the same thing.

Why does completeness matter? The proof leverages the open mapping theorem: a bijective bounded linear operator between Banach spaces has a bounded inverse. If T has a closed graph, one can construct an auxiliary operator that makes T continuous by exploiting the closed graph to "borrow" convergence from one space to the other. The full argument uses the completeness of both spaces in a critical way — the theorem fails for incomplete spaces. This is why Banach spaces, not just normed spaces, are the natural setting.

The practical value of the closed graph theorem is that it shifts the proof burden. To show T is continuous, you don't need to find the constant C or directly verify the bound. Instead, you verify a sequential condition: if xₙ → x and T(xₙ) → y, then y = T(x). This is often much easier to check from the definition of T. Many operators in analysis — differential operators, integral operators — are most naturally verified continuous by this route rather than by direct estimation.
