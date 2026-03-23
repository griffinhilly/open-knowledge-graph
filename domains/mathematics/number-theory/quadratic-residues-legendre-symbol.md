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
status: validated
---

# Quadratic Residues and the Legendre Symbol

## Core Idea
For odd prime p and a not divisible by p, the Legendre symbol (a/p) is +1 if a is a quadratic residue mod p (i.e., x^2 ≡ a mod p solvable) and -1otherwise. Exactly (p-1)/2 residues among 1, 2, ..., p-1 are quadratic residues.

## Questions

```yaml
- question: "If the Legendre symbol satisfies (ab/p) = (a/p)(b/p), and you know that (a/p) = −1 and (b/p) = −1, what is (ab/p)?"
  type: multiple-choice
  options:
    - "−1, because the product of two non-residues should remain a non-residue"
    - "+1, because the Legendre symbol is multiplicative and (−1)(−1) = +1"
    - "0, because the product of two non-residues might be divisible by p"
    - "It depends on the specific values of a and b, not just their symbols"
  answer: 1
  explanation: "The Legendre symbol is a group homomorphism from (ℤ/pℤ)× to {±1}, so it multiplies exactly like signs: (−1)(−1) = +1. The product of two quadratic non-residues is always a quadratic residue. This can be understood structurally: the QRs form an index-2 subgroup of (ℤ/pℤ)×, and the product of two elements from the non-residue coset lands back in the subgroup. Option A represents the common intuition that 'two bad things make a bad thing' — it is exactly wrong here."

- question: "How many quadratic residues are there among {1, 2, 3, ..., 10} modulo 11?"
  type: multiple-choice
  options:
    - "4"
    - "5"
    - "6"
    - "10"
  answer: 1
  explanation: "For any odd prime p, exactly (p−1)/2 of the nonzero residues mod p are quadratic residues. With p = 11, that's (11−1)/2 = 5. The reason: the squaring map x ↦ x² on (ℤ/11ℤ)× is 2-to-1, since x and −x (= 11−x) both square to x². With 10 nonzero elements and each QR hit twice, there are exactly 5 distinct squares. You can verify: 1²=1, 2²=4, 3²=9, 4²=5, 5²=3 (mod 11) — these 5 values are the QRs."

- question: "If a is a quadratic non-residue mod p, then a² is also a quadratic non-residue mod p."
  type: true-false
  answer: false
  explanation: "False. For any integer a with p ∤ a, a² is by definition a perfect square — it is always a quadratic residue mod p. Non-residuosity of a means no integer x satisfies x² ≡ a; but a itself squares to a², so a² is always a QR. The Legendre symbol confirms this: (a²/p) = (a/p)² = (−1)² = +1."

- question: "The Legendre symbol (ab/p) = (a/p)(b/p) holds even when a or b is a quadratic non-residue mod p."
  type: true-false
  answer: true
  explanation: "True. Multiplicativity is unconditional (as long as p does not divide a or b). The formula works whether each factor is +1 or −1. This is what makes the Legendre symbol a group homomorphism: it respects multiplication in (ℤ/pℤ)× and sends it to multiplication in {±1}. The fact that QNR × QNR = QR (i.e., (−1)(−1) = 1) is a consequence of this homomorphism property, not an exception to it."

- question: "Explain why exactly half of the integers in {1, 2, ..., p−1} are quadratic residues mod p, for an odd prime p."
  type: short-answer
  answer: "The squaring map x ↦ x² on (ℤ/pℤ)× is exactly 2-to-1: both x and −x square to x², and since p is odd, x and −x are always distinct (x ≡ −x would force 2x ≡ 0, i.e., p | x, contradicting our assumption). So the p−1 nonzero elements pair up into (p−1)/2 pairs {x, −x}, with each pair producing one distinct square. The image of the squaring map therefore has exactly (p−1)/2 elements — precisely half the nonzero residues."
  explanation: "The key is that x ≠ −x mod p when p is odd, so the 2-to-1 pairing is exact with no collisions. The same argument fails for p = 2 (where x ≡ −x for all x), which is why the theory of quadratic residues restricts to odd primes. The (p−1)/2 QRs form the kernel of the Legendre symbol homomorphism, making them a subgroup of index 2 in (ℤ/pℤ)×."
```

## Explainer

A **quadratic residue** mod p is an integer congruent to a perfect square mod p. More precisely, a (with p ∤ a) is a quadratic residue if x² ≡ a (mod p) has a solution. You already know from modular arithmetic that the nonzero residues mod p form a group under multiplication — the group (ℤ/pℤ)×, which has p−1 elements. A fundamental fact is that among these p−1 nonzero residues, exactly half are quadratic residues.

Why exactly half? The squaring map x ↦ x² sends (ℤ/pℤ)× to itself, but is 2-to-1: both x and −x square to x². Since gcd(m,p) = 1, x ≢ −x (mod p) when p is odd (as x ≡ −x would give 2x ≡ 0, so p | x), so x and −x are genuinely distinct. Each quadratic residue is hit exactly twice, and there are p−1 elements total, giving (p−1)/2 distinct squares — exactly half the nonzero residues. The **Legendre symbol** packages this: (a/p) = +1 if a is a quadratic residue (QR), −1 if a is a non-residue (QNR), and 0 if p | a.

The Legendre symbol is **multiplicative**: (ab/p) = (a/p)(b/p). This follows from the group structure. QR × QR = QR (the product of two squares is a square); QNR × QNR = QR (the product of two non-residues turns out to be a residue, since the squaring map's kernel — the QRs — forms an index-2 subgroup of (ℤ/pℤ)×, and the coset product of two non-residues lands in the subgroup); QR × QNR = QNR. The sign pattern is identical to multiplying +1 and −1, which is why the Legendre symbol is a group homomorphism from (ℤ/pℤ)× to {±1}.

**Euler's criterion** connects the Legendre symbol to direct computation: (a/p) ≡ a^{(p−1)/2} (mod p). To see why: by Fermat's little theorem, a^{p−1} ≡ 1 (mod p), so a^{(p−1)/2} is a square root of 1 mod p, meaning it equals ±1. If a = x² is a QR, then a^{(p−1)/2} = x^{p−1} ≡ 1. If a is a QNR, the value is −1. This criterion lets you determine quadratic residuosity by fast exponentiation, without searching for square roots. For example, is 3 a quadratic residue mod 11? Compute 3⁵ = 243 = 22 × 11 + 1 ≡ 1 (mod 11), so (3/11) = +1, confirming that x² ≡ 3 (mod 11) is solvable (x = 5 and x = 6 both work). The Legendre symbol and Euler's criterion together set up the machinery for the law of quadratic reciprocity, which relates (p/q) and (q/p) for distinct odd primes p and q.
