---
id: multi-stage-programming
title: Multi-Stage Programming and Staged Compilation
domain: computer-science
course: compilers
prerequisites:
- id: intermediate-code-representation
  type: hard
- id: code-generation
  type: hard
builds-toward:
- compiler-bootstrapping
tags:
- metaprogramming
- stages
- codegen
stage: expert
status: validated
---

# Multi-Stage Programming and Staged Compilation

## Core Idea
Multi-stage programming separates computation into stages: stage 1 generates code as data structures, stage 2 executes the generated code. Used for compiler generators, template instantiation, and partial evaluation, it brings code-generation capabilities into the language itself.

## Questions

```yaml
- question: "What is the key advantage of multi-stage programming over traditional metaprogramming approaches like C macros or eval()?"
  type: multiple-choice
  options:
    - "Multi-stage programs run faster at runtime because all code generation happens before execution begins"
    - "The type system guarantees that generated code is well-typed at stage 1, before it is ever executed — type errors in generated code are caught at compile time"
    - "Multi-stage programming can generate code that macros cannot express, enabling more complex transformations"
    - "Staging requires fewer lines of code than macro-based approaches, improving maintainability"
  answer: 1
  explanation: "Type safety across stages is the defining advantage. With C macros or string-based eval(), generated code is not checked until it runs — a type error in generated code only surfaces as a runtime failure. In a well-designed multi-stage language like MetaOCaml, the stage-1 type checker verifies that bracketed code (.<e>.) is well-typed even before it is executed. This means you cannot accidentally produce type-incorrect code at stage 2. Speed may also improve, but that is a consequence of specialization — not the fundamental property that distinguishes multi-stage programming."

- question: "A programmer writes a multi-stage expression: .<fun x -> x + .~(some_int_computation)>. If some_int_computation produces a string instead of an integer at stage 1, when is the error detected?"
  type: multiple-choice
  options:
    - "At stage 2, when the bracketed code is finally executed and the type mismatch causes a runtime failure"
    - "Never — the type error is silently coerced to match the expected type"
    - "At stage 1, when the type checker validates the bracketed expression and finds that splicing a string into integer addition is ill-typed"
    - "Only if the programmer explicitly adds type annotations to the bracket expression"
  answer: 2
  explanation: "This illustrates the core value proposition of multi-stage typing. The bracket construct .<e>. does not defer type checking — it defers evaluation. The type checker inspects the bracketed expression at stage 1 and propagates types through the splice (.~) to detect mismatches. Contrast this with eval() in Python or JavaScript, where a dynamically constructed string of code is only type-checked (if at all) when it runs. The guarantee is: if stage-1 compilation succeeds, stage-2 execution will not encounter type errors from the generated code."

- question: "C++ template instantiation is a limited form of multi-stage programming where type parameters are resolved at compile time to produce specialized code."
  type: true-false
  answer: true
  explanation: "This analogy is accurate. In C++ templates, stage 1 is compilation — the compiler resolves template parameters and instantiates specialized versions of functions or classes. Stage 2 is execution of the specialized code. The 'multi-stage' nature is constrained: C++ templates operate only on types and compile-time constants, not arbitrary code generation with the full expressiveness of languages like MetaOCaml. But the structure — generate specialized code at one stage, execute it at another — is the same principle. Partial evaluation and compiler generators (like Yacc) are similarly understood as two-stage systems."

- question: "Multi-stage programming and C macros provide equivalent safety guarantees because both generate code before runtime, so errors are generally caught before the program executes."
  type: true-false
  answer: false
  explanation: "C macros are purely textual substitution with no type awareness — the preprocessor replaces tokens without understanding their types, and the resulting code is only type-checked after substitution. A type error in a macro-generated expression surfaces during compilation of the expanded output, but complex macros can generate code that type-checks incorrectly or has subtle semantic errors that are hard to diagnose. Multi-stage programming explicitly type-checks generated code at the stage where it is constructed, providing a formal guarantee that the code product is well-typed. The safety guarantee is categorically stronger."

- question: "What are brackets and escapes in multi-stage programming, and why is type safety across stages the critical property in practice?"
  type: short-answer
  answer: "Brackets (.<e>.) delay evaluation of e to a later stage — e is treated as code-as-data rather than executed immediately. Escapes (.~e) splice a current-stage value into bracketed (delayed) code. Together they let programmers explicitly control when computation happens. Type safety across stages means the type checker verifies the bracketed code is well-typed at stage 1, before stage 2 executes it — so code generation errors are caught early, not at runtime."
  explanation: "In practice, the value of staging is generating specialized, efficient code (e.g., a partially evaluated interpreter) without losing correctness guarantees. If type errors in generated code could only be caught at stage-2 runtime, staging would offer the same debugging experience as eval() — errors appear late, in code that is hard to inspect. The compile-time guarantee transforms code generation from a debugging nightmare into a safe, composable programming technique."
```

## Explainer

You already understand intermediate representations and code generation — how a compiler transforms source programs into executable output. Multi-stage programming takes this idea and makes it available *within* the language itself: a program can construct another program (as an IR or code fragment) at one stage and then execute or compile that generated code at the next stage. Instead of the compiler being the only entity that generates code, the programmer gets explicit control over when code is produced and when it runs.

The simplest way to understand staging is through a concrete example. Imagine you have an interpreter for mathematical expressions, and you know at compile time that a particular expression will always be `x * 2 + 1`. A staged program can **partially evaluate** the interpreter at stage 1, "baking in" the known expression structure and producing specialized code that just computes `x * 2 + 1` directly — no interpretation overhead at runtime. The key language constructs are **brackets** (which delay computation to a later stage) and **escapes** (which splice a current-stage value into delayed code). In MetaOCaml, for instance, `.<e>.` brackets an expression for later execution, and `.~e` escapes a value into bracketed code.

What makes this different from ordinary metaprogramming (like C macros or string-based code generation) is **type safety across stages**. In a well-designed multi-stage language, the type system guarantees that the generated code is well-typed before it is ever executed. You cannot accidentally produce code with a type error at stage 2 — the stage-1 type checker catches it. This is the crucial advantage over approaches like `eval()` or template-based code generation, where errors only surface at runtime.

Staged compilation connects directly to several compiler techniques you have already studied. **Compiler generators** like Yacc are essentially two-stage systems: stage 1 reads a grammar and generates a parser (code), stage 2 compiles and runs that parser. **Template instantiation** in C++ is a limited form of staging where the template parameters are resolved at compile time to produce specialized code. **Partial evaluation** — automatically specializing a general program given some known inputs — is the theoretical foundation underlying all of these. Multi-stage programming makes this pipeline explicit, composable, and safe, turning the compiler's own code-generation machinery into a first-class tool for the programmer.
