---
id: bipartite-matching
title: Matchings in Bipartite Graphs
domain: mathematics
course: graph-theory-and-combinatorics
prerequisites:
- id: bipartite-graphs
  type: hard
builds-toward:
- halls-marriage-theorem
- konigs-theorem
tags:
- graph-theory
- matching
- bipartite
stage: advanced
status: validated
---

# Matchings in Bipartite Graphs

## Core Idea
A matching is a set of edges with no shared vertices; in bipartite graphs, matchings model assignments between two sets. A maximum matching uses the most edges; a perfect matching covers all vertices. Bipartite matching is fundamental to applications like job assignment, resource allocation, and network optimization.

## Questions

```yaml
- question: "In a bipartite graph with |L| = |R| = 6, the maximum matching has size 5. What can you conclude?"
  type: multiple-choice
  options:
    - "A perfect matching exists — size 5 is close enough to size 6 that it qualifies"
    - "A perfect matching does not exist, since at least one vertex on each side is unmatched"
    - "A perfect matching does not exist, since at least one vertex on some side is unmatched"
    - "You cannot conclude anything about perfect matchings from the maximum matching size alone"
  answer: 2
  explanation: "A perfect matching requires every vertex on both sides to be matched. A maximum matching of size 5 in a 6-6 bipartite graph leaves at least one vertex unmatched on one side. In fact, since matching edges pair one vertex from L with one from R, a matching of size 5 leaves exactly one vertex unmatched on each side — so no perfect matching exists. Note that option B says 'each side,' which is correct for this case."

- question: "An augmenting path in a matching M alternates between edges not in M and edges in M. What property must it have for it to actually augment (increase) the matching?"
  type: multiple-choice
  options:
    - "It must start and end at matched vertices so that flipping edges doesn't disturb the matching"
    - "It must start and end at unmatched vertices so that flipping edges increases the matching size by one"
    - "It must contain an even number of edges so that the matching remains balanced after flipping"
    - "It must pass through a vertex of maximum degree so that the flip has maximum effect"
  answer: 1
  explanation: "An augmenting path starts at an unmatched vertex in L, alternates between unmatched edges (not in M) and matched edges (in M), and ends at an unmatched vertex in R. When you flip the path — making unmatched edges matched and matched edges unmatched — the path gains one more matched edge than it loses. Both endpoints (previously unmatched) become matched. The net effect is that the matching size increases by exactly one. If the path started or ended at a matched vertex, flipping would not increase the matching size."

- question: "A perfect matching in a bipartite graph can only exist if |L| = |R|."
  type: true-false
  answer: true
  explanation: "A perfect matching covers every vertex on both sides. Since each matching edge pairs exactly one vertex from L with one from R, a perfect matching must use exactly |L| = |R| edges. If |L| ≠ |R|, the smaller side would be fully matched while the larger side would still have unmatched vertices — violating the definition of a perfect matching. Equal cardinality is necessary (though not sufficient — Hall's condition must also hold)."

- question: "Most maximum matching in a bipartite graph is also a perfect matching."
  type: true-false
  answer: false
  explanation: "A maximum matching is simply the largest possible matching — it may or may not cover all vertices. A perfect matching covers every vertex on both sides. For example, in a bipartite graph where |L| = |R| = 3 but only one worker is qualified for any job, the maximum matching has size 1, not 3. Maximum matching = as many edges as possible given the graph structure; perfect matching = complete coverage. They coincide only when the graph's structure (and Hall's condition) permits it."

- question: "Why does 'flipping' an augmenting path — switching which edges are in the matching — increase the matching size by exactly one?"
  type: short-answer
  answer: "An augmenting path has k edges and alternates: the first edge is unmatched, the second is matched, and so on. Because the path starts and ends at unmatched vertices, it must have an odd number of edges — (k+1)/2 unmatched edges and k/2 matched edges, so one more unmatched than matched. After flipping, the unmatched edges become matched and the matched edges become unmatched. The net gain is one matched edge. The two previously unmatched endpoints are now matched, and no other vertex's matching status changes."
  explanation: "The parity argument is the key. An augmenting path starts unmatched, so its edge sequence is: unmatched, matched, unmatched, matched, …, unmatched. This odd-length alternation gives exactly one more unmatched edge than matched edge. Flipping converts each unmatched edge to matched and each matched edge to unmatched — so the matching gains one edge net. The algorithm repeats until no augmenting path exists, at which point the matching is maximum (by Berge's theorem)."
```

## Explainer

Your prerequisite on bipartite graphs established that a bipartite graph has two disjoint vertex sets L and R, with all edges running between L and R (never within a side). Think of L as a set of workers and R as a set of jobs, with an edge meaning "this worker is qualified for this job." The question of interest is: how many workers can we assign to jobs simultaneously, with each worker doing at most one job and each job going to at most one worker? This is the **matching problem**.

A **matching** is a subset of edges in which no vertex appears more than once — each worker is assigned at most one job, and each job is filled by at most one worker. A **maximum matching** is the largest such set. A **perfect matching** goes further: every vertex on both sides is matched, so the assignment is total with no unmatched workers or jobs. Perfect matchings are only possible when |L| = |R| and the structure of the graph permits it. The upcoming topic Hall's Marriage Theorem gives the exact condition: a perfect matching from L into R exists if and only if for every subset S ⊆ L, the neighborhood of S (jobs reachable from S) has |N(S)| ≥ |S|. Intuitively, no group of workers can "crowd" a smaller pool of jobs.

The standard algorithm for finding a maximum matching uses **augmenting paths**. An augmenting path starts at an unmatched vertex in L, alternates between unmatched and matched edges, and ends at an unmatched vertex in R. Following such a path and flipping which edges are in the matching (matched edges become unmatched, unmatched become matched) increases the matching size by one. This process repeats until no augmenting path exists, at which point the matching is maximum. The algorithm runs in O(V·E) time.

The breadth of applications is remarkable. Bipartite matching models medical residency assignments, school scheduling (teachers to classrooms), network flow routing, and even database query optimization. Extending from matchings to weighted matchings — where each assignment has a cost and you want minimum or maximum total cost — leads to the Hungarian algorithm and the theory of **optimal transport**. The bipartite case is the cleanest entry point to a rich family of combinatorial optimization problems that appear throughout operations research and theoretical computer science.
