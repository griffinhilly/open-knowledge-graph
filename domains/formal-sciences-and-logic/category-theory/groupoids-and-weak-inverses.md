---
id: groupoids-and-weak-inverses
title: Groupoids and Weak Inverses
domain: formal-sciences-and-logic
course: category-theory
prerequisites:
- id: categories-and-morphisms
  type: hard
- id: isomorphisms-in-categories
  type: hard
builds-toward:
- the-fundamental-groupoid
tags:
- groupoids
- invertible-morphisms
- automorphisms
stage: advanced
status: draft
---

# Groupoids and Weak Inverses

## Core Idea
A groupoid is a category in which every morphism is an isomorphism, generalizing both groups and equivalence relations. Groupoids provide a framework for studying 'partial' algebraic structures where not all pairs of elements can be composed, and arise naturally in topology, combinatorics, and analysis. The theory of groupoids captures aspects of both group theory and category theory.

## How It's Best Learned
Study the fundamental groupoid of a topological space, the groupoid of a group action, and abstract groupoids given by presentations. Verify that morphisms are invertible and explore the automorphism groups at each object. Compute groupoid homology and cohomology.

## Common Misconceptions
A groupoid is not just a group with extra structure; it has multiple objects. The identity morphisms at different objects are distinct, and composition is only defined when target and source match appropriately.

## Questions

```yaml
- question: "Define objects as points of a topological space X, and morphisms from x to y as homotopy classes of paths from x to y, with composition as path concatenation. What is the correct algebraic classification of this structure?"
  type: multiple-choice
  options:
    - "A group, because path composition is associative and every path has a reverse"
    - "A groupoid, because every path has an inverse (its reversal) but composition is only defined when the endpoint of one path matches the start of the next"
    - "A category but not a groupoid, because paths between distinct points cannot be inverted in the homotopy sense"
    - "Neither a group nor a groupoid, because path concatenation is not strictly associative"
  answer: 1
  explanation: "This is the fundamental groupoid Π₁(X). It is a groupoid — not a group — because it has multiple objects (the points of X) and morphisms only compose when endpoints match. Every path from x to y has an inverse (the path traversed backwards), making every morphism an isomorphism. It cannot be a group because a group has a single object (all elements compose with all others), whereas here composition x→y composed with z→w is undefined unless y = z."

- question: "How does a groupoid fundamentally differ from a group?"
  type: multiple-choice
  options:
    - "A groupoid relaxes associativity — composition is only associative when all morphisms have the same source"
    - "A groupoid allows morphisms without inverses, whereas a group requires every element to have an inverse"
    - "A groupoid has multiple objects, so composition is only defined when the target of one morphism equals the source of the next"
    - "A groupoid requires all objects to be isomorphic, whereas a group has a single identity element"
  answer: 2
  explanation: "The defining difference is that a groupoid has multiple objects. In a group, there is exactly one object, so every pair of elements (morphisms) can be composed. In a groupoid, a morphism f: A → B and g: C → D can only be composed as g ∘ f when B = C. Both structures require all morphisms to be invertible — that is not the distinction. Option B is wrong because a groupoid requires all morphisms to have inverses (that is what makes it a groupoid rather than just a category)."

- question: "A group can be viewed as a special case of a groupoid — specifically, a groupoid with exactly one object."
  type: true-false
  answer: true
  explanation: "This is a clean categorical fact. In a one-object category where every morphism is an isomorphism, the single object provides the common source and target for all morphisms, so any two morphisms compose. The set of all morphisms with composition as the binary operation satisfies the group axioms: associativity (inherited from category axioms), identity (the single object's identity morphism), and inverses (since every morphism is an isomorphism). The groupoid concept genuinely extends the group concept by allowing more than one object."

- question: "In a groupoid, any two morphisms can be composed, just as any two elements of a group can be multiplied."
  type: true-false
  answer: false
  explanation: "This is the core distinction between groups and groupoids. In a group (viewed as a one-object category), every morphism shares the same source and target, so all pairs compose. In a groupoid with multiple objects, morphism f: A → B and morphism g: C → D compose as g ∘ f only when B = C — the target of f must equal the source of g. This partial composition is what makes groupoids useful for structures where 'elements' only interact with compatible partners, such as paths between specific points in a space."

- question: "Explain why an equivalence relation on a set can be viewed as a groupoid, and what property of the equivalence relation corresponds to invertibility of morphisms."
  type: short-answer
  answer: "Given an equivalence relation ~ on a set S, define a category where objects are elements of S, and there is exactly one morphism from x to y whenever x ~ y (and no morphism otherwise). Composition is forced (there is at most one morphism between any two objects, so the composition of x→y and y→z is the unique morphism x→z, which exists because ~ is transitive). This is a groupoid because symmetry of ~ guarantees that if x ~ y then y ~ x — so every morphism x→y has an inverse y→x. The identity morphisms exist because ~ is reflexive."
  explanation: "The three axioms of an equivalence relation correspond exactly to the categorical structure: reflexivity (x ~ x) gives identity morphisms; symmetry (x ~ y implies y ~ x) gives inverses, making every morphism an isomorphism; transitivity (x ~ y and y ~ z imply x ~ z) gives composition. This example shows how groupoids unify two seemingly different mathematical objects — equivalence relations and groups — under a single framework. A group is the special case where every element is related to every other; an equivalence relation is the special case where at most one morphism exists between any two objects."
```

## Explainer

From your prerequisite on categories and morphisms, you know that a category has objects and arrows between them, with composition satisfying associativity and unit laws. From isomorphisms in categories, you know that a morphism f: A → B is an isomorphism when there exists g: B → A such that g ∘ f = id_A and f ∘ g = id_B. A **groupoid** is simply a category in which *every* morphism is an isomorphism — all arrows are invertible. This single requirement transforms the algebraic structure dramatically.

To see why, consider the two extreme cases. A category with a single object and all morphisms invertible is exactly a **group**: composition is the group operation, the identity morphism is the identity element, and inverses are the morphism inverses. A groupoid generalizes this by allowing many objects, so you can have "partial group structure" — some pairs of elements compose, others do not, depending on whether source and target match. An **equivalence relation** on a set gives another extreme: objects are elements of the set, and there is exactly one morphism from x to y whenever x ~ y (and none otherwise). Invertibility corresponds to symmetry of the relation. So groupoids unify groups and equivalence relations in a single framework.

The richest example is the **fundamental groupoid** Π₁(X) of a topological space X. Objects are points of X, and a morphism from x to y is a homotopy class of paths from x to y. Composition is concatenation of paths; the identity at x is the constant path at x; and the inverse of a path is the same path traversed backwards. This is automatically a groupoid because every path can be reversed. When X is path-connected and you restrict to a single basepoint x₀, you recover the familiar fundamental group π₁(X, x₀) as the **automorphism group** at the object x₀. The fundamental groupoid is strictly more informative: it captures all basepoints and all paths between them simultaneously, without privileging any one basepoint.

The structure of a groupoid is thus richer than a group in one key respect: it has multiple objects, so the automorphism groups at different objects (the "local groups" Aut(x) = Hom(x, x)) may differ. In the fundamental groupoid of a space with multiple path components, the automorphism groups at points in different components are unrelated. In a groupoid arising from a group action — where objects are elements acted upon and a morphism from x to y exists for each group element g with g·x = y — the automorphism group at each object is the **stabilizer** of that object under the action. Groupoids make the relationship between global symmetry and local stabilizers transparent.

**Weak inverses** in the title refer to the morphism-level inverses in a groupoid, to distinguish them from strict inverses in a group. In a group, the inverse of g is unique and satisfies g⁻¹g = e = gg⁻¹ exactly. In higher categorical contexts (bicategories, 2-groupoids), one weakens the notion of invertibility to require only that the composites are *isomorphic* to the identity, rather than equal — this is the "weak" part. Ordinary groupoids are the 1-dimensional version of this tower. Your next topic, the fundamental groupoid, will develop the topological interpretation further and show how groupoids serve as the natural language for describing paths, loops, and homotopies across a space simultaneously.
