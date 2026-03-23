---
id: cardinality-and-countability-methods-of-proof
title: Cardinality and Countability
domain: mathematics
course: methods-of-proof
prerequisites:
- id: injective-surjective-bijective
  type: hard
tags:
- cardinality
- infinity
- countability
stage: formal-systems
status: validated
---

# Cardinality and Countability

## Core Idea
Cardinality measures set size via bijections: two sets have equal cardinality if a bijection exists between them. A set is countable if it has the same cardinality as ℕ. This enables precise reasoning about infinite sets.

## Questions

```yaml
- question: "The set of even natural numbers {0, 2, 4, 6, ...} compared to the set of all natural numbers ℕ has:"
  type: multiple-choice
  options:
    - "Smaller cardinality, since it is a proper subset"
    - "The same cardinality, since the bijection n ↦ 2n maps ℕ onto the even numbers"
    - "Larger cardinality, since even numbers grow faster"
    - "Incomparable cardinality — they cannot be directly compared"
  answer: 1
  explanation: "The function n ↦ 2n is a bijection from ℕ to the even natural numbers: it is injective (different inputs give different outputs) and surjective (every even number is hit). Since a bijection exists, the two sets have the same cardinality — both are countably infinite (cardinality ℵ₀). This is one of the counterintuitive consequences of Cantor's definition: a proper subset of an infinite set can have the same cardinality as the whole set. Option A reflects the naive view that proper subsets must be smaller, which holds for finite sets but fails for infinite ones."

- question: "Cantor's diagonal argument shows that the real numbers ℝ are uncountable. What is the key move that makes the proof work?"
  type: multiple-choice
  options:
    - "It counts the number of real numbers and shows there are more than ℕ"
    - "It assumes a complete list of reals exists and constructs a real number that differs from every entry on the list"
    - "It shows that the rationals ℚ cannot be listed, so ℝ cannot be either"
    - "It uses the fact that ℝ contains irrational numbers, which ℕ cannot index"
  answer: 1
  explanation: "The diagonal argument is a proof by contradiction. Assume you have a list r₁, r₂, r₃, ... that purportedly covers every real in [0,1]. Construct a new real by taking the nth decimal digit of rₙ and changing it. This new number differs from r₁ in the first digit, from r₂ in the second digit, and so on — it cannot be anywhere on the list. This contradicts the assumption that the list was complete. The proof doesn't count the reals; it shows that ANY list must be incomplete. Option C is wrong because ℚ is actually countable."

- question: "The rational numbers ℚ are uncountable because they are densely packed between the integers."
  type: true-false
  answer: false
  explanation: "This is a common misconception. Despite being dense (between any two rationals lies another), the rationals are countably infinite — the same cardinality as ℕ. Cantor's diagonal-grid argument shows this: arrange all fractions p/q in a 2D grid (rows indexed by numerator, columns by denominator), then trace a zigzag path through the grid. Every rational appears somewhere, so this path defines a bijection with ℕ. Density is not the same as uncountability — density is about ordering, cardinality is about size measured by bijection."

- question: "The power set of any infinite set A has strictly greater cardinality than A itself."
  type: true-false
  answer: true
  explanation: "This is Cantor's theorem, and it holds for any set — finite or infinite. The proof uses a diagonal argument: suppose a bijection f: A → P(A) exists. Define the set D = {x ∈ A : x ∉ f(x)}. Since f is a bijection, D = f(a) for some a. Is a ∈ D? If yes, then a ∉ f(a) = D — contradiction. If no, then a ∈ f(a) = D — contradiction. So no bijection can exist, meaning |P(A)| > |A|. This generates the infinite hierarchy ℵ₀ < c < |P(ℝ)| < ..., with no largest infinity."

- question: "Explain the key step in Cantor's diagonal argument that makes it a proof that no list of real numbers can be complete."
  type: short-answer
  answer: "The key step is the construction of the 'diagonal number.' Given any purported list of reals, you build a new real number by examining the nth decimal digit of the nth entry and choosing a different digit for the nth position of your new number. This construction guarantees the new number differs from every entry on the list in at least one decimal place — it is not r₁ (differs in position 1), not r₂ (position 2), and so on. Because this procedure works for ANY list, no list can be complete. The brilliance is that the argument is constructive: it shows exactly how to find the missing element rather than just asserting one exists."
  explanation: "Students often misunderstand the diagonal argument as a counting proof. It is actually a constructive contradiction: it produces a specific missing element from any proposed list, making the incompleteness explicit rather than merely asserting it. The diagonal structure — using the nth entry to define the nth digit — is what ensures the new number is missed by every entry simultaneously."
```

## Explainer

You have already studied injections, surjections, and bijections as tools for comparing sets by pairing their elements. **Cardinality** lifts this idea to a definition of "size": two sets have the same cardinality if and only if a bijection exists between them. For finite sets this agrees with ordinary counting — a bijection from a 5-element set to a 3-element set cannot exist, and that impossibility is exactly what "5 ≠ 3" means. The power of the definition is that it extends unchanged to infinite sets, generating a rich and surprising theory.

A set is **countably infinite** if a bijection exists between it and the natural numbers ℕ. This might seem to describe only ℕ itself, but many larger-looking sets turn out countable too. The integers ℤ are countable: list them as 0, 1, −1, 2, −2, 3, −3, ..., which is an explicit bijection with ℕ. The rationals ℚ are countable via Cantor's diagonal-grid argument: arrange all fractions p/q in a grid indexed by numerator and denominator, then trace a zigzag path through the grid — every rational appears, so the path defines a surjection from ℕ onto ℚ, implying countability. More generally, a countable union of countable sets is countable, so countability is surprisingly hard to escape once you have it.

Yet not all infinite sets are countable. The real numbers ℝ are **uncountable** — their cardinality, denoted **c**, is strictly greater than ℵ₀ (the cardinality of ℕ). Cantor's diagonal proof demonstrates this directly. Suppose you claim to have a list r₁, r₂, r₃, ... covering every real in [0, 1]. Construct a new number by taking the nth decimal digit of rₙ and changing it. This new number differs from every rₙ in at least one position, so it cannot appear on the list — contradicting completeness. Any list misses a real; therefore no bijection between ℕ and ℝ exists. Notice that the proof is constructive: it shows you exactly how to find the missing element given any purported bijection.

The argument generalizes: the **power set** P(A) always has strictly greater cardinality than A, for any set A. This means there is no "largest" infinity — there is an unending hierarchy ℵ₀ < c < P(c) < .... In proof work, cardinality arguments appear in two modes. Constructively, you exhibit a bijection to establish equality of size (e.g., show that an odd natural number corresponds bijectively to every natural number). By contradiction, you assume a bijection exists and derive a diagonalization contradiction to prove no such bijection can exist — as with ℝ. Recognizing which mode applies is a core skill in reasoning about infinite sets.
