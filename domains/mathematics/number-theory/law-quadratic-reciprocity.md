---
id: law-quadratic-reciprocity
title: Law of Quadratic Reciprocity
domain: mathematics
course: number-theory
prerequisites:
- id: eulers-criterion
  type: hard
- id: quadratic-residues-legendre-symbol
  type: hard
builds-toward:
- jacobi-symbol
tags:
- reciprocity
- quadratic-residues
- legendre-symbol
stage: advanced
status: validated
---

# Law of Quadratic Reciprocity

## Core Idea
For distinct odd primes p and q: (p/q)(q/p) = (-1)^((p-1)(q-1)/4). Combined with supplementary laws for (-1/p) and (2/p), it enables efficient Legendre symbol computation and is central to number theory.

## How It's Best Learned
Prove a special case (e.g., p=3, q=5) to understand the counting argument. Use it to compute (a/p) without explicit square-root verification.

## Common Misconceptions
Forgetting supplementary laws for (-1/p) and (2/p). Misremembering the sign in the reciprocity formula.

## Questions

```yaml
- question: "To compute (3/7) using the Law of Quadratic Reciprocity, you note that 3 ≡ 3 (mod 4) and 7 ≡ 3 (mod 4). What is the correct conclusion?"
  type: multiple-choice
  options:
    - "(3/7) = (7/3), because both primes are odd and the law allows free flipping"
    - "(3/7) = −(7/3), because both primes are ≡ 3 (mod 4), making the product (3/7)(7/3) = −1"
    - "(3/7) = (7/3) · (−1)^3 = −(7/3), but only if 3 < 7"
    - "(3/7)(7/3) = 1, because the exponent (p−1)/2 · (q−1)/2 = 1 · 3 = 3 is always positive"
  answer: 1
  explanation: "The reciprocity formula says (p/q)(q/p) = (−1)^{(p−1)/2 · (q−1)/2}. With p=3, q=7: (3−1)/2 = 1, (7−1)/2 = 3, product = 3, which is odd. So (3/7)(7/3) = (−1)³ = −1, meaning the symbols have opposite signs. The sign flip happens exactly when both primes are ≡ 3 (mod 4) — since that makes (p−1)/2 and (q−1)/2 both odd, and their product odd. To finish: (7/3) = (1/3) = 1 since 7 ≡ 1 (mod 3), so (3/7) = −1. Indeed, 3 is not a quadratic residue mod 7 (the QRs mod 7 are 1, 2, 4)."

- question: "When does the Law of Quadratic Reciprocity alone suffice to compute any Legendre symbol (a/p)?"
  type: multiple-choice
  options:
    - "Always — the law handles all cases by repeated flipping until a small base case is reached"
    - "Whenever a and p are both odd primes — the law handles all such pairs directly"
    - "Never alone — you also need the supplementary laws for (−1/p) and (2/p) to handle reductions that produce −1 or 2"
    - "Only when a < p, since flipping reduces the larger argument"
  answer: 2
  explanation: "The main reciprocity law handles pairs of distinct odd primes p and q. But the reduction process — analogous to the Euclidean algorithm — will eventually produce residues of −1 or 2 (just as Euclidean algorithm eventually reaches small remainders). These cannot be handled by the main law, which requires two odd primes. The first supplementary law (−1/p) = (−1)^{(p−1)/2} and the second supplementary law (2/p) = (−1)^{(p²−1)/8} are essential components of the complete algorithm. Forgetting them is the most common error in practice."

- question: "The sign flip in the Law of Quadratic Reciprocity — (p/q)(q/p) = −1 — occurs if and only if both p and q are congruent to 3 mod 4."
  type: true-false
  answer: true
  explanation: "The exponent (p−1)/2 · (q−1)/2 is odd (giving a product of −1) if and only if both factors are odd — i.e., both (p−1)/2 and (q−1)/2 are odd — i.e., both p ≡ 3 (mod 4) and q ≡ 3 (mod 4). If at least one prime is ≡ 1 (mod 4), then at least one factor is even, making the product even, so (p/q)(q/p) = 1 and you can flip freely without a sign change. The sign flip is the case to remember because it is the exception; free flipping is the rule."

- question: "The Law of Quadratic Reciprocity, together with its two supplementary laws, provides a complete algorithm for computing (a/p) for any integer a and odd prime p, without computing any large powers."
  type: true-false
  answer: true
  explanation: "This is the practical payoff of the law. Without reciprocity, computing (a/p) requires evaluating a^{(p−1)/2} mod p — a large modular exponentiation. With the full toolkit (main law + both supplementary laws), you can reduce (a/p) recursively — flipping the symbol, reducing mod the new modulus, handling factors of −1 and 2 — until you reach trivial base cases. The process terminates because the numbers decrease, just like the Euclidean algorithm. No large powers are needed at any step."

- question: "Explain why computing Legendre symbols via the Law of Quadratic Reciprocity is analogous to computing GCDs via the Euclidean algorithm. What plays the role of 'division with remainder'?"
  type: short-answer
  answer: "In the Euclidean algorithm, you reduce gcd(a, b) to gcd(b, a mod b) — replacing the larger number by the smaller remainder. In Legendre symbol computation, you reduce (p/q) to ±(q/p) by flipping (the sign depends on whether both are ≡ 3 mod 4), then reduce further by replacing p with p mod q. The 'division with remainder' step is: (p/q) = (p mod q / q), because the Legendre symbol (p/q) depends only on p mod q by periodicity. The numbers decrease with each step, guaranteeing termination, and supplementary laws handle the base cases (analogous to gcd terminating when the remainder reaches 1)."
  explanation: "Both algorithms achieve efficiency by recursive reduction. The Euclidean algorithm can compute gcd(10^100, 10^100 − 1) in about 300 steps by reduction. Similarly, reciprocity lets you compute (10^100 + 3 / some large prime) by reducing the problem size at each step. The parallel is not just metaphorical — both algorithms have similar worst-case step counts proportional to the number of digits, and both exploit the same periodicity structure (remainder for gcd; congruence for Legendre symbol)."
```

## Explainer

From your work on quadratic residues and Euler's criterion, you can already decide whether a given integer a is a square mod p: compute a^{(p-1)/2} mod p and check whether the result is 1 or -1. But this requires computing a large modular power, and it gives you no pattern for how the answer changes as p varies. The **Legendre symbol** (a/p) = ±1 packages this answer neatly, and the Law of Quadratic Reciprocity provides a powerful shortcut for computing it by reducing the problem recursively.

The reciprocity law states: for distinct odd primes p and q, **(p/q)(q/p) = (-1)^{(p-1)/2 · (q-1)/2}**. This exponent is 1 — making the product negative — only when *both* p and q are congruent to 3 mod 4; otherwise the product is 1. The practical consequence is that you can flip the symbol: to compute (p/q), replace it with ±(q/p), which may be easier because q < p or because q is a familiar number. Then apply reciprocity again, just like in the Euclidean algorithm. The computation terminates because the numbers decrease.

Two supplementary laws complete the toolkit. The **first supplementary law** says (-1/p) = (-1)^{(p-1)/2}: the symbol equals 1 if p ≡ 1 (mod 4), and -1 if p ≡ 3 (mod 4). The **second supplementary law** says (2/p) = (-1)^{(p²-1)/8}: the symbol equals 1 if p ≡ 1 or 7 (mod 8), and -1 if p ≡ 3 or 5 (mod 8). Together with the main law, these three rules let you reduce any Legendre symbol computation to a chain of flips and small residues, analogous to how the Euclidean algorithm reduces any gcd computation to a chain of divisions.

To see this in action, compute (5/13): flip by reciprocity (both ≡ 1 mod 4, so sign is +1) to get (13/5) = (3/5) since 13 ≡ 3 (mod 5). Now compute (3/5): both are odd primes with 3 ≡ 3 mod 4 and 5 ≡ 1 mod 4, so only one is ≡ 3 mod 4, meaning the exponent is 0 and the product is +1, giving (3/5) = (5/3) = (2/3). Finally (2/3): using the second supplementary law, 3 ≡ 3 (mod 8), so (2/3) = -1. Tracing back: (5/13) = -1, meaning 5 is not a quadratic residue mod 13. At no point did you compute any large powers.
