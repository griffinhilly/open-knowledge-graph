---
id: semantic-analysis
title: Semantic Analysis Phase
domain: computer-science
course: compilers
prerequisites:
- id: abstract-syntax-trees
  type: hard
- id: symbol-tables-and-scope
  type: hard
- id: formal-logic-propositions
  type: soft
builds-toward:
- type-inference-algorithms
- intermediate-code-representation
tags:
- semantic-analysis
- type-checking
- language-semantics
stage: advanced
status: draft
---

# Semantic Analysis Phase

## Core Idea
Semantic analysis checks the AST for semantic correctness beyond syntax. It verifies that identifiers are declared before use, types are compatible, function calls have correct arities, and other language rules are obeyed. This phase builds symbol tables, resolves names, and annotates the AST with type information. Errors here (undefined variables, type mismatches) are caught before code generation.

## Questions

```yaml
- question: "A program passes the parser successfully but fails during semantic analysis. Which of the following is the most likely cause?"
  type: multiple-choice
  options:
    - "The program has a syntax error — a missing semicolon or mismatched brace"
    - "The program uses a variable that was never declared in the current scope"
    - "The program has an infinite loop that the compiler detected"
    - "The program uses an unsupported keyword not in the grammar"
  answer: 1
  explanation: "Parsing only checks structural correctness — whether the program follows the grammar rules. An undeclared variable is syntactically valid (the grammar allows any identifier in an expression position) but semantically invalid (the symbol table lookup fails). Option A describes a syntax error, which the *parser* would catch — it never reaches semantic analysis. Option C (infinite loop detection) is the halting problem, which compilers generally cannot solve. Option D (unsupported keyword) would fail at lexing or parsing, not semantic analysis."

- question: "During semantic analysis, type checking proceeds bottom-up through the AST. Which of the following best explains why this direction is correct?"
  type: multiple-choice
  options:
    - "Bottom-up processing is faster than top-down, which is why compilers prefer it"
    - "Types of composite expressions depend on the types of their subexpressions — you must know the parts before you can determine the whole"
    - "The symbol table is built top-down, so type checking must go in the opposite direction to avoid conflicts"
    - "Top-down type checking would require the compiler to know the expected type before reading the expression, which is only needed for type inference"
  answer: 1
  explanation: "Type checking is bottom-up because an expression's type is computed from its children. The type of `a + b` cannot be determined until the types of `a` and `b` are known. Literals have base types (e.g., `3` is int); variables get their types from symbol table lookups; operators combine the types of their operands according to typing rules. This is a natural post-order traversal of the AST: process children, then combine their results at the parent. Option D has a grain of truth about type inference but does not explain why basic type checking is bottom-up."

- question: "Semantic analysis can catch all runtime errors, so a program that passes semantic analysis will execute without errors."
  type: true-false
  answer: false
  explanation: "Semantic analysis catches a specific class of errors detectable at compile time from the program's static structure: undeclared variables, type mismatches, arity errors, contextual constraint violations. It cannot catch dynamic errors that depend on runtime values — array index out of bounds, null pointer dereferences, division by zero (when the divisor is a variable), or any error whose occurrence depends on input data. Static analysis is inherently incomplete for this reason: the set of runtime behaviors is undecidable in general. Semantic analysis is the last line of defense the compiler can offer, not a guarantee of correct execution."

- question: "The output of semantic analysis is the same AST produced by the parser, since semantic analysis only checks for errors without modifying the tree."
  type: true-false
  answer: false
  explanation: "Semantic analysis produces a *decorated* (or annotated) AST — the original tree augmented with type information at each node. This decoration is not optional; it is essential for the next compiler phase. Code generation must know the type of every expression to emit correct machine code (e.g., whether `+` should compile to an integer add instruction, a floating-point add, or a string concatenation). Without type annotations on the AST, the code generator would need to re-derive types, duplicating work. The decorated AST is the primary output that later phases consume."

- question: "What is the role of the symbol table during semantic analysis, and what two types of errors does it enable the compiler to detect?"
  type: short-answer
  answer: "The symbol table records all declared identifiers — their names, types, scopes, and attributes (e.g., whether a variable is a const, a function's parameter list). During semantic analysis, the AST walk consults the symbol table on every identifier use. This enables detection of two major error classes: (1) *use-before-declaration errors* — an identifier is used but has no entry in the current scope chain (undeclared variable or function); (2) *type mismatch errors* — the declared type of an identifier conflicts with how it is being used (e.g., calling an integer as a function, assigning a string to an int variable, passing the wrong number of arguments). The symbol table is what connects the declaration site of every name to all its use sites."
  explanation: "The scope structure of the symbol table (nested scopes, block scoping) is critical for getting name resolution right in languages with shadowing or block scoping. Semantic analysis must enter and exit scopes in sync with the AST traversal so that the correct declarations are visible at each use site — the same way the runtime would resolve names during execution. Getting this right is why semantic analysis is a non-trivial phase despite not generating any code."
```

## Explainer

Parsing tells you whether a program is grammatically well-formed — whether `x = 3 + y;` follows the language's syntax rules. But it cannot tell you whether `y` has been declared, whether `3 + y` makes sense given `y`'s type, or whether the result can be assigned to `x`. These are **semantic** questions, and answering them is the job of semantic analysis. Think of it this way: parsing checks spelling and grammar, while semantic analysis checks whether the sentences actually mean something coherent.

The central data structure you bring into this phase is the **abstract syntax tree** from parsing, and the central tool you build is the **symbol table** from your prerequisite on scope. Semantic analysis walks the AST, and at each node it consults and updates the symbol table. When it encounters a variable declaration, it inserts an entry. When it encounters a variable use, it looks the name up — if it's missing, that's an "undeclared variable" error. When it encounters a function call, it checks that the number and types of arguments match the function's signature. The symbol table's scope structure (nested scopes, block scoping, function scoping) determines which declarations are visible at each point in the program.

**Type checking** is the most substantial part of semantic analysis for most languages. The analyzer assigns a type to every expression in the AST, working bottom-up: literals have known types, variables get their types from the symbol table, and operators combine types according to the language's rules. If you write `"hello" + 3` in a language that doesn't allow string-integer addition, the type checker flags it here. The result is a **decorated AST** — the original tree annotated with type information at each node. This annotated tree is what the code generator will consume, because generating correct machine code requires knowing whether `+` means integer addition, floating-point addition, or string concatenation.

Beyond type checking, semantic analysis enforces a grab bag of language-specific rules that don't fit neatly into syntax. Does a `break` statement appear inside a loop? Does a `return` statement appear inside a function? Is a `const` variable being reassigned? Are all paths through a function guaranteed to return a value? These checks are sometimes called **contextual constraints** — they depend on the surrounding program context in ways that a context-free grammar cannot express. Together, they form the last line of defense before the compiler commits to generating code: if a program passes semantic analysis, the compiler can proceed with confidence that the program is meaningful and internally consistent.
