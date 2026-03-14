---
id: context-free-grammars-compiler-design
title: Context-Free Grammars in Compiler Design
domain: computer-science
course: compilers
prerequisites:
- id: context-free-grammars
  type: hard
- id: parse-trees-derivations
  type: hard
builds-toward:
- parsing-problem-overview
- abstract-syntax-trees
tags:
- grammar
- parsing
- language-definition
stage: advanced
status: draft
---

# Context-Free Grammars in Compiler Design

## Core Idea
Context-free grammars formally describe the syntax of programming languages. Each grammar rule specifies how nonterminals can be rewritten into terminals and nonterminals. A parse tree derives a sentence by applying rules recursively; the tree structure encodes the program's grammatical composition. CFGs are expressive enough for most language constructs but leave semantics to later compilation phases.
