---
id: euclidean-algorithm
title: The Euclidean Algorithm
domain: mathematics
course: discrete-math
prerequisites:
- id: divisibility-and-gcd
  type: hard
- id: mathematical-induction
  type: soft
builds-toward:
- modular-arithmetic
- chinese-remainder-theorem
tags:
- euclidean-algorithm
- gcd
- extended-euclidean
- bezout
- modular-inverse
stage: formal-systems
status: validated
---

# The Euclidean Algorithm

## Core Idea
The Euclidean algorithm computes gcd(a,b) by repeated application of the division algorithm: gcd(a,b) = gcd(b, a mod b), stopping when the remainder is 0. The algorithm runs in O(log(min(a,b))) steps — far faster than factoring. The extended Euclidean algorithm additionally computes integers x, y satisfying ax + by = gcd(a,b) by back-substituting through the remainder table. This is the standard method for computing modular inverses, essential in RSA and other cryptographic algorithms.

## How It's Best Learned
Trace the algorithm step-by-step for several pairs, recording the remainder at each step. Practice back-substitution to find Bezout coefficients. Implement in pseudocode to appreciate the algorithm's efficiency versus exhaustive search.

## Common Misconceptions
- Stopping too early — the algorithm terminates only when the remainder reaches exactly 0.
- Making sign errors during the back-substitution step of the extended algorithm.
- Thinking GCD computation requires factoring — the Euclidean algorithm avoids factoring entirely.

## Explainer

You already know from divisibility that gcd(a, b) is the largest number that divides both a and b. The naive approach — list all divisors of each number and find the largest common one — works fine for small inputs but becomes impractical for large numbers. The **Euclidean algorithm** sidesteps this by exploiting a single elegant observation: gcd(a, b) = gcd(b, a mod b). Whatever divides a and b also divides their remainder; conversely, whatever divides b and the remainder also divides a. So each step replaces a larger problem with a smaller one without changing the answer.

Tracing the algorithm concretely locks in the intuition. Suppose you want gcd(252, 105). Divide: 252 = 2 × 105 + 42, so gcd(252, 105) = gcd(105, 42). Divide again: 105 = 2 × 42 + 21, so gcd(105, 42) = gcd(42, 21). Finally: 42 = 2 × 21 + 0, so gcd(42, 21) = 21. The algorithm terminates as soon as the remainder hits zero, and the last nonzero remainder is the answer. The number of steps is proportional to the number of digits in the input — O(log(min(a, b))) — because each pair of steps at least halves the size of the smaller number. This is dramatically faster than factoring.

The **extended Euclidean algorithm** keeps track of how each remainder can be expressed as a linear combination of the original inputs. At every step, you have equations like 42 = 252 − 2 × 105 and 21 = 105 − 2 × 42. Back-substituting these gives 21 = 105 − 2(252 − 2 × 105) = 5 × 105 − 2 × 252. This produces **Bézout's identity**: integers x and y such that ax + by = gcd(a, b). When gcd(a, b) = 1 (the inputs are coprime), this gives ax ≡ 1 (mod b), so x is the **modular inverse** of a modulo b.

Modular inverses are why this algorithm is everywhere in cryptography. RSA key generation requires computing the inverse of the public exponent modulo φ(n). The extended Euclidean algorithm does this in milliseconds for 2048-bit numbers where factoring would take longer than the age of the universe. From a prerequisite perspective, induction gives you the proof that the algorithm is correct (the invariant gcd(a, b) = gcd(b, a mod b) is preserved at every step); divisibility gives you the definition being computed. The algorithm itself is pure mechanical efficiency built on top of those foundations.
