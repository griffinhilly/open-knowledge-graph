---
id: derived-functors
title: Derived Functors
domain: formal-sciences-and-logic
course: category-theory
prerequisites:
- id: homology-and-cohomology
  type: hard
- id: adjoint-functors
  type: soft
- id: abelian-categories
  type: soft
- id: vector-spaces
  type: soft
- id: composition-of-functions
  type: soft
- id: linear-transformations
  type: soft
- id: linear-transformations-definition
  type: soft
tags:
- derived functor
- Ext
- Tor
- projective resolution
- injective resolution
- left derived
- right derived
stage: expert
status: validated
---
# Derived Functors

## Core Idea
Derived functors measure how a functor between abelian categories fails to be exact. Given a left exact functor F (such as Hom(M, −)), its right derived functors R^nF are computed by taking an injective resolution of the input, applying F, and taking cohomology: R^nF(A) = H^n(F(I^*)). Dually, left derived functors L_nF of a right exact functor (such as − ⊗ M) use projective resolutions. The key examples are Ext^n(M, N) = R^n Hom(M, −)(N), which classifies n-fold extensions, and Tor_n(M, N) = L_n(− ⊗ N)(M), which detects torsion phenomena. Derived functors convert exactness failures into computable invariants and are the foundation of homological algebra.

## How It's Best Learned
Compute Ext^1_Z(Z/2, Z) by hand: take a projective resolution of Z/2 (namely 0 → Z →(×2) Z → Z/2 → 0), apply Hom(−, Z), and compute the cohomology. Then compute Tor_1^Z(Z/2, Z/3) using a projective resolution of Z/2 and tensoring with Z/3. Connect these computations to the abstract definition and verify independence of the choice of resolution.

## Common Misconceptions
- Derived functors are independent of the choice of resolution (projective or injective); this is a theorem, not obvious, and relies on comparison lemmas and homotopy invariance.
- Ext^0 and Tor_0 recover the original functors (Hom and ⊗ respectively); the higher derived functors measure the non-exactness.
- Not every abelian category has enough projectives or injectives; derived functors require such existence conditions, which must be verified for each category.

## Questions

```yaml
- question: "To compute Ext¹(ℤ/2, ℤ), one takes the projective resolution of ℤ/2 — namely 0 → ℤ →(×2)→ ℤ → ℤ/2 → 0 — applies Hom(−, ℤ) to the projective part, and takes cohomology. The result is:"
  type: multiple-choice
  options:
    - "0, because ℤ is a free ℤ-module and free modules have trivial Ext"
    - "ℤ/2, capturing the single non-trivial extension class corresponding to the original sequence"
    - "ℤ, because the sequence involves integer multiplication"
    - "Undefined, because ℤ/2 does not have a projective resolution over ℤ"
  answer: 1
  explanation: "Applying Hom(−, ℤ) to the projective part 0 → ℤ →(×2)→ ℤ gives the complex 0 → Hom(ℤ,ℤ) →(×2)→ Hom(ℤ,ℤ), i.e., 0 → ℤ →(×2)→ ℤ. The first cohomology H¹ = coker(×2: ℤ → ℤ) = ℤ/2ℤ. This Ext¹ classifies extensions of ℤ/2 by ℤ — there is exactly one non-trivial class, the original sequence. Option A is wrong: free target modules do not make Ext vanish; what matters is whether the source module is projective (ℤ/2 is not). Option D is wrong — ℤ/2 has the explicit projective resolution shown."

- question: "Which statement best explains why Ext^n(M, N) is well-defined — that is, independent of which projective resolution of M is used to compute it?"
  type: multiple-choice
  options:
    - "All projective resolutions of M are isomorphic as chain complexes, so they produce identical cohomology groups"
    - "Any two projective resolutions of M are connected by a chain map unique up to chain homotopy, and chain-homotopic maps induce identical maps on cohomology"
    - "The definition of Ext uses only the module M itself and not any resolution, making independence trivial"
    - "Only one projective resolution of each module exists in any abelian category with enough projectives"
  answer: 1
  explanation: "The comparison lemma guarantees that any two projective resolutions P* and Q* of M are connected by a chain map P* → Q*, and any two such maps are chain-homotopic. Since homotopic chain maps induce the same maps on cohomology, applying Hom(−, N) and taking cohomology gives canonically isomorphic groups regardless of which resolution was used. This is a non-trivial theorem — it is not obvious, and it relies specifically on the projective (or injective) property of the resolution objects. Option A is wrong: resolutions are not isomorphic as complexes, only homotopy equivalent. Option C is wrong: the construction fundamentally requires a resolution. Option D is wrong: resolutions are far from unique."

- question: "The zeroth right derived functor R⁰F of a left exact functor F satisfies R⁰F(A) = F(A), meaning the derived functor construction recovers the original functor at degree zero."
  type: true-false
  answer: true
  explanation: "This confirms the construction is correctly calibrated. For a left exact functor F, applying F to the injective resolution 0 → A → I⁰ → I¹ → ... and taking H⁰ of the resulting complex gives ker(F(I⁰) → F(I¹)). By left exactness of F, this kernel equals F(A) — the same result you would get by just applying F to A directly. The higher derived functors R^nF for n ≥ 1 are genuinely new groups that capture where exactness fails beyond degree zero."

- question: "The value of R^nF(A) depends on which injective resolution of A is chosen, so a careful computation must specify which resolution is being used."
  type: true-false
  answer: false
  explanation: "Independence from the choice of resolution is the central theorem that makes derived functors well-defined as functors of A. Any two injective resolutions of A are connected by a chain map unique up to homotopy, and chain-homotopic maps induce the same maps on cohomology. This independence is not obvious — it requires proof. If R^nF(A) depended on the resolution, it would not be a functor of A at all. The theorem is foundational: it is one of the first results established in any systematic treatment of homological algebra."

- question: "What does it mean for a functor to 'fail to be exact,' and how do derived functors convert this failure into useful algebraic invariants?"
  type: short-answer
  answer: "A functor is exact if it preserves short exact sequences in both directions. Many natural functors are only partially exact: Hom(M, −) is left exact (preserves the beginning of a short exact sequence but may lose surjectivity at the end), and − ⊗ M is right exact (preserves the end but may lose injectivity at the beginning). The derived functors measure what is missing: R^nF(A) extends the truncated exact sequence in the direction where exactness fails, with each degree measuring the obstruction at that level. Ext¹(M, N) classifies extensions; Tor₁(M, N) detects torsion."
  explanation: "The key reframe is that 'failure to be exact' is information, not merely an obstacle. If Hom(M, −) were exact, there would be nothing to measure. The failure creates non-trivial groups that classify algebraic structure: Ext¹ = 0 characterizes projective modules; Tor₁ = 0 characterizes flat modules. Derived functors organize all of module theory around exactness failures, giving a coherent indexed hierarchy of invariants. This is the sense in which homological algebra turns obstructions into computable data."
```

## Explainer

From homology and cohomology, you know that chain complexes and their homology groups detect structural information that is invisible at the level of individual objects. Derived functors are built on the same intuition, but the question they answer is different: instead of asking what is true about a topological space, they ask **how much a functor distorts exact sequences**. This is a question about the functor itself — specifically, about the algebraic information it fails to preserve.

Recall that a functor F between abelian categories is **exact** if it sends short exact sequences to short exact sequences. Many natural functors are only partially exact. The functor Hom(M, −) is **left exact**: given 0 → A → B → C → 0, it produces 0 → Hom(M,A) → Hom(M,B) → Hom(M,C), but the last map need not be surjective. The functor − ⊗ M is **right exact**: it preserves the right end of the sequence but the first map may lose injectivity. The derived functors measure exactly what is lost at the missing end. Right derived functors R^nF (built from injective resolutions) extend the exact sequence to the right; left derived functors L_nF (built from projective resolutions) extend it to the left.

The construction works as follows for right derived functors of a left exact F. Given an object A, choose an **injective resolution**: an exact sequence 0 → A → I⁰ → I¹ → I² → ⋯ where each Iⁿ is an injective object. Apply F to get a (possibly inexact) complex 0 → F(I⁰) → F(I¹) → F(I²) → ⋯. The nth cohomology of this complex is R^nF(A). The zeroth term R⁰F(A) = F(A) recovers the original functor, because F is left exact. The higher terms R^nF(A) for n ≥ 1 are new groups that capture how far F deviates from exactness. That these groups are independent of which injective resolution you chose is the key theorem — any two resolutions are connected by a chain map unique up to homotopy, and homotopic chain maps induce the same maps on cohomology.

The two canonical examples are **Ext** and **Tor**. Ext^n(M, N) = R^n Hom(M, −)(N) is computed by resolving N injectively (or M projectively — both give the same answer, a non-trivial fact). Ext¹(M, N) classifies extensions of M by N, meaning short exact sequences 0 → N → E → M → 0 up to isomorphism of E. Ext²(M, N) classifies obstructions to certain constructions in algebra. **Tor_n(M, N)** = L_n(− ⊗ N)(M) is computed by resolving M projectively and tensoring. Tor₁(M, N) detects torsion: if M = ℤ/kℤ and N = ℤ/lℤ, then Tor₁(M, N) = ℤ/gcd(k,l)ℤ — it measures how much the tensor product "wraps around." When Tor₁(M, N) = 0 for all N, M is flat; when Ext¹(M, N) = 0 for all N, M is projective. Derived functors thus give algebraic invariants that classify module properties and organize homological algebra into a coherent, computable framework.


