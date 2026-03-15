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
