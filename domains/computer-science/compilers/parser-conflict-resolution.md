---
id: parser-conflict-resolution
title: Parser Conflict Resolution
domain: computer-science
course: compilers
prerequisites:
- id: lalr-grammar-construction
  type: hard
builds-toward:
- syntax-error-recovery-techniques
tags:
- parsing
- conflicts
- debugging
stage: advanced
status: draft
---

# Parser Conflict Resolution

## Core Idea
Shift-reduce and reduce-reduce conflicts occur when the parser cannot uniquely decide the next action. Conflicts are resolved through grammar rewrites, precedence declarations, or associativity rules. Understanding conflicts is essential for writing parsable grammars.

## How It's Best Learned
Create grammars generating conflicts (e.g., dangling-else problem). Interpret parser generator conflict reports and fix them methodically.

## Common Misconceptions
All conflicts are errors (some can be safely suppressed with precedence rules). Suppressing conflicts with %left is always safe (you must understand intended parsing semantics).
