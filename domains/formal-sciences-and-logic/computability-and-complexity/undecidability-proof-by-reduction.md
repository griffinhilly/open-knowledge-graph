---
id: undecidability-proof-by-reduction
title: Proving Undecidability via Reduction
domain: formal-sciences-and-logic
course: computability-and-complexity
prerequisites:
- id: halting-problem-formal
  type: hard
- id: reducibility-many-one-formal
  type: hard
builds-toward:
- rices-theorem-applications
- post-correspondence-problem
tags:
- undecidability
- proofs
- reduction
stage: advanced
status: draft
---

# Proving Undecidability via Reduction

## Core Idea
To show a language L is undecidable, reduce the halting problem (or another known undecidable language) to L: if HALT ≤_m L and HALT is undecidable, then L is undecidable. This technique avoids directly reasoning about diagonal arguments and makes undecidability results intuitive: L inherits the computational hardness of HALT.

## How It's Best Learned
Practice reductions from HALT to at least three non-trivial languages (e.g., emptiness of a Turing machine's language, equivalence of machines, totality of a function).

## Common Misconceptions
- Confusing the direction of reduction (reducing HALT to L proves L is hard, not the other way around).
- Assuming a reduction must preserve decidability; it preserves undecidability.

## Explainer

You know the halting problem is undecidable: no Turing machine can determine, for all pairs (M, w), whether machine M halts on input w. **Reduction-based undecidability proofs** turn this established fact into a general technique. To show a new language L is undecidable, demonstrate that being able to decide L would let you decide the halting problem. Since the halting problem is already known to be undecidable, L must be undecidable too.

The formal tool is **many-one reducibility**: HALT ≤ₘ L means there exists a computable, total function f such that (M, w) ∈ HALT ⟺ f(M, w) ∈ L. The function f transforms halting-problem instances into L-instances, and it does so completely and computably — you can always compute the transformation, even though you cannot solve either problem. The undecidability proof is by contrapositive: if you had a decider for L, composing it with f would yield a decider for HALT. Since no HALT-decider exists, no L-decider can exist either.

Getting the **direction of the reduction** right is the most common pitfall. The reduction goes *from* the known-hard problem *to* the problem you want to prove hard. "HALT ≤ₘ L" says "L is at least as hard as HALT." If you accidentally reduce in the wrong direction (L ≤ₘ HALT), you are only showing that HALT is at least as hard as L — which is uninformative since HALT was already known to be hard. The intuition: if you can transform any HALT instance into an L instance, then a hypothetical L-solver is strong enough to solve HALT.

A worked example cements the technique. Consider L_empty = {⟨M⟩ : L(M) = ∅}, the set of machine encodings whose language is empty. Given any pair (M, w), construct a new machine M' that, on any input x, first simulates M on w and then accepts. M' accepts at least one string if and only if M halts on w — so (M, w) ∈ HALT ⟺ ⟨M'⟩ ∉ L_empty. The map (M, w) ↦ ⟨M'⟩ is computable, making this a valid many-one reduction. Since HALT is undecidable, L_empty must be too. This pattern generalizes: any non-trivial property of Turing machine languages is undecidable, which is precisely Rice's theorem.
