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

## Explainer

From syntax error recovery techniques and semantic error detection, you know that parsers can detect when input violates the grammar and that type checkers can flag mismatched types and undeclared variables. **Compiler error recovery** is the art of continuing compilation *after* encountering an error so that the compiler can report as many problems as possible in a single run. Without error recovery, a compiler stops at the first mistake, and a developer with ten errors must compile ten times — an unacceptable workflow for real-world development.

The simplest recovery strategy is **panic mode**: when the parser encounters an unexpected token, it discards tokens until it finds a **synchronization point** — a token that reliably marks the start of a new construct, like a semicolon, closing brace, or keyword such as `class` or `function`. The parser then resumes normal parsing from that synchronizing token. Panic mode is crude but robust: it rarely produces cascading false errors because it skips past the damaged region entirely. The tradeoff is that it may miss errors in the skipped tokens, but in practice the errors it does find are almost always genuine problems rather than artifacts of the first error.

More sophisticated strategies attempt finer-grained recovery. **Phrase-level recovery** tries to patch the input minimally — inserting a missing semicolon, deleting an extra operator, or replacing a malformed token — to let parsing continue from the exact point of failure. This catches more errors but risks producing **cascading errors**: a single real mistake triggers a chain of spurious error messages because the "repair" puts the parser into a state that does not match the programmer's intent. Good compilers limit cascading by tracking error counts and suppressing messages when errors cluster, or by switching to panic mode after a phrase-level repair fails to stabilize.

The challenge extends beyond parsing into semantic analysis. A type checker that encounters an expression with an error typically assigns it a special **error type** (sometimes called "poison" or "bottom") that is compatible with every other type. This prevents a single type error from producing dozens of downstream "type mismatch" messages that are all consequences of the original problem. Similarly, if a variable declaration fails to parse, the name resolver records the variable as existing-but-erroneous so that every subsequent use does not generate a redundant "undeclared variable" error. The goal throughout is **maximum signal, minimum noise**: report every genuine mistake exactly once, suppress the false positives that would bury real problems in a flood of irrelevant messages.
