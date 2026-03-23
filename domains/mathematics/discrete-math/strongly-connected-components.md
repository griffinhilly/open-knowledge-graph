---
id: strongly-connected-components
title: Strongly Connected Components
domain: mathematics
course: discrete-math
prerequisites:
- id: directed-graphs-and-digraphs
  type: hard
- id: graph-connectivity
  type: hard
builds-toward:
- topological-sorting
- condensation-digraph
tags:
- directed-graphs
- connectivity
- components
stage: formal-systems
status: validated
---

# Strongly Connected Components

## Core Idea
A strongly connected component (SCC) is a maximal subset of vertices where every vertex is reachable from every other vertex following directed edges. Partitioning a digraph into SCCs reveals its underlying structure and identifies cycles.

## Questions

```yaml
- question: "Vertex v in a digraph has no outgoing edges and no self-loop. What is v's strongly connected component?"
  type: multiple-choice
  options:
    - "v is part of the SCC containing all vertices that can reach v"
    - "v forms a trivial SCC containing only itself"
    - "v cannot be part of any SCC because it has no outgoing edges"
    - "v belongs to whichever SCC has a vertex with an edge pointing to v"
  answer: 1
  explanation: "Every vertex belongs to exactly one SCC — even if it cannot reach any other vertex. Since v has no outgoing edges, no other vertex is reachable from v. The only vertex reachable from v is v itself (trivially, via a path of length 0). So the largest subset with mutual reachability involving v is just {v}. Trivial SCCs of size 1 are common in digraphs, especially for source-like or sink-like vertices."

- question: "Why is the condensation digraph (the DAG formed by collapsing each SCC to a node) always acyclic?"
  type: multiple-choice
  options:
    - "Because DFS on the reversed graph processes SCCs in topological order"
    - "Because the original digraph has no cycles, only directed paths"
    - "Because if two SCCs had a cycle between them, all their vertices would mutually reach each other, making them one SCC — contradicting maximality"
    - "Because each SCC has a unique finish time in Kosaraju's algorithm"
  answer: 2
  explanation: "This is the key structural reason. Suppose two distinct SCCs, C₁ and C₂, had edges C₁→C₂ and C₂→C₁ in the condensation. Then every vertex in C₁ could reach every vertex in C₂ (via the inter-SCC edges) and vice versa. That means all vertices of C₁ ∪ C₂ mutually reach each other — so they would form a single SCC, contradicting the assumption that C₁ and C₂ are distinct. Therefore no cycles can exist in the condensation."

- question: "In a strongly connected digraph, every pair of vertices can reach each other via directed paths."
  type: true-false
  answer: true
  explanation: "By definition, a strongly connected graph is one where the entire vertex set forms a single SCC — i.e., every vertex is reachable from every other vertex following directed edges. This is the meaning of 'strongly connected': mutual reachability holds globally. (Compare to 'weakly connected,' which only requires connectivity when edge directions are ignored.)"

- question: "If vertices u and v are in the same strongly connected component, there must be a direct edge from u to v and from v to u."
  type: true-false
  answer: false
  explanation: "SCCs require mutual reachability via directed *paths*, not direct edges. u and v can be in the same SCC if there is a directed path u → w₁ → w₂ → v and a separate path v → x₁ → u, even if no direct u↔v edges exist. Requiring direct edges would be a much stricter condition (essentially requiring a tournament-style structure), and most real SCCs involve multi-hop paths."

- question: "Explain why the condensation of a digraph is always a DAG, and why this property is useful."
  type: short-answer
  answer: "The condensation is a DAG because any cycle in the condensation would imply that two or more SCCs are mutually reachable, which would mean they should be merged into a single larger SCC — contradicting the maximality requirement. The DAG property is useful because DAGs support topological sorting, allowing you to determine a valid ordering of tasks or dependencies. It also reveals the large-scale causal or flow structure of the original digraph: which components influence others, and whether feedback is possible."
  explanation: "The condensation transforms a complex digraph with cycles into a hierarchy. Once cycles are identified and contracted, what remains is a pure flow structure with no mutual dependencies — every edge in the condensation points 'forward' in some topological sense. This is why SCC decomposition is the first step in many graph algorithms, including those that compute reachability, scheduling order, or influence propagation."
```

## Explainer

From your prerequisite on directed graphs, you know that a digraph's edges have direction — getting from A to B doesn't mean you can get from B to A. This asymmetry creates a richer notion of connectivity than in undirected graphs. A **strongly connected component** (SCC) is a maximal group of vertices where mutual reachability holds: from any vertex in the group, you can follow directed edges to reach every other vertex in the group. "Maximal" means you can't add any more vertices to the group while preserving this mutual reachability.

Think of a social network where edges represent "can directly contact." An SCC is a clique of mutual accessibility — a set of people who can all communicate with each other along the directed links. Vertices outside each other's SCCs have one-way or no reachability. A digraph always decomposes into SCCs, and this decomposition is unique: every vertex belongs to exactly one SCC (even if it's a trivial SCC of size 1, a vertex that can't reach itself).

The two classic algorithms — **Kosaraju's** and **Tarjan's** — both run in O(V+E) time using depth-first search from your graph connectivity background. Kosaraju's is conceptually clean: run DFS on the original graph, recording finish times; then run DFS on the *reversed* graph in decreasing finish-time order. Each DFS tree in the second pass is exactly one SCC. The key insight is that reversing all edges swaps "reachable from" with "can reach" — so the two passes together identify exactly the mutual-reachability clusters.

Once you've found all SCCs, you can build the **condensation digraph**: collapse each SCC to a single super-vertex and keep the inter-SCC edges. The condensation is always a DAG (directed acyclic graph) — if it had a cycle, those SCCs would merge into one larger SCC, contradicting maximality. This DAG view is powerful: it reveals the large-scale flow structure of the original graph, which is the first step toward topological sorting and understanding which parts of a system can influence other parts without possibility of feedback.
