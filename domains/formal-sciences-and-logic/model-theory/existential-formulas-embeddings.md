---
id: existential-formulas-embeddings
title: Existential Formulas and Preservation under Embeddings
domain: formal-sciences-and-logic
course: model-theory
prerequisites:
- id: first-order-logic-syntax
  type: hard
- id: model-interpretation-and-satisfaction
  type: hard
- id: universal-formulas-substructures
  type: soft
builds-toward:
- model-completeness-theorems
- definable-algebraic-closure
tags:
- existential-formulas
- preservation
- embeddings
stage: advanced
status: validated
---
# Existential Formulas and Preservation under Embeddings

## Core Idea
An existential formula (of the form ∃x φ where φ is quantifier-free) is preserved under embeddings: if an existential formula holds in a structure, it holds in any embedding of that structure. This dual preservation property characterizes which formulas propagate forward through embeddings.

## Questions

```yaml
- question: "Graph G satisfies the sentence ∃x ∃y (x ≠ y ∧ E(x,y)). Graph H is formed by taking G and adding new vertices and edges. Must H also satisfy this sentence?"
  type: multiple-choice
  options:
    - "Not necessarily — H might be a different graph that assigns different meanings to the variables x and y"
    - "Yes — the witness elements (the two adjacent vertices in G) are still present in H after embedding, so the existential sentence remains satisfied"
    - "Only if H is isomorphic to G, since embeddings preserve structure only between isomorphic structures"
    - "Not necessarily — adding edges to H might change the truth value of edge relation E for the original vertices"
  answer: 1
  explanation: "This is the key property of existential formulas: they are preserved under embeddings. The sentence requires witnesses — two vertices a, b with a ≠ b and E(a,b). These witnesses exist in G. Since H embeds G (injectively, preserving relations), the images of a and b in H still satisfy a ≠ b and E(a,b). The new vertices and edges added to form H cannot destroy the existence of witnesses already present. Option D is wrong because embeddings preserve relations: if E(a,b) holds in G, then E(f(a),f(b)) holds in H for any embedding f."

- question: "Which of the following formulas is preserved under embeddings — meaning that if it holds in a structure A, it must hold in any structure B into which A embeds?"
  type: multiple-choice
  options:
    - "∀x ∀y (E(x,y) → E(y,x))   [the graph is symmetric]"
    - "∀x ¬E(x,x)   [the graph has no self-loops]"
    - "∃x ∃y ∃z (E(x,y) ∧ E(y,z) ∧ E(z,x))   [the graph contains a triangle]"
    - "∀x ∃y E(x,y)   [every vertex has at least one neighbor]"
  answer: 2
  explanation: "Only the existential sentence (option C) is preserved under embeddings. It asserts the existence of a triangle — three vertices with the required edges. If such witnesses exist in A, they persist in any embedding of A. The universal sentences (A, B, D) are not preserved: embedding A into B can add elements that violate universal conditions. For example, B might contain a non-symmetric edge (violating option A), a self-loop (violating B), or an isolated vertex (violating D), even though A had no such elements. Universal formulas are preserved in the other direction — downward, under substructures."

- question: "The Łoś-Tarski theorem states that a formula is preserved under embeddings if and only if it is logically equivalent to an existential formula. This means the semantic property (preserved under embeddings) and the syntactic property (being existential) coincide exactly."
  type: true-false
  answer: true
  explanation: "This is the content of the Łoś-Tarski theorem — a characterization result that bridges syntax and semantics. The 'if' direction is straightforward: existential formulas are preserved under embeddings because witness elements survive the injection. The 'only if' direction is deeper: any formula preserved under embeddings must be expressible as an existential formula. This means you cannot have a formula that is semantically preserved under embeddings but syntactically requires universal or nested quantifiers. Preservation properties directly characterize quantifier structure — one of the central achievements of preservation theory."

- question: "The sentence 'this graph has no edges' — formally ∀x ∀y ¬E(x,y) — is an existential property because it makes a claim about the absence of witnesses."
  type: true-false
  answer: false
  explanation: "Despite being about absence, this is a universal formula: it universally quantifies over all pairs of vertices and asserts a negative property. It cannot be expressed as a purely existential formula. This matters for preservation: the property 'no edges' is NOT preserved under embeddings. A graph with no edges embeds into any graph (since you add new vertices and edges but preserve the existing empty-edge relation on the original vertices) — but the larger graph likely has edges. So the embedded structure satisfies 'no edges' while the embedding target does not. Universal formulas are preserved under substructures (going to smaller structures), not under embeddings (going to larger ones)."

- question: "Explain in your own words why existential formulas are preserved upward under embeddings, while universal formulas are preserved downward under substructures. What is the underlying logical reason?"
  type: short-answer
  answer: "Existential formulas say 'something exists' — they are satisfied by providing witnesses. An embedding injects the small structure into the large one and preserves all relations, so any witnesses present in the small structure are still present (as their images) in the large structure. You cannot 'lose' witnesses by adding more elements. Universal formulas say 'everything satisfies this condition' — they can be violated by adding new elements that fail the condition. Going to a smaller structure (substructure) cannot introduce new violating elements, so universal formulas are preserved downward."
  explanation: "The intuition is about what each quantifier type is 'at risk' of: existential claims risk losing witnesses (so they are stable when you add elements, i.e., going upward), while universal claims risk gaining counterexamples (so they are stable when you remove elements, i.e., going downward). An embedding is a passage to a potentially larger structure — safe for existential, dangerous for universal. A substructure passage removes elements — safe for universal, dangerous for existential (witnesses might be removed). The Łoś-Tarski theorem shows these intuitions are exact: the syntactic classification (∃ vs ∀) perfectly predicts the direction of preservation."
```

## Explainer

You already know how to interpret a first-order formula in a structure — you assign elements to variables and check whether the formula is satisfied. An **embedding** is a structure map that injects one structure into another while preserving all the basic relational facts: if a relation holds between elements in the small structure, it holds between their images in the large structure. Think of embedding the integers into the rationals, or a subgraph into a larger graph. The question preservation theory asks is: which formulas, once satisfied in a small structure, must stay satisfied in any larger structure containing it?

**Existential formulas** are exactly the formulas of the form ∃x₁ ∃x₂ … ∃xₙ φ(x₁,…,xₙ) where φ contains no quantifiers. The key insight is that existential formulas only require *witness elements to exist* — they never assert that something fails to exist or that all elements have some property. If the witnesses are present in the small structure, they are present in any structure that embeds the small one (since embeddings are injective and preserve relations). So satisfying an existential formula is "upward stable" along embeddings.

A concrete example: "there exist two elements a, b such that a ≠ b and E(a,b)" is an existential formula asserting that the graph has at least one edge. If a graph G satisfies this, any graph H into which G embeds also satisfies it — because the same two vertices a, b with edge E(a,b) appear in H. Contrast this with a universal formula "for all a, b, if E(a,b) then E(b,a)" (symmetry of the edge relation). This can fail after embedding: you might add asymmetric edges in the larger structure. Universal formulas are preserved under *substructures* (going downward), not embeddings.

The **Łoś-Tarski theorem** makes this connection precise: a first-order formula (or set of formulas) is preserved under embeddings if and only if it is logically equivalent to an existential formula. This is a characterization theorem — it says the syntactic property of being existential and the semantic property of being preserved under embeddings are the same thing. This is a model-theoretic analog of a compactness argument: you cannot express a property that vanishes after embedding unless it has universal quantifiers.

The practical importance is in algebra and combinatorics. When you study classes of structures defined by existential conditions — graphs containing a triangle, groups with a non-identity element of finite order, fields with a root of a polynomial — you know these properties are inherited by larger structures. Conversely, if a property can be lost after extending a structure (e.g., torsion-freeness, which can fail after taking quotients), it cannot be captured by existential sentences alone. Preservation theorems are one of the core tools for matching syntactic form to semantic behavior in model theory.
