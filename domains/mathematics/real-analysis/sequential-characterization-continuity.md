---
id: sequential-characterization-continuity
title: Sequential Characterization of Continuity
domain: mathematics
course: real-analysis
prerequisites:
- id: epsilon-delta-continuity
  type: hard
- id: epsilon-n-convergence
  type: hard
builds-toward:
- uniform-continuity
- extreme-value-theorem-rigorous
tags:
- continuity
- sequences
- limits
stage: advanced
status: draft
---

# Sequential Characterization of Continuity

## Core Idea
A function f is continuous at c if and only if for every sequence (xₙ) converging to c, the sequence (f(xₙ)) converges to f(c). This sequential characterization makes it easy to apply continuity proofs using sequence arguments rather than epsilon-delta arguments.

## Explainer

You now know two rigorous definitions of convergence: the epsilon-delta definition of continuity and the epsilon-N definition of sequence convergence. The **Sequential Characterization of Continuity** is the theorem that ties them together — it says these two languages are fully interchangeable for talking about continuity. A function f is continuous at c if and only if whenever xₙ → c (in the sequence sense), f(xₙ) → f(c) (also in the sequence sense). This is not a new definition of continuity but an equivalent reformulation, and its power lies in giving you a choice of which machinery to use.

To see why the equivalence holds, consider the forward direction: suppose f is continuous at c (epsilon-delta), and let xₙ → c. Given any ε > 0, the continuity of f at c supplies a δ > 0 such that |x − c| < δ implies |f(x) − f(c)| < ε. Since xₙ → c, there exists N such that for all n > N, |xₙ − c| < δ. Combining these: for all n > N, |f(xₙ) − f(c)| < ε. That is exactly f(xₙ) → f(c). The argument is a clean handoff between the two definitions, with δ playing the role of the tolerance that N must eventually satisfy.

The reverse direction — and the most practically useful direction — is a contrapositive argument. If f is **not** continuous at c, there exists some ε₀ > 0 such that for every δ > 0, you can find a point within δ of c where f moves more than ε₀ away from f(c). Taking δ = 1/n for each n, you produce a sequence xₙ with |xₙ − c| < 1/n but |f(xₙ) − f(c)| ≥ ε₀. This sequence satisfies xₙ → c but f(xₙ) ↛ f(c) — violating the sequential condition. Therefore: if f fails the sequential condition, f is discontinuous.

The practical payoff is that sequences are often easier to construct than epsilon-delta arguments. To **prove** continuity, you can work with sequences directly. To **disprove** continuity, you only need to exhibit a single sequence xₙ → c for which f(xₙ) fails to converge to f(c) — no epsilon-delta bookkeeping required. The classic example is f(x) = sin(1/x) near x = 0: take xₙ = 1/(2πn), so xₙ → 0 and f(xₙ) = 0; then take yₙ = 1/(π/2 + 2πn), so yₙ → 0 and f(yₙ) = 1. Two sequences converge to 0 but map to different limits — immediately, f is discontinuous at 0. The sequential characterization makes this clean.
