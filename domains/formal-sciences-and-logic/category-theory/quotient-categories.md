---
id: quotient-categories
title: Quotient Categories
domain: formal-sciences-and-logic
course: category-theory
prerequisites:
- id: categories-and-morphisms
  type: hard
- id: functors
  type: hard
builds-toward: []
tags:
- quotient-construction
- equivalence-relations
- morphism-identification
stage: advanced
status: draft
---
# Quotient Categories

## Core Idea
A quotient category is formed by identifying morphisms in a category according to an equivalence relation that respects composition, resulting in a category where some formerly distinct morphisms are identical. Quotient categories generalize the notion of quotient structures in algebra and provide a framework for understanding how categorical information changes under identifications.

## How It's Best Learned
Start with simple examples: quotient of a discrete category by an equivalence relation on objects, and quotient of a category of complexes by homotopy equivalence. Verify that the quotient map is universal and that the quotient respects categorical structure.

## Common Misconceptions
Not every equivalence relation on morphisms descends to a valid quotient category; the relation must be compatible with composition. Additionally, the quotient category may collapse structure in surprising ways.

## Questions

```yaml
- question: "You impose an equivalence relation ~ on morphisms of a category C where f ~ f' and g ~ g', but you find that g∘f and g'∘f' land in different equivalence classes. What has gone wrong?"
  type: multiple-choice
  options:
    - "Nothing — composed morphisms don't need to be equivalent just because their components are"
    - "Composition in the quotient is ambiguous: the class [g∘f] depends on which representative you pick for [f] and [g], so the quotient structure is not a well-defined category"
    - "The identity morphisms are not preserved, which violates the axioms of the quotient"
    - "You need to also impose an equivalence on objects before the quotient on morphisms can be defined"
  answer: 1
  explanation: "This is the congruence failure. In the proposed quotient, [g] ∘ [f] should equal [g∘f] — but if different representatives g' and f' give a different composite, the composition law is ill-defined. The quotient category construction requires ~ to be a congruence: f ~ f' and g ~ g' must imply g∘f ~ g'∘f'. Without this, there is no canonical way to compose equivalence classes, and the putative quotient is not a category. This is the categorical analog of requiring a subgroup to be normal for the quotient group to have well-defined multiplication."

- question: "In the homotopy category K(A), two chain maps f, g: A• → B• are identified if they are chain-homotopic. Why is this a valid quotient category construction?"
  type: multiple-choice
  options:
    - "Chain homotopy is a trivial relation — all chain maps between any two complexes are homotopic"
    - "Chain homotopy defines a congruence: if f ~ f' and g ~ g' (both chain-homotopic pairs), then the composites g∘f and g'∘f' are also chain-homotopic, so composition is well-defined on homotopy classes"
    - "Chain homotopy identifies objects (chain complexes), not morphisms, so the congruence condition does not apply"
    - "The construction is valid because chain complexes form an abelian category, which automatically makes any equivalence relation a congruence"
  answer: 1
  explanation: "The critical check for any quotient category construction is the congruence condition. For chain homotopy, if h: f → f' is a homotopy between f, f': A• → B• and k: g → g' is a homotopy between g, g': B• → C•, then one can explicitly construct a homotopy between g∘f and g'∘f'. This computation is the key step that validates K(A) as a category. The verification is not automatic — it is specific to the algebraic properties of chain homotopy — which is why checking congruence is always the first obligation in constructing a quotient category."

- question: "Any equivalence relation on the morphism sets of a category can be used to form a valid quotient category."
  type: true-false
  answer: false
  explanation: "This is the central misconception about quotient categories. An arbitrary equivalence relation on morphisms does not produce a category because composition may become ambiguous: if you represent [g∘f] as the class of g∘f, then using different representatives g' ~ g and f' ~ f might give g'∘f' in a different class. The relation must be a congruence — compatible with composition — to ensure that the composition of equivalence classes is well-defined. Without congruence, the putative quotient fails one of the basic axioms of a category."

- question: "In a quotient category C/~, the objects are the same as in C, but morphisms are replaced by equivalence classes of morphisms under a congruence relation."
  type: true-false
  answer: true
  explanation: "Quotient categories identify morphisms, not objects. The objects of C/~ are identical to those of C. For each pair of objects X, Y, the hom-set Hom_{C/~}(X, Y) = Hom_C(X, Y)/~ is the set of equivalence classes. Composition is defined on representatives: [g] ∘ [f] = [g∘f], which the congruence condition guarantees is independent of the choice. Identity morphisms descend directly: [id_X] is the identity in C/~. This construction is the categorical generalization of quotient groups, rings, or vector spaces — modding out by a compatible equivalence to coarsen the structure."

- question: "Explain why the congruence condition (compatibility with composition) is necessary for forming a valid quotient category. What goes wrong if it fails?"
  type: short-answer
  answer: "Composition in the quotient category C/~ is defined by choosing representatives: [g] ∘ [f] = [g∘f]. For this to be well-defined, the class of the composite must not depend on which representatives we choose from [f] and [g]. If f ~ f' and g ~ g' but g∘f is not equivalent to g'∘f', then [g] ∘ [f] would give different results depending on whether we compute g∘f or g'∘f' — composition is ambiguous, and we don't have a category. The congruence condition — f ~ f' and g ~ g' implies g∘f ~ g'∘f' — is exactly what prevents this ambiguity. It is the necessary and sufficient condition for the quotient to inherit a well-defined composition law."
  explanation: "An analogy: modding out a group G by a subgroup H gives a quotient group only if H is normal. The normality condition is the 'congruence' for groups: it ensures coset multiplication is well-defined. In categories, congruence generalizes normality to the setting of morphism composition. Without it, the quotient fails to be a group (in the algebraic case) or a category (in the categorical case)."
```

## Explainer

You know from categories and morphisms that a category consists of objects, morphisms between them, and a composition law. You know from functors that structure-preserving maps between categories must respect this composition. A **quotient category** is what you get when you decide that some formerly distinct morphisms should be considered equal — you "mod out" the morphism sets by an equivalence relation, just as you mod out a group or ring by a normal subgroup or ideal.

The construction is as follows. Start with a category **C**. For each pair of objects X, Y, you impose an equivalence relation ~ on the set Hom_C(X, Y). The critical constraint is that ~ must be a **congruence relation**: it must respect composition. That is, if f ~ f' (morphisms from X to Y) and g ~ g' (morphisms from Y to Z), then g ∘ f ~ g' ∘ f'. This is the categorical analog of a normal subgroup being closed under conjugation — it's precisely the condition that ensures composition in the quotient is well-defined. If you impose an arbitrary equivalence relation that doesn't satisfy congruence, the resulting structure fails to be a category because composition becomes ambiguous.

The **quotient category C/~** then has the same objects as C, but its morphism sets are the equivalence classes: Hom_{C/~}(X, Y) = Hom_C(X, Y)/~. Composition is defined by choosing representatives: [g] ∘ [f] = [g ∘ f], and the congruence condition guarantees this is independent of the choice. The identity morphisms descend immediately: [id_X] is the identity in C/~. The quotient functor Q: C → C/~ sends each morphism f to its class [f]; it is a functor by construction and is the universal functor that identifies all related morphisms — any functor out of C that makes ~ equivalent morphisms go to equal morphisms factors uniquely through C/~.

The most important example in practice is the **homotopy category of chain complexes**: two chain maps f, g: A• → B• are declared equivalent if they are chain-homotopic (there exists a degree-1 map h with f − g = dh + hd). This is a congruence relation, and the quotient category is denoted K(A). The homotopy category collapses an enormous amount of data — two chain maps related by a homotopy are "equivalent for homological purposes" — and is the first step toward the derived category, where one further inverts quasi-isomorphisms. Understanding quotient categories thus unlocks the conceptual foundation of homological algebra: derived categories, derived functors, and localization are all built on this basic machinery of identifying morphisms by categorical equivalence.
