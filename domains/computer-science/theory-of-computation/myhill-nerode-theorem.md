---
id: myhill-nerode-theorem
title: Myhill-Nerode Theorem
domain: computer-science
course: theory-of-computation
prerequisites:
- id: dfa-state-minimization
  type: hard
- id: regular-language-properties
  type: hard
tags:
- automata
- regular-languages
- minimization
stage: advanced
status: draft
---

# Myhill-Nerode Theorem

## Core Idea
The Myhill-Nerode theorem characterizes regular languages via equivalence classes over strings: a language is regular if and only if the set of right equivalence classes (where two strings are equivalent if appending any suffix produces the same acceptance result) is finite. This provides a criterion for regularity independent of any automaton, showing that regularity is fundamentally about how many 'distinct behaviors' a language requires. The theorem yields an algorithm for computing minimal DFAs and proves certain languages (like palindromes) cannot be regular by showing infinite equivalence classes.

## How It's Best Learned
Compute equivalence classes for both regular and non-regular languages explicitly. Prove non-regularity using infinite equivalence classes. Construct minimal DFAs from equivalence class partitions.

## Common Misconceptions
Confusing the right-invariant equivalence relation with other string equivalences. Assuming equivalent strings must be identical. Applying the theorem to non-regular language classes.
