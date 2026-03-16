---
id: parsing-problem-overview
title: The Parsing Problem
domain: computer-science
course: compilers
prerequisites:
- id: context-free-grammars-compiler-design
  type: hard
- id: lexical-analyzer-design
  type: hard
- id: formal-languages-and-strings
  type: soft
builds-toward:
- ll-parsing
- lr-parsing
tags:
- parsing
- syntax-analysis
- problem-formulation
stage: advanced
status: draft
---

# The Parsing Problem

## Core Idea
Syntax analysis (parsing) determines whether a token stream is valid according to a grammar and builds a parse tree or AST. The problem is: given a CFG and input tokens, construct a derivation tree. Not all grammars admit efficient parsing; ambiguous grammars have multiple derivations. Practical parsers require restrictive grammar classes (LL, LR) or disambiguating rules.

## Explainer

The lexical analyzer you already built breaks source code into tokens — identifiers, keywords, operators, literals. But a flat list of tokens says nothing about structure. The expression `3 + 4 * 5` is five tokens, but its meaning depends entirely on how those tokens group: does the multiplication bind tighter than the addition? **Parsing** is the phase that recovers this hierarchical structure from the linear token stream, guided by the rules of a context-free grammar.

Recall that a **context-free grammar** defines a language through production rules: a nonterminal on the left can be replaced by a sequence of terminals and nonterminals on the right. Parsing is the inverse problem — given the terminals (tokens), find a sequence of production applications (a **derivation**) that produces them. The result is a **parse tree** (or its compressed form, an abstract syntax tree) that makes the grammatical structure explicit. For `3 + 4 * 5`, the parse tree shows multiplication nested deeper than addition, capturing the precedence rule encoded in the grammar.

The core difficulty is that not all grammars can be parsed efficiently. A grammar is **ambiguous** if some input has more than one valid parse tree — meaning the grammar assigns two different structures (and potentially two different meanings) to the same program. The classic example is the dangling-else problem: `if a then if b then s1 else s2` can associate the `else` with either `if`. Ambiguity must be resolved, either by rewriting the grammar or by adding disambiguating rules (such as "else binds to the nearest if").

Even unambiguous grammars may require exponential time to parse with a naive algorithm. Practical compilers restrict themselves to grammar subclasses that guarantee linear-time parsing. **LL grammars** are parsed top-down by reading input left-to-right and choosing productions by looking ahead a fixed number of tokens. **LR grammars** are parsed bottom-up by shifting tokens onto a stack and reducing them when a complete right-hand side is recognized. These two families cover nearly all programming language constructs, and the choice between them shapes the entire front end of a compiler. Understanding the parsing problem — what makes it hard, what makes it tractable — is the foundation for studying both approaches.
