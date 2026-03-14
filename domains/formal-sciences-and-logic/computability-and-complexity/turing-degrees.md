---
id: turing-degrees
title: Turing Degrees
domain: formal-sciences-and-logic
course: computability-and-complexity
prerequisites:
- id: computability-reductions
  type: hard
- id: halting-problem-formal
  type: hard
builds-toward:
- arithmetical-hierarchy
tags:
- computability
- degree-theory
- reducibility
stage: formal-systems
status: draft
---

# Turing Degrees

## Core Idea
Two sets have the same Turing degree if each is Turing-reducible to the other — they are equally hard to compute. The Turing degrees form a partially ordered structure under reducibility, with the computable sets at degree 0 (the bottom) and the halting problem at degree 0' (zero-jump). The jump operator maps each degree d to a strictly higher degree d', producing an ascending chain. Post's problem asked whether there exist degrees strictly between 0 and 0'; Friedberg and Muchnik independently answered yes using the priority method, revealing that the degree structure is far richer than a simple linear chain.

## How It's Best Learned
First internalize Turing reducibility as "A is computable given B as an oracle." Then study the jump operator and verify that 0 < 0' < 0'' forms a strict chain. Finally, learn the statement (not necessarily the full proof) of the Friedberg-Muchnik theorem to appreciate that incomparable degrees exist — the structure branches, not just climbs.

## Common Misconceptions
- The Turing degrees are NOT linearly ordered — there exist incomparable degrees where neither set is reducible to the other.
- Turing degree 0 contains infinitely many distinct sets (all computable sets), not just the empty set — a degree is an equivalence class, not a single set.
