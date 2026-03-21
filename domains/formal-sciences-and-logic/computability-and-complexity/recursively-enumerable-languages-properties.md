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

## Questions

```yaml
- question: "Suppose L₁ and L₂ are both recursively enumerable but neither is decidable. Which of the following is guaranteed to also be recursively enumerable?"
  type: multiple-choice
  options:
    - "The complement of L₁"
    - "L₁ minus L₂ (strings in L₁ but not in L₂)"
    - "L₁ intersected with L₂"
    - "L₁ symmetric difference with L₂"
  answer: 2
  explanation: "RE is closed under intersection. If M₁ semi-decides L₁ and M₂ semi-decides L₂, running both in parallel and accepting only when both accept semi-decides L₁ ∩ L₂. This works because acceptance is a positive event you can detect. RE is NOT closed under complement (option A), set difference (option B — L₁ \\ L₂ = L₁ ∩ co-L₂, and co-L₂ may not be RE), or symmetric difference (option D — which involves complements). Only union and intersection preserve RE membership."

- question: "Why does the dovetailing argument that works for RE union fail when applied to complement?"
  type: multiple-choice
  options:
    - "Dovetailing requires both machines to eventually halt, which they may not do for languages in RE"
    - "To semi-decide the complement, you need to accept strings not in L, but you can only recognize non-acceptance if the machine halts and rejects — you cannot detect an infinite loop as a positive event"
    - "Dovetailing works for complement too; the problem is that complement is not preserved under parallel composition"
    - "The complement construction requires deterministic machines, but dovetailing only works for nondeterministic machines"
  answer: 1
  explanation: "For union, dovetailing works because acceptance is a positive event you can detect when it happens — if either machine accepts, accept. For complement, you need to recognize strings NOT in L. But 'not accepted by M' has two causes: M rejects (detectable) or M loops forever (undetectable). You cannot observe a non-halting loop as a positive event — you would have to wait forever to confirm it. There is no computational signal that tells you 'this machine will never halt,' which is precisely why the halting problem's complement is not RE."

- question: "A language L is decidable if and only if both L and its complement are recursively enumerable."
  type: true-false
  answer: true
  explanation: "This is the characterization RE ∩ co-RE = decidable. If L is decidable, a machine that always halts witnesses both L and co-L as semi-decidable. Conversely, if both L and co-L are RE (say, semi-decided by M and M'), run both in parallel. Every input is in either L or co-L, so exactly one of M or M' will eventually accept. When one accepts, halt. This gives a decider. The argument crucially uses that one of them will halt — you just don't know which one will go first."

- question: "Since RE is closed under both union and intersection, it follows by De Morgan's laws that RE must also be closed under complement."
  type: true-false
  answer: false
  explanation: "De Morgan's laws apply to sets but don't transfer computational closure properties. RE closure under union and intersection does not imply closure under complement because the complement of an RE language is not necessarily RE — it may be in co-RE but not RE itself. If RE were closed under complement, then every RE language would be decidable (run the RE machine and the co-RE machine in parallel; one will halt), which would mean RE = co-RE = decidable, contradicting the undecidability of the halting problem."

- question: "Explain why the inability to detect non-termination is the fundamental barrier to RE closure under complement."
  type: short-answer
  answer: "A Turing machine M semi-decides L: it halts and accepts on every string in L, but on strings not in L it either halts-and-rejects or loops forever. To semi-decide the complement co-L, you need a machine that accepts exactly the strings M does NOT accept. But 'M does not accept x' could mean M halts-and-rejects (detectable) or M runs forever (undetectable). There is no finite computation that can distinguish 'M will reject at step 10,000' from 'M will loop for all eternity' — both look the same up to any finite number of steps. You cannot convert non-acceptance into acceptance without solving the halting problem."
  explanation: "The asymmetry is fundamental: acceptance is observable (you see the 'accept' event) but non-acceptance by a non-halting machine is not observable (you see nothing, forever). RE captures exactly the 'verifiable' languages — you can verify membership by running long enough to see an accept. Closing under complement would require verifying non-membership, which requires detecting infinite loops, which the halting problem shows is impossible."
```

## Explainer

You already know the essential picture: a language L is **recursively enumerable** (RE) if some Turing machine semi-decides it — halting and accepting on every string in L, but possibly running forever on strings not in L. A language is **decidable** (recursive) if there is a machine that always halts, accepting or rejecting every input. The gap between these classes is precisely the asymmetry in closure properties you are now studying.

**Union** is closed in RE. If M₁ semi-decides L₁ and M₂ semi-decides L₂, you can semi-decide L₁ ∪ L₂ by running M₁ and M₂ in parallel (dovetailing their steps). If either machine accepts, you accept. If neither accepts, you run forever — exactly the right behavior, since a string outside both L₁ and L₂ will never be accepted. **Intersection** is also closed: run M₁ and M₂ in parallel and accept only when both accept. Both constructions preserve the semi-deciding contract because acceptance is a positive event you can detect when it happens.

**Complement** breaks this. To semi-decide the complement of L, you need to recognize strings not in L. But "not accepted by M" could mean M rejects (which is fine) or M loops forever (which you cannot detect). You can never observe a non-terminating loop as a positive event — you would have to wait forever. Formally, RE is not closed under complement because the halting problem's complement is not RE: there is no machine that accepts exactly those (M, x) pairs for which M does not halt on x. If RE were closed under complement, the halting problem would be decidable (run a machine for L and a machine for co-L in parallel; one will halt), contradicting undecidability.

The deep structural point is that RE ∩ co-RE = decidable languages. A language is decidable if and only if both it and its complement are RE — meaning you can verify both membership and non-membership. This gives a clean picture of what semi-decidability buys you: you can accumulate positive evidence forever but cannot convert finite non-evidence into a rejection. The recursion-theoretic **arithmetical hierarchy** extends this idea: define Σ₁ = RE, Π₁ = co-RE, and then alternate quantifiers to produce Σₙ and Πₙ classes each strictly harder than the last. Every level is closed under union and intersection, and the gap to the next level is precisely the inability to take complements. RE's closure properties are thus not a quirk — they are the opening chapter of a rich structural theory of computational complexity beyond decidability.

