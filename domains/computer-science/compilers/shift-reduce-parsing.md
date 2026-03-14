---
id: shift-reduce-parsing
title: Shift-Reduce Parsing Mechanics
domain: computer-science
course: compilers
prerequisites:
- id: lr-parsing
  type: hard
- id: stacks-data-structure
  type: hard
builds-toward:
- lr-state-machine-construction
tags:
- parsing-algorithm
- stack-operations
stage: advanced
status: draft
---

# Shift-Reduce Parsing Mechanics

## Core Idea
Shift-reduce parsing uses two operations on a stack: shift (push the next input token) and reduce (pop a production's right-hand side and push the left-hand side). The parser decides on each step whether to shift or reduce using a state machine and lookahead. Shift-reduce conflicts are resolved by precedence rules or grammar restrictions.
