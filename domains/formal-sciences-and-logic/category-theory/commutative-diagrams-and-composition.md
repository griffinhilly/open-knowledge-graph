---
id: commutative-diagrams-and-composition
title: Commutative Diagrams and Composition
domain: formal-sciences-and-logic
course: category-theory
prerequisites:
- id: categories-and-morphisms
  type: hard
- id: commutative-diagrams-in-categories
  type: soft
- id: functor-composition
  type: soft
builds-toward:
- diagram-chasing-lemmas
- natural-transformations
tags:
- diagrams
- composition
- fundamentals
stage: expert
status: validated
---
# Commutative Diagrams and Composition

## Core Idea
Commutative diagrams are the primary visual language of category theory, where paths between objects represent compositions of morphisms. A diagram commutes when different paths between the same objects have equal compositions, a principle that underlies almost all categorical reasoning. Understanding how to read, construct, and verify commutativity is essential for any categorical argument.

## How It's Best Learned
Begin with simple two-object, two-path diagrams and verify commutativity by hand. Graduate to three- and four-object diagrams. Practice translating prose proofs into diagram form and vice versa.

## Common Misconceptions
Students often think commutativity means all paths are equal; it only means designated paths are equal. Another confusion: a diagram need not be 'rectangular'—any shape of commutative diagram is valid.

## Questions

```yaml
- question: "A square diagram has objects A, B, C, D with morphisms f: A → B, g: B → D, h: A → C, k: C → D. The diagram is said to commute. What exactly does this assert?"
  type: multiple-choice
  options:
    - "All four morphisms f, g, h, k are equal to each other as arrows in the category"
    - "The composite g∘f equals the composite k∘h — the two paths from A to D yield the same result"
    - "Every morphism in the diagram factors through every other object, meaning f = h and g = k"
    - "The diagram has exactly one morphism between each pair of objects, so there is only one path and commutativity is automatic"
  answer: 1
  explanation: "Commutativity asserts that specific paths between the same source and target produce equal composites. In this square, the two paths from A to D are: A→B→D (composite g∘f) and A→C→D (composite k∘h). The diagram commutes if and only if g∘f = k∘h. The morphisms f, g, h, k are generally distinct arrows — for example, f: A→B and h: A→C have different codomains, so they cannot possibly be equal. Commutativity is not a claim about individual morphisms being equal; it is a claim about equality of composed paths between designated endpoints."

- question: "In a commutative triangle with morphisms f: A→B, g: B→C, and h: A→C, what equation does commutativity assert, and what type of object is on each side?"
  type: multiple-choice
  options:
    - "f = g∘h, asserting that the direct morphism equals a composite; both sides are morphisms A→B"
    - "h = g∘f, asserting the direct morphism A→C equals the composite going through B; both sides are morphisms A→C"
    - "g = h∘f, asserting the morphism B→C equals a composite; both sides are morphisms B→C"
    - "f∘g = h, asserting that the order of composition determines commutativity; both sides are endomorphisms"
  answer: 1
  explanation: "In the triangle, the two paths from A to C are: directly via h, and through B via f then g (written g∘f in standard notation where composition is applied right-to-left). Commutativity asserts h = g∘f. Both sides are morphisms A→C — they have the same source and target, which is required for the equality to even be well-typed. Note option A reverses f and h and gets the composition order wrong; option C confuses which morphism is claimed equal to the composite."

- question: "A commutative diagram asserts that all morphisms appearing in the diagram are equal to one another, since all paths lead to the same objects."
  type: true-false
  answer: false
  explanation: "This is the most common misreading of commutative diagrams. Commutativity asserts that certain *composite paths* with the same source and target are equal — not that the individual morphisms are equal. In a commutative square, g∘f = k∘h, but f, g, h, and k are generally distinct arrows. Indeed, f: A→B and h: A→C cannot even be equal (they have different codomains). The diagram encodes a specific equality between two composite paths, nothing more. Different commutative diagrams in the same category encode different equalities — the diagram is the proof obligation, not a claim about all morphisms."

- question: "When a definition in category theory states 'the following diagram commutes,' it is making a constructive assertion: it is claiming that specific morphisms are chosen or constructed so that the stated path equalities hold by design."
  type: true-false
  answer: true
  explanation: "This is a crucial distinction between two uses of commutative diagrams. When a diagram appears in a *theorem*, commutativity is something to be *proved* — it is a consequence of other axioms or hypotheses. When a diagram appears in a *definition* (such as the definition of a natural transformation or a pullback), commutativity is *imposed by construction* — the objects and morphisms being defined are required to make the diagram commute, and this requirement is what gives them their universal property. Reading 'the following diagram commutes' in a definition tells you what equalities must hold for something to count as an instance of that defined concept."

- question: "Two students examine a square commutative diagram showing paths A→B→D and A→C→D. One student says: 'So the morphism f: A→B must equal the morphism h: A→C, since they both start at A.' Explain what's wrong with this reasoning and state what the diagram actually asserts."
  type: short-answer
  answer: "The student's error is conflating the morphisms themselves with the paths they participate in. The morphism f: A→B and the morphism h: A→C have different codomains (B vs. C), so they cannot be equal — they live in different hom-sets. Commutativity makes no claim about individual morphisms being equal. What the diagram asserts is that the two full paths from A to D produce the same composite: g∘f = k∘h (where g: B→D and k: C→D). Both sides are morphisms A→D — same source, same target — so the equality is well-typed. The claim is about the result of traversing each complete path, not about any individual step."
  explanation: "This error is common because students borrow geometric intuition (all roads lead to the same destination, so the roads must be the same) and apply it to categorical composition. In geometry, two paths from A to D that are equal in length might seem 'the same,' but in category theory, morphisms are abstract arrows with sources and targets — what matters is the equality of their composites, not the equality of the arrows themselves. Keeping the type-checking in mind (checking that source and target match before asserting equality) prevents this confusion."
```

## Explainer

From your study of categories and morphisms, you know that a category consists of objects, morphisms, a composition rule, and identity morphisms. The composite of f: A → B and g: B → C is written g∘f: A → C. A **commutative diagram** is simply a drawing of this structure: nodes represent objects, directed edges represent morphisms, and the diagram encodes an equality claim. The diagram **commutes** when every pair of directed paths with the same source and target produces the same composite morphism.

The simplest example is a triangle: three objects A, B, C with morphisms f: A → B, g: B → C, and h: A → C. The triangle commutes if h = g∘f. You trace the two paths from A to C — either go directly via h, or go through B via f then g — and check they are equal. That equality is the entire content of commutativity. A square with objects A, B, C, D and morphisms f: A → B, g: B → D, h: A → C, k: C → D commutes if g∘f = k∘h: going right-then-down equals going down-then-right.

The power of commutative diagrams is that they turn equality statements into geometry. A prose proof might say "the composite of these five morphisms equals the composite of those four" — a diagram makes this immediately visible and checkable by eye. When you encounter the phrase "the following diagram commutes" in a theorem or definition, it is asserting a specific equality between compositions of the labeled morphisms. Reading the diagram correctly means identifying all the paths between each pair of objects and confirming the equality claimed.

Note carefully: commutativity is **not** a global property of a diagram saying all morphisms are somehow the same. Two morphisms f, g: A → B are generally distinct. A diagram specifies particular morphisms along particular edges, and commutativity is the assertion that certain pairs of paths are equal — only those paths, not all paths. Different diagrams in the same category assert different equalities. This is why diagrams can encode definitions (a diagram that commutes *by construction*, defining a universal property) and theorems (a diagram one proves commutes from other axioms). Diagram chasing — your next topic — builds on this by proving that if certain sub-diagrams commute, other diagrams in the same figure must also commute, enabling chain-of-equality arguments that would be cumbersome in pure notation.
