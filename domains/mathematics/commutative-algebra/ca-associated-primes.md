---
id: ca-associated-primes
title: Associated Primes
domain: mathematics
course: commutative-algebra
prerequisites:
- id: ca-primary-decomposition
  type: hard
- id: ca-noetherian-rings
  type: hard
- id: ca-modules-over-rings
  type: soft
builds-toward:
- ca-regular-sequences
tags:
- associated-prime
- support
- zero-divisor
- embedded-prime
- minimal-prime
- annihilator
stage: expert
status: validated
---

# Associated Primes

## Core Idea
An associated prime of an R-module M is a prime ideal that occurs as the annihilator of some element of M. The set Ass(M) captures where M "lives" in Spec R: the zero divisors on M are exactly the union of the associated primes, the minimal associated primes correspond to the irreducible components of the support, and the embedded associated primes detect deeper non-reduced structure. For Noetherian rings, Ass(M) is finite and provides the prime-level data underlying primary decomposition.

## Questions

```yaml
- question: "What are the associated primes of Z/12Z as a Z-module?"
  type: multiple-choice
  options:
    - "{(2), (3)}"
    - "{(2), (3), (12)}"
    - "{(2), (4), (3)}"
    - "{(0), (2), (3)}"
  answer: 0
  explanation: "The primary decomposition of (12) in Z is (12) = (4) ∩ (3). The associated primes are the radicals of the primary components: √(4) = (2) and √(3) = (3). So Ass(Z/12Z) = {(2), (3)}. These are both minimal primes of (12); there are no embedded primes in this case."

- question: "In a Noetherian ring R, the set of zero divisors equals the union of the associated primes of R (as a module over itself)."
  type: true-false
  answer: true
  explanation: "An element r is a zero divisor on R iff r annihilates some nonzero element, iff r lies in ann(x) for some x ≠ 0. In a Noetherian ring, every such annihilator is contained in an associated prime (an annihilator that is itself prime). So the zero divisors are exactly the union of Ass(R). This characterization is much more precise than just 'the set of zero divisors.'"

- question: "What is the difference between minimal and embedded associated primes?"
  type: short-answer
  answer: "Minimal associated primes are the minimal elements of Ass(M) under inclusion -- they correspond to irreducible components of Supp(M). Embedded associated primes are non-minimal elements of Ass(M) -- they are 'hidden' inside larger components and represent non-reduced or non-generic structure."
  explanation: "For example, in k[x,y] the ideal I = (x^2, xy) has Ass(R/I) = {(x), (x,y)}. The prime (x) is minimal (it defines the line x = 0), while (x,y) is embedded (the origin is 'inside' the line). Embedded primes depend on the particular decomposition and are the source of much subtlety in algebraic geometry."

- question: "For a Noetherian module M over a Noetherian ring R, Ass(M) is always a finite set."
  type: true-false
  answer: true
  explanation: "This follows from the existence of primary decomposition for submodules of Noetherian modules. The zero submodule 0 ⊂ M has a primary decomposition 0 = Q_1 ∩ ... ∩ Q_n in M, and Ass(M) equals the set of primes {√ann(M/Q_i)}. Since primary decomposition is finite, so is Ass(M). The minimal primes are independent of the decomposition; the embedded ones may vary."

- question: "Explain the relationship between Ass(M), Supp(M), and the minimal primes of ann(M)."
  type: short-answer
  answer: "Ass(M) ⊆ Supp(M), and the minimal elements of both sets coincide (they equal the minimal primes of ann(M)). Supp(M) is the closure of Ass(M) in Spec R. Every prime in Supp(M) contains an associated prime."
  explanation: "Supp(M) = {P in Spec R : M_P ≠ 0} = V(ann(M)), the set of primes containing ann(M). The minimal primes of Supp(M) are exactly the minimal associated primes. Supp(M) can be much larger than Ass(M) -- it is the closure, while Ass(M) picks out the 'generic points' of the irreducible components plus any embedded structure."
```

## Explainer

**Associated primes** provide a prime-by-prime decomposition of the structure of a module. For an R-module M, a prime ideal P is an **associated prime** of M if P = ann(m) for some element m in M -- that is, P is the exact set of ring elements that kill some specific module element. The collection Ass(M) of all associated primes is the fundamental invariant connecting modules to the geometry of Spec R.

The most important property of associated primes is their relationship to **zero divisors**: in a Noetherian ring, the set of zero divisors on M equals the union of the associated primes of M. This transforms the amorphous "set of zero divisors" into a precise union of prime ideals. For a Noetherian ring R itself, the zero divisors of R are the union of Ass(R), and R is a domain if and only if Ass(R) = {(0)}. The associated primes also determine the **support** of M: Supp(M) is the Zariski closure of Ass(M), and the minimal primes of Supp(M) are exactly the minimal associated primes.

The distinction between **minimal** and **embedded** associated primes is geometrically significant. The minimal associated primes correspond to the irreducible components of Supp(M) -- they are the "generic points" of the locus where M lives. The embedded associated primes are strictly contained in some other associated prime and represent non-reduced or higher-order structure at special points. For example, if I = (x^2, xy) in k[x, y], then R/I has associated primes (x) and (x, y). The prime (x) is minimal, corresponding to the line {x = 0}. The prime (x, y) is embedded -- the origin has "extra nilpotent structure" not captured by the minimal component. Embedded primes are not determined by the module alone in the same way minimal primes are; different primary decompositions of the same ideal can produce different embedded primes.

Associated primes connect to primary decomposition via the formula: if 0 = Q_1 ∩ ... ∩ Q_n is an irredundant primary decomposition of the zero submodule of M, then Ass(M) = {√(ann(M/Q_1)), ..., √(ann(M/Q_n))}. This gives Ass(M) as the set of primes "appearing in" the primary decomposition. The technology of associated primes extends naturally to the study of **depth** (the length of a maximal regular sequence in the maximal ideal, which equals the smallest i with Ext^i(R/m, M) ≠ 0 for local rings) and **Cohen-Macaulay** conditions, where the interplay between associated primes and regular sequences becomes central.
