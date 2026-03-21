---
id: lagranges-four-square-theorem
title: Lagrange's Four-Square Theorem
domain: mathematics
course: number-theory
prerequisites:
- id: fundamental-theorem-arithmetic-rigorous
  type: hard
tags:
- four-squares
- representation
- diophantine
stage: advanced
status: draft
---

# Lagrange's Four-Square Theorem

## Core Idea
Every non-negative integer is the sum of four perfect squares. Unlike the two-square case, this holds universally with a clean statement, proven via quaternion algebras or generating functions.

## Questions

```yaml
- question: "The integer 7 cannot be expressed as a sum of three or fewer perfect squares. Why does Lagrange's theorem NOT produce a similar exception for sums of four squares?"
  type: multiple-choice
  options:
    - "The quaternion norm identity ensures that if m and n are each sums of four squares, so is mn — so the property reduces to primes, and every prime can be shown to admit a four-square representation"
    - "Seven was an oversight in the earlier three-square theorem; four-square sums are simply computed in a wider arithmetic"
    - "Adding a fourth square always converts any non-representable remainder into a perfect square by pigeonhole"
    - "The four-square theorem only applies to integers greater than 7, sidestepping that case entirely"
  answer: 0
  explanation: "The key is quaternion norm multiplicativity: N(qr) = N(q)N(r), where N(a+bi+cj+dk) = a²+b²+c²+d². This means the product of two four-square sums is itself a four-square sum. The proof therefore reduces to showing every prime is a sum of four squares — the rest follows from prime factorization. Seven requires four squares but is not a prime-factorization obstacle in the way it would be for a purely multiplicative structure without that identity."

- question: "According to Legendre's three-square theorem, which of the following integers requires all four squares and cannot be written as a sum of three?"
  type: multiple-choice
  options:
    - "11, since 11 = 8(1) + 3 and fits the pattern"
    - "28, since 28 = 4¹ · 7 = 4¹(8·0 + 7), fitting the form 4ᵃ(8b + 7)"
    - "9, since 9 = 3² uses only one square"
    - "5, since 5 = 4 + 1 uses only two squares"
  answer: 1
  explanation: "Legendre's three-square theorem states that a positive integer requires four squares (and cannot be written as a sum of three) if and only if it has the form 4ᵃ(8b + 7). For 28: 28 = 4 × 7, and 7 = 8(0) + 7, so 28 = 4¹(8·0 + 7) — exactly this form. For 11: 11 = 9 + 1 + 1 = 3² + 1² + 1², so three squares suffice. For 9 and 5: one and two squares respectively."

- question: "The proof that Lagrange's four-square theorem holds for all positive integers reduces to proving it just for prime numbers, because the set of four-square sums is closed under multiplication."
  type: true-false
  answer: true
  explanation: "Quaternion norm multiplicativity is the key algebraic fact: the product of two integers each expressible as sums of four squares is itself expressible as a sum of four squares. This means the property is multiplicative in the same way that prime factorization is. To show every positive integer is a four-square sum, it suffices to show every prime is — the general result follows by combining prime four-square representations using the quaternion identity."

- question: "The integers that require all four squares and cannot be written as a sum of three form a finite set known completely by mathematicians."
  type: true-false
  answer: false
  explanation: "The integers requiring four squares are exactly those of the form 4ᵃ(8b + 7) — an infinite set. For example, 7, 15, 23, 28, 55, 60, 63, 112, … all belong to this family. Legendre's three-square theorem gives a complete characterization, not a finite list. This is what makes Lagrange's result simultaneously tight (four cannot be reduced to three in general) and complete (four always suffices)."

- question: "Why is the multiplicativity of quaternion norms the key step in proving Lagrange's four-square theorem, rather than trying to verify it directly for each integer?"
  type: short-answer
  answer: "Quaternion norms satisfy N(qr) = N(q)N(r), where N(a+bi+cj+dk) = a²+b²+c²+d². This means that if two integers are each sums of four squares, their product is also a sum of four squares. Combined with unique prime factorization, this reduces the entire theorem to just one case: proving that every prime is a sum of four squares. A direct case-by-case verification would be impossible (infinitely many integers), but the multiplicativity turns an infinite problem into a single hard case about primes."
  explanation: "This is a classic reduction strategy in number theory. Instead of verifying a property for every integer, you establish a multiplicative closure property and then check the 'atoms' (primes). The quaternion identity provides an explicit algebraic formula: (a²+b²+c²+d²)(e²+f²+g²+h²) = (ae−bf−cg−dh)² + (af+be+ch−dg)² + (ag−bh+ce+df)² + (ah+bg−cf+de)². Euler discovered this identity before quaternions were formalized; Hamilton's quaternion algebra later explained why it works."
```

## Explainer

Start with a simple empirical observation: 1 = 1², 2 = 1² + 1², 3 = 1² + 1² + 1², 4 = 2², 5 = 2² + 1², 6 = 2² + 1² + 1², 7 = 2² + 1² + 1² + 1². Notice that 7 requires all four squares — no way to write it as the sum of three or fewer squares of integers. Lagrange's Four-Square Theorem, proved in 1770, asserts that this never gets worse: four squares always suffice for every non-negative integer.

To understand why four is special, contrast with two. From the **Fundamental Theorem of Arithmetic** you know that every integer factors uniquely into primes. The **sum-of-two-squares theorem** (a consequence of Fermat) says a positive integer is a sum of two squares if and only if in its prime factorization, every prime of the form 4k + 3 appears to an even power. So 3 (a 4k+3 prime to the first power) fails: 3 cannot be written as a² + b² for integers a, b. The two-square representation is selective. The **three-square theorem** (Legendre) says all integers are sums of three squares except those of the form 4^a(8b + 7). So 7 itself is excluded from three squares. But no such exceptions survive with four squares.

The classical proof uses **quaternion algebras** — a number system generalizing complex numbers to four dimensions, of the form a + bi + cj + dk. Crucially, quaternion norms multiply: N(qr) = N(q)N(r), where N(a + bi + cj + dk) = a² + b² + c² + d². This gives an **identity of four squares**: if m and n are each sums of four squares, then mn is also a sum of four squares. This multiplicativity means it suffices to prove the theorem for primes — the general case follows automatically from the prime factorization. For any prime p, one can show that among the p + 1 values 0², 1², …, ((p−1)/2)² and −1 − 0², −1 − 1², …, the pigeonhole principle guarantees a solution to a² + b² ≡ −1 (mod p), which bootstraps into representing p as a sum of four integer squares.

The theorem is tight in a precise sense: **Legendre's three-square theorem** shows that exactly the integers 4^a(8b + 7) require four squares and cannot be done with three. So Lagrange's result answers the question definitively — four squares are necessary in the worst case, and always sufficient. This makes the theorem a satisfying capstone: a clean, universal statement that falls out of the deep multiplicative structure of integers and the arithmetic of primes.
