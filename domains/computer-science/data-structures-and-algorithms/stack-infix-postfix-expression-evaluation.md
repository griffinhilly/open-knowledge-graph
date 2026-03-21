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

## Questions

```yaml
- question: "Evaluate the postfix expression: 3 4 2 * +"
  type: multiple-choice
  options:
    - "14 — computed as (3 + 4) × 2"
    - "11 — computed as 3 + (4 × 2)"
    - "24 — computed as 3 × 4 × 2"
    - "10 — computed as (3 + 4) + 2 + 1"
  answer: 1
  explanation: "Scan left to right: push 3, push 4, push 2. Hit *: pop 2 and 4, compute 4×2=8, push 8. Hit +: pop 8 and 3, compute 3+8=11, push 11. Result: 11. The key point: multiplication is applied first because * appears first in the postfix sequence, encoding the correct evaluation order without any precedence rules. Option A (14) is the error of reading postfix as if it were infix and computing left-to-right naively."

- question: "Why does postfix (RPN) notation not require parentheses or operator precedence rules?"
  type: multiple-choice
  options:
    - "Because postfix expressions are always shorter and simpler than their infix equivalents"
    - "Because the position of operators in postfix already encodes the correct evaluation order"
    - "Because stacks handle parentheses through automatic bracket matching"
    - "Because postfix only applies to expressions where all operators have equal precedence"
  answer: 1
  explanation: "In postfix, the sequence in which operators appear IS the sequence in which they are applied — no external rules needed. '3 4 2 * +' unambiguously applies * before + because * appears before +. Parentheses exist in infix notation to override the default precedence order; postfix has no default order to override, so no parentheses are needed. The evaluation order is fully determined by the token sequence."

- question: "Evaluating a postfix expression requires no knowledge of operator precedence."
  type: true-false
  answer: true
  explanation: "True. The postfix algorithm is purely mechanical: scan left to right, push numbers, apply operators to the top two stack elements. No precedence table is consulted at any point. This is precisely why compilers convert infix to postfix before evaluation — the conversion step resolves all precedence ambiguity once, so the evaluation step can be a simple linear scan."

- question: "The postfix expression '3 4 + 2 *' has the same value as the infix expression '3 + 4 * 2'."
  type: true-false
  answer: false
  explanation: "False. '3 4 + 2 *' evaluates as (3+4)×2 = 14. The infix '3 + 4 * 2' evaluates as 3+(4×2) = 11 due to multiplication precedence. The postfix expression that matches '3 + 4 * 2' is '3 4 2 * +'. This illustrates exactly what postfix encodes: different operator positions represent different groupings, and the position difference between '3 4 + 2 *' and '3 4 2 * +' is what distinguishes (3+4)×2 from 3+(4×2)."

- question: "Explain why the stack is the natural data structure for evaluating postfix expressions — what role does LIFO ordering play?"
  type: short-answer
  answer: "As you scan postfix left to right, numbers must be held until their operator arrives. When an operator is encountered, it should apply to the two most recently seen operands — exactly the two on top of the stack. LIFO ordering ensures the most recently pushed numbers are consumed first, matching postfix's sequential evaluation. Intermediate results are pushed back onto the stack, ready to serve as operands for subsequent operators. The stack's depth naturally tracks nesting without any explicit bookkeeping."
  explanation: "The stack's LIFO property maps directly onto the nested structure of arithmetic. An expression like '3 4 2 * +' computes an inner sub-expression (* on 4 and 2) before an outer one (+ on 3 and 8) — the inner result must be remembered until the outer operator arrives. The stack holds it automatically. Any data structure that retrieved items in a different order (e.g., a queue in FIFO order) would produce incorrect results."
```

## Explainer

You already know how a stack works — push items on top, pop them off in LIFO order. Expression evaluation is one of the stack's most elegant applications, and understanding it reveals why compilers don't process math the way humans read it.

Consider the expression `3 + 4 * 2`. Humans handle this by remembering operator precedence rules: multiplication before addition, so the answer is 11, not 14. But a computer scanning left to right sees `3`, then `+`, then `4` — and must somehow "wait" to apply the addition until it knows whether a higher-precedence operator follows. This is the fundamental problem with **infix notation**: the order you read tokens isn't the order you execute them, and parentheses add further complexity. Every infix expression carries implicit evaluation rules that require look-ahead or backtracking to resolve.

**Postfix notation** (also called Reverse Polish Notation) eliminates this problem entirely. The same expression becomes `3 4 2 * +`. The rule is dead simple: scan left to right. When you see a number, push it onto the stack. When you see an operator, pop its two operands, apply the operation, and push the result back. For `3 4 2 * +`: push 3, push 4, push 2. Hit `*` — pop 2 and 4, compute 8, push 8. Hit `+` — pop 8 and 3, compute 11, push 11. Done. No precedence rules, no parentheses, no ambiguity. The stack naturally holds intermediate results exactly as long as they're needed.

Converting from infix to postfix uses a second classic algorithm called the **Shunting Yard algorithm** (after Dijkstra). It also uses a stack, but this time the stack holds operators rather than numbers. As you scan the infix expression, numbers pass straight to the output. When you encounter an operator, you pop and output any operators on the stack that have higher or equal precedence, then push the new operator. Parentheses act as barriers — a left parenthesis is pushed onto the stack, and when a right parenthesis appears, you pop operators to the output until you hit the matching left parenthesis. The result is a postfix expression that encodes the correct evaluation order without any parentheses. This two-step pipeline — infix to postfix, then postfix evaluation — is how calculators and compilers process arithmetic, and both steps rely on the stack's ability to defer and recall operations in the right order.
