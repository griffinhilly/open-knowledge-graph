---
id: chomsky-hierarchy
title: The Chomsky Hierarchy
domain: computer-science
course: theory-of-computation
prerequisites:
- id: formal-languages-and-strings
  type: hard
- id: grammar-fundamentals-and-definitions
  type: hard
- id: context-free-grammars
  type: hard
builds-toward:
- context-sensitive-languages
- recursively-enumerable-languages
tags:
- formal-languages
- classification
- hierarchy
stage: advanced
status: draft
---

# The Chomsky Hierarchy

## Core Idea
The Chomsky hierarchy classifies grammars and languages into four nested levels by production restrictions: Type 3 (regular), Type 2 (context-free), Type 1 (context-sensitive), Type 0 (recursively enumerable). Each level corresponds to an automaton class with increasing power: finite automata, pushdown automata, linear-bounded automata, and Turing machines. The hierarchy represents a fundamental ordering of computational expressiveness, with each level properly containing the previous one.

## How It's Best Learned
Study production rules for each grammar type and their corresponding automaton. Prove languages belong to specific levels by constructing appropriate grammars. Understand proper subset inclusions via pumping lemma and undecidability arguments.

## Common Misconceptions
Thinking membership in one level precludes membership in higher levels (actually Type 3 ⊂ Type 2 ⊂ Type 1 ⊂ Type 0). Confusing grammar type with language type. Assuming all CFLs must be in CNF.
