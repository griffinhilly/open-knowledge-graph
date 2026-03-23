---
id: proof-by-cases-exhaustion
title: Proof by Cases
domain: mathematics
course: methods-of-proof
prerequisites:
- id: proof-structure-terminology
  type: hard
- id: set-operations-union-intersection-complement
  type: soft
builds-toward:
- mathematical-induction-intro
tags:
- proof
- cases
- exhaustion
stage: formal-systems
status: validated
---

# Proof by Cases

## Core Idea
A proof by cases partitions the domain into exhaustive, non-overlapping cases and proves the goal within each case. If the goal holds for every case, it holds overall. This technique is essential when direct proof requires considering different scenarios or when natural divisions in the domain suggest different proof strategies.

## Questions

```yaml
- question: "A student proves 'for all real numbers x, |x| ≥ 0' with two cases: Case 1 (x > 0) and Case 2 (x < 0). Is this a valid proof?"
  type: multiple-choice
  options:
    - "Yes — positive and negative numbers cover all real numbers"
    - "No — the case x = 0 is missing, leaving a gap in the proof"
    - "Yes — since the claim holds in both cases, it holds for all reals"
    - "No — absolute value proofs must use the definition directly, not cases"
  answer: 1
  explanation: "The case x = 0 is neither positive nor negative, and the two cases {x > 0} and {x < 0} do not cover it — their union is all nonzero reals, not all reals. The proof has a gap. For x = 0, we need to verify that |0| = 0 ≥ 0 separately. Exhaustiveness is the non-negotiable requirement: every element of the domain must fall into at least one case, and 0 falls into none of the student's cases."

- question: "What is the key structural requirement that makes a proof by cases logically valid?"
  type: multiple-choice
  options:
    - "Each case must use a different proof technique so the argument is varied"
    - "The cases must be non-overlapping and together cover every element of the domain"
    - "There must be exactly two cases representing a binary division of the domain"
    - "The cases must be ordered from simplest to most complex to aid readability"
  answer: 1
  explanation: "Exhaustiveness is the requirement that cannot be relaxed: the union of all cases must equal the entire domain. Every element must be covered by at least one case. Non-overlapping (disjointness) is convenient but not strictly required — an element in two overlapping cases is fine as long as no element falls through a gap. The key is coverage, not separation."

- question: "In a proof by cases, the cases are required to be non-overlapping — if any two cases share even one element, the proof is invalid."
  type: true-false
  answer: false
  explanation: "Overlap is permitted. An element that falls into two cases is simply proved twice, which is harmless. What is never permitted is an element that falls into zero cases — that element is uncovered, and the proof makes no claim about it. The formal requirement is that the union of all cases equals the domain. Disjointness (non-overlapping) is a common organizational choice but is not a logical necessity."

- question: "A proof by cases establishes a universal claim by verifying the claim separately within each region of an exhaustive partition of the domain."
  type: true-false
  answer: true
  explanation: "This captures the logic exactly. 'For all x in D, P(x)' is proved by: (1) partition D into cases C₁, C₂, ..., Cₙ with C₁ ∪ ... ∪ Cₙ = D; (2) prove P(x) holds for every x in each Cᵢ. Since every element of D is in at least one case, and P holds within every case, P holds for all elements of D. The partition is the bridge between local arguments and the universal claim."

- question: "Why is exhaustiveness the non-negotiable requirement in a proof by cases? What goes wrong logically if even one element of the domain falls through the cracks?"
  type: short-answer
  answer: "If an element x₀ falls into none of the cases, the proof says nothing about x₀. The universal claim 'for all x, P(x)' would remain unverified for x₀. The conclusion could be false at x₀ — and in fact this is often exactly where counterexamples hide. A proof with a missing case has a logical gap that cannot be patched by the quality of the argument within the other cases."
  explanation: "The entire force of a proof by cases depends on the claim 'every element is somewhere in my case structure.' Without exhaustiveness, the proof is not a proof but a collection of conditional arguments: 'IF x is in case 1, THEN P(x).' The universal quantifier requires unconditional coverage. This is why checking exhaustiveness is the first thing to verify when reviewing a cases-based proof."
```

## Explainer

You know the standard proof structure: state what you assume, state what you want to show, provide a valid sequence of steps. Proof by cases applies when a single chain of reasoning cannot handle every element of the domain at once — different parts of the domain require different arguments. The key idea is **partitioning**: you divide the domain into a finite collection of cases whose union covers the entire domain (exhaustive) and whose pairwise intersections are empty (non-overlapping). Prove the goal for each case, and the union of those proofs constitutes a proof for all elements.

The exhaustiveness requirement is non-negotiable. If you miss a case, your proof has a gap — there exist elements the argument does not cover, and the conclusion may fail there. From your prerequisite knowledge of set operations, exhaustiveness means the union of your cases equals the entire domain. Non-overlapping means the cases' pairwise intersections are empty, though in practice some overlap is allowed as long as every element is covered — what matters is that no element falls through the cracks.

A classic example illustrates the technique cleanly. **Claim**: For any integer n, n² + n is even. Proof by cases on the parity of n. *Case 1: n is even.* Then n = 2k for some integer k, so n² + n = 4k² + 2k = 2(2k² + k), which is even. *Case 2: n is odd.* Then n = 2k + 1 for some integer k, so n² + n = (2k+1)² + (2k+1) = 4k² + 4k + 1 + 2k + 1 = 4k² + 6k + 2 = 2(2k² + 3k + 1), which is even. Since every integer is either even or odd (exhaustive), and these cases are non-overlapping, the result holds for all integers.

The art of proof by cases is identifying the right partition. Natural partitions arise from sign (positive, zero, negative), parity (even, odd), ordering (x < y, x = y, x > y), or membership in a set. In more advanced proofs, the partition may arise from whether a certain condition holds (satisfies property P vs. does not satisfy P). Good cases are ones where the proof inside each case simplifies — if your cases don't make the internal argument easier, you have probably chosen the wrong partition. Practice recognizing the natural fault lines in a problem before writing the proof.
