---
id: wagners-theorem
title: Wagner's Theorem
domain: mathematics
course: graph-theory-and-combinatorics
prerequisites:
- id: kuratowskis-theorem
  type: hard
builds-toward:
- graph-minors
tags:
- graph-theory
- planar-graphs
- minors
stage: formal-systems
status: draft
---

# Wagner's Theorem

## Core Idea
Wagner's Theorem states that a graph is planar if and only if it contains neither K₅ nor K₃,₃ as minors. This formulation is equivalent to Kuratowski's theorem but uses the stronger minor relation, showing that planarity can be characterized by two forbidden minors alone.

## How It's Best Learned
Study the relationship between subdivisions and minors; understand why contracting edges gives a weaker condition than just forbidding subdivisions.

## Common Misconceptions
Forbidding K₅ and K₃,₃ as minors is sufficient; you do not need to check any other minors or forbidden subgraphs.

## Explainer

From **Kuratowski's Theorem**, you know that a graph is planar if and only if it contains no **subdivision** of K₅ or K₃,₃. A subdivision takes a graph and inserts new degree-2 vertices along its edges — stretching edges into paths without changing the graph's essential connectivity. Kuratowski says planarity fails precisely when K₅ or K₃,₃ is "hiding inside" the graph as a subdivided copy. **Wagner's Theorem** restates this using a different concept — the **graph minor** — and in doing so reveals a deeper structural truth.

A **minor** of G is obtained by repeatedly applying three operations: deleting vertices, deleting edges, or **contracting edges** (merging two adjacent vertices into one, inheriting all their edges). The key distinction from subdivision: edge contraction is more powerful. It can merge two high-degree vertices, not just undo a degree-2 insertion. This means "G contains H as a minor" is a *weaker* condition than "G contains a subdivision of H" — every subdivision yields a minor (contract the inserted degree-2 vertices back out), but not every minor comes from a subdivision. So forbidding K₅ and K₃,₃ as minors should, in principle, ban a *larger* class of graphs than Kuratowski's condition. Wagner's Theorem says it doesn't: the two conditions are equivalent. A graph is planar if and only if it has neither K₅ nor K₃,₃ as a minor.

Why does the equivalence hold despite the minor relation being weaker? The proof shows that any graph containing K₅ or K₃,₃ as a minor also contains a subdivision of K₅ or K₃,₃ (or can be reduced to a graph that does via a case analysis). For general H this implication fails — there exist graphs with H as a minor but no subdivision of H — but K₅ and K₃,₃ are special enough that the implication goes through. Verifying this is the technical heart of the equivalence between Wagner's and Kuratowski's theorems.

Wagner's formulation matters enormously for the broader theory of graph structure. The concept of a **graph minor** opens the door to the Robertson–Seymour Graph Minor Theorem, one of the deepest results in combinatorics: every **minor-closed family** of graphs (a family where any minor of a member is also a member) can be characterized by a *finite* list of forbidden minors. Planar graphs form a minor-closed family — any minor of a planar graph is planar — and Wagner's Theorem identifies that family's forbidden minors as exactly {K₅, K₃,₃}. This made planarity the prototype for a vast classification program: what are the forbidden minors for graphs on a torus? For graphs of bounded treewidth? Wagner's Theorem is the first and most elegant answer in this deep structural story.
