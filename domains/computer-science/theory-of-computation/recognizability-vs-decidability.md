---
id: recognizability-vs-decidability
title: Recognizability vs. Decidability
domain: computer-science
course: theory-of-computation
prerequisites:
- id: halting-problem
  type: hard
builds-toward:
- undecidability-reductions
tags:
- RE
- co-RE
- recognizable
- decidable
- complement
stage: advanced
status: validated
---

# Recognizability vs. Decidability

## Core Idea
A language is decidable if and only if both it and its complement are Turing-recognizable. This gives a useful test: if a language is recognizable but its complement is not, it cannot be decidable. The class of Turing-recognizable languages (RE) and the class of co-RE languages (complements of RE) overlap exactly at the decidable languages. HALT_TM is in RE but not co-RE (its complement is not recognizable), confirming its undecidability. Understanding this landscape is essential for classifying computational problems.

## Common Misconceptions
- Thinking every recognizable language is decidable — recognizability is strictly weaker.
- Confusing the complement of a language with the complement of a complexity class — co-RE is not the same as 'not RE'.
