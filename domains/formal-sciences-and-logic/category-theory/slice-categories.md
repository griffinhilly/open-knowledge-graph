---
id: slice-categories
title: Slice and Coslice Categories
domain: formal-sciences-and-logic
course: category-theory
prerequisites:
- id: categories-and-morphisms
  type: hard
- id: functors
  type: soft
builds-toward:
- universal-properties
- kan-extensions
tags:
- slice
- coslice
- comma
- relative
- over
stage: advanced
status: validated
---

# Slice and Coslice Categories

## Core Idea
The slice category C/X has objects as morphisms f: Y → X and morphisms as commutative triangles. The coslice category X/C has objects as morphisms X → Y with the same commutative structure. Slice categories formalize 'relative' categorical properties and are essential for defining limits and colimits in a relative sense. They appear naturally in studying fibrations and in defining universal properties with a fixed reference object.

## How It's Best Learned
Study slice categories of Set over a set S (equivalent to S-indexed families of sets). Examine slice categories of a poset over an element, and verify that limits in the slice category correspond to special limits in the original category.

## Common Misconceptions
A slice category is not a full subcategory—morphisms in C/X are defined relative to X. Not every limit in C/X lifts to a limit in C. The universal properties in slice categories are weaker than absolute universal properties because they depend on the choice of X.

## Questions

```yaml
- question: "In the slice category Set/S where S = {0, 1, 2}, which of the following correctly describes an object of Set/S?"
  type: multiple-choice
  options:
    - "A subset A ⊆ S"
    - "A function f: A → S, which partitions the set A into three labeled fibers f⁻¹(0), f⁻¹(1), f⁻¹(2)"
    - "A set A with no additional structure, because S is the reference and provides all the structure"
    - "A pair of sets (A, B) where A and B are both subsets of S"
  answer: 1
  explanation: "Objects of C/X are not objects of C — they are morphisms f: Y → X in C. In Set/S, an object is a function f: A → S, which assigns each element of A a label in S. This is equivalent to an S-indexed family of sets: the fiber f⁻¹(s) for each s ∈ S. Option A (subset of S) confuses the objects of C with objects of C/X. Option C misses that the object is the function, not just the domain set. The key shift is that in a slice category, *morphisms become objects*."

- question: "A morphism in the slice category C/X from (Y, f: Y → X) to (Z, g: Z → X) is a morphism h: Y → Z in C. What additional condition must h satisfy?"
  type: multiple-choice
  options:
    - "h must be an isomorphism in C"
    - "h must factor through X — there must exist a morphism X → Z"
    - "The triangle must commute: g ∘ h = f, so h preserves the relationship of Y and Z to X"
    - "No additional condition — any morphism h: Y → Z in C is automatically a morphism in C/X"
  answer: 2
  explanation: "A morphism in C/X is not just any morphism between the underlying objects — it must make the triangle over X commute. The condition g ∘ h = f says that h is compatible with both objects' maps to X: following h and then g gives the same result as following f directly. Without this condition, C/X would just be C (ignoring X entirely), not a genuinely new 'relative' category. Option D is the most tempting wrong answer and captures the misconception that the slice category is just a full subcategory of C."

- question: "The slice category C/X is a full subcategory of C, with objects being those Y for which there exists at least one morphism Y → X."
  type: true-false
  answer: false
  explanation: "This is a precise and important distinction. First, objects of C/X are morphisms f: Y → X — not just objects Y. Multiple distinct objects of C/X can have the same underlying object Y (if there are multiple morphisms Y → X). Second, C/X is not full: a morphism in C/X between (Y, f) and (Z, g) is not every morphism Y → Z in C, only those h satisfying g ∘ h = f. C/X imposes an additional constraint that makes it a *relative* structure, not a restriction of C."

- question: "In Set/S, a morphism h from (A, f: A → S) to (B, g: B → S) maps each fiber f⁻¹(s) into the corresponding fiber g⁻¹(s) for every s ∈ S."
  type: true-false
  answer: true
  explanation: "The morphism condition in Set/S is g ∘ h = f. If a ∈ A and f(a) = s, then g(h(a)) = f(a) = s, so h(a) ∈ g⁻¹(s). This means h maps elements labeled s by f to elements labeled s by g — exactly fiber-preservation. This is the concrete meaning of the abstract commutativity condition in Set/S: morphisms of S-indexed families must respect the indexing, sending the s-fiber to the s-fiber for every s."

- question: "Explain what makes a universal property in a slice category C/X 'relative' to X, and in what sense is this weaker than an absolute universal property in C itself?"
  type: short-answer
  answer: "A universal property in C/X is defined within the world of objects-over-X: it asserts that some object (A, f: A → X) is initial or terminal among all objects equipped with a morphism to X, with morphisms being commuting triangles. The entire notion of 'unique' morphism is relative to this constrained universe — uniqueness among morphisms h: (Y, g) → (A, f) in C/X, not among all morphisms Y → A in C. Changing X produces an entirely different slice category with different universal objects. An absolute universal property in C holds with no reference to a fixed base object. The slice property is weaker because the uniqueness is asserted only within the restricted context where everything comes with a map to X; outside that context, the object may have no universal character at all."
  explanation: "This question targets the conceptual core of why slice categories matter: they relativize categorical notions, making them context-dependent. Understanding that universal properties in C/X depend on the choice of X — and fail to hold absolutely in C — is the key to grasping how slice categories generalize the idea of 'structure over a base,' which is the foundation for fibrations, dependent types, and parameterized constructions throughout mathematics."
```

## Explainer

You already know that a category consists of objects and morphisms satisfying identity and composition laws. The slice construction takes a fixed object X in a category C and builds an entirely new category whose objects are **morphisms landing in X**. An object of the **slice category** C/X is a pair (Y, f) where f: Y → X is a morphism in C. Think of it as "everything that maps into X, organized as a category in its own right."

A morphism in C/X from (Y, f) to (Z, g) is a morphism h: Y → Z in C such that the triangle commutes: g ∘ h = f. In other words, h must be compatible with the maps to X — it doesn't just connect Y to Z, it connects Y to Z **in a way that respects both objects' relationship to X**. Composition is inherited from C (compose the underlying morphisms), and the commutativity condition is preserved under composition. Identity morphisms are the identity morphisms from C, which trivially satisfy the commutativity condition.

The concrete example worth internalizing is **Set/S**, the slice of **Set** over a set S. An object is a function f: A → S — equivalently, an S-indexed family of sets (the fiber over each s ∈ S is f⁻¹(s)). A morphism from f: A → S to g: B → S is a function h: A → B preserving fibers: g(h(a)) = f(a) for all a. This is precisely a morphism of S-indexed families of sets. So **Set/S** is equivalent to the category of S-indexed families — and this makes slice categories the correct setting for studying variable or parameterized structures.

The **coslice category** X/C reverses the arrows: its objects are morphisms X → Y (things that X maps **into**), and morphisms are commutative triangles pointing outward. Coslice categories capture "things equipped with a distinguished element or basepoint," since a morphism X → Y in Set is the same as a choice of element in Y (when X is a singleton). Both slice and coslice categories appear naturally in the theory of limits and colimits — a cone over a diagram D with apex X is exactly an object of the appropriate slice category built from D — and they are essential for expressing universal properties in a relative, contextual way. When the fixed object X changes, so does the entire categorical context for what "universal" means.
