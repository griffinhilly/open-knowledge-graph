---
id: congruences-and-crt
title: Linear Congruences and the Chinese Remainder Theorem
domain: mathematics
course: discrete-math
prerequisites:
- id: modular-arithmetic-discrete
  type: hard
- id: chinese-remainder-theorem
  type: hard
tags:
- linear-congruences
- CRT
- simultaneous-congruences
- solution-existence
stage: formal-systems
status: draft
---

# Linear Congruences and the Chinese Remainder Theorem

## Core Idea
A linear congruence ax ≡ b (mod n) has solutions iff gcd(a, n) divides b. If a solution exists, there are gcd(a, n) distinct solutions mod n. The Chinese Remainder Theorem: if n₁, n₂, ..., nₖ are pairwise coprime, the system x ≡ aᵢ (mod nᵢ) has a unique solution mod (n₁n₂...nₖ).

## How It's Best Learned
Solve ax ≡ b (mod n) by finding a multiplicative inverse (if it exists) via extended Euclidean algorithm. Apply CRT to solve systems of congruences. Use CRT for applications: secret sharing, garbled circuits.

## Common Misconceptions
Linear congruences don't always have solutions; check gcd(a, n) | b first. CRT requires pairwise coprimality, not just mutual primality. Solutions are unique mod the product, not individually.

## Explainer

A **linear congruence** ax ≡ b (mod n) is a modular equation asking: which values of x satisfy it? Think of it as asking "which numbers, when multiplied by a and reduced mod n, give b?" This is the modular analogue of solving ax = b in ordinary arithmetic — but modular arithmetic is cyclical, so the answer is not a single number but a residue class (all numbers of the form x₀ + k·(n/d) for integer k, where d = gcd(a, n)).

The existence condition is the key insight: ax ≡ b (mod n) has a solution if and only if **gcd(a, n) divides b**. To see why, notice that the values ax mod n, as x ranges over all integers, cycle through exactly the multiples of gcd(a, n). So b must be one of those multiples. When a solution exists, you find it by dividing through by d = gcd(a, n) to get a reduced congruence (a/d)x ≡ (b/d) (mod n/d), where a/d and n/d are now coprime — meaning a/d has a multiplicative inverse mod n/d, which you compute via the extended Euclidean algorithm. There are exactly d = gcd(a, n) distinct solutions modulo n, evenly spaced by n/d.

The **Chinese Remainder Theorem (CRT)** takes this further: instead of one congruence, you have a *system* — x ≡ a₁ (mod n₁), x ≡ a₂ (mod n₂), …, x ≡ aₖ (mod nₖ). The theorem guarantees a unique solution modulo N = n₁n₂···nₖ, but only when the moduli are **pairwise coprime** (every pair nᵢ, nⱼ shares no common factor). The word "pairwise" matters: three numbers can all be mutually coprime as a triple but still share factors in pairs — pairwise coprimality is strictly stronger. The construction is explicit: for each i, let Nᵢ = N/nᵢ, compute the inverse of Nᵢ mod nᵢ, call it Mᵢ, and then x = Σ aᵢNᵢMᵢ (mod N).

To see why uniqueness holds: if two solutions x and y both satisfy all congruences, then x − y ≡ 0 modulo each nᵢ, so each nᵢ divides x − y. Since the nᵢ are pairwise coprime, their product N also divides x − y, meaning x ≡ y (mod N). A concrete example makes this vivid: find x with x ≡ 2 (mod 3) and x ≡ 3 (mod 5). Since gcd(3,5) = 1, a unique solution exists mod 15. Testing: x = 8 satisfies both (8 = 3·2+2, 8 = 5·1+3), and the next solution is 8 + 15 = 23, confirming periodicity mod 15. CRT has far-reaching applications: it lets you do arithmetic with large numbers by working modulo several small primes simultaneously, which is the backbone of many cryptographic constructions.
