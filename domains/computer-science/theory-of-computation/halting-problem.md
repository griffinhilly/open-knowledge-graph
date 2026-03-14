---
id: halting-problem
title: The Halting Problem
domain: computer-science
course: theory-of-computation
prerequisites:
- id: decidability
  type: hard
- id: cantor-diagonalization
  type: soft
- id: cardinality-and-countability
  type: soft
- id: church-turing-thesis
  type: soft
builds-toward:
- undecidability-reductions
- rice-theorem
- recognizability-vs-decidability
tags:
- halting-problem
- undecidability
- diagonalization
- HALT_TM
stage: advanced
status: validated
---
# The Halting Problem

## Core Idea
The halting problem asks: given a Turing machine M and input w, does M halt on w? Turing proved in 1936 that no TM can decide this — HALT_TM is undecidable. The proof uses diagonalization: assume a decider H exists, construct a machine D that does the opposite of what H predicts for D itself, yielding a contradiction. The halting problem is the canonical undecidable problem; hundreds of other undecidable problems are proved undecidable by reducing the halting problem to them.

## How It's Best Learned
Follow the diagonalization argument carefully, constructing the contradiction step-by-step. Then read Turing's original 1936 paper for historical context. Finally, practice the reduction technique by showing ε_TM (does M accept ε?) is undecidable via a reduction from HALT_TM.

## Common Misconceptions
- Thinking undecidability means the problem is hard to compute — it means no algorithm can solve it *at all*, not merely that it's slow.
- Confusing undecidability with unrecognizability — HALT_TM is recognizable (run M; if it halts, accept) but not decidable.
- Misunderstanding the diagonalization: the contradiction arises from a self-referential TM, not from a counting argument.
