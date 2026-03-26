---
id: graph-minors
title: Graph Minors and Minor-Closed Families
domain: mathematics
course: graph-theory-and-combinatorics
prerequisites:
- id: graph-theory-intro
  type: hard
tags:
- graph-theory
- minors
- structure
stage: formal-systems
status: validated
---

# Graph Minors and Minor-Closed Families

## Core Idea
A graph H is a minor of G if H can be obtained by deleting vertices/edges and contracting edges. Minor-closed families are sets closed under taking minors (e.g., planar graphs, forests, bounded treewidth graphs). The theory of graph minors underpins modern structural graph theory and has led to deep results about decomposition and decidability.

## Questions

```yaml
- question: "A researcher claims: 'H is a minor of G because I found a copy of H as a subgraph of G.' A colleague objects. What is wrong with the researcher's reasoning?"
  type: multiple-choice
  options:
    - "The reasoning is correct: every subgraph relationship is also a minor relationship, and the two definitions are equivalent"
    - "The reasoning is too restrictive: H could be a minor of G even if H is not isomorphic to any subgraph of G, because edge contraction can produce graphs that no amount of deletion alone could create from G"
    - "The reasoning is too broad: a minor relationship requires that H and G share the same vertex set, which a subgraph relationship does not guarantee"
    - "The reasoning confuses directed and undirected graphs — the minor relationship is only defined for undirected graphs"
  answer: 1
  explanation: "While it's true that every subgraph of G is also a minor of G (using only deletions), the converse is false — and this is the key point. Edge contraction merges vertices in a way that deletion cannot, so H can be a minor of G without being isomorphic to any subgraph of G. For example, K₄ is a minor of many sparse graphs where it doesn't appear as a subgraph: find four connected 'blobs' of vertices and contract each blob to a single vertex. The minor relationship is strictly more general than the subgraph relationship precisely because of contraction."

- question: "The Robertson-Seymour theorem guarantees that every minor-closed family of graphs can be characterized by a finite list of forbidden minors. What is the key algorithmic implication of this theorem?"
  type: multiple-choice
  options:
    - "It provides an efficient algorithm for computing all forbidden minors of any given minor-closed family in polynomial time"
    - "If the forbidden minors of a family can each be recognized in polynomial time, then membership in the family can be decided in polynomial time — producing a meta-theorem that converts any finite forbidden-minor characterization into an efficient algorithm"
    - "It proves that all graph problems restricted to minor-closed families are in P, regardless of the specific problem"
    - "It shows that the only minor-closed families relevant to algorithms are planar graphs and forests, since other families have infinitely many forbidden minors"
  answer: 1
  explanation: "The theorem's power is as a meta-algorithm generator. Because every minor-closed family has a finite forbidden-minor list, and because testing for a fixed minor H in a graph G can be done in polynomial time (Robertson and Seymour also proved this), membership in any minor-closed family is decidable in polynomial time. This is remarkable: it means that for problems like 'is this graph embeddable on a surface of genus k?' or 'does this graph have treewidth ≤ k?', polynomial-time algorithms are guaranteed to exist — even when we don't know the forbidden minors explicitly."

- question: "Planar graphs form a minor-closed family: any minor of a planar graph is also planar, because edge deletion and contraction cannot introduce new edge crossings into a planar embedding."
  type: true-false
  answer: true
  explanation: "This is the foundational example of a minor-closed family. Deleting a vertex or edge from a planar embedding trivially preserves planarity. Edge contraction — merging two adjacent vertices — also preserves planarity: the merged vertex can be placed in the region shared by the two original vertices, and no new crossings are introduced. Since planarity is preserved under all three minor operations (vertex deletion, edge deletion, edge contraction), planar graphs are closed under taking minors. Wagner's theorem then characterizes this family by its two forbidden minors: K₅ and K₃,₃."

- question: "The Robertson-Seymour theorem tells us the explicit list of forbidden minors for nearly every minor-closed family, including those families whose forbidden minors are currently unknown to researchers."
  type: true-false
  answer: false
  explanation: "The theorem proves existence — every minor-closed family has a finite forbidden-minor list — but it is non-constructive and does not provide an algorithm for finding that list. For many natural minor-closed families (e.g., graphs embeddable on a torus, graphs of treewidth ≤ 4), the complete forbidden-minor list is either unknown or contains so many elements that it is only partially characterized. The theorem guarantees finiteness; it says nothing about what the forbidden minors are or how to find them."

- question: "What is the key difference between a graph minor and a subgraph, and why does edge contraction make the minor relation strictly more powerful? Give an example showing how a minor can differ dramatically from any subgraph."
  type: short-answer
  answer: "A subgraph is obtained by deleting vertices and/or edges only — the remaining graph is literally a 'piece' of the original, with the same structure among surviving vertices. A minor adds edge contraction: merging two adjacent vertices into one, with all their edges redirected to the merged vertex. This can radically transform a graph's structure. Example: start with a cycle on 6 vertices (C₆). No subgraph of C₆ is K₃ (a triangle), because C₆ has no triangles and no vertex has degree 3. But by contracting every other edge, you merge pairs of adjacent vertices and obtain C₃ (a triangle) — so K₃ is a minor of C₆ without being a subgraph. More dramatically, K₅ is a minor of many planar-looking graphs: find five large connected subsets that are mutually connected, contract each subset to a single vertex, and K₅ emerges."
  explanation: "The practical significance is that the minor relation captures 'hidden structure' that the subgraph relation cannot see. When we say a graph has K₃,₃ as a minor, we're saying there is a way to 'see' K₃,₃'s connectivity pattern in the graph after collapsing some of its structure — which is exactly the right notion for characterizing planarity and other topological graph properties."
```

## Explainer

You know from graph theory that subgraphs are obtained by removing vertices and edges. **Graph minors** introduce a third operation: **edge contraction**. To contract an edge {u, v}, you merge u and v into a single new vertex w, and every edge that previously connected to u or v now connects to w (deleting any resulting loops or duplicate edges). A graph H is a **minor** of G if H can be obtained from G by any combination of these three operations — deleting vertices, deleting edges, and contracting edges — in any order. Crucially, H doesn't need to look anything like a subgraph of G; contraction lets you "collapse" structure in ways that deletion alone cannot.

The best way to build intuition is with a concrete example. Start with a cycle on 5 vertices (C₅). Contract one edge — you merge two adjacent vertices and get a cycle on 4 vertices (C₄). Contract another — you get a triangle (C₃). So C₃ is a minor of C₅. More dramatically: the complete graph K₄ is a minor of almost any sufficiently connected graph, because you can always find four "blobs" of vertices that are mutually connected and contract each blob to a single vertex. The **complete graph K₅** and the **complete bipartite graph K₃,₃** are the two obstructions to planarity in Kuratowski's theorem, but the minor version (Wagner's theorem) says a graph is planar if and only if it has neither K₅ nor K₃,₃ as a **minor** — a cleaner and more fundamental statement.

A family of graphs is **minor-closed** if, whenever G is in the family, every minor of G is also in the family. Planar graphs form a minor-closed family: any minor of a planar graph is still planar (deleting or contracting edges can't introduce crossings). Forests (acyclic graphs) are minor-closed: removing edges or contracting them in a tree gives smaller trees or single vertices. **Bounded treewidth** graphs are minor-closed, and treewidth is a fundamental measure of how "tree-like" a graph is — many NP-hard problems become polynomial when restricted to bounded-treewidth graphs.

The deepest result in this area is the **Robertson-Seymour theorem** (Graph Minor Theorem): in any infinite sequence of graphs, some graph is a minor of a later one. Equivalently, every minor-closed family can be characterized by a *finite* list of **forbidden minors** — graphs not in the family such that any minor not in the family contains one of these as a minor. Planar graphs have exactly two forbidden minors (K₅ and K₃,₃). Forests have one (a triangle). The Robertson-Seymour theorem guarantees such a finite list exists for *every* minor-closed family, even when we don't know what the list is. This connects abstract structure theory to algorithms: if you can recognize a forbidden minor in polynomial time, you can recognize membership in the family in polynomial time, giving a meta-theorem that produces efficient algorithms from structural characterizations.
