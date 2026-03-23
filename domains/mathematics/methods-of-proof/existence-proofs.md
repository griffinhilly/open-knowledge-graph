---
id: existence-proofs
title: Existence Proofs
domain: mathematics
course: methods-of-proof
prerequisites:
- id: proof-by-contradiction
  type: soft
tags:
- existence
- proof
- quantifiers
stage: formal-systems
status: validated
---

# Existence Proofs

## Core Idea
An existence proof establishes that an object satisfying certain properties exists. This can be constructive (exhibiting the object explicitly) or non-constructive (showing non-existence leads to contradiction). Both are valid.

## Questions

```yaml
- question: "A proof proceeds as follows: 'Either √2^√2 is rational (done — take a = b = √2), or it is irrational. If irrational, then (√2^√2)^√2 = √2² = 2 is rational. Either way, an example exists.' The proof never determines which case holds. This proof is best described as:"
  type: multiple-choice
  options:
    - "Invalid — a proof of existence must identify and exhibit the specific witnessing object"
    - "A valid non-constructive existence proof that establishes existence via a dilemma without pinpointing the witness"
    - "Incomplete — it would become a valid proof once a calculation resolves which case holds"
    - "A proof by induction, since it considers two cases and builds to a conclusion"
  answer: 1
  explanation: "This is the classic example of a non-constructive existence proof. It proves that at least one of two specific values is the witness, but never determines which one — and this uncertainty is irrelevant to validity. In mainstream mathematics, logical correctness is the standard, not the ability to compute or exhibit the object. Option A expresses the constructivist objection, which is a minority philosophical position, not a mainstream mathematical requirement."

- question: "A constructive existence proof differs from a non-constructive one primarily in that:"
  type: multiple-choice
  options:
    - "A constructive proof uses contradiction to derive the object; a non-constructive proof builds it directly"
    - "A constructive proof is accepted in mainstream mathematics; a non-constructive proof is not"
    - "A constructive proof explicitly exhibits an object satisfying the required property"
    - "A constructive proof applies only to finite mathematical objects, not infinite sets"
  answer: 2
  explanation: "A constructive proof exhibits the actual witness: to prove a prime greater than 100 exists, exhibit 101. A non-constructive proof establishes existence indirectly — typically by showing that non-existence leads to a contradiction. Both are accepted in mainstream mathematics (option B is wrong). Option A reverses the typical association: contradiction is often used in non-constructive proofs, not constructive ones."

- question: "In a non-constructive existence proof, it is possible to know that an object with property P exists while being unable to determine which specific object satisfies P."
  type: true-false
  answer: true
  explanation: "The √2^√2 example demonstrates this precisely: the proof establishes that a rational number of the form a^b (with a, b irrational) exists, but leaves open which of the two candidates is the witness. Mathematical knowledge of existence and computational ability to identify the witness are distinct."

- question: "Non-constructive existence proofs are considered invalid in mainstream mathematics because they fail to produce a concrete witnessing object."
  type: true-false
  answer: false
  explanation: "This is the constructivist position, not mainstream mathematics. Constructivism (associated with Brouwer and others) holds that existence requires constructibility, but it is a minority philosophical view. Mainstream mathematics accepts non-constructive proofs fully — logical validity, not computability, is the criterion. Many important existence results in analysis and algebra are non-constructive."

- question: "What is the philosophical objection to non-constructive existence proofs, and why does mainstream mathematics accept them anyway?"
  type: short-answer
  answer: "Constructivists argue that mathematical existence should require the ability to construct or compute the object — a proof that something 'must exist' because its absence leads to contradiction is epistemically empty if you cannot exhibit it. Mainstream mathematics accepts non-constructive proofs because the standard of proof is logical validity, not computability. If assuming non-existence leads to a contradiction, classical logic guarantees the object exists. Whether this satisfies philosophical intuitions about 'real' existence is a separate question from mathematical correctness."
  explanation: "This debate matters practically: constructive proofs give you an algorithm; non-constructive proofs only guarantee existence. In computer science and applied mathematics, constructive existence is often more useful. But for pure mathematics, non-constructive proofs extend the range of provable results significantly — some truths can only be proven non-constructively."
```

## Explainer

In mathematics, an **existence proof** answers the question "does there exist an object satisfying property P?" with a definitive yes. What counts as a valid answer — and which kind of answer is philosophically satisfying — has been debated by mathematicians for over a century, making existence proofs one of the most intellectually interesting topics in the methods-of-proof toolkit.

The most direct approach is a **constructive proof**: you actually exhibit the object. To prove there exists a prime number greater than 100, you can simply observe that 101 is prime and 101 > 100. Done. The object is in hand. Constructive proofs are the gold standard when available, because they not only confirm existence but also give you something to work with. If you need an algorithm, a specific value, or a counterexample, a constructive proof delivers it directly.

The alternative is a **non-constructive proof**: you show that the object's non-existence leads to a contradiction, and therefore it must exist — without ever producing it. You're familiar with this pattern from proof by contradiction. A famous example is the proof that there exist irrational numbers a and b such that aᵇ is rational. Consider √2^√2. Either this is rational (done — take a = b = √2) or it is irrational. If irrational, then (√2^√2)^√2 = √2² = 2, which is rational. So in either case we have an example — but we never determined which case holds. The object exists; we just don't know which one.

This non-constructive style can feel philosophically unsatisfying: you've proven something exists without ever finding it. Some mathematicians (constructivists) reject non-constructive proofs on principle. In mainstream mathematics, however, both methods are fully accepted. What makes an existence proof valid is logical correctness, not the ability to compute the witness. When you write an existence proof, always ask: is this constructive or non-constructive? If non-constructive, be explicit that you're using contradiction, and make sure the argument is airtight — you're asserting something exists that you cannot touch.
