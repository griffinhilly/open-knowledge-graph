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

## Questions

```yaml
- question: "During 2-coloring to check bipartiteness, you find you must assign the same color to two adjacent vertices. What does this prove?"
  type: multiple-choice
  options:
    - "The graph has a cycle of even length, which disqualifies it from being bipartite"
    - "The graph contains an odd-length cycle and is therefore not bipartite"
    - "The graph is disconnected, so the 2-coloring algorithm does not apply"
    - "You chose the wrong starting color — restart with the opposite color assignment"
  answer: 1
  explanation: "The 2-coloring algorithm alternates colors as it traverses the graph. A conflict — needing to assign the same color to adjacent vertices — means you have traced a path that returns to a previously colored vertex with the wrong parity. That path forms an odd-length cycle. A graph is bipartite if and only if it contains no odd-length cycle, so a conflict proves non-bipartiteness. Restarting with a different color will not help — the odd cycle is a structural property of the graph."

- question: "In a bipartite job-assignment graph, 3 workers (w₁, w₂, w₃) are all connected exclusively to the same 2 jobs. According to Hall's theorem, what can you conclude?"
  type: multiple-choice
  options:
    - "A perfect matching might still exist if the other workers have enough options"
    - "No perfect matching exists, because Hall's condition is violated: |N({w₁, w₂, w₃})| = 2 < 3"
    - "A maximum matching can still include all 3 workers if the 2 jobs are assigned carefully"
    - "Hall's theorem does not apply here because the graph is not connected"
  answer: 1
  explanation: "Hall's condition requires that for every subset S of the Left vertices, |N(S)| ≥ |S|. The subset {w₁, w₂, w₃} has only 2 neighbors, so |N(S)| = 2 < 3 = |S|. Hall's theorem says this bottleneck is both necessary and sufficient to determine that no perfect matching exists — you cannot match 3 workers to only 2 distinct jobs with no sharing."

- question: "A bipartite graph can contain cycles, as long as every cycle in it has even length."
  type: true-false
  answer: true
  explanation: "Bipartiteness and the absence of cycles are not the same thing. The bipartite condition bans only odd-length cycles — a path that goes from Left to Right and back must take an even number of steps. Even-length cycles are perfectly compatible with the two-partition structure. Bipartite graphs are frequently cycle-rich; thinking them must be trees is a common misconception."

- question: "If most vertex on the Left side of a bipartite graph is connected to at least one vertex on the Right side, a perfect matching is very likely to exist."
  type: true-false
  answer: false
  explanation: "Hall's condition requires that for *every subset* S of Left, the neighborhood N(S) is at least as large as S — not just that each individual vertex has a neighbor. Three workers all connected only to the same one job each have at least one neighbor, but no perfect matching is possible. Individual connectivity is necessary but nowhere near sufficient."

- question: "Explain what Hall's marriage theorem says, and describe the 'bottleneck' it identifies as the sole obstruction to a perfect matching."
  type: short-answer
  answer: "Hall's theorem states that a bipartite graph has a perfect matching (from Left into Right) if and only if for every subset S of Left vertices, the neighborhood N(S) has at least |S| vertices. The bottleneck is a subset S where |N(S)| < |S| — more vertices in S than they collectively see in the Right. If any such bottleneck exists, no perfect matching is possible; if none exists, a perfect matching is guaranteed."
  explanation: "The 'only if' direction is easy: you cannot match |S| vertices to fewer than |S| distinct neighbors. The 'if' direction (no bottleneck → matching exists) is the substantive content, proved constructively using augmenting paths. Hall's theorem is powerful because it converts a global question (does a perfect matching exist?) into a family of local neighborhood checks."
```

## Explainer

A **bipartite graph** splits its vertices into two groups — call them Left and Right — where every edge crosses between the groups. No edge stays within Left, and no edge stays within Right. A classic example is a job-assignment problem: Left is a set of workers, Right is a set of jobs, and an edge means "this worker can do this job." The two-group structure is exactly the right model whenever you have a relationship between two distinct types of objects.

The bipartite test — 2-coloring — follows directly from what you know about graph connectivity. Start at any vertex and color it red. Color all its neighbors blue. Color their unvisited neighbors red again, alternating as you traverse. If you ever need to assign the same color to two adjacent vertices, you have found an odd-length cycle, and the graph is not bipartite. If you complete the traversal with no conflict, the coloring itself certifies bipartiteness. Bipartite graphs can only contain even-length cycles: a path from Left to Right and back must take an even number of steps.

A **matching** is a set of edges that share no endpoints — each vertex is "used" at most once. Think of assigning workers to jobs with no worker doing two jobs and no job having two workers. A **perfect matching** covers every vertex. The critical question is: when does a perfect matching exist? This is where **Hall's theorem** answers precisely. For the Left side to be fully matched into Right, every subset S of Left vertices must collectively "see" at least |S| Right neighbors. Intuitively, you cannot match 3 workers if they all compete for only 2 jobs. Hall's condition says this congestion problem is the *only* obstruction — if no such bottleneck exists, a perfect matching is guaranteed.

To use Hall's theorem in practice, you check the neighborhood condition for all subsets of Left. This sounds expensive, but in proofs and small examples it reveals exactly where a matching fails: find the subset S where |N(S)| < |S|, and you have found the bottleneck. Algorithms like augmenting paths find maximum matchings efficiently by finding paths that can extend the current matching — each augmenting path increases the matching size by one. The structure of bipartite graphs (no odd cycles) is precisely what makes augmenting-path algorithms clean and correct here.
