---
id: categories-and-morphisms
title: Categories and Morphisms
domain: formal-sciences-and-logic
course: category-theory
prerequisites:
- id: naive-set-theory
  type: hard
- id: binary-relations
  type: soft
- id: composition-of-functions
  type: soft
- id: set-theory-basics
  type: soft
- id: injective-surjective-bijective
  type: soft
- id: set-fundamentals
  type: soft
- id: functions-and-function-properties
  type: soft
- id: relations-as-set-subsets
  type: soft
- id: functions-and-mappings-formal
  type: soft
builds-toward:
- functors
- isomorphisms-in-categories
- opposite-categories-and-duality
tags:
- categories
- morphisms
- objects
- composition
- identity
stage: expert
status: validated
---

# Categories and Morphisms

## Core Idea
A category consists of a collection of objects and a collection of morphisms (arrows) between them, together with a composition operation that is associative and has identity morphisms for each object. Categories abstract the essential structure of mathematical systems: sets with functions, groups with homomorphisms, vector spaces with linear maps, and topological spaces with continuous maps all form categories. The morphisms, not the objects, carry most of the structural content—category theory studies what can be said about mathematical structures purely from the arrows between them.

## How It's Best Learned
Start by recognizing familiar mathematical structures as categories: Set (sets and functions), Grp (groups and homomorphisms), Vect (vector spaces and linear maps). Verify the axioms—associativity of composition and existence of identities—in each case. Then work through small finite categories drawn as directed graphs to build intuition before abstract definitions.

## Common Misconceptions
- Objects need not have internal structure; in some categories, objects are just placeholders and all information is in the morphisms.
- A morphism is not necessarily a function—in a poset category, each morphism represents a ≤ relation, not a map.
- Identity morphisms are required for every object, not just for some.

## Questions

```yaml
- question: "In the category Set, what plays the role of morphisms?"
  type: multiple-choice
  options: ["Subsets of a given set", "Functions between sets", "Elements belonging to a set", "Equivalence relations on a set"]
  answer: 1
  explanation: "In Set, objects are sets and morphisms are functions between sets. Composition is function composition (which is associative), and identity morphisms are identity functions (which send every element to itself). This is the canonical example of a category and the one that most closely matches intuitions from prior mathematics."

- question: "In every category, every morphism must be a function that maps elements from one object to elements of another."
  type: true-false
  answer: false
  explanation: "Morphisms need not be functions. In a poset (partially ordered set) viewed as a category, objects are elements of the poset and there is at most one morphism from a to b — it exists if and only if a ≤ b. This morphism records an ordering relationship, not a mapping of elements. Category theory deliberately abstracts away internal structure, so 'morphism' means only 'arrow satisfying the composition and identity axioms,' not 'function.'"

- question: "State the two axioms that composition of morphisms must satisfy in any category."
  type: short-answer
  answer: "Associativity: (h ∘ g) ∘ f = h ∘ (g ∘ f) whenever defined. Identity: for every object A there is id_A such that f ∘ id_A = f and id_B ∘ f = f for any morphism f: A → B."
  explanation: "Associativity ensures that chaining multiple morphisms is unambiguous — parenthesization does not matter. The identity axiom ensures every object has a 'do-nothing' arrow that acts as a neutral element under composition, analogous to 0 under addition or 1 under multiplication. These two axioms are the entire algebraic content of the definition of a category."
```

## Explainer

Category theory begins with a unifying question: what do sets-and-functions, groups-and-homomorphisms, and vector-spaces-and-linear-maps have in common? The answer is the structure of a category: a collection of objects, a collection of morphisms (arrows) between them, and a composition operation. Category theory extracts this shared pattern and studies it in the abstract — any theorem proved from the category axioms alone holds simultaneously in every category, no matter how different the objects look.

A category C has two ingredients. First, a class of objects — think of these as the mathematical structures you care about (sets, groups, topological spaces). Second, for each ordered pair of objects A and B, a class of morphisms from A to B, written f: A → B. Morphisms compose: given f: A → B and g: B → C, there is a composite g ∘ f: A → C. Two axioms govern this composition. Associativity: (h ∘ g) ∘ f = h ∘ (g ∘ f) whenever the composites are defined — the order of association does not matter. Identity: every object A has an identity morphism id_A: A → A such that f ∘ id_A = f and id_B ∘ f = f for any f: A → B. That is the entire definition. No mention of elements, no mention of structure inside the objects.

The canonical example is Set: objects are sets, morphisms are functions, composition is function composition. You can verify the axioms directly — function composition is associative, and the identity function x ↦ x is a neutral element. Other examples reward careful examination. In Grp (groups and homomorphisms), morphisms must preserve the group operation — not every function between groups counts, only structure-preserving ones. In a poset viewed as a category, objects are elements of the poset and morphisms encode the ≤ relation: there is exactly one morphism from a to b if a ≤ b, and none otherwise. Morphisms here are not functions at all — they are just relationships. This variety shows why the definition is stated in terms of abstract arrows rather than functions.

The most important conceptual shift in category theory is from internal structure to relational structure. Set theory asks: what is inside a set? Category theory asks: how do objects relate to each other via morphisms? Two objects are considered isomorphic — essentially the same from the categorical perspective — if there are morphisms f: A → B and g: B → A such that g ∘ f = id_A and f ∘ g = id_B. They may look completely different internally, but if they behave identically with respect to all arrows, category theory treats them as equivalent. This relational point of view is what makes category theory so powerful as a unifying language across mathematics.

As you proceed to functors and natural transformations, you will see this abstraction pay off. A functor is a map between categories that preserves composition and identities — it is to categories what a homomorphism is to groups. Natural transformations are maps between functors. These higher-level structures let mathematicians transport theorems between entirely different areas of mathematics: a construction proved categorically in topology can apply immediately to algebra if both can be phrased in the same categorical language. The seemingly minimal axioms of a category are the foundation for this remarkable generality.
