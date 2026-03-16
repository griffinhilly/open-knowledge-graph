---
id: stack-applications-expression-parsing
title: 'Stack Applications: Expression Evaluation and Parsing'
domain: computer-science
course: data-structures-and-algorithms
prerequisites:
- id: stack-adt-using-arrays-linked-lists
  type: hard
- id: stack-infix-postfix-expression-evaluation
  type: hard
builds-toward:
- operator-precedence-parsing
tags:
- stacks
- parsing
- expressions
stage: formal-systems
status: draft
---

# Stack Applications: Expression Evaluation and Parsing

## Core Idea
Stacks naturally solve parsing problems like matching parentheses, converting infix to postfix notation, and evaluating postfix expressions. The Last-In-First-Out structure mirrors the nesting structure of expressions.

## How It's Best Learned
Implement a postfix calculator, then extend to infix parsing using the shunting-yard algorithm. Verify on expressions with varying operator precedence and associativity.

## Common Misconceptions
- Not recognizing that the stack order reflects operator precedence and associativity rules.
- Confusing postfix and infix notation; each has natural applications.
- Thinking stack-based parsing is limited to arithmetic; it applies to any nested structure.

## Explainer

You already know the stack as a Last-In-First-Out data structure and have seen how infix and postfix notation relate. Now consider why the stack is the natural tool for expression parsing. Mathematical expressions have nested structure: in `3 * (2 + 5)`, the inner addition must complete before the multiplication can proceed. This nesting is exactly what a stack captures — you push deferred operations onto the stack and pop them when their operands are ready. The stack's LIFO order mirrors the "most recently opened context must close first" pattern of nested expressions.

**Postfix evaluation** is the simplest application. In postfix (reverse Polish) notation like `3 2 5 + *`, you scan left to right. When you see a number, push it. When you see an operator, pop two operands, apply the operator, and push the result. The expression above pushes 3, 2, 5, then hits `+`: pop 5 and 2, compute 7, push 7. Then `*`: pop 7 and 3, compute 21, push 21. The final value on the stack is the answer. No parentheses are needed because the order of operations is encoded in the sequence itself. This is why calculators and stack-based languages (like Forth) use postfix internally — evaluation is a single linear scan with a stack.

The harder problem is converting **infix to postfix**, which is what Dijkstra's **shunting-yard algorithm** solves. Infix notation (the familiar `3 * (2 + 5)`) requires precedence and associativity rules that postfix makes explicit. The algorithm maintains an operator stack. When you encounter a number, output it immediately. When you encounter an operator, pop and output any operators on the stack that have higher precedence (or equal precedence if left-associative), then push the new operator. Left parentheses get pushed onto the stack; when a right parenthesis appears, you pop and output operators until you hit the matching left parenthesis. The operator stack acts as a holding area that reorders operators according to precedence — higher-precedence operators get output before lower-precedence ones that arrived earlier.

**Parenthesis matching** is the simplest case of the same pattern. Push each opening delimiter onto the stack; when you encounter a closing delimiter, pop and verify it matches. If the stack is empty when you try to pop, or non-empty when the expression ends, the delimiters are unbalanced. This extends naturally to matching braces in code, XML tags, and any structure where opening and closing tokens must nest correctly. The unifying insight is that stacks are the computational equivalent of nesting — whenever a problem involves deferred processing of enclosing contexts, a stack is the right tool.
