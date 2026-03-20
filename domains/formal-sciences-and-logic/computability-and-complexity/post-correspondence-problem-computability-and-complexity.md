---
id: post-correspondence-problem-computability-and-complexity
title: Post Correspondence Problem
domain: formal-sciences-and-logic
course: computability-and-complexity
prerequisites:
- id: halting-problem-formal
  type: hard
- id: computability-reductions
  type: soft
tags:
- computability
- undecidability
- formal-languages
stage: advanced
status: draft
---

# Post Correspondence Problem

## Core Idea
The Post Correspondence Problem (PCP) asks, given a finite set of domino-like pairs of strings (u_i, v_i), whether there exists a nonempty sequence of indices i_1, ..., i_k such that u_{i_1}...u_{i_k} = v_{i_1}...v_{i_k}. Despite its deceptively simple formulation, PCP is undecidable — there is no algorithm that can solve it for all instances. PCP is a workhorse for proving undecidability of other problems: many undecidability results in formal language theory (ambiguity of CFGs, equivalence of CFGs) are established by reduction from PCP rather than directly from the halting problem.

## How It's Best Learned
Work through small PCP instances by hand — some with solutions and some without — to develop intuition for the matching constraint. Then study the reduction from the halting problem to PCP, which encodes a TM computation as a growing sequence of domino matches. Finally, see how PCP is reduced to prove undecidability of CFG ambiguity.

## Common Misconceptions
- PCP is undecidable in general, but specific restricted variants (e.g., over a unary alphabet, or with only two pairs under certain constraints) may be decidable.
- The difficulty is not finding a short solution — it is that no algorithm can determine whether any solution exists at all, regardless of length.

## Explainer

From the halting problem, you know that some questions about computation have no algorithmic answer — no matter how clever your program, it cannot decide whether an arbitrary Turing machine halts on an arbitrary input. The Post Correspondence Problem is a second, structurally simpler-looking problem that is also undecidable, and its value lies precisely in that simplicity. Because PCP is undecidable and involves nothing more than matching strings, it makes an efficient stepping stone for proving other problems undecidable without always tracing a path back through Turing machine encodings.

The setup is this: you are given a finite collection of **dominoes**, each with a top string and a bottom string — for example, [ab/a], [b/ba], [a/bab]. Your task is to pick a nonempty sequence of these dominoes (with repetition allowed) such that reading all the top strings in order yields exactly the same string as reading all the bottom strings in order. For the example above, the sequence [ab/a], [b/ba], [ab/a], [b/ba] gives top = "ab" + "b" + "ab" + "b" = "abbabb" and bottom = "a" + "ba" + "a" + "ba" = "abaaba" — not a match. Finding a match requires trial and error, and the length of the solution sequence can be astronomically large even when a solution exists.

The undecidability proof shows that if you could solve PCP, you could solve the halting problem — a contradiction. The reduction works by encoding a Turing machine's computation history as a PCP instance. Each step of the TM's computation corresponds to a domino designed so that a valid matching sequence spells out a valid sequence of configuration snapshots: the full history from start to halt. The top strings spell out one phase of the computation and the bottom strings spell out the next, and a solution exists exactly when the machine halts. Because constructing this reduction is mechanical, a PCP solver would become a halting problem solver, which we know is impossible.

PCP's real utility is as a **reduction intermediate**. Many problems in formal language theory — does a context-free grammar generate an ambiguous language? Are two context-free grammars equivalent? — are proved undecidable by reducing PCP to them rather than going directly from the halting problem. The reductions are shorter because PCP has a cleaner combinatorial structure than Turing machine computations. You can think of PCP as a "laundered" form of undecidability: the messiness of TM encodings has been pushed into the PCP construction once, and all downstream reductions start from that clean domino-matching form.

The key intuition for why no algorithm can solve PCP is that the search space has no exploitable bound. If no solution exists among sequences of length up to k, a solution might still exist at length k+1. There is no certificate of non-existence to check, no structural property that rules out longer solutions, and no depth at which you can safely stop searching. This "no finite witness of failure" structure is characteristic of undecidable problems and is worth recognizing as a general pattern: deciding that something cannot happen, over an infinite search space, is the hard direction.

