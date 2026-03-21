---
id: ast-node-representation
title: AST Node Representation
domain: computer-science
course: compilers
prerequisites:
- id: abstract-syntax-trees
  type: hard
- id: recursion-basics
  type: hard
builds-toward:
- attribute-grammar-framework
tags:
- ast
- data-structures
- representation
stage: advanced
status: draft
---

# AST Node Representation

## Core Idea
AST nodes must efficiently represent program structure and support traversal, annotation, and transformation. Node representation choices—classes, variant types, tagged unions—affect memory, performance, and pattern matching.

## How It's Best Learned
Implement AST nodes using different strategies (classes vs unions vs tagged pointers). Measure memory and traversal performance differences.

## Common Misconceptions
AST design is obvious (it is actually a key design decision). ASTs should mirror the grammar exactly (often they abstract away syntactic sugar).

## Questions

```yaml
- question: "A parser produces a tree for the statement x += 1. How should a well-designed AST represent this statement, compared to the parser's concrete syntax tree?"
  type: multiple-choice
  options:
    - "Identically — the AST should preserve all syntactic details including the += operator to accurately represent the source"
    - "As an assignment node where the right-hand side is x + 1 — abstracting the syntactic sugar x += 1 into its semantic equivalent"
    - "As a single terminal node containing the string 'x += 1', since operator precedence is handled by later passes"
    - "As a binary expression node with x and 1 as children, omitting the = since it is implied by the assignment context"
  answer: 1
  explanation: "The AST's job is to represent semantic structure, not syntactic form. x += 1 is syntactic sugar for x = x + 1. An AST that keeps the += node forces every downstream pass (type checker, optimizer, code generator) to handle a special case that is semantically identical to a plain assignment. By desugaring to an assignment of a binary addition, the AST gives every subsequent pass a simpler, more uniform structure. This is the 'abstract' in 'abstract syntax tree' — it abstracts away syntactic variations that don't change meaning."

- question: "A compiler team is adding a new pass: constant folding (evaluating constant expressions at compile time). Which AST representation strategy makes this easiest to implement correctly?"
  type: multiple-choice
  options:
    - "Class hierarchy — you can add a new ConstantFoldingVisitor class without touching existing node classes"
    - "Class hierarchy — you add a constantFold() method to the base ASTNode class and override it in each subclass"
    - "Algebraic data types — pattern matching forces exhaustive case analysis, catching at compile time if any node type lacks a constant-folding rule"
    - "Tagged unions in C — the explicit tag field makes it easy to switch over all node types"
  answer: 2
  explanation: "Algebraic data types (sum types) are the best fit for adding new operations over a fixed set of node types. When you pattern match over an ADT, the compiler enforces exhaustiveness — if you add a new node type later, every existing pattern match that doesn't handle it becomes a compile error. This catches bugs at compile time rather than runtime. With a class hierarchy, adding a new operation like constant folding requires either modifying every subclass (violating open/closed principles) or implementing the Visitor pattern, which is more indirect. The tradeoff is reversed for adding new node types: easy with class hierarchy, hard with ADTs."

- question: "An AST should mirror the grammar rules exactly, preserving all concrete syntax (parentheses, semicolons, operator sugar) to ensure no information is lost."
  type: true-false
  answer: false
  explanation: "This describes a concrete syntax tree (parse tree), not an AST. The AST deliberately discards syntactically irrelevant information: parentheses are implicit in tree structure, semicolons are artifacts of syntax not semantics, and syntactic sugar like x++ or x += 1 is desugared to its semantic equivalent. This abstraction is the point — every compiler pass after parsing operates on a cleaner, more uniform structure without handling redundant syntactic variants. The 'abstract' in AST means abstracting from surface syntax to semantic structure. Source location and formatting information may need to be stored separately as annotations if error messages or refactoring tools need it."

- question: "Preserving source location information (line and column numbers) on AST nodes adds memory overhead but is important for error messages and source-level tooling."
  type: true-false
  answer: true
  explanation: "When a type error occurs in a 10,000-line program, the compiler must report which line caused it — this requires mapping AST nodes back to their source positions. Similarly, IDE features like 'go to definition', refactoring tools, and debuggers all need accurate source location data. This information is not semantically needed for compilation itself, but it is essential for the developer experience. Production compilers like Clang and the Rust compiler carefully preserve source spans on every AST node precisely for this reason, accepting the memory cost as necessary. The decision of what metadata to attach to nodes is a genuine design tradeoff."

- question: "Why do compiler engineers invest heavily in AST representation even though the AST is an intermediate structure that gets transformed or discarded? What makes the representation choice matter?"
  type: short-answer
  answer: "Every subsequent compiler pass — name resolution, type checking, optimization, code generation — must traverse the AST repeatedly. With millions of nodes in a large codebase, representation choices (heap allocation vs. arena allocation, pointer-based vs. index-based children, inline data vs. side tables) compound across every pass. Cache-friendly layouts reduce memory bandwidth; compact representations reduce GC pressure; well-chosen node types reduce branching. The AST representation is a performance multiplier: a bad choice is paid for on every pass, while a good choice pays dividends across the entire compilation pipeline."
  explanation: "The insight is that efficiency in a compiler is about repeated operations, not one-time costs. An AST built for a production compiler may be visited dozens of times across all passes. Choices that seem minor in isolation — like whether to store a child list inline or as a heap pointer — become significant when multiplied by millions of nodes and dozens of traversals. This is why production compilers like LLVM, Clang, and rustc treat AST representation as a serious engineering concern, using arena allocators, flattened representations, and careful memory layout, rather than the naive 'allocate each node separately on the heap' approach that is simplest to implement."
```

## Explainer

From your work with abstract syntax trees, you know that an AST captures the hierarchical structure of a program — expressions contain subexpressions, statements contain expressions, functions contain statements. But knowing *what* an AST represents leaves open the question of *how* to represent it in memory. **AST node representation** is the set of design decisions that determine how each node stores its type, its children, and any associated data (like the name of a variable or the value of a literal). These decisions ripple through every compiler pass that touches the tree.

The most common approach in object-oriented languages is a **class hierarchy**: a base `ASTNode` class with subclasses like `BinaryExpr`, `IfStatement`, and `FunctionDecl`. Each subclass has fields specific to its node type — a `BinaryExpr` stores an operator and two child expression nodes, while an `IfStatement` stores a condition, a then-branch, and an optional else-branch. This is clean and extensible, but it scatters node types across many classes, and adding a new operation over the tree (like a type-checking pass) requires modifying every class or using the visitor pattern. In functional languages, **algebraic data types** (also called variant types or tagged unions) are the natural choice: you define `Expr = Literal Int | BinOp Op Expr Expr | Var String | ...` and pattern-match exhaustively. The compiler enforces that you handle every case, catching bugs at compile time.

A subtler decision is what *not* to include in the AST. The parser's concrete syntax tree mirrors the grammar exactly, including parentheses, semicolons, and syntactic sugar like `x += 1`. The AST abstracts these away: parentheses are implicit in tree structure, semicolons are irrelevant, and `x += 1` becomes an assignment of `x + 1` to `x`. This simplification is what makes the AST "abstract" — every downstream pass works with a cleaner, more uniform structure. However, if your compiler must produce good error messages or support source-level refactoring tools, you may need to preserve source locations (line and column numbers) and sometimes even formatting information on each node, which adds memory overhead.

Performance matters more than it might seem. A compiler for a large codebase may construct millions of AST nodes. Choices like whether nodes are heap-allocated individually (flexible but memory-heavy) or packed into arena allocators (cache-friendly but less flexible), whether children are stored as pointers or indices into a flat array, and whether nodes carry inline data or point to side tables all affect traversal speed and memory footprint. Production compilers like Clang and the Rust compiler invest heavily in AST representation precisely because every subsequent pass — name resolution, type checking, optimization, code generation — must walk this structure, and the representation's efficiency compounds across every pass.
