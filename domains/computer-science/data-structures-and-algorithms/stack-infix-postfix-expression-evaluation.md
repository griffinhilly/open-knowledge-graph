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
