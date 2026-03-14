---
id: compiler-error-recovery
title: Error Recovery in Compilation
domain: computer-science
course: compilers
prerequisites:
- id: syntax-error-recovery-techniques
  type: hard
- id: semantic-error-detection-reporting
  type: hard
- id: parser-generators
  type: soft
tags:
- error-handling
- parsing
- compilation
stage: advanced
status: draft
---

# Error Recovery in Compilation

## Core Idea
Production compilers continue parsing after syntax errors to report multiple errors in one pass. Techniques include token insertion/deletion (minimal fixes), phrase-level recovery (skip to known safe states), and resynchronization on high-confidence tokens, enabling developers to fix all errors at once.

## How It's Best Learned
Add error recovery to a hand-written recursive-descent parser: insert panic-mode recovery after encountering an unexpected token, then verify it finds subsequent errors.
