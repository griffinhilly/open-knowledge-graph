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
status: validated
---

# Tokenization and Lexemes

## Core Idea
Tokenization is the process of converting a source code string into a sequence of tokens (lexemes). Each token represents the smallest meaningful unit of a program: keywords, identifiers, operators, literals. Regular expressions define patterns for each token type, and the lexer matches input against these patterns to classify characters into tokens.

## Questions

```yaml
- question: "A tokenizer encounters the input `<=`. It has defined patterns: `<` maps to LESS_THAN, and `<=` maps to LESS_EQUAL. Which token does it produce, and why?"
  type: multiple-choice
  options:
    - "Two tokens: LESS_THAN for `<` followed by EQUAL for `=`"
    - "One token: LESS_EQUAL for `<=`, because the longest match rule selects the pattern that matches the most characters"
    - "An error — `<=` is ambiguous because both patterns could apply"
    - "One token: LESS_THAN, because simpler patterns take priority"
  answer: 1
  explanation: "The longest match rule (maximal munch) resolves this: when multiple patterns match at the current position, the tokenizer picks the one that consumes the most characters. `<=` matches two characters, while `<` alone matches only one. So `<=` wins and produces LESS_EQUAL. Without this rule, operators like `<=`, `>=`, `==`, and `!=` would be incorrectly broken into single-character tokens."

- question: "In the tokenized output for the source text `if (count >= 10)`, what is the *lexeme* for the `>=` operator?"
  type: multiple-choice
  options:
    - "GE (the token type name)"
    - "`>=` (the actual two-character substring from source code)"
    - "2 (the character count of the match)"
    - "Both `>=` and GE together — a lexeme is always a type-value pair"
  answer: 1
  explanation: "A lexeme is the raw substring of source text that was matched — in this case, the two characters `>=`. A token is the lexeme *paired with* its category label (GE or GREATER_EQUAL). The distinction matters: many different lexemes can produce the same token type (every variable name like `count`, `total`, `i` produces an IDENTIFIER token), but the lexeme preserves what was actually written so error messages and debugging can refer back to the source."

- question: "The keyword `while` in most programming languages would be tokenized as an IDENTIFIER, because it matches the identifier pattern `[a-zA-Z_][a-zA-Z0-9_]*`."
  type: true-false
  answer: false
  explanation: "When `while` matches both the keyword pattern and the identifier pattern at the same length, the *priority rule* breaks the tie by giving keywords higher priority than identifiers. The resulting token is KEYWORD or WHILE, not IDENTIFIER. This priority rule is essential: without it, every language keyword would be treated as a user-defined variable name, making the language effectively unable to distinguish reserved words from identifiers."

- question: "In most compilers, whitespace and comments between tokens are consumed by the tokenizer but not emitted as tokens in the output sequence."
  type: true-false
  answer: true
  explanation: "This is a fundamental design choice in tokenization: whitespace (spaces, tabs, newlines) and comments carry no semantic meaning for the parser, so they are consumed and discarded rather than emitted. The result is a clean, linear token stream where every element is semantically meaningful. This simplifies every subsequent compiler phase — the parser never has to check 'is this a space or a real token?' Some tools (formatters, documentation generators) choose to preserve whitespace and comments, but this is non-standard and done for specific tooling purposes."

- question: "Explain the difference between a lexeme and a token, and give a concrete example showing why the distinction matters."
  type: short-answer
  answer: "A lexeme is the actual substring of source code that was matched by the tokenizer — the raw text. A token is the lexeme paired with its category label (token type). For example, the identifiers `count`, `totalItems`, and `x` are three different lexemes, but all produce tokens of type IDENTIFIER. Conversely, `+` and `-` are two different lexemes that produce tokens of different types (PLUS and MINUS). The distinction matters because the parser works with token types (not raw text) to recognize grammatical structure, while error messages and source maps need the original lexeme text to point back to specific locations in source code. A lexeme with no type would be meaningless; a type with no lexeme would lose source location information."
```

## Explainer

Source code as written by a programmer is just a stream of characters — letters, digits, spaces, punctuation. Before a compiler can understand the structure of a program, it needs to group those characters into meaningful chunks. This is what **tokenization** (also called lexical analysis or scanning) does: it reads the raw character stream and produces a sequence of **tokens**, each labeled with a type and carrying the original text. Given the input `if (x >= 42)`, a tokenizer produces something like: `[KEYWORD:"if", LPAREN:"(", IDENT:"x", GE:">=", INT_LIT:"42", RPAREN:")"]`.

The terminology can be confusing, so here is the precise distinction. A **lexeme** is the actual substring of source code that was matched — for instance, `">="`or `"42"`. A **token** is the lexeme paired with its category — `GE` for the greater-than-or-equal operator, `INT_LIT` for an integer literal. Some token types have many possible lexemes (every variable name is an `IDENT`), while others have exactly one (`>=` is always `GE`). The tokenizer's job is to decide where each lexeme begins and ends, and which category it belongs to.

Your prerequisite knowledge of **regular expressions** is directly applied here. Each token type is defined by a regex pattern: identifiers might match `[a-zA-Z_][a-zA-Z0-9_]*`, integer literals match `[0-9]+`, and so on. The tokenizer tries all patterns at the current position in the input and picks the one that matches the longest prefix — this is the **longest match rule**. When two patterns match the same length (like `if` matching both the keyword pattern and the identifier pattern), a **priority rule** breaks the tie, typically favoring keywords over identifiers. These two rules — longest match and priority — are enough to make tokenization unambiguous for most programming languages.

Tokenization also handles the parts of source code that carry no semantic meaning: **whitespace** and **comments** are consumed but typically not emitted as tokens (though some compilers preserve them for formatting tools or documentation generators). This stripping is what makes subsequent phases simpler — the parser never has to worry about spaces between tokens or comments interrupting expressions. The output of tokenization is a clean, linear sequence of meaningful tokens that the parser can process using the grammar rules you will study next.
