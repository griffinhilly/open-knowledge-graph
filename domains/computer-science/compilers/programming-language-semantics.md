---
id: programming-language-semantics
title: Programming Language Semantics
domain: computer-science
course: compilers
prerequisites:
- id: lambda-calculus-foundations
  type: hard
- id: context-free-grammars
  type: soft
builds-toward:
- type-inference-algorithms
- runtime-function-calls
tags:
- semantics
- formal-methods
- language-design
stage: advanced
status: draft
---

# Programming Language Semantics

## Core Idea
Semantics defines what a program means—its runtime behavior. Formal semantics uses denotational (functions mapping programs to meanings), operational (step-by-step execution rules), or axiomatic (assertions about properties) approaches. These frameworks allow compilers to reason about correctness and optimization validity.

## Explainer

A grammar tells you whether `x = 3 + y` is a syntactically valid program, but it says nothing about what the program *does*. **Programming language semantics** fills that gap — it is the formal study of program meaning. If syntax is the grammar of sentences, semantics is what those sentences actually say. Your background in lambda calculus gives you the right foundation here, because lambda calculus is itself a minimal programming language with precisely defined semantics, and much of formal semantics extends its ideas.

**Operational semantics** is the most concrete approach. It defines meaning by specifying evaluation rules — literally, "given this expression in this state, the next step produces that expression in that state." For example, an operational rule might say: to evaluate `if true then e1 else e2`, evaluate `e1`. These rules resemble an interpreter specification. There are two flavors: **small-step** (structural) operational semantics breaks evaluation into individual reduction steps, making it easy to reason about intermediate states and non-termination. **Big-step** (natural) semantics jumps directly from an expression to its final value, which is closer to how you intuitively think about evaluation but hides intermediate computation.

**Denotational semantics** takes a more mathematical approach. Instead of describing how a program executes step by step, it maps each program to a mathematical object — its "denotation." A variable maps to its value in an environment, a function maps to a mathematical function from inputs to outputs, and a while loop maps to a fixed point. This builds directly on the function-as-value idea from lambda calculus. The advantage is compositionality: the meaning of a compound expression is built entirely from the meanings of its parts, which makes it possible to prove program equivalences algebraically.

**Axiomatic semantics**, most associated with Hoare logic, defines meaning through the properties you can prove about a program. A **Hoare triple** `{P} S {Q}` says: if precondition P holds before executing statement S, then postcondition Q holds after. For instance, `{x > 0} x = x - 1 {x >= 0}`. This approach is less about what the program computes and more about what guarantees it provides, making it the foundation for formal verification. For compiler writers, all three frameworks matter: operational semantics guides interpreter and code generator design, denotational semantics justifies optimization (two expressions with the same denotation can be freely substituted), and axiomatic semantics validates that transformations preserve program correctness.
