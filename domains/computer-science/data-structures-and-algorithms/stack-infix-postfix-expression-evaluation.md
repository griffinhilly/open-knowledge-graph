---
id: stack-infix-postfix-expression-evaluation
title: 'Expression Evaluation: Infix, Postfix, Prefix'
domain: computer-science
course: data-structures-and-algorithms
prerequisites:
- id: stack-adt-using-arrays-linked-lists
  type: hard
tags:
- stack
- expression
- parsing
stage: formal-systems
status: draft
---

# Expression Evaluation: Infix, Postfix, Prefix

## Core Idea
Infix notation (e.g., 3 + 4) is human-readable but requires operator precedence and parentheses. Postfix (e.g., 3 4 +) eliminates ambiguity and is evaluated left-to-right with a stack. Converting infix to postfix and evaluating postfix are fundamental compiler and calculator operations.

## Explainer

You already know how a stack works — push items on top, pop them off in LIFO order. Expression evaluation is one of the stack's most elegant applications, and understanding it reveals why compilers don't process math the way humans read it.

Consider the expression `3 + 4 * 2`. Humans handle this by remembering operator precedence rules: multiplication before addition, so the answer is 11, not 14. But a computer scanning left to right sees `3`, then `+`, then `4` — and must somehow "wait" to apply the addition until it knows whether a higher-precedence operator follows. This is the fundamental problem with **infix notation**: the order you read tokens isn't the order you execute them, and parentheses add further complexity. Every infix expression carries implicit evaluation rules that require look-ahead or backtracking to resolve.

**Postfix notation** (also called Reverse Polish Notation) eliminates this problem entirely. The same expression becomes `3 4 2 * +`. The rule is dead simple: scan left to right. When you see a number, push it onto the stack. When you see an operator, pop its two operands, apply the operation, and push the result back. For `3 4 2 * +`: push 3, push 4, push 2. Hit `*` — pop 2 and 4, compute 8, push 8. Hit `+` — pop 8 and 3, compute 11, push 11. Done. No precedence rules, no parentheses, no ambiguity. The stack naturally holds intermediate results exactly as long as they're needed.

Converting from infix to postfix uses a second classic algorithm called the **Shunting Yard algorithm** (after Dijkstra). It also uses a stack, but this time the stack holds operators rather than numbers. As you scan the infix expression, numbers pass straight to the output. When you encounter an operator, you pop and output any operators on the stack that have higher or equal precedence, then push the new operator. Parentheses act as barriers — a left parenthesis is pushed onto the stack, and when a right parenthesis appears, you pop operators to the output until you hit the matching left parenthesis. The result is a postfix expression that encodes the correct evaluation order without any parentheses. This two-step pipeline — infix to postfix, then postfix evaluation — is how calculators and compilers process arithmetic, and both steps rely on the stack's ability to defer and recall operations in the right order.
