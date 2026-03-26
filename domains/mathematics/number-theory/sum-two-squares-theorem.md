---
id: sum-two-squares-theorem
title: Sum of Two Squares Theorem
domain: mathematics
course: number-theory
prerequisites:
- id: fundamental-theorem-arithmetic-rigorous
  type: hard
- id: lagranges-four-square-theorem
  type: soft
tags:
- sum-of-squares
- diophantine
- representation
stage: advanced
status: validated
---
# Sum of Two Squares Theorem

## Core Idea
An integer n is representable as n = a^2 + b^2 iff in its prime factorization, every prime p ≡ 3 (mod 4) appears to an even power. This theorem connects number theory and geometry; Gaussian integers provide an elegant proof.

## Questions

```yaml
- question: "Is the number 45 = 3² × 5 expressible as a sum of two squares?"
  type: multiple-choice
  options:
    - "No, because 3 ≡ 3 (mod 4) and 3 divides 45"
    - "Yes, because although 3 ≡ 3 (mod 4), it appears to an even power (3²), so the theorem allows it"
    - "No, because 45 is odd and sums of two squares are always even"
    - "Yes, because 5 ≡ 1 (mod 4), which dominates the factorization"
  answer: 1
  explanation: "The theorem states that n is a sum of two squares if and only if every prime p ≡ 3 (mod 4) in its factorization appears to an even power. Here 3 ≡ 3 (mod 4) but appears to the power 2 (even), and 5 ≡ 1 (mod 4) so it imposes no constraint. Therefore 45 is representable: 45 = 36 + 9 = 6² + 3². Option A is the classic error: seeing a mod-3 prime and immediately concluding 'not representable,' forgetting the even-power exception. Option C is wrong: squares can be odd (e.g., 1² = 1)."

- question: "What does it mean in the Gaussian integers ℤ[i] for a prime p to 'remain inert,' and why does inertness prevent p from being a sum of two squares?"
  type: multiple-choice
  options:
    - "An inert prime p does not generate any ideals in ℤ[i], so it cannot be decomposed as a norm"
    - "An inert prime remains prime in ℤ[i] — it cannot be written as a product of two Gaussian integers of smaller norm — so p ≠ |α|² for any α ∈ ℤ[i]"
    - "An inert prime has no Gaussian conjugate, so it cannot appear in a factorization involving complex numbers"
    - "An inert prime generates a principal ideal in ℤ[i] that is also prime in ℤ, creating a circular factorization"
  answer: 1
  explanation: "In ℤ[i], the norm of α = a + bi is N(α) = a² + b² — exactly the quantity we want to represent. So p is a sum of two squares if and only if p = N(α) for some Gaussian integer α, i.e., p = α·ᾱ splits as a product of two conjugate Gaussian primes. A prime that is 'inert' remains prime in ℤ[i] — it does not split. Since inert primes cannot be expressed as such a product, they cannot equal a norm N(α), and therefore cannot be sums of two squares. Primes p ≡ 3 (mod 4) are exactly the inert primes."

- question: "Every prime p ≡ 1 (mod 4) can be written as a sum of two squares."
  type: true-false
  answer: true
  explanation: "This is part of Fermat's theorem on sums of two squares. Primes p ≡ 1 (mod 4) split in the Gaussian integers: p = π · π̄ where π = a + bi is a Gaussian prime with |π|² = a² + b² = p. Examples: 5 = 1² + 2², 13 = 2² + 3², 17 = 1² + 4², 29 = 2² + 5². The splitting behavior is controlled by quadratic reciprocity: −1 is a quadratic residue mod p exactly when p ≡ 1 (mod 4), which is what allows ℤ[i] to factor p. Primes p ≡ 3 (mod 4) are inert and never split, so they cannot be sums of two squares."

- question: "The number 63 = 3² × 7 can seldom be expressed as a sum of two squares, because both 3 and 7 are congruent to 3 mod 4."
  type: true-false
  answer: false
  explanation: "The theorem requires that *every* prime p ≡ 3 (mod 4) appear to an even power. Here 3 appears to the power 2 (even) — this is allowed. But 7 ≡ 3 (mod 4) appears to the power 1 (odd) — this blocks representability. So 63 cannot be a sum of two squares, but *not* because both primes are ≡ 3 mod 4. It fails because 7 appears to an odd power. If 63 = 3² × 7 fails but 45 = 3² × 5 succeeds, the question is about the specific prime 7 appearing to an odd power. The statement's reasoning ('because both are ≡ 3 mod 4') is wrong even though the conclusion (not representable) happens to be right."

- question: "Why do primes p ≡ 3 (mod 4) block the representation of n as a sum of two squares when they appear to an odd power, but not when they appear to an even power? Use the Gaussian integer framework."
  type: short-answer
  answer: "In ℤ[i], primes p ≡ 3 (mod 4) are inert — they remain prime and do not split. This means p cannot be written as N(π) = a² + b² for any Gaussian integer π. When p appears to an odd power in n, the factorization of n in ℤ[i] contains a factor of p that cannot be paired with its conjugate, so n cannot be expressed as a norm N(α) = a² + b². But when p appears to an even power, two copies of p together give p² = (p + 0i)(p − 0i), which is a norm (N(p) = p²), and this can contribute to a representation of n. The even-power condition is exactly what allows the inert primes to 'cancel out' and leave n as a norm."
  explanation: "The Gaussian integer framework reveals why the condition is about even vs. odd powers, not just about which primes appear. Each inert prime must appear in matched pairs to be expressible as a norm. One unpaired inert prime leaves a factor that lives in ℤ[i] only as an integer (no complex part), preventing the overall expression as a² + b² with b ≠ 0. This is why 9 = 3² = 3² + 0² barely works (as a trivial square) while 3 itself cannot be written as a sum of two squares in a nontrivial way."
```

## Explainer

You already know from the fundamental theorem of arithmetic that every positive integer has a unique factorization into primes. The sum of two squares theorem gives a precise answer to the question: which integers live on the integer lattice of a circle? That is, for which n does the equation n = a² + b² have an integer solution? The answer depends entirely on the prime factorization of n, and specifically on how primes behave modulo 4.

Start with primes. The prime 2 = 1² + 1² works. For odd primes, there are only two residues mod 4: either p ≡ 1 (mod 4) or p ≡ 3 (mod 4). It turns out that every prime p ≡ 1 (mod 4) is representable as a sum of two squares — for example, 5 = 1² + 2², 13 = 2² + 3², 17 = 1² + 4² — while no prime p ≡ 3 (mod 4) is representable. You can verify the latter: modulo 4, squares are always 0 or 1, so a² + b² is congruent to 0, 1, or 2 (mod 4) — never 3. This means primes like 3, 7, 11, 19 can never be written as a sum of two squares.

The elegant proof uses the **Gaussian integers** ℤ[i] = {a + bi : a, b ∈ ℤ}. The key insight is that a² + b² = (a + bi)(a − bi) = |a + bi|². So asking whether n is a sum of two squares is the same as asking whether n is the norm of a Gaussian integer. Primes p ≡ 3 (mod 4) remain **inert** (prime) in ℤ[i] — they don't factor further. Primes p ≡ 1 (mod 4) **split**: p = π · π̄ for a Gaussian prime π = a + bi with |π|² = p. This is why such primes are sums of two squares. The prime 2 **ramifies**: 2 = −i(1+i)².

To handle composite n, you need a multiplicative identity: if m and n are both sums of two squares, so is mn. This follows from the Gaussian integer norm being multiplicative: N(αβ) = N(α)N(β). It means you can assemble the representation of n from those of its prime factors. The constraint "every prime p ≡ 3 (mod 4) appears to an even power" comes from the fact that such primes must pair up — each contributes a factor of p to the norm, and two inert primes p · p = p² = (p + 0i)(p − 0i) is representable. The theorem is one of the cleanest examples of how algebraic structure in an extended ring (ℤ[i]) illuminates purely arithmetic questions about ℤ.
