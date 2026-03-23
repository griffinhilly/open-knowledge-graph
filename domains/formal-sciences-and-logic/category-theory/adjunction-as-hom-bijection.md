---
id: adjunction-as-hom-bijection
title: Adjunctions as Natural Hom-set Bijections
domain: formal-sciences-and-logic
course: category-theory
prerequisites:
- id: left-adjoint-functors
  type: hard
- id: right-adjoint-functors
  type: hard
- id: adjoint-functors
  type: soft
builds-toward:
- monads-in-category-theory
- kan-extensions
tags:
- adjunction
- hom-sets
- natural-transformation
stage: expert
status: validated
---

# Adjunctions as Natural Hom-set Bijections

## Core Idea
An adjunction L ⊣ R is a pair of functors with a natural isomorphism φ: Hom_D(Lc, d) ≅ Hom_C(c, Rd) for all objects c and d. The unit η: id_C ⇒ RL and counit ε: LR ⇒ id_D encapsulate the adjunction. This framework unifies diverse constructions—free groups, tensor products, completions—as universal solutions.

## Questions

```yaml
- question: "You want to define a group homomorphism from the free group F({a, b, c}) to the symmetric group S₃. Using the adjunction between Set and Grp, what information is it sufficient to specify?"
  type: multiple-choice
  options:
    - "The images of all elements of F({a, b, c}), listed explicitly, since the homomorphism must be total"
    - "The images of the three generators a, b, c in S₃, since the hom-set bijection reduces a group homomorphism to a function on generators"
    - "A surjective map from F({a, b, c}) to S₃, ensuring the homomorphism is well-defined"
    - "The kernel of the homomorphism, from which all other values can be recovered"
  answer: 1
  explanation: "The adjunction Hom_Grp(F(S), G) ≅ Hom_Set(S, U(G)) says exactly this: a group homomorphism from the free group on S to G is completely determined by a function from the generating set S to the underlying set of G. To define a homomorphism F({a,b,c}) → S₃, you only need to say where a, b, and c go in S₃ — three elements of S₃. The homomorphism then extends uniquely because every element of F({a,b,c}) is a word in a, b, c and their inverses, and homomorphisms must respect the group operations. Option A describes an exponentially larger specification that the universal property makes unnecessary. Options C and D describe different properties and do not follow from the adjunction."

- question: "In the free-forgetful adjunction between Set and Grp, what does the unit map η_S: S → U(F(S)) represent?"
  type: multiple-choice
  options:
    - "The group multiplication map, defining how elements of F(S) combine"
    - "The canonical inclusion of the generating set S into the underlying set of the free group F(S)"
    - "The quotient map collapsing F(S) to the trivial group by setting all generators equal"
    - "A natural transformation from F to the identity functor on Grp"
  answer: 1
  explanation: "The unit η_S: S → U(F(S)) is the 'canonical inclusion': it sends each element s ∈ S to the corresponding generator word in F(S), viewed as an element of the underlying set. It is the most natural way to embed the original set into the free structure built on it. This is the 'insert generators' map: every element of S appears in F(S) as a generator. The unit's naturality ensures this inclusion behaves coherently with all set functions. Option A confuses the unit with the group operation. Option C describes a collapse, which is the opposite of an inclusion. Option D misidentifies the domain and codomain of η."

- question: "The naturality condition on the hom-set bijection φ: Hom_D(Lc, d) ≅ Hom_C(c, Rd) ensures that transposing a morphism commutes with pre- and post-composition by arbitrary morphisms."
  type: true-false
  answer: true
  explanation: "Naturality in c means: for any morphism h: c' → c in C, we have φ(f ∘ Lh) = φ(f) ∘ h. Naturality in d means: for any morphism k: d → d' in D, we have φ(k ∘ f) = Rk ∘ φ(f). These two conditions together say the bijection is not just object-by-object but globally coherent — it commutes with all morphisms in both categories. This is what makes an adjunction a structural relationship between the categories rather than a collection of independent accidents. Without naturality, the bijection at each (c, d) pair could be arbitrary and unrelated to bijections at other pairs."

- question: "The hom-set bijection Hom_D(Lc, d) ≅ Hom_C(c, Rd) is merely a coincidence that holds separately for each pair of objects (c, d), with no coherence constraint relating bijections at different objects."
  type: true-false
  answer: false
  explanation: "This is precisely what naturality rules out. An adjunction requires the bijection to be natural in both c and d — meaning it must commute with pre- and post-composition in a specific way. This naturality is the difference between an adjunction and a mere family of bijections. It ensures that the entire structure of both categories is respected: the bijection is not a coincidence at each point but a consequence of a global structural relationship between L and R. Without naturality, one could construct bijections Hom_D(Lc, d) ≅ Hom_C(c, Rd) at each (c, d) pair independently that do not constitute an adjunction."

- question: "Why is naturality of the hom-set bijection φ: Hom_D(Lc, d) ≅ Hom_C(c, Rd) a stronger condition than saying it is a bijection for each pair (c, d)?  What does naturality add?"
  type: short-answer
  answer: "A bijection for each pair (c, d) independently could be completely arbitrary and unrelated across pairs — there would be no reason the bijection at (c, d) should be consistent with the bijection at (c', d) or (c, d'). Naturality adds coherence: the bijection must commute with all morphisms in both categories. Specifically, naturality in c requires that transposing and then precomposing gives the same result as precomposing and then transposing (via L). Naturality in d requires the same for postcomposition (via R). This means the transposition operation itself is a natural transformation, not just a collection of set bijections. It is this global coherence that makes adjunctions ubiquitous and structurally significant: free constructions, tensor products, products, and many other categorical constructions satisfy exactly this coherence condition, which is why adjunctions appear throughout mathematics."
  explanation: "A student who says 'naturality means the bijection is natural' is circular. The answer should articulate concretely what naturality adds: coherence with morphisms, or equivalently, that the bijection is functorial in both arguments. The contrast with a 'mere family of bijections' is essential to the answer."
```

## Explainer

You already understand left and right adjoints separately — you know that a left adjoint L "freely generates" something and a right adjoint R "forgets" or "restricts." The hom-set formulation makes the relationship between them precise. The claim is that maps from Lc to d in category D are in **natural bijective correspondence** with maps from c to Rd in category C. The word "natural" carries real weight: this bijection must be compatible with pre- and post-composition by morphisms, meaning it commutes with all relevant functorial operations. This naturality is what elevates the bijection from a coincidence to a structural fact.

The canonical example is the free-forgetful adjunction between **Set** and **Grp**. The free functor L sends a set S to the free group F(S); the forgetful functor R sends a group G to its underlying set. The adjunction says: a group homomorphism from F(S) to G is the same thing as a function from S to the underlying set of G. Concretely, to define a homomorphism out of the free group, you only need to specify where the generators go — an element of Hom_Set(S, R(G)). This is the **universal property of free constructions** in hom-set language.

The **unit** η: id_C ⇒ RL is a natural transformation that sends each object c to a morphism ηc: c → R(Lc). It is the "canonical inclusion": every set embeds into the underlying set of its free group, every vector space basis embeds into the span it generates. The **counit** ε: LR ⇒ id_D goes the other way: εd: L(Rd) → d is the "evaluation map," the canonical map out of the free object built on the underlying structure of d back to d itself (e.g., the free group on the underlying set of G maps canonically onto G by sending each generator word to its product in G). The unit and counit together satisfy the **triangle identities**, which encode that round trips through the adjunction (first apply η, then ε, in the right order) are the identity natural transformation.

The power of the hom-set perspective is that it packages all of this into a single natural isomorphism φ: Hom_D(Lc, d) ≅ Hom_C(c, Rd), making explicit what the unit and counit only imply. Given any morphism f: Lc → d, its **transpose** φ(f): c → Rd is the corresponding map in C; given g: c → Rd, its transpose φ⁻¹(g): Lc → d is the corresponding map in D. The naturality of φ means these transpositions interact correctly with all morphisms in both categories — the bijection is not just object-by-object but globally coherent across the entire categorical structure. This is the sense in which adjunctions "unify diverse constructions": tensor-hom adjunctions, product-diagonal adjunctions, and suspension-loop adjunctions in topology all have exactly this hom-set structure.
