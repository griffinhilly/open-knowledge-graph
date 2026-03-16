---
id: intermediate-value-theorem-rigorous
title: Intermediate Value Theorem (Rigorous)
domain: mathematics
course: real-analysis
prerequisites:
- id: epsilon-delta-continuity
  type: hard
- id: connected-sets
  type: hard
tags:
- intermediate-value
- connectedness
- continuity
stage: advanced
status: draft
---

# Intermediate Value Theorem (Rigorous)

## Core Idea
If f is continuous on an interval [a,b] and f(a) ≠ f(b), then for every value w between f(a) and f(b), there exists c ∈ (a,b) with f(c) = w. The rigorous proof uses connectedness: the continuous image of a connected set is connected, and connected subsets of ℝ are intervals.

## Explainer

The Intermediate Value Theorem captures a simple intuition: if a continuous function starts at one value and ends at another, it must pass through every value in between. A function that teleports over a value — jumping from below 0 to above 0 without ever equaling 0 — would have to be discontinuous. In your calculus courses you likely used this without a deep justification. The rigorous treatment, which you are now ready for, derives the theorem not by direct construction but by combining your two prerequisites: ε-δ continuity and the topological notion of connectedness.

The key insight is that **connectedness is preserved by continuous functions**. A subset S of a topological space is connected if it cannot be split into two disjoint, nonempty open subsets. Intervals on ℝ are connected — you cannot partition (0,1) into two nonempty disjoint open sets. Conversely, a set like (0,1) ∪ (2,3) is disconnected because those two pieces separate it. Now: if f: X → Y is continuous and X is connected, then the image f(X) must also be connected. The proof is by contradiction — suppose f(X) = A ∪ B with A, B disjoint and open in f(X); then f⁻¹(A) and f⁻¹(B) would be disjoint, nonempty, and open in X (by continuity), contradicting connectedness of X.

Applying this to the IVT: [a,b] is a closed interval, which is connected. So f([a,b]) is a connected subset of ℝ. But the **connected subsets of ℝ are exactly the intervals** (another theorem you can prove using the same separation argument). A connected subset of ℝ that contains f(a) and f(b) must contain everything between them — it is an interval straddling both values. Therefore every w between f(a) and f(b) lies in f([a,b]), meaning there exists c with f(c) = w. The IVT drops out as a corollary of the structure of ℝ and the definition of continuity.

This approach generalizes far beyond ℝ. The same proof — continuous image of connected = connected, connected subsets of ℝ are intervals — shows that the IVT holds for continuous functions from any connected space to ℝ. More importantly, the proof technique itself is a template: many theorems in analysis and topology have the form "property P is preserved by continuous maps," and the method of contradicting connectedness or compactness reappears constantly. Understanding the IVT rigorously is really an introduction to the style of proof that drives the entire subject.
