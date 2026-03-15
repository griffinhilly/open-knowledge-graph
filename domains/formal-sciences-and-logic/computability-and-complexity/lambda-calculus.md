---
id: lambda-calculus
title: Lambda Calculus
domain: formal-sciences-and-logic
course: computability-and-complexity
prerequisites:
- id: first-order-logic-syntax
  type: soft
- id: injective-surjective-bijective
  type: soft
- id: propositional-syntax
  type: soft
- id: functions-and-function-properties
  type: soft
- id: composition-of-functions
  type: soft
- id: function-composition
  type: hard
- id: set-fundamentals
  type: soft
- id: functions-and-mappings-formal
  type: soft
- id: composition-of-functions-sets
  type: soft
builds-toward:
- church-turing-thesis-formal
- general-recursive-functions
tags:
- computation
- functional-programming
- models-of-computation
- rewriting-systems
stage: advanced
status: validated
---

# Lambda Calculus

## Core Idea
Lambda calculus is a formal system for expressing computation through function abstraction and application. The syntax is minimal: variables, lambda abstractions (λx.M), and applications (M N). Computation proceeds via β-reduction: replacing formal parameters with actual arguments. Despite its simplicity, lambda calculus is Turing-complete and captures all computable functions, making it the theoretical foundation of functional programming languages.

## How It's Best Learned
Practice β-reduction step by step on concrete lambda terms before studying Church encodings of booleans, natural numbers, and recursion. Understanding the Y combinator (fixed-point combinator) is a key milestone that illustrates how recursion emerges from pure function application.

## Common Misconceptions
- Lambda calculus has no built-in numbers, booleans, or data structures — these must be encoded as functions (Church encodings).
- α-equivalence means λx.x and λy.y are the same term; variable names carry no meaning beyond scope.
