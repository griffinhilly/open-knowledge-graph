---
id: bipartite-graphs
title: Bipartite Graphs and Matchings
domain: mathematics
course: discrete-math
prerequisites:
- id: graph-connectivity
  type: hard
- id: graph-theory-intro
  type: hard
tags:
- bipartite
- matching
- graph-theory
- two-colorable
- hall-theorem
stage: formal-systems
status: validated
---

# Bipartite Graphs and Matchings

## Core Idea
A bipartite graph has its vertices divided into two disjoint sets U and V such that every edge connects a vertex in U to one in V — no edges exist within either set. A graph is bipartite if and only if it contains no odd-length cycle. A matching is a set of edges with no shared vertices; a perfect matching saturates every vertex. Hall's marriage theorem gives a necessary and sufficient condition for a perfect matching to exist: for every subset S of U, the neighborhood N(S) satisfies |N(S)| ≥ |S|.

## How It's Best Learned
Check bipartiteness by 2-coloring: alternate colors while traversing the graph. If you must assign the same color to two adjacent vertices, the graph has an odd cycle and is not bipartite. Model Hall's theorem with practical assignment problems (students to internships) before examining its proof.

## Common Misconceptions
- Thinking any graph without an odd cycle must be a tree — bipartite graphs can have many even cycles.
- Confusing a matching with a path or Hamiltonian circuit — matchings are a set of disjoint edges, not a traversal.

## Explainer

A **bipartite graph** splits its vertices into two groups — call them Left and Right — where every edge crosses between the groups. No edge stays within Left, and no edge stays within Right. A classic example is a job-assignment problem: Left is a set of workers, Right is a set of jobs, and an edge means "this worker can do this job." The two-group structure is exactly the right model whenever you have a relationship between two distinct types of objects.

The bipartite test — 2-coloring — follows directly from what you know about graph connectivity. Start at any vertex and color it red. Color all its neighbors blue. Color their unvisited neighbors red again, alternating as you traverse. If you ever need to assign the same color to two adjacent vertices, you have found an odd-length cycle, and the graph is not bipartite. If you complete the traversal with no conflict, the coloring itself certifies bipartiteness. Bipartite graphs can only contain even-length cycles: a path from Left to Right and back must take an even number of steps.

A **matching** is a set of edges that share no endpoints — each vertex is "used" at most once. Think of assigning workers to jobs with no worker doing two jobs and no job having two workers. A **perfect matching** covers every vertex. The critical question is: when does a perfect matching exist? This is where **Hall's theorem** answers precisely. For the Left side to be fully matched into Right, every subset S of Left vertices must collectively "see" at least |S| Right neighbors. Intuitively, you cannot match 3 workers if they all compete for only 2 jobs. Hall's condition says this congestion problem is the *only* obstruction — if no such bottleneck exists, a perfect matching is guaranteed.

To use Hall's theorem in practice, you check the neighborhood condition for all subsets of Left. This sounds expensive, but in proofs and small examples it reveals exactly where a matching fails: find the subset S where |N(S)| < |S|, and you have found the bottleneck. Algorithms like augmenting paths find maximum matchings efficiently by finding paths that can extend the current matching — each augmenting path increases the matching size by one. The structure of bipartite graphs (no odd cycles) is precisely what makes augmenting-path algorithms clean and correct here.
