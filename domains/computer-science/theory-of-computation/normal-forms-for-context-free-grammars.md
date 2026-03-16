---
id: normal-forms-for-context-free-grammars
title: Normal Forms for Context-Free Grammars
domain: computer-science
course: theory-of-computation
prerequisites:
- id: cfg-pda-equivalence
  type: hard
builds-toward:
- cyk-parsing-algorithm
- closure-properties-context-free
tags:
- cfg
- normal-forms
- cnf
- gnf
stage: abstract-reasoning
status: draft
---

# Normal Forms for Context-Free Grammars

## Core Idea
Chomsky Normal Form (CNF) restricts productions to A → BC or A → a, eliminating ε-productions and unit productions. Greibach Normal Form (GNF) requires A → aα where a is a terminal. Both normal forms simplify parsing and proofs while maintaining expressiveness; any CFG can be converted to CNF or GNF.

## Explainer

You already know that context-free grammars and pushdown automata recognize exactly the same class of languages. But context-free grammars in their general form are messy — productions can have arbitrary mixes of terminals and nonterminals on the right side, chains of unit productions like A → B → C → D, and ε-productions that generate the empty string. This freedom makes grammars flexible for language designers but nightmarish for algorithm designers. Normal forms solve this by constraining production rules into a disciplined shape while preserving the grammar's generative power.

**Chomsky Normal Form** (CNF) is the most widely used normal form. Every production must be either A → BC (two nonterminals) or A → a (a single terminal). That's it — no mixed right-hand sides, no long chains, no epsilon. The conversion process works in stages: first eliminate ε-productions by propagating their effect into other rules, then eliminate unit productions by short-circuiting chains, then break long right-hand sides into binary pairs by introducing fresh nonterminals, and finally replace terminals that appear alongside nonterminals with dedicated "terminal nonterminals." Each step preserves the language (possibly minus ε). The result is a grammar where every derivation of a string of length n takes exactly 2n − 1 steps, which makes CNF the foundation for the CYK parsing algorithm — a dynamic programming approach that relies on this binary branching structure.

**Greibach Normal Form** (GNF) takes a different approach: every production starts with a terminal followed by zero or more nonterminals, as in A → aBC. This means every derivation step consumes exactly one input symbol, which directly corresponds to one move of a pushdown automaton. GNF conversion is more involved — it requires eliminating left recursion and rewriting productions using substitution — but the result makes the grammar-to-PDA construction transparent and eliminates the possibility of infinite loops in top-down parsing.

The key insight is that normal forms are not about changing what a grammar can express — they are about standardizing structure to enable algorithms and proofs. CNF gives you binary parse trees and polynomial-time parsing. GNF gives you deterministic single-symbol consumption and clean PDA construction. When you encounter a proof that says "without loss of generality, assume the grammar is in CNF," the claim rests on the fact that any CFG can be mechanically transformed into CNF while generating the same language, so anything proved about CNF grammars holds for all context-free languages.
