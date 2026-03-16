---
id: reducibility-many-one-formal
title: Many-One Reducibility in Computability
domain: formal-sciences-and-logic
course: computability-and-complexity
prerequisites:
- id: turing-machines-formal
  type: hard
- id: computability-reductions
  type: hard
builds-toward:
- undecidability-proof-by-reduction
- turing-degrees
tags:
- reductions
- decidability
- undecidability
stage: advanced
status: draft
---

# Many-One Reducibility in Computability

## Core Idea
A language A is many-one reducible to B (A ≤_m B) if there is a computable function f such that w ∈ A iff f(w) ∈ B. This formal notion of reduction allows us to transfer decidability properties: if A ≤_m B and B is decidable, then A is decidable. Many-one reducibility is the foundational tool for proving undecidability via reduction.

## Explainer

You know from Turing machines that a language is **decidable** if some Turing machine always halts and correctly accepts or rejects every input. Many-one reducibility gives you a way to compare languages by computational difficulty without solving them directly. The definition is precise: A ≤_m B via f means there is a total computable function f such that for *every* string w, the string w belongs to A if and only if f(w) belongs to B. The function f translates the membership question for A into a membership question for B.

The key transfer property is what makes reductions useful. **If A ≤_m B and B is decidable, then A is decidable.** The proof is a simple composition: to decide whether w ∈ A, compute f(w) (which halts since f is total computable), then run the decider for B on f(w). If B accepts, accept; if B rejects, reject. This works because f(w) ∈ B iff w ∈ A. Reading the contrapositive: **if A ≤_m B and A is undecidable, then B is undecidable**. This contrapositive is how you actually use reductions in practice — to prove B is undecidable, reduce a *known* undecidable language to B.

The canonical undecidable language is the **halting problem** H_TM = {⟨M,w⟩ : M halts on w}. To show that a new language L is undecidable, you construct a computable function f such that ⟨M,w⟩ ∈ H_TM iff f(⟨M,w⟩) ∈ L. The key technique is **simulating inside the description**: you construct a new Turing machine M' whose description encodes the behavior of M on w, then map ⟨M,w⟩ to ⟨M'⟩ or some related object. When you verify the reduction, you check both directions of the iff: if ⟨M,w⟩ ∈ H_TM (M does halt on w), show f(⟨M,w⟩) ∈ L; if ⟨M,w⟩ ∉ H_TM (M does not halt), show f(⟨M,w⟩) ∉ L.

A common stumbling block is building f correctly. The function f must be *total* and *computable* — it cannot run M on w itself (that might not halt). Instead, f just *describes* what the constructed machine would do: it outputs a description of M' without executing M. This distinction between describing a computation and running it is at the heart of diagonalization-style arguments. The constructed machine M' typically says something like "simulate M on w; if M halts, then do something." The description of M' is always finite and constructible from ⟨M,w⟩, even though M might run forever if we ever executed it. Once you internalize this "describe but don't run" pattern, many-one reductions become a systematic and powerful tool for mapping the frontier of undecidability.

