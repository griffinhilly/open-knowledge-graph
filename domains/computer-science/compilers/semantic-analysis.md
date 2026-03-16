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

## Explainer

Parsing tells you whether a program is grammatically well-formed — whether `x = 3 + y;` follows the language's syntax rules. But it cannot tell you whether `y` has been declared, whether `3 + y` makes sense given `y`'s type, or whether the result can be assigned to `x`. These are **semantic** questions, and answering them is the job of semantic analysis. Think of it this way: parsing checks spelling and grammar, while semantic analysis checks whether the sentences actually mean something coherent.

The central data structure you bring into this phase is the **abstract syntax tree** from parsing, and the central tool you build is the **symbol table** from your prerequisite on scope. Semantic analysis walks the AST, and at each node it consults and updates the symbol table. When it encounters a variable declaration, it inserts an entry. When it encounters a variable use, it looks the name up — if it's missing, that's an "undeclared variable" error. When it encounters a function call, it checks that the number and types of arguments match the function's signature. The symbol table's scope structure (nested scopes, block scoping, function scoping) determines which declarations are visible at each point in the program.

**Type checking** is the most substantial part of semantic analysis for most languages. The analyzer assigns a type to every expression in the AST, working bottom-up: literals have known types, variables get their types from the symbol table, and operators combine types according to the language's rules. If you write `"hello" + 3` in a language that doesn't allow string-integer addition, the type checker flags it here. The result is a **decorated AST** — the original tree annotated with type information at each node. This annotated tree is what the code generator will consume, because generating correct machine code requires knowing whether `+` means integer addition, floating-point addition, or string concatenation.

Beyond type checking, semantic analysis enforces a grab bag of language-specific rules that don't fit neatly into syntax. Does a `break` statement appear inside a loop? Does a `return` statement appear inside a function? Is a `const` variable being reassigned? Are all paths through a function guaranteed to return a value? These checks are sometimes called **contextual constraints** — they depend on the surrounding program context in ways that a context-free grammar cannot express. Together, they form the last line of defense before the compiler commits to generating code: if a program passes semantic analysis, the compiler can proceed with confidence that the program is meaningful and internally consistent.
