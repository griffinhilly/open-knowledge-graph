---
id: quadratic-residues-legendre-symbol
title: Quadratic Residues and the Legendre Symbol
domain: mathematics
course: number-theory
prerequisites:
- id: congruence-properties
  type: hard
- id: modular-arithmetic
  type: hard
builds-toward:
- eulers-criterion
- law-quadratic-reciprocity
tags:
- quadratic-residues
- legendre-symbol
stage: advanced
status: draft
---

# Quadratic Residues and the Legendre Symbol

## Core Idea
For odd prime p and a not divisible by p, the Legendre symbol (a/p) is +1 if a is a quadratic residue mod p (i.e., x^2 ≡ a mod p solvable) and -1otherwise. Exactly (p-1)/2 residues among 1, 2, ..., p-1 are quadratic residues.

## Explainer

A **quadratic residue** mod p is an integer congruent to a perfect square mod p. More precisely, a (with p ∤ a) is a quadratic residue if x² ≡ a (mod p) has a solution. You already know from modular arithmetic that the nonzero residues mod p form a group under multiplication — the group (ℤ/pℤ)×, which has p−1 elements. A fundamental fact is that among these p−1 nonzero residues, exactly half are quadratic residues.

Why exactly half? The squaring map x ↦ x² sends (ℤ/pℤ)× to itself, but is 2-to-1: both x and −x square to x². Since gcd(m,p) = 1, x ≢ −x (mod p) when p is odd (as x ≡ −x would give 2x ≡ 0, so p | x), so x and −x are genuinely distinct. Each quadratic residue is hit exactly twice, and there are p−1 elements total, giving (p−1)/2 distinct squares — exactly half the nonzero residues. The **Legendre symbol** packages this: (a/p) = +1 if a is a quadratic residue (QR), −1 if a is a non-residue (QNR), and 0 if p | a.

The Legendre symbol is **multiplicative**: (ab/p) = (a/p)(b/p). This follows from the group structure. QR × QR = QR (the product of two squares is a square); QNR × QNR = QR (the product of two non-residues turns out to be a residue, since the squaring map's kernel — the QRs — forms an index-2 subgroup of (ℤ/pℤ)×, and the coset product of two non-residues lands in the subgroup); QR × QNR = QNR. The sign pattern is identical to multiplying +1 and −1, which is why the Legendre symbol is a group homomorphism from (ℤ/pℤ)× to {±1}.

**Euler's criterion** connects the Legendre symbol to direct computation: (a/p) ≡ a^{(p−1)/2} (mod p). To see why: by Fermat's little theorem, a^{p−1} ≡ 1 (mod p), so a^{(p−1)/2} is a square root of 1 mod p, meaning it equals ±1. If a = x² is a QR, then a^{(p−1)/2} = x^{p−1} ≡ 1. If a is a QNR, the value is −1. This criterion lets you determine quadratic residuosity by fast exponentiation, without searching for square roots. For example, is 3 a quadratic residue mod 11? Compute 3⁵ = 243 = 22 × 11 + 1 ≡ 1 (mod 11), so (3/11) = +1, confirming that x² ≡ 3 (mod 11) is solvable (x = 5 and x = 6 both work). The Legendre symbol and Euler's criterion together set up the machinery for the law of quadratic reciprocity, which relates (p/q) and (q/p) for distinct odd primes p and q.
