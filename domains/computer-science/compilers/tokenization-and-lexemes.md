---
id: tokenization-and-lexemes
title: Tokenization and Lexemes
domain: computer-science
course: compilers
prerequisites:
- id: regular-expressions-formal
  type: hard
- id: string-basics
  type: hard
builds-toward:
- lexical-analyzer-design
tags:
- lexical-analysis
- tokenization
- input-processing
stage: advanced
status: draft
---

# Tokenization and Lexemes

## Core Idea
Tokenization is the process of converting a source code string into a sequence of tokens (lexemes). Each token represents the smallest meaningful unit of a program: keywords, identifiers, operators, literals. Regular expressions define patterns for each token type, and the lexer matches input against these patterns to classify characters into tokens.
