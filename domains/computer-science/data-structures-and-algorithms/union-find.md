---
id: union-find
title: Union-Find (Disjoint Set Union)
domain: computer-science
course: data-structures-and-algorithms
prerequisites:
- id: arrays-and-lists
  type: hard
- id: amortized-analysis
  type: soft
- id: time-space-complexity
  type: soft
- id: equivalence-relations
  type: soft
- id: depth-first-search
  type: soft
tags:
- union-find
- disjoint-sets
- DSU
- connectivity
stage: formal-systems
status: validated
---
# Union-Find (Disjoint Set Union)

## Core Idea
Union-Find (Disjoint Set Union, DSU) tracks a collection of elements partitioned into disjoint sets, supporting union (merge two sets) and find (identify a set's representative). With two optimizations — union by rank and path compression — both operations run in nearly O(1) amortized time, formally O(α(n)) where α is the inverse Ackermann function, an astronomically slowly growing function. Union-Find is used to detect cycles in undirected graphs and is the core component of Kruskal's minimum spanning tree algorithm.

## How It's Best Learned
Implement union-find with a plain parent array first, then add union by rank, then path compression. Measure how the effective tree height changes with each optimization on large inputs.

## Common Misconceptions
- Path compression restructures the tree during find operations, but this does not affect correctness — only future query speed.
- The near-O(1) amortized bound requires BOTH union by rank AND path compression; either optimization alone gives a weaker guarantee.

## Questions

```yaml
- question: "A developer implements union-find with union by rank but forgets to add path compression. What is the amortized time complexity per operation?"
  type: multiple-choice
  options:
    - "O(α(n)) — essentially constant, the same as with both optimizations"
    - "O(log n) — better than naive O(n) but worse than using both optimizations together"
    - "O(n) — linear, the same as the naive implementation without any optimization"
    - "O(1) — union by rank alone is sufficient for constant-time performance"
  answer: 1
  explanation: "Union by rank alone bounds tree height at O(log n), so find operations take O(log n) in the worst case — significantly better than naive O(n) but far from near-constant. The near-O(1) amortized bound of O(α(n)) requires *both* optimizations working together. Path compression alone also gives roughly O(log n) amortized. Only the combination of union by rank AND path compression achieves the nearly-constant O(α(n)) bound."

- question: "In Kruskal's minimum spanning tree algorithm, union-find is used to evaluate each candidate edge. What specific question does the find operation answer?"
  type: multiple-choice
  options:
    - "Whether the edge has the minimum weight among all remaining candidate edges"
    - "Whether the two endpoints of the edge are currently in the same connected component"
    - "Whether the edge forms the shortest path between its two endpoints"
    - "Whether the edge's weight exceeds the average weight of edges already added to the tree"
  answer: 1
  explanation: "Kruskal's algorithm adds edges in sorted order by weight, skipping any edge that would form a cycle. An edge creates a cycle if and only if its two endpoints are already in the same connected component — i.e., they share the same representative in the union-find structure. The find operation returns each endpoint's root; if both roots are the same, the edge is rejected. If they differ, the edge is added and the two components are merged via union."

- question: "Path compression during a find operation changes which element is the representative (root) of the set."
  type: true-false
  answer: false
  explanation: "Path compression only shortens the path from each traversed node to the root — it does not change which node is the root. Every node along the path from the queried element to the root is redirected to point directly at the root, making future finds on those nodes faster. But the root (the representative) remains unchanged. This is why path compression is safe: it restructures the internal tree for efficiency without altering the logical partition into sets."

- question: "The near-O(1) amortized time bound for union-find operations requires both path compression and union by rank; either optimization alone gives a weaker guarantee."
  type: true-false
  answer: true
  explanation: "Union by rank alone limits tree height to O(log n). Path compression alone reduces depths but can still encounter tall trees before compression kicks in. The combination achieves O(α(n)) amortized, where α is the inverse Ackermann function — effectively constant for any practical input size (α(n) ≤ 4 for n up to roughly 10^80). Applying only one of the two optimizations yields at best O(log n) amortized."

- question: "Why does path compression speed up future find operations, even though it doesn't change which element is the representative of a set?"
  type: short-answer
  answer: "When find traverses a chain of parent pointers to reach the root, path compression redirects every node along that chain to point directly at the root. On future find calls for any of those nodes, the traversal reaches the root in a single step instead of following the entire chain again. The representative (root) doesn't change — only the internal tree structure is flattened. Because future operations are dramatically shorter, the total cost of many operations is amortized to nearly O(1) per operation."
  explanation: "Path compression is a rare case of an optimization that pays for itself over time: the initial find might traverse a long chain, but it flattens that chain as it goes, making all subsequent finds on those nodes essentially free. This amortized analysis — where a costly operation makes future operations cheap — is the core reason union-find with both optimizations achieves such strong theoretical guarantees in practice."
```

## Explainer

Imagine you're at a party where people keep forming groups. Initially everyone stands alone. Periodically, two people decide their groups should merge. At any moment, someone might ask: "Are Alice and Bob in the same group?" **Union-Find** is the data structure that answers this question efficiently, even as groups keep merging — and it does so in nearly constant time per operation.

The core representation is surprisingly simple: an array `parent[]` where `parent[i]` points to i's parent in a tree. Each group forms a tree, and the root of that tree is the group's **representative**. To find which group an element belongs to, you follow parent pointers until you reach a root (an element that is its own parent). To merge two groups, you find their roots and make one point to the other. This is where your knowledge of arrays comes in — the entire structure is just an integer array, with indices representing elements and values representing parent links.

The naive version has a problem: trees can become long chains. If you always attach the second root under the first, a sequence of unions can produce a tree of depth n, making find operations O(n). **Union by rank** fixes this by always attaching the shorter tree under the taller one, keeping tree heights logarithmic. But the real magic is **path compression**: every time you call find and walk up to the root, you redirect every node along the path to point directly at the root. Future finds on those nodes become O(1). The combination of both optimizations yields an amortized cost of O(α(n)) per operation, where α is the **inverse Ackermann function** — a function that grows so slowly it's effectively constant for any input size you'll ever encounter (α(n) ≤ 4 for n up to roughly 10^80).

Union-Find's most important application is in graph algorithms. To detect whether adding an edge creates a **cycle** in an undirected graph, check whether the two endpoints are already in the same set — if they are, connecting them would form a cycle. This is exactly what **Kruskal's algorithm** does when building a minimum spanning tree: sort edges by weight, then greedily add each edge unless it would create a cycle (i.e., unless find returns the same representative for both endpoints). With Union-Find powering the cycle check, Kruskal's runs in O(E log E) time, dominated by the initial sort. The Union-Find operations themselves contribute essentially O(E) total work — nearly free.
