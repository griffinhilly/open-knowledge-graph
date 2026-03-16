---
id: recursively-enumerable-languages-properties
title: Properties of Recursively Enumerable Languages
domain: formal-sciences-and-logic
course: computability-and-complexity
prerequisites:
- id: re-and-co-re-languages
  type: hard
- id: decidability-and-semi-decidability
  type: hard
builds-toward:
- enumeration-and-index-sets
tags:
- r.e.-languages
- closure-properties
- computability
stage: advanced
status: draft
---

# Properties of Recursively Enumerable Languages

## Core Idea
The class RE of recursively enumerable languages is closed under union and intersection but not complement (unless the language is also in co-RE, i.e., decidable). This asymmetry—verification closure without complement closure—reflects the asymmetry between 'semi-deciding' and 'deciding' and motivates the study of the recursion-theoretic hierarchy.

## Explainer

You already know the essential picture: a language L is **recursively enumerable** (RE) if some Turing machine semi-decides it — halting and accepting on every string in L, but possibly running forever on strings not in L. A language is **decidable** (recursive) if there is a machine that always halts, accepting or rejecting every input. The gap between these classes is precisely the asymmetry in closure properties you are now studying.

**Union** is closed in RE. If M₁ semi-decides L₁ and M₂ semi-decides L₂, you can semi-decide L₁ ∪ L₂ by running M₁ and M₂ in parallel (dovetailing their steps). If either machine accepts, you accept. If neither accepts, you run forever — exactly the right behavior, since a string outside both L₁ and L₂ will never be accepted. **Intersection** is also closed: run M₁ and M₂ in parallel and accept only when both accept. Both constructions preserve the semi-deciding contract because acceptance is a positive event you can detect when it happens.

**Complement** breaks this. To semi-decide the complement of L, you need to recognize strings not in L. But "not accepted by M" could mean M rejects (which is fine) or M loops forever (which you cannot detect). You can never observe a non-terminating loop as a positive event — you would have to wait forever. Formally, RE is not closed under complement because the halting problem's complement is not RE: there is no machine that accepts exactly those (M, x) pairs for which M does not halt on x. If RE were closed under complement, the halting problem would be decidable (run a machine for L and a machine for co-L in parallel; one will halt), contradicting undecidability.

The deep structural point is that RE ∩ co-RE = decidable languages. A language is decidable if and only if both it and its complement are RE — meaning you can verify both membership and non-membership. This gives a clean picture of what semi-decidability buys you: you can accumulate positive evidence forever but cannot convert finite non-evidence into a rejection. The recursion-theoretic **arithmetical hierarchy** extends this idea: define Σ₁ = RE, Π₁ = co-RE, and then alternate quantifiers to produce Σₙ and Πₙ classes each strictly harder than the last. Every level is closed under union and intersection, and the gap to the next level is precisely the inability to take complements. RE's closure properties are thus not a quirk — they are the opening chapter of a rich structural theory of computational complexity beyond decidability.

