---
id: polya-enumeration-theorem
title: Pólya Enumeration Theorem
domain: mathematics
course: graph-theory-and-combinatorics
prerequisites:
- id: group-actions
  type: hard
tags:
- combinatorics
- enumeration
stage: advanced
status: draft
---

# Pólya Enumeration Theorem

## Core Idea
Pólya's Enumeration Theorem counts equivalence classes of structures under group actions via the cycle index polynomial of the group. If G acts on positions and we color with c colors, the number of distinct colorings is (1/|G|) Σ c^(cyc(g)) over g in G, where cyc(g) is the number of cycles. This solves counting problems involving symmetries.

## How It's Best Learned
Apply the theorem to necklaces and bracelets using the cyclic group, verifying results by hand enumeration for small cases.

## Common Misconceptions
The formula counts distinct colorings under the group action, not all colorings; it 'quotients out' the symmetry.
