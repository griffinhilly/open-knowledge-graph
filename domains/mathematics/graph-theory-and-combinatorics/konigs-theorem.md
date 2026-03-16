---
id: konigs-theorem
title: König's Theorem and Matching-Cover Duality
domain: mathematics
course: graph-theory-and-combinatorics
prerequisites:
- id: halls-marriage-theorem
  type: hard
tags:
- graph-theory
- matching
- vertex-cover
stage: formal-systems
status: draft
---

# König's Theorem and Matching-Cover Duality

## Core Idea
König's Theorem states that in a bipartite graph, the size of the maximum matching equals the size of the minimum vertex cover. This fundamental duality shows that finding maximum matchings and minimum covers are essentially the same problem in bipartite graphs, with profound implications for optimization.

## How It's Best Learned
Work through small bipartite graphs, computing maximum matchings and minimum covers, verifying they have equal size.

## Common Misconceptions
This equality holds ONLY for bipartite graphs; in general graphs, matching size can be strictly less than vertex cover size.

## Explainer

You've studied Hall's Marriage Theorem, which tells you when a perfect matching exists in a bipartite graph: every subset S on one side must have at least |S| neighbors. König's Theorem deepens this insight into a duality: in a bipartite graph, the size of the **maximum matching** always equals the size of the **minimum vertex cover**. These are two different optimization problems that turn out to have the same answer — a surprising and powerful equivalence.

First, make sure both concepts are clear. A **matching** is a set of edges sharing no endpoints — each vertex appears in at most one selected edge. The goal is to select as many edges as possible without conflict. A **vertex cover** is a set of vertices such that every edge has at least one endpoint in the set. The goal is to "cover" all edges using as few vertices as possible. These objectives pull in opposite directions: a matching wants many non-overlapping edges, a cover wants few vertices touching everything. For any graph, the minimum vertex cover size is at least the maximum matching size — because each matched edge needs a separate vertex to cover it. König's Theorem says equality holds for bipartite graphs.

The proof uses the augmenting path technique underlying Hall's theorem. Given a maximum matching M, start from the left-side vertices not matched by M and explore alternating paths: edges not in M followed by edges in M, and so on. The vertices reachable by these alternating paths define a set Z. The minimum vertex cover is then constructed as: the left-side vertices not in Z, plus the right-side vertices that are in Z. Careful analysis shows this cover has exactly the same size as the matching M, proving equality. The bipartite structure is essential: in a general graph, odd cycles can cause the matching to be strictly smaller than the minimum cover, breaking the equality.

The theorem has a striking min-max interpretation. In scheduling problems modeled as bipartite graphs — tasks on one side, machines on the other, edges indicating compatibility — the maximum number of simultaneously assignable task-machine pairs equals the minimum number of conflicts that must be blocked to make any assignment feasible. This **min-max duality** (maximum of one thing equals minimum of another) is a recurring theme in combinatorics and optimization. König's Theorem is in fact the combinatorial analogue of LP duality for bipartite matching: the primal problem (maximize matching) and its dual (minimize cover) have equal optimal values. For non-bipartite graphs, this breaks — the Petersen graph's maximum matching has size 5 while its minimum vertex cover has size 6 — demonstrating that König's result is uniquely a bipartite phenomenon.
