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
