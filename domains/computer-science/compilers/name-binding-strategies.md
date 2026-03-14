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
