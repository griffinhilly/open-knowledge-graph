---
id: cfg-pda-equivalence
title: CFG–PDA Equivalence
domain: computer-science
course: theory-of-computation
prerequisites:
- id: pushdown-automata
  type: hard
- id: chomsky-normal-form
  type: hard
builds-toward:
- closure-properties-cfl
- pumping-lemma-cfl
- turing-machines
tags:
- CFG
- PDA
- equivalence
- context-free-languages
stage: advanced
status: validated
---

# CFG–PDA Equivalence

## Core Idea
The CFGs and PDAs are equivalent models: a language is context-free if and only if some PDA recognizes it. The proof goes both ways — any CFG can be converted to a PDA (using a one-state PDA that simulates leftmost derivations), and any PDA can be converted to a CFG. This equivalence firmly establishes the context-free languages as a well-defined class, analogous to Kleene's theorem for regular languages. The construction from CFG to PDA mirrors the Earley/CYK parsing algorithms in practice.

## Common Misconceptions
- Thinking the CFG-to-PDA construction requires multiple states — a single state plus the stack is sufficient.
- Confusing the equivalence of CFG and (nondeterministic) PDA with the equivalence of deterministic PDA and some grammar class — deterministic PDAs correspond to a strictly smaller class (DCFLs).
