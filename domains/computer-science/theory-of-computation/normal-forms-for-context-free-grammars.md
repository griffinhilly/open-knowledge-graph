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
