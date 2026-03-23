---
id: semantic-error-detection-reporting
title: Semantic Error Detection and Reporting
domain: computer-science
course: compilers
prerequisites:
- id: attribute-grammar-framework
  type: hard
- id: semantic-analysis
  type: hard
builds-toward:
- scope-binding-resolution
tags:
- semantic-analysis
- error-detection
- diagnostics
stage: advanced
status: validated
---

# Semantic Error Detection and Reporting

## Core Idea
Semantic analysis discovers errors invisible to the parser—undeclared variables, type mismatches, undefined functions. Effective error detection requires traversing the AST, gathering context, and comparing actual vs expected properties.

## How It's Best Learned
Implement a semantic analyzer detecting multiple error categories. Practice writing clear, actionable error messages with precise locations.

## Common Misconceptions
Semantic analysis is just type checking (it includes scope checking, usage rules, and more). Errors should stop compilation immediately (collect all errors so users see all problems).

## Questions

```yaml
- question: "A compiler's semantic analyzer finds an undeclared variable `total` on line 12. If it records an 'error' type for `total` and continues analysis, what problem does this solve?"
  type: multiple-choice
  options:
    - "It automatically fixes the error by inferring the correct type for `total`"
    - "It prevents every subsequent use of `total` from generating a new, spurious type-mismatch error"
    - "It makes the compiler faster by skipping further checks on `total`"
    - "It converts the semantic error into a syntactic error for easier reporting"
  answer: 1
  explanation: "This technique is called error dampening. If the analyzer stops after finding `total` undeclared, the user fixes it and recompiles — only to discover the next error. If instead it inserts a placeholder 'error type' for `total`, then every subsequent expression involving `total` can be treated as having a valid (if poisoned) type, suppressing cascading follow-on errors. The programmer sees one root-cause error rather than dozens of spurious errors. Error dampening is what makes it possible to collect a clean, actionable error list in a single compilation pass."

- question: "Which of the following errors would a syntactic parser catch, and which would require semantic analysis?"
  type: multiple-choice
  options:
    - "Parser catches: missing semicolon. Semantic analysis catches: calling a function with too many arguments"
    - "Parser catches: using a variable before declaring it. Semantic analysis catches: mismatched parentheses"
    - "Parser catches: passing a string to a function expecting an integer. Semantic analysis catches: a typo in a keyword"
    - "Both are caught by the parser — semantic analysis only checks style"
  answer: 0
  explanation: "Parsers check grammatical structure: missing semicolons, mismatched brackets, malformed expressions — anything the grammar rules can express. Semantic analysis checks meaning: whether names are declared, whether types are compatible, whether function calls match signatures. A statement like `print(\"hello\", \"world\")` when `print` takes one argument is syntactically valid (it's a well-formed function call expression) but semantically wrong. The parser has no access to the symbol table that would reveal the argument count mismatch — that information only becomes available during semantic analysis."

- question: "A program can have semantic errors even if it compiles successfully through the parsing phase."
  type: true-false
  answer: true
  explanation: "True. Parsing only verifies that the program matches the language's grammar — it confirms that the token sequence is syntactically well-formed. Semantic errors are invisible to grammar rules: `x = y + z;` is syntactically perfect but fails semantically if `y` is undeclared or if `z` is a type incompatible with addition. The parser has no knowledge of variable declarations, types, or usage rules. Semantic analysis is an entirely separate phase that traverses the AST using the symbol table and type environment to enforce these meaning-level constraints."

- question: "The best practice in compiler error handling is to stop and report only the first semantic error, because additional errors found after the first may be spurious and confuse the programmer."
  type: true-false
  answer: false
  explanation: "False. While some follow-on errors can be spurious (caused by an earlier error, not a real bug), stopping at the first error forces the programmer into a frustrating cycle: fix one error, recompile, discover the next. Good compilers collect as many real errors as possible in a single pass using error dampening — inserting placeholder types for undeclared identifiers so that subsequent uses don't cascade. The goal is to report all root-cause errors while suppressing the spurious ones, not to stop early. This principle is explicitly embodied in compilers like Rust's rustc and Elm's compiler, which are renowned for their diagnostic quality."

- question: "Why is the quality of semantic error messages just as important as whether errors are detected at all? What information should a good error message include?"
  type: short-answer
  answer: "A compiler that detects an error but reports only 'type error on line 47' forces the programmer to investigate manually — it tells them something is wrong but not what or why. A good error message includes: the source location (file, line, column), the specific mismatch (e.g., 'expected int but got string'), context about what was expected and what was found, and ideally a suggestion (e.g., 'did you mean `count`?'). The semantic analyzer has access to rich context — the symbol table, type environment, AST structure — and leveraging this context to produce precise messages is what turns a compiler into a productive tool rather than an obstacle."
  explanation: "Error messages are the primary user interface between a compiler and its users. The semantic analyzer is in a uniquely privileged position: it knows what variable was expected, what type was found, what names are in scope, and the full program structure. Failing to use this information produces messages that are technically correct but practically useless. Modern compilers like Rust's rustc have demonstrated that excellent diagnostics dramatically reduce debugging time and improve language adoption."
```

## Explainer

From your study of semantic analysis and attribute grammars, you know that parsing confirms a program's syntactic structure — it answers "is this grammatically valid?" Semantic analysis goes further, answering "does this program make sense?" A statement like `x = y + z;` is syntactically perfect, but if `y` is an undeclared variable or `z` is a string being added to an integer in a language that forbids it, those are **semantic errors** — problems that no grammar rule can catch. Detecting and reporting these errors is one of the compiler's most user-facing responsibilities.

Semantic error detection works by traversing the abstract syntax tree and checking each node against the language's rules using information accumulated in the symbol table and type environment. The major categories of errors include **undeclared names** (using a variable that was never defined), **type mismatches** (passing a string where an integer is expected), **arity errors** (calling a function with the wrong number of arguments), **duplicate declarations** (defining the same variable twice in the same scope), and **access violations** (reading a private field from outside a class). Attribute grammars give you a formal framework for specifying these checks: inherited attributes carry context down the tree (like what variables are in scope), and synthesized attributes carry results back up (like the type of an expression).

A critical design decision is **error recovery** — what the compiler does after finding a semantic error. The naive approach is to stop at the first error, but this forces the programmer into a frustrating cycle of fix-one-recompile-find-next. Good compilers collect as many errors as possible in a single pass. This requires the analyzer to continue after an error, which means it needs a strategy for the "damaged" state: if a variable is undeclared, the analyzer can insert a placeholder entry with an "error" type so that subsequent uses of that variable do not cascade into dozens of spurious follow-on errors. This technique, called **error dampening**, is essential for producing a clean, actionable error list.

The quality of error messages is just as important as the detection itself. A message like "type error on line 47" is technically correct but nearly useless. Effective error reporting includes the **source location** (file, line, and column), the **specific mismatch** ("expected int but got string"), and ideally a **suggestion** ("did you mean `count` instead of `coutn`?"). Modern compilers like Rust's `rustc` and Elm's compiler have raised the bar for diagnostic quality, treating error messages as a user interface. The semantic analyzer has access to rich context — the symbol table, the type environment, the AST structure — and leveraging this context to produce precise, helpful messages is what separates a good compiler from a frustrating one.
