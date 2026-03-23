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
status: validated
---

# Linear Congruences and the Chinese Remainder Theorem

## Core Idea
A linear congruence ax ≡ b (mod n) has solutions iff gcd(a, n) divides b. If a solution exists, there are gcd(a, n) distinct solutions mod n. The Chinese Remainder Theorem: if n₁, n₂, ..., nₖ are pairwise coprime, the system x ≡ aᵢ (mod nᵢ) has a unique solution mod (n₁n₂...nₖ).

## How It's Best Learned
Solve ax ≡ b (mod n) by finding a multiplicative inverse (if it exists) via extended Euclidean algorithm. Apply CRT to solve systems of congruences. Use CRT for applications: secret sharing, garbled circuits.

## Common Misconceptions
Linear congruences don't always have solutions; check gcd(a, n) | b first. CRT requires pairwise coprimality, not just mutual primality. Solutions are unique mod the product, not individually.

## Questions

```yaml
- question: "Consider the congruence 6x ≡ 9 (mod 15). How many distinct solutions exist modulo 15?"
  type: multiple-choice
  options:
    - "No solutions, because 6 and 15 are not coprime"
    - "Exactly one solution, since the equation simplifies to 2x ≡ 3 (mod 5)"
    - "Exactly 3 solutions, since gcd(6, 15) = 3 and 3 divides 9"
    - "Exactly 6 solutions, one for each multiple of the coefficient"
  answer: 2
  explanation: "The existence condition: ax ≡ b (mod n) has solutions iff gcd(a,n) | b, and when solutions exist there are exactly gcd(a,n) of them modulo n. Here gcd(6,15) = 3, and 3 divides 9, so solutions exist. The number of solutions is exactly gcd(6,15) = 3. Option A is the most tempting mistake: students often conclude that non-coprimality means no solution, but you must actually check whether gcd(a,n) divides b. When it does, there are gcd(a,n) solutions, not one."

- question: "You need to solve the system: x ≡ 2 (mod 4) and x ≡ 3 (mod 6). A student applies CRT and claims a unique solution modulo 24. What is wrong?"
  type: multiple-choice
  options:
    - "Nothing is wrong — CRT applies whenever you have exactly two congruences"
    - "CRT requires pairwise coprime moduli; since gcd(4, 6) = 2 ≠ 1, the standard CRT does not guarantee a unique solution modulo 24"
    - "CRT only applies when there are at least 3 congruences in the system"
    - "The moduli must be prime for CRT to apply"
  answer: 1
  explanation: "CRT requires pairwise coprimality of all moduli — every pair must share no common factor. Since gcd(4,6) = 2, the standard CRT does not apply. The system may have no solution or may have solutions with a period smaller than 24. Naively multiplying the moduli gives 24, but the actual period could be lcm(4,6) = 12 at most. The pairwise coprimality condition is exactly what ensures the product equals the lcm, giving a unique solution modulo that product."

- question: "If gcd(a, n) does not divide b, the congruence ax ≡ b (mod n) has no solutions."
  type: true-false
  answer: true
  explanation: "This is the exact existence condition for linear congruences. The values ax mod n, as x ranges over all integers, cycle through exactly the multiples of gcd(a,n). If b is not a multiple of gcd(a,n), it never appears in that cycle, and there is no solution. For example, 6x ≡ 4 (mod 9): gcd(6,9) = 3, and 3 does not divide 4, so this congruence has no solutions at all — not one, not many, none."

- question: "The Chinese Remainder Theorem guarantees a unique solution modulo n₁n₂···nₖ whenever the moduli are all distinct prime numbers."
  type: true-false
  answer: false
  explanation: "CRT requires pairwise coprimality, not that each modulus be prime. Distinct primes are automatically pairwise coprime (since two distinct primes share no common factor), so using distinct primes does work — but it is a sufficient condition, not a necessary one. Composite numbers like 4 and 9 are pairwise coprime (gcd(4,9) = 1), so CRT applies to them too. What CRT strictly requires is gcd(nᵢ,nⱼ) = 1 for every pair i ≠ j, not that each nᵢ be prime."

- question: "Why must pairwise coprimality — not just the absence of a single common factor shared by all moduli — be required for the Chinese Remainder Theorem?"
  type: short-answer
  answer: "Pairwise coprimality is what allows the uniqueness argument to go through. If two solutions x and y both satisfy all congruences, then each nᵢ divides (x − y). Pairwise coprimality means the product N = n₁n₂···nₖ also divides (x − y), so x ≡ y (mod N) — uniqueness modulo N. If two moduli share a factor d > 1, that factor is 'counted twice' in the product, so N overestimates the true period, and the system may have solutions with a period smaller than N, or no solution at all when incompatible residues are required modulo d."
  explanation: "A concrete failure case: moduli 6, 10, 15 — each pair shares a factor (gcd(6,10)=2, gcd(6,15)=3, gcd(10,15)=5), even though no single factor divides all three. CRT fails because the pairwise non-coprimality means a candidate x must satisfy conflicting divisibility conditions. The product 6·10·15 = 900, but no unique solution modulo 900 is guaranteed. The uniqueness proof requires every pair to be coprime, not just the collection as a whole."
```

## Explainer

A **linear congruence** ax ≡ b (mod n) is a modular equation asking: which values of x satisfy it? Think of it as asking "which numbers, when multiplied by a and reduced mod n, give b?" This is the modular analogue of solving ax = b in ordinary arithmetic — but modular arithmetic is cyclical, so the answer is not a single number but a residue class (all numbers of the form x₀ + k·(n/d) for integer k, where d = gcd(a, n)).

The existence condition is the key insight: ax ≡ b (mod n) has a solution if and only if **gcd(a, n) divides b**. To see why, notice that the values ax mod n, as x ranges over all integers, cycle through exactly the multiples of gcd(a, n). So b must be one of those multiples. When a solution exists, you find it by dividing through by d = gcd(a, n) to get a reduced congruence (a/d)x ≡ (b/d) (mod n/d), where a/d and n/d are now coprime — meaning a/d has a multiplicative inverse mod n/d, which you compute via the extended Euclidean algorithm. There are exactly d = gcd(a, n) distinct solutions modulo n, evenly spaced by n/d.

The **Chinese Remainder Theorem (CRT)** takes this further: instead of one congruence, you have a *system* — x ≡ a₁ (mod n₁), x ≡ a₂ (mod n₂), …, x ≡ aₖ (mod nₖ). The theorem guarantees a unique solution modulo N = n₁n₂···nₖ, but only when the moduli are **pairwise coprime** (every pair nᵢ, nⱼ shares no common factor). The word "pairwise" matters: three numbers can all be mutually coprime as a triple but still share factors in pairs — pairwise coprimality is strictly stronger. The construction is explicit: for each i, let Nᵢ = N/nᵢ, compute the inverse of Nᵢ mod nᵢ, call it Mᵢ, and then x = Σ aᵢNᵢMᵢ (mod N).

To see why uniqueness holds: if two solutions x and y both satisfy all congruences, then x − y ≡ 0 modulo each nᵢ, so each nᵢ divides x − y. Since the nᵢ are pairwise coprime, their product N also divides x − y, meaning x ≡ y (mod N). A concrete example makes this vivid: find x with x ≡ 2 (mod 3) and x ≡ 3 (mod 5). Since gcd(3,5) = 1, a unique solution exists mod 15. Testing: x = 8 satisfies both (8 = 3·2+2, 8 = 5·1+3), and the next solution is 8 + 15 = 23, confirming periodicity mod 15. CRT has far-reaching applications: it lets you do arithmetic with large numbers by working modulo several small primes simultaneously, which is the backbone of many cryptographic constructions.
