---
id: tree-walking-interpreters
title: Tree-Walking Interpreters
domain: computer-science
course: compilers
prerequisites:
- id: abstract-syntax-trees
  type: hard
- id: recursion-basics
  type: hard
builds-toward:
- type-inference-algorithms
tags:
- interpreters
- execution
- ast-traversal
stage: advanced
status: draft
---

# Tree-Walking Interpreters

## Core Idea
A tree-walking interpreter executes a program by recursively traversing its AST, evaluating each node according to language semantics. Evaluation of an expression node typically involves evaluating its children and applying an operation. Tree-walking is simple to implement but slower than compiled execution. It's useful for prototyping languages and understanding semantics.

## Explainer

You already know how to parse source code into an abstract syntax tree, and you understand how recursion can process tree structures by handling base cases and recursive cases. A **tree-walking interpreter** combines these two ideas directly: it takes the AST produced by the parser and executes the program by walking the tree, evaluating each node on the spot. There is no compilation step, no intermediate bytecode, no machine code generation — the AST *is* the executable representation.

The core of a tree-walking interpreter is an `eval` function that takes an AST node and an environment (a mapping from variable names to their current values) and returns a result. The function dispatches on the node type. For a number literal node, it simply returns the number. For a binary operation like `3 + 4`, it recursively evaluates the left child (getting 3), recursively evaluates the right child (getting 4), then applies the `+` operator to produce 7. For variable references, it looks up the name in the environment. For assignment statements, it evaluates the right-hand side and updates the environment. For `if` statements, it evaluates the condition, then recursively evaluates either the then-branch or the else-branch. Every language construct maps to a case in this recursive function.

The environment is where things get interesting. A simple flat dictionary works for global variables, but once you add functions and local scope, you need a chain of environments — each function call creates a new environment that points back to its enclosing scope. When looking up a variable, the interpreter walks this chain from the innermost scope outward until it finds a match. This is lexical scoping implemented at runtime, and it is both elegantly simple and easy to get right. Function calls work by creating a new environment, binding the arguments to the parameter names, and evaluating the function body in that new environment. The return value becomes the result of the call expression.

The tradeoff of tree-walking is performance. Every operation requires navigating pointer-based tree nodes, dispatching on node types, and managing environment chains — overhead that compiled code avoids entirely. A compiled `3 + 4` becomes a single machine instruction; a tree-walked `3 + 4` involves allocating node objects, recursive function calls, and type dispatch. For this reason, production language implementations almost always compile to bytecode or machine code. But tree-walking interpreters are invaluable for prototyping a new language, testing language semantics, building scripting engines where startup time matters more than throughput, and understanding how programming languages work at a fundamental level. If you can write a tree-walking interpreter for a language, you understand that language's semantics completely.
