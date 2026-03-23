---
id: quadratic-congruences
title: Quadratic Congruences
domain: mathematics
course: number-theory
prerequisites:
- id: quadratic-residues-legendre-symbol
  type: hard
- id: chinese-remainder-theorem
  type: soft
builds-toward:
- pells-equation
tags:
- quadratic-congruences
- quadratic-equations
stage: advanced
status: validated
---

# Quadratic Congruences

## Core Idea
Quadratic congruences ax^2 + bx + c ≡ 0 (mod n) reduce to a = 1 and a = prime power cases. Solutions exist iff the discriminant is a quadratic residue modulo relevant prime factors, determined via Legendre symbols and Hensel lifting.

## Questions

```yaml
- question: "You want to solve x² ≡ 5 (mod 21). What is the correct first step, and what does success at this step guarantee?"
  type: multiple-choice
  options:
    - "Apply Hensel's lemma directly to lift a solution from mod 3 to mod 21"
    - "Check whether 5 is a quadratic residue mod 21 using the Legendre symbol (5/21)"
    - "Factor 21 = 3 × 7, then check solvability mod 3 and mod 7 separately using Legendre symbols; a solution mod 21 exists iff solutions exist for both"
    - "Use the Chinese Remainder Theorem to immediately write down the solution without checking solvability"
  answer: 2
  explanation: "The Legendre symbol is only defined for odd primes, not for composite moduli. The correct strategy is to factor 21 = 3 × 7, then apply (5/3) and (5/7) separately. If both are 1, a solution mod 21 exists and can be assembled via CRT. If either is -1, no solution exists mod 21. Option B is the tempting wrong answer: (5/21) is not a standard Legendre symbol, and computing it without decomposing the modulus bypasses the actual check. Solvability mod a composite number requires solvability mod each prime factor."

- question: "You have found that r₁ = 3 satisfies r₁² ≡ 4 (mod 5). You want to lift this to a solution mod 25 using Hensel's lemma. What is the key condition that must hold for the lift to succeed, and why?"
  type: multiple-choice
  options:
    - "r₁ must be odd; even solutions cannot be lifted to higher prime powers"
    - "2r₁ must not be ≡ 0 (mod 5), i.e., the derivative of x² - 4 evaluated at r₁ must be nonzero mod p"
    - "The discriminant of x² - 4 must be a perfect square; otherwise lifting fails for all k > 1"
    - "The prime p = 5 must divide r₁; otherwise the lift formula is undefined"
  answer: 1
  explanation: "Hensel's lemma lifts solutions when the 'derivative condition' holds: 2r₁ ≢ 0 (mod p). Here, 2·3 = 6 ≡ 1 (mod 5) ≠ 0, so the lift succeeds. This condition fails precisely when p = 2 (since 2r₁ is always even) or when p | r₁ (making 2r₁ divisible by p). When it fails, solutions mod pᵏ must be analyzed directly, which is why p = 2 requires special treatment. Option D is backwards: the condition requires p ∤ r₁, not p | r₁."

- question: "If x² ≡ d (mod p) has no solution for some prime p dividing n, then x² ≡ d (mod n) also has no solution."
  type: true-false
  answer: true
  explanation: "By the Chinese Remainder Theorem, x² ≡ d (mod n) splits into independent congruences x² ≡ d (mod pᵢᵃⁱ) for each prime power factor of n. A solution mod n exists only if all component congruences have solutions. In particular, any solution mod n reduces mod p to a solution of x² ≡ d (mod p). Contrapositive: if no solution exists mod p, no solution can exist mod n. This is why the Legendre symbol check is the first gating step — it can immediately rule out solvability."

- question: "The Legendre symbol (d/p) = 1 is sufficient to guarantee that x² ≡ d (mod pᵏ) has a solution for all k ≥ 1, with no further conditions needed."
  type: true-false
  answer: false
  explanation: "For odd primes p and when p ∤ d, Hensel's lemma does extend solutions from mod p to mod pᵏ, so for odd primes with p ∤ r₁ the statement is true. But for p = 2, the Legendre symbol is not even defined, and solvability mod 2ᵏ for k ≥ 3 requires additional conditions on d mod 8. The statement is false as a universal claim. More precisely, the derivative condition 2r₁ ≢ 0 (mod p) must hold for Hensel lifting to succeed automatically, and p = 2 is the primary exception requiring separate analysis."

- question: "Explain the three-tool strategy for solving a general quadratic congruence ax² + bx + c ≡ 0 (mod n), and explain why each of the three tools is necessary."
  type: short-answer
  answer: "Step 1: Complete the square to reduce to x² ≡ d (mod n). Step 2: Factor n = p₁ᵃ¹ · p₂ᵃ² · ··· and use the Chinese Remainder Theorem to decompose into congruences mod each prime power. Step 3: For each prime p, use the Legendre symbol (d/p) to check solvability mod p; then use Hensel's lemma to lift solutions from mod p to mod pᵏ. The three tools are necessary for different levels: the Legendre symbol handles the prime-level existence check, CRT handles how prime-power solutions combine into a solution mod n, and Hensel lifting handles the gap between prime and prime-power solutions."
  explanation: "No single tool handles the full problem: the Legendre symbol only works for primes, not prime powers or composites; CRT requires knowing solutions modulo each prime power component; Hensel lifting only applies to odd primes satisfying the derivative condition. Together they form a complete algorithm. This three-step structure — check, decompose, lift — mirrors the general strategy in number theory of reducing problems about arbitrary moduli to problems about prime powers."
```

## Explainer

A **quadratic congruence** is an equation of the form ax² + bx + c ≡ 0 (mod n). Like a quadratic equation over the reals, the first move is to complete the square and reduce to the form x² ≡ d (mod n) — but now "solving" means deciding whether d is a perfect square in modular arithmetic, and if so, finding the square roots.

Your two prerequisites each handle one part of the problem. The **Legendre symbol** (d/p) tells you whether d is a **quadratic residue** mod p — that is, whether x² ≡ d (mod p) has any solution at all. It equals 1 if a solution exists, −1 if not, and 0 if p | d. So for a prime modulus, you can immediately check solvability. For example, does x² ≡ 5 (mod 7) have a solution? Euler's criterion says (5/7) ≡ 5^(3) ≡ 125 ≡ 6 ≡ −1 (mod 7), so no — 5 is a non-residue mod 7.

The **Chinese Remainder Theorem** handles composite moduli. If n = p₁^(a₁) · p₂^(a₂) · ··· , then x² ≡ d (mod n) splits into separate congruences x² ≡ d (mod p₁^(a₁)), x² ≡ d (mod p₂^(a₂)), and so on. Each can be solved independently, and any combination of solutions can be reassembled into a solution mod n. A solution exists mod n if and only if it exists for every prime power factor.

Solving x² ≡ d (mod pᵏ) for k > 1 is where **Hensel's Lemma** (also called Hensel lifting) enters. The idea mirrors Newton's method: if you have a solution r₁ with r₁² ≡ d (mod p), you can "lift" it to a solution mod p², then mod p³, and so on, as long as 2r₁ ≢ 0 (mod p) — i.e., as long as p is odd and p ∤ r₁. Concretely, the lift is rₖ₊₁ = rₖ − (rₖ² − d)/(2rₖ) mod pᵏ⁺¹, where the division is taken modulo pᵏ⁺¹. The prime p = 2 requires special treatment since the derivative condition fails, and solutions mod 8 must be analyzed by hand before lifting. Combining these tools — Legendre symbol to check solvability, CRT to decompose, Hensel lifting to elevate — gives a complete algorithm for any quadratic congruence.
