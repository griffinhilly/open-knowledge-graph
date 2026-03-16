---
id: grothendieck-construction
title: The Grothendieck Construction
domain: formal-sciences-and-logic
course: category-theory
prerequisites:
- id: fibered-categories
  type: hard
- id: natural-transformations
  type: hard
- id: functor-categories
  type: soft
- id: comma-categories
  type: soft
- id: product-topology
  type: soft
tags:
- Grothendieck construction
- pseudofunctor
- total category
- fibration equivalence
- category of elements
- lax colimit
stage: advanced
status: draft
---
# The Grothendieck Construction

## Core Idea
The Grothendieck construction transforms a (pseudo)functor F: B → Cat into a single fibered category ∫F (the total category) equipped with a projection p: ∫F → B. Objects of ∫F are pairs (b, x) where b is an object of B and x is an object of F(b); a morphism (b, x) → (b', x') is a pair (f, φ) where f: b → b' in B and φ: F(f)(x) → x' in F(b'). This construction establishes an equivalence between pseudofunctors B → Cat and fibered categories over B, providing a bridge between "indexed" and "fibered" perspectives on families of categories. For set-valued functors F: C → Set, the Grothendieck construction yields the category of elements ∫F, and the Yoneda lemma can be rephrased as a statement about this category.

## How It's Best Learned
Start with a functor F: C → Set for a small category C (e.g., a presheaf on a poset). Build the category of elements ∫F explicitly: list all pairs (c, x ∈ F(c)) as objects and all morphisms induced by arrows in C. Verify this gives a category fibered over C. Then generalize to a pseudofunctor to Cat and understand how the morphism definition accounts for the pseudofunctorial coherence data.

## Common Misconceptions
- The Grothendieck construction for Set-valued functors (category of elements) and the general Cat-valued version are related but not identical; the Set version is a special case where each fiber is a discrete category.
- The equivalence between pseudofunctors and fibrations is an equivalence of 2-categories, not merely a bijection; the 2-categorical structure (with pseudonatural transformations and modifications) is essential.
- The total category ∫F is not the disjoint union of the fibers; the morphisms in ∫F encode how the fibers are connected via the action of F on morphisms in the base.

## Explainer

From fibered categories, you know the idea of a category E fibered over a base B: morphisms in E decompose into vertical parts (within fibers) and horizontal parts (Cartesian lifts that transport objects along morphisms in the base). From natural transformations, you're comfortable with coherent families of maps between functors. The Grothendieck construction starts from the opposite side: you have a **pseudofunctor** F: B → Cat that assigns a category F(b) to each object b of B and a functor F(f): F(b) → F(b') to each morphism f: b → b', with coherence isomorphisms for composition (not strict equalities — hence "pseudo"). The construction assembles all these fibers into one total category ∫F, recovering the fibered-category picture.

The **objects of ∫F** are pairs (b, x) where b ∈ B and x ∈ F(b) — an index paired with an element of the fiber at that index. Think of B as a parameter space and F(b) as the collection of things parametrized by b. A **morphism** (b, x) → (b', x') in ∫F is a pair (f, φ) where f: b → b' is a morphism in B and φ: F(f)(x) → x' is a morphism in the *target* fiber F(b'). The reindexing functor F(f) transports x from the source fiber F(b) to the target fiber F(b'), and then φ is an additional internal morphism in F(b'). This asymmetric structure — reindex first, then move inside the fiber — is what makes ∫F a genuine category with associative composition.

The simplest special case is F: C → Set, a **set-valued functor** (presheaf). Each fiber F(c) is a set, so morphisms within fibers can only be identities. The total category ∫F is the **category of elements**: objects are pairs (c, x) with x ∈ F(c), and a morphism (c, x) → (c', x') is just an arrow f: c → c' in C such that F(f)(x) = x' (the φ component is forced to be the identity). The Yoneda lemma rephrases neatly: natural transformations Hom(c, −) → F biject with elements of F(c), and each such element corresponds to a functor from the terminal object in the category of elements of Hom(c, −) to ∫F over C.

The Grothendieck construction establishes a genuine **equivalence of 2-categories**: pseudofunctors B → Cat are equivalent to Grothendieck fibrations over B. In one direction: given F, construct ∫F and observe that the projection p: ∫F → B sending (b, x) ↦ b is a fibration — the Cartesian morphisms are precisely the pairs (f, id_{F(f)(x)}), which lift f by reindexing with no internal displacement. In the other direction: given a fibration p: E → B, define F(b) = p^{−1}(b) (the fiber over b as a category), and F(f) = "pull back along f" using the chosen Cartesian lifts. The pseudofunctoriality coherence isomorphisms arise from the non-uniqueness of Cartesian lifts (they are unique only up to unique vertical isomorphism). The equivalence is of 2-categories: pseudonatural transformations between pseudofunctors correspond to morphisms of fibrations over B (functors that preserve Cartesian morphisms), and modifications correspond to natural transformations between such functors.

The Grothendieck construction appears throughout higher-dimensional category theory and homotopy theory. In the **∞-categorical** setting, it generalizes to the straightening/unstraightening equivalence between ∞-functors C → ∞-Grpd and left fibrations over C — the foundation of the theory of ∞-categories of presheaves. In **homotopy type theory**, the construction corresponds to the type-theoretic notion of a dependent type: the total type Σ(b:B) F(b) is the Grothendieck construction of the type family F. Recognizing the Grothendieck construction pattern — "fiber over each object, with reindexing along morphisms" — gives you a unified language for fibered, dependent, and parametrized structures across mathematics.
