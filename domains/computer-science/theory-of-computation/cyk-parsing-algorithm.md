---
id: cyk-parsing-algorithm
title: CYK Parsing Algorithm and CFL Membership
domain: computer-science
course: theory-of-computation
prerequisites:
- id: normal-forms-for-context-free-grammars
  type: hard
builds-toward:
- closure-properties-context-free
- limitations-of-context-free
tags:
- parsing
- cyk-algorithm
- membership
stage: abstract-reasoning
status: draft
---

# CYK Parsing Algorithm and CFL Membership

## Core Idea
The Cocke-Younger-Kasami (CYK) algorithm determines in O(n³) time whether a string is in a context-free language given a grammar in CNF. It uses dynamic programming, filling a table where entry (i, j) contains non-terminals that derive the substring of length j starting at position i.
