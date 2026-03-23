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
status: validated
---

# König's Theorem and Matching-Cover Duality

## Core Idea
König's Theorem states that in a bipartite graph, the size of the maximum matching equals the size of the minimum vertex cover. This fundamental duality shows that finding maximum matchings and minimum covers are essentially the same problem in bipartite graphs, with profound implications for optimization.

## How It's Best Learned
Work through small bipartite graphs, computing maximum matchings and minimum covers, verifying they have equal size.

## Common Misconceptions
This equality holds ONLY for bipartite graphs; in general graphs, matching size can be strictly less than vertex cover size.

## Questions

```yaml
- question: "In the Petersen graph (a non-bipartite graph), the maximum matching has size 5 but the minimum vertex cover has size 6. What does this demonstrate?"
  type: multiple-choice
  options:
    - "König's Theorem was applied incorrectly — the maximum matching must be recalculated"
    - "The Petersen graph has a structural error in its construction"
    - "König's Theorem applies only to bipartite graphs; the equality between maximum matching and minimum vertex cover fails in general graphs"
    - "A larger matching could be found with a different augmenting-path algorithm"
  answer: 2
  explanation: "König's Theorem is a bipartite-only result. In any graph, the minimum vertex cover is at least as large as the maximum matching (each matched edge needs at least one cover vertex). In bipartite graphs, equality holds. In general graphs, odd cycles prevent this equality — the Petersen graph is the canonical counterexample with matching size 5 and cover size 6. This gap confirms the bipartite condition is essential, not incidental."

- question: "In a bipartite graph where the maximum matching has size 7, what is the minimum number of vertices needed to cover every edge?"
  type: multiple-choice
  options:
    - "It cannot be determined without knowing the total number of vertices"
    - "14 vertices — one for each endpoint of each matched edge"
    - "7 vertices, by König's Theorem"
    - "At least 7, but possibly more depending on graph structure"
  answer: 2
  explanation: "König's Theorem states that in a bipartite graph, maximum matching size = minimum vertex cover size. If the maximum matching has size 7, then the minimum vertex cover also has size exactly 7. Option D would be correct for general graphs, where the minimum cover can exceed the maximum matching. The theorem provides the exact equality for bipartite graphs."

- question: "In any graph (bipartite or not), the minimum vertex cover size is at least as large as the maximum matching size."
  type: true-false
  answer: true
  explanation: "This lower bound holds universally. In any matching, the matched edges share no endpoints, so each matched edge requires at least one distinct vertex in any cover. Therefore the cover must contain at least as many vertices as there are matched edges. König's Theorem says this lower bound is achieved exactly in bipartite graphs — the maximum matching and minimum vertex cover have the same size — but the inequality holds for all graphs."

- question: "König's Theorem states that maximum matching equals minimum vertex cover in all graphs."
  type: true-false
  answer: false
  explanation: "This equality holds only for bipartite graphs. In general (non-bipartite) graphs, odd cycles cause the matching size to be strictly less than the minimum vertex cover. The Petersen graph provides a concrete counterexample: maximum matching size 5, minimum vertex cover size 6. The bipartite condition is necessary for the min-max equality to hold."

- question: "Why is König's Theorem described as a 'min-max duality,' and what makes this surprising?"
  type: short-answer
  answer: "A min-max duality means the maximum value of one optimization objective equals the minimum value of a different, apparently opposite objective. Maximum matching aims to select as many non-overlapping edges as possible; minimum vertex cover aims to select as few vertices as possible while touching every edge. These seem like unrelated problems pulling in opposite directions — one maximizing, one minimizing, one operating on edges, one on vertices. What is surprising is that in bipartite graphs, these two problems yield exactly the same optimal value. This reflects a deep combinatorial structure analogous to LP duality: the primal and dual problems are equivalent, with no gap between them."
  explanation: "This duality is not obvious from the problem definitions. The fact that 'how many independent edges can you pack?' and 'how few vertices can you use to touch everything?' give the same answer in bipartite graphs is the content of the theorem. It enables efficient algorithms: solving one problem automatically solves the other. The failure in general graphs (due to odd cycles) further demonstrates that the equality is a structural property of bipartiteness, not a universal combinatorial coincidence."
```

## Explainer

You've studied Hall's Marriage Theorem, which tells you when a perfect matching exists in a bipartite graph: every subset S on one side must have at least |S| neighbors. König's Theorem deepens this insight into a duality: in a bipartite graph, the size of the **maximum matching** always equals the size of the **minimum vertex cover**. These are two different optimization problems that turn out to have the same answer — a surprising and powerful equivalence.

First, make sure both concepts are clear. A **matching** is a set of edges sharing no endpoints — each vertex appears in at most one selected edge. The goal is to select as many edges as possible without conflict. A **vertex cover** is a set of vertices such that every edge has at least one endpoint in the set. The goal is to "cover" all edges using as few vertices as possible. These objectives pull in opposite directions: a matching wants many non-overlapping edges, a cover wants few vertices touching everything. For any graph, the minimum vertex cover size is at least the maximum matching size — because each matched edge needs a separate vertex to cover it. König's Theorem says equality holds for bipartite graphs.

The proof uses the augmenting path technique underlying Hall's theorem. Given a maximum matching M, start from the left-side vertices not matched by M and explore alternating paths: edges not in M followed by edges in M, and so on. The vertices reachable by these alternating paths define a set Z. The minimum vertex cover is then constructed as: the left-side vertices not in Z, plus the right-side vertices that are in Z. Careful analysis shows this cover has exactly the same size as the matching M, proving equality. The bipartite structure is essential: in a general graph, odd cycles can cause the matching to be strictly smaller than the minimum cover, breaking the equality.

The theorem has a striking min-max interpretation. In scheduling problems modeled as bipartite graphs — tasks on one side, machines on the other, edges indicating compatibility — the maximum number of simultaneously assignable task-machine pairs equals the minimum number of conflicts that must be blocked to make any assignment feasible. This **min-max duality** (maximum of one thing equals minimum of another) is a recurring theme in combinatorics and optimization. König's Theorem is in fact the combinatorial analogue of LP duality for bipartite matching: the primal problem (maximize matching) and its dual (minimize cover) have equal optimal values. For non-bipartite graphs, this breaks — the Petersen graph's maximum matching has size 5 while its minimum vertex cover has size 6 — demonstrating that König's result is uniquely a bipartite phenomenon.
