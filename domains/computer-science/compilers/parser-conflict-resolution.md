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
status: validated
---

# Parser Conflict Resolution

## Core Idea
Shift-reduce and reduce-reduce conflicts occur when the parser cannot uniquely decide the next action. Conflicts are resolved through grammar rewrites, precedence declarations, or associativity rules. Understanding conflicts is essential for writing parsable grammars.

## How It's Best Learned
Create grammars generating conflicts (e.g., dangling-else problem). Interpret parser generator conflict reports and fix them methodically.

## Common Misconceptions
All conflicts are errors (some can be safely suppressed with precedence rules). Suppressing conflicts with %left is always safe (you must understand intended parsing semantics).

## Questions

```yaml
- question: "In the dangling-else problem, a parser generator defaults to preferring shift over reduce when it encounters the conflict on the 'else' token. What parse tree does this default produce for `if a then if b then s1 else s2`?"
  type: multiple-choice
  options:
    - "The else binds to the outer if, because shifting extends the outer construct"
    - "The else binds to the nearest (inner) if, because shifting continues building the inner if-then-else"
    - "A syntax error is reported, because the grammar is ambiguous"
    - "Both parse trees are generated and the programmer must choose"
  answer: 1
  explanation: "When the parser shifts the 'else', it continues building the inner 'if-then-else' construct rather than reducing the inner 'if-then' to a complete statement. This binds the else to the nearest enclosing if — which is the intended semantics of most languages. This is a case where the default shift preference happens to match the desired language semantics, making it safe to leave the conflict resolved by precedence rather than grammar rewriting."

- question: "A grammar has a reduce-reduce conflict. The developer adds '%left' declarations to suppress it and all parser tests pass. What risk has been introduced?"
  type: multiple-choice
  options:
    - "None — precedence declarations are designed to resolve all types of conflicts safely"
    - "The parser may silently produce incorrect parse trees, because precedence rules don't naturally model the semantics of reduce-reduce conflicts"
    - "The grammar becomes LALR(2) instead of LALR(1), requiring a more powerful parser"
    - "Compilation will be slower because the parser must check precedence at every step"
  answer: 1
  explanation: "Precedence and associativity declarations are designed for operator-precedence ambiguities (arithmetic expressions, dangling-else). A reduce-reduce conflict typically means two competing production rules overlap, which is a structural grammar problem — not an operator-precedence problem. Suppressing it with '%left' makes the conflict disappear from the report but doesn't fix the underlying ambiguity; the parser simply picks one rule silently, which may produce incorrect parse trees for some inputs. Unlike shift-reduce conflicts (which often have natural resolutions), reduce-reduce conflicts almost always indicate genuine grammar design problems."

- question: "Any conflict in an LALR grammar is evidence of a design error and should be eliminated by rewriting the grammar."
  type: true-false
  answer: false
  explanation: "This is false. Some conflicts — particularly the dangling-else shift-reduce conflict — have natural, semantically correct resolutions using precedence and associativity declarations. Operator precedence conflicts (e.g., 'a + b * c') are also routinely resolved via '%left' and '%right' rather than grammar rewrites. The key is understanding which conflicts have clear intended semantics that precedence declarations can safely encode, versus which conflicts signal genuine ambiguity requiring grammar restructuring."

- question: "A reduce-reduce conflict is generally more dangerous than a shift-reduce conflict and should rarely be suppressed with precedence declarations."
  type: true-false
  answer: true
  explanation: "True. A shift-reduce conflict often arises from natural language ambiguities (like dangling-else or operator precedence) where the intended resolution is clear and well-modeled by precedence declarations. A reduce-reduce conflict means two different grammar rules match the same input in the same parser state — this almost always indicates a genuine design flaw in the grammar, such as overlapping or redundant productions. Suppressing it with precedence rules hides the problem and may silently accept incorrect parse trees."

- question: "Why is a reduce-reduce conflict generally more concerning than a shift-reduce conflict, and what should a grammar designer do when they encounter one?"
  type: short-answer
  answer: "A reduce-reduce conflict means two different production rules can both legally apply to the same stack contents in the same parser state, representing a genuine structural ambiguity in the grammar. This almost always indicates a design problem — two rules that shouldn't compete are overlapping. The correct response is to restructure the grammar to eliminate the overlap, not to suppress the conflict with precedence declarations. A shift-reduce conflict, by contrast, often has a natural resolution (prefer shift for dangling-else; use operator precedence for arithmetic), so precedence declarations are appropriate. Suppressing a reduce-reduce conflict with '%left' or '%right' merely hides the ambiguity and can cause the parser to silently accept incorrect parse trees."
  explanation: "The distinction matters because shift-reduce conflicts frequently arise from predictable, well-understood language patterns (operator precedence, optional clauses) where the semantics clearly dictate one resolution. Reduce-reduce conflicts lack this natural mapping — the competing rules typically shouldn't coexist, and choosing between them arbitrarily via precedence is not semantically principled."
```

## Explainer

When you build an LALR parse table from a grammar, you may encounter situations where the parser reaches a state and cannot uniquely determine what to do next. These ambiguities manifest as two specific types of conflicts. A **shift-reduce conflict** occurs when the parser could either shift the next token onto the stack (continuing to build a longer match) or reduce the tokens already on the stack (applying a production rule). A **reduce-reduce conflict** occurs when two different production rules could both apply to the same stack contents. Both arise because the grammar, as written, does not give the parser enough information to decide.

The most famous example is the **dangling-else problem**. Given `if a then if b then s1 else s2`, the parser reaches the `else` and faces a choice: reduce the inner `if-then` to a statement (binding `else` to the outer `if`), or shift the `else` to continue building the inner `if-then-else` (binding `else` to the inner `if`). Most languages intend the second interpretation — `else` binds to the nearest `if` — and this is naturally what shifting produces. This is a case where the conflict has a correct resolution, and you can tell the parser generator to prefer shifting.

Parser generators like Yacc and Bison provide **precedence and associativity declarations** to resolve conflicts without rewriting the grammar. Declaring `%left '+'` tells the parser that `+` is left-associative: when it sees `a + b + c`, it should reduce `a + b` first rather than shifting the second `+`. Declaring `%right '='` makes assignment right-associative. Precedence levels (determined by declaration order) resolve conflicts between different operators: `a + b * c` shifts `*` because `*` has higher precedence than `+`. These declarations are powerful but dangerous if used carelessly — they silently suppress conflicts, and if the suppression does not match your intended semantics, you get a parser that quietly accepts wrong parse trees.

The safest approach treats conflicts as signals that your grammar needs attention. Start by reading the parser generator's conflict report, which tells you the exact state, the conflicting items, and the lookahead token involved. Many conflicts can be eliminated by **grammar refactoring**: left-factoring common prefixes, introducing new nonterminals to disambiguate, or restructuring productions. Reserve precedence declarations for the cases where they are natural and well-understood — arithmetic operators, assignment, and the dangling-else — and always verify that the resolved parser produces the parse trees you expect. A reduce-reduce conflict is almost always a sign of a genuine grammar design problem and should rarely be suppressed with precedence; instead, restructure the grammar so the two competing rules no longer overlap.
