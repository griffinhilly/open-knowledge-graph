---
id: proving-by-direct-method
title: Proving by Direct Method
domain: mathematics
course: methods-of-proof
prerequisites:
- id: conditional-implication-statements
  type: hard
- id: modus-ponens-and-modus-tollens
  type: soft
- id: universal-quantifier-introduction
  type: soft
builds-toward:
- proving-by-contrapositive
- proving-by-cases
tags:
- proof
- direct proof
- deduction
stage: formal-systems
status: draft
---

# Proving by Direct Method

## Core Idea
Direct proof establishes a conclusion P by assuming the hypothesis H and using logical deduction (modus ponens, substitution, algebra) to reach P. The structure is: assume H is true, then apply valid inferences to derive P. Direct proof is the most straightforward proof method.

## How It's Best Learned
Study well-written proofs and identify the hypothesis, conclusion, and steps of deduction. Write simple proofs and get feedback on clarity and rigor.

## Common Misconceptions
- Confusing assuming the hypothesis with circular reasoning.
- Skipping steps and claiming something is 'obvious'.
- Using the conclusion somewhere in the proof (begging the question).

## Questions

```yaml
- question: "In a direct proof that 'if n is even, then n² is even,' a student writes: 'Let n = 2k. Then n² = 4k² = 2(2k²), which has the form 2m and is therefore even.' Which step is the crucial move that makes this a proof?"
  type: multiple-choice
  options:
    - "Squaring n to get 4k², since this introduces the algebraic structure needed"
    - "Writing n = 2k, because this unpacks the hypothesis into usable algebraic form"
    - "Noting that 4k² = 2(2k²), since this is where the conclusion is established"
    - "Concluding that n² is even, since this names the result"
  answer: 1
  explanation: "The key move is unpacking the hypothesis: writing 'n is even' as 'n = 2k for some integer k.' This transforms an abstract property into a concrete algebraic object that can be manipulated. Everything that follows — squaring, factoring, recognizing the form 2m — is routine algebra. Direct proof works by finding the algebraic machinery hidden inside the hypothesis; that unpacking step is where the proof actually begins."

- question: "A student attempting to prove 'if n² is even, then n is even' writes: 'Assume n² is even. Since n² is even, n must be even, so n is even.' What logical error did the student commit?"
  type: multiple-choice
  options:
    - "Assuming the hypothesis — the student should not assume anything in a direct proof"
    - "Begging the question — the student used the conclusion ('n is even') as a step in the argument"
    - "Circular reasoning — the student repeated the hypothesis instead of using it"
    - "A valid proof — the step 'n must be even' follows directly from 'n² is even'"
  answer: 1
  explanation: "The step 'since n² is even, n must be even' is precisely the conclusion the student is supposed to prove — not a logical step that follows from anything established so far. This is begging the question (petitio principii): assuming the conclusion as part of the argument for the conclusion. Assuming the hypothesis (H) is correct and not circular; the error is assuming P (the conclusion) in order to prove P. Notably, this particular theorem is hard to prove by direct method — contrapositive ('if n is odd, then n² is odd') works more cleanly."

- question: "In a direct proof of 'if H then P,' assuming H at the start of the proof is a form of circular reasoning."
  type: true-false
  answer: false
  explanation: "Assuming H is exactly what the conditional statement licenses you to do — you are not claiming H is universally true, but showing what follows under the assumption that H holds. Circular reasoning would be using P (the conclusion) somewhere in the argument to establish P. Assuming the hypothesis is the starting point of every direct proof; using the conclusion is the error. The distinction is between 'assume H to prove P' (correct) and 'assume P to prove P' (circular)."

- question: "Direct proof is the most effective method for every conditional statement of the form 'if H then P.'"
  type: true-false
  answer: false
  explanation: "Direct proof works well when the hypothesis, when unpacked, contains the algebraic or logical machinery needed to produce the conclusion. When the hypothesis and conclusion feel 'far apart' — when reasoning forward from H doesn't naturally lead to P — an indirect method (proof by contrapositive or proof by contradiction) is usually cleaner. For example, 'if n² is even then n is even' is awkward by direct proof but elegant by contrapositive. Choosing the right proof strategy is itself a mathematical skill."

- question: "What is the difference between 'assuming the hypothesis' and 'begging the question,' and why does only one of them make a direct proof invalid?"
  type: short-answer
  answer: "Assuming the hypothesis means taking H as given at the start and reasoning forward to show P follows — this is exactly what proving 'if H then P' requires. Begging the question means using P (the conclusion) as a step in the argument for P — sneaking in what you're trying to prove as if it were already established. Only the second is logically invalid: a proof of 'if H then P' is supposed to show that P follows from H, so using P before it's been established makes the argument circular. Assuming H doesn't make the proof circular because H and P are different statements."
  explanation: "The key is which statement you're assuming. You are licensed to assume H because that's the hypothesis of the conditional you're proving — you're not proving H is always true. But you haven't established P yet, so you cannot use P as a reason for P. Direct proof is essentially an exercise in following the logical implications of H step by step until P emerges — any step that relies on P before that emergence is circular."
```

## Explainer

Most mathematical theorems have the form "if H, then P" — a conditional statement. You've seen this in your study of conditional implication: the claim is not that H or P is unconditionally true, but that P follows from H. **Direct proof** is the method of taking that conditional seriously: assume H is true, then reason forward step by step until you reach P. Every step must be a valid logical inference — substitution, algebraic manipulation, applying a known theorem, or an application of modus ponens.

Here is a simple example. Theorem: if n is an odd integer, then n² is odd. Direct proof: assume n is odd. By definition of odd, n = 2k + 1 for some integer k. Then n² = (2k + 1)² = 4k² + 4k + 1 = 2(2k² + 2k) + 1. Since 2k² + 2k is an integer, n² has the form 2m + 1 and is therefore odd. The structure is: unpack the hypothesis (n is odd means n = 2k + 1), compute (square it), recognize the pattern (it's 2m + 1), invoke the definition (therefore odd). That's a direct proof.

A key confusion for beginners is whether assuming H is circular. It is not. Circular reasoning would be using P in order to prove P — sneaking the conclusion into the argument. Assuming H to prove P is exactly what the conditional "if H then P" licenses you to do. You are not asserting H is always true; you are saying "under the assumption that H holds, here is why P must also hold." This is precisely the force of modus ponens, which you've studied: from H and H → P, conclude P.

The other common failure mode is **begging the question** — using the conclusion at some step in the argument. For example, to prove that if n² is even then n is even, you might be tempted to say "since n² is even, n must be even." That is just restating the conclusion, not proving it. A correct direct proof would need more structure (in fact, this theorem is easier by contrapositive). Direct proof works best when the hypothesis, when unpacked, contains exactly the algebraic or logical machinery needed to produce the conclusion. When the hypothesis and conclusion feel far apart — when you'd need to "go backward" from the conclusion to find the argument — an indirect method (contrapositive or contradiction) is usually cleaner.
