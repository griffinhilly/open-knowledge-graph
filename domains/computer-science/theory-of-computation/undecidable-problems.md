---
id: undecidable-problems
title: Undecidable Problems and the Halting Problem
domain: computer-science
course: theory-of-computation
prerequisites:
- id: recognizable-languages
  type: hard
builds-toward:
- reductions-and-undecidability
- rice-theorem
tags:
- undecidability
- halting-problem
- limits
stage: abstract-reasoning
status: draft
---

# Undecidable Problems and the Halting Problem

## Core Idea
The halting problem—determining whether a Turing machine halts on a given input—is undecidable. This is proved by contradiction: if a halting decider existed, a diagonalization argument would construct a machine that produces a contradiction. The halting problem represents a fundamental limit on computation.

## How It's Best Learned
Follow the diagonal construction proof carefully. Understand why the self-reference ('a machine that halts iff it loops') creates a logical contradiction. Work through small examples of the argument.
