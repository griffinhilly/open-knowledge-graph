---
id: post-correspondence-problem
title: Post Correspondence Problem and Applications
domain: computer-science
course: theory-of-computation
prerequisites:
- id: reduction-techniques-undecidability
  type: hard
tags:
- pcp
- undecidability
- tiling
- string-matching
- canonical
stage: advanced
status: draft
---

# Post Correspondence Problem and Applications

## Core Idea
The Post Correspondence Problem (PCP) asks: given domino pairs (u₁, v₁), ..., (uₙ, vₙ) of strings, can you arrange them to form identical strings? PCP is undecidable without direct reference to TMs—undecidability arises from combinatorial structure. PCP reductions elegantly prove undecidability of grammar problems (CFG equivalence, ambiguity of unrestricted grammars).

## Explainer

From your work on reduction techniques, you know that proving a problem undecidable typically involves showing that a known undecidable problem (like the halting problem) can be reduced to it. The **Post Correspondence Problem (PCP)** is valuable because it provides an undecidable problem that looks nothing like Turing machines — it is purely about string manipulation — yet carries the same computational power, making it an ideal intermediate step for proving other problems undecidable.

Here is the setup. You are given a finite collection of **dominoes**, each with a string on top and a string on bottom. For example: domino 1 has "ab" on top and "a" on bottom; domino 2 has "b" on top and "ba" on bottom; domino 3 has "a" on top and "ab" on bottom. You may use any domino as many times as you like, in any order. The question is: can you arrange a sequence of dominoes so that the concatenation of all the top strings exactly equals the concatenation of all the bottom strings? In this example, choosing dominoes 1, 2, 3 gives top = "ab" + "b" + "a" = "abba" and bottom = "a" + "ba" + "ab" = "abba" — a match. Finding such a sequence, or determining that none exists, is the PCP.

The undecidability of PCP is established by reducing the acceptance problem for Turing machines to it. The construction encodes a TM's computation history — its sequence of configurations — into domino pairs, so that a matching sequence of dominoes exists if and only if the TM accepts its input. The top strings always "lag behind" the bottom strings by one configuration step, and the dominoes are designed so the only way to close this gap and achieve a match is if the TM reaches an accepting state. This encoding is intricate but the key insight is that the combinatorial freedom of choosing and repeating dominoes can simulate arbitrary computation.

PCP's real power is as a **reduction tool**. Because it involves only string concatenation and matching — no tapes, heads, or states — it connects naturally to problems about formal languages and grammars. For instance, proving that equivalence of context-free grammars is undecidable becomes straightforward by reducing PCP to it: construct two CFGs whose generated languages correspond to the top and bottom concatenations of domino sequences, so the grammars generate the same language if and only if PCP has a solution. Similarly, PCP reductions prove undecidability of ambiguity for context-free grammars and various properties of unrestricted grammars. PCP thus serves as a bridge between the Turing machine world and the formal language world, making many undecidability proofs cleaner and more direct than going through the halting problem itself.
