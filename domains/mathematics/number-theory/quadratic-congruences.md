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
status: draft
---

# Quadratic Congruences

## Core Idea
Quadratic congruences ax^2 + bx + c ≡ 0 (mod n) reduce to a = 1 and a = prime power cases. Solutions exist iff the discriminant is a quadratic residue modulo relevant prime factors, determined via Legendre symbols and Hensel lifting.

## Explainer

A **quadratic congruence** is an equation of the form ax² + bx + c ≡ 0 (mod n). Like a quadratic equation over the reals, the first move is to complete the square and reduce to the form x² ≡ d (mod n) — but now "solving" means deciding whether d is a perfect square in modular arithmetic, and if so, finding the square roots.

Your two prerequisites each handle one part of the problem. The **Legendre symbol** (d/p) tells you whether d is a **quadratic residue** mod p — that is, whether x² ≡ d (mod p) has any solution at all. It equals 1 if a solution exists, −1 if not, and 0 if p | d. So for a prime modulus, you can immediately check solvability. For example, does x² ≡ 5 (mod 7) have a solution? Euler's criterion says (5/7) ≡ 5^(3) ≡ 125 ≡ 6 ≡ −1 (mod 7), so no — 5 is a non-residue mod 7.

The **Chinese Remainder Theorem** handles composite moduli. If n = p₁^(a₁) · p₂^(a₂) · ··· , then x² ≡ d (mod n) splits into separate congruences x² ≡ d (mod p₁^(a₁)), x² ≡ d (mod p₂^(a₂)), and so on. Each can be solved independently, and any combination of solutions can be reassembled into a solution mod n. A solution exists mod n if and only if it exists for every prime power factor.

Solving x² ≡ d (mod pᵏ) for k > 1 is where **Hensel's Lemma** (also called Hensel lifting) enters. The idea mirrors Newton's method: if you have a solution r₁ with r₁² ≡ d (mod p), you can "lift" it to a solution mod p², then mod p³, and so on, as long as 2r₁ ≢ 0 (mod p) — i.e., as long as p is odd and p ∤ r₁. Concretely, the lift is rₖ₊₁ = rₖ − (rₖ² − d)/(2rₖ) mod pᵏ⁺¹, where the division is taken modulo pᵏ⁺¹. The prime p = 2 requires special treatment since the derivative condition fails, and solutions mod 8 must be analyzed by hand before lifting. Combining these tools — Legendre symbol to check solvability, CRT to decompose, Hensel lifting to elevate — gives a complete algorithm for any quadratic congruence.
