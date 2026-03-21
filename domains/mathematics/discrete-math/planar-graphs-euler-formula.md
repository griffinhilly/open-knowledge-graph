---
id: planar-graphs-euler-formula
title: Planar Graphs, Euler's Formula, and Structure
domain: mathematics
course: discrete-math
prerequisites:
- id: graph-theory-fundamentals
  type: soft
tags:
- graph-theory
- planar-graphs
stage: formal-systems
status: draft
---

# Planar Graphs, Euler's Formula, and Structure

## Core Idea
A planar graph can be drawn on a plane without edge crossings. For any connected planar graph: V - E + F = 2 (Euler's formula, where V is vertices, E is edges, F is faces). Kuratowski's theorem: a graph is planar if and only if it contains no K₅ or K₃,₃ subdivisions.

## Questions

```yaml
- question: "A simple connected graph has 8 vertices and 22 edges. Without drawing it, what can you conclude?"
  type: multiple-choice
  options:
    - "It is planar, because 22 edges is not too many for 8 vertices"
    - "It is non-planar, because E = 22 > 3(8) − 6 = 18, violating the necessary condition for planarity"
    - "It might be planar — you would need to try all possible drawings to be sure"
    - "It is non-planar, because Kuratowski's theorem applies to all graphs with more than 20 edges"
  answer: 1
  explanation: "The inequality E ≤ 3V − 6 is a necessary condition for planarity of a simple graph. For V = 8, the bound is 3(8) − 6 = 18. Since 22 > 18, the graph cannot be planar — the arithmetic proof is sufficient, no drawing attempts needed. Option C reflects the misconception that planarity can only be determined by exhaustive drawing; Euler's formula gives us a way to rule it out algebraically."

- question: "A graph G looks like it requires edge crossings in every drawing you attempt. What does this tell you about whether G is planar?"
  type: multiple-choice
  options:
    - "G is definitely non-planar — if all attempted drawings have crossings, no crossing-free drawing can exist"
    - "Nothing definitive — planarity means there EXISTS some drawing without crossings, and you may not have found it yet"
    - "G is planar if the edge crossings can be reduced to fewer than V crossings"
    - "G is non-planar only if it fails both Euler's inequality and Kuratowski's theorem simultaneously"
  answer: 1
  explanation: "Planarity is a property of the abstract graph: does there exist ANY drawing without crossings? The fact that several attempts all produce crossings is not proof of non-planarity. The Explainer gives K₄ as an example — it looks like it needs a crossing, but a redrawing with the fourth vertex inside a triangle shows it is planar. To prove non-planarity, you need either the edge-count inequality or Kuratowski's theorem, not just failed drawing attempts."

- question: "In Euler's formula V − E + F = 2 for connected planar graphs, the unbounded outer region counts as a face."
  type: true-false
  answer: true
  explanation: "This is essential and explicit in the Explainer. For a triangle, V=3, E=3, F=2 — the two faces are the triangular interior region and the unbounded exterior region. If you forgot the outer face, you would get F=1 and the formula would give 3 − 3 + 1 = 1 ≠ 2. Always including the outer region is required for Euler's formula to hold."

- question: "K₅ is non-planar because every possible drawing of it in the plane produces at least one edge crossing."
  type: true-false
  answer: true
  explanation: "This is actually true and consistent with the topic, but the important nuance is *why*: K₅'s non-planarity is not just an empirical observation from failed drawing attempts — it is provable from the edge-count inequality. K₅ has V=5, E=10, and 3V−6=9, so E > 3V−6, which violates the necessary condition for planarity. This algebraic proof guarantees that no drawing without crossings can exist, which is a stronger and more general claim than 'we've tried many drawings.'"

- question: "How does Euler's formula allow you to prove that K₅ is non-planar without trying all possible drawings?"
  type: short-answer
  answer: "Euler's formula implies a necessary inequality for planar graphs: E ≤ 3V − 6 (since every face is bounded by at least 3 edges, and each edge borders at most 2 faces, giving 3F ≤ 2E; substituting F = 2 − V + E yields E ≤ 3V − 6). K₅ has V=5 and E=10, but 3(5)−6=9 < 10. Since K₅ violates this necessary condition, it cannot be planar — regardless of how it is drawn."
  explanation: "This is the payoff of Euler's formula: it turns a topological/geometric question (can this graph be drawn without crossings?) into an algebraic inequality that can be checked in seconds. The key conceptual move is deriving the edge bound from the face-edge relationship and then substituting Euler's formula to eliminate F. Kuratowski's theorem then gives the converse: not just that K₅ fails this test, but that every non-planar graph contains K₅ or K₃,₃ as a subdivision."
```

## Explainer

From graph theory fundamentals, you know vertices and edges can be connected in arbitrary ways. But draw a graph on paper and edges might cross. **Planarity** asks whether there exists *some* drawing of the graph where no two edges cross — it's a property of the abstract graph, not any particular drawing. Many graphs that look messy at first glance can be redrawn cleanly. K₄ (four vertices, all pairs connected) looks like it needs crossings, but it can be drawn as a triangle with the fourth vertex inside and edges to all corners.

Once you have a planar graph drawn without crossings, it divides the plane into regions called **faces** — including the unbounded outer region. Count the vertices (V), edges (E), and faces (F) of any connected planar graph, and you'll always find V - E + F = 2. This is **Euler's formula**, and it's remarkably universal. For a triangle: V=3, E=3, F=2 (one inner face + one outer). For a square with a diagonal: V=4, E=5, F=3 (two inner + one outer). Check: 4 - 5 + 3 = 2. The formula can be proved by induction: start with a spanning tree (which has V-1 edges and 1 face, giving V - (V-1) + 1 = 2), then add edges back one at a time, each adding one edge and splitting one face into two, keeping V - E + F constant.

Euler's formula gives you a powerful tool to *prove* a graph is not planar without needing to try every possible drawing. Since every face in a simple graph is bounded by at least 3 edges, and each edge borders at most 2 faces, we get 3F ≤ 2E, or F ≤ 2E/3. Substituting into Euler's formula: E ≤ 3V - 6. K₅ has 5 vertices and 10 edges. But 3(5) - 6 = 9 < 10, so K₅ violates the inequality and cannot be planar. Similarly K₃,₃ is ruled out using the tighter bound for bipartite graphs (every face has ≥ 4 edges).

**Kuratowski's theorem** makes this classification complete: a graph is planar *if and only if* it contains no subdivision of K₅ or K₃,₃. A subdivision means you can insert extra vertices along edges. This means those two graphs are essentially the only "obstruction" to planarity — any non-planar graph has one of them lurking inside it, possibly disguised by extra vertices on edges. This is a deep structural result: it characterizes planarity not just by a necessary inequality but by an exact forbidden-substructure criterion, connecting the combinatorial (edge counting) with the topological (embeddability in the plane).
