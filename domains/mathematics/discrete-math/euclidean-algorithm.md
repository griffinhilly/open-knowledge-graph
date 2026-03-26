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

## Questions

```yaml
- question: "A student tries to find gcd(252, 105) by listing all divisors of each number and finding the largest match. The Euclidean algorithm finds the same answer far more efficiently because:"
  type: multiple-choice
  options:
    - "The Euclidean algorithm uses prime factorization, which is faster than enumerating divisors"
    - "The Euclidean algorithm only works when one number divides the other evenly"
    - "The Euclidean algorithm avoids factoring entirely by repeatedly replacing gcd(a, b) with gcd(b, a mod b), reducing problem size in O(log n) steps"
    - "The Euclidean algorithm is only more efficient for numbers larger than one million"
  answer: 2
  explanation: "The Euclidean algorithm's efficiency comes from the key identity gcd(a, b) = gcd(b, a mod b), which replaces each problem with a strictly smaller one without any factoring. For gcd(252, 105): step 1 gives gcd(105, 42), step 2 gives gcd(42, 21), step 3 terminates at gcd(21, 0) = 21. Three steps, no factoring. Listing divisors requires finding all factors of both numbers — an O(√n) operation per number — and the approach becomes completely impractical for large numbers. For a 2048-bit number used in RSA, listing divisors is computationally infeasible; the Euclidean algorithm runs in milliseconds."

- question: "After running the Euclidean algorithm on two coprime inputs a and b (gcd = 1), what does the extended Euclidean algorithm additionally produce, and why is this output critical in RSA cryptography?"
  type: multiple-choice
  options:
    - "The prime factorizations of a and b, needed to construct the RSA public key"
    - "Integers x and y satisfying ax + by = 1, which gives a modular inverse of a mod b — used to compute the RSA private key from the public exponent"
    - "The least common multiple of a and b, needed to verify RSA signatures"
    - "The binary representation of gcd(a, b), enabling efficient modular exponentiation"
  answer: 1
  explanation: "Bézout's identity states that for any a, b there exist integers x, y with ax + by = gcd(a, b). When gcd(a, b) = 1 (coprime inputs), this gives ax + by = 1, which means ax ≡ 1 (mod b) — so x is the modular inverse of a modulo b. In RSA, the private exponent d is the modular inverse of the public exponent e modulo φ(n). Computing this inverse via the extended Euclidean algorithm takes O(log n) steps even for 2048-bit numbers — making RSA key generation fast. Without a fast modular inverse algorithm, public-key cryptography as currently implemented would be computationally infeasible."

- question: "The Euclidean algorithm terminates when the remainder equals 1, because 1 is a divisor of most integers and therefore the GCD of any two numbers is at least 1."
  type: true-false
  answer: false
  explanation: "The algorithm terminates when the remainder equals exactly 0 — not 1. The last nonzero remainder before the 0 is the GCD. For example, gcd(252, 105) terminates when the remainder becomes 0 after gcd(42, 21): 42 = 2×21 + 0, so the GCD is 21 (the last nonzero remainder). If the algorithm stopped at remainder 1, it would terminate too early for inputs whose GCD is greater than 1. Stopping at 0 is logically necessary: a mod 0 is undefined, so reaching 0 signals that the previous step's remainder divides the one before it exactly — that remainder is the answer."

- question: "The Euclidean algorithm can compute gcd(a, b) without ever determining the prime factorizations of a or b."
  type: true-false
  answer: true
  explanation: "This is one of the algorithm's most important properties. The entire computation uses only division with remainders — no factoring at any step. The key identity gcd(a, b) = gcd(b, a mod b) preserves the GCD while shrinking the inputs, and the termination condition (remainder = 0) identifies the answer. This is why the algorithm works for large numbers where factoring would be computationally infeasible. RSA security depends partly on the hardness of factoring large numbers — but computing GCDs, which requires only the Euclidean algorithm, remains fast regardless of number size."

- question: "Explain why the identity gcd(a, b) = gcd(b, a mod b) is true — why does replacing a with its remainder after division by b not change the GCD?"
  type: short-answer
  answer: "Any common divisor of a and b also divides a − qb (where q = ⌊a/b⌋) = a mod b, so it is a common divisor of b and a mod b. Conversely, any common divisor of b and a mod b also divides a = qb + (a mod b). The sets of common divisors are identical, so the largest common divisor (the GCD) is the same. Each step replaces a larger pair with a smaller pair having the same set of common divisors."
  explanation: "This is the mathematical heart of why the algorithm is correct. The proof relies on a simple divisibility fact: if d divides both a and b, it must also divide any linear combination of a and b, including a − qb. The algorithm exploits this to make the problem smaller at every step without changing the answer. The efficiency then follows from how quickly the remainder shrinks: Fibonacci numbers are the worst case (they minimize the ratio b/(a mod b)), and even for them the number of steps is proportional to the number of digits — O(log n). The algorithm is both provably correct and provably fast, two properties that together make it one of the oldest and most important algorithms in mathematics."
```

## Explainer

You already know from divisibility that gcd(a, b) is the largest number that divides both a and b. The naive approach — list all divisors of each number and find the largest common one — works fine for small inputs but becomes impractical for large numbers. The **Euclidean algorithm** sidesteps this by exploiting a single elegant observation: gcd(a, b) = gcd(b, a mod b). Whatever divides a and b also divides their remainder; conversely, whatever divides b and the remainder also divides a. So each step replaces a larger problem with a smaller one without changing the answer.

Tracing the algorithm concretely locks in the intuition. Suppose you want gcd(252, 105). Divide: 252 = 2 × 105 + 42, so gcd(252, 105) = gcd(105, 42). Divide again: 105 = 2 × 42 + 21, so gcd(105, 42) = gcd(42, 21). Finally: 42 = 2 × 21 + 0, so gcd(42, 21) = 21. The algorithm terminates as soon as the remainder hits zero, and the last nonzero remainder is the answer. The number of steps is proportional to the number of digits in the input — O(log(min(a, b))) — because each pair of steps at least halves the size of the smaller number. This is dramatically faster than factoring.

The **extended Euclidean algorithm** keeps track of how each remainder can be expressed as a linear combination of the original inputs. At every step, you have equations like 42 = 252 − 2 × 105 and 21 = 105 − 2 × 42. Back-substituting these gives 21 = 105 − 2(252 − 2 × 105) = 5 × 105 − 2 × 252. This produces **Bézout's identity**: integers x and y such that ax + by = gcd(a, b). When gcd(a, b) = 1 (the inputs are coprime), this gives ax ≡ 1 (mod b), so x is the **modular inverse** of a modulo b.

Modular inverses are why this algorithm is everywhere in cryptography. RSA key generation requires computing the inverse of the public exponent modulo φ(n). The extended Euclidean algorithm does this in milliseconds for 2048-bit numbers where factoring would take longer than the age of the universe. From a prerequisite perspective, induction gives you the proof that the algorithm is correct (the invariant gcd(a, b) = gcd(b, a mod b) is preserved at every step); divisibility gives you the definition being computed. The algorithm itself is pure mechanical efficiency built on top of those foundations.
