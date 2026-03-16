---
id: abstract-syntax-trees
title: Abstract Syntax Trees (ASTs)
domain: computer-science
course: compilers
prerequisites:
- id: context-free-grammars-compiler-design
  type: hard
- id: tree-traversals
  type: hard
- id: formal-languages-and-strings
  type: soft
- id: set-fundamentals
  type: soft
builds-toward:
- tree-walking-interpreters
- semantic-analysis
tags:
- ast
- intermediate-representation
- syntax-trees
stage: advanced
status: draft
---

# Abstract Syntax Trees (ASTs)

## Core Idea
An abstract syntax tree (AST) is a condensed parse tree that retains syntactic structure but omits punctuation and formatting. Internal nodes represent language constructs (expressions, statements, declarations); leaves are tokens. ASTs are easier to traverse and analyze than full parse trees. Compilers typically convert parse trees to ASTs before semantic analysis and code generation.

## Questions

```yaml
- question: "Which of the following is present in a concrete parse tree but typically absent from an AST for the same source code?"
  type: multiple-choice
  options:
    - "A node representing a function call expression"
    - "Parenthesis tokens used to group a sub-expression like (a + b)"
    - "A node for a binary addition operation"
    - "Leaf nodes for variable names"
  answer: 1
  explanation: "ASTs are 'abstract' because they strip away concrete syntax details — punctuation like parentheses, semicolons, and delimiter keywords that only exist to guide the parser are omitted. Grouping is encoded structurally by nesting: (a + b) * c and a + b * c produce different AST shapes without needing explicit parenthesis nodes. The parse tree records every terminal symbol including punctuation; the AST does not."

- question: "The source expressions `(a + b)` and `a + b` will produce different ASTs because they have different surface syntax."
  type: true-false
  answer: false
  explanation: "The whole point of 'abstracting' away from concrete syntax is that semantically equivalent expressions produce identical ASTs. Both `(a + b)` and `a + b` represent the same binary addition and generate the same AST node: a '+' node with children 'a' and 'b'. The parentheses affect the parse tree (which tracks concrete tokens) but not the AST (which captures meaning). This is precisely why compilers use ASTs rather than parse trees for subsequent analysis."

- question: "What information does a function-call AST node typically need to store, and why is each piece necessary for later compilation phases?"
  type: short-answer
  answer: "A function-call node typically stores the callee (function name or expression being called), the list of argument sub-expressions, and source-location metadata. The callee is needed for name resolution and type-checking during semantic analysis. The argument list is needed to verify arity and argument types, and to generate the calling convention during code generation. Source location enables precise error reporting at every phase."
  explanation: "AST node design is driven by downstream requirements: each field exists because a specific later phase needs it. This illustrates why AST design is an architectural decision — compilers often add fields to AST nodes incrementally as they discover what information semantic analysis, optimization, and code generation require."
```

## Explainer

When a parser processes source code it produces a *concrete syntax tree* (or parse tree) that mirrors the grammar rules exactly — every matched rule becomes a node, and every token becomes a leaf, including parentheses, semicolons, commas, and keywords like `if` and `then`. This is useful for verifying that the input is syntactically valid, but it is cluttered with structure that carries no semantic meaning. An *abstract syntax tree* strips all of that away, keeping only the information that matters for what the compiler needs to do next.

The key principle is that grouping and punctuation are implied by *tree structure*, not by explicit nodes. In a concrete parse tree, `(a + b) * c` might have a node for the parentheses and a node for the grouping rule around `a + b`. In the AST, those are replaced by a single multiplication node whose left child is an addition node with children `a` and `b`. The tree shape itself encodes the grouping — no parenthesis node is needed. This is what "abstract" means: the essential logical structure, without syntactic noise.

Internal AST nodes represent language constructs: binary operators, function calls, if-statements, variable declarations, loops. Leaf nodes are the atomic values: literals, variable names, type names. Because the tree closely mirrors the logical structure of the program (rather than the grammar rules used to parse it), later passes can traverse it with simple recursive algorithms. A type-checker walks the tree bottom-up, attaching types to each node. A code generator walks it recursively, emitting instructions for each subtree. Tree traversal patterns from your data-structures course — pre-order, post-order, visitor — apply directly.

An important design question is how much information each AST node should carry. A minimal node stores only what the grammar captured. In practice, nodes get annotated with additional data as compilation progresses: the semantic analysis phase attaches resolved type information and symbol-table references to each identifier node; the optimization phase may attach cost estimates; the code generation phase may attach register assignments. Many compilers use a single AST enriched across phases rather than building a new data structure at each step.

Understanding ASTs is also directly useful outside traditional compilers. Linters, formatters, refactoring tools, static analyzers, and transpilers all operate on ASTs. When you use a tool that renames a variable across a codebase without breaking unrelated strings, or that reformats code while preserving semantics, it is almost certainly parsing source into an AST, transforming the tree, and pretty-printing the result. The AST is the universal intermediate language for any tool that needs to understand and manipulate code.
