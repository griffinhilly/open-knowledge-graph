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

## Explainer

From your work with abstract syntax trees, you know that an AST captures the hierarchical structure of a program — expressions contain subexpressions, statements contain expressions, functions contain statements. But knowing *what* an AST represents leaves open the question of *how* to represent it in memory. **AST node representation** is the set of design decisions that determine how each node stores its type, its children, and any associated data (like the name of a variable or the value of a literal). These decisions ripple through every compiler pass that touches the tree.

The most common approach in object-oriented languages is a **class hierarchy**: a base `ASTNode` class with subclasses like `BinaryExpr`, `IfStatement`, and `FunctionDecl`. Each subclass has fields specific to its node type — a `BinaryExpr` stores an operator and two child expression nodes, while an `IfStatement` stores a condition, a then-branch, and an optional else-branch. This is clean and extensible, but it scatters node types across many classes, and adding a new operation over the tree (like a type-checking pass) requires modifying every class or using the visitor pattern. In functional languages, **algebraic data types** (also called variant types or tagged unions) are the natural choice: you define `Expr = Literal Int | BinOp Op Expr Expr | Var String | ...` and pattern-match exhaustively. The compiler enforces that you handle every case, catching bugs at compile time.

A subtler decision is what *not* to include in the AST. The parser's concrete syntax tree mirrors the grammar exactly, including parentheses, semicolons, and syntactic sugar like `x += 1`. The AST abstracts these away: parentheses are implicit in tree structure, semicolons are irrelevant, and `x += 1` becomes an assignment of `x + 1` to `x`. This simplification is what makes the AST "abstract" — every downstream pass works with a cleaner, more uniform structure. However, if your compiler must produce good error messages or support source-level refactoring tools, you may need to preserve source locations (line and column numbers) and sometimes even formatting information on each node, which adds memory overhead.

Performance matters more than it might seem. A compiler for a large codebase may construct millions of AST nodes. Choices like whether nodes are heap-allocated individually (flexible but memory-heavy) or packed into arena allocators (cache-friendly but less flexible), whether children are stored as pointers or indices into a flat array, and whether nodes carry inline data or point to side tables all affect traversal speed and memory footprint. Production compilers like Clang and the Rust compiler invest heavily in AST representation precisely because every subsequent pass — name resolution, type checking, optimization, code generation — must walk this structure, and the representation's efficiency compounds across every pass.
