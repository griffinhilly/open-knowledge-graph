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
status: validated
---

# The Visitor Pattern for AST Traversal

## Core Idea
The visitor pattern decouples tree traversal from node operations: each visitor defines an operation (pretty-printing, type-checking, code generation) without modifying AST classes. This keeps the AST stable while allowing new operations to be added independently, following the open/closed principle.

## Questions

```yaml
- question: "A compiler team needs to add a new constant-folding optimization pass that walks the AST. They use the visitor pattern. What does adding this pass require?"
  type: multiple-choice
  options:
    - "Modifying every existing AST node class to add the folding logic"
    - "Writing one new ConstantFoldVisitor class that implements the visitor interface, without touching any existing AST classes"
    - "Rewriting the parser to produce a different AST structure suited to optimization"
    - "Adding a new method to the Visitor interface and updating all existing visitor classes"
  answer: 1
  explanation: "This is the core benefit of the visitor pattern. New operations become new visitor classes — the AST node classes stay unchanged. Option A is exactly what the visitor pattern avoids: without it, every pass would require modifying every AST node class. Option D confuses adding a new operation (new visitor class) with adding a new node type, which would indeed require updating the interface and all existing visitors."

- question: "What is 'double dispatch' in the visitor pattern, and why is it necessary?"
  type: multiple-choice
  options:
    - "Dispatching to a method twice to handle recursive tree traversal efficiently"
    - "Selecting which visit method to execute based on both the runtime type of the visitor and the runtime type of the AST node"
    - "Calling accept() twice per node to support both pre-order and post-order traversal"
    - "Using two interfaces — Visitor and Visitable — to decouple the tree from operations"
  answer: 1
  explanation: "In most object-oriented languages, method dispatch is single: the method called depends on the runtime type of one object (the receiver). The visitor pattern achieves double dispatch by combining two single dispatches: when a node's accept(visitor) method calls visitor.visitBinaryExpr(this), the first dispatch selects the right accept() method based on the node type, and the second dispatch selects the right visit method based on the visitor type. This means the same node object, visited by a TypeCheckVisitor vs. a PrettyPrintVisitor, executes completely different logic — without requiring if/instanceof chains."

- question: "The visitor pattern makes it easy to add new AST node types without modifying any existing code."
  type: true-false
  answer: false
  explanation: "This is the classic tradeoff inverted. The visitor pattern makes it easy to add new *operations* (new visitor classes) without touching existing code. But adding a new AST node type requires updating the Visitor interface with a new visit method, which then forces every existing visitor class to implement that method. This is the 'expression problem' tradeoff: the visitor pattern optimizes for extensibility across operations at the cost of extensibility across types. It works best when node types are stable but operations grow — exactly the typical compiler development trajectory."

- question: "In the visitor pattern, each visitor controls the order in which it traverses child nodes by deciding when and whether to call child.accept(this) within its own visit methods."
  type: true-false
  answer: true
  explanation: "Traversal order is not fixed by the pattern — it is determined inside each visit method. A type-checking visitor might do post-order traversal (process children before parent, so types are known bottom-up). A pretty-printing visitor might do in-order traversal for binary expressions (left operand, operator, right operand). The visitor pattern gives each pass full flexibility to walk the tree however its semantics require, which is a significant advantage over traversal approaches that impose a fixed order."

- question: "Why does the visitor pattern work best when the set of AST node types is stable, and what goes wrong if node types frequently change?"
  type: short-answer
  answer: "Each time a new AST node type is added, the Visitor interface must gain a new visit method, and every existing visitor class must implement it. In a compiler with many passes (type checking, optimization, several code generation backends, debugging tools), this means touching many files for every grammar change. The visitor pattern trades extensibility across types for extensibility across operations. When the grammar is settled — which is normal once a language is mature — this tradeoff is favorable, because new optimization passes can be added without touching the AST at all."
  explanation: "This tension is sometimes called the 'expression problem.' The visitor pattern solves half of it: easy to add operations, hard to add types. The alternative (putting all operation logic directly in node classes) solves the other half: easy to add types, hard to add operations. Compilers typically settle on the visitor pattern because grammars stabilize before the tooling around them does."
```

## Explainer

You already know that an **abstract syntax tree** is the central data structure a compiler builds after parsing — it represents the hierarchical structure of the source program with nodes for expressions, statements, declarations, and so on. You also know from studying compiler phases that many different passes need to walk this tree: type-checking examines every expression to verify types are consistent, code generation translates each node into target instructions, an optimizer might look for constant expressions to simplify. The naive approach is to add a method for each operation directly to each AST node class — but this quickly becomes unmanageable as the number of operations grows, and it violates the principle that the AST's structure should remain stable across compiler phases.

The **visitor pattern** solves this by separating "what to do at each node" from "how to traverse the tree." You define a Visitor interface (or abstract class) with one method per AST node type: `visitBinaryExpr`, `visitIfStatement`, `visitFunctionDecl`, and so on. Each AST node class gets a single method — conventionally called `accept` — that takes a visitor and calls the appropriate visit method on it: `visitor.visitBinaryExpr(this)`. This is **double dispatch**: the specific operation executed depends on both the type of the visitor and the type of the node. To add a new compiler pass, you write a new visitor class implementing the interface. The AST classes never change.

In practice, a concrete visitor like a `TypeCheckVisitor` implements each visit method with the logic for that pass. When `visitBinaryExpr` is called with a binary expression node, the type checker first recursively visits the left and right children (by calling `left.accept(this)` and `right.accept(this)`), then checks that the operand types are compatible with the operator. A `PrettyPrintVisitor` for the same node would instead recursively print the left operand, print the operator symbol, and print the right operand. The traversal order — pre-order, post-order, or a custom mix — is controlled within the visit methods themselves, giving each pass full flexibility over how it walks the tree.

The tradeoff is the classic tension between extending operations and extending data types. The visitor pattern makes it trivial to add new operations (new visitors) without touching existing code. But adding a new AST node type requires updating every existing visitor with a new visit method, which can be painful in a compiler with many passes. This is why the pattern works best when the set of node types is relatively stable — which is usually true for a language's AST once the grammar is settled — and the set of operations grows over time, which is exactly what happens as a compiler matures and gains new optimization passes, analysis tools, and code generation backends.
