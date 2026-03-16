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

## Explainer

From your study of recognizable languages, you know that Turing machines can accept languages — saying "yes" for strings in the language, though possibly looping forever on strings outside it. A **decidable** problem is one where a Turing machine always halts with a correct yes or no answer. The halting problem asks the seemingly reasonable question: given a Turing machine M and an input w, does M halt on w? The shocking answer is that no algorithm can solve this problem in general.

The proof uses **diagonalization**, a technique of self-reference that forces a contradiction. Suppose a decider H exists that correctly answers "yes" or "no" for every (M, w) pair. Now construct a new machine D that takes a Turing machine description M as input and does the following: D runs H on the pair (M, M) — asking whether M halts when given its own description as input. If H says "yes, M halts on M," then D deliberately loops forever. If H says "no, M does not halt on M," then D halts. Now ask: what happens when D is run on its own description? If D halts on D, then by construction H said "no" — meaning D does not halt on D. Contradiction. If D does not halt on D, then H said "yes" — meaning D does halt on D. Contradiction again. Either way, H gave the wrong answer, so H cannot exist.

This result reveals a **fundamental limit** of computation, not a limitation of current technology or programming skill. No faster computer, cleverer algorithm, or future programming language can solve the halting problem. The argument works for any computational model equivalent to Turing machines, which by the Church-Turing thesis includes everything we consider "computable." The undecidability of the halting problem is not an engineering obstacle — it is a mathematical theorem about the structure of computation itself.

The halting problem is the first and most important undecidable problem, but it is far from the only one. Once you have one undecidable problem, you can prove others undecidable through **reductions** — showing that if you could solve the new problem, you could use it to solve the halting problem, which you know is impossible. This technique reveals that virtually every non-trivial semantic property of programs is undecidable: Does this program ever print "hello"? Does it compute the same function as that program? Is it free of infinite loops? Rice's theorem formalizes this, establishing that any non-trivial property of the language recognized by a Turing machine is undecidable. The halting problem is thus not an isolated curiosity but the gateway to a vast landscape of unsolvable problems.
