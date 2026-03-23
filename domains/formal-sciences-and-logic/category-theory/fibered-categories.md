---
id: fibered-categories
title: Fibered Categories
domain: formal-sciences-and-logic
course: category-theory
prerequisites:
- id: comma-categories
  type: hard
- id: functor-categories
  type: hard
- id: two-categories
  type: soft
- id: opposite-categories-and-duality
  type: soft
builds-toward:
- grothendieck-construction
tags:
- fibered category
- fibration
- cartesian morphism
- Grothendieck fibration
- descent
- cleavage
stage: expert
status: draft
---
# Fibered Categories

## Core Idea
A fibered category (or Grothendieck fibration) over a base category B is a functor p: E → B such that for every morphism f: b → b' in B and object e' in E with p(e') = b', there exists a cartesian morphism (or cartesian lifting) φ: e → e' with p(φ) = f, satisfying a universal property. Intuitively, E is a "family of categories parametrized by B": the fiber E_b = p^{-1}(b) is the category sitting over each object b, and cartesian morphisms provide canonical ways to pull back along morphisms in B. Fibered categories formalize the notion of "varying algebraic/geometric structure over a base" and are central to descent theory, stacks, and the Grothendieck construction.

## How It's Best Learned
Consider the codomain fibration cod: Arr(C) → C sending each arrow f: A → B to its codomain B. The fiber over B is the slice category C/B. A cartesian morphism is a pullback square. Verify the universal property of cartesian liftings in this example. Then consider the category of vector bundles over a base space, where the fiber functor sends each bundle to its base space—pullback of bundles provides the cartesian liftings.

## Common Misconceptions
- A fibered category is not the same as a functor to Cat; the Grothendieck construction provides the precise correspondence, but a fibration is a single functor p: E → B, not a diagram of categories.
- Cartesian morphisms are not simply morphisms in the total category; they must satisfy a universal property relative to the projection functor.
- A cleavage (choice of cartesian liftings) is not unique; different cleavages give equivalent structures, and a split fibration is one where the cleavage is strictly functorial.

## Questions

```yaml
- question: "In the codomain fibration cod: Arr(C) → C, morphisms are commutative squares. Under what condition is a commutative square a cartesian morphism?"
  type: multiple-choice
  options:
    - "When the square is commutative — any commutative square is automatically cartesian in the codomain fibration"
    - "When the horizontal arrows of the square are isomorphisms"
    - "When the square is a pullback square — satisfying the universal property that any competing morphism factors uniquely through it"
    - "When the domain objects of the top and bottom arrows coincide"
  answer: 2
  explanation: "In the codomain fibration, a morphism in Arr(C) is cartesian if and only if it is a pullback square. This is the key example making the abstract definition concrete: the universal property of a cartesian morphism — any morphism in E with the same base morphism in B factors uniquely through it — becomes exactly the universal property of the pullback. Not every commutative square is a pullback (option A is the most common error), and isomorphisms of horizontal arrows (option B) would be a much stronger, and incorrect, condition."

- question: "What is the precise relationship between a Grothendieck fibration p: E → B and a pseudofunctor F: B^{op} → Cat?"
  type: multiple-choice
  options:
    - "They are the same structure: every fibration is a pseudofunctor and every pseudofunctor is a fibration, with no translation needed"
    - "They are equivalent via the Grothendieck construction, which provides a 2-categorical equivalence between fibrations over B and pseudofunctors B^{op} → Cat"
    - "A pseudofunctor is a special case of a fibration: every pseudofunctor gives a fibration, but not every fibration comes from a pseudofunctor"
    - "A fibration is strictly stronger: fibrations always yield split functorial compositions, which pseudofunctors only satisfy up to isomorphism"
  answer: 1
  explanation: "The Grothendieck construction gives a 2-categorical equivalence between fibrations over B and pseudofunctors B^{op} → Cat. Given a fibration, one extracts a pseudofunctor by b ↦ E_b and f ↦ f* (the pullback functor); given a pseudofunctor, one constructs the total category. They are equivalent — two different but compatible ways to describe 'a family of categories varying over B' — but not identical. A fibration is a single functor p: E → B; a pseudofunctor is a contravariant assignment B → Cat. Conflating them (option A) is the most common misconception in the topic."

- question: "In the codomain fibration cod: Arr(C) → C, the fiber over an object b ∈ C is the slice category C/b."
  type: true-false
  answer: true
  explanation: "The fiber over b consists of all objects e in Arr(C) with cod(e) = b — that is, all morphisms in C with codomain b — together with all morphisms between them that project to the identity on b. This is exactly the slice category C/b: objects are arrows f: a → b in C, and morphisms from f: a → b to g: a' → b are arrows h: a → a' making the triangle commute. The codomain fibration is the canonical first example for building intuition about fibered categories."

- question: "A fibered category p: E → B is the same mathematical object as a pseudofunctor B^{op} → Cat, so there is no need to distinguish between them."
  type: true-false
  answer: false
  explanation: "A fibration p: E → B is a single functor satisfying the cartesian lifting property. A pseudofunctor F: B^{op} → Cat is a contravariant assignment of categories and functors to objects and morphisms of B. They are *equivalent* structures via the Grothendieck construction, but they are not the same object. In particular, a fibration does not come with a canonical choice of pullback functors (that requires choosing a cleavage), while a pseudofunctor specifies F(f) = f* explicitly. Most natural fibrations are not split, meaning the induced pseudofunctor satisfies (f ∘ g)* ≅ g* ∘ f* only up to coherent isomorphism, not on the nose."

- question: "Why is the universal property essential in the definition of a cartesian morphism, rather than simply requiring φ: e' → e to be any morphism in E lying over f: b' → b in B?"
  type: short-answer
  answer: "Without the universal property, there would be no canonical way to relate fibers across morphisms in B — any morphism over f would qualify as a 'lifting,' and different choices would give incompatible fiber relationships. The universal property says φ is the unique best lifting of f above a fixed target e: any other morphism ψ over a factorization of f factors uniquely through φ. This uniqueness makes the pullback functor f*: E_b → E_{b'} well-defined up to unique isomorphism, which is what makes descent theory coherent and the Grothendieck construction work."
  explanation: "If we only required existence of some morphism over f, different choices of liftings would yield non-canonically related fibers, and the pullback functors f* could not be assembled into a well-defined pseudofunctor. The universal property is precisely what characterizes each cartesian lifting uniquely (up to isomorphism), ensuring that two different cleavages give equivalent, not merely isomorphic, total categories."
```

## Explainer

From your study of comma categories and functor categories, you know how to form slice categories C/b and how to assemble categories of functors into structured wholes. Fibered categories answer a subtler organizational question: how do you talk about a *family* of categories varying over a base, where morphisms in the base tell you how to transport objects between fibers? The motivating example is geometric: over each topological space (or scheme) B, you have a category of vector bundles — small changes in the base space induce pullback operations on bundles, and those pullbacks are the "transport maps" the fibration formalizes.

Formally, a **Grothendieck fibration** is a functor p: E → B such that for every morphism f: b' → b in B and every object e in E with p(e) = b, there exists a **cartesian morphism** φ: e' → e in E with p(φ) = f, satisfying a universal lifting property. The universal property says: any morphism ψ: e'' → e in E with p(ψ) factoring through f in B factors uniquely through φ. Concretely, φ is the "best" way to lift f to E above the target e — it is canonical once the target and the base morphism are fixed. The object e' = f*(e) is the **pullback** of e along f, and this is exactly a pullback in the geometric sense when E is the category of vector bundles.

The **fiber** E_b over an object b ∈ B is the subcategory of E consisting of objects e with p(e) = b and morphisms φ with p(φ) = id_b. In the vector bundle example, E_b is the category of vector bundles on the single space b. A morphism f: b' → b in B induces a **pullback functor** f*: E_b → E_{b'}, defined (up to canonical isomorphism) by the cartesian liftings. This is where your comma-category intuition applies: the comma category b'/p in E records all ways to map into a fixed fiber. The codomain fibration cod: Arr(C) → C, sending each arrow g: A → B to its codomain B, has fiber (Arr(C))_b = C/b — precisely the slice category over b. The cartesian morphisms are exactly the pullback squares in C.

A **cleavage** is a choice, for each (f, e) pair, of a specific cartesian lifting φ_{f,e}. Different cleavages give equivalent total categories, but choosing one converts the fibration into a strict assignment b ↦ E_b and f ↦ f* that almost forms a pseudofunctor B^{op} → Cat — the composition f* ∘ g* need not equal (g ∘ f)* on the nose, only up to coherent isomorphism. A **split fibration** is one where the cleavage is strictly functorial: (g ∘ f)* = f* ∘ g* strictly. Most natural fibrations are not split, but every fibration is equivalent to a split one.

The deeper significance is the **Grothendieck construction**: there is an equivalence (more precisely, a 2-categorical equivalence) between fibrations p: E → B and pseudofunctors F: B^{op} → Cat. Given a fibration, you extract F by b ↦ E_b and f ↦ f*. Given a pseudofunctor, you build the total category E with objects (b, x) where x ∈ F(b), and morphisms (b', x') → (b, x) given by pairs (f: b' → b, α: x' → F(f)(x)). This is precisely why fibered categories are central to **descent theory**: a presheaf F: B^{op} → Set (or Cat) descends along a covering if and only if the corresponding fibration satisfies a gluing condition. Stacks are fibered categories over sites that satisfy the descent conditions, and the entire language of algebraic geometry over varying base schemes is organized through this formalism.
