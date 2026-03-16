---
id: grammar-normal-forms-analysis
title: 'Grammar Normal Forms: CNF and GNF'
domain: computer-science
course: theory-of-computation
prerequisites:
- id: chomsky-normal-form
  type: hard
- id: context-free-grammar-properties-and-ambiguity
  type: soft
builds-toward:
- cyk-algorithm-membership-testing
tags:
- cnf
- greibach-normal-form
- normal-forms
- transformation
- simplification
stage: advanced
status: draft
---

# Grammar Normal Forms: CNF and GNF

## Core Idea
Chomsky Normal Form (CNF) restricts productions to A → BC or A → a, enabling efficient algorithms and theoretical analysis. Greibach Normal Form ensures rightmost symbols are terminals, useful for top-down parsing. Transforming to normal form eliminates epsilon, unit, and useless productions—a preprocessing step that may increase grammar size but simplifies downstream algorithms.

## How It's Best Learned
Work through transformation steps (eliminate epsilon, unit productions, chain productions) on a concrete grammar. Verify the resulting grammar generates the same language.

## Explainer

From your study of Chomsky Normal Form, you know that any context-free grammar can be restructured so that every production has a specific shape. Normal forms are not about changing *what* a grammar generates — the language stays exactly the same — but about restricting *how* productions are written so that algorithms and proofs become simpler. Think of it like converting a fraction to lowest terms: the value does not change, but the simplified form is far easier to work with.

**Chomsky Normal Form (CNF)** requires every production to be either A → BC (two non-terminals) or A → a (a single terminal). No epsilon productions (except possibly S → ε for the start symbol), no unit productions (A → B), and no right-hand sides with more than two symbols. This rigid binary structure is what makes the **CYK parsing algorithm** possible: because every production splits into exactly two parts, you can fill in a triangular parsing table bottom-up in O(n³) time. Without CNF, the variable-length right-hand sides make systematic parsing much harder.

**Greibach Normal Form (GNF)** takes a different approach: every production must begin with a terminal followed by zero or more non-terminals (A → aα, where a is a terminal and α is a string of non-terminals). This form is useful for **top-down parsing** because reading one input symbol always consumes exactly one terminal from the front of a production, guaranteeing that the parser makes progress on every step without risk of infinite left-recursive loops. GNF also simplifies certain proofs about pushdown automata, since each derivation step corresponds naturally to one input read and one stack operation.

The transformation process follows a standard pipeline. First, **eliminate epsilon productions**: for every rule A → ε, find all places A appears on the right-hand side of other rules and create versions both with and without A. Second, **eliminate unit productions** (A → B): trace chains of unit productions and replace them with direct rules to the eventual terminal or multi-symbol result. Third, **remove useless symbols**: any non-terminal that cannot be reached from the start symbol or cannot derive a terminal string is dead weight. Finally, restructure the remaining productions into the target normal form — for CNF, break long right-hand sides into chains of binary rules using fresh non-terminals. The grammar may grow in size (more rules, more non-terminals), but it generates exactly the same language, and the standardized structure unlocks efficient algorithms downstream.
