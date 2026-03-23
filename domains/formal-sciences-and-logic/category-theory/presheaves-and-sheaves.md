---
id: presheaves-and-sheaves
title: Presheaves and Sheaves on Categories
domain: formal-sciences-and-logic
course: category-theory
prerequisites:
- id: presheaves
  type: hard
- id: yoneda-embedding-full-faithful
  type: soft
builds-toward:
- topos-theory-intro
tags:
- presheaf
- sheaf
- grothendieck-topology
- topos
- gluing
stage: expert
status: validated
---

# Presheaves and Sheaves on Categories

## Core Idea
A presheaf on a category C is a contravariant functor C^op → Set. The presheaf category [C^op, Set] is a Grothendieck topos: cartesian closed, complete, cocomplete, and satisfying the internal axiom of choice. Sheaves are presheaves satisfying a gluing condition with respect to a Grothendieck topology, forming a reflective subcategory. Presheaves and sheaves provide the fundamental examples of topoi and model intuitionistic logic.

## How It's Best Learned
Study simplicial sets [∆^op, Set] as the canonical presheaf example. Verify that [C^op, Set] is cartesian closed and complete. Define sheafification and verify that sheaves form a reflective subcategory. Compute limits and colimits of presheaves and sheaves explicitly.

## Common Misconceptions
Presheaves are not sheaves; sheafification requires imposing a Grothendieck topology. Not every presheaf is representable; non-representable presheaves are essential to the theory. Topos logic is intuitionistic; classical logic requires additional axioms (like axiom of choice), and not all topoi satisfy them.

## Questions

```yaml
- question: "A presheaf F on a category C assigns data to objects and restriction maps to morphisms. What additional condition must F satisfy to be a sheaf with respect to a Grothendieck topology J?"
  type: multiple-choice
  options:
    - "F must be representable — it must equal hom(–, c) for some object c ∈ C"
    - "Local sections on a covering family that agree on all pairwise overlaps must glue uniquely to a global section on the covered object"
    - "F must preserve all limits and colimits in C, making it a full functor"
    - "The sets F(c) must be abelian groups, not arbitrary sets, to allow gluing"
  answer: 1
  explanation: "The gluing (or descent) condition is what distinguishes a sheaf from a mere presheaf. Given a covering family {f_i : c_i → c} and local sections s_i ∈ F(c_i) that agree on all pairwise overlaps (F(c_i ×_c c_j) maps both s_i and s_j to the same element), there must exist a unique global section s ∈ F(c) that restricts to each s_i. Option A is false: not every sheaf is representable, and non-representable sheaves are essential to the theory. Option C confuses functoriality conditions with the sheaf condition. Option D is false: sheaves in the Grothendieck sense take values in any category, including Set."

- question: "Why is the presheaf category [C^op, Set] much 'larger' than the original category C, and what role do non-representable presheaves play?"
  type: multiple-choice
  options:
    - "It is larger only in a set-theoretic sense; representable presheaves capture all the relevant structure and non-representables are redundant"
    - "[C^op, Set] is the free cocompletion of C — it freely adds all colimits, including objects that represent 'idealized' or 'generalized' elements that C itself lacks"
    - "The size difference arises from the contravariance; covariant functors from C to Set would give a category the same size as C"
    - "Non-representable presheaves are artifacts of set-theoretic foundations and have no mathematical content"
  answer: 1
  explanation: "[C^op, Set] is the free cocompletion of C: it adds all small colimits, creating a much richer universe. Non-representable presheaves represent genuinely new objects — for example, in algebraic geometry, the functor of points of a scheme may be a sheaf that is not representable by any scheme in a naive sense, but is representable in the enlarged category. The Yoneda embedding embeds C fully faithfully into [C^op, Set], but the latter is vastly larger. Option A fundamentally misunderstands the purpose of the presheaf construction: non-representable presheaves are not redundant — they are the objects you freely add when completing C."

- question: "Every sheaf is a presheaf, but not every presheaf is a sheaf."
  type: true-false
  answer: true
  explanation: "A sheaf is a presheaf with an additional condition (the gluing axiom). Since sheaves satisfy all presheaf axioms plus the gluing condition, every sheaf is automatically a presheaf. The reverse fails: a presheaf may fail the gluing condition. For example, the presheaf that assigns to each open set U the set of *bounded* continuous functions fails to be a sheaf on R because local sections that agree on overlaps may glue to an unbounded global function. The category of sheaves Sh(C, J) is a full subcategory of the presheaf category [C^op, Set], and the inclusion has a left adjoint (sheafification) that converts arbitrary presheaves into sheaves."

- question: "The internal logic of any Grothendieck topos is classical — it satisfies the law of excluded middle and the axiom of choice."
  type: true-false
  answer: false
  explanation: "This is a key misconception about topos theory. The internal logic of a Grothendieck topos is intuitionistic by default — it satisfies intuitionistic higher-order logic but not necessarily classical logic. The law of excluded middle (P ∨ ¬P for all propositions) and the axiom of choice fail in many topoi. For example, the topos of sheaves on a topological space satisfies classical logic only if the space is discrete. Different Grothendieck topologies on the same category C produce different internal logics, some classical and some not. This logical richness is precisely why topos theory is foundational to categorical logic and constructive mathematics."

- question: "What is the gluing condition for a sheaf, and why is it described as the formal mathematical expression of 'local-to-global' reasoning?"
  type: short-answer
  answer: "Given a covering family {c_i → c} and local sections s_i ∈ F(c_i) that pairwise agree on overlaps, the gluing condition requires a unique global section s ∈ F(c) restricting to each s_i. This captures 'local-to-global' reasoning because it says: if you have consistent local data (data on each patch that agrees where patches overlap), you can always reconstruct a unique global datum. The word 'unique' is crucial — not only does a global section exist, but it is the only one compatible with the local data."
  explanation: "The topological motivation is transparent: a continuous function on a space is completely determined by its values on any open cover, and locally defined functions that agree on overlaps patch together uniquely. The sheaf condition formalizes this. When the gluing condition fails, you have a presheaf: local data exists but cannot always be assembled globally. Sheafification forces this assembly to work by identifying presheaf sections that 'want to be' the same global section. In logic, the gluing condition corresponds to the idea that truth is a local-global property: a statement holds globally if and only if it holds locally on every cover."
```

## Explainer

A **presheaf** on a small category C is a contravariant functor F : C^op → **Set**: to each object c ∈ C it assigns a set F(c), and to each morphism f : c → d it assigns a function F(f) : F(d) → F(c) going the opposite way, with functoriality. You should think of C as a category of "open sets" (or patches of some space), and F(c) as the set of "local data" (sections) defined on c. The contravariancy captures restriction: if d is a smaller patch inside c, and f : d → c is the inclusion, then F(f) restricts data from c down to d.

From your study of the Yoneda embedding, you know that every representable presheaf yc = hom(–, c) is a presheaf, and the Yoneda lemma says natural transformations from yc to F correspond bijectively to elements of F(c). The presheaf category [C^op, **Set**] is vastly larger than C itself — it contains representables, but also all the non-representable presheaves that arise when you "freely complete" C. This category is a **Grothendieck topos**: it has all limits and colimits, it is cartesian closed (internal function objects exist), and it has a subobject classifier Ω. Limits and colimits in [C^op, **Set**] are computed pointwise — (lim F_i)(c) = lim(F_i(c)) — making it one of the most tractable categories to work with concretely.

A **sheaf** imposes an additional *gluing condition*. Given a **Grothendieck topology** J on C — a system specifying, for each object c, which families of morphisms "cover" c — a presheaf F is a *J-sheaf* if whenever you have local sections defined on a covering family that agree on all overlaps, there is a unique global section that restricts to each local one. This is exactly the classical condition from topology: a continuous function on a space is determined by its values on an open cover, and a sheaf formalizes this "local-to-global" principle categorically. The category of J-sheaves **Sh(C, J)** is a reflective subcategory of [C^op, **Set**]: the inclusion has a left adjoint called **sheafification**, which forces a presheaf to satisfy the gluing condition by "forcing" agreement on overlaps.

Sheaves and presheaves connect the abstract machinery of category theory to concrete mathematics in both directions. Going toward topology and geometry: sheaves on the site of open sets of a topological space model varying algebraic structures (the structure sheaf of a scheme, the sheaf of continuous functions). Going toward logic: the internal language of a Grothendieck topos is intuitionistic higher-order logic, and different Grothendieck topologies on the same category C give different logical universes — some satisfying classical logic, some not. This is why the theory of presheaves and sheaves is foundational to topos theory, algebraic geometry (the étale site, the flat site), and categorical logic: the gluing axiom is the precise mathematical expression of the idea that local truth implies global truth, and its failure or variation gives rise to rich structure.
