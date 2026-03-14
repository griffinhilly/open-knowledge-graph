---
id: reductions-and-undecidability
title: Reductions and Proving Undecidability
domain: computer-science
course: theory-of-computation
prerequisites:
- id: undecidable-problems
  type: hard
builds-toward:
- rice-theorem
tags:
- reductions
- undecidability
- proof-technique
stage: abstract-reasoning
status: draft
---

# Reductions and Proving Undecidability

## Core Idea
A many-to-one reduction from language A to language B shows that if B is decidable, then A is decidable. Contrapositive: if A is undecidable, then B is undecidable. Reductions allow proving undecidability of new problems without reconstructing diagonalization proofs.
