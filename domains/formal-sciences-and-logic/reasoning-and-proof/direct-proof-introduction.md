---
id: direct-proof-introduction
title: Introduction to Direct Proof
domain: formal-sciences-and-logic
course: reasoning-and-proof
prerequisites:
  - id: deductive-vs-inductive-reasoning
    type: hard
  - id: conditional-statements-formal
    type: hard
  - id: valid-vs-invalid-arguments
    type: hard
builds-toward:
  - proof-by-contradiction-introduction
  - when-is-something-proven
  - direct-proof
  - proof-structure-and-terminology
tags: [proof, direct-proof, deduction, reasoning]
stage: abstract-reasoning
status: draft
---

# Introduction to Direct Proof

## Core Idea
A direct proof establishes the truth of a statement by starting from known facts, definitions, or previously proven results and reasoning forward step by step until the desired conclusion is reached. To prove "If P, then Q" directly, you assume P is true, then use logical steps to show Q must also be true. Each step must follow from previous steps by known rules or definitions — no gaps, no hand-waving, no "it is obvious." Direct proof is the most straightforward proof strategy and the one you should try first.

## How It's Best Learned
Start with simple numerical proofs: "Prove that the sum of two even numbers is even." Define even: n is even if n = 2k for some integer k. Let a = 2j and b = 2k. Then a + b = 2j + 2k = 2(j + k), which is 2 times an integer, hence even. Walk through each step explicitly. Then have students write their own proofs for similar claims. Emphasize that every step must be justified — writing "so clearly..." without justification is not acceptable.

## Common Misconceptions
- Thinking a proof can start from what you want to prove. A direct proof starts from what you know (the hypothesis) and works toward the conclusion, not the other way around.
- Believing that checking examples constitutes a proof. Showing that 2 + 4 = 6 is even does not prove that all sums of even numbers are even — you need a general argument.
- Assuming proofs must be complicated. Many important proofs are just two or three lines of careful reasoning.

## Questions

```yaml
- question: "To prove 'If n is an odd integer, then n² is odd' by direct proof, what should you assume?"
  type: multiple-choice
  options:
    - "Assume n² is odd"
    - "Assume n is an odd integer"
    - "Assume n² is even"
    - "Assume n is an even integer"
  answer: 1
  explanation: "In a direct proof of 'If P, then Q,' you assume P (the hypothesis) and derive Q (the conclusion). Here P is 'n is an odd integer,' so you assume that and work toward showing n² is odd. Starting from the conclusion (option A) would be working backwards; starting from the negation (options C, D) would be a different proof strategy."

- question: "A direct proof of a statement about all even numbers can be completed by checking the first 100 even numbers."
  type: true-false
  answer: false
  explanation: "Checking specific cases is testing, not proving. A direct proof must work for ALL even numbers simultaneously. You achieve this by using the definition (an even number is 2k for some integer k) and reasoning with the variable k, which represents any integer. The proof then covers every even number at once, not just the ones you checked."

- question: "Write a direct proof that the product of two odd numbers is odd."
  type: short-answer
  answer: "Let a and b be odd. By definition, a = 2j + 1 and b = 2k + 1 for some integers j and k. Then ab = (2j+1)(2k+1) = 4jk + 2j + 2k + 1 = 2(2jk + j + k) + 1. Since 2jk + j + k is an integer, ab has the form 2m + 1, so ab is odd."
  explanation: "The proof follows the direct proof template: assume the hypothesis (a and b are odd), unpack the definition (write each as 2·integer + 1), perform algebra, and show the result matches the definition of the conclusion (the product has the form 2·integer + 1, hence odd). Every step is justified and no cases are left uncovered."
```

## Explainer

A direct proof is the most natural form of mathematical reasoning: you start from what you know and work forward to what you want to show. The strategy is simple in principle — assume the hypothesis, apply definitions and known facts, and arrive at the conclusion. The challenge is in the execution: every step must be justified, and the chain of reasoning must be complete.

Consider a claim like "the sum of two even numbers is even." A direct proof begins by unpacking definitions. What does "even" mean? An integer n is even if n = 2k for some integer k. So let a and b be even: a = 2j and b = 2k for integers j and k. Now compute: a + b = 2j + 2k = 2(j + k). Since j + k is an integer, a + b is 2 times an integer, which means a + b is even. Done.

Notice what happened: you did not check any specific numbers. You did not verify that 2 + 4 = 6 is even, or that 10 + 14 = 24 is even. Instead, you used variables (j and k) that represent any integers, so the proof covers every possible pair of even numbers simultaneously. This is the leap from inductive reasoning (checking cases) to deductive proof (covering all cases at once), and it is exactly what makes the direct proof strategy so powerful.

The structure of a direct proof of "If P, then Q" always follows the same skeleton. Step 1: Assume P. Step 2: Unpack definitions and known facts. Step 3: Reason forward using algebra, logic, or previously proven results. Step 4: Arrive at Q. The proof is complete when you have shown that Q is an unavoidable consequence of P, with no gaps in the reasoning.

A common mistake is to start from the conclusion and work backward. If you are trying to prove "If n is odd, then n² is odd," you should not begin with "n² is odd" and try to derive that n is odd — that would be proving the converse, which is a different statement. Always start from the hypothesis and reason toward the conclusion. There are proof techniques (like proof by contradiction) that start differently, but in a direct proof, the direction is always forward from hypothesis to conclusion.
