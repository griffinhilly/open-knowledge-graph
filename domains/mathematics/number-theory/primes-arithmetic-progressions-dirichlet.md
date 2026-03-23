---
id: primes-arithmetic-progressions-dirichlet
title: Primes in Arithmetic Progressions (Dirichlet's Theorem)
domain: mathematics
course: number-theory
prerequisites:
- id: dirichlet-series-l-functions
  type: hard
- id: congruence-properties
  type: hard
tags:
- dirichlet-theorem
- primes
- arithmetic-progressions
- analytic-number-theory
stage: advanced
status: validated
---

# Primes in Arithmetic Progressions (Dirichlet's Theorem)

## Core Idea
If gcd(a,d) = 1, there are infinitely many primes p ≡ a (mod d). The proof uses Dirichlet characters and L-functions, showing primes equidistribute among allowed residue classes.

## Questions

```yaml
- question: "Consider arithmetic progressions modulo 10. Which residue classes mod 10 contain infinitely many primes?"
  type: multiple-choice
  options:
    - "Only class 1 (mod 10), since 1 is the identity residue"
    - "Classes 1 and 9 (mod 10), since these are symmetric around 5"
    - "Classes 1, 3, 7, and 9 (mod 10) — exactly those coprime to 10"
    - "All odd residue classes: 1, 3, 5, 7, 9 (mod 10)"
  answer: 2
  explanation: "Dirichlet's theorem guarantees infinitely many primes in class a (mod d) if and only if gcd(a, d) = 1. The classes coprime to 10 are exactly {1, 3, 7, 9} — the φ(10) = 4 classes sharing no factor with 10. Class 5 (mod 10) fails because every element is divisible by 5, so at most one prime (namely 5 itself) can appear there. Class 9 is coprime to 10 and does contain infinitely many primes, as does class 3. The equidistribution result further says each eligible class receives asymptotically 1/4 of all primes."

- question: "In Dirichlet's proof, the key step is showing L(1, χ) ≠ 0 for all non-principal Dirichlet characters χ. Why is this non-vanishing essential?"
  type: multiple-choice
  options:
    - "It guarantees the L-function converges absolutely for all s in the complex plane"
    - "It prevents the divergence argument — which forces infinitely many primes in each eligible class — from collapsing to a finite sum"
    - "It establishes that Dirichlet characters form a complete orthogonal basis for functions mod d"
    - "It implies the Riemann hypothesis holds for these L-functions"
  answer: 1
  explanation: "The proof shows that the sum of 1/p over primes p ≡ a (mod d) diverges, which forces infinitely many such primes. This divergence is derived from the logarithm of a product of L(s, χ) values. If any non-principal L(1, χ) = 0, the relevant factor would cancel the divergence, collapsing the argument to a finite sum. Non-vanishing at s = 1 keeps the divergence intact. This is the deepest step and requires using the full group structure of Dirichlet characters — no single character suffices."

- question: "The arithmetic progression 4, 10, 16, 22, 28, ... (i.e., a ≡ 4 mod 6) contains infinitely many primes."
  type: true-false
  answer: false
  explanation: "Every element has the form 6k + 4 = 2(3k + 2), which is divisible by 2. All elements are even and greater than 2, so none can be prime. The condition gcd(a, d) = 1 fails here: gcd(4, 6) = 2 ≠ 1. Dirichlet's theorem applies precisely when gcd(a, d) = 1. When this fails, every element of the progression shares a factor with d, allowing at most one prime (the factor itself) to appear — and in this case, even 2 does not appear since all elements exceed 2."

- question: "Among primes up to a large number N, approximately 1/φ(d) of all primes lie in each residue class a (mod d) with gcd(a, d) = 1."
  type: true-false
  answer: true
  explanation: "This is the equidistribution part of the Prime Number Theorem for Arithmetic Progressions, which strengthens Dirichlet's theorem. Beyond merely asserting infinitely many primes in each eligible class, it says the primes are distributed democratically: each of the φ(d) eligible classes receives asymptotically the same share 1/φ(d) of all primes. For example, among primes mod 4, roughly half are ≡ 1 (mod 4) and half are ≡ 3 (mod 4). Despite their irregular individual behavior, primes collectively show perfect fairness across eligible residue classes."

- question: "Why is gcd(a, d) = 1 both necessary and sufficient for the progression a, a+d, a+2d, ... to contain infinitely many primes? What goes wrong in each direction when the condition fails?"
  type: short-answer
  answer: "Necessity: if gcd(a, d) = k > 1, then every term a + nd is divisible by k, so no term greater than k can be prime — at most one prime appears. Sufficiency: when gcd(a, d) = 1, Dirichlet's proof via Dirichlet characters and the non-vanishing of L(1, χ) establishes that the sum of 1/p over eligible primes diverges, which forces infinitely many such primes."
  explanation: "The necessity side is elementary — any common factor of a and d divides every term of the progression, blocking primality for all but possibly the factor itself. The sufficiency side requires deep analytic machinery. Together, gcd(a, d) = 1 is the exact dividing line: infinitely many primes when the condition holds, at most one when it fails. This clean characterization is what makes the theorem so satisfying — the number-theoretic condition and the analytic proof align perfectly."
```

## Explainer

Start with a basic observation from your study of congruences: the integers modulo d split into residue classes 0, 1, 2, ..., d−1. Some of these classes cannot contain primes other than d itself — for example, class 0 mod d contains only multiples of d, and class 0 mod 6 contains multiples of 6, which are composite. But what about the classes that *could* contain primes? Is it possible that primes, becoming sparser as you go higher, all eventually pile into one residue class and avoid the others?

Dirichlet's Theorem answers this decisively: if gcd(a, d) = 1 — that is, if a and d share no common factor — then the arithmetic progression a, a+d, a+2d, a+3d, ... contains infinitely many primes. The condition gcd(a, d) = 1 is exactly the right condition: if gcd(a, d) = k > 1, then every element of the progression is divisible by k, so only finitely many (if any) can be prime. Beyond this, though, Dirichlet guarantees primes spread out across all the "eligible" residue classes — not just some of them.

The proof strategy draws on the Dirichlet series and L-functions you've studied. The key tool is **Dirichlet characters** — completely multiplicative functions χ: ℤ → ℂ that are periodic mod d and encode information about residue classes. From these characters, Dirichlet constructed **L-functions** L(s, χ) = ∑ χ(n)/n^s, analytic relatives of the Riemann zeta function. The central step of the proof shows that log(number of primes ≤ x in the progression a mod d) grows like (1/φ(d)) · log log x, where φ(d) is Euler's totient — the count of residue classes coprime to d. Since this diverges, there must be infinitely many such primes.

A stronger result, the **Prime Number Theorem for Arithmetic Progressions**, refines this: among primes up to x, approximately x/(φ(d) · ln x) lie in each eligible class mod d. Primes don't just appear infinitely often in each valid class — they appear *equally often* in the long run, a phenomenon called **equidistribution**. This is remarkable: the primes, despite their irregular individual behavior, are perfectly democratic among residue classes when viewed in aggregate.

The key technical ingredient is proving that L(1, χ) ≠ 0 for all non-principal characters χ. This is where Dirichlet's original proof was subtle — he had to show the L-function doesn't vanish at s = 1, which would collapse the divergence argument. The non-vanishing at s = 1 is what separates Dirichlet's theorem from a near-theorem, and it requires using the full multiplicative structure of Dirichlet characters rather than any single character in isolation. This interplay between number-theoretic structure (congruences) and analytic tools (L-functions) is the hallmark of analytic number theory.
