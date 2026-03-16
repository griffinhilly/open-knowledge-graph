---
id: chain-complexes-exact-sequences
title: Chain Complexes and Exact Sequences
domain: formal-sciences-and-logic
course: category-theory
prerequisites:
- id: abelian-categories
  type: hard
- id: functors
  type: soft
- id: vector-spaces
  type: soft
- id: linear-transformations
  type: hard
- id: basis-and-dimension
  type: soft
- id: linear-transformations-definition
  type: soft
builds-toward:
- homology-and-cohomology
tags:
- chain complex
- boundary map
- exact sequence
- short exact sequence
- differential
- cochain complex
stage: advanced
status: draft
---
# Chain Complexes and Exact Sequences

## Core Idea
A chain complex in an abelian category A is a sequence of objects and morphisms ··· → C_{n+1} → C_n → C_{n-1} → ··· where the composition of any two consecutive morphisms (called boundary or differential maps, d_{n} ∘ d_{n+1} = 0) is zero. A sequence is exact at C_n if the image of d_{n+1} equals the kernel of d_n, meaning "what goes in as boundaries is exactly what would be killed." A short exact sequence 0 → A → B → C → 0 captures the idea that A embeds in B and C is the quotient B/A. Chain complexes and their morphisms form an abelian category Ch(A), enabling the systematic study of homological invariants.

## How It's Best Learned
Work with chain complexes of abelian groups. Construct the short exact sequence 0 → Z →(×2) Z → Z/2Z → 0 and verify exactness at each position. Then build a longer chain complex, compute where it fails to be exact, and observe that the failure is measured by homology groups. Understand the chain map between two complexes and verify it preserves the differential.

## Common Misconceptions
- A chain complex is not necessarily exact; exactness is a special property, and the deviation from exactness is precisely what homology measures.
- The condition d ∘ d = 0 does not mean d = 0; it means the image of one differential is contained in the kernel of the next.
- Short exact sequences do not always split; the splitting lemma gives conditions, but in general the middle term B is a non-trivial extension of C by A.

## Questions

```yaml
- question: "In a chain complex · · · → B →(d_n) C →(d_{n-1}) D → · · ·, the condition d_{n-1} ∘ d_n = 0 implies which relationship between the image of d_n and the kernel of d_{n-1}?"
  type: multiple-choice
  options:
    - "im(d_n) = ker(d_{n-1}), so the complex is exact at C"
    - "im(d_n) ⊆ ker(d_{n-1}), so every boundary is a cycle, but not every cycle need be a boundary"
    - "im(d_n) and ker(d_{n-1}) are disjoint"
    - "d_n = 0 or d_{n-1} = 0"
  answer: 1
  explanation: "d_{n-1} ∘ d_n = 0 means every element in the image of d_n is sent to zero by d_{n-1}, i.e., im(d_n) ⊆ ker(d_{n-1}). This is weaker than exactness: exactness at C would require equality im(d_n) = ker(d_{n-1}). The gap — elements in ker(d_{n-1}) that are not in im(d_n) — is exactly what the homology group H_n = ker(d_n) / im(d_{n+1}) measures."

- question: "If 0 → A →f B →g C → 0 is a short exact sequence of abelian groups, then B is necessarily isomorphic to A ⊕ C."
  type: true-false
  answer: false
  explanation: "Exactness forces f to be injective, g to be surjective, and im(f) = ker(g), so C ≅ B/A. But this does not mean the sequence splits. The sequence 0 → Z →(×2) Z → Z/2Z → 0 is exact, yet Z ≇ Z ⊕ Z/2Z — the integers cannot split into a copy of Z plus a finite group. Splitting requires an additional section (a right inverse of g or a retraction of f), which may not exist."

- question: "The homology group H_n of a chain complex is defined as ker(d_n)/im(d_{n+1}). What does H_n = 0 mean about the complex at position n?"
  type: short-answer
  answer: "H_n = 0 means ker(d_n) = im(d_{n+1}), i.e., the complex is exact at position n: every cycle (element killed by d_n) is a boundary (in the image of d_{n+1}), and there are no 'holes' at that position."
  explanation: "Homology measures the failure of exactness. When H_n = ker(d_n)/im(d_{n+1}) = 0, the quotient is trivial, meaning the two subgroups are equal. Exactness at every position means the entire complex is an exact sequence, and all homology groups vanish. Nontrivial H_n indicates topological or algebraic 'holes' that the complex detects."
```

## Explainer

A chain complex is a sequence of objects linked by maps — called boundary or differential maps — with one crucial constraint: the composition of any two consecutive maps is zero. Written as d ∘ d = 0, this says that whatever the first map sends into the middle object lies entirely in the kernel of the next map. If you think of the differentials as "boundary operators" in a geometric context, d ∘ d = 0 encodes the intuition that the boundary of a boundary is always empty. In the algebraic setting it simply means im(d_{n+1}) ⊆ ker(d_n) at every position.

Exactness is a stronger condition than d ∘ d = 0. A complex is exact at object C_n if im(d_{n+1}) = ker(d_n) — not just a subset, but equality. An exact sequence has no "holes": every element killed by the outgoing map was the image of something from the incoming map. Short exact sequences 0 → A → B → C → 0 are the building blocks of this theory. Exactness at A means the first map is injective (A embeds into B); exactness at C means the second map is surjective; exactness at B means the image of A in B is precisely the kernel of the map to C, so C ≅ B/A. These sequences encode extension problems: given A and C, how many non-isomorphic ways can B be built?

Homology is the tool for measuring how far a complex deviates from exactness. The n-th homology group is defined as H_n = ker(d_n)/im(d_{n+1}). Elements of ker(d_n) are called cycles; elements of im(d_{n+1}) are called boundaries. Since d ∘ d = 0 guarantees every boundary is a cycle, this quotient is well-defined. When H_n = 0 at every position, the complex is exact everywhere. When H_n ≠ 0, the non-trivial elements are cycles that are not boundaries — they detect "holes" that the differential cannot reach.

A subtle but important point is that short exact sequences do not automatically split. Splitting would mean B ≅ A ⊕ C, with the sequence decomposing into a direct sum. But the sequence 0 → Z →(×2) Z → Z/2Z → 0 is exact, and yet Z cannot be written as Z ⊕ Z/2Z — an infinite cyclic group cannot contain a nontrivial finite cyclic group as a direct summand. The splitting lemma characterizes exactly when splitting occurs (when a right-inverse or left-inverse exists), and failure to split is precisely what makes extension theory rich. Chain complexes and exact sequences are the language in which homological algebra, algebraic topology, and derived functors are all formulated, so mastering these definitions is the gateway to understanding how algebraic invariants detect geometric structure.
