---
id: space-hierarchy-theorem-computability-and-complexity
title: Space Hierarchy Theorem
domain: formal-sciences-and-logic
course: computability-and-complexity
prerequisites:
- id: space-complexity-classes-formal
  type: hard
- id: time-hierarchy-theorem
  type: soft
tags:
- separations
- space-complexity
- resource-bounded
stage: advanced
status: draft
---

# Space Hierarchy Theorem

## Core Idea
The space hierarchy theorem states that for space-constructible functions f and g with f = o(g), we have DSPACE(f) ⊊ DSPACE(g). Unlike the time hierarchy, the theorem is unconditional and requires no logarithmic factor. This implies strict hierarchy among space classes: L ⊂ PSPACE ⊂ EXPSPACE, guaranteeing more languages become decidable with more space.

## Explainer

You've studied space complexity classes and the intuition that more resources enable more computation. The **space hierarchy theorem** makes this precise: if g(n) grows strictly faster than f(n) — formally, f = o(g), meaning f/g → 0 — then DSPACE(g) strictly contains DSPACE(f). There are languages that can be decided with g(n) space but provably cannot be decided with only f(n) space, no matter how clever the algorithm. More space means strictly more power, and no optimization can eliminate the gap.

The proof uses **diagonalization**, the same technique at the heart of the undecidability of the halting problem. You construct a language L that "diagonalizes" against all machines using only f(n) space. The diagonalizer M works as follows: on input ⟨e, x⟩, it simulates the e-th Turing machine on input x while carefully tracking its space usage, staying within g(n) space. At the end, M flips the answer. By construction, M disagrees with every f(n)-space machine on at least one input (the input that encodes the machine itself). So L — the language accepted by M — is not in DSPACE(f). But M itself uses g(n) space, so L ∈ DSPACE(g). This is the diagonal witness.

A key advantage of the space hierarchy over the **time hierarchy theorem** is that it requires no logarithmic slack. The time hierarchy needs g = Ω(f log f) because simulating a machine on a universal TM incurs a logarithmic overhead in time. Space simulation is more efficient: you can reuse space, so the constant-factor overhead in space is absorbed without a log penalty. This means the space hierarchy gives cleaner, tighter separations: DSPACE(n) ⊊ DSPACE(n²) follows immediately, without any caveat.

The practical consequence is that the classes you've already studied form a *strict* hierarchy. The inclusions L ⊊ PSPACE ⊊ EXPSPACE are not conjectured — they are theorems. Each class strictly contains the previous. This stands in sharp contrast to the situation between P and NP, or even P and PSPACE, where strict containment is expected but unproven. The space hierarchy theorem is one of the few clean, **unconditional separations** in complexity theory: a result that requires no unproven assumptions, no circuit lower bounds, no algebraic tools — just the diagonalization argument applied carefully.
