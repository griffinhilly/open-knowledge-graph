---
id: cyk-algorithm-membership-testing
title: CYK Algorithm and Membership Testing
domain: computer-science
course: theory-of-computation
prerequisites:
- id: grammar-normal-forms-analysis
  type: hard
- id: dynamic-programming-intro
  type: soft
builds-toward:
- pushdown-automata
tags:
- cyk
- parsing
- membership
- dynamic-programming
- cubic-time
stage: advanced
status: draft
---

# CYK Algorithm and Membership Testing

## Core Idea
The Cocke-Younger-Kasami algorithm tests whether a string belongs to a CFL in O(n³) time, assuming grammar in CNF. It builds a table: entry [i,j] lists non-terminals deriving substring i..j. CYK is polynomial—optimal for arbitrary CFGs without compilation overhead—making it crucial for parsing without grammar restrictions.

## How It's Best Learned
Trace CYK on a small example (e.g., balanced parentheses grammar). Fill the table bottom-up, checking which rules produce needed sub-derives.
