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
status: draft
---

# Lagrange's Four-Square Theorem

## Core Idea
Every non-negative integer can be expressed as a sum of four squares. While the sum-of-two-squares theorem characterizes which numbers require four squares, Lagrange's result guarantees that four always suffice, contrasting sharply with two-square representations.

## Explainer

The question "which integers are sums of squares?" has a satisfying but incomplete answer for two squares, and a complete answer for four. A number is a sum of two squares if and only if every prime of the form 4k + 3 appears to an even power in its factorization — so 5 = 1² + 2² works, but 3 does not (and cannot). Many integers simply cannot be written as a sum of two squares. Three squares handle more cases, but still fail for numbers of the form 4ᵃ(8b + 7). **Lagrange's four-square theorem** closes the door entirely: four squares always suffice, no matter the integer.

The proof strategy centers on two key ingredients. First, it suffices to prove the theorem for prime numbers, because if n = a² + b² + c² + d² and m = e² + f² + g² + h², then the product nm is also a sum of four squares — this follows from the **Euler four-square identity**, an algebraic identity involving quaternion-like multiplication. So if every prime is a sum of four squares, every integer is too (via its prime factorization).

Second, every prime p is shown to be a sum of four squares by a counting argument. Consider the sets {a² mod p} and {−1 − b² mod p} for a, b ranging from 0 to (p−1)/2. Each set has (p+1)/2 elements, and together they contain more than p values, so by the **pigeonhole principle** they must overlap: there exist a, b with a² ≡ −1 − b² (mod p), giving a² + b² + 1 ≡ 0 (mod p). This produces mp = a² + b² + 0² + 1² for some m < p, and then a **descent argument** (reducing m step by step) shows p itself is a sum of four squares.

What makes this theorem philosophically satisfying is its universality. Unlike the two-square case, there are no exceptions, no congruence conditions, no special forms to check. Any positive integer you can name — whether it is 7 (= 4 + 1 + 1 + 1), or 15 (= 9 + 4 + 1 + 1), or any prime of the form 4k + 3 — can be expressed as four squares. The theorem also opens the door to **Waring's problem**: if four squares always suffice, what is the analogous result for cubes, fourth powers, and beyond? The four-square theorem is both a complete answer and a beginning.
