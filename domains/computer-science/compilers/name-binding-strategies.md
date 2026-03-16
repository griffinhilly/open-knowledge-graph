---
id: name-binding-strategies
title: Name Binding Strategies
domain: computer-science
course: compilers
prerequisites:
- id: scope-binding-resolution
  type: hard
builds-toward:
- type-checking-bidirectional
tags:
- binding
- names
- implementation
stage: advanced
status: draft
---

# Name Binding Strategies

## Core Idea
Names can be bound at compile-time (static binding) or run-time (dynamic binding). Different strategies have different performance and expressive power implications, illuminating language design choices and compiler differences.

## How It's Best Learned
Implement both static and dynamic binding for a language. Compare performance, expressiveness, and implementation complexity.

## Common Misconceptions
Static binding is always better (dynamic binding enables reflection and metaprogramming). Binding is separate from scoping (binding is what scoping rules determine).

## Explainer

From your study of scope and binding resolution, you understand that when a program uses a name like `x`, the compiler or interpreter must figure out which declaration that name refers to. **Name binding** is the mechanism that creates this association between a name and the entity it denotes — a variable, function, type, or module. The strategy a language uses for binding has far-reaching consequences for performance, safety, and expressiveness.

**Static binding** (also called early binding) resolves all names at compile time. When the compiler encounters a variable reference, it walks the scope chain determined by the program's lexical structure and locks in the binding before execution begins. This means every use of a name is resolved to a fixed memory location or symbol table entry. The advantage is speed — there is no lookup cost at runtime — and safety, because the compiler can catch undeclared variables, type mismatches, and ambiguous references before the program ever runs. Languages like C, Java, and Rust rely almost entirely on static binding.

**Dynamic binding** (also called late binding) defers name resolution to runtime. When the interpreter encounters a name, it searches the current call stack or environment at that moment to find a matching declaration. This means the same textual name in the same function can refer to different variables depending on who called the function and what names are in scope at call time. Early Lisp dialects used dynamic binding by default, and languages like Python and JavaScript use it selectively — for example, method dispatch in Python resolves at runtime based on the actual object's type, not the declared type. Dynamic binding enables powerful metaprogramming patterns like monkey-patching and runtime reflection, but it makes programs harder to reason about statically and prevents many compile-time optimizations.

Most modern languages use a hybrid approach. Local variables and function calls are statically bound for performance and correctness, while features like virtual method dispatch, dynamic module loading, and reflection introduce controlled dynamic binding where flexibility is needed. Understanding where a language draws this line helps you predict both its runtime characteristics and the kinds of errors its compiler can catch. When implementing a language, the binding strategy shapes nearly every part of the compiler: the symbol table design, the code generator's ability to emit direct references versus indirect lookups, and the kinds of optimizations that are sound to apply.
