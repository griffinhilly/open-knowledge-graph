---
id: two-categories-and-weak-functors
title: 2-Categories and Weak Functors
domain: formal-sciences-and-logic
course: category-theory
prerequisites:
- id: categories-and-morphisms
  type: hard
- id: functors
  type: hard
- id: natural-transformations
  type: hard
tags:
- higher-categories
- two-categories
- weak-functors
- natural-transformations
stage: expert
status: validated
---

# 2-Categories and Weak Functors

## Core Idea
A 2-category consists of objects, morphisms (1-cells) between objects, and 2-morphisms (2-cells) between morphisms, with composition operations at both levels. Weak (or lax) functors between 2-categories preserve the 2-categorical structure up to invertible 2-morphisms, generalizing both ordinary functors and natural transformations. This framework encompasses categories, functors, and natural transformations as a single 2-categorical structure.

## How It's Best Learned
Study the 2-category Cat of all categories, functors, and natural transformations. Understand how ordinary categories and functors sit inside this structure. Explore other 2-categories: 2-categories arising from partial orders, from rings, and from algebraic structures.

## Common Misconceptions
In a 2-category, 2-morphisms need not have inverses; strict equality of compositions is replaced by isomorphism. Weak functors are less restrictive than strict functors and are often more natural, but this requires care in applications.

## Questions

```yaml
- question: "In the 2-category Cat, what play the roles of 0-cells, 1-cells, and 2-cells respectively?"
  type: multiple-choice
  options:
    - "Categories, functors, and natural transformations"
    - "Objects, morphisms, and functors between categories"
    - "Sets, functions, and natural transformations between them"
    - "Functors, natural transformations, and modifications between natural transformations"
  answer: 0
  explanation: "Cat is the canonical example of a strict 2-category. Its 0-cells are categories (the 'objects' at the top level), its 1-cells are functors between categories (the 'morphisms'), and its 2-cells are natural transformations between functors. Composition of 1-cells is functor composition (strictly associative), and composition of 2-cells is vertical composition of natural transformations. The 2-categorical framework unifies these three layers — which were previously described separately — into a single coherent structure where categorical concepts like equivalence and adjunction become statements about 1-cells and 2-cells."

- question: "A mathematician observes that the functor assigning to each ring its category of modules only preserves composition 'up to natural isomorphism' rather than strictly. She concludes this construction is defective and should be replaced by one that is strictly associative. This conclusion is:"
  type: multiple-choice
  options:
    - "Wrong — most naturally occurring constructions only preserve structure up to coherent isomorphism, making weak functors the appropriate and more general framework; the failure of strict preservation is a feature of mathematical reality, not a defect"
    - "Correct — strict 2-functors are always preferable because they are easier to work with and just as expressive in all practical situations"
    - "Wrong, but only because the ring-modules construction can always be strictified with sufficient bookkeeping"
    - "Correct — if a functor fails to preserve composition strictly, it technically violates the definition of a functor and cannot be used as a 2-functor"
  answer: 0
  explanation: "In mathematics, most naturally occurring functorial constructions (tensor product of modules, pullback of sheaves, etc.) preserve composition only up to coherent isomorphism. The 2-categorical framework accommodates this through weak (pseudo) functors, which specify explicit comparison 2-cells φ_{g,f}: F(g∘f) → F(g)∘F(f) satisfying coherence conditions. This is not a compromise — it is the correct description of the mathematical reality. While strictification theorems sometimes allow replacing a weak functor with a strict equivalent, this often destroys naturality or simplicity. Weak functors are the standard, not the exception."

- question: "A strict 2-functor F between 2-categories satisfies F(g ∘ f) = F(g) ∘ F(f) exactly on the nose, whereas a weak 2-functor only guarantees an invertible 2-cell F(g ∘ f) ≅ F(g) ∘ F(f)."
  type: true-false
  answer: true
  explanation: "This is precisely the distinction between strict and weak 2-functors. A strict 2-functor preserves all structure at the level of equality: F of a composite equals the composite of F's. A weak (pseudo) functor replaces equality with specified invertible 2-cells φ_{g,f}: F(g∘f) → F(g)∘F(f), together with coherence conditions (a pentagon for triple composites and unit conditions for identities) ensuring the comparison 2-cells are compatible with associativity. The coherence conditions are essential: without them, 'preservation up to isomorphism' would be ill-defined because different re-bracketings of the same composite could give different results."

- question: "In a 2-category, most 2-cells (morphisms between morphisms) should be invertible for the structure to be well-defined."
  type: true-false
  answer: false
  explanation: "2-cells in a 2-category need not be invertible. In Cat, the 2-cells are natural transformations, and most natural transformations are not natural isomorphisms — they do not have inverses as 2-cells. The 2-category axioms only require that 2-cells compose (horizontally and vertically) in ways consistent with associativity and identity laws; they impose no invertibility requirement. A 2-groupoid is the special case where all 1-cells and 2-cells are invertible, but this is a restricted substructure. Weak functors specify invertible comparison 2-cells, but this is a property of the functor, not a requirement on the ambient 2-category."

- question: "What is the significance of coherence conditions in weak functors? Why can't we simply assert that F(g ∘ f) is isomorphic to F(g) ∘ F(f) without specifying additional requirements?"
  type: short-answer
  answer: "A weak functor specifies, for each composable pair (f, g), an invertible 2-cell φ_{g,f}: F(g∘f) → F(g)∘F(f). But when three 1-cells h, g, f are composable, there are two distinct ways to re-bracket the triple composite using the comparison 2-cells: one can apply φ_{h,g∘f} then (id_F(h) ∗ φ_{g,f}), or apply φ_{h∘g,f} then (φ_{h,g} ∗ id_F(f)), and these must agree. The coherence condition — a pentagon diagram analogous to the pentagon in monoidal categories — ensures that all re-bracketings of any composite give the same result. Without this, 'preservation up to isomorphism' would be ambiguous: the functor's action on composites would depend on the order of re-bracketing, destroying functoriality."
  explanation: "Coherence is what makes the isomorphisms canonical rather than arbitrary. It is the 2-categorical analogue of the associativity and unit axioms in ordinary category theory, lifted one dimension. The same pattern repeats in higher category theory: at each new dimension, equality is replaced by a specified equivalence one dimension up, with coherence conditions ensuring consistency. Understanding this pattern at the 2-categorical level gives the conceptual vocabulary for ∞-categories and homotopy type theory."
```

## Explainer

You already know three layers of categorical structure: **objects** (things), **morphisms** (maps between things, satisfying composition and identity laws), and **natural transformations** (maps between functors, which are themselves maps between categories). A **2-category** takes these three layers and treats them as a unified structure. Objects are 0-cells, morphisms are 1-cells, and natural transformations — or their generalizations — are **2-cells**. The defining example is Cat itself: objects are categories, 1-cells are functors, and 2-cells are natural transformations. The strictness of Cat (composition of functors is strictly associative on the nose) makes it the prototypical **strict** 2-category.

The power of the 2-categorical framework is that it unifies phenomena that otherwise require separate language. The statement "a functor F is an equivalence of categories" becomes, in 2-categorical terms, "F is a 1-cell with a quasi-inverse": there exists G and 2-cell isomorphisms FG ≅ Id and GF ≅ Id. Adjunctions, too, are 2-categorical data: the unit η: Id → GF and counit ε: FG → Id are 2-cells satisfying the triangle identities, so an adjunction is a structured pair of 1-cells with specified 2-cells. Once you recognize that functors, natural transformations, and adjunctions are all just 0-, 1-, and 2-dimensional cells in Cat, you can lift these concepts to any 2-category and reason about them uniformly.

**Strict 2-functors** between 2-categories preserve all structure exactly: composition of 1-cells is preserved on the nose, and 2-cells are sent to 2-cells respecting all compositions. But in practice, many natural constructions only preserve composition up to coherent isomorphism, not up to strict equality. A **weak functor** (also called a **pseudofunctor** or **homomorphism** of 2-categories) preserves composition of 1-cells only up to specified invertible 2-cells, together with coherence conditions ensuring these comparison 2-cells are compatible with associativity and identity. The prototypical example is the functor that assigns to each ring its category of modules: the "tensor product of modules" construction gives a functor that is only associative up to natural isomorphism, not strictly.

The distinction between strict and weak is the first instance of a deep pattern in higher category theory: as dimension increases, equality of composites is progressively weakened to "equivalence up to a cell one dimension higher," with coherence conditions ensuring the cells behave consistently. A **strict** 2-functor sends F(g ∘ f) = F(g) ∘ F(f) exactly. A **weak** 2-functor sends F(g ∘ f) ≅ F(g) ∘ F(f) via an invertible 2-cell φ_{g,f}, and this family of 2-cells must satisfy a pentagon-like coherence condition when composing three 1-cells. These coherence diagrams are the 2-categorical analogues of the associativity and unit axioms for monoidal categories — they ensure all ways of re-bracketing composites using the comparison 2-cells give the same result.

The **builds-toward** topic of higher category theory extends this pattern further: in a 3-category, 3-cells are maps between 2-cells, and weak functors between 3-categories preserve composition only up to invertible 3-cells, and so on up through the n-categorical hierarchy. The 2-categorical layer is where the essential new phenomena first appear — the distinction between strict and weak, the need for coherence data, and the recognition that "equality" of higher-dimensional structure is too strong a demand. Understanding 2-categories and weak functors gives you the conceptual vocabulary to engage with ∞-categories, homotopy type theory, and modern algebraic topology, all of which are grounded in the same hierarchical logic of cells and coherence conditions at increasing dimensions.

