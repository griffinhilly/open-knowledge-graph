---
id: distribution-of-primes
title: Distribution of Primes
domain: mathematics
course: number-theory
prerequisites:
- id: fundamental-theorem-of-arithmetic-rigorous
  type: soft
builds-toward:
- prime-number-theorem
- prime-counting-function
tags:
- primes
- distribution
- analytic-number-theory
stage: advanced
status: draft
---

# Distribution of Primes

## Core Idea
The distribution of primes among integers is irregular locally yet systematic globally. Prime gaps grow, primes become sparser as numbers increase, yet never entirely disappear. Understanding this distribution is central to analytic number theory and has applications to cryptography and computational mathematics.

## Explainer

The primes 2, 3, 5, 7, 11, 13, 17, 19, 23, 29 look almost random at first glance — they don't follow an obvious arithmetic pattern like the even numbers or multiples of 3. Yet zoom out far enough, and a striking regularity emerges: primes thin out in a precise, predictable way as numbers grow larger. This tension between local randomness and global order is what makes the distribution of primes one of the deepest subjects in mathematics.

Your prerequisite — the **Fundamental Theorem of Arithmetic** — tells you that every integer greater than 1 factors uniquely into primes. This means primes are the "atoms" of multiplication: every composite number is built from them. From this perspective, asking how primes are distributed is really asking how the multiplicative structure of the integers thins out. A number near N is prime only if it is not divisible by any prime up to √N. As N grows, there are more small primes that could divide it, so the chance of escaping all of them shrinks — and indeed, primes do become sparser as numbers grow larger.

How much sparser? The **prime-counting function** π(N) counts the number of primes up to N. Empirically, π(100) = 25, π(1000) = 168, π(10000) = 1229. Notice that while the count keeps growing, it grows more slowly relative to N — primes become less dense. The key insight, formalized by the **Prime Number Theorem** (which this topic builds toward), is that π(N) ≈ N / ln(N). The natural logarithm appears here not by coincidence but because of deep connections between primes and the logarithm through the Riemann zeta function and related machinery.

**Prime gaps** — the spacings between consecutive primes — illustrate the local irregularity directly. After 2 and 3 (the only gap of 1), the gaps are 2, 2, 4, 2, 4, 2, 4, 6, 2... and grow without bound on average, yet "twin primes" (gaps of 2 like 11 and 13, or 17 and 19) keep reappearing, apparently forever. Whether they appear infinitely often is one of the great unsolved problems in mathematics. The upshot is this: globally, the density of primes near N is approximately 1/ln(N) — so among integers near a billion, roughly 1 in 20 is prime — but locally, the exact placement of individual primes remains unpredictable, governed by a randomness that is, in a deep sense, not really random at all.
