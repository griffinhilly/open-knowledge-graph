---
id: set-theoretic-cardinality
title: Set-Theoretic Cardinality
domain: formal-sciences-and-logic
course: set-theory
prerequisites:
- id: infinite-cardinal-numbers
  type: hard
- id: cantor-theorem
  type: hard
builds-toward:
- aleph-numbers
- descriptive-set-theory-intro
tags:
- cardinality
- countability
- bijection
- Hilbert's hotel
- diagonalization
- uncountability
- equinumerosity
stage: formal-systems
status: validated
---

# Set-Theoretic Cardinality

## Core Idea
Two sets A and B have the same cardinality (|A| = |B|) if and only if there exists a bijection between them — a function that is both injective and surjective. A set is countably infinite if it has the same cardinality as the natural numbers ℕ, and countable if it is either finite or countably infinite. Hilbert's hotel illustrates the surprising properties of countable infinity: the integers, rationals, and even ℕ × ℕ are all countable despite appearing 'larger' than ℕ. Cantor's diagonal argument then shatters the intuition that all infinite sets are the same size by proving that the reals (equivalently, P(ℕ)) are uncountable. Within ZFC, the Cantor-Bernstein-Schroeder theorem provides a powerful tool: if |A| ≤ |B| and |B| ≤ |A| (injections in both directions), then |A| = |B|.

## How It's Best Learned
Construct explicit bijections: ℕ → ℤ (dovetail positive and negative), ℕ → ℚ (Cantor's zigzag through a grid), ℕ → ℕ × ℕ (pairing function). Then work through the diagonal argument to prove [0,1] is uncountable. The contrast — building bijections for 'large-looking' countable sets, then failing for the reals — drives home what cardinality really measures. Finally, prove the Cantor-Bernstein theorem to see that cardinality comparison is well-behaved.

## Common Misconceptions
- 'Countable' does not mean 'listable in order' — the rationals are countable but cannot be listed in their natural order (which is dense, not well-ordered).
- The existence of a surjection from A onto B does not mean |A| = |B|; equality requires a bijection (or injections in both directions, by the Cantor-Bernstein theorem).

## Questions

```yaml
- question: "A student argues that the set of integers ℤ must have strictly greater cardinality than the natural numbers ℕ, because ℤ contains all of ℕ plus all the negative integers. What is wrong with this reasoning?"
  type: multiple-choice
  options:
    - "ℤ is actually a finite set, so the argument about size doesn't apply"
    - "The student is correct — ℤ has strictly greater cardinality than ℕ"
    - "A bijection can be constructed between ℕ and ℤ, so they have the same cardinality despite ℤ appearing larger"
    - "Cardinality comparisons are only meaningful for finite sets — infinite sets cannot be compared"
  answer: 2
  explanation: "The student's intuition that 'more elements → larger cardinality' works for finite sets but fails for infinite ones. Cardinality is defined by bijection existence, not by subset relations. The function f(n) = n/2 for even n and -(n+1)/2 for odd n maps ℕ → ℤ bijectively: 0↔0, 1↔−1, 2↔1, 3↔−2, ... Every integer appears exactly once. Because a bijection exists, |ℕ| = |ℤ| — they are both countably infinite, even though ℕ ⊂ ℤ. This is the signature property of infinite sets: they can be put in bijection with proper subsets of themselves."

- question: "Which of the following sets is uncountable — having strictly greater cardinality than the natural numbers?"
  type: multiple-choice
  options:
    - "The set of all integers ℤ"
    - "The set of all rational numbers ℚ"
    - "The set of all real numbers ℝ"
    - "The set of all pairs of natural numbers ℕ × ℕ"
  answer: 2
  explanation: "ℤ, ℚ, and ℕ × ℕ are all countably infinite — explicit bijections to ℕ can be constructed for each (sign-interleave for ℤ, Cantor's zigzag for ℕ × ℕ and then ℚ). The real numbers ℝ are provably uncountable: Cantor's diagonal argument shows that any attempted listing of real numbers in [0,1] is incomplete — a real number can always be constructed that differs from the nth listed number in the nth decimal place. |ℝ| > |ℕ|, representing a genuinely larger infinite cardinality."

- question: "Two infinite sets can have the same cardinality even when one appears to contain 'more elements' — cardinality equality is determined by bijection existence, not by subset relations or apparent density."
  type: true-false
  answer: true
  explanation: "True. This is the counterintuitive core of set-theoretic cardinality. ℕ ⊂ ℤ ⊂ ℚ, and the rationals are dense (between any two rationals lies another), yet |ℕ| = |ℤ| = |ℚ|. All three are countably infinite. The bijection criterion replaces intuitive 'size' with a precise matching condition. For infinite sets, being a proper subset is consistent with having equal cardinality — a fact that troubled mathematicians when Cantor first proposed it."

- question: "Because the rational numbers are dense — between any two rationals there is always another rational — the set of rational numbers must be uncountable, having strictly greater cardinality than the natural numbers."
  type: true-false
  answer: false
  explanation: "False. Density and cardinality are independent properties. The rational numbers are dense in ℝ (no gaps between rationals) but are countably infinite — the same cardinality as ℕ. Cantor's zigzag argument constructs an explicit enumeration of all positive rationals by traversing the grid ℕ × ℕ diagonally, then extending to all rationals. Density tells you about the order structure (no isolated points, no gaps in the ordering); cardinality tells you about the size of the set in the bijection sense. These two notions are logically independent."

- question: "What does it mean for two sets to have the same cardinality, and why does the Cantor-Bernstein-Schroeder theorem make establishing cardinality equality practically useful?"
  type: short-answer
  answer: "Two sets A and B have the same cardinality (|A| = |B|) if and only if there exists a bijection between them — a function that is both injective (one-to-one) and surjective (onto). The Cantor-Bernstein-Schroeder theorem makes this practical by allowing a two-step shortcut: rather than constructing an explicit bijection (which can be technically difficult), you can establish |A| = |B| by finding any injection from A into B and any separate injection from B into A. The theorem guarantees these two injections can be combined into a bijection, even without constructing it explicitly. This is analogous to the squeeze theorem: bounding |A| ≤ |B| ≤ |A| pins down equality."
  explanation: "Explicit bijections between infinite sets are often hard to construct directly. For example, proving |(0,1)| = |ℝ| is straightforward via CBS: embed (0,1) into ℝ via inclusion, and embed ℝ into (0,1) via arctan rescaled. Without CBS, you would need to write down an explicit bijection from all of ℝ to the open interval — a more demanding construction. The theorem's non-constructive nature (it proves the bijection exists without exhibiting it) is a powerful feature of modern set theory."
```

## Explainer

Cardinality is the rigorous answer to the question "how many elements does a set have?" For finite sets the answer seems obvious — count them. But counting is really just constructing a bijection to {1, 2, ..., n}. **Cardinality** generalizes this idea: two sets have the same cardinality if and only if there exists a **bijection** (a one-to-one correspondence) between them. This definition sidesteps the question "how many?" entirely and replaces it with the question "can they be paired up perfectly?"

The power of the definition becomes clear when you apply it to infinite sets. From your work with infinite cardinal numbers, you know that "infinity" is not a single thing. But the bijection criterion lets you compare infinite sets precisely. The integers ℤ seem much larger than the naturals ℕ — after all, ℤ includes all negative numbers too. Yet the function f(n) = (n/2 for even n, -(n+1)/2 for odd n) constructs a perfect pairing: 0↔0, 1↔−1, 2↔1, 3↔−2, ... This is **Hilbert's Hotel** made formal: a hotel with infinitely many rooms can always accommodate new guests by shifting everyone down. The takeaway is that countably infinite sets can absorb new elements or even finitely many copies of themselves without changing cardinality. The rationals are countable too — Cantor's zigzag argument through the grid ℕ × ℕ lists every positive fraction exactly once, showing |ℚ| = |ℕ|.

Then comes Cantor's diagonal argument, which you already know through Cantor's theorem. Applied to the real numbers, it shows that no matter how you try to list all real numbers in [0,1] — even infinitely — you can always construct a real number not on the list by differing from the nth entry in the nth decimal place. This proves the reals are **uncountable**: |ℝ| > |ℕ|. The rationals and reals both look like "lots of numbers," but they belong to fundamentally different size classes. There are multiple infinite cardinalities, forming a strict hierarchy.

The **Cantor-Bernstein-Schroeder theorem** is the tool that makes cardinality comparison practical. Rather than constructing an explicit bijection — which can be fiendishly difficult — you can establish |A| = |B| by finding an injection from A into B and a separate injection from B into A. The theorem guarantees these two one-way matchings can be woven into a two-way bijection, even though the proof is non-constructive. Think of it as the cardinality analogue of the squeeze theorem: bounding |A| ≤ |B| ≤ |A| pins down equality. This technique is indispensable for proving, for example, that |(0,1)| = |ℝ| by embedding each into the other.
