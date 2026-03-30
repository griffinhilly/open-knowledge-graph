---
id: advanced-network-flow
title: Advanced Network Flow Algorithms
domain: computer-science
course: advanced-algorithms
prerequisites:
- id: maximum-flow-network-algorithms
  type: hard
- id: linear-programming-algorithms
  type: hard
- id: breadth-first-search
  type: soft
tags:
- network-flow
- max-flow-min-cut
- push-relabel
- min-cost-flow
stage: expert
status: validated
---

# Advanced Network Flow Algorithms

## Core Idea
Network flow algorithms extend beyond basic Ford-Fulkerson to achieve faster runtimes and solve richer problems. The push-relabel algorithm (Goldberg-Tarjan) achieves O(V^2 * E) time for max-flow by maintaining a preflow (allowing excess at vertices) and using height labels to guide flow toward the sink — avoiding the repeated BFS of augmenting-path methods. Dinic's algorithm achieves O(V^2 * E) using blocking flows in layered graphs, with O(E * sqrt(V)) for unit-capacity networks. Minimum-cost flow generalizes max-flow by adding edge costs and finding the cheapest way to route a given flow value, solvable via successive shortest paths or cost-scaling in O(V * E * log V * log(VC)). These algorithms reduce to LP but exploit network structure for dramatically faster specialized solutions. Applications span bipartite matching, project selection, image segmentation, and airline scheduling.

## Questions

```yaml
- question: "The push-relabel algorithm maintains a 'preflow' where flow into a vertex can exceed flow out (creating excess). Why is this approach faster than augmenting-path methods like Edmonds-Karp?"
  type: multiple-choice
  options:
    - "Preflows require fewer total operations than augmenting paths"
    - "Push-relabel operates locally — each push or relabel operation modifies a single vertex's excess or label in O(1) time, avoiding the global BFS that augmenting-path methods require for each augmentation. The total work across all operations is bounded by O(V^2 * E) through amortized analysis of relabel operations"
    - "Push-relabel uses less memory than augmenting-path methods"
    - "Preflows are always closer to the maximum flow than partial flows"
  answer: 1
  explanation: "Augmenting-path methods like Edmonds-Karp perform O(VE) augmentations, each requiring a BFS costing O(E), for O(VE^2) total. Push-relabel avoids global BFS entirely: it processes vertices with excess flow locally, pushing flow along edges to neighbors or relabeling (raising height) when no downhill push is possible. The height labels (a potential function) ensure progress: the total number of relabels is O(V^2), each non-saturating push decreases the total potential, and saturating pushes are bounded by O(VE). The resulting O(V^2 E) bound improves on Edmonds-Karp's O(VE^2) for dense graphs."

- question: "Dinic's algorithm on unit-capacity networks runs in O(E * sqrt(V)) time, which is optimal for maximum bipartite matching. Why does unit capacity improve the runtime from O(V^2 E)?"
  type: short-answer
  answer: "In unit-capacity networks, each augmenting path carries exactly 1 unit of flow and saturates at least one edge. After sqrt(V) phases of blocking flow (each computed in O(E) time on the layered graph), the maximum flow value increases by at most sqrt(V) more units — because the remaining augmenting paths have length > sqrt(V) and are therefore few in number (at most sqrt(V), since the paths are edge-disjoint in a unit graph). So the total number of phases is O(sqrt(V)), each costing O(E), giving O(E * sqrt(V)) total. For bipartite matching (a unit-capacity flow problem), this gives the Hopcroft-Karp bound of O(E * sqrt(V))."
  explanation: "The argument is subtle: after sqrt(V) phases, remaining augmenting paths are long (> sqrt(V) edges), and in a unit-capacity network, long edge-disjoint paths are scarce. This structural argument about path lengths is what gives the sqrt(V) bound on the number of additional flow units needed."

- question: "Every maximum flow problem can be formulated and solved as a linear program, but specialized flow algorithms are preferred because they exploit network structure for faster running times."
  type: true-false
  answer: true
  explanation: "The max-flow LP has variables for flow on each edge, constraints for capacity and conservation, and maximizes total flow out of the source. A general LP solver runs in O(n^3.5 L) time (interior point) where n includes all edges and vertices. But flow algorithms exploit the total unimodularity of the constraint matrix (guaranteeing integer optimal solutions) and the network structure (BFS, layered graphs, height functions) to achieve O(V^2 E) or better. For a graph with millions of edges, the specialized algorithms are orders of magnitude faster. However, the LP formulation is valuable for theoretical analysis — LP duality directly yields the max-flow min-cut theorem."

- question: "The max-flow min-cut theorem states that the maximum flow value equals the minimum cut capacity. This is a consequence of LP strong duality applied to the flow LP."
  type: true-false
  answer: true
  explanation: "The max-flow LP has a dual that is exactly the min-cut LP (with variables on edges indicating whether they cross the cut, and constraints ensuring a valid s-t cut). LP strong duality guarantees that the optimal primal (max-flow) and dual (min-cut) values are equal. This gives a clean proof of the max-flow min-cut theorem and illustrates how LP duality produces combinatorial results. The total unimodularity of the flow constraint matrix further guarantees that the LP has an integer optimal solution, meaning the continuous LP directly yields the combinatorial max-flow."
```

## Explainer

You already understand the Ford-Fulkerson framework: find augmenting paths from source to sink, push flow along them, repeat until no augmenting path exists. The advanced algorithms you encounter here improve the runtime by orders of magnitude through deeper structural insights — preflow techniques, layered graph decompositions, and potential function arguments.

Dinic's algorithm introduces the concept of blocking flows on layered graphs. First, BFS from the source constructs a layered graph where each edge goes from layer i to layer i+1 (these are the shortest-path layers). A blocking flow saturates at least one edge on every source-to-sink path in this layered graph, and can be found in O(VE) time. After each blocking flow, the shortest augmenting path length increases by at least 1, so at most V-1 phases suffice. The total work is O(V^2 E). On unit-capacity networks, each phase costs only O(E) and the argument about path lengths after sqrt(V) phases reduces the total to O(E sqrt(V)) — this is the Hopcroft-Karp algorithm for bipartite matching.

The push-relabel algorithm (Goldberg and Tarjan, 1988) takes a radically different approach. Instead of finding global augmenting paths, it maintains a preflow — flow that may violate conservation by having excess at non-source/sink vertices — and works locally. Each vertex has a height label; flow is pushed "downhill" (from higher to lower labels). When a vertex has excess but no downhill neighbors, its label is raised (relabeled). The key insight is that the height labels form a valid distance estimate to the sink in the residual graph, so the algorithm implicitly routes excess flow toward the sink. The amortized analysis bounds the total work at O(V^2 E), with practical implementations using FIFO or highest-label selection achieving much better empirical performance.

Minimum-cost flow extends the framework by assigning costs to edges and finding the cheapest flow of a given value. The successive shortest paths algorithm repeatedly finds shortest (minimum cost) augmenting paths using Bellman-Ford or Dijkstra with Johnson's reweighting. Cost-scaling algorithms achieve O(V E log V log(VC)) by iteratively refining approximate complementary slackness conditions. Applications include transportation problems, assignment problems, and any optimization where both capacity and cost constraints matter. The LP dual of minimum-cost flow yields the economic interpretation: dual variables are node potentials (prices), and complementary slackness means flow only uses edges where the reduced cost (cost minus potential difference) is optimal.
