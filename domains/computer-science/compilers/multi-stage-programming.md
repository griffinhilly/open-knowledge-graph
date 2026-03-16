---
id: multi-stage-programming
title: Multi-Stage Programming and Staged Compilation
domain: computer-science
course: compilers
prerequisites:
- id: intermediate-code-representation
  type: hard
- id: code-generation
  type: hard
builds-toward:
- compiler-bootstrapping
tags:
- metaprogramming
- stages
- codegen
stage: advanced
status: draft
---

# Multi-Stage Programming and Staged Compilation

## Core Idea
Multi-stage programming separates computation into stages: stage 1 generates code as data structures, stage 2 executes the generated code. Used for compiler generators, template instantiation, and partial evaluation, it brings code-generation capabilities into the language itself.

## Explainer

You already understand intermediate representations and code generation — how a compiler transforms source programs into executable output. Multi-stage programming takes this idea and makes it available *within* the language itself: a program can construct another program (as an IR or code fragment) at one stage and then execute or compile that generated code at the next stage. Instead of the compiler being the only entity that generates code, the programmer gets explicit control over when code is produced and when it runs.

The simplest way to understand staging is through a concrete example. Imagine you have an interpreter for mathematical expressions, and you know at compile time that a particular expression will always be `x * 2 + 1`. A staged program can **partially evaluate** the interpreter at stage 1, "baking in" the known expression structure and producing specialized code that just computes `x * 2 + 1` directly — no interpretation overhead at runtime. The key language constructs are **brackets** (which delay computation to a later stage) and **escapes** (which splice a current-stage value into delayed code). In MetaOCaml, for instance, `.<e>.` brackets an expression for later execution, and `.~e` escapes a value into bracketed code.

What makes this different from ordinary metaprogramming (like C macros or string-based code generation) is **type safety across stages**. In a well-designed multi-stage language, the type system guarantees that the generated code is well-typed before it is ever executed. You cannot accidentally produce code with a type error at stage 2 — the stage-1 type checker catches it. This is the crucial advantage over approaches like `eval()` or template-based code generation, where errors only surface at runtime.

Staged compilation connects directly to several compiler techniques you have already studied. **Compiler generators** like Yacc are essentially two-stage systems: stage 1 reads a grammar and generates a parser (code), stage 2 compiles and runs that parser. **Template instantiation** in C++ is a limited form of staging where the template parameters are resolved at compile time to produce specialized code. **Partial evaluation** — automatically specializing a general program given some known inputs — is the theoretical foundation underlying all of these. Multi-stage programming makes this pipeline explicit, composable, and safe, turning the compiler's own code-generation machinery into a first-class tool for the programmer.
