---
id: divisibility-theory-formal
title: Divisibility Theory (Formal Treatment)
domain: mathematics
course: number-theory
prerequisites:
- id: fundamental-theorem-of-arithmetic
  type: hard
- id: mathematical-induction
  type: hard
builds-toward:
- bezout-identity
- linear-diophantine-equations
tags:
- divisibility
- number-theory
- foundations
stage: advanced
status: validated
---

# Divisibility Theory (Formal Treatment)

## Core Idea
Divisibility is the foundational concept of number theory: a divides b (written a|b) means b = ka for some integer k. Divisibility is reflexive and transitive, establishing a partial order on integers. Rigorous treatment develops divisibility properties essential for all subsequent number-theoretic structures.

## How It's Best Learned
Start with concrete examples (12|48, 7∤50) and verify the formal definition. Prove basic properties: if a|b and b|c, then a|c.

## Common Misconceptions
Confusing divisibility with being divisible (a|b means b is divisible by a). Thinking divisibility requires positive integers (it applies to all nonzero integers).

## Questions

```yaml
- question: "A student writes: '12 | 4, because 12 = 3 × 4.' What is wrong with this claim?"
  type: multiple-choice
  options:
    - "Nothing — if 12 = 3 × 4, then 12 divides 4 by definition"
    - "The notation is reversed: 'a | b' means b = k·a for some integer k, so 4 | 12 (since 12 = 3·4), not 12 | 4"
    - "The claim would be correct only if k were required to be a prime number"
    - "Divisibility requires both numbers to be positive, so neither 4 nor 12 can appear in this notation"
  answer: 1
  explanation: "The definition is: a | b means b = k·a for some integer k. Here 12 = 3 × 4 means 4 | 12 (4 divides 12), not 12 | 4. The student has the relationship backwards. '12 | 4' would require an integer k such that 4 = k·12, which has no integer solution. This direction confusion — conflating 'a divides b' with 'a is divisible by b' — is the most persistent error in divisibility notation."

- question: "If a | b and a | c, what can be concluded about a | (3b − 7c)?"
  type: multiple-choice
  options:
    - "Nothing can be concluded without knowing the specific values of a, b, and c"
    - "a | (3b − 7c), because divisibility is preserved under any integer linear combination"
    - "a | (3b − 7c) only if 3 and 7 are also divisible by a"
    - "a | (3b − 7c) only if b > c"
  answer: 1
  explanation: "The linear combination property states: if a | b and a | c, then a | (xb + yc) for any integers x and y. Here x = 3 and y = −7, so a | (3b − 7c) follows directly. This is the seed from which the theory of gcd and Bézout's identity grow — the integers divisible by a fixed a are closed under linear combination, forming what will later be recognized as an ideal."

- question: "Divisibility is defined only for positive integers; extending it to negative integers requires a separate definition."
  type: true-false
  answer: false
  explanation: "Divisibility applies to all nonzero integers. The definition b = k·a holds when k is any integer — positive, negative, or zero (though a itself must be nonzero to avoid division by zero). For example, −4 | 12 because 12 = (−3)(−4), and 4 | (−12) because −12 = (−3)(4). This generality is essential when working in the integers as a ring, where negative numbers have equal status with positive ones."

- question: "If a and b are positive integers with a | b and b | a, then a = b."
  type: true-false
  answer: true
  explanation: "This is the antisymmetry of the divisibility partial order. If a | b, then b = k·a for some positive integer k (since both are positive). If b | a, then a = m·b for some positive integer m. Substituting: a = m·b = m·k·a, so mk = 1. Since m and k are positive integers, mk = 1 forces m = k = 1, so a = b. This property — along with reflexivity (a | a) and transitivity (a | b and b | c implies a | c) — makes divisibility a partial order."

- question: "Why is divisibility called a 'partial order' on positive integers rather than a 'total order'? What property does it lack that would be required for a total order?"
  type: short-answer
  answer: "A total order requires that any two elements be comparable — for any a and b, either a | b or b | a. Divisibility fails this: consider 4 and 6. Neither 4 | 6 (since 6 = k·4 has no integer solution) nor 6 | 4 (since 4 = k·6 has no integer solution). So 4 and 6 are incomparable under divisibility, making it only a partial order."
  explanation: "Divisibility satisfies the three axioms of a partial order (reflexivity, antisymmetry, transitivity) but not comparability. This is geometrically visible in the Hasse diagram of the divisibility lattice: elements that are not related by divisibility (like 4 and 6) appear side by side with no connecting path. The lattice structure — with gcd as meet (greatest lower bound) and lcm as join (least upper bound) — is a richer consequence of this partial order that does not exist for total orders."
```

## Explainer

You already know from the **Fundamental Theorem of Arithmetic** that every integer greater than 1 factors uniquely into primes. Divisibility theory is the formal scaffolding beneath that theorem — it gives precise meaning to "a divides b" and establishes the structural properties that make the rest of number theory work. The definition is deceptively simple: we say **a divides b** (written a | b) if there exists an integer k such that b = k · a. So 4 | 12 because 12 = 3 · 4, and 7 ∤ 50 because no integer k satisfies 50 = 7k. Notice the notation: a | b says "a divides b," which is equivalent to saying "b is divisible by a." The two phrasings are converses of each other, and confusing them is a persistent error.

The formal treatment establishes that divisibility is a **partial order** on the positive integers — it is reflexive (a | a, since a = 1 · a), antisymmetric (if a | b and b | a with positive integers, then a = b), and transitive (if a | b and b | c, then a | c). The transitivity proof is where **mathematical induction** connects: the proof is direct, not inductive, but induction is the engine for more complex divisibility arguments that follow. The key properties to internalize are: if a | b and a | c, then a | (bx + cy) for any integers x, y — that is, divisibility is preserved under linear combinations. This is the seed from which Bézout's identity and the theory of greatest common divisors grow.

What makes the formal treatment powerful is that it extends cleanly to negative integers. We allow a and b to be any nonzero integers: −4 | 12 because 12 = (−3)(−4). This generality is essential for working in the integers as a ring, where negative numbers play equal status with positive ones. The Fundamental Theorem tells you *what* the prime factors are; divisibility theory tells you *how divisibility behaves structurally* — the rules of the game. Every subsequent result, from Bézout's identity to linear Diophantine equations, is built on exactly these properties.

The deepest insight at this stage is that divisibility gives the integers a **lattice structure**: for any two positive integers a and b, there is a unique greatest common divisor gcd(a,b) and a unique least common multiple lcm(a,b), related by gcd(a,b) · lcm(a,b) = ab. The gcd is the largest element below both a and b in the divisibility partial order; the lcm is the smallest element above both. This perspective reframes gcd and lcm as structural features of the integer lattice, not just computational results — a viewpoint that pays dividends when you move to more abstract algebraic settings.
