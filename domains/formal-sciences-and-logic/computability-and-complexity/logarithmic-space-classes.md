---
id: logarithmic-space-classes
title: Logarithmic Space Classes (L and NL)
domain: formal-sciences-and-logic
course: computability-and-complexity
prerequisites:
- id: space-complexity-classes-formal
  type: hard
builds-toward:
- nl-completeness
tags:
- space-complexity
- resource-bounded
- turing-machines
stage: advanced
status: draft
---

# Logarithmic Space Classes (L and NL)

## Core Idea
L (deterministic log space) and NL (nondeterministic log space) are fundamental space-bounded complexity classes capturing problems solvable with logarithmic auxiliary space. While it is unknown whether L = NL, Savitch's theorem shows NL ⊆ P, placing space-bounded computation between log space and polynomial time. These classes model algorithm design where space is severely constrained relative to input size.

## How It's Best Learned
Consider what computation is possible with log-space: you can store a few pointers and counters but not the entire input. Understand Savitch's theorem by simulating nondeterministic choices via DFS with limited space.

## Explainer

From space complexity, you know that PSPACE allows polynomial workspace and captures problems much harder than polynomial time. Logarithmic space goes to the other extreme: if the input is n characters long, an L or NL machine may use only O(log n) bits of auxiliary workspace. On a 1000-character input, that means roughly 10 bits — enough for a handful of counters or indices, but nowhere near enough to copy the input. The **two-tape model** is standard: one read-only input tape (not counted in space) and one read-write work tape bounded at O(log n) cells. This enforces a genuinely extreme resource constraint.

The canonical example of an L problem is determining whether a path of a certain length exists between two nodes in a directed graph. The canonical NL problem is **graph reachability** (ST-REACHABILITY): given a directed graph and two nodes s and t, is there any directed path from s to t? An NL machine solves it by guessing the path one node at a time, storing only the current node (an index fits in log n bits) and a step counter. You never need to store the whole path. The key insight is that NL captures problems where you can verify a "witness" of polynomial length by checking it one piece at a time with log-space bookkeeping.

**Savitch's theorem** is the central structural result: NL ⊆ SPACE(log² n), and therefore NL ⊆ P. The proof is elegant: simulate nondeterminism via depth-first reachability. To check if t is reachable from s in k steps, recursively check whether there is a midpoint m reachable from s in k/2 steps and from which t is reachable in k/2 steps. This recursion halves the path length at each level, using log n recursive calls each needing log n space — O(log² n) total. Notice you do not need to enumerate all nondeterministic branches simultaneously; you recompute each sub-check deterministically. This is why space is more "powerful" than time in this regime: space can be reused across branches in a way time cannot.

Whether L = NL is one of the central open questions in complexity theory, related to but separate from P vs NP. We know L ⊆ NL ⊆ P ⊆ PSPACE and that at least one of these inclusions is strict (the whole chain cannot collapse without collapsing P = PSPACE). The class NL is known to equal co-NL — a nondeterministic computation for "t is NOT reachable from s" — by Immerman–Szelepcsényi, which shows NL is more symmetric than RE (where RE ≠ co-RE). Logarithmic space thus represents a regime where both nondeterminism and complement behave better than their time-complexity analogues, making it a rich testing ground for understanding the structure of computation itself.

