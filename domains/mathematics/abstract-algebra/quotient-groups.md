---
id: quotient-groups
title: Quotient Groups
domain: mathematics
course: abstract-algebra
prerequisites:
- id: normal-subgroups
  type: hard
builds-toward:
- first-isomorphism-theorem-groups
- second-isomorphism-theorem-groups
tags:
- quotient
- coset-multiplication
- G/N
stage: advanced
status: draft
---

# Quotient Groups

## Core Idea
If N is a normal subgroup of G, the set of cosets G/N forms a group under coset multiplication: (aN)(bN) = (ab)N. The quotient group G/N has order |G| / |N|.

## Explainer

To understand quotient groups, start with what you already know about cosets: given a subgroup N of G, the left cosets aN = {an : n ∈ N} partition G into equal-sized pieces. The crucial question is: can these pieces themselves form a group? The answer is yes — but only when N is **normal**, meaning aN = Na for every a ∈ G. Normality is exactly what is needed for coset multiplication to be well-defined.

Here is why normality matters. If you try to multiply two cosets by picking representatives — compute (aN)(bN) = (ab)N — you need the result to be independent of which representatives you chose. If you had picked a' = an₁ and b' = bn₂ instead, you'd compute (a'b')N = (an₁bn₂)N. For this to equal (ab)N, you need n₁b to equal b times something in N — that is, b⁻¹n₁b ∈ N for all n₁ ∈ N. This is exactly the condition that N is closed under conjugation by elements of G, which is precisely the definition of a normal subgroup. Without normality, the multiplication rule breaks down and you don't get a well-defined group structure.

A canonical example: take G = ℤ₆ = {0,1,2,3,4,5} under addition, and N = {0,3}. The cosets are {0,3}, {1,4}, {2,5}. The quotient G/N has three elements and is isomorphic to ℤ₃. What the quotient is doing conceptually: it "collapses" N to zero, treats elements that differ by an element of N as equivalent, and what survives is the structure that remains after that identification. The **order formula** |G/N| = |G|/|N| follows directly from the partition: there are |G|/|N| cosets, each of size |N|.

The quotient group captures the idea of "G modulo the symmetry described by N." If N encodes some kind of equivalence — elements that are "the same" for some purpose — then G/N is the group you get when you stop distinguishing between equivalent elements. This idea leads directly to the **First Isomorphism Theorem**: whenever you have a group homomorphism φ: G → H, the image is isomorphic to G/ker(φ). The kernel is always a normal subgroup, and the quotient group is precisely the image of G under φ, with all the "collapsing" made explicit. Quotient groups are thus the bridge between subgroup structure and the structure-preserving maps between groups.
