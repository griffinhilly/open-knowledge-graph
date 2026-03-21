---
id: cardinal-comparison-and-schroeder-bernstein
title: 'Comparing Cardinalities: The Schröder-Bernstein Theorem'
domain: formal-sciences-and-logic
course: set-theory
prerequisites:
- id: injections-surjections-and-inverse-functions
  type: hard
- id: uncountable-sets-and-the-reals
  type: soft
builds-toward:
- aleph-and-beth-hierarchy-introduction
- cardinal-arithmetic
tags:
- comparison
- order
- bijection
stage: formal-systems
status: draft
---

# Comparing Cardinalities: The Schröder-Bernstein Theorem

## Core Idea
The Schröder-Bernstein theorem states: if there exist injections f: A → B and g: B → A, then there exists a bijection between A and B. This makes cardinality a total order: for any two sets A and B, either |A| < |B|, |A| = |B|, or |A| > |B|. It avoids needing explicit bijections.

## Questions

```yaml
- question: "To prove that the open interval (0,1) and the closed interval [0,1] have the same cardinality, which approach correctly applies the Schröder-Bernstein theorem?"
  type: multiple-choice
  options:
    - "Construct an explicit bijection between (0,1) and [0,1] directly"
    - "Show an injection from (0,1) into [0,1] and an injection from [0,1] into (0,1), then conclude a bijection exists"
    - "Show that both sets are uncountable, so they must have the same cardinality"
    - "Show that [0,1] differs from (0,1) by only two points, so the two sets are the same size"
  answer: 1
  explanation: "Schröder-Bernstein: two injections in opposite directions guarantee a bijection. The injection from (0,1) into [0,1] is trivial — the identity function works. The injection from [0,1] into (0,1) requires slightly more care: x ↦ (x+1)/3 maps [0,1] into (1/3, 2/3) ⊂ (0,1). Two easy injections found; the theorem delivers the bijection without requiring you to construct it. Option C is wrong: uncountability alone does not establish equal cardinality — ℝ and ℝ² are both uncountable but comparing them requires further argument."

- question: "What does the notation |A| ≤ |B| mean formally in the theory of cardinal comparison?"
  type: multiple-choice
  options:
    - "A has fewer elements than B in the usual numerical sense"
    - "There exists a surjection from B onto A"
    - "There exists an injection from A into B"
    - "A is a proper subset of B"
  answer: 2
  explanation: "In set theory, |A| ≤ |B| is defined as: there exists an injection (one-to-one function) from A into B. An injection maps every element of A to a distinct element of B — intuitively, A 'fits inside' B without collisions. Option B (surjection from B onto A) is a different relationship — it means every element of A has at least one preimage in B, which captures a kind of 'coverage' rather than 'fitting inside.' Option D (subset) is also distinct: you can have an injection without A being a subset."

- question: "The Schröder-Bernstein theorem states that if |A| ≤ |B| and |B| ≤ |A|, then |A| = |B|."
  type: true-false
  answer: true
  explanation: "This is the antisymmetry property that makes cardinality comparison well-behaved. It says: if A injects into B and B injects into A, then a bijection exists between them. The proof constructs the bijection explicitly through a partitioning argument — elements are classified by whether their 'ancestry chain' under the two injections terminates in A, terminates in B, or loops forever. The result is foundational: it means the cardinality ordering cannot produce contradictions where |A| ≤ |B| and |B| ≤ |A| but |A| ≠ |B|."

- question: "To prove that two infinite sets have the same cardinality, you must construct an explicit bijection between them."
  type: true-false
  answer: false
  explanation: "The Schröder-Bernstein theorem provides an alternative: prove two injections (one in each direction) and conclude a bijection must exist, even without constructing it. This is enormously useful because direct bijections between infinite sets can be difficult or unnatural to write down, while injections are often straightforward. For example, proving |(0,1)| = |[0,1]| directly requires a clever countable-sequence trick, but Schröder-Bernstein makes it follow immediately from two simple injections."

- question: "Why is the Schröder-Bernstein theorem so valuable for comparing cardinalities of infinite sets? What problem does it solve that direct bijection construction doesn't always handle well?"
  type: short-answer
  answer: "For infinite sets, constructing a bijection explicitly can be very difficult — the bijection may require a non-obvious trick or a case-by-case definition that is hard to verify. Schröder-Bernstein replaces one hard problem (find a bijection) with two easy problems (find an injection each way). Injections are often trivial: the identity works in one direction, and a simple scaling or shift works in the other. The theorem guarantees the bijection exists without requiring you to write it down, making cardinality proofs accessible for cases where the bijection would be complicated or counterintuitive."
  explanation: "The deeper significance is foundational: Schröder-Bernstein establishes that ≤ on cardinalities is antisymmetric, making cardinality comparison a partial order. Without it, you could potentially have |A| ≤ |B| and |B| ≤ |A| while |A| ≠ |B| — which would make the cardinality ordering incoherent. Schröder-Bernstein rules this out, confirming that 'same size' for infinite sets is a logically consistent notion. All of cardinal arithmetic and the aleph hierarchy rest on this foundation."
```

## Explainer

From your work on injections and bijections, you know that two sets have the same cardinality when there exists a bijection between them. But finding an explicit bijection can be surprisingly hard. The **Schröder-Bernstein theorem** (also called the Cantor-Schröder-Bernstein theorem) gives you a way around this: instead of one bijection, you provide two injections going in opposite directions, and the theorem guarantees a bijection must exist.

The theorem says: if f: A → B is an injection and g: B → A is an injection, then |A| = |B|. Intuitively, if A can fit inside B without collisions, and B can fit inside A without collisions, then they must be the same size. The proof constructs the bijection explicitly through a clever partitioning argument — elements are classified by whether their "ancestry chain" (repeatedly applying f and g backwards) terminates in A, terminates in B, or loops forever. This tri-partite structure lets you piece together a bijection from the two injections.

The theorem is most powerful when finding a direct bijection is difficult but finding two injections is easy. For example, proving |(0,1)| = |[0,1]| (the open and closed intervals have the same cardinality) directly is awkward because the endpoints of [0,1] have no obvious bijective image in (0,1). But injecting (0,1) → [0,1] is trivial (the identity works), and injecting [0,1] → (0,1) is easy (scale: x ↦ (x+1)/3 works). Two easy injections, and Schröder-Bernstein delivers the bijection.

This theorem establishes that **cardinal comparison** is a total order. We write |A| ≤ |B| if there exists an injection from A to B. Schröder-Bernstein shows this is antisymmetric: if |A| ≤ |B| and |B| ≤ |A|, then |A| = |B|. Combined with transitivity of injections, cardinality becomes a well-behaved ordering on sets. This is the foundation for comparing infinite cardinalities — the aleph hierarchy and cardinal arithmetic all build on this ordering, and Schröder-Bernstein is the essential tool that makes the ordering coherent.
