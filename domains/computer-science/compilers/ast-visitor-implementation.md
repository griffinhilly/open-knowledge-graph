---
id: ast-visitor-implementation
title: The Visitor Pattern for AST Traversal
domain: computer-science
course: compilers
prerequisites:
- id: abstract-syntax-trees
  type: hard
- id: compiler-phases-and-organization
  type: hard
builds-toward:
- type-reconstruction-algorithms
tags:
- design-patterns
- AST
- semantics
stage: advanced
status: draft
---

# The Visitor Pattern for AST Traversal

## Core Idea
The visitor pattern decouples tree traversal from node operations: each visitor defines an operation (pretty-printing, type-checking, code generation) without modifying AST classes. This keeps the AST stable while allowing new operations to be added independently, following the open/closed principle.

## Explainer

You already know that an **abstract syntax tree** is the central data structure a compiler builds after parsing — it represents the hierarchical structure of the source program with nodes for expressions, statements, declarations, and so on. You also know from studying compiler phases that many different passes need to walk this tree: type-checking examines every expression to verify types are consistent, code generation translates each node into target instructions, an optimizer might look for constant expressions to simplify. The naive approach is to add a method for each operation directly to each AST node class — but this quickly becomes unmanageable as the number of operations grows, and it violates the principle that the AST's structure should remain stable across compiler phases.

The **visitor pattern** solves this by separating "what to do at each node" from "how to traverse the tree." You define a Visitor interface (or abstract class) with one method per AST node type: `visitBinaryExpr`, `visitIfStatement`, `visitFunctionDecl`, and so on. Each AST node class gets a single method — conventionally called `accept` — that takes a visitor and calls the appropriate visit method on it: `visitor.visitBinaryExpr(this)`. This is **double dispatch**: the specific operation executed depends on both the type of the visitor and the type of the node. To add a new compiler pass, you write a new visitor class implementing the interface. The AST classes never change.

In practice, a concrete visitor like a `TypeCheckVisitor` implements each visit method with the logic for that pass. When `visitBinaryExpr` is called with a binary expression node, the type checker first recursively visits the left and right children (by calling `left.accept(this)` and `right.accept(this)`), then checks that the operand types are compatible with the operator. A `PrettyPrintVisitor` for the same node would instead recursively print the left operand, print the operator symbol, and print the right operand. The traversal order — pre-order, post-order, or a custom mix — is controlled within the visit methods themselves, giving each pass full flexibility over how it walks the tree.

The tradeoff is the classic tension between extending operations and extending data types. The visitor pattern makes it trivial to add new operations (new visitors) without touching existing code. But adding a new AST node type requires updating every existing visitor with a new visit method, which can be painful in a compiler with many passes. This is why the pattern works best when the set of node types is relatively stable — which is usually true for a language's AST once the grammar is settled — and the set of operations grows over time, which is exactly what happens as a compiler matures and gains new optimization passes, analysis tools, and code generation backends.
