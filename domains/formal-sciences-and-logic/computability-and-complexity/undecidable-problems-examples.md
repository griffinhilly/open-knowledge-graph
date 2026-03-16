---
id: undecidable-problems-examples
title: 'Undecidable Problems: Beyond the Halting Problem'
domain: formal-sciences-and-logic
course: computability-and-complexity
prerequisites:
- id: halting-problem-formal
  type: hard
- id: rices-theorem
  type: soft
builds-toward:
- many-one-reductions
- turing-degrees-equivalence
tags:
- undecidability
- halting
- post-correspondence
- context-free
stage: advanced
status: draft
---

# Undecidable Problems: Beyond the Halting Problem

## Core Idea
While the Halting Problem is the canonical undecidable problem, many other natural problems are also undecidable: determining if a Diophantine equation has solutions, whether a context-free grammar is ambiguous, and whether two grammars are equivalent. These examples demonstrate the pervasiveness of uncomputability across different domains.

## How It's Best Learned
Study 2-3 undecidable problems and their reduction relationships. The Post Correspondence Problem and grammar ambiguity are particularly illuminating.

## Common Misconceptions
- Assuming all undecidable problems are variants of the Halting Problem. Many arise from independent domains.
- Thinking undecidability is rare; it is pervasive.

## Explainer

The Halting Problem proved that no Turing machine can decide, for all pairs (M, w), whether machine M halts on input w. Rice's theorem extended this: no machine can decide any non-trivial semantic property of programs. But undecidability is not merely a feature of computing about computing — it appears throughout mathematics in domains that seem to have nothing to do with Turing machines.

The **Post Correspondence Problem (PCP)** is a clean example. You are given a finite list of pairs of strings over some alphabet: (u₁, v₁), (u₂, v₂), …, (uₙ, vₙ). Can you choose a sequence of indices i₁, i₂, …, iₖ (with repetition allowed) such that the concatenation uᵢ₁uᵢ₂…uᵢₖ equals vᵢ₁vᵢ₂…vᵢₖ? This is purely a string-matching puzzle with no machines or programs in sight. Yet PCP is undecidable: the proof reduces the Halting Problem to PCP by encoding computation histories as string-matching constraints. PCP is then used as an intermediate step to prove undecidability of many other problems.

**Grammar problems** are a rich source of undecidability. The question "is this context-free grammar ambiguous?" (does some string have two parse trees?) is undecidable — proved by reducing PCP to it. The question "do two context-free grammars generate the same language?" is also undecidable. Remarkably, context-free languages are one of the simplest classes beyond regular languages, yet basic questions about their structure are already incomputable. In contrast, the *membership* problem for context-free grammars (given a grammar G and string w, is w ∈ L(G)?) is decidable — so decidability is fine-grained even within a single class.

**Hilbert's Tenth Problem** asked whether there is an algorithm to determine if a given polynomial equation with integer coefficients has integer solutions (i.e., whether a **Diophantine equation** is solvable). The negative answer, proved by Matiyasevich in 1970 completing work of Davis, Putnam, and Robinson, showed this is undecidable. The proof encodes Turing machine computation into Diophantine equations — the set of solutions to a Diophantine equation can represent any recursively enumerable set. This connects number theory directly to computability theory and shows that even elementary questions about integer arithmetic are beyond algorithmic resolution. The pervasiveness of undecidability across formal language theory, number theory, and logic is not coincidental: via reductions, each undecidable problem provides a template for discovering more, building the dense web of undecidability that makes the boundaries of computability such a rich research area.
