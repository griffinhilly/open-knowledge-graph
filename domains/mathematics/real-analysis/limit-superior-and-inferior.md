---
id: limit-superior-and-inferior
title: Limit Superior and Inferior
domain: mathematics
course: real-analysis
prerequisites:
- id: epsilon-n-convergence
  type: hard
- id: subsequences
  type: hard
builds-toward:
- uniform-convergence-functions
tags:
- limsup
- liminf
- convergence
- oscillation
stage: advanced
status: draft
---

# Limit Superior and Inferior

## Core Idea
The limit superior (limsup) and limit inferior (liminf) of a sequence are the largest and smallest limit points of its subsequences, respectively. For any bounded sequence, liminf ≤ limsup, and equality holds if and only if the sequence converges. These tools allow precise analysis of oscillating sequences without traditional limits.

## Explainer

From your work on ε-N convergence and subsequences, you know that a sequence (aₙ) converges to L if and only if every subsequence also converges to L. But what tools do you have when a sequence does not converge — when it oscillates or accumulates near multiple values? The **limit superior** and **limit inferior** are precisely the tools built for this situation.

The formal definition: lim sup aₙ = lim_{n→∞} sup_{k≥n} aₖ. In words, look at the "tail" of the sequence starting at index n, take the supremum of that tail, then let n grow. Each tail is a subset of the previous one, so the suprema form a non-increasing sequence — it always has a limit (possibly +∞ or −∞). This limit is the limsup. Symmetrically, lim inf aₙ = lim_{n→∞} inf_{k≥n} aₙ, and the infima form a non-decreasing sequence. The limsup captures the largest value the sequence "approaches arbitrarily closely, infinitely often"; the liminf captures the smallest such value.

The canonical example is aₙ = (−1)ⁿ. The sequence alternates between +1 and −1, never converging. Yet lim sup aₙ = 1: the tail sup is always 1 (since +1 appears in every tail), and lim inf aₙ = −1 (since −1 also appears in every tail). These are the two accumulation points of the sequence, and the limsup and liminf identify them exactly. Now recall your subsequence work: a value L is a limit point of (aₙ) if some subsequence converges to L. The limsup is the largest such L, and the liminf is the smallest. This is why the Core Idea's characterization holds: limsup = liminf if and only if every subsequence has the same limit, which is exactly convergence.

The power of these tools becomes clear in applications. The limsup appears naturally in the **ratio test** and **root test** for series convergence: you replace lim|aₙ₊₁/aₙ| with lim sup|aₙ₊₁/aₙ| to handle sequences where the ratio doesn't converge but is still bounded. In the theory of **uniform convergence** (which you'll encounter next), you'll use lim sup across a domain to define the sup-norm, the right measure of how close two functions are. Any time a classical limit fails to exist but you still need to make a quantitative statement about limiting behavior, lim sup and lim inf give you the language to do it. They are not a workaround for convergence — they are a strictly more general notion that reduces to the ordinary limit as a special case.
