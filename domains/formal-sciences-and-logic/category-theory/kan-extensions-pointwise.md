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
stage: advanced
status: draft
---

# Kan Extensions and Pointwise Formulae

## Core Idea
Given functors p: A → B and F: A → C, the right Kan extension Ran_p F: B → C is the universal functor extending F and compatible with p. When C is complete, pointwise formula holds: (Ran_p F)(b) ≅ lim_{a → b} F(a), a limit over the comma category (a ↓ b). Left Kan extensions are dual, using colimits. Pointwise formulae allow explicit computation and reveal Kan extensions as limit/colimit operations, connecting them to universal constructions.

## How It's Best Learned
Prove the pointwise formula directly from the universal property. Compute right Kan extensions along inclusion functors (restriction and pointwise limit). Study how adjoint functors arise as Kan extensions and how tensor products relate to Kan extension constructions.

## Common Misconceptions
Pointwise formula requires target completeness; without it, Kan extensions exist abstractly but cannot be computed via limits. Not every functor looking like a Kan extension satisfies the universal property. Left and right Kan extensions are fundamentally different—left uses colimits, not limits.

## Explainer

From your study of Kan extensions, you know the abstract setup: given functors p: A → B and F: A → C, the right Kan extension Ran_p F is the functor B → C that best approximates extending F along p, universal in the sense that any other such functor factors through it. The abstract universal property tells you *that* Ran_p F exists (under mild conditions) but not *what* it looks like at each point b ∈ B. The **pointwise formula** fills that gap: it gives an explicit recipe for computing the value of Ran_p F at any object.

The recipe is: **(Ran_p F)(b) ≅ lim_{(a, p(a)→b)} F(a)**, a limit taken over the **comma category** (p ↓ b). The comma category (p ↓ b) has objects (a, f) where a ∈ A and f: p(a) → b is a morphism in B, and morphisms are maps a → a' in A that make the triangle over b commute. Intuitively: you look at all the objects in A whose image under p "reaches" b, and then take a limit of F over all of them. When p(a) = b exactly (like a restriction along an inclusion), the formula specializes to a limit over the fiber — giving back the expected behavior for restriction functors.

The dual statement holds for left Kan extensions using colimits over the opposite comma category: **(Lan_p F)(b) ≅ colim_{(a, b→p(a))} F(a)**. The asymmetry is conceptually important: a right Kan extension aggregates all A-objects that map *to* b under p (a limit that "projects"), while a left Kan extension aggregates all A-objects that b maps *to* under p (a colimit that "generates"). Right extensions are conservative and limit-like; left extensions are expansive and colimit-like.

Two canonical applications make the pointwise formula concrete. First, **restriction and extension of presheaves**: given an inclusion i: C → D of categories, restricting a presheaf F: D^op → Set along i gives the right Kan extension Ran_i F — and the formula says its value at each d ∈ D is the limit of F over all C-objects reachable from d. This is the right Kan extension as a "sheaf extension." Second, **adjoint functors as Kan extensions**: if F ⊣ G, then G = Ran_F Id_C and F = Lan_G Id_D, expressing every adjoint pair as a Kan extension of the identity. The pointwise formula in this case says G(b) = lim_{(Fc → b)} c — the limit over the comma category of F descending to b, which is exactly the adjoint's universal property in disguise. This reveals Kan extensions as the most general notion of which adjunctions are a special case.
