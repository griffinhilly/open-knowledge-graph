---
id: many-one-and-turing-reductions
title: Many-One and Turing Reducibility
domain: formal-sciences-and-logic
course: computability-and-complexity
prerequisites:
- id: computability-reductions
  type: hard
- id: polynomial-time-reductions
  type: soft
tags:
- reductions
- hardness
- decidability
stage: advanced
status: draft
---

# Many-One and Turing Reducibility

## Core Idea
Many-one reducibility (A ≤_m B) transforms instances of A to instances of B via a single function and preserves hardness notions while defining degree structures. Turing reducibility (A ≤_T B) allows using a B-oracle adaptively during computation, classifying problems by computational power more finely. While many-one reducibility is standard for NP-completeness, Turing reducibility is more fundamental in computability theory and degree theory.

## Explainer

You already understand reductions as the tool for comparing problem difficulty: if A reduces to B, then B is at least as hard as A. The distinction between **many-one** and **Turing** reducibility is about *how much power* the reduction itself is allowed to use — specifically, how many oracle queries it makes and whether it can adapt based on the answers.

A **many-one reduction** from A to B (written A ≤_m B) is the most restrictive form: you are given one instance of A, you compute a single instance of B, and you accept or reject based solely on whether that one B-instance is in B. The reduction makes exactly one non-adaptive query. This is the reduction you use in NP-completeness: to show SAT ≤_m 3-COLOR, you map each SAT formula to a graph such that the formula is satisfiable iff the graph is 3-colorable. You never look at what the answer is before finishing the transformation.

A **Turing reduction** from A to B (written A ≤_T B) models computation *with a B-oracle*: a machine that can query "is x ∈ B?" at any point during computation, receive a yes/no answer immediately, and then continue computing based on the result. It can make many queries, and later queries can depend on the answers to earlier ones. This is strictly more powerful. For example, the complement of the halting problem is not many-one reducible to the halting problem, but it *is* Turing reducible (use the oracle to answer the halting question, then flip the output). Many-one reduction can preserve complement only in special cases; Turing reduction handles complements trivially.

The difference creates two distinct **degree structures**. **Turing degrees** (also called degrees of unsolvability) group languages together if A ≤_T B and B ≤_T A — they have the same computational power, even if one is not many-one reducible to the other. **Many-one degrees** are finer: A and its complement are in the same Turing degree but generally different many-one degrees. Computability theory is largely organized around Turing degrees, while complexity theory (especially NP-completeness) uses many-one reductions because they better capture the notion of "no extra power in the reduction itself."

The key contrast to internalize: many-one reducibility is the **one-query, no-feedback** version — the reduction commits to a single transformed instance before seeing any answer. Turing reducibility is the **adaptive oracle** version — the reduction can conduct a dialogue with B, updating its strategy as it learns. Because many-one is strictly weaker, A ≤_m B implies A ≤_T B but not conversely. When a problem is **NP-complete under many-one reductions**, it is also complete under Turing reductions — but not vice versa. This makes NP-completeness under many-one reductions the more informative (and harder to achieve) statement.

