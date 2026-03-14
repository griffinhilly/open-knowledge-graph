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
