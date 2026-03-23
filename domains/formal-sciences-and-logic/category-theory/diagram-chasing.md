---
id: diagram-chasing
title: Diagram Chasing and Commutative Diagrams
domain: formal-sciences-and-logic
course: category-theory
prerequisites:
- id: categories-and-morphisms
  type: hard
builds-toward:
- exact-sequences
- snake-lemma
- natural-isomorphisms
tags:
- proof-technique
- reasoning
- homological-algebra
stage: expert
status: draft
---

# Diagram Chasing and Commutative Diagrams

## Core Idea
Diagram chasing is a proof technique using commutative diagrams: proving statements by composing morphisms along paths and verifying they commute. In abelian categories, it allows element-like reasoning despite working purely with morphisms. Chasing along paths captures logical deductions about morphism composition.

## Questions

```yaml
- question: "A commutative square has morphisms f: A→B, g: B→D, h: A→C, k: C→D satisfying g∘f = k∘h. You know that g∘f is the zero morphism (g∘f = 0). What can you immediately conclude about k∘h?"
  type: multiple-choice
  options:
    - "k∘h may or may not be zero — you need to know whether k or h individually is zero"
    - "k∘h = 0, because commutativity of the diagram means the two paths give the same morphism"
    - "k∘h = 0 only if h is injective (a monomorphism)"
    - "The diagram cannot commute if g∘f = 0, because zero morphisms break commutativity"
  answer: 1
  explanation: "This is a direct application of diagram chasing. Commutativity means g∘f = k∘h as an equation of morphisms. If g∘f = 0, then immediately k∘h = 0 by substitution — no further information about k or h individually is needed. This is the fundamental move in a diagram chase: replace one path with another using the commutativity constraint. The power of the technique is that you can propagate known properties (like being zero, or being surjective, or having a certain kernel) across the diagram simply by following commutativity."

- question: "A proof in homological algebra invokes diagram chasing to conclude that a certain morphism must be the zero map. The diagram involves modules over a ring (a concrete abelian category). A student asks whether the same proof works for an abstract abelian category with no underlying sets. What is the correct answer?"
  type: multiple-choice
  options:
    - "No — diagram chasing requires picking elements from the objects, which is only possible in concrete categories like groups or modules"
    - "Yes — the Freyd-Mitchell embedding theorem guarantees that any small abelian category embeds fully and faithfully into a module category, so element-style diagram chases are universally valid in abelian categories"
    - "Yes, but only if the category is locally small — diagram chasing fails for large abelian categories"
    - "No — abstract abelian categories require the five lemma to be reproved from scratch without elements"
  answer: 1
  explanation: "The Freyd-Mitchell embedding theorem is precisely the justification for element-style diagram chasing in abstract abelian categories. It states that any small abelian category can be fully and faithfully embedded into the category of left R-modules for some ring R. 'Fully and faithfully' means the embedding preserves all categorical structure: isomorphisms, exact sequences, limits, colimits. So any element-level argument valid in module categories transfers unchanged to the abstract setting. In practice, algebraic topologists and algebraic geometers write diagram chases in terms of elements with the implicit understanding that Freyd-Mitchell justifies this — they do not need to reprove everything in purely morphism-level language."

- question: "A commutative diagram asserts that any two directed paths between the same pair of objects, when their morphisms are composed, yield the same composite morphism."
  type: true-false
  answer: true
  explanation: "This is the definition of a commutative diagram. For a simple square with f: A→B, g: B→D, h: A→C, k: C→D, commutativity means g∘f = k∘h — both paths from A to D agree. For more complex diagrams with multiple squares or triangles, commutativity asserts this equality for every pair of objects connected by multiple paths. The entire technique of diagram chasing rests on this: when you reach object D via one path and know the result, you can substitute the other path (which may land somewhere more convenient for your argument) and obtain the same result."

- question: "Diagram chasing only works for diagrams composed of squares; triangular diagrams require a different technique because there is only one path between most pairs of objects."
  type: true-false
  answer: false
  explanation: "Diagram chasing applies to any commutative diagram, regardless of shape. In a commutative triangle A→B→C and A→C, commutativity asserts that the two paths from A to C agree: h∘g = f (where f: A→C, g: A→B, h: B→C). This is a usable constraint — knowing a morphism is zero or has a certain property along one path immediately constrains the other. Complex diagrams in homological algebra often combine squares, triangles, and longer sequences; chasing elements through them uses the same move repeatedly: follow one path, use commutativity to switch to another path, apply hypotheses about specific morphisms, and conclude."

- question: "In your own words, describe how diagram chasing works: starting from a known element or property in one object, how do you use commutativity to derive a conclusion about a different morphism or object?"
  type: short-answer
  answer: "You begin by choosing an element x in some object A (or a morphism with a known property). You then apply a morphism to move x to another object — say f(x) in B. At each step, you look for an alternative path through the diagram that connects the same objects: commutativity guarantees the other path produces the same result. By alternating between paths, you can route x through morphisms whose properties you know (injectivity, surjectivity, being zero) to conclude something about morphisms or elements that were initially unknown. For example: if x maps to zero along one route (g∘f(x) = 0), commutativity tells you it also maps to zero along the other route (k∘h(x) = 0); if k is injective, that forces h(x) = 0; if h is surjective, then x must have come from somewhere, placing a constraint back on A."
  explanation: "The general structure of a diagram chase is: assume something about an element at one corner → apply morphisms to move it through the diagram → use commutativity to swap paths → use injectivity/surjectivity/exactness hypotheses at each step → conclude a property at another corner. The Snake Lemma and Five Lemma are both proved entirely by this technique, and their proofs are the best exercises for internalizing it."
```

## Explainer

You already know what categories and morphisms are — objects connected by arrows that compose associatively with identity arrows at every object. A **commutative diagram** is simply a picture of a category (or a functor's image) where the assertion is: any two paths between the same pair of objects, composed along their arrows, give the same morphism. For example, if there are arrows f: A → B, g: B → D, and h: A → C, k: C → D, then the square "commutes" if g ∘ f = k ∘ h. The diagram is a visual encoding of equational constraints on morphisms.

**Diagram chasing** is the proof technique that exploits commutativity to deduce new facts. The idea is simple: you want to show that some morphism has a certain property (is zero, is an isomorphism, is unique, etc.). You start at a known object and "chase" across the diagram by substituting one path for another using commutativity, applying hypotheses about specific morphisms as you go. In abelian categories (like the category of abelian groups, or R-modules), you can reason about elements explicitly — an element x in object A can be "chased" through a morphism f to land at f(x) in B, then through g to reach g(f(x)) = (g∘f)(x) in D. The commutativity constraint then says this is the same as k(h(x)). By following the element x along every available path, you uncover what constraints the diagram imposes.

The technique becomes powerful for proving structural theorems in homological algebra. The **five lemma** and the **snake lemma** (which you'll encounter soon) are proved entirely by diagram chasing: assume some maps are isomorphisms or have trivial kernel, then chase elements through the commutative squares to show other maps must also be isomorphisms or have some property. The argument always has the same shape: take an element with some property in one object, chase it along one path to land somewhere, chase it along another path to land somewhere else, use commutativity to equate the two, use injectivity or surjectivity of specific maps to conclude it must be zero or have a preimage.

What makes diagram chasing elegant is that it works purely from the categorical structure — the names of the objects don't matter, only the arrows and their commutativity relations. In an arbitrary abelian category, you cannot literally "pick an element" (there may be no underlying sets), but a theorem by Mitchell (the **Freyd-Mitchell embedding theorem**) guarantees that any small abelian category can be fully faithfully embedded into a category of modules, so element-style arguments remain valid. In practice, most chasing proofs in algebraic topology, homological algebra, and algebraic geometry are written informally in terms of elements, with the understanding that the argument is really a morphism-level statement in the underlying category.
