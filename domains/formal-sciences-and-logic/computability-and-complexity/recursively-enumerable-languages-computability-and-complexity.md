---
id: recursively-enumerable-languages-computability-and-complexity
title: 'Recursively Enumerable Languages: Semi-Decidability'
domain: formal-sciences-and-logic
course: computability-and-complexity
prerequisites:
- id: recursive-languages
  type: hard
builds-toward:
- turing-degrees-equivalence
- undecidable-problems-examples
tags:
- semi-decidable
- recursively-enumerable
- halting
- verification
stage: formal-systems
status: validated
---

# Recursively Enumerable Languages: Semi-Decidability

## Core Idea
A language is recursively enumerable (RE) if there exists a Turing machine that accepts exactly those strings in the language but may not halt on strings outside the language. RE languages represent problems where 'yes' answers are verifiable but 'no' answers may require infinite computation. Every recursive language is RE, but not vice versa.

## How It's Best Learned
Use the Halting Problem as motivating example: it's RE (simulate and accept if halts) but not recursive. Contrast with problems that are RE and recursive.

## Common Misconceptions
- Confusing 'enumerates' with 'lists in order.' RE means we can verify membership by simulation, not necessarily list in canonical order.
- Thinking RE languages are rarer than recursive. In fact, the complement of an undecidable problem is often not RE.

## Questions

```yaml
- question: "The Halting Problem H = {(M, w) | M halts on w} is recursively enumerable but not recursive. What does this imply about its complement H̄ = {(M, w) | M does not halt on w}?"
  type: multiple-choice
  options:
    - "H̄ is also recursively enumerable, since we can simulate M and accept if it runs forever"
    - "H̄ is recursive, since a machine can detect non-halting by running for a sufficiently long time"
    - "H̄ is not recursively enumerable, because if H̄ were RE we could combine semi-deciders for H and H̄ to decide H, contradicting its undecidability"
    - "H̄ is recursively enumerable but harder than H to semi-decide"
  answer: 2
  explanation: "If H̄ were RE, we would have a semi-decider for H̄ (halts and accepts iff M does NOT halt on w). Combined with the semi-decider for H (simulate M on w; accept if M halts), we could run both in parallel and decide H: whichever semi-decider accepts first gives the answer — and since every input is in exactly one of H and H̄, one must eventually accept. This would make H recursive, contradicting its undecidability. Therefore H̄ cannot be RE. More generally: if L is RE but not recursive, then L̄ is not RE."

- question: "A Turing machine M accepts all strings in language L and loops forever on all strings not in L. What class does L belong to?"
  type: multiple-choice
  options:
    - "Recursive (decidable), because M correctly identifies all members of L"
    - "Not even recursively enumerable, because M provides no information about non-members"
    - "Recursively enumerable (semi-decidable), because M halts and accepts exactly the strings in L, even though it may loop on non-members"
    - "Context-sensitive, because the looping behavior corresponds to a bounded computation"
  answer: 2
  explanation: "The definition of a recursively enumerable (RE) language is exactly this: there exists a Turing machine that halts and accepts on every string in the language, and may loop forever on strings outside the language. M's behavior — accept on L, loop on L̄ — satisfies this definition precisely. The machine gives one-sided answers: 'yes' is confirmed by halting, but 'no' is never confirmed (just never answered). RE does not require the machine to halt on non-members, which is the key distinction from recursive (decidable) languages."

- question: "A language L is recursive (decidable) if and only if both L and its complement L̄ are recursively enumerable."
  type: true-false
  answer: true
  explanation: "This is the key closure theorem for RE languages. (→) If L is recursive, then both L and L̄ are RE: just use the decider for L directly as a semi-decider for L, and use the decider (which always halts) but accept on 'no' answers for L̄. (←) If both L and L̄ are RE, run their semi-deciders in parallel. Every input is in exactly one of L or L̄, so one semi-decider must eventually halt and accept — this gives a decider that always halts, making L recursive. The contrapositive is equally important: if L is RE but not recursive, then L̄ cannot be RE."

- question: "Every recursively enumerable language is also recursive, because any Turing machine that accepts a language can be modified to also reject non-members by detecting loops."
  type: true-false
  answer: false
  explanation: "This is the fundamental misconception about RE languages. There is no general algorithm for detecting that a Turing machine will loop forever — this is precisely the content of the undecidability of the Halting Problem. A Turing machine that accepts L might loop forever on some inputs outside L, and no modification can guarantee it will halt on those inputs without potentially also changing which inputs it accepts. The Halting Problem is RE but not recursive precisely because we can verify 'yes' answers (simulate until halt) but cannot verify 'no' answers in general."

- question: "Explain why the Halting Problem is recursively enumerable but not recursive, using the definitions of semi-decidability and decidability."
  type: short-answer
  answer: "The Halting Problem is RE because there exists a Turing machine that semi-decides it: given input (M, w), simulate M on w. If M halts, accept. This machine halts and correctly accepts every (M, w) pair where M halts on w. It never gives a wrong 'yes' answer. However, if M does not halt on w, the simulation runs forever — the machine loops rather than rejecting. This satisfies the RE definition (accept all yes-instances, may loop on no-instances) but not the recursive definition (which requires halting on all inputs with a correct yes/no answer). The Halting Problem is not recursive because no Turing machine can decide, for every (M, w), whether M halts on w — proven by diagonalization: any claimed decider D can be contradicted by constructing a machine that does the opposite of what D predicts."
  explanation: "The diagonalization proof constructs a machine D' that, on input M, runs D to predict whether M halts on M, then does the opposite. D' on input D': if D says D' halts, D' loops; if D says D' loops, D' halts. Either way D is wrong on this input. This shows no decider D can exist for the Halting Problem, while the simulation argument shows it is RE."
```

## Explainer

You already know what a **recursive (decidable) language** is: a Turing machine that always halts and always gives the correct yes/no answer. Now weaken that requirement in one direction only: the machine must halt and accept when the answer is yes, but it is allowed to run forever when the answer is no. This is **semi-decidability**, and languages with this property are called **recursively enumerable (RE)**. The name comes from an equivalent characterization: a language is RE if and only if some Turing machine can enumerate (print out, one by one) all its members — not necessarily in any particular order, but eventually producing each member.

The relationship to recursive languages is a strict containment. Every recursive language is RE — just ignore the "run forever on no" permission. But there are RE languages that are not recursive. The canonical example is the **Halting Problem**: the set of (M, w) pairs where Turing machine M halts on input w. To verify a "yes" answer, just simulate M on w; if M halts, accept. But to answer "no," you would need to confirm that M runs forever — and no algorithm can do that in general. The Halting Problem is RE but not recursive.

This asymmetry between yes and no has a striking consequence for complements. A language L is recursive if and only if both L and its complement L̄ are RE. This is because if you have a semi-decider for L and a semi-decider for L̄, you can run them in parallel: whichever halts first tells you the answer, guaranteeing termination. If a language is RE but not recursive, its complement cannot be RE at all — otherwise we could combine the two semi-deciders to get a full decider, contradicting undecidability. The complement of the Halting Problem is the prototypical example of a language that is **not** RE.

RE languages form the top of the Chomsky hierarchy: they are exactly what unrestricted Turing machines can recognize. Understanding them sharpens your mental model of what computation can and cannot do. The recursive languages are the "safe" territory — problems we can fully decide. The RE languages are the "one-sided" territory — problems where we can confirm yes answers but may loop on no. And beyond RE lies the truly unrecognizable: problems where no Turing machine gives even a one-sided answer. The boundary between recursive and RE, marked by the Halting Problem, is the deepest fault line in computability theory.
