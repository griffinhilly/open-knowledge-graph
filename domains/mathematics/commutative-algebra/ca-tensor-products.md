---
id: ca-tensor-products
title: Tensor Products of Modules
domain: mathematics
course: commutative-algebra
prerequisites:
- id: ca-modules-over-rings
  type: hard
builds-toward:
- ca-flat-modules
tags:
- tensor-product
- bilinear-map
- base-change
- right-exact
stage: expert
status: validated
---

# Tensor Products of Modules

## Core Idea
The tensor product M ⊗_R N of two R-modules is the module that universally linearizes bilinear maps: every R-bilinear map M × N → P factors uniquely through M ⊗_R N. Tensor products perform "base change" (extending scalars from one ring to another), are right exact but not left exact in general, and are the algebraic mechanism behind many constructions in geometry and algebra.

## Questions

```yaml
- question: "Which of the following correctly describes ℤ/2ℤ ⊗_ℤ ℤ/3ℤ?"
  type: multiple-choice
  options:
    - "ℤ/6ℤ, by the Chinese Remainder Theorem"
    - "ℤ/2ℤ ⊕ ℤ/3ℤ"
    - "The zero module, because 2 and 3 are coprime"
    - "ℤ/2ℤ, because ℤ/3ℤ has no 2-torsion"
  answer: 2
  explanation: "For any a̅ ⊗ b̅ ∈ ℤ/2ℤ ⊗_ℤ ℤ/3ℤ, we have a̅ ⊗ b̅ = a̅ ⊗ 3b̅ = 3(a̅ ⊗ b̅) (since 3b̅ = 0̅ in ℤ/3ℤ) and also a̅ ⊗ b̅ = 2(a̅ ⊗ b̅)·something. More directly: 1̅ ⊗ b̅ = 1̅ ⊗ (3·1̅)b̅... The cleanest argument: a̅ ⊗ b̅ = a̅ ⊗ 1̅ · b = a̅ · 1 ⊗ b̅, and since 2(a̅ ⊗ b̅) = 0 and 3(a̅ ⊗ b̅) = 0, we get 1·(a̅ ⊗ b̅) = (3-2)(a̅ ⊗ b̅) = 0. So every pure tensor is zero, and the entire module is zero. This is the tensor product's way of saying 'ℤ/2ℤ and ℤ/3ℤ have no common structure to combine.'"

- question: "For an R-module M and an ideal I ⊆ R, which of the following is the correct relationship between M ⊗_R R/I and M/IM?"
  type: multiple-choice
  options:
    - "They are not generally related"
    - "M ⊗_R R/I ≅ M/IM — tensoring with R/I is the same as 'reducing modulo I'"
    - "M ⊗_R R/I ≅ IM"
    - "M ⊗_R R/I ≅ Hom_R(R/I, M)"
  answer: 1
  explanation: "This is one of the most useful computational identities for tensor products. Applying − ⊗_R R/I to M is equivalent to quotienting by IM. For example, M ⊗_ℤ ℤ/nℤ ≅ M/nM for any abelian group M. This identity says that tensoring with R/I performs 'reduction modulo I' — it is the algebraic version of restricting to a closed subvariety in geometry. The proof uses the right exactness of tensor product applied to 0 → I → R → R/I → 0."

- question: "The tensor product functor − ⊗_R N is right exact: it preserves surjections and cokernels."
  type: true-false
  answer: true
  explanation: "If A → B → C → 0 is exact, then A ⊗_R N → B ⊗_R N → C ⊗_R N → 0 is exact. This is a fundamental property of tensor products. The critical limitation is that tensor products are NOT left exact in general: the map A ⊗ N → B ⊗ N need not be injective even when A → B is injective. The failure of left exactness is measured by the Tor functor, and modules for which tensoring is exact are called flat."

- question: "Tensor products commute with direct sums: M ⊗_R (⊕ᵢ Nᵢ) ≅ ⊕ᵢ (M ⊗_R Nᵢ)."
  type: true-false
  answer: true
  explanation: "This follows from the universal property: bilinear maps from M × (⊕Nᵢ) correspond to families of bilinear maps from each M × Nᵢ. Concretely, R^n ⊗_R M ≅ M^n (tensoring with a free module of rank n gives n copies). This is one of the key computational tools: to compute M ⊗ N, present N as a quotient of a free module (via generators and relations) and use right exactness and the direct sum formula."

- question: "Why is the tensor product ℤ/2ℤ ⊗_ℤ ℤ/3ℤ zero, and what general principle does this illustrate?"
  type: short-answer
  answer: "For any element a̅ ⊗ b̅, we compute: a̅ ⊗ b̅ = 1·(a̅ ⊗ b̅) = (3 - 2)(a̅ ⊗ b̅) = 3(a̅ ⊗ b̅) - 2(a̅ ⊗ b̅). But 2(a̅ ⊗ b̅) = (2a̅) ⊗ b̅ = 0̅ ⊗ b̅ = 0, and 3(a̅ ⊗ b̅) = a̅ ⊗ (3b̅) = a̅ ⊗ 0̅ = 0. So a̅ ⊗ b̅ = 0 for every pure tensor, hence M ⊗ N = 0. The general principle: ℤ/mℤ ⊗_ℤ ℤ/nℤ ≅ ℤ/gcd(m,n)ℤ. When gcd(m,n) = 1, the tensor product is zero. Modules annihilated by coprime integers have 'no common information' to combine."
  explanation: "This illustrates how tensor products detect common structure. The tensor product of two modules is zero when their annihilators generate the whole ring. Geometrically, this corresponds to two subvarieties with empty intersection: their structure sheaves have zero tensor product. The formula ℤ/mℤ ⊗ ℤ/nℤ ≅ ℤ/gcd(m,n)ℤ is a clean example of the general identity M ⊗_R R/I ≅ M/IM."
```

## Explainer

In linear algebra, given two vector spaces V and W over a field k, the tensor product V ⊗_k W constructs a new vector space whose elements represent "bilinear combinations" of elements from V and W. The dimension satisfies dim(V ⊗ W) = dim(V) · dim(W), and if {vᵢ} and {wⱼ} are bases, then {vᵢ ⊗ wⱼ} is a basis for V ⊗ W. The module-theoretic tensor product generalizes this to modules over any commutative ring, but the behavior is richer and more surprising because modules lack bases in general.

The **tensor product** M ⊗_R N is defined by a universal property: it is an R-module together with an R-bilinear map M × N → M ⊗_R N such that every R-bilinear map M × N → P factors uniquely through it. The elements m ⊗ n (called **pure tensors**) are generators, subject to the relations of bilinearity: (m₁ + m₂) ⊗ n = m₁ ⊗ n + m₂ ⊗ n, m ⊗ (n₁ + n₂) = m ⊗ n₁ + m ⊗ n₂, and r(m ⊗ n) = (rm) ⊗ n = m ⊗ (rn). A general element is a sum of pure tensors, and recognizing when such sums are zero is the main computational challenge.

The most important property of tensor products for commutative algebra is **right exactness**. If 0 → A → B → C → 0 is exact, then A ⊗ N → B ⊗ N → C ⊗ N → 0 is exact — the tensor product preserves surjections and cokernels. But the map A ⊗ N → B ⊗ N need not be injective: tensor products can kill elements. This failure of left exactness is precisely what the **Tor** functor measures, and modules N for which − ⊗ N is exact (preserves all short exact sequences) are called **flat modules**.

The computation ℤ/mℤ ⊗_ℤ ℤ/nℤ ≅ ℤ/gcd(m,n)ℤ illustrates the key features. When gcd(m,n) = 1, the tensor product vanishes — the two modules have "incompatible" structures. The general identity M ⊗_R R/I ≅ M/IM shows that tensoring with a quotient ring performs "reduction modulo I," which is the algebraic operation underlying restriction to a closed subvariety. In algebraic geometry, tensor products implement fiber products and base change — changing the ring over which a module is defined. These operations are ubiquitous: extending scalars from ℤ to ℚ (rationalization), from R to R/𝔭 (reduction modulo a prime), or from R to its completion are all instances of tensor product base change.
