---
id: cantor-theorem
title: Cantor's Theorem
domain: formal-sciences-and-logic
course: set-theory
prerequisites:
- id: infinite-cardinal-numbers
  type: hard
- id: axiom-of-power-set
  type: soft
- id: cantor-diagonalization
  type: soft
- id: cardinality-and-countability
  type: soft
builds-toward:
- continuum-hypothesis
- cofinality-and-regular-cardinals
tags:
- Cantor's theorem
- power set
- cardinality
- diagonal argument
- uncountability
stage: formal-systems
status: validated
---

# Cantor's Theorem

## Core Idea
Cantor's theorem states that for any set A, the power set P(A) has strictly greater cardinality than A: there is an injection A → P(A) but no surjection. The proof is a diagonal argument: given any function f: A → P(A), the set D = {x ∈ A : x ∉ f(x)} lies in P(A) but is not in the range of f. Applied to ℕ, this shows P(ℕ) is uncountable; applied to any infinite cardinal κ, it shows 2^κ > κ, generating an unbounded tower of infinities. Consequently, there is no largest cardinal — the cardinal numbers form a proper class.

## How It's Best Learned
Prove the theorem first for A = ℕ (Cantor's diagonal argument for the reals). Then abstract the proof to an arbitrary set A. Work through the tower P(ℕ), P(P(ℕ)), P(P(P(ℕ))), ... and verify that each step strictly increases cardinality. Confirm that the diagonal set D is well-defined and always escapes any given f.

## Common Misconceptions
- Cantor's theorem applies to ALL sets, including finite ones: |P(∅)| = 1 > 0 and |P({a})| = 2 > 1.
- The theorem shows no surjection A → P(A) exists, but there is always an injection x ↦ {x} from A into P(A).

## Questions

```yaml
- question: "Cantor's theorem states that |P(A)| > |A| for any set A. Applied to the natural numbers ℕ, what does this imply?"
  type: multiple-choice
  options:
    - "P(ℕ) is countably infinite — larger than ℕ but still in correspondence with it via a clever enumeration"
    - "P(ℕ) is uncountable — its cardinality strictly exceeds that of ℕ, and no bijection between them can exist"
    - "P(ℕ) has the same cardinality as ℕ because both are infinite sets"
    - "P(ℕ) is a proper class, not a set, and cardinality does not apply to it"
  answer: 1
  explanation: "Cantor's theorem guarantees no surjection ℕ → P(ℕ) exists, and hence no bijection — so |P(ℕ)| > |ℕ| = ℵ₀. P(ℕ) is strictly larger than ℕ and is in fact uncountable, having cardinality 2^ℵ₀ = |ℝ|. The common misconception is that 'all infinite sets are the same size' — this was the revolutionary content of Cantor's work, showing that infinities come in different sizes. The result for ℕ is a special case of the theorem, which applies to every set."

- question: "In the proof of Cantor's theorem, the diagonal set D = {x ∈ A : x ∉ f(x)} is constructed. Why does this set produce a contradiction when we assume f: A → P(A) is a surjection?"
  type: multiple-choice
  options:
    - "Because D is the empty set, and surjections cannot map any element to the empty set"
    - "Because D has larger cardinality than P(A), which is impossible"
    - "Because D is a well-defined subset of A (so D ∈ P(A)), but asking whether the element d with f(d) = D belongs to D leads to a logical contradiction in either case"
    - "Because the axiom of choice fails for infinite sets, making the construction of D impossible"
  answer: 2
  explanation: "D is a perfectly well-defined subset of A — no choice axiom or cardinality argument is needed. If f is a surjection, then D = f(d) for some d. Now: if d ∈ D, then by D's definition, d ∉ f(d) = D — contradiction. If d ∉ D, then d ∉ f(d), so by D's definition, d ∈ D — contradiction. Both cases are impossible, so the assumption that f is a surjection must be false. The elegance is that D's definition is self-referential in exactly the way needed to escape any proposed surjection."

- question: "Cantor's theorem applies only to infinite sets — for finite sets, it is possible for A and P(A) to have the same cardinality."
  type: true-false
  answer: false
  explanation: "Cantor's theorem applies to ALL sets without exception, including finite and empty ones. For the empty set: |P(∅)| = |{∅}| = 1 > 0 = |∅|. For a singleton: |P({a})| = |{∅, {a}}| = 2 > 1 = |{a}|. For any finite set of size n, |P(A)| = 2^n > n. The proof by diagonal argument works for finite sets too — there is simply no surjection A → P(A) for any set, finite or infinite. This is one of the misconceptions explicitly flagged in the topic."

- question: "Cantor's theorem implies there is no largest cardinal number — for any infinite cardinal κ, there exists a strictly larger cardinal 2^κ."
  type: true-false
  answer: true
  explanation: "Cantor's theorem gives |P(A)| > |A| for every set A. Applied to any infinite cardinal κ (the cardinality of some set A), the power set P(A) has cardinality 2^κ > κ. This generates an unbounded tower: ℵ₀ < 2^ℵ₀ < 2^(2^ℵ₀) < ···. Since every step strictly increases cardinality and there is no ceiling, there is no largest cardinal. The collection of all cardinals is a proper class — it cannot itself be a set, because that would require a set larger than any cardinal, contradicting Cantor's theorem applied to that set."

- question: "Explain in your own words why the diagonal set D in Cantor's proof always escapes any proposed surjection f: A → P(A), no matter how cleverly f is constructed."
  type: short-answer
  answer: "D is built by adversarially exploiting the structure of f itself: for each element x in A, D includes x if and only if x is NOT in the subset f(x). This means D disagrees with f(x) about whether x belongs — for every single x in A. If f(d) = D for some d, then asking 'is d in D?' generates a direct contradiction: D includes d iff d is not in f(d) = D. No matter how f is chosen, D is specifically constructed to differ from every set in f's range. It's a moving target that is always exactly one step ahead of f: f tries to hit D, but D is defined to dodge by checking whether f(d) contains d and doing the opposite. The diagonal argument is a formalization of self-referential evasion."
  explanation: "This is the deep structure of diagonal arguments, which reappear across mathematics and logic: in the proof that the reals are uncountable (Cantor's diagonal), in Russell's paradox (the set of all sets that don't contain themselves), in Gödel's incompleteness proof (the statement that says 'I am not provable'), and in the undecidability of the halting problem. Recognizing this structure is one of the most transferable insights in foundational mathematics."
```

## Explainer

You have studied cardinality and countability, and you know that two sets have the same cardinality when there is a bijection between them. Cantor's theorem is the most powerful result in this territory: for any set A whatsoever, the **power set** P(A) — the set of all subsets of A — is strictly larger than A. There is an injection A → P(A) (send each element x to its singleton {x}), but no surjection. Since cardinality comparison requires a bijection, and no bijection can exist when there's no surjection, we get |A| < |P(A)|.

The proof is the diagonal argument you studied for Cantor's diagonalization. Suppose for contradiction that f: A → P(A) is a surjection. Then every subset of A is in the range of f. Construct the set D = {x ∈ A : x ∉ f(x)} — the set of all elements of A that are *not* members of the subset assigned to them by f. D is a perfectly well-defined subset of A. Since f is a surjection, D = f(d) for some d ∈ A. Now ask: is d ∈ D? If d ∈ D, then by the definition of D, d ∉ f(d) = D — contradiction. If d ∉ D, then d ∉ f(d), so by the definition of D, d ∈ D — contradiction. Either way, we reach an impossibility. Therefore no surjection f: A → P(A) can exist.

The consequences are sweeping. Applied to A = ℕ, the theorem gives |P(ℕ)| > |ℕ|: the power set of the natural numbers is uncountable. (In fact, P(ℕ) has the same cardinality as the reals ℝ, both equal to 2^ℵ₀.) Applied to any infinite cardinal κ, it gives 2^κ > κ: the power of the power set always exceeds the original. This generates an unbounded tower of infinities: ℵ₀ < 2^ℵ₀ < 2^(2^ℵ₀) < ···, none of which can be the largest cardinal, since we can always take another power set. The cardinals form a proper class — there is no set containing all of them.

This connects directly to the **continuum hypothesis** question that builds from this theorem: is there a cardinal strictly between ℵ₀ and 2^ℵ₀? Cantor's theorem tells you 2^ℵ₀ > ℵ₀, but does not tell you how much bigger it is. That question turns out to be independent of ZFC — neither provable nor disprovable — a fact that took nearly a century after Cantor's proof to establish. The diagonal argument itself becomes a versatile proof technique: the same structure appears in the proof that the reals are uncountable, in Russell's paradox, in Gödel's incompleteness proof, and in the proof that the halting problem is undecidable. Learning to recognize the diagonal structure across these contexts is one of the deepest payoffs of studying Cantor's theorem.
