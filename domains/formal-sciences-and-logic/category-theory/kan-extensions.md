---
id: kan-extensions
title: Kan Extensions
domain: formal-sciences-and-logic
course: category-theory
prerequisites:
- id: yoneda-lemma
  type: hard
- id: limits-and-colimits
  type: hard
- id: adjoint-functors
  type: soft
- id: functor-categories
  type: soft
- id: functions-and-function-properties
  type: soft
- id: function-composition
  type: soft
- id: set-operations
  type: soft
- id: function-composition-and-inverses
  type: soft
tags:
- Kan extension
- left Kan extension
- right Kan extension
- pointwise Kan extension
- colimit formula
- universal construction
stage: expert
status: validated
---
# Kan Extensions

## Core Idea
Given functors K: C → D and F: C → E, the left Kan extension Lan_K F: D → E is the universal functor extending F along K, satisfying a universal property: Nat(Lan_K F, G) ≅ Nat(F, G ∘ K) for all G: D → E. Dually, the right Kan extension Ran_K F satisfies Nat(G, Ran_K F) ≅ Nat(G ∘ K, F). When E is cocomplete, left Kan extensions can be computed pointwise as colimits: (Lan_K F)(d) = colim_{(c, K(c)→d)} F(c) over the comma category (K ↓ d). Saunders Mac Lane famously wrote that "all concepts are Kan extensions," since limits, colimits, adjunctions, and even the Yoneda embedding can be expressed as Kan extensions.

## How It's Best Learned
Start with the simplest case: K is the inclusion of a subcategory and F assigns values on that subcategory. Compute the left Kan extension as a colimit over the relevant comma category for a concrete example (e.g., extending a functor defined on a discrete category to a larger one). Then verify that adjoint functors are a special case: the left adjoint of G is the left Kan extension of the identity along G.

## Common Misconceptions
- Kan extensions need not exist in general; existence requires sufficient (co)completeness conditions or specific properties of the functors involved.
- Pointwise Kan extensions (computed as (co)limits) are stronger than abstract Kan extensions defined solely by the universal property; the pointwise version implies the abstract one but not conversely.
- The phrase "all concepts are Kan extensions" is a conceptual statement about the universality of the construction, not a claim that every theorem in category theory literally reduces to a Kan extension computation.

## Questions

```yaml
- question: "The universal property of the left Kan extension Lan_K F states that Nat(Lan_K F, G) ≅ Nat(F, G ∘ K) for all G: D → E. A colleague interprets this as meaning (Lan_K F)(K(c)) = F(c) for all c ∈ C. Is this correct?"
  type: multiple-choice
  options:
    - "Yes — the universal property ensures the extension agrees pointwise with F on all objects in the image of K"
    - "No — there is a canonical natural transformation η: F ⇒ (Lan_K F) ∘ K (the unit), but the values may differ because (Lan_K F)(K(c)) is computed as a colimit over the comma category (K ↓ K(c)), which may aggregate multiple F-values"
    - "Yes — Kan extensions are defined to be exact extensions that preserve all values on the image of K by construction"
    - "No — Lan_K F is undefined on objects in the image of K; it is only defined on objects of D outside that image"
  answer: 1
  explanation: "The unit of the Kan extension is a natural transformation η: F ⇒ (Lan_K F) ∘ K, which gives a canonical map from F(c) into (Lan_K F)(K(c)), but they need not be equal. The value (Lan_K F)(K(c)) is computed as the colimit over the comma category (K ↓ K(c)) — all pairs (c', K(c') → K(c)). This category includes the identity K(c) → K(c) but may include other objects too, so the colimit may be 'larger than' F(c). The universal property governs the bijection of natural transformations, not pointwise equality. Only when K is fully faithful does (Lan_K F)(K(c)) recover F(c) exactly."

- question: "Mac Lane wrote that 'all concepts are Kan extensions.' Which statement correctly describes how left adjoint functors arise as a special case?"
  type: multiple-choice
  options:
    - "Every left adjoint can be factored into a sequential composition of two Kan extensions along intermediate functors"
    - "The left adjoint of G: D → C, when it exists, equals the left Kan extension Lan_G Id_C — the extension of the identity functor on C along G"
    - "Adjoint functors satisfy a similar universal property to Kan extensions but are defined differently; the connection is a metaphor, not a formal identification"
    - "Mac Lane meant that Kan extensions are always adjoint pairs, not that adjoints are themselves Kan extensions"
  answer: 1
  explanation: "If F ⊣ G with G: D → C, the adjoint bijection gives Hom_D(F(c), d) ≅ Hom_C(c, G(d)) for all c ∈ C, d ∈ D. Now consider Lan_G Id_C: C → D, the left Kan extension of the identity Id_C along G. Its universal property is Nat(Lan_G Id_C, H) ≅ Nat(Id_C, H ∘ G) for all H: C → D. Specializing to representable H recovers exactly the adjoint bijection. So F = Lan_G Id_C: the left adjoint is precisely the left Kan extension of the identity along G. This is one concrete sense in which adjunctions are Kan extensions — and why Mac Lane's dictum carries formal weight."

- question: "When the target category E is cocomplete, the left Kan extension of F: C → E along K: C → D is computed pointwise as (Lan_K F)(d) = colim_{(K ↓ d)} F, where (K ↓ d) is the comma category of objects of C equipped with morphisms into d via K."
  type: true-false
  answer: true
  explanation: "This is the pointwise computation formula for left Kan extensions when E has sufficient colimits. For each d ∈ D, the comma category (K ↓ d) has as objects all pairs (c ∈ C, f: K(c) → d), and the colimit of the functor F (composed with the projection (K ↓ d) → C) gives the value of the Kan extension at d. Intuitively: to extend F to d, you collect all values F(c) for objects c whose image K(c) maps into d, and glue them together in the most general way — a colimit. This pointwise formula exists when E is cocomplete and defines a Kan extension that is also preserved by representable functors."

- question: "A left Kan extension Lan_K F always exists for any pair of functors K: C → D and F: C → E, because the universal property uniquely characterizes what the values must be at every object of D."
  type: true-false
  answer: false
  explanation: "The universal property defines what a Kan extension IS if it exists, but does not guarantee existence. Existence of Lan_K F requires sufficient cocompleteness of E (for the colimit formula to work) or other conditions on the functors involved. For small C and D with E = Set (which is cocomplete), left Kan extensions always exist. But for general E lacking necessary colimits, the extension may fail to exist. This is analogous to adjoint functor theorems: the universal property of an adjoint characterizes it precisely, but existence requires additional conditions (solution set condition, completeness). Universal properties characterize; they do not guarantee existence."

- question: "Explain why Mac Lane's claim that 'all concepts are Kan extensions' is meaningful rather than merely metaphorical. Provide one concrete example showing how a standard categorical construction arises as a Kan extension."
  type: short-answer
  answer: "The claim is meaningful because Kan extensions subsume the universal properties of the most fundamental constructions in category theory under a single schema. The clearest example is adjoint functors: given G: D → C, its left adjoint F (if it exists) equals the left Kan extension Lan_G Id_C of the identity functor on C along G. The Kan extension universal property Nat(Lan_G Id_C, H) ≅ Nat(Id_C, H ∘ G) specializes to the adjoint bijection Hom(F(c), d) ≅ Hom(c, G(d)) when H is representable. Another example: the colimit of F: J → C is the left Kan extension of F along the unique functor J → 1 (to the terminal category), since the colimit is the universal cocone — exactly what Lan_! F computes at the single object of 1."
  explanation: "The claim is also qualified in the Common Misconceptions: it is a statement about the universality of the construction, not a claim that every theorem in category theory is literally computed as a Kan extension. What it means is that the one concept of Kan extension unifies limits, colimits, adjunctions, the Yoneda embedding, Day convolution, and nerve-realization adjunctions — all fall out of the same abstract pattern. Understanding this unification is what it means to have a mature categorical perspective."
```

## Explainer

The motivating question is simple: given a functor F: C → E and a functor K: C → D that "embeds" or "changes" the indexing, can you extend F to all of D in the most economical way? Concretely, imagine F is defined on a small subcategory C but you need a functor defined on all of D — the left Kan extension Lan_K F is the "best approximation from the left" to this problem. The universal property says: natural transformations from Lan_K F to any G: D → E are in natural bijection with natural transformations from F to G ∘ K. This is the same pattern you know from adjunctions: Lan_K F is left adjoint to the precomposition functor (− ∘ K) between functor categories. When you see Nat(Lan_K F, G) ≅ Nat(F, G ∘ K), read it as "the extension sees everything the original functor saw, and nothing more."

When E is cocomplete, you can compute the left Kan extension **pointwise** as a colimit. For each object d ∈ D, the comma category (K ↓ d) consists of all pairs (c ∈ C, K(c) → d) — the objects of C that map into d via K, together with those maps. The colimit of F over this comma category gives (Lan_K F)(d) = colim_{(K ↓ d)} F. Intuitively, to define the extension at d, you look at all the "ways d can be reached from C via K," take the values of F at those sources, and glue them together in the most general way — a colimit. The right Kan extension is the dual, using limits over the comma category (d ↓ K) instead. Pointwise Kan extensions are particularly well-behaved: they are preserved by representable functors and interact cleanly with composition.

Adjunctions are among the most important special cases. If you take K = G: D → C (a functor you want a left adjoint for) and set F = Id_C, then Lan_G Id_C: C → D is exactly the left adjoint of G — if it exists. The universal property of the Kan extension precisely recovers the adjoint bijection Hom_C(c, G(d)) ≅ Hom_D(Fd, d). This is why Mac Lane's dictum "all concepts are Kan extensions" carries weight: limits (right Kan extensions along the diagonal), colimits (left Kan extensions along the diagonal), the Yoneda embedding (the right Kan extension of the identity along itself), and adjoints all fall out of the one construction. Understanding Kan extensions is essentially understanding the universal properties that hold all of category theory together.

A practical technique worth mastering is computing Kan extensions via the **coend formula** for functor categories: (Lan_K F)(d) = ∫^{c ∈ C} Hom_D(K(c), d) ⊗ F(c), a "weighted colimit" that generalizes the pointwise formula. This expression makes it transparent that the extension at d is built by "gluing copies of F(c) weighted by how many ways K(c) maps to d." For discrete categories, it collapses to a coproduct; for enriched categories, it becomes a tensor product. Once you see this formula, constructions like Day convolution (the monoidal structure on functor categories) and nerve-realization adjunctions appear as instances of the same underlying Kan extension machinery.
