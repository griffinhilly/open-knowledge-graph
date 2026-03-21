---
id: planar-graphs
title: Planar Graphs and Euler's Formula
domain: mathematics
course: discrete-math
prerequisites:
- id: graph-connectivity
  type: hard
- id: trees-in-graph-theory
  type: soft
builds-toward:
- graph-coloring
tags:
- planar-graphs
- euler-formula
- kuratowski
- faces
- four-color-theorem
stage: formal-systems
status: validated
---

# Planar Graphs and Euler's Formula

## Core Idea
A graph is planar if it can be drawn in the plane with no edge crossings. For any connected planar graph, Euler's formula states V − E + F = 2, where V, E, F are the counts of vertices, edges, and faces (including the unbounded outer face). This implies every simple planar graph satisfies E ≤ 3V − 6, providing a quick non-planarity test. Kuratowski's theorem characterizes planarity completely: a graph is planar if and only if it contains no subdivision of K₅ or K₃,₃.

## How It's Best Learned
Draw K₄ without crossings to see planarity, then try and fail with K₅ and K₃,₃. Apply Euler's formula to derive the edge bound and use it to prove specific graphs are non-planar. Connect to map coloring (planar graphs model maps) as a natural application of the four-color theorem.

## Common Misconceptions
- Concluding a graph is non-planar because one particular drawing has crossings — what matters is whether any crossing-free drawing exists.
- Forgetting to count the outer unbounded region as a face when applying Euler's formula.

## Questions

```yaml
- question: "A student draws graph G in a particular way and produces 3 edge crossings. She concludes that G is non-planar. Is her reasoning valid?"
  type: multiple-choice
  options:
    - "Yes — any drawing with crossings is sufficient evidence of non-planarity"
    - "No — a graph is non-planar only if every possible drawing has crossings; one bad drawing proves nothing"
    - "Yes — three crossings exceeds the planarity threshold"
    - "No — only Kuratowski's theorem can establish non-planarity"
  answer: 1
  explanation: "Planarity is an existential property: a graph is planar if *some* crossing-free drawing exists. The fact that one particular drawing has crossings says nothing about whether a better drawing is possible. K₄ looks tangled in a naive square drawing but can be redrawn as a triangle with one interior vertex — no crossings. To prove non-planarity you must show that no crossing-free drawing exists, which is done via Euler's formula inequality (E > 3V − 6) or Kuratowski's theorem, not by exhibiting one bad drawing."

- question: "A connected planar graph has V = 7 vertices and E = 11 edges. How many faces does it have?"
  type: multiple-choice
  options:
    - "4"
    - "5"
    - "6"
    - "7"
  answer: 2
  explanation: "Euler's formula for connected planar graphs states V − E + F = 2. Substituting: 7 − 11 + F = 2, so F = 6. This counts all faces, including the unbounded outer region surrounding the entire drawing. Forgetting to count the outer face is the most common error when applying this formula — it always counts as one face regardless of how large it is."

- question: "A graph is non-planar if and only if it contains K₅ or K₃,₃ as a subgraph (not just a subdivision)."
  type: true-false
  answer: false
  explanation: "Kuratowski's theorem requires a *subdivision* of K₅ or K₃,₃, not the graphs themselves. A subdivision replaces each edge with a path through new degree-2 vertices. A graph can be non-planar while containing neither K₅ nor K₃,₃ as literal subgraphs — but it will always contain a subdivision of one of them. The distinction matters: subdivisions introduce extra vertices along edges, so the obstruction graphs can appear in disguised form."

- question: "When Euler's formula V − E + F = 2 is applied to a planar graph drawn without crossings, the large unbounded region surrounding the entire drawing counts as one of the F faces."
  type: true-false
  answer: true
  explanation: "The outer unbounded region is always counted as one face in Euler's formula. This is why a triangle (V=3, E=3) has F=2: one triangular face inside, plus the outer face. Students who forget this will compute F = 1 for a triangle and get V − E + F = 2, apparently satisfied — but only by luck of having undercounted F by exactly 1. For the formula to give consistent results across all planar graphs, the outer face must always be included."

- question: "Explain how the inequality E ≤ 3V − 6 is derived from Euler's formula, and how it can prove a graph is non-planar without examining any specific drawing."
  type: short-answer
  answer: "In any planar graph, every face is bounded by at least 3 edges, and each edge borders at most 2 faces, so 3F ≤ 2E, giving F ≤ 2E/3. Substituting into V − E + F = 2 yields V − E + 2E/3 ≥ 2, which rearranges to E ≤ 3V − 6. If a graph violates this bound (E > 3V − 6), no planar drawing can exist — regardless of how cleverly you try to draw it."
  explanation: "The power of this approach is that it derives a necessary condition for planarity purely from counting, bypassing the need to reason about specific drawings. For K₅: V=5, so 3V−6=9, but E=10 > 9 — immediate contradiction. For K₃,₃: V=6, so 3V−6=12, but E=9 ≤ 12, so this bound alone doesn't rule out K₃,₃ (a tighter bound using the absence of triangles is needed). The inequality is a quick first test; Kuratowski's theorem provides the complete characterization."
```

## Explainer

A graph is **planar** if it can be drawn in the plane with no two edges crossing. Notice the careful phrasing: it is not that a specific drawing is crossing-free, but that *some* drawing exists with no crossings. K₄ (four vertices, every pair connected) looks tangled when drawn naively, but it can be redrawn with one vertex inside a triangle — no crossings. That's enough to make it planar. The question is always existential: does any valid embedding exist?

When a planar graph *is* drawn without crossings, its edges divide the plane into regions called **faces**. Count the regions, including the unbounded outer region that surrounds the whole drawing. For any connected planar graph, these quantities satisfy a remarkable identity discovered by Euler: **V − E + F = 2**, where V is vertices, E is edges, and F is faces. Try it on K₄ drawn as a triangle with an interior point: V = 4, E = 6, F = 4 (three inner faces plus the outer). Indeed 4 − 6 + 4 = 2. This identity is not just a curiosity — it is a powerful counting tool.

The most useful application of Euler's formula is proving non-planarity without finding a specific bad drawing. In any simple planar graph, every face is bounded by at least 3 edges, and every edge borders at most 2 faces, giving 3F ≤ 2E. Substituting F = 2 − V + E from Euler's formula yields **E ≤ 3V − 6**. For K₅: V = 5, so 3V − 6 = 9, but E = 10. Since 10 > 9, K₅ cannot be planar. This one inequality, derived from Euler's formula, immediately disqualifies K₅ without any case analysis on drawings.

**Kuratowski's theorem** completes the picture by giving an exact characterization: a graph is planar if and only if it contains no *subdivision* of K₅ or K₃,₃ as a subgraph (a subdivision replaces edges with paths through new vertices). This means non-planarity always reduces to one of these two "obstructions." Your prerequisite on graph connectivity matters here because Euler's formula applies to connected planar graphs; for disconnected graphs the formula generalizes to V − E + F = 1 + C where C is the number of connected components. The four-color theorem — that every planar map can be colored with four colors — is one of the deepest downstream applications of planarity theory.
