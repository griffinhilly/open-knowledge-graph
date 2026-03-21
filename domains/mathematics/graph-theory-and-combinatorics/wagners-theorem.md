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

## Questions

```yaml
- question: "Graph G contains K₅ as a minor but does NOT contain any subdivision of K₅ or K₃,₃. By Wagner's theorem, is G planar?"
  type: multiple-choice
  options:
    - "Yes — G contains no subdivision of K₅ or K₃,₃, so Kuratowski's condition is satisfied and G must be planar."
    - "No — Wagner's theorem shows that containing K₅ as a minor is sufficient to conclude non-planarity, and this condition is equivalent to Kuratowski's."
    - "We cannot determine planarity without checking Kuratowski's condition separately from Wagner's."
    - "Only K₃,₃ as a minor is relevant to planarity; K₅ minors alone do not determine it."
  answer: 1
  explanation: "Wagner's theorem states that a graph is planar if and only if it contains neither K₅ nor K₃,₃ as a *minor*. The theorem proves this is equivalent to Kuratowski's subdivision condition, so no separate check is needed. The premise of the question is actually impossible — Wagner's equivalence guarantees that if G contains K₅ as a minor, it must also contain a subdivision of K₅ or K₃,₃. Option A is the classic misconception: thinking the conditions are independent."

- question: "Why is 'containing H as a minor' a weaker condition than 'containing a subdivision of H'?"
  type: multiple-choice
  options:
    - "Minors can only be formed by edge contraction, making them harder to find than subdivisions."
    - "A graph that contains a subdivision of H automatically contains H as a minor (by contracting the inserted degree-2 vertices), but not every minor arises from a subdivision."
    - "Subdivisions insert vertices that always increase the minor count of a graph."
    - "Minors require the graph to have more vertices, while subdivisions only require more edges."
  answer: 1
  explanation: "A subdivision of H can be turned into H as a minor by contracting away the degree-2 vertices inserted along each edge. So every graph containing a subdivision of H also contains H as a minor — meaning 'contains H as minor' is satisfied by a larger class of graphs. For general H, this gap is real: graphs can contain H as a minor without any subdivision. The surprise of Wagner's theorem is that for K₅ and K₃,₃ specifically, the gap closes and the two conditions are equivalent."

- question: "Wagner's theorem and Kuratowski's theorem give equivalent characterizations of planarity, even though graph minors and subdivisions are different structural relationships."
  type: true-false
  answer: true
  explanation: "This is Wagner's theorem. Despite 'containing H as a minor' being a weaker (more permissive) condition than 'containing a subdivision of H,' both conditions identify exactly the same set of non-planar graphs when H ranges over {K₅, K₃,₃}. The proof shows that any graph with K₅ or K₃,₃ as a minor also contains a subdivision of one of them, closing the gap for these two specific graphs."

- question: "Since 'containing H as a minor' is weaker than 'containing a subdivision of H,' Wagner's theorem forbids a strictly larger class of graphs than Kuratowski's theorem."
  type: true-false
  answer: false
  explanation: "The two conditions are equivalent — they forbid exactly the same class of graphs. Although the minor relation is logically weaker in general, Wagner's theorem proves that for K₅ and K₃,₃, any graph containing one of them as a minor also contains a subdivision of one of them. So no graph is banned by Wagner that isn't also banned by Kuratowski, and vice versa. The planarity boundary is the same; only the characterization language differs."

- question: "Why does Wagner's theorem matter beyond being an alternative restatement of Kuratowski's theorem?"
  type: short-answer
  answer: "Wagner's theorem frames planarity using graph minors, which opens the door to the Robertson–Seymour Graph Minor Theorem: every minor-closed family of graphs can be characterized by a finite list of forbidden minors. Planar graphs form a minor-closed family (any minor of a planar graph is planar), and Wagner identifies its two forbidden minors as K₅ and K₃,₃. This turns planarity into the prototype for a vast classification program — the same question ('what are the forbidden minors?') can be asked for graphs on other surfaces, graphs of bounded treewidth, and many other families."
  explanation: "The shift from subdivisions to minors is not just notational. Minors define a partial order on graphs (the graph minor order), and the Robertson–Seymour theorem proves this order is a well-quasi-order — implying every minor-closed family has finitely many forbidden minors. Wagner's theorem is the first and most elegant instance of this general theory."
```

## Explainer

From **Kuratowski's Theorem**, you know that a graph is planar if and only if it contains no **subdivision** of K₅ or K₃,₃. A subdivision takes a graph and inserts new degree-2 vertices along its edges — stretching edges into paths without changing the graph's essential connectivity. Kuratowski says planarity fails precisely when K₅ or K₃,₃ is "hiding inside" the graph as a subdivided copy. **Wagner's Theorem** restates this using a different concept — the **graph minor** — and in doing so reveals a deeper structural truth.

A **minor** of G is obtained by repeatedly applying three operations: deleting vertices, deleting edges, or **contracting edges** (merging two adjacent vertices into one, inheriting all their edges). The key distinction from subdivision: edge contraction is more powerful. It can merge two high-degree vertices, not just undo a degree-2 insertion. This means "G contains H as a minor" is a *weaker* condition than "G contains a subdivision of H" — every subdivision yields a minor (contract the inserted degree-2 vertices back out), but not every minor comes from a subdivision. So forbidding K₅ and K₃,₃ as minors should, in principle, ban a *larger* class of graphs than Kuratowski's condition. Wagner's Theorem says it doesn't: the two conditions are equivalent. A graph is planar if and only if it has neither K₅ nor K₃,₃ as a minor.

Why does the equivalence hold despite the minor relation being weaker? The proof shows that any graph containing K₅ or K₃,₃ as a minor also contains a subdivision of K₅ or K₃,₃ (or can be reduced to a graph that does via a case analysis). For general H this implication fails — there exist graphs with H as a minor but no subdivision of H — but K₅ and K₃,₃ are special enough that the implication goes through. Verifying this is the technical heart of the equivalence between Wagner's and Kuratowski's theorems.

Wagner's formulation matters enormously for the broader theory of graph structure. The concept of a **graph minor** opens the door to the Robertson–Seymour Graph Minor Theorem, one of the deepest results in combinatorics: every **minor-closed family** of graphs (a family where any minor of a member is also a member) can be characterized by a *finite* list of forbidden minors. Planar graphs form a minor-closed family — any minor of a planar graph is planar — and Wagner's Theorem identifies that family's forbidden minors as exactly {K₅, K₃,₃}. This made planarity the prototype for a vast classification program: what are the forbidden minors for graphs on a torus? For graphs of bounded treewidth? Wagner's Theorem is the first and most elegant answer in this deep structural story.
