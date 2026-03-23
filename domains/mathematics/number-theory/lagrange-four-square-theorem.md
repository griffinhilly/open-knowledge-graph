---
id: lagrange-four-square-theorem
title: Lagrange's Four-Square Theorem
domain: mathematics
course: number-theory
prerequisites:
- id: fundamental-theorem-of-arithmetic-rigorous
  type: soft
tags:
- representations
- quadratic-forms
- diophantine
stage: advanced
status: validated
---

# Lagrange's Four-Square Theorem

## Core Idea
Every non-negative integer can be expressed as a sum of four squares. While the sum-of-two-squares theorem characterizes which numbers require four squares, Lagrange's result guarantees that four always suffice, contrasting sharply with two-square representations.

## Questions

```yaml
- question: "Which of the following integers CANNOT be expressed as a sum of two perfect squares?"
  type: multiple-choice
  options:
    - "5"
    - "25"
    - "3"
    - "13"
  answer: 2
  explanation: "By the sum-of-two-squares theorem, a number is a sum of two squares iff every prime factor of the form 4k+3 appears to an even power. The number 3 is itself a prime of the form 4k+3 (k=0) appearing to an odd power, so it cannot be expressed as a sum of two squares. Lagrange's theorem guarantees it can be expressed as four: 3 = 1² + 1² + 1² + 0²."

- question: "In the proof of Lagrange's theorem, what role does the Euler four-square identity play?"
  type: multiple-choice
  options:
    - "It directly proves that every prime is a sum of four squares"
    - "It shows that a product of two sums of four squares is itself a sum of four squares, so the result extends from primes to all integers"
    - "It establishes that the number of four-square representations grows with the integer"
    - "It proves that the descent argument terminates at m = 1"
  answer: 1
  explanation: "The Euler four-square identity shows that the set of integers expressible as sums of four squares is closed under multiplication. Since every positive integer factors into primes, it suffices to prove the result for primes — the identity then propagates it to all integers via prime factorization. The identity itself does not prove the prime case; that requires the pigeonhole and descent arguments."

- question: "Every integer that cannot be expressed as a sum of three squares also cannot be expressed as a sum of four squares."
  type: true-false
  answer: false
  explanation: "Integers of the form 4ᵃ(8b+7) cannot be expressed as a sum of three squares, but Lagrange's theorem guarantees every non-negative integer can be expressed as a sum of four squares — with no exceptions. The passage from three to four squares closes the remaining gap entirely."

- question: "The proof that every prime p is a sum of four squares uses a descent argument that starts from a multiple mp expressible as a sum of four squares (with m < p) and reduces m until reaching 1."
  type: true-false
  answer: true
  explanation: "A pigeonhole counting argument shows that a² + b² + 1 ≡ 0 (mod p) for some a, b, giving mp = a² + b² + 0² + 1² for some m < p. The descent then reduces m step by step, using the Euler identity at each stage, until m = 1, at which point p itself is expressed as a sum of four squares."

- question: "Why does it suffice, in proving Lagrange's four-square theorem, to prove only that every prime can be expressed as a sum of four squares?"
  type: short-answer
  answer: "Because the Euler four-square identity shows that a product of two integers each expressible as sums of four squares is itself expressible as a sum of four squares. Since every positive integer has a prime factorization, establishing the result for primes and applying the identity inductively extends it to all positive integers."
  explanation: "The multiplicative closure provided by the Euler identity is what allows a proof about primes to become a universal theorem. Without it, the prime case would not obviously generalize."
```

## Explainer

The question "which integers are sums of squares?" has a satisfying but incomplete answer for two squares, and a complete answer for four. A number is a sum of two squares if and only if every prime of the form 4k + 3 appears to an even power in its factorization — so 5 = 1² + 2² works, but 3 does not (and cannot). Many integers simply cannot be written as a sum of two squares. Three squares handle more cases, but still fail for numbers of the form 4ᵃ(8b + 7). **Lagrange's four-square theorem** closes the door entirely: four squares always suffice, no matter the integer.

The proof strategy centers on two key ingredients. First, it suffices to prove the theorem for prime numbers, because if n = a² + b² + c² + d² and m = e² + f² + g² + h², then the product nm is also a sum of four squares — this follows from the **Euler four-square identity**, an algebraic identity involving quaternion-like multiplication. So if every prime is a sum of four squares, every integer is too (via its prime factorization).

Second, every prime p is shown to be a sum of four squares by a counting argument. Consider the sets {a² mod p} and {−1 − b² mod p} for a, b ranging from 0 to (p−1)/2. Each set has (p+1)/2 elements, and together they contain more than p values, so by the **pigeonhole principle** they must overlap: there exist a, b with a² ≡ −1 − b² (mod p), giving a² + b² + 1 ≡ 0 (mod p). This produces mp = a² + b² + 0² + 1² for some m < p, and then a **descent argument** (reducing m step by step) shows p itself is a sum of four squares.

What makes this theorem philosophically satisfying is its universality. Unlike the two-square case, there are no exceptions, no congruence conditions, no special forms to check. Any positive integer you can name — whether it is 7 (= 4 + 1 + 1 + 1), or 15 (= 9 + 4 + 1 + 1), or any prime of the form 4k + 3 — can be expressed as four squares. The theorem also opens the door to **Waring's problem**: if four squares always suffice, what is the analogous result for cubes, fourth powers, and beyond? The four-square theorem is both a complete answer and a beginning.
