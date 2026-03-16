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
status: draft
---

# Semantic Error Detection and Reporting

## Core Idea
Semantic analysis discovers errors invisible to the parser—undeclared variables, type mismatches, undefined functions. Effective error detection requires traversing the AST, gathering context, and comparing actual vs expected properties.

## How It's Best Learned
Implement a semantic analyzer detecting multiple error categories. Practice writing clear, actionable error messages with precise locations.

## Common Misconceptions
Semantic analysis is just type checking (it includes scope checking, usage rules, and more). Errors should stop compilation immediately (collect all errors so users see all problems).

## Explainer

From your study of semantic analysis and attribute grammars, you know that parsing confirms a program's syntactic structure — it answers "is this grammatically valid?" Semantic analysis goes further, answering "does this program make sense?" A statement like `x = y + z;` is syntactically perfect, but if `y` is an undeclared variable or `z` is a string being added to an integer in a language that forbids it, those are **semantic errors** — problems that no grammar rule can catch. Detecting and reporting these errors is one of the compiler's most user-facing responsibilities.

Semantic error detection works by traversing the abstract syntax tree and checking each node against the language's rules using information accumulated in the symbol table and type environment. The major categories of errors include **undeclared names** (using a variable that was never defined), **type mismatches** (passing a string where an integer is expected), **arity errors** (calling a function with the wrong number of arguments), **duplicate declarations** (defining the same variable twice in the same scope), and **access violations** (reading a private field from outside a class). Attribute grammars give you a formal framework for specifying these checks: inherited attributes carry context down the tree (like what variables are in scope), and synthesized attributes carry results back up (like the type of an expression).

A critical design decision is **error recovery** — what the compiler does after finding a semantic error. The naive approach is to stop at the first error, but this forces the programmer into a frustrating cycle of fix-one-recompile-find-next. Good compilers collect as many errors as possible in a single pass. This requires the analyzer to continue after an error, which means it needs a strategy for the "damaged" state: if a variable is undeclared, the analyzer can insert a placeholder entry with an "error" type so that subsequent uses of that variable do not cascade into dozens of spurious follow-on errors. This technique, called **error dampening**, is essential for producing a clean, actionable error list.

The quality of error messages is just as important as the detection itself. A message like "type error on line 47" is technically correct but nearly useless. Effective error reporting includes the **source location** (file, line, and column), the **specific mismatch** ("expected int but got string"), and ideally a **suggestion** ("did you mean `count` instead of `coutn`?"). Modern compilers like Rust's `rustc` and Elm's compiler have raised the bar for diagnostic quality, treating error messages as a user interface. The semantic analyzer has access to rich context — the symbol table, the type environment, the AST structure — and leveraging this context to produce precise, helpful messages is what separates a good compiler from a frustrating one.
