---
id: church-turing-thesis
title: The Church-Turing Thesis
domain: computer-science
course: theory-of-computation
prerequisites:
- id: turing-machine-variants
  type: hard
builds-toward:
- decidability
- halting-problem
tags:
- Church-Turing
- computability
- algorithm
- thesis
stage: advanced
status: draft
---

# The Church-Turing Thesis

## Core Idea
The Church-Turing thesis is the informal claim that every effectively computable function — everything that any physical computer, algorithm, or reasonable computational model can compute — is computable by a Turing machine. It is not a theorem (it cannot be formally proved) but a philosophical thesis supported by decades of evidence: every proposed computational model has turned out equivalent to TMs. The thesis licenses defining 'algorithm' as 'Turing machine', which allows formal proofs about the limits of computation.

## Common Misconceptions
- Treating the Church-Turing thesis as a proven theorem — it is a widely accepted but informal claim.
- Confusing the thesis with claims about efficiency — TMs can compute everything algorithms can, but not necessarily at the same speed.
- Thinking quantum computers refute the thesis — they may compute faster but are believed to compute the same set of functions.
