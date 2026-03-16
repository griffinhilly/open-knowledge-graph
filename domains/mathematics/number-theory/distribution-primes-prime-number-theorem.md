---
id: distribution-primes-prime-number-theorem
title: Distribution of Primes and the Prime Number Theorem
domain: mathematics
course: number-theory
prerequisites:
- id: fundamental-theorem-arithmetic-rigorous
  type: hard
- id: introduction-riemann-zeta-function
  type: soft
tags:
- primes
- distribution
- prime-number-theorem
- analytic-number-theory
stage: advanced
status: draft
---

# Distribution of Primes and the Prime Number Theorem

## Core Idea
The Prime Number Theorem states: π(x) ~ x / ln(x) as x → ∞, where π(x) counts primes ≤ x. This central analytic result uses the Riemann zeta function and shows primes thin at a well-defined logarithmic rate.

## Explainer

The Prime Number Theorem is one of the most surprising results in all of mathematics: primes, which seem to appear with no pattern, turn out to be governed by a precise asymptotic law. From your prerequisite work on the Fundamental Theorem of Arithmetic, you know that primes are the irreducible building blocks of the integers. The question the Prime Number Theorem answers is: how abundant are they? If you pick a large number x, how many primes do you expect to find at or below it?

The counting function **π(x)** records exactly that — the number of primes ≤ x. For small values you can compute it directly: π(10) = 4 (the primes 2, 3, 5, 7), π(100) = 25, π(1000) = 168. But as x grows, counting by hand is impossible. The Prime Number Theorem provides the approximation π(x) ~ x / ln(x), meaning the ratio π(x) / (x / ln(x)) tends to 1 as x → ∞. Equivalently, the "probability" that a randomly chosen integer near x is prime is roughly 1/ln(x). The average gap between consecutive primes near x grows like ln(x) — logarithmically, not like a polynomial.

Why ln(x) and not some other function? The connection runs through the **Riemann zeta function** ζ(s) = Σ n⁻ˢ, which encodes prime information via the Euler product formula ζ(s) = Π_p (1 − p⁻ˢ)⁻¹. The zeros of ζ(s) in the complex plane control the error in the approximation — this is why the Riemann Hypothesis, about where those zeros sit, is so important. The proof of the Prime Number Theorem (by Hadamard and de la Vallée-Poussin in 1896) shows ζ(s) has no zeros on the line Re(s) = 1, which is sufficient to establish the asymptotic. A better approximation replaces x/ln(x) with the **logarithmic integral** li(x) = ∫₂ˣ dt/ln(t), which fits the data far more closely.

To build intuition, notice that primes thin out precisely as fast as their own density predicts. Near x = 10⁶, about 1 in every ln(10⁶) ≈ 14 integers is prime. Near x = 10¹⁰, about 1 in 23. The thinning is slow — primes never disappear entirely — but it is regular. The Prime Number Theorem is the first great triumph of analytic methods in number theory: using tools from complex analysis (the zeta function, contour integration) to answer a purely combinatorial question about integers.
