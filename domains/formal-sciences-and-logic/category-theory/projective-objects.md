---
id: projective-objects
title: Projective Objects and Projective Covers
domain: formal-sciences-and-logic
course: category-theory
prerequisites:
- id: additive-categories
  type: hard
- id: free-objects
  type: soft
builds-toward:
- derived-functors
- homological-dimension-intro
tags:
- homological-algebra
- universal-properties
- lifts
stage: expert
status: validated
---

# Projective Objects and Projective Covers

## Core Idea
An object P is projective if Hom(P, −) preserves epimorphisms, equivalently, if every morphism P → C/B lifts to a morphism P → C. Projectives are dual to injectives and generalize free modules. In Module categories, projectives are direct summands of free modules. Every object has a projective cover, a surjection from a projective object with 'minimal kernel'.

## Questions

```yaml
- question: "Let P be a projective R-module, e: C ↠ B a surjective module homomorphism, and f: P → B a module map. What does the projective property guarantee?"
  type: multiple-choice
  options:
    - "There exists a surjection g: C ↠ P such that f ∘ g = e"
    - "The module C must also be projective whenever P maps into B via a surjection from C"
    - "There exists a homomorphism f̃: P → C such that e ∘ f̃ = f, i.e., the map f lifts through the surjection e"
    - "The kernel of e is isomorphic to P as an R-module"
  answer: 2
  explanation: "The defining property of a projective object is the lifting property: given any epimorphism e: C ↠ B and any morphism f: P → B, there exists a morphism f̃: P → C making the triangle commute (e ∘ f̃ = f). The map from P to B can always be 'lifted' to a map from P to C passing through the surjection. This says nothing about C being projective, about the kernel of e, or about maps in the reverse direction — it is purely about the existence of a compatible lift."

- question: "Over a general commutative ring R (not necessarily a principal ideal domain), which statement about projective and free modules is correct?"
  type: multiple-choice
  options:
    - "Projective and free are synonymous in any module category — 'projective' is just an abstract name for 'free'"
    - "Every free module is projective, but projective modules need not be free — they are precisely the direct summands of free modules"
    - "Every projective module is free, but not all free modules are projective over non-commutative rings"
    - "Projective modules are the quotients of free modules, making them strictly weaker than free modules"
  answer: 1
  explanation: "Every free module is projective (an explicit lift can always be constructed using the basis). But over general rings, projective-but-not-free modules exist: M is projective if and only if there exists N such that M ⊕ N is free — M is a direct summand of a free module, but need not be free itself. Over a PID like ℤ, every projective module is free. The Serre-Swan theorem gives geometric content to the distinction: finitely generated projective modules over C(X) correspond to vector bundles over X, and non-trivial vector bundles are projective-but-not-free."

- question: "Projective objects and injective objects are categorical duals: the definition of each is obtained from the other by reversing all arrows, replacing surjections with injections, and lifts with extensions."
  type: true-false
  answer: true
  explanation: "An injective object I satisfies: for every monomorphism m: A ↪ B and any map f: A → I, there exists an extension f̃: B → I with f̃ ∘ m = f. Comparing with the projective definition (lifting through epimorphisms) reveals the precise categorical duality — the direction of the diagram's 'given' morphisms reverses, epimorphisms become monomorphisms, and lifting (factoring P → B through C ↠ B) becomes extending (factoring A → I through A ↪ B). Passing to the opposite category converts projective definitions into injective ones and vice versa."

- question: "Every abelian category has enough projective objects, so projective resolutions and minimal projective covers are universally available tools in homological algebra."
  type: true-false
  answer: false
  explanation: "Projective covers — and even projective objects — do not exist in every abelian category. The category of sheaves on a topological space is a standard example of an abelian category that in general lacks enough projectives (and often lacks projective covers entirely). Projective resolutions are available in module categories over rings (which have enough projectives), but this is a special property, not a universal feature of abelian categories. When projective covers do not exist, one typically works with injective resolutions instead, or accepts non-minimal projective resolutions."

- question: "Explain why the projective lifting property makes projective modules the natural building blocks for resolutions used in homological algebra."
  type: short-answer
  answer: "To compute derived functors (like Tor and Ext), you need to replace a module M with a resolution consisting of objects on which functors behave simply — specifically, objects where applying Hom(−, N) or (−) ⊗ N preserves exactness. Projective modules are precisely those on which Hom(P, −) preserves epimorphisms (the defining lifting property), meaning exact sequences remain exact after applying Hom(P, −). By replacing M with a projective resolution P₀ ← P₁ ← P₂ ← ⋯ and applying the functor of interest, you can read off the derived functors from the cohomology of the resulting complex. The lifting property ensures that morphisms between modules can always be compared through projective objects, making projective resolutions the canonical tool for measuring how far a functor deviates from exactness."
  explanation: "This is why projective covers and minimal projective resolutions (where each Pᵢ is as small as possible, with a superfluous kernel) are particularly useful: they give the most economical way to resolve M, producing the sharpest invariants."
```

## Explainer

From your study of free objects, you know that free modules have a remarkable property: given any surjection M → N and any map F → N from a free module F, there exists a map F → M that makes the diagram commute — the map can always be "lifted." **Projective objects** are defined by exactly this lifting property, generalized to arbitrary additive or abelian categories without requiring the object to be free in any literal sense.

The definition is this: an object P is **projective** if for every epimorphism e: C ↠ B and every morphism f: P → B, there exists a morphism f̃: P → C such that e ∘ f̃ = f. The map f̃ is the lift — it reaches through the surjection and lands in the "larger" object C rather than the quotient B. Equivalently, the functor **Hom(P, −)** preserves epimorphisms: whenever C → B is surjective, the induced map Hom(P, C) → Hom(P, B) is also surjective. This is the categorical dual of the definition of **injective objects**, where it is Hom(−, I) that preserves monomorphisms. Projective and injective objects are mirror images — the duality of "surjections lift in" versus "injections extend out."

In the category of R-modules, projective modules are precisely the **direct summands of free modules**: M is projective if and only if there exists a module N such that M ⊕ N is free. Over a field, every module is free and hence projective. Over ℤ (a principal ideal domain), every projective module is in fact free — the two notions coincide for PIDs. Over more general rings, projective-but-not-free modules exist and are geometrically meaningful. The finitely generated projective modules over the ring of continuous functions on a compact space are exactly the **vector bundles** over that space (Serre-Swan theorem). A vector bundle that becomes trivial when you add a trivial bundle is algebraically a projective module that becomes free when summed with a free module — the projective condition captures stable triviality.

The **projective cover** of an object M is a surjection P ↠ M from a projective object P such that the kernel is **superfluous** — removing it cannot produce a smaller projective surjecting onto M. Projective covers are the minimal projective objects that map onto M, and they provide canonical **minimal projective resolutions**: exact sequences 0 ← M ← P₀ ← P₁ ← P₂ ← ··· where each Pᵢ is projective and as small as possible. These resolutions are the raw material for **derived functors** such as Tor and Ext — which measure how far a functor deviates from exactness and encode deep information about the module structure of a ring. Not every abelian category has projective covers (sheaves often lack them), but in the module categories where they exist, minimal projective resolutions are the canonical tool for homological computation.
