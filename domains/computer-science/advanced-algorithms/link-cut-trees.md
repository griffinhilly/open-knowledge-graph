---
id: link-cut-trees
title: Link-Cut Trees
domain: computer-science
course: advanced-algorithms
prerequisites:
- id: binary-search-trees
  type: hard
- id: amortized-analysis
  type: hard
- id: maximum-flow-network-algorithms
  type: soft
- id: red-black-trees
  type: soft
tags:
- link-cut-trees
- splay-trees
- dynamic-trees
- sleator-tarjan
- path-decomposition
- dynamic-connectivity
stage: expert
status: validated
---

# Link-Cut Trees

## Core Idea
Link-cut trees, introduced by Sleator and Tarjan (1983), maintain a forest of rooted trees under link (add an edge), cut (remove an edge), and path queries (find minimum/aggregate on root-to-node path), all in O(log n) amortized time. The data structure represents each tree as a collection of preferred paths (heavy paths chosen dynamically based on access patterns), each stored as a splay tree keyed by depth. The access operation splays a node to the root of its auxiliary tree and restructures preferred paths, making it the foundation for all other operations. Link-cut trees achieve O(m log n) total time for max-flow algorithms (by maintaining the residual tree structure) and are essential for dynamic graph algorithms, making them one of the most powerful data structures in advanced algorithm design.

## Questions

```yaml
- question: "What is the role of splay trees within the link-cut tree data structure?"
  type: multiple-choice
  options:
    - "Each node in the represented forest is stored in a single global splay tree"
    - "Each preferred path in the represented forest is stored as a splay tree, keyed by depth, so that path operations (find root, aggregate, update) can be performed in O(log n) amortized time by splaying and traversing the auxiliary tree"
    - "Splay trees are used only for balancing the forest, not for query operations"
    - "Each child pointer in the represented forest is replaced by a splay tree of that child's subtree"
  answer: 1
  explanation: "Link-cut trees decompose each represented tree into preferred paths — contiguous root-to-leaf chains selected based on the most recent access. Each preferred path is stored in an auxiliary splay tree where the key is the node's depth in the represented tree (so an in-order traversal of the splay tree gives the path from shallowest to deepest). Splay trees provide O(log n) amortized operations (splay, split, join) which directly translate to O(log n) amortized link-cut tree operations. The self-adjusting property of splay trees is essential: frequently accessed paths naturally rise to the top of their auxiliary trees, giving good amortized performance without explicit balancing."

- question: "The access(v) operation in a link-cut tree makes v the root of its auxiliary splay tree and makes the path from v to the root of its represented tree the preferred path. This operation runs in O(n) worst-case time but O(log n) amortized time."
  type: true-false
  answer: true
  explanation: "Access(v) works by: (1) splaying v within its current auxiliary tree, (2) detaching the right child of v in the auxiliary tree (cutting the preferred path below v), (3) following the path-parent pointer to the next auxiliary tree, splaying the node there, joining v's tree as the right child, and repeating until reaching the root. Each step involves a splay and a join. The worst case of a single access is O(n) — if v is at the bottom of a long non-preferred path, every step changes a preferred child. But the amortized analysis (using the same potential function as splay trees, Phi = sum log(size of subtree)) shows the amortized cost is O(log n) per access, and all other operations (link, cut, find-root) are implemented using O(1) accesses plus O(1) additional work."

- question: "Explain how link-cut trees improve the running time of maximum flow algorithms."
  type: short-answer
  answer: "In augmenting-path max-flow algorithms (e.g., Dinic's blocking flow), each augmentation finds a path from source to sink and pushes flow along it, updating residual capacities. Without link-cut trees, finding and updating a path takes O(n) time. With link-cut trees maintaining the current tree of edges being used, the operations become: (1) find the bottleneck edge on the source-to-sink path (path minimum query, O(log n)), (2) update all edge capacities on the path (path update, O(log n)), (3) remove saturated edges and add new edges (cut and link, O(log n) each). This reduces the per-path cost from O(n) to O(log n). For Dinic's algorithm with O(n^2) blocking flow phases and O(m) paths total, link-cut trees yield O(mn log n) total time, versus O(mn^2) without them. For unit-capacity graphs, this gives O(m * sqrt(n) * log n)."
  explanation: "The key insight is that link-cut trees turn path operations (find min, update all edges, delete saturated edge) into O(log n) operations by maintaining the augmenting tree dynamically. Each augmentation corresponds to an access, a path-minimum query, a path-update, and one or more cuts — all O(log n) amortized."

- question: "Link-cut trees support make-tree, link, and cut operations. Which of the following correctly describes the link operation?"
  type: multiple-choice
  options:
    - "Link(u, v) makes u a child of v in the represented forest, requiring that u is currently a root of its tree and u and v are in different trees"
    - "Link(u, v) merges the splay trees of u and v without changing the represented forest"
    - "Link(u, v) swaps the subtrees of u and v"
    - "Link(u, v) makes v a child of u regardless of whether v is a root"
  answer: 0
  explanation: "Link(u, v) adds the edge (u, v) to the represented forest, making u (which must be a root of its represented tree) a child of v. The implementation: access(u) to make u the root of its auxiliary tree (it has no left child since it's the shallowest node on its preferred path after access), then set u's path-parent pointer to v. The preconditions — u must be a root and u, v must be in different trees — ensure the result is still a forest. Cut(u) removes the edge between u and its parent: access(u), then detach u's left child in the auxiliary tree (which represents the path above u)."

- question: "Link-cut trees can be used to maintain a dynamic forest under edge insertions and deletions. They cannot answer lowest-common-ancestor (LCA) queries."
  type: true-false
  answer: false
  explanation: "Link-cut trees support LCA queries in O(log n) amortized time. To find LCA(u, v): first access(u), which makes the path from u to the root preferred. Then access(v) — as this access walks up from v toward the root, the last node where it crosses from one auxiliary tree to another (the last node on the u-to-root path that is encountered) is the LCA. Specifically, after access(u), access(v) returns the LCA as the last node that was splayed during the path-switching steps. This makes link-cut trees a powerful tool for dynamic LCA queries in addition to their primary use in path queries and dynamic connectivity."
```

## Explainer

Link-cut trees solve the dynamic trees problem: maintain a forest of rooted trees under edge insertions (link), edge deletions (cut), and path queries (find the minimum or sum along the path from a node to its tree's root), all in O(log n) amortized time per operation. Sleator and Tarjan introduced them in 1983, building on their earlier invention of splay trees. The data structure is subtle but powerful, and its applications to network flow, dynamic connectivity, and dynamic graph algorithms make it one of the most important advanced data structures.

The key idea is path decomposition. Each tree in the represented forest is decomposed into preferred paths — vertex-disjoint paths covering all vertices, where each node has at most one preferred child. The preferred child of a node v is the child most recently accessed (in the subtree rooted at v). This means that after accessing a node, the entire root-to-node path becomes preferred, concentrating the data structure's representation on the most relevant path. Each preferred path is stored in an auxiliary splay tree, keyed by depth: an in-order traversal of the splay tree visits the nodes from shallowest (closest to root) to deepest. Non-preferred edges between paths are represented by path-parent pointers connecting the top of one auxiliary tree to its parent in the represented tree.

The access(v) operation is the core of the data structure. It makes v the root of its auxiliary splay tree and restructures preferred paths so that the entire root-to-v path becomes a single preferred path. This involves: (1) splaying v within its current auxiliary tree, (2) cutting the preferred path below v (detaching the right subtree in the auxiliary tree), (3) following the path-parent pointer to the parent auxiliary tree, splaying the relevant node there, and joining v's tree as the right child. This repeats until v's path reaches the root of the represented tree. Each step changes an O(1) number of preferred-child designations and performs a splay. The amortized cost of access is O(log n), proved using the same potential function as splay tree analysis: Phi = sum of log(subtree sizes) across all auxiliary trees.

All other operations reduce to access. Link(u, v) accesses u (making it the root of its auxiliary tree), then sets u's path-parent to v. Cut(v) accesses v, then detaches the left subtree in v's auxiliary tree (which contains the path from v's parent to the root). Find-root(v) accesses v, then walks to the leftmost node in the auxiliary tree (the shallowest, which is the root). Path queries (minimum, sum, update) are handled by augmenting the splay trees with subtree aggregates, identical to augmented BSTs.

The application to maximum flow is where link-cut trees have their greatest algorithmic impact. In Dinic's algorithm, each blocking flow phase pushes flow along paths from source to sink in a layered graph. Maintaining the current augmenting tree as a link-cut tree reduces per-path cost from O(n) to O(log n): find the bottleneck via path-minimum, update capacities via path-update, remove saturated edges via cut, and add new tree edges via link. This improvement, from O(mn) to O(m log n) per blocking flow phase, is significant for dense graphs and has theoretical implications for the best known max-flow running times. Beyond flow, link-cut trees are essential for dynamic connectivity, dynamic minimum spanning trees, and any problem where a forest evolves over time and path queries must be answered efficiently.
