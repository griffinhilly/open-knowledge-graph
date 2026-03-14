---
id: alternating-turing-machines
title: Alternating Turing Machines
domain: computer-science
course: theory-of-computation
prerequisites:
- id: turing-machines
  type: hard
- id: nondeterministic-finite-automata
  type: soft
builds-toward:
- polynomial-hierarchy
tags:
- automata
- alternation
- quantifiers
stage: advanced
status: draft
---

# Alternating Turing Machines

## Core Idea
An alternating Turing machine (ATM) is a nondeterministic TM where states are classified as existential (∃-states: accept if any branch accepts) or universal (∀-states: accept only if all branches accept), mirroring quantifier alternation. Alternation depth k defines ATIME(f(n)) and ASPACE(f(n)) classes. A key result: ATM with one level of alternation matches nondeterministic TM power. ATMs formalize the polynomial hierarchy via alternating quantifiers, providing clean models for understanding quantified complexity classes.
