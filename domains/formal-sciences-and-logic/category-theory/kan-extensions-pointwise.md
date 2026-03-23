---
id: kan-extensions-pointwise
title: Kan Extensions and Pointwise Formulae
domain: formal-sciences-and-logic
course: category-theory
prerequisites:
- id: kan-extensions
  type: hard
- id: limits-and-colimits
  type: hard
builds-toward:
- topos-theory-intro
tags:
- kan-extension
- pointwise
- limit
- colimit
- universal
stage: expert
status: draft
---

# Kan Extensions and Pointwise Formulae

## Core Idea
Given functors p: A → B and F: A → C, the right Kan extension Ran_p F: B → C is the universal functor extending F and compatible with p. When C is complete, pointwise formula holds: (Ran_p F)(b) ≅ lim_{a → b} F(a), a limit over the comma category (a ↓ b). Left Kan extensions are dual, using colimits. Pointwise formulae allow explicit computation and reveal Kan extensions as limit/colimit operations, connecting them to universal constructions.

## How It's Best Learned
Prove the pointwise formula directly from the universal property. Compute right Kan extensions along inclusion functors (restriction and pointwise limit). Study how adjoint functors arise as Kan extensions and how tensor products relate to Kan extension constructions.

## Common Misconceptions
Pointwise formula requires target completeness; without it, Kan extensions exist abstractly but cannot be computed via limits. Not every functor looking like a Kan extension satisfies the universal property. Left and right Kan extensions are fundamentally different—left uses colimits, not limits.

## Questions

```yaml
- question: "The pointwise formula for the right Kan extension computes (Ran_p F)(b) as a limit over the comma category (p ↓ b). What are the objects of this comma category?"
  type: multiple-choice
  options:
    - "All objects b' in B such that there exists a morphism b → b' in B"
    - "All pairs (a, f) where a is an object in A and f: p(a) → b is a morphism in B"
    - "All morphisms in B with codomain b, regardless of their domain"
    - "Only the objects a in A for which p(a) = b exactly (the strict fiber of p over b)"
  answer: 1
  explanation: "The comma category (p ↓ b) has as objects all pairs (a, f) where a ∈ A and f: p(a) → b is a morphism in B. Morphisms in (p ↓ b) are maps α: a → a' in A such that the triangle commutes: f' ∘ p(α) = f. Intuitively, this captures all objects of A whose image under p 'reaches' b via some morphism in B — not just those mapping exactly to b. Option D describes the strict fiber, which is a special case when only identity morphisms are considered. The full comma category is needed for the general formula."

- question: "Which condition is required for the pointwise formula (Ran_p F)(b) ≅ lim_{(p↓b)} F to give a concrete computation of the right Kan extension?"
  type: multiple-choice
  options:
    - "The functor p: A → B must be a full embedding (fully faithful inclusion)"
    - "The category C (the target of F) must have all small limits"
    - "The category A must be a discrete category (no non-identity morphisms)"
    - "The functor F must be a representable presheaf"
  answer: 1
  explanation: "The pointwise formula requires taking a limit over the comma category (p ↓ b) in the category C. For this limit to exist for every b ∈ B, C must be complete — it must have all small limits. Without completeness, the Kan extension may still exist (the universal property can be satisfied abstractly), but the pointwise formula fails to provide a concrete computation: you cannot 'compute' the value at b because the required limit doesn't exist in C. This is why the Common Misconceptions section emphasizes: without completeness of C, Kan extensions exist abstractly but cannot be computed via limits."

- question: "The left Kan extension Lan_p F is computed by the same pointwise formula as the right Kan extension, but using limits over the opposite comma category (b ↓ p) instead of (p ↓ b)."
  type: true-false
  answer: false
  explanation: "The left Kan extension uses colimits, not limits, and over a different comma category. The correct formula is (Lan_p F)(b) ≅ colim_{(b ↓ p)} F(a), where the comma category (b ↓ p) has objects (a, f: b → p(a)). The asymmetry is conceptual: a right Kan extension 'projects' by taking limits over objects whose image reaches b from A (all p(a) with morphisms to b); a left Kan extension 'generates' via colimits over objects that b can reach in B (all p(a) with morphisms from b). Substituting limits for colimits would change right to left and vice versa — they are fundamentally dual, not identical with a small modification."

- question: "Every adjoint pair (F ⊣ G) can be expressed as a pair of Kan extensions of identity functors, making adjunctions a special case of Kan extensions."
  type: true-false
  answer: true
  explanation: "This is one of the deepest results connecting Kan extensions to the rest of category theory. Given an adjunction F ⊣ G with F: C → D and G: D → C, we have G = Ran_F Id_C (the right Kan extension of the identity on C along F) and F = Lan_G Id_D (the left Kan extension of the identity on D along G). The pointwise formula in this case gives G(b) = lim_{(Fc → b)} c — a limit over the comma category of F descending to b — which is precisely the universal property of the right adjoint. Kan extensions generalize adjunctions: every adjunction is a Kan extension, but not every Kan extension is an adjunction."

- question: "Explain why the pointwise formula for Kan extensions requires the target category C to be complete, and what 'fails' if C lacks the necessary limits."
  type: short-answer
  answer: "The pointwise formula (Ran_p F)(b) ≅ lim_{(p↓b)} F(a) defines the value of the Kan extension at each object b by taking a limit of F over the comma category (p ↓ b). This limit must exist in C for every b ∈ B. If C is not complete, some of these limits may not exist in C, so the formula fails to define a functor. The Kan extension itself may still exist — it can be defined by its universal property (a natural transformation with a universal factorization property) even when C lacks limits — but without completeness, this abstract existence does not translate into an explicit computation at each point. The pointwise formula is a computational tool, not the definition of the Kan extension."
  explanation: "The distinction between 'exists abstractly via universal property' and 'can be computed pointwise via limits' is central to Kan extension theory. Completeness is what makes the abstract definition constructive. In practice, target categories like Set, Ab, and vector spaces are complete, which is why Kan extensions are routinely computable in algebraic and geometric contexts. When working in categories without all limits (like categories of smooth manifolds or certain homotopy categories), Kan extensions require more care and the pointwise formula cannot be applied directly."
```

## Explainer

From your study of Kan extensions, you know the abstract setup: given functors p: A → B and F: A → C, the right Kan extension Ran_p F is the functor B → C that best approximates extending F along p, universal in the sense that any other such functor factors through it. The abstract universal property tells you *that* Ran_p F exists (under mild conditions) but not *what* it looks like at each point b ∈ B. The **pointwise formula** fills that gap: it gives an explicit recipe for computing the value of Ran_p F at any object.

The recipe is: **(Ran_p F)(b) ≅ lim_{(a, p(a)→b)} F(a)**, a limit taken over the **comma category** (p ↓ b). The comma category (p ↓ b) has objects (a, f) where a ∈ A and f: p(a) → b is a morphism in B, and morphisms are maps a → a' in A that make the triangle over b commute. Intuitively: you look at all the objects in A whose image under p "reaches" b, and then take a limit of F over all of them. When p(a) = b exactly (like a restriction along an inclusion), the formula specializes to a limit over the fiber — giving back the expected behavior for restriction functors.

The dual statement holds for left Kan extensions using colimits over the opposite comma category: **(Lan_p F)(b) ≅ colim_{(a, b→p(a))} F(a)**. The asymmetry is conceptually important: a right Kan extension aggregates all A-objects that map *to* b under p (a limit that "projects"), while a left Kan extension aggregates all A-objects that b maps *to* under p (a colimit that "generates"). Right extensions are conservative and limit-like; left extensions are expansive and colimit-like.

Two canonical applications make the pointwise formula concrete. First, **restriction and extension of presheaves**: given an inclusion i: C → D of categories, restricting a presheaf F: D^op → Set along i gives the right Kan extension Ran_i F — and the formula says its value at each d ∈ D is the limit of F over all C-objects reachable from d. This is the right Kan extension as a "sheaf extension." Second, **adjoint functors as Kan extensions**: if F ⊣ G, then G = Ran_F Id_C and F = Lan_G Id_D, expressing every adjoint pair as a Kan extension of the identity. The pointwise formula in this case says G(b) = lim_{(Fc → b)} c — the limit over the comma category of F descending to b, which is exactly the adjoint's universal property in disguise. This reveals Kan extensions as the most general notion of which adjunctions are a special case.
