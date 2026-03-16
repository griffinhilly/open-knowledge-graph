---
id: axiom-of-choice
title: Axiom of Choice
domain: formal-sciences-and-logic
course: set-theory
prerequisites:
- id: zfc-axioms-overview
  type: hard
- id: binary-relations
  type: soft
- id: set-operations
  type: soft
- id: equivalence-relations
  type: soft
builds-toward:
- well-ordering-theorem
- zorns-lemma
- cardinal-arithmetic
tags:
- ZFC
- axiom of choice
- choice function
- AC
- independence
stage: formal-systems
status: validated
---

# Axiom of Choice

## Core Idea
The axiom of choice (AC) states that for any collection of non-empty sets {A_i : i ∈ I}, there exists a choice function f satisfying f(i) ∈ A_i for every i ∈ I. AC is required whenever one needs to simultaneously select elements from infinitely many sets without an explicit selection rule. It is independent of ZF — neither provable nor refutable from the other axioms — yet accepted in ZFC. AC is equivalent over ZF to both Zorn's lemma and the well-ordering theorem; it implies non-constructive results like the existence of non-measurable sets (Vitali sets) and bases for all vector spaces.

## How It's Best Learned
Start with finite families (where choice is trivial) and countable families (where AC is provable from ZF). Study constructions that require full AC: bases for vector spaces over arbitrary fields, the fact that every surjection has a right inverse, and Tychonoff's theorem for products. Then study the equivalences with Zorn's lemma and the well-ordering theorem.

## Common Misconceptions
- For finite or countable families, choice is provable in ZF without the additional axiom.
- AC does not specify which element to choose — it only asserts that a choice exists; it is inherently non-constructive.
- AC is consistent with ZF; accepting it does not introduce contradictions.

## Explainer

From your study of ZFC, you know that most axioms — extensionality, pairing, union, power set, infinity — describe how to *construct* sets from other sets. The Axiom of Choice is different. It does not build anything; it asserts that something *exists* without telling you what it is. Specifically, it says: given any collection of non-empty sets, you can simultaneously pick one element from each. For finite collections, this is obvious — just describe your picks. For countably infinite collections, you can often describe a rule (e.g., "pick the smallest element" works when each set contains natural numbers). The axiom becomes genuinely necessary when the collection is *uncountably* infinite and you have no uniform rule for picking.

The most natural setting where AC is needed is **linear algebra over arbitrary fields**. Every vector space has a basis — a maximal linearly independent set. For ℝ over ℚ (viewing the reals as a vector space over the rationals), such a basis (called a **Hamel basis**) exists but cannot be explicitly described; its existence requires AC. Similarly, AC is equivalent to saying that every surjective function has a right inverse: if f: A → B is surjective, there is a g: B → A with f(g(b)) = b for all b. This "section" g chooses, for each b, one element of the fiber f⁻¹(b). For uncountable B this requires simultaneous choices — exactly what AC provides.

AC is equivalent to two other fundamental statements, and you should know all three:
- **Well-ordering theorem**: every set can be well-ordered (every non-empty subset has a least element). This lets you do transfinite induction on any set at all.
- **Zorn's lemma**: if every chain in a partially ordered set has an upper bound, then the set has a maximal element. This is the form used in algebra to prove things like "every ideal is contained in a maximal ideal" and "every vector space has a basis."

All three are provably equivalent over ZF, meaning any one implies the other two. The proofs of these equivalences (AC → well-ordering → Zorn → AC) are important metatheorems in set theory. The well-ordering theorem is the most "shocking" — it says that even the reals can be well-ordered, though no one can exhibit such an ordering explicitly.

The price of AC is **non-constructivity**. The Vitali set construction shows that AC implies there are sets of real numbers that are not Lebesgue measurable — sets whose "size" cannot be consistently assigned. The Banach–Tarski paradox goes further: using AC, a solid ball can be partitioned into finitely many pieces and reassembled into two balls of the same size as the original. None of these are physical impossibilities (they involve non-measurable sets that cannot be physically realized), but they signal that AC authorizes highly non-explicit mathematical objects. Accepting ZFC, which includes AC, is a choice — one that virtually all working mathematicians make because the mathematics it unlocks (transfinite arithmetic, algebraic structures, topology) is so powerful and coherent.

