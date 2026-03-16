---
id: ring-homomorphisms
title: Ring Homomorphisms
domain: mathematics
course: abstract-algebra
prerequisites:
- id: ring-definition-examples
  type: hard
builds-toward:
- subrings-ideals
- quotient-rings
tags:
- ring-homomorphism
- kernel
- ideal
stage: advanced
status: draft
---

# Ring Homomorphisms

## Core Idea
A ring homomorphism φ: R → S preserves both addition and multiplication: φ(a + b) = φ(a) + φ(b) and φ(ab) = φ(a)φ(b). The kernel of φ is an ideal of R.

## Explainer

A **ring homomorphism** is the natural notion of a structure-preserving map between rings. From your study of ring definitions, you know that a ring comes equipped with two operations: addition and multiplication. A homomorphism φ: R → S must respect both simultaneously. This is a stronger condition than just being a group homomorphism on the additive side — it also requires φ(ab) = φ(a)φ(b). Think of it as a translation: φ converts ring-theoretic statements in R into ring-theoretic statements in S, with the guarantee that calculations come out the same on either side of the translation.

A simple example anchors the idea. Consider the map φ: ℤ → ℤ/nℤ that sends each integer to its residue class mod n. Check the conditions: φ(a + b) = (a + b) mod n = (a mod n) + (b mod n) = φ(a) + φ(b). Similarly φ(ab) = ab mod n = (a mod n)(b mod n) = φ(a)φ(b). This map is a surjective ring homomorphism, and it is the prototype for all quotient maps. More exotic examples: the evaluation map φ: ℝ[x] → ℝ sending p(x) ↦ p(3) is a homomorphism (the constant 3 is fixed), and the inclusion ℤ ↪ ℚ is an injective homomorphism.

The **kernel** ker(φ) = {r ∈ R : φ(r) = 0} captures how much information φ forgets. A critical fact is that the kernel is always an **ideal** of R — not just a subring, but a subset I ⊆ R with the absorption property: if i ∈ I and r ∈ R, then ri ∈ I and ir ∈ I. The absorption property is forced by homomorphism: if φ(i) = 0 then φ(ri) = φ(r)φ(i) = φ(r)·0 = 0. This is why ideals arise naturally in ring theory — they are exactly the objects that can be kernels. The parallel with group theory is exact: normal subgroups are kernels of group homomorphisms, ideals are kernels of ring homomorphisms.

The **image** im(φ) is a subring of S, and the **First Isomorphism Theorem** ties everything together: R/ker(φ) ≅ im(φ). The quotient ring R/I, which you will study next, is constructed precisely to make the natural map R → R/I a homomorphism with kernel I. So understanding homomorphisms is the same thing as understanding ideals and quotient rings — these three concepts form a single interconnected cluster, and the First Isomorphism Theorem is the statement that they are all saying the same thing from different angles.
