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
builds-toward: []
tags:
- scoping
- name-resolution
- binding
stage: advanced
status: validated
---

# Scope and Binding Resolution

## Core Idea
Scope determines which declarations are visible at each program point. Scope resolution maps uses to declarations by walking scope hierarchies, handling shadowing, and checking access rules. Different languages have different scoping rules (static vs dynamic, lexical vs block scope).

## How It's Best Learned
Implement scope resolution for nested scopes with shadowing. Trace name lookups manually through complex scope structures.

## Common Misconceptions
Scope can always be resolved in a single pass (some languages require multiple passes or context from type inference). Symbol tables must be flat (hierarchical or chained tables handle nesting more naturally).

## Questions

```yaml
- question: "Consider this pseudocode: x = 10 is defined globally, then a function outer() defines x = 20 and calls an inner function inner() which prints x. inner() prints 20, not 10. Which principle explains this?"
  type: multiple-choice
  options:
    - "Dynamic scoping — x is resolved at runtime by scanning the call stack for the most recent assignment"
    - "Lexical (static) scoping — the compiler searches outward from the innermost enclosing scope; outer's x = 20 is found before the global x = 10"
    - "Flat symbol tables — only one x can exist per program, so the most recently written value is used"
    - "Forward reference resolution — the compiler always uses the last assignment to x anywhere in the program"
  answer: 1
  explanation: "In lexical scoping, name lookup starts at the immediately enclosing scope and walks outward. When inner() looks up x, it finds outer()'s x = 20 before reaching the global scope — so 20 is printed. This is static because the lookup path is determined entirely by the textual structure of the program, not by how it runs. Dynamic scoping would also print 20 here (since outer() called inner()), but the reason is different — dynamic scoping follows the call stack, not textual nesting, and gives different results in other call patterns."

- question: "A language allows two mutually recursive functions — A calls B, and B calls A — declared in the same scope, with A defined before B. What special handling does this require during scope resolution?"
  type: multiple-choice
  options:
    - "None — a single forward pass handles all name uses automatically"
    - "Either a two-pass approach or a declare-then-define protocol, because when A is being processed, B has not yet been declared and the forward reference cannot be resolved in one pass"
    - "Dynamic scoping, because the mutual call order cannot be determined at compile time"
    - "Flat symbol tables, so both functions share a global namespace and see each other immediately"
  answer: 1
  explanation: "When function A is processed and contains a call to B, B has not yet appeared in the source. In a single-pass compiler, B is simply unknown at that point. Solutions include: (1) a two-pass approach where the first pass registers all top-level declarations and the second resolves uses; or (2) a declare-then-define protocol where the compiler accepts a forward declaration of B's signature before seeing its body. Neither flat tables nor dynamic scoping solves the problem — they change where names are stored or when resolution happens, but the forward reference still needs to be handled explicitly."

- question: "In a language with lexical scoping, declaring a variable with the same name as an outer-scope variable inside an inner scope causes the inner declaration to shadow the outer one during name lookup."
  type: true-false
  answer: true
  explanation: "Shadowing is a direct consequence of how scope stacks work. When the compiler looks up a name, it starts at the innermost (most recently pushed) scope and walks outward. The first match wins. An inner declaration with the same name is found before the outer one, so the outer variable is inaccessible by that name within the inner scope. This is intentional — it allows inner scopes to introduce local bindings without breaking outer code — but it can cause subtle bugs when the shadowing is accidental."

- question: "After scope resolution is complete, later compiler phases such as type checking and code generation must re-perform name lookups to ensure they reference the correct declarations."
  type: true-false
  answer: false
  explanation: "The purpose of scope resolution is precisely to eliminate repeated lookups. Each name-use node in the AST is annotated with a direct pointer to its resolved declaration during the resolution phase. Later phases — type checking, optimization, code generation — follow these stored pointers rather than re-walking the scope hierarchy. This makes subsequent phases simpler, faster, and correct by construction: the resolved binding is an immutable fact recorded in the AST. Re-doing lookups would be redundant and could introduce inconsistencies if the scope structure changed between phases."

- question: "What is the difference between lexical (static) scoping and dynamic scoping, and why does the distinction matter for compiler design?"
  type: short-answer
  answer: "In lexical scoping, a name's binding is determined by its textual position in the source code — the compiler searches outward through the textually enclosing scopes at compile time. In dynamic scoping, a name is resolved by searching the call stack at runtime — the most recently active binding in the call chain wins. Lexical scoping can be fully resolved at compile time, allowing the compiler to annotate each name-use with a static pointer to its declaration; code generation is straightforward. Dynamic scoping requires a runtime lookup mechanism (often a global association list or per-thread stack), which is slower and harder to reason about. Most modern languages (Python, Java, C, Haskell) use lexical scoping; dynamic scoping survives in some Lisps (for special variables) and shell scripts."
  explanation: "The compiler design implication is significant: lexical scoping lets the compiler 'freeze' all name bindings into the AST before generating code, so downstream phases never need name lookups. Dynamic scoping defers this work to runtime, which means code generation must emit lookup instructions, and the type checker cannot statically verify which declaration a name refers to without whole-program analysis."
```

## Explainer

From your work with semantic analysis and symbol tables, you know that the compiler maintains a mapping from names to their declarations, and that programs organize names into nested regions of visibility. **Scope and binding resolution** is the process of connecting each use of a name in the source code to the specific declaration it refers to — the step that turns a bare identifier like `x` into a reference to a particular variable, function, or type with known properties.

The most common model is **lexical (static) scoping**, where a name's meaning is determined by its textual position in the source code. When the compiler encounters a use of `x`, it searches the innermost enclosing scope first, then the next outer scope, and so on until it either finds a declaration or reports an error. This is implemented with a **scope stack** or **chained symbol tables**: each time the compiler enters a new block, function, or class, it pushes a new scope onto the stack; when it exits, it pops the scope. A lookup walks from the top of the stack downward, and the first match wins. This is why an inner variable named `x` **shadows** an outer one — the search finds the inner declaration first and stops.

Real languages add layers of complexity to this basic model. **Shadowing** must be tracked so the compiler can warn about potentially confusing redefinitions. **Forward references** — where a name is used before it is declared, common in mutually recursive functions — require either a second pass or a "declare-then-define" protocol. **Access rules** like `private`, `protected`, and `public` in class hierarchies add visibility constraints on top of scope: a name might exist in an enclosing scope but be inaccessible due to its access modifier. **Overloading** means a single name may map to multiple declarations, and the compiler must use type information to disambiguate. Languages with **dynamic scoping** (rare, but present in some Lisps and shell languages) resolve names based on the call stack at runtime rather than the textual nesting, which makes resolution a runtime rather than compile-time operation.

The practical implementation typically involves building the scope structure during a dedicated pass (or as part of the AST-walking semantic analysis phase) and annotating each name-use node in the AST with a pointer to its resolved declaration. Once resolution is complete, later compiler phases — type checking, code generation — never need to perform name lookups again. They simply follow the resolved pointers. Getting scope resolution right is essential because every downstream analysis depends on knowing exactly which declaration each name refers to: a type error, an incorrect optimization, or a wrong code emission can all trace back to a binding resolution mistake.
