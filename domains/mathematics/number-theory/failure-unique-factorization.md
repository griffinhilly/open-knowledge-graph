---
id: failure-unique-factorization
title: Failure of Unique Factorization
domain: mathematics
course: number-theory
prerequisites:
- id: norm-algebraic-number-fields
  type: hard
- id: introduction-to-ideal-class-group
  type: soft
builds-toward:
- introduction-ideal-class-group
tags:
- unique-factorization-failure
- algebraic-number-theory
stage: advanced
status: validated
---
# Failure of Unique Factorization

## Core Idea
Unlike ℤ and Gaussian integers, most rings of algebraic integers lack unique factorization. In ℤ[√(-5)], we have 6 = 2·3 = (1+√(-5))(1-√(-5)), two distinct factorizations. This motivates ideals, where factorization recovers uniqueness.

## Questions

```yaml
- question: "In ℤ[√(−5)], the element 2 is irreducible but not prime. What does this mean, concretely?"
  type: multiple-choice
  options:
    - "2 cannot be written as a product in ℤ[√(−5)], and it does not divide any products"
    - "2 cannot be factored further in ℤ[√(−5)], yet 2 divides (1+√(−5))(1−√(−5))=6 without dividing either factor"
    - "2 is irreducible and its prime norm implies it is prime as a ring element"
    - "2 becomes prime in the ideal-theoretic sense, so the failure of primeness is only apparent"
  answer: 1
  explanation: "2 is irreducible because N(2) = 4 and there is no element of norm 2 in ℤ[√(−5)] (a²+5b²=2 has no integer solutions), so 2 cannot split. But 2 divides 6 = (1+√(−5))(1−√(−5)) = 6 without dividing either factor in the ring — that is the precise failure of primeness. Option C is wrong: prime norm implies irreducibility in many cases, but not primeness; this divergence is exactly what breaks unique factorization. Option D describes the ideal-level resolution, not why element factorization fails."

- question: "Why does ℤ have unique factorization while ℤ[√(−5)] does not?"
  type: multiple-choice
  options:
    - "ℤ is a field while ℤ[√(−5)] is only a ring, and fields always have unique factorization"
    - "In ℤ, every irreducible element is also prime; in ℤ[√(−5)], irreducible and prime diverge"
    - "ℤ[√(−5)] contains elements of both positive and negative norm, making factorization ambiguous"
    - "ℤ has a norm function while ℤ[√(−5)] does not, preventing irreducibility detection"
  answer: 1
  explanation: "A ring is a UFD if and only if every irreducible element is prime. In ℤ, this holds — the Euclidean algorithm yields Bézout's identity, which forces every irreducible to be prime. In ℤ[√(−5)], the element 2 is irreducible but not prime, breaking the chain. Option A is wrong — ℤ is not a field (1/2 ∉ ℤ). Option D is wrong — ℤ[√(−5)] does have a norm function N(a+b√(−5)) = a²+5b²; it is essential for proving irreducibility."

- question: "In any ring of algebraic integers, every irreducible element is prime."
  type: true-false
  answer: false
  explanation: "This is false in general, and the failure is precisely what produces non-unique factorization. In ℤ[√(−5)], the element 2 is irreducible but not prime — it divides a product without dividing either factor. In ℤ and ℤ[i], irreducible and prime coincide, but that is a special property of those rings (they are UFDs). The divergence between irreducible and prime is the algebraic heart of the phenomenon this topic describes."

- question: "The two factorizations 6 = 2·3 = (1+√(−5))(1−√(−5)) in ℤ[√(−5)] show that 2 and (1+√(−5)) are associates — equal up to multiplication by a unit."
  type: true-false
  answer: false
  explanation: "Associates differ by a unit. The only units in ℤ[√(−5)] are ±1, so two elements are associates only if one equals ±1 times the other. The four irreducibles 2, 3, (1+√(−5)), (1−√(−5)) are pairwise distinct and none is ±1 times another — they are genuinely different. The two factorizations of 6 are not the same factorization 'up to associates'; they are truly distinct, which is the content of the failure of unique factorization."

- question: "Why do ideals restore unique factorization when element arithmetic fails in rings like ℤ[√(−5)]?"
  type: short-answer
  answer: "In ℤ[√(−5)], element-level irreducibles like 2 are not prime. But when we pass to ideals, the principal ideal (2) factors into prime ideals: (2) = 𝔭₁·𝔭₂. The two apparently different element factorizations of 6 arise from the same underlying unique ideal factorization — they differ because the prime ideals happen to combine differently into principal ideals at the element level. The ideal class group measures how far such recombinations are from trivial, quantifying the failure."
  explanation: "Dedekind invented ideals to rescue unique factorization. Elements are too coarse to see the true multiplicative structure: two different element factorizations can reflect the same prime ideal factorization viewed through different groupings. Passing to ideals resolves the ambiguity. The ideal class group is trivial (all ideals are principal) if and only if the ring is a UFD — making it the natural measure of how badly unique factorization fails."
```

## Explainer

The unique factorization theorem — the fundamental theorem of arithmetic — guarantees that every integer greater than 1 factors into primes in exactly one way. This feels inevitable until you extend arithmetic to larger number systems and watch it break down. The norm of an algebraic integer, which you studied as a prerequisite, is the key tool for detecting irreducibility in these rings.

In the ring ℤ[√(-5)], consider the number 6. On one hand, 6 = 2 × 3. On the other hand, 6 = (1 + √(-5))(1 - √(-5)). Both are factorizations into elements that cannot be factored further — they are **irreducible** in ℤ[√(-5)]. To verify irreducibility, use norms: N(2) = 4, and there is no element in ℤ[√(-5)] with norm 2, since a² + 5b² = 2 has no integer solutions. So 2 cannot split. Similarly for 3, (1 + √(-5)), and (1 - √(-5)). We have four distinct irreducibles appearing in two different products equaling 6.

The failure is subtle: these irreducibles are not **prime** in the ring-theoretic sense. A prime p satisfies: if p divides ab, then p divides a or p divides b. In ℤ, every irreducible is prime — the two concepts coincide. In ℤ[√(-5)], they diverge. For example, 2 divides (1 + √(-5))(1 - √(-5)) = 6, but 2 does not divide either factor individually in this ring. This divergence between irreducible and prime is precisely what produces the two factorizations of 6. Unique factorization holds if and only if every irreducible is prime — equivalently, if and only if the ring is a **unique factorization domain (UFD)**.

The cure is the theory of **ideals**. Rather than factoring elements, we factor ideals, and ideal factorization is always unique in rings of algebraic integers. The ideal (2) in ℤ[√(-5)] factors as a product of two prime ideals, and the ideals (1 ± √(-5)) each factor further. When you recombine these ideal factorizations, the two seemingly different element-level factorizations emerge from the same underlying unique ideal factorization. This is why Dedekind invented ideals: they restore the uniqueness that element arithmetic alone cannot guarantee, and the **ideal class group** — measuring how far a ring is from being a UFD — becomes the central object for quantifying the failure.
