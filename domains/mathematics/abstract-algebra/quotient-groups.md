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
status: validated
---

# Quotient Groups

## Core Idea
If N is a normal subgroup of G, the set of cosets G/N forms a group under coset multiplication: (aN)(bN) = (ab)N. The quotient group G/N has order |G| / |N|.

## Questions

```yaml
- question: "Let H be a subgroup of G that is NOT normal. Why can't coset multiplication (aH)(bH) = (ab)H define a group structure on the set of left cosets of H?"
  type: multiple-choice
  options:
    - "The cosets of H don't all have the same size, so a consistent group operation cannot be defined"
    - "The product (ab)H may depend on which representatives a and b you pick, so the operation is not well-defined"
    - "The cosets of H do not partition G into disjoint pieces"
    - "The set of cosets is too large to form a group"
  answer: 1
  explanation: "When you define (aH)(bH) = (ab)H, you need the result to be independent of representative choice. If you replace a with a' = an₁ and b with b' = bn₂, you get (a'b')H = (an₁bn₂)H. This equals (ab)H only if b⁻¹n₁b ∈ H for all n₁ ∈ H — exactly the conjugation-closure condition that defines normality. Options A and C are both false: cosets of ANY subgroup always partition G into pieces of equal size (this follows from basic coset properties, not from normality)."

- question: "In G = ℤ₁₂ (integers mod 12 under addition) with N = {0, 4, 8}, what is the order of the quotient group G/N?"
  type: multiple-choice
  options:
    - "12 — the quotient group has the same order as G"
    - "3 — the quotient group has the same order as N"
    - "4 — the order equals |G| / |N|"
    - "This quotient cannot be formed because N is not normal in ℤ₁₂"
  answer: 2
  explanation: "The order formula |G/N| = |G| / |N| gives 12/3 = 4. The quotient group has 4 cosets: {0,4,8}, {1,5,9}, {2,6,10}, {3,7,11}. Since ℤ₁₂ is abelian, every subgroup is automatically normal (option D is wrong). Beginners often confuse the order of N with the order of the quotient — but G/N has |G|/|N| elements, not |N| elements."

- question: "Any subgroup N of a group G can be used to form a quotient group G/N, because the cosets of any subgroup always partition G."
  type: true-false
  answer: false
  explanation: "It is true that cosets of ANY subgroup partition G — that is a general property of subgroups, not specific to normal ones. However, forming a *group* on those cosets requires the multiplication rule (aN)(bN) = (ab)N to be well-defined, independent of representative choice. This is only guaranteed when N is a normal subgroup. The partition exists for any subgroup; the valid group structure on the partition requires normality."

- question: "In the quotient group G/N, the coset N itself (the coset of the identity element e) plays the role of the identity element of G/N."
  type: true-false
  answer: true
  explanation: "The coset eN = N serves as the identity in G/N because (aN)(eN) = (ae)N = aN and (eN)(aN) = (ea)N = aN for any coset aN. This is consistent with the conceptual picture: G/N treats all elements of N as equivalent to the identity, and N itself is the equivalence class representing 'zero.' The identity of the quotient group is always the coset containing the identity of G."

- question: "Explain why the quotient group G/N can be thought of as 'G with N collapsed to the identity.' What is being identified with what, and how does normality make this possible?"
  type: short-answer
  answer: "G/N treats any two elements g₁ and g₂ as equivalent whenever g₁⁻¹g₂ ∈ N — that is, whenever they differ by an element of N. All elements of N are identified with the identity (they all land in the same coset, N = eN). The group structure on these equivalence classes is well-defined precisely because N is normal: normality ensures that if you replace a group element with an equivalent one, the products you compute stay in the same equivalence class. Without normality, shifting representatives could land you in a different coset, making the group operation ambiguous."
  explanation: "Forming a quotient means declaring an equivalence relation 'g₁ ~ g₂ iff g₁⁻¹g₂ ∈ N' and asking whether the group operation is compatible with it — equivalent inputs must yield equivalent outputs. This compatibility is exactly what normality provides. A non-normal subgroup still defines an equivalence relation on G, but multiplication is not compatible with it, so you have a set of cosets but not a group."
```

## Explainer

To understand quotient groups, start with what you already know about cosets: given a subgroup N of G, the left cosets aN = {an : n ∈ N} partition G into equal-sized pieces. The crucial question is: can these pieces themselves form a group? The answer is yes — but only when N is **normal**, meaning aN = Na for every a ∈ G. Normality is exactly what is needed for coset multiplication to be well-defined.

Here is why normality matters. If you try to multiply two cosets by picking representatives — compute (aN)(bN) = (ab)N — you need the result to be independent of which representatives you chose. If you had picked a' = an₁ and b' = bn₂ instead, you'd compute (a'b')N = (an₁bn₂)N. For this to equal (ab)N, you need n₁b to equal b times something in N — that is, b⁻¹n₁b ∈ N for all n₁ ∈ N. This is exactly the condition that N is closed under conjugation by elements of G, which is precisely the definition of a normal subgroup. Without normality, the multiplication rule breaks down and you don't get a well-defined group structure.

A canonical example: take G = ℤ₆ = {0,1,2,3,4,5} under addition, and N = {0,3}. The cosets are {0,3}, {1,4}, {2,5}. The quotient G/N has three elements and is isomorphic to ℤ₃. What the quotient is doing conceptually: it "collapses" N to zero, treats elements that differ by an element of N as equivalent, and what survives is the structure that remains after that identification. The **order formula** |G/N| = |G|/|N| follows directly from the partition: there are |G|/|N| cosets, each of size |N|.

The quotient group captures the idea of "G modulo the symmetry described by N." If N encodes some kind of equivalence — elements that are "the same" for some purpose — then G/N is the group you get when you stop distinguishing between equivalent elements. This idea leads directly to the **First Isomorphism Theorem**: whenever you have a group homomorphism φ: G → H, the image is isomorphic to G/ker(φ). The kernel is always a normal subgroup, and the quotient group is precisely the image of G under φ, with all the "collapsing" made explicit. Quotient groups are thus the bridge between subgroup structure and the structure-preserving maps between groups.
