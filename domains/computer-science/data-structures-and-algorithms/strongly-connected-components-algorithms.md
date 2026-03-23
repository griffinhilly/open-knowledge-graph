---
id: strongly-connected-components-algorithms
title: 'Strongly Connected Components: Kosaraju and Tarjan Algorithms'
domain: computer-science
course: data-structures-and-algorithms
prerequisites:
- id: graph-depth-first-search-applications
  type: hard
- id: topological-sort
  type: soft
tags:
- scc
- kosaraju
- tarjan
- graph-algorithm
stage: formal-systems
status: validated
---

# Strongly Connected Components: Kosaraju and Tarjan Algorithms

## Core Idea
A strongly connected component (SCC) is a maximal subgraph where every vertex reaches every other vertex. Kosaraju's algorithm: DFS forward, DFS backward on transpose in reverse finish order. Tarjan's: single DFS with a stack, outputs SCCs on the fly. Both run in O(V + E).

## Questions

```yaml
- question: "In Kosaraju's algorithm, why are vertices processed in *decreasing* order of their first-pass finish times during the second DFS on the transpose graph?"
  type: multiple-choice
  options:
    - "To ensure vertices with more edges are processed first, improving cache efficiency"
    - "To guarantee each DFS tree in the second pass explores exactly one SCC, starting from a source SCC in the component DAG"
    - "To avoid revisiting vertices already assigned to an SCC during the first pass"
    - "To replicate the topological ordering of the original graph within the transpose"
  answer: 1
  explanation: "The vertex with the highest first-pass finish time belongs to a 'source' SCC in the condensed DAG — an SCC with no incoming edges from other SCCs. In the *transpose* graph, that source SCC becomes a sink (all its edges are reversed). Running DFS from this vertex in the transpose therefore cannot escape the SCC's boundaries — there are no transposed edges pointing outward. Once that SCC is identified and removed, the next highest-finish-time vertex is the source of the next SCC in the remainder. This ordering guarantees correct decomposition with no complex bookkeeping."

- question: "In Tarjan's algorithm, a vertex v is identified as the root of an SCC when its low-link value equals its own discovery index. What does this condition mean?"
  type: multiple-choice
  options:
    - "v has no outgoing edges remaining in the DFS tree"
    - "v was the very first vertex discovered in the entire DFS traversal"
    - "No vertex in v's DFS subtree can reach an ancestor above v via a back edge — the SCC is 'closed' at v"
    - "v has the maximum discovery index among all vertices currently on the stack"
  answer: 2
  explanation: "The low-link value of vertex v is the smallest discovery index reachable from v through its DFS subtree and back edges. If low[v] == disc[v], no descendant of v has a back edge to an ancestor *above* v — equivalently, the group of vertices rooted at v in the DFS tree cannot 'escape' to an earlier part of the search. This means v is the topmost vertex of a maximal set of mutually reachable vertices: an SCC. Everything on the stack from v upward forms that SCC. Options A and B don't relate to low-link semantics; D confuses discovery index with stack position."

- question: "If a directed graph has exactly one strongly connected component, then every vertex can reach every other vertex via directed paths."
  type: true-false
  answer: true
  explanation: "By definition, an SCC is a maximal set of vertices where every vertex can reach every other vertex. If the entire graph is a single SCC, then for any two vertices u and v, there are directed paths from u to v and from v to u. The 'maximal' qualifier just means no additional vertices can be added — here there are none to add. A graph with exactly one SCC is called a strongly connected graph."

- question: "Reversing all edges in a strongly connected graph produces a graph that is no longer strongly connected."
  type: true-false
  answer: false
  explanation: "The transpose (edge-reversal) of a strongly connected graph is still strongly connected. If there is a directed path u → ... → v in the original, there is a directed path v → ... → u in the transpose (traverse the reversed edges in reverse order). Since the original has directed paths in both directions between every pair of vertices, so does its transpose. This property is precisely what Kosaraju's algorithm exploits: SCCs are preserved under edge reversal, but cross-component edges change direction, turning sources into sinks."

- question: "Why does Kosaraju's algorithm use the *transpose* graph (reversed edges) in its second pass rather than running DFS on the original graph again?"
  type: short-answer
  answer: "In the original graph, a DFS from the source SCC (highest finish time) would follow edges into other SCCs, mixing multiple components in a single DFS tree. In the transpose, edges between SCCs are reversed: the former source SCC is now a sink with no outgoing cross-component edges. Therefore, DFS from that vertex in the transpose stays confined to exactly that SCC. The transpose blocks cross-component travel while preserving intra-component reachability (since SCCs are strongly connected and transpose-invariant), so each DFS tree in the second pass is exactly one SCC."
  explanation: "The two passes work together: the first encodes reachability information in finish times; the edge reversal ensures DFS cannot leak across component boundaries in the second pass. The elegance is that no special data structure is needed — just two standard DFS traversals on the original and its transpose, both O(V + E)."
```

## Explainer

From your work with DFS applications, you know that depth-first search reveals structural properties of directed graphs — back edges indicate cycles, finish times encode reachability information, and the transpose graph reverses all edges. **Strongly connected components** (SCCs) decompose a directed graph into its most tightly connected pieces: within each SCC, every vertex can reach every other vertex via directed paths. Between SCCs, the connections are one-directional — forming a DAG (directed acyclic graph) of components. This decomposition is fundamental because it reduces a complex cyclic graph to a simpler DAG structure that you can analyze with topological sort.

**Kosaraju's algorithm** uses two passes of DFS. In the first pass, run DFS on the original graph and record each vertex's finish time. Vertices that finish later in DFS tend to be in SCCs that can reach more of the graph. In the second pass, construct the **transpose graph** (reverse every edge) and run DFS again, but process vertices in decreasing order of their first-pass finish times. Each DFS tree in this second pass corresponds to exactly one SCC. The intuition: the vertex with the latest finish time belongs to a "source" SCC in the component DAG. In the transpose graph, that source becomes a sink, so DFS from it only reaches vertices within the same SCC. Once that component is removed, the next highest-finish-time vertex identifies the next SCC, and so on.

**Tarjan's algorithm** accomplishes the same decomposition in a single DFS pass using a cleverly maintained stack. Each vertex is assigned a **discovery index** (when it was first visited) and a **low-link value** (the smallest discovery index reachable from it through the DFS subtree and back edges). As DFS explores, vertices are pushed onto a stack. When DFS finishes a vertex and its low-link value equals its own discovery index, that vertex is the **root** of an SCC — pop everything from the stack down to and including that vertex, and you have the complete SCC. The low-link value propagates upward through the DFS: if a descendant can reach back to an ancestor, the ancestor's low-link is updated, and the SCC won't be popped until the true root is finished.

Both algorithms run in O(V + E) — linear in the size of the graph. Kosaraju's is often easier to understand and implement (two standard DFS passes), while Tarjan's is more elegant (single pass, no transpose construction) and can be preferred when memory or implementation simplicity matters. The SCC decomposition itself has wide applications: in a dependency graph, SCCs represent circular dependencies; in a web graph, they identify clusters of mutually linked pages; and condensing the graph to its **DAG of SCCs** enables efficient reachability queries using topological ordering.
