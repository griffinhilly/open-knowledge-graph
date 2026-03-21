---
id: monomorphisms-epimorphisms
title: Monomorphisms and Epimorphisms
domain: formal-sciences-and-logic
course: category-theory
prerequisites:
- id: categories-and-morphisms
  type: hard
builds-toward:
- additive-categories
- abelian-structure-properties
tags:
- morphisms
- universal-properties
- categorical-structure
stage: advanced
status: draft
---

# Monomorphisms and Epimorphisms

## Core Idea
Monomorphisms generalize injective functions to arbitrary categories: a morphism f: A → B is monic if whenever gf = hf, then g = h. Epimorphisms are the dual concept, generalizing surjections. In categories without a notion of elements, these abstract properties capture injectivity and surjectivity without requiring explicit set-theoretic membership.

## How It's Best Learned
Start in Set and Ring where monomorphisms are exactly injections and epimorphisms are exactly surjections. Then explore categories where these concepts diverge—for example, in rings the natural homomorphism R → R[x] is epic but not surjective.

## Common Misconceptions
Assuming monomorphisms are always injective (false in general). Thinking epimorphisms must be surjective (counterexample: R → R[x] in Ring). Assuming every morphism is either monic or epic.

## Questions

```yaml
- question: "In the category Ring of rings with ring homomorphisms, the inclusion ι: ℤ → ℚ is an epimorphism. Why, even though ℚ contains elements (non-integer rationals) that ι never reaches?"
  type: multiple-choice
  options:
    - "Because ι is surjective onto a dense subset of ℚ, and dense maps are always epimorphisms"
    - "Because any ring homomorphism f: ℚ → R is completely determined by its value on ℤ, so if g ∘ ι = h ∘ ι then g = h everywhere on ℚ"
    - "Because ℤ and ℚ are isomorphic as abelian groups, making the inclusion an isomorphism"
    - "Because epimorphism in Ring just means the map has dense image, which ι has"
  answer: 1
  explanation: "Epimorphism means right-cancellability: g ∘ ι = h ∘ ι implies g = h. For ring homomorphisms out of ℚ, if g and h agree on all integers, they must agree on all rationals: f(p/q) = f(p) · f(q)^{−1} is forced by the homomorphism axioms, and f(p) is determined by f(1). So any two ring homomorphisms ℚ → R that agree on ℤ must be identical — ι is right-cancellable. This shows epimorphism is NOT about surjectivity; it's about whether morphisms out of the codomain are uniquely determined by precomposition. Dense image (option D) is the correct characterization in Top (topological spaces), not Ring."

- question: "A morphism f: A → B in a category is a monomorphism if and only if it has a left inverse (a morphism g: B → A with g ∘ f = id_A)."
  type: multiple-choice
  options:
    - "True — only morphisms with left inverses satisfy the left-cancellability condition"
    - "False — having a left inverse (being a split monomorphism) is sufficient for being monic, but not necessary; there are monomorphisms without left inverses"
    - "True — in any category, monic and split monic are equivalent concepts"
    - "False — left inverses make morphisms epic, not monic"
  answer: 1
  explanation: "Having a left inverse implies being monic (split monics are monic), but the converse fails. In Ab, the inclusion ℤ → ℚ is monic (injective) but has no left inverse as an abelian group homomorphism — any homomorphism ℚ → ℤ must send 1/n to an element r with n·r = 1 in ℤ, which is impossible for n > 1. The monomorphism condition (left-cancellability: f ∘ g = f ∘ h ⟹ g = h) is strictly weaker than having a left inverse. Confusing the two is a common error when moving from Set (where all injections split) to general categories."

- question: "In the category Set, every epimorphism is surjective."
  type: true-false
  answer: true
  explanation: "In Set, epimorphisms coincide exactly with surjective functions. If f: A → B is not surjective, there exists an element b ∈ B not in the image of f. Define two functions g, h: B → {0,1} where g is the constant 0 function and h sends b to 1 and everything else to 0. Then g ∘ f = h ∘ f (both are constant 0 on A), but g ≠ h — so f is not right-cancellable, hence not epic. This makes Set a well-behaved category where the categorical definition aligns perfectly with the set-theoretic one."

- question: "In the category of topological spaces (Top) with continuous maps, the epimorphisms are exactly the surjective continuous maps."
  type: true-false
  answer: false
  explanation: "In Top, the epimorphisms are the *dense* continuous maps — maps whose image is dense in the codomain (every open set intersects the image) — not just the surjective ones. A surjection is always dense (and hence epic), but a dense map need not be surjective. This is the same divergence as ℤ → ℚ in Ring: the codomain is 'generated' in the appropriate sense by the image, even though the image doesn't cover every point. This example illustrates why 'epic ≠ surjective' is a structural feature of many natural categories."

- question: "Explain why category theory defines monomorphisms via left-cancellability rather than via 'no two inputs give the same output,' and what is gained by the categorical definition."
  type: short-answer
  answer: "The element-based definition ('injective: f(a) = f(b) ⟹ a = b') requires objects to have elements, which is not the case in an arbitrary category. Left-cancellability (f ∘ g = f ∘ h ⟹ g = h) is expressed entirely in terms of morphisms and composition, requiring no reference to elements. The gain is universality: the categorical definition applies to categories of sets, groups, rings, topological spaces, vector spaces, and purely abstract categories — and it reveals which properties of injectivity are truly 'structural' versus which depend on set-theoretic membership. The divergence between mono and injective in some categories (and their coincidence in others) then becomes a theorem that tells you something about the category itself."
  explanation: "This is the core move of category theory: reformulate element-dependent definitions in terms of morphisms. The result is a definition that is simultaneously more abstract and more powerful — it generalizes to settings where 'element' has no meaning and, in concrete categories, recovers the familiar notion while revealing its true algebraic content."
```

## Explainer

From your study of categories and morphisms, you know that category theory abstracts mathematical structures away from their internal elements, describing objects only through their relationships — the morphisms between them. Most concepts that feel element-dependent in familiar settings (like injectivity: "no two inputs give the same output") must be reformulated in terms of morphisms to make sense in an arbitrary category. **Monomorphisms** and **epimorphisms** are the categorical versions of injective and surjective maps, and the reformulation reveals what those concepts truly mean structurally.

A morphism f: A → B is a **monomorphism** (or *monic*) if it is **left-cancellable**: for any two morphisms g, h: C → A, if f ∘ g = f ∘ h then g = h. In Set, this coincides exactly with injectivity. Here's the intuition: if f is injective, then knowing f(g(x)) = f(h(x)) for all x forces g(x) = h(x), since different inputs can't produce the same output under an injective map. The categorical definition extracts this "information-preserving" property without ever mentioning elements. A monomorphism is a morphism through which you can distinguish the domain — you cannot "compress" information passing through it. Dually, f: A → B is an **epimorphism** (or *epic*) if it is **right-cancellable**: for any g, h: B → C, if g ∘ f = h ∘ f then g = h. In Set, surjectivity ensures this: if f hits every element of B, then any two functions that agree on all outputs of f must agree everywhere on B.

The surprise is that these concepts **diverge from injectivity/surjectivity** outside of Set. In the category **Ring** (with ring homomorphisms), the inclusion ι: ℤ → ℚ is an epimorphism even though it is far from surjective. The reason: any ring homomorphism f: ℚ → R is entirely determined by f(1) (since f(p/q) = f(p)/f(q) by homomorphism axioms, and f(p) is determined by f(1)). So if g ∘ ι = h ∘ ι — meaning g and h agree on all integers — they must agree on all rationals. Right-cancellability holds, so ι is epic. Yet ℚ has elements (non-integer rationals) that ι never reaches. This shows that epimorphism is *not* about surjectivity; it's about whether morphisms out of the codomain are uniquely determined by composition with f.

Understanding where mono/epic do and don't coincide with injective/surjective is important for each category you work in. In **Ab** (abelian groups) and more generally in any abelian category, the coincidence is restored: monomorphisms are exactly injections (kernel = 0) and epimorphisms are exactly surjections (cokernel = 0), with the natural notion of image and coimage defined via universal properties. This is part of why abelian categories are so well-behaved for homological algebra. In topological spaces, monomorphisms are again injections, but epimorphisms are *dense* continuous maps (not necessarily surjective). The categorical definitions thus serve as diagnostic tools: when mono ≠ injective or epic ≠ surjective in a given category, it reveals something structural about that category's morphisms — and understanding this divergence is the first step toward the richer theory of abelian and additive categories you'll study next.
