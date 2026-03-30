---
id: matroid-intersection
title: Matroid Intersection
domain: computer-science
course: advanced-algorithms
prerequisites:
- id: greedy-algorithms
  type: hard
- id: advanced-network-flow
  type: hard
- id: linear-programming-algorithms
  type: soft
tags:
- matroids
- matroid-intersection
- combinatorial-optimization
- polyhedral-combinatorics
stage: expert
status: validated
---

# Matroid Intersection

## Core Idea
A matroid is a combinatorial structure that captures the notion of "independence" — generalizing linear independence in vector spaces and acyclicity in graphs. The matroid intersection problem asks: given two matroids on the same ground set, find a maximum-weight common independent set. This elegant framework unifies many classical optimization problems: bipartite matching is the intersection of two partition matroids; colorful spanning forests arise from graphic and partition matroid intersection. While a single matroid's optimization is solved by greedy (this is essentially what defines matroids), intersecting two matroids requires augmenting-path techniques analogous to network flow. The matroid intersection theorem states that the maximum common independent set size equals the minimum of a certain dual quantity, yielding a min-max theorem generalizing König's theorem.

## Questions

```yaml
- question: "The greedy algorithm finds a maximum-weight independent set in any single matroid. Why does greedy fail for matroid intersection, and what technique replaces it?"
  type: multiple-choice
  options:
    - "Greedy fails because matroid intersection is NP-hard"
    - "Greedy optimizes for one matroid but may violate independence in the other. Matroid intersection uses an augmenting-path algorithm on an exchange graph: vertices are ground set elements, edges represent exchange pairs where adding one element and removing another maintains independence in both matroids, and augmenting paths increase the common independent set size"
    - "Greedy fails because matroid intersection requires dynamic programming"
    - "Greedy works for matroid intersection if you alternate between the two matroids"
  answer: 1
  explanation: "A greedy element that is optimal for matroid M1 may not be independent in M2. The exchange graph captures the structure of feasible swaps: for current common independent set I, element y not in I, and element x in I, there is a directed edge from y to x if (I - x + y) is independent in M1, and from x to y if (I - x + y) is independent in M2. An augmenting path from a free element (addable to M1's span) to another free element (addable to M2's span) yields a symmetric difference that increases |I| by 1. This is the matroid analog of augmenting paths in bipartite matching."

- question: "Bipartite matching can be formulated as the intersection of two partition matroids. This means the Hopcroft-Karp algorithm is a special case of matroid intersection."
  type: true-false
  answer: true
  explanation: "Given a bipartite graph with parts L and R, define matroid M1 on the edges: a set of edges is independent if no two share an L-vertex (partition matroid on L-partition). Define M2 similarly for R-vertices. A common independent set is a set of edges sharing no endpoints on either side — a matching. Maximum matroid intersection finds a maximum matching. The augmenting-path structure of matroid intersection, specialized to partition matroids, recovers exactly the augmenting-path algorithm for bipartite matching. This reveals matching as a special case of a deeper combinatorial structure."

- question: "Explain the matroid intersection min-max theorem and its relationship to König's theorem for bipartite graphs."
  type: short-answer
  answer: "The matroid intersection theorem (Edmonds) states: the maximum size of a common independent set of matroids M1, M2 on ground set E equals min over all subsets A of E of (rank_M1(A) + rank_M2(E\\A)). This says you can 'certify' the optimality of a common independent set by finding a partition of the ground set where the sum of ranks is minimized. For bipartite matching (partition matroids), this specializes to König's theorem: max matching = min vertex cover. The A-partition corresponds to choosing which side's vertices are in the cover, and rank_M1(A) + rank_M2(E\\A) counts the cover size. The matroid min-max theorem thus generalizes König's theorem from bipartite graphs to arbitrary matroid pairs."
  explanation: "This min-max theorem is a cornerstone of combinatorial optimization. It demonstrates that matroid intersection, despite being more general than bipartite matching, retains the beautiful duality property where the primal optimum equals the dual optimum — a property that fails for general 3-dimensional matching (which is NP-hard)."

- question: "The intersection of THREE or more matroids can always be optimized in polynomial time, just like two-matroid intersection."
  type: true-false
  answer: false
  explanation: "3-matroid intersection is NP-hard. This is proved by reducing Hamiltonian path to the intersection of three matroids: a graphic matroid (independent sets are forests), a partition matroid (each vertex has at most one outgoing edge), and another partition matroid (each vertex has at most one incoming edge). Their intersection is a set of edges forming a Hamiltonian path. The jump from 2 to 3 is a sharp complexity boundary — two-matroid intersection is polynomial (augmenting paths), three-matroid intersection is NP-hard. This is one of the cleanest examples of a phase transition in combinatorial optimization complexity."
```

## Explainer

Matroids are the combinatorial structures that make the greedy algorithm work. Formally, a matroid is a pair (E, I) where E is a ground set and I is a collection of "independent" subsets satisfying three axioms: the empty set is independent, subsets of independent sets are independent (hereditary property), and if one independent set is larger than another, some element of the larger set can be added to the smaller (exchange property). The exchange property is what guarantees the greedy algorithm — always add the heaviest available element that maintains independence — finds a maximum-weight independent set.

Examples ground the abstraction. In a graphic matroid, E is the edge set of a graph and independent sets are acyclic subsets (forests). The greedy algorithm on a graphic matroid is Kruskal's MST algorithm. In a partition matroid, E is partitioned into groups and an independent set contains at most one element from each group. In a linear matroid, E is a set of vectors and independent sets are linearly independent subsets. Each captures a different flavor of "independence," but all satisfy the same axioms and all respond to greedy.

Matroid intersection asks for the largest (or heaviest) set that is independent in two matroids simultaneously. This is strictly harder than single-matroid optimization but still polynomial. The algorithm builds an exchange graph: nodes are ground set elements, and directed edges represent swaps that maintain independence in one matroid or the other. Augmenting paths in this exchange graph (from an element addable in M1 to one addable in M2) yield improved common independent sets via symmetric differences. This is the matroid generalization of augmenting-path algorithms for bipartite matching, and the connection is exact: bipartite matching equals partition-matroid intersection.

The matroid intersection theorem provides the min-max dual: max |common independent set| = min_{A subset E} (r_1(A) + r_2(E\A)), where r_1, r_2 are the rank functions. This generalizes König's theorem and provides optimality certificates. The polynomial tractability of 2-matroid intersection versus the NP-hardness of 3-matroid intersection is a fundamental boundary in combinatorial optimization — it shows that the structure of two matroids interacting is rich enough to capture bipartite matching, spanning trees, and arborescences, but adding a third matroid pushes into NP-hard territory (capturing Hamiltonian paths).
