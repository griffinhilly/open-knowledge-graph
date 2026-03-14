---
id: existence-proofs
title: Existence Proofs
domain: mathematics
course: methods-of-proof
prerequisites:
- id: direct-proof
  type: hard
- id: predicates-and-quantifiers
  type: hard
- id: proof-by-contradiction
  type: soft
- id: proof-by-cases
  type: soft
builds-toward:
- uniqueness-proofs
tags:
- existence
- constructive-proof
- non-constructive-proof
- existence-and-uniqueness
stage: formal-systems
status: validated
---
# Existence Proofs

## Core Idea
An existence proof establishes that ∃x P(x) is true — that at least one object satisfying a property exists. A constructive proof explicitly exhibits such an object. A non-constructive proof demonstrates existence without construction, often by contradiction (assuming no such object exists leads to a contradiction). The distinction matters philosophically and practically: constructive proofs provide algorithms, while non-constructive proofs only guarantee existence.

## How It's Best Learned
Compare constructive and non-constructive proofs of the same claim, such as the existence of irrational numbers or prime factorizations. Ask: 'Can we find an explicit example, or only argue that one must exist?' This distinction previews deep questions in logic and computability.

## Common Misconceptions
- Assuming all existence proofs must produce a concrete example — non-constructive proofs are fully valid.
- Proving ∃x P(x) by verifying P for one arbitrary x rather than finding a specific x that works.
- Confusing proving existence with proving uniqueness.
