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

## Questions

```yaml
- question: "An NL machine solves graph reachability (ST-REACHABILITY) on an n-node graph by 'guessing' a path from s to t one node at a time. Why can this be done with only O(log n) workspace, even if the path visits O(n) nodes?"
  type: multiple-choice
  options:
    - "The NL machine compresses the path into a logarithmic representation using a hash function"
    - "Only the current node and a step counter need to be stored at any point — the full path is never written down, and both fit within O(log n) bits"
    - "An n-node graph always has a reachable path of at most log n steps, so the counter stays small"
    - "NL machines are allowed to use polynomial space to store the path but only report a log-space-sized answer"
  answer: 1
  explanation: "At each step, the machine guesses the next node on the path (one of n possibilities, requiring log n bits to name), verifies it has an edge from the current node, then overwrites 'current node' with the new node — discarding the previous one. A step counter (also log n bits) tracks that the total path length doesn't exceed n. At no point is the accumulated path stored; only the current position and count are kept. This demonstrates the key insight about NL: it captures problems where a witness of polynomial length can be verified one piece at a time with only log-space bookkeeping, rather than requiring the full witness to be in memory."

- question: "Savitch's theorem proves NL ⊆ SPACE(log² n). The proof converts a nondeterministic log-space computation to a deterministic one. What is the core resource trade-off that makes this work?"
  type: multiple-choice
  options:
    - "The deterministic simulation is faster than the nondeterministic one, freeing up the space that would have been used for the time overhead"
    - "The deterministic simulation uses more time but reuses workspace across recursive sub-problems, keeping total space to O(log² n) via divide-and-conquer reachability"
    - "The simulation converts space usage to randomness, reducing worst-case space from log² n to log n with high probability"
    - "The simulation encodes the nondeterministic branch choices in the work tape, using log n bits per level of branching"
  answer: 1
  explanation: "Savitch's proof works by asking: is t reachable from s in ≤ k steps? To answer this, guess a midpoint m and recursively check s→m in k/2 steps AND m→t in k/2 steps. This recursion has log n levels (halving k each time), and each level requires log n bits for the midpoint and counter. Total space: O(log² n). The key insight is that space can be reused: once the s→m sub-check is done, that workspace is cleared before checking m→t. Time cannot be reused the same way — if you've already spent time on a branch that failed, you can't get it back. This asymmetry explains why NL ⊆ SPACE(log² n) but we don't know NL ⊆ TIME(n^c) for small c."

- question: "An NL machine can solve the graph reachability problem on an n-node graph while storing only the current node index and a step counter, because both require only O(log n) bits."
  type: true-false
  answer: true
  explanation: "True. A graph with n nodes can be indexed with ⌈log₂ n⌉ bits — enough to name any node. A step counter bounded by n (since any simple path has at most n − 1 edges) also requires O(log n) bits. Together these constitute the entire working memory needed: store the current node, check that an edge exists to a guessed next node (readable from the input tape), update the counter, overwrite the current node. Total workspace: O(log n). This is the canonical demonstration of how nondeterministic log-space captures graph reachability — a problem central to algorithm design — by leveraging the ability to 'forget' the path history while guessing it forward."

- question: "Since NL ⊆ P by Savitch's theorem, every problem in NL can be efficiently solved in practice using the deterministic algorithm implied by the proof."
  type: true-false
  answer: false
  explanation: "False. Savitch's theorem shows NL ⊆ SPACE(log² n) ⊆ P (since SPACE(log² n) ⊆ P by the time-space tradeoff), but the resulting deterministic algorithm's time complexity may be polynomial with a large exponent or constant. 'Contained in P' means polynomial time exists in principle, not that the algorithm is efficient in practice. Moreover, the proof constructs a simulation that works in log² n space but may use time exponential in log n for each space-bounded step. Separately, complexity containment tells you the class boundary, not whether we have good algorithms for specific problems — NL problems like graph reachability happen to have very fast practical algorithms, but Savitch's theorem is not why."

- question: "What is the key insight behind Savitch's proof that NL ⊆ SPACE(log² n)? Specifically, why can the deterministic simulation avoid storing all nondeterministic branches simultaneously?"
  type: short-answer
  answer: "Savitch's proof uses a divide-and-conquer reachability approach: to check if t is reachable from s in k steps, enumerate all possible midpoints m and recursively verify s→m in k/2 steps and m→t in k/2 steps. The space saving comes from sequential reuse: the s→m sub-check occupies log n bits on the work tape, and once it finishes (success or failure), that space is completely freed before the m→t sub-check begins. The recursion has depth log n (since k is halved each level), and each level uses log n bits, giving O(log² n) total. This works because space, unlike time, is reusable across branches. A nondeterministic machine explores all branches in parallel; Savitch's simulation explores them sequentially, clearing and reusing workspace between branches at the cost of more time."
  explanation: "This contrast between space and time reuse is a fundamental insight in complexity theory. Time spent on a failed branch is genuinely lost; space occupied during a failed branch can be reclaimed and reassigned. This asymmetry partially explains why L ⊆ NL has a much tighter bound (at most quadratic space blowup for determinism vs. nondeterminism) than P ⊆ NP (where the deterministic simulation of polynomial-time nondeterminism might require exponential time). It also motivates why researchers study space complexity separately from time complexity — the two resources behave fundamentally differently."
```

## Explainer

From space complexity, you know that PSPACE allows polynomial workspace and captures problems much harder than polynomial time. Logarithmic space goes to the other extreme: if the input is n characters long, an L or NL machine may use only O(log n) bits of auxiliary workspace. On a 1000-character input, that means roughly 10 bits — enough for a handful of counters or indices, but nowhere near enough to copy the input. The **two-tape model** is standard: one read-only input tape (not counted in space) and one read-write work tape bounded at O(log n) cells. This enforces a genuinely extreme resource constraint.

The canonical example of an L problem is determining whether a path of a certain length exists between two nodes in a directed graph. The canonical NL problem is **graph reachability** (ST-REACHABILITY): given a directed graph and two nodes s and t, is there any directed path from s to t? An NL machine solves it by guessing the path one node at a time, storing only the current node (an index fits in log n bits) and a step counter. You never need to store the whole path. The key insight is that NL captures problems where you can verify a "witness" of polynomial length by checking it one piece at a time with log-space bookkeeping.

**Savitch's theorem** is the central structural result: NL ⊆ SPACE(log² n), and therefore NL ⊆ P. The proof is elegant: simulate nondeterminism via depth-first reachability. To check if t is reachable from s in k steps, recursively check whether there is a midpoint m reachable from s in k/2 steps and from which t is reachable in k/2 steps. This recursion halves the path length at each level, using log n recursive calls each needing log n space — O(log² n) total. Notice you do not need to enumerate all nondeterministic branches simultaneously; you recompute each sub-check deterministically. This is why space is more "powerful" than time in this regime: space can be reused across branches in a way time cannot.

Whether L = NL is one of the central open questions in complexity theory, related to but separate from P vs NP. We know L ⊆ NL ⊆ P ⊆ PSPACE and that at least one of these inclusions is strict (the whole chain cannot collapse without collapsing P = PSPACE). The class NL is known to equal co-NL — a nondeterministic computation for "t is NOT reachable from s" — by Immerman–Szelepcsényi, which shows NL is more symmetric than RE (where RE ≠ co-RE). Logarithmic space thus represents a regime where both nondeterminism and complement behave better than their time-complexity analogues, making it a rich testing ground for understanding the structure of computation itself.

