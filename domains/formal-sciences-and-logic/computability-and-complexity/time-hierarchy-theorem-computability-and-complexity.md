---
id: time-hierarchy-theorem-computability-and-complexity
title: Time Hierarchy Theorem
domain: formal-sciences-and-logic
course: computability-and-complexity
prerequisites:
- id: time-complexity-classes-formal
  type: hard
- id: turing-machines-formal
  type: hard
builds-toward:
- space-hierarchy-theorem
tags:
- separations
- resource-bounded
- computability
stage: advanced
status: draft
---

# Time Hierarchy Theorem

## Core Idea
The time hierarchy theorem states that for reasonable complexity measures, strictly greater time allows a Turing machine to decide strictly more languages. Formally, if f and g are time-constructible functions with f·log(f) = o(g), then DTIME(f) ⊊ DTIME(g). This unconditionally proves P ⊂ EXPTIME and guarantees unbounded growth of computational power with time resources.

## How It's Best Learned
Understand the proof using diagonalization: a TM with more time can solve the time-bounded halting problem for TMs with less time, constructing a language not in the smaller class.

## Explainer

From your study of **Turing machines** and **time complexity classes**, you know that DTIME(f(n)) is the set of languages decidable by a deterministic TM in O(f(n)) steps. A natural question follows immediately: does more time actually buy you more computational power? Could DTIME(n²) and DTIME(n³) be the same class — where the extra time is just wasted? The time hierarchy theorem answers definitively: no. More time strictly expands what can be decided.

The formal statement requires a technical condition: f and g must be **time-constructible** (a TM can compute f(n) in O(f(n)) steps, so the function is "usable" as a resource bound), and the gap between them must satisfy f(n)·log f(n) = o(g(n)). Under these conditions, DTIME(f) is a *strict subset* of DTIME(g) — there are languages in the larger class that provably cannot be decided in the smaller time bound. The log f factor is a minor technical artifact of simulating one TM on another; in practice the theorem says things like DTIME(n) ⊊ DTIME(n²) ⊊ DTIME(n³) ⊊ ··· and P ⊊ EXPTIME.

The proof uses **diagonalization** — the same technique Cantor used to prove uncountability, adapted by Turing to prove undecidability, and now applied to complexity. The idea: a TM D with time bound g(n) enumerates all TMs Mᵢ in order, simulates Mᵢ on input ⟨i⟩ for at most f(|i|)·log f(|i|) steps, and does the opposite of what Mᵢ does. D has enough time to run this simulation (because g grows faster than f·log f) and enough time to *not* be fooled by any time-f(n) machine. The language D decides — "all inputs ⟨i⟩ where Mᵢ doesn't accept within the time limit" — cannot be decided in time f(n), because D's own construction ensures it differs from every such machine on at least one input.

The theorem has immediate structural consequences. It guarantees the polynomial hierarchy is infinite *if* the classes are all distinct: P is strictly inside EXP, which is strictly inside doubly-exponential time, and so on without bound. More subtly, it shows that computational power grows continuously with time — there is no "plateau" where extra time stops helping. This is the unconditional separation in complexity theory, requiring no assumption about P vs. NP or any open conjecture.

One important contrast with NP: the time hierarchy theorem gives a separation between *deterministic* time classes. We know DTIME(n) ⊊ DTIME(n²) unconditionally. But the question of whether P ⊊ NP — a separation between deterministic and nondeterministic time — remains open. Diagonalization works cleanly when both sides of the comparison are deterministic; the nondeterministic case resists the same technique, which is part of why P vs. NP is so hard.
