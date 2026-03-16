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

## Explainer

When you build an LALR parse table from a grammar, you may encounter situations where the parser reaches a state and cannot uniquely determine what to do next. These ambiguities manifest as two specific types of conflicts. A **shift-reduce conflict** occurs when the parser could either shift the next token onto the stack (continuing to build a longer match) or reduce the tokens already on the stack (applying a production rule). A **reduce-reduce conflict** occurs when two different production rules could both apply to the same stack contents. Both arise because the grammar, as written, does not give the parser enough information to decide.

The most famous example is the **dangling-else problem**. Given `if a then if b then s1 else s2`, the parser reaches the `else` and faces a choice: reduce the inner `if-then` to a statement (binding `else` to the outer `if`), or shift the `else` to continue building the inner `if-then-else` (binding `else` to the inner `if`). Most languages intend the second interpretation — `else` binds to the nearest `if` — and this is naturally what shifting produces. This is a case where the conflict has a correct resolution, and you can tell the parser generator to prefer shifting.

Parser generators like Yacc and Bison provide **precedence and associativity declarations** to resolve conflicts without rewriting the grammar. Declaring `%left '+'` tells the parser that `+` is left-associative: when it sees `a + b + c`, it should reduce `a + b` first rather than shifting the second `+`. Declaring `%right '='` makes assignment right-associative. Precedence levels (determined by declaration order) resolve conflicts between different operators: `a + b * c` shifts `*` because `*` has higher precedence than `+`. These declarations are powerful but dangerous if used carelessly — they silently suppress conflicts, and if the suppression does not match your intended semantics, you get a parser that quietly accepts wrong parse trees.

The safest approach treats conflicts as signals that your grammar needs attention. Start by reading the parser generator's conflict report, which tells you the exact state, the conflicting items, and the lookahead token involved. Many conflicts can be eliminated by **grammar refactoring**: left-factoring common prefixes, introducing new nonterminals to disambiguate, or restructuring productions. Reserve precedence declarations for the cases where they are natural and well-understood — arithmetic operators, assignment, and the dangling-else — and always verify that the resolved parser produces the parse trees you expect. A reduce-reduce conflict is almost always a sign of a genuine grammar design problem and should rarely be suppressed with precedence; instead, restructure the grammar so the two competing rules no longer overlap.
