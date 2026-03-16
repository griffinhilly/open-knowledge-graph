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

## Explainer

Source code as written by a programmer is just a stream of characters — letters, digits, spaces, punctuation. Before a compiler can understand the structure of a program, it needs to group those characters into meaningful chunks. This is what **tokenization** (also called lexical analysis or scanning) does: it reads the raw character stream and produces a sequence of **tokens**, each labeled with a type and carrying the original text. Given the input `if (x >= 42)`, a tokenizer produces something like: `[KEYWORD:"if", LPAREN:"(", IDENT:"x", GE:">=", INT_LIT:"42", RPAREN:")"]`.

The terminology can be confusing, so here is the precise distinction. A **lexeme** is the actual substring of source code that was matched — for instance, `">="`or `"42"`. A **token** is the lexeme paired with its category — `GE` for the greater-than-or-equal operator, `INT_LIT` for an integer literal. Some token types have many possible lexemes (every variable name is an `IDENT`), while others have exactly one (`>=` is always `GE`). The tokenizer's job is to decide where each lexeme begins and ends, and which category it belongs to.

Your prerequisite knowledge of **regular expressions** is directly applied here. Each token type is defined by a regex pattern: identifiers might match `[a-zA-Z_][a-zA-Z0-9_]*`, integer literals match `[0-9]+`, and so on. The tokenizer tries all patterns at the current position in the input and picks the one that matches the longest prefix — this is the **longest match rule**. When two patterns match the same length (like `if` matching both the keyword pattern and the identifier pattern), a **priority rule** breaks the tie, typically favoring keywords over identifiers. These two rules — longest match and priority — are enough to make tokenization unambiguous for most programming languages.

Tokenization also handles the parts of source code that carry no semantic meaning: **whitespace** and **comments** are consumed but typically not emitted as tokens (though some compilers preserve them for formatting tools or documentation generators). This stripping is what makes subsequent phases simpler — the parser never has to worry about spaces between tokens or comments interrupting expressions. The output of tokenization is a clean, linear sequence of meaningful tokens that the parser can process using the grammar rules you will study next.
