---
id: scope-binding-resolution
title: Scope and Binding Resolution
domain: computer-science
course: compilers
prerequisites:
- id: semantic-analysis
  type: hard
- id: symbol-tables-and-scope
  type: hard
builds-toward:
- name-binding-strategies
tags:
- scoping
- name-resolution
- binding
stage: advanced
status: draft
---

# Scope and Binding Resolution

## Core Idea
Scope determines which declarations are visible at each program point. Scope resolution maps uses to declarations by walking scope hierarchies, handling shadowing, and checking access rules. Different languages have different scoping rules (static vs dynamic, lexical vs block scope).

## How It's Best Learned
Implement scope resolution for nested scopes with shadowing. Trace name lookups manually through complex scope structures.

## Common Misconceptions
Scope can always be resolved in a single pass (some languages require multiple passes or context from type inference). Symbol tables must be flat (hierarchical or chained tables handle nesting more naturally).

## Explainer

From your work with semantic analysis and symbol tables, you know that the compiler maintains a mapping from names to their declarations, and that programs organize names into nested regions of visibility. **Scope and binding resolution** is the process of connecting each use of a name in the source code to the specific declaration it refers to — the step that turns a bare identifier like `x` into a reference to a particular variable, function, or type with known properties.

The most common model is **lexical (static) scoping**, where a name's meaning is determined by its textual position in the source code. When the compiler encounters a use of `x`, it searches the innermost enclosing scope first, then the next outer scope, and so on until it either finds a declaration or reports an error. This is implemented with a **scope stack** or **chained symbol tables**: each time the compiler enters a new block, function, or class, it pushes a new scope onto the stack; when it exits, it pops the scope. A lookup walks from the top of the stack downward, and the first match wins. This is why an inner variable named `x` **shadows** an outer one — the search finds the inner declaration first and stops.

Real languages add layers of complexity to this basic model. **Shadowing** must be tracked so the compiler can warn about potentially confusing redefinitions. **Forward references** — where a name is used before it is declared, common in mutually recursive functions — require either a second pass or a "declare-then-define" protocol. **Access rules** like `private`, `protected`, and `public` in class hierarchies add visibility constraints on top of scope: a name might exist in an enclosing scope but be inaccessible due to its access modifier. **Overloading** means a single name may map to multiple declarations, and the compiler must use type information to disambiguate. Languages with **dynamic scoping** (rare, but present in some Lisps and shell languages) resolve names based on the call stack at runtime rather than the textual nesting, which makes resolution a runtime rather than compile-time operation.

The practical implementation typically involves building the scope structure during a dedicated pass (or as part of the AST-walking semantic analysis phase) and annotating each name-use node in the AST with a pointer to its resolved declaration. Once resolution is complete, later compiler phases — type checking, code generation — never need to perform name lookups again. They simply follow the resolved pointers. Getting scope resolution right is essential because every downstream analysis depends on knowing exactly which declaration each name refers to: a type error, an incorrect optimization, or a wrong code emission can all trace back to a binding resolution mistake.
