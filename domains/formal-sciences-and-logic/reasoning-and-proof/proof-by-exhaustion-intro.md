---
id: proof-by-exhaustion-intro
title: Proof by Exhaustion
domain: formal-sciences-and-logic
course: reasoning-and-proof
prerequisites:
  - id: direct-proof-introduction
    type: hard
  - id: systematic-listing
    type: soft
builds-toward:
  - when-is-something-proven
  - proof-by-cases-exhaustion
  - proof-by-cases
tags: [proof, exhaustion, cases, enumeration]
stage: abstract-reasoning
status: validated
---

# Proof by Exhaustion

## Core Idea
Proof by exhaustion (also called proof by cases) works by splitting a problem into a complete list of cases and proving the statement separately for each case. If every case is covered and the statement holds in each one, it holds universally. The key requirement is that the cases must be exhaustive — they must cover every possibility with no gaps. This strategy is especially useful when a small number of cases exist, or when different cases require different reasoning.

## How It's Best Learned
Start with a concrete example: "Prove that n² + n is even for every integer n." Split into two cases: n is even or n is odd. Case 1: n = 2k, so n² + n = 4k² + 2k = 2(2k² + k), which is even. Case 2: n = 2k+1, so n² + n = (2k+1)² + (2k+1) = 4k² + 4k + 2 = 2(2k² + 2k + 1), which is even. Both cases proven, so the statement holds for all integers. Emphasize the checklist mentality: list cases, prove each, verify the list is complete.

## Common Misconceptions
- Forgetting a case. If the cases do not cover every possibility, the proof has a hole. Always verify that your cases partition the entire domain.
- Thinking exhaustion only works for small finite sets. It also works when you can split infinite sets into a small number of categories (like "even or odd," which covers all integers).
- Confusing checking examples with proof by exhaustion. Checking n = 1, 2, 3, 4, 5 is not proof by exhaustion unless those are literally all the cases. Proof by exhaustion requires covering every case.

## Questions

```yaml
- question: "A proof by exhaustion of a statement about all one-digit prime numbers would require how many cases?"
  type: multiple-choice
  options: ["3", "4", "5", "9"]
  answer: 1
  explanation: "The one-digit primes are 2, 3, 5, and 7 — four numbers. A proof by exhaustion would verify the statement for each of these four cases. Since these are all the one-digit primes, the four cases are exhaustive. No other one-digit number is prime, so no other case needs checking."

- question: "To prove a statement about most integers by exhaustion, you is expected to check infinitely many individual cases."
  type: true-false
  answer: false
  explanation: "You can partition all integers into a finite number of categories. For example, every integer is either even or odd — that is two cases, not infinitely many. Proof by exhaustion over the cases 'even' and 'odd' covers all integers with just two sub-proofs. The trick is choosing categories that are exhaustive and that allow each sub-proof to go through."

- question: "Prove by exhaustion that for any integer n with 1 ≤ n ≤ 4, the value n² ≤ 20."
  type: short-answer
  answer: "Case n=1: 1² = 1 ≤ 20. Case n=2: 2² = 4 ≤ 20. Case n=3: 3² = 9 ≤ 20. Case n=4: 4² = 16 ≤ 20. All four cases satisfy n² ≤ 20, and these are all integers in the range [1,4], so the statement is proven."
  explanation: "This is a pure exhaustion proof — the domain is finite (four integers), so you check each one. Every case satisfies the inequality, and no cases are missing. Note that n=5 would give 25 > 20, but n=5 is outside the stated domain, so it is irrelevant."
```

## Explainer

Sometimes the most effective proof strategy is the simplest one: check every case. If a statement applies to a finite set, or to an infinite set that splits naturally into a small number of categories, you can prove it by handling each case separately. This is proof by exhaustion — exhaustive in the sense that you exhaust (use up) all possibilities.

The method has two requirements. First, your cases must be exhaustive: together they must cover every element in the domain. If you are proving something about all integers and you split into "positive" and "negative," you have missed zero — the proof has a gap. You need "positive," "negative," and "zero," or alternatively "even" and "odd," or "divisible by 3," "one more than a multiple of 3," and "two more than a multiple of 3." Second, the statement must be proven in each case individually. A single unproven case invalidates the entire proof.

For finite domains, exhaustion is often the fastest approach. "Prove that every prime less than 10 is either 2, 3, 5, or 7." Well, the integers from 2 to 9 are: 2 (prime), 3 (prime), 4 = 2×2 (not prime), 5 (prime), 6 = 2×3 (not prime), 7 (prime), 8 = 2×4 (not prime), 9 = 3×3 (not prime). Check each one, confirm the primes, done. No cleverness needed.

For infinite domains, the key insight is that you do not need to check infinitely many individual elements — you need to split the domain into finitely many categories and prove the result for each category. Every integer is either even or odd. Every integer is either positive, negative, or zero. Every integer modulo 3 is either 0, 1, or 2. These partitions give you a finite number of cases, each covering infinitely many integers.

Proof by exhaustion is sometimes dismissed as inelegant, but elegance is overrated when correctness is the goal. The Four Color Theorem — one of the most famous results in mathematics — was proven in 1976 by checking 1,936 configurations by computer. Some mathematicians were uncomfortable with a proof that no human could verify by hand, but the logic is valid: if the cases are exhaustive and each is verified, the theorem is proven. Exhaustion is a legitimate and powerful proof technique.
