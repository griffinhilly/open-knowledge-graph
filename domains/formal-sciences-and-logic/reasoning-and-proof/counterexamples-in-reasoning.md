---
id: counterexamples-in-reasoning
title: Counterexamples in Reasoning
domain: formal-sciences-and-logic
course: reasoning-and-proof
prerequisites:
  - id: valid-vs-invalid-arguments
    type: hard
  - id: all-some-none
    type: soft
builds-toward:
  - conjectures-and-testing
  - proof-by-contradiction-introduction
  - counterexamples-and-disproofs
  - counterexample-and-refutation
tags: [counterexamples, disproof, reasoning, falsification]
stage: abstract-reasoning
status: draft
---

# Counterexamples in Reasoning

## Core Idea
A counterexample is a specific case that proves a general statement false. If someone claims "all prime numbers are odd," the number 2 is a counterexample — it is prime and even. One counterexample is all it takes to destroy a universal claim. Counterexamples are the primary tool for disproving conjectures and showing arguments are invalid. Learning to search for counterexamples systematically is as important as learning to construct proofs — it is the critical thinking skill that prevents you from accepting false claims.

## How It's Best Learned
Start with obvious false generalizations and have students find counterexamples: "All numbers ending in 5 are divisible by 5" (true — no counterexample exists) vs. "All odd numbers are prime" (9 is a counterexample). Progress to claims where counterexamples are harder to find. Emphasize that one counterexample is sufficient and final — no amount of supporting examples can save a statement once a counterexample exists. Practice distinguishing between "I cannot find a counterexample" and "no counterexample exists."

## Common Misconceptions
- Thinking you need multiple counterexamples to disprove something. One is enough — it shows the universal claim is false.
- Confusing a counterexample with a disagreement. A counterexample is not an opinion; it is a concrete instance that satisfies the premises but violates the conclusion.
- Believing that failing to find a counterexample proves a statement true. It might mean the statement is true, or it might mean you have not looked hard enough.

## Questions

```yaml
- question: "What is a counterexample to the claim 'All multiples of 4 are also multiples of 8'?"
  type: multiple-choice
  options:
    - "16, because 16 is a multiple of both 4 and 8"
    - "12, because 12 is a multiple of 4 but not a multiple of 8"
    - "9, because 9 is odd"
    - "8, because 8 is a multiple of 8"
  answer: 1
  explanation: "A counterexample must satisfy the hypothesis (be a multiple of 4) but violate the conclusion (not be a multiple of 8). 12 = 4 x 3 is a multiple of 4, but 12/8 = 1.5, so 12 is not a multiple of 8. Options A and D confirm the claim rather than refuting it. Option C is irrelevant — 9 is not a multiple of 4, so it cannot serve as a counterexample."

- question: "If you test 100 examples and none of them disprove a conjecture, the conjecture is proven true."
  type: true-false
  answer: false
  explanation: "Testing examples can increase your confidence in a conjecture, but it never proves a universal claim true. Goldbach's conjecture (every even number greater than 2 is the sum of two primes) has been verified for trillions of numbers but remains unproven. The 101st case — or the trillionth-and-first — could be the counterexample. Only a proof can establish certainty; examples establish plausibility."

- question: "A student claims: 'n² > n for all integers n.' Find a counterexample and explain why it works."
  type: short-answer
  answer: "n = 0 is a counterexample: 0² = 0, which is not greater than 0. Also n = 1: 1² = 1, which is not greater than 1. The claim requires n² to be strictly greater than n, but for n = 0 and n = 1, n² equals n."
  explanation: "The claim says 'for all integers,' so any single integer where n² is not strictly greater than n disproves it. Both 0 and 1 work. Negative integers do not work as counterexamples here because for negative n, n² is positive and thus greater than n. The correct statement would need to restrict the domain, for example: 'n² > n for all integers n > 1.'"
```

## Explainer

You know that an invalid argument is one where the premises can be true while the conclusion is false. A counterexample is the concrete demonstration of that gap — it is the specific case that makes the premises true and the conclusion false, thereby disproving the claim.

The power of counterexamples comes from a fundamental asymmetry in logic: proving a universal statement ("all X are Y") requires checking every case or constructing a proof, but disproving it requires finding just one exception. If someone says "all swans are white," observing a million white swans does not prove them right — but spotting one black swan proves them wrong, instantly and permanently. This asymmetry is why counterexamples are so important: they are efficient destroyers of false beliefs.

When searching for counterexamples, be strategic. Test boundary cases first: zero, one, negative numbers, the empty set, the smallest possible example. Most false generalizations break at the edges. If someone claims "the sum of any two prime numbers is even," test small primes: 2 + 3 = 5 is odd, so the claim fails. The number 2 is a frequent troublemaker because it is the only even prime — boundary cases like this are where intuition built on "typical" examples goes wrong.

A critical distinction: failing to find a counterexample is not the same as proving a statement true. If you test a hundred cases and the claim holds for all of them, you have evidence but not proof. The claim "every even number greater than 2 can be written as the sum of two primes" (Goldbach's Conjecture) has been verified computationally for numbers up to 4 × 10¹⁸ — that is an astronomically large amount of evidence — and yet it remains unproven. The difference between "I checked a lot of cases" and "I proved it for all cases" is the difference between inductive evidence and deductive proof, a distinction you will explore next.

Counterexamples also play a constructive role: they sharpen your thinking. When a counterexample breaks a conjecture, the right response is not to discard the idea but to ask "can I fix it?" If "n² > n for all integers" fails at n = 0 and n = 1, perhaps the true statement is "n² > n for all integers with |n| > 1." The counterexample tells you exactly where the claim breaks, which guides you toward the correct version. This cycle of conjecture, counterexample, and refinement is how mathematical knowledge actually develops.
