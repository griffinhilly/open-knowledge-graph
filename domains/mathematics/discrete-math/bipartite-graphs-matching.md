---
id: bipartite-graphs-matching
title: Bipartite Graphs and Matching Problems
domain: mathematics
course: discrete-math
prerequisites:
- id: bipartite-graphs
  type: hard
- id: graph-coloring-discrete
  type: soft
builds-toward:
- hamiltonian-cycles-discrete
tags:
- bipartite
- matching
- Hall's-theorem
- perfect-matching
stage: formal-systems
status: validated
---

# Bipartite Graphs and Matching Problems

## Core Idea
A bipartite graph has vertex partition into two sets with edges only between sets (not within). A matching is a set of disjoint edges. Hall's marriage theorem characterizes when a perfect matching (every vertex matched) exists in a bipartite graph.

## How It's Best Learned
Recognize bipartite graphs: they have no odd cycles. Use BFS/DFS to 2-color them. Apply Hall's theorem to prove existence of matchings. Model problems as bipartite matching: job assignments, system administrators, Latin rectangles.

## Common Misconceptions
A bipartite graph need not be complete bipartite. Hall's condition is necessary and sufficient: every subset S of one part must have at least |S| neighbors on the other side.

## Questions

```yaml
- question: "Five job applicants each have exactly two job openings they qualify for, drawn from a pool of 10 openings. Does this guarantee a perfect matching exists?"
  type: multiple-choice
  options:
    - "Yes — each applicant has 2 choices, and 2 ≥ 1 so Hall's condition is satisfied"
    - "No — Hall's condition depends on which specific jobs each applicant qualifies for, not just how many"
    - "Yes — there are more openings (10) than applicants (5), so matches are always available"
    - "No — bipartite matching only applies when all left vertices have degree at least 3"
  answer: 1
  explanation: "Hall's condition must be checked for every subset S of left vertices, not just for individual vertices. Even though each applicant has 2 options, it is possible that all 5 applicants are only interested in the same 2 jobs — in which case the subset S = {all 5 applicants} has |N(S)| = 2 < 5, violating Hall's condition and making a perfect matching impossible. The number of openings and individual degrees don't capture this 'too many applicants share the same options' failure."

- question: "Hall's condition fails for some subset S of left vertices — specifically, S has 4 left vertices but only 3 distinct neighbors on the right. What can you conclude?"
  type: multiple-choice
  options:
    - "No matching of any kind exists in the graph"
    - "A perfect matching from the left side is impossible, but a maximum matching may still include some left vertices"
    - "The graph cannot be bipartite if Hall's condition fails"
    - "The condition only shows that a perfect matching from the right side doesn't exist"
  answer: 1
  explanation: "Hall's theorem is specifically about perfect matchings from the left side (matching every left vertex). If the condition fails for S, those 4 left vertices cannot all be matched simultaneously since there are only 3 right vertices available for them. However, a maximum matching still exists — it may match 3 of those 4 vertices and all others where the condition holds. Hall's failure rules out 'everyone matched,' not 'anyone matched.'"

- question: "Hall's condition must be verified for every subset of left vertices — even a single subset violating the condition is sufficient to prove no perfect matching exists."
  type: true-false
  answer: true
  explanation: "Hall's theorem is an 'if and only if' result: a perfect matching from the left side exists precisely when Hall's condition holds for ALL subsets. This means necessity runs both ways — if any single subset S has |N(S)| < |S|, you immediately know no perfect matching is possible, because those |S| left vertices cannot all find distinct mates. You don't need to check the rest of the graph once a violating subset is found."

- question: "If every left vertex in a bipartite graph has at least one neighbor on the right side, Hall's condition is automatically satisfied and a perfect matching must exist."
  type: true-false
  answer: false
  explanation: "This is the most common misconception about Hall's theorem. Having at least one neighbor for each individual vertex only checks subsets of size 1. The condition can still fail for larger subsets. A simple counterexample: three left vertices all connected to the same single right vertex — each has a neighbor, but the subset {all three} has |N(S)| = 1 < 3, and no perfect matching exists. Hall's condition is collective, not individual."

- question: "Why is Hall's condition 'collective' rather than 'individual'? Give a concrete example that shows why checking each left vertex individually is insufficient to guarantee a perfect matching."
  type: short-answer
  answer: "Hall's condition is collective because a perfect matching requires each left vertex to be assigned a *distinct* right vertex — sharing is not allowed. Checking individually only verifies that each vertex has some neighbor, not that the neighborhood structure allows all of them to be matched simultaneously. Example: 3 applicants (A, B, C) each qualified for exactly 1 job, and all three qualify for the same job J. Each has a neighbor, but the subset S = {A, B, C} has N(S) = {J}, so |N(S)| = 1 < 3 = |S|. No perfect matching exists — only one applicant can get job J."
  explanation: "The insight is that a perfect matching is a global combinatorial constraint. Local availability (each vertex has a neighbor) does not imply global feasibility (all can be matched simultaneously without conflict). Hall's theorem captures exactly what must hold globally — that no subset is 'too picky' — and proves that this necessary condition is also sufficient."
```

## Explainer

A bipartite graph divides its vertices into two distinct groups — call them "left" and "right" — where edges only connect a left vertex to a right vertex, never two vertices within the same group. From your prior work on bipartite graphs, you know this two-colorability is equivalent to having no odd cycles. The classic real-world picture: left vertices are job applicants, right vertices are open positions, and edges connect each applicant to the jobs they qualify for. The question "can we assign everyone to a job?" is exactly a **matching** problem.

A matching is a set of edges with no shared endpoints — each vertex appears in at most one matched pair. A **perfect matching** matches every vertex on one side (or both sides if they're equal in size). The central theorem is **Hall's Marriage Theorem**: a bipartite graph has a perfect matching from the left side if and only if for every subset S of left vertices, the set of their neighbors N(S) satisfies |N(S)| ≥ |S|. This is called **Hall's condition**. Intuitively, it says no subset of applicants is "too picky" — every group of k applicants must collectively be interested in at least k distinct jobs.

The necessity of Hall's condition is immediate: if some subset S of left vertices has fewer than |S| neighbors on the right, there simply aren't enough distinct right vertices to match all of S, so a perfect matching is impossible. The sufficiency — that Hall's condition guarantees a perfect matching exists — requires a proof, typically by induction on the size of the graph. You build a matching greedily where the condition is tight (|N(S)| = |S| for some S), then handle the slack cases where you have room to maneuver.

In practice, **augmenting path algorithms** find the actual maximum matching efficiently. An augmenting path is a path that starts and ends at unmatched vertices and alternates between unmatched and matched edges. Following this path toggles the matching status of each edge on the path, increasing the matching size by one. The algorithm terminates when no augmenting path exists — at that point, the matching is maximum. Hall's theorem converts an existential question ("does a perfect matching exist?") into a combinatorial condition you can verify, while augmenting paths give you the constructive algorithm to find it.
