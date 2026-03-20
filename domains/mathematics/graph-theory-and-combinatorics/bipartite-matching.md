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
stage: formal-systems
status: draft
---

# Matchings in Bipartite Graphs

## Core Idea
A matching is a set of edges with no shared vertices; in bipartite graphs, matchings model assignments between two sets. A maximum matching uses the most edges; a perfect matching covers all vertices. Bipartite matching is fundamental to applications like job assignment, resource allocation, and network optimization.

## Explainer

Your prerequisite on bipartite graphs established that a bipartite graph has two disjoint vertex sets L and R, with all edges running between L and R (never within a side). Think of L as a set of workers and R as a set of jobs, with an edge meaning "this worker is qualified for this job." The question of interest is: how many workers can we assign to jobs simultaneously, with each worker doing at most one job and each job going to at most one worker? This is the **matching problem**.

A **matching** is a subset of edges in which no vertex appears more than once — each worker is assigned at most one job, and each job is filled by at most one worker. A **maximum matching** is the largest such set. A **perfect matching** goes further: every vertex on both sides is matched, so the assignment is total with no unmatched workers or jobs. Perfect matchings are only possible when |L| = |R| and the structure of the graph permits it. The upcoming topic Hall's Marriage Theorem gives the exact condition: a perfect matching from L into R exists if and only if for every subset S ⊆ L, the neighborhood of S (jobs reachable from S) has |N(S)| ≥ |S|. Intuitively, no group of workers can "crowd" a smaller pool of jobs.

The standard algorithm for finding a maximum matching uses **augmenting paths**. An augmenting path starts at an unmatched vertex in L, alternates between unmatched and matched edges, and ends at an unmatched vertex in R. Following such a path and flipping which edges are in the matching (matched edges become unmatched, unmatched become matched) increases the matching size by one. This process repeats until no augmenting path exists, at which point the matching is maximum. The algorithm runs in O(V·E) time.

The breadth of applications is remarkable. Bipartite matching models medical residency assignments, school scheduling (teachers to classrooms), network flow routing, and even database query optimization. Extending from matchings to weighted matchings — where each assignment has a cost and you want minimum or maximum total cost — leads to the Hungarian algorithm and the theory of **optimal transport**. The bipartite case is the cleanest entry point to a rich family of combinatorial optimization problems that appear throughout operations research and theoretical computer science.
