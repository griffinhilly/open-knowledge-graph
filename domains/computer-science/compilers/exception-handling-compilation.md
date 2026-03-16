---
id: exception-handling-compilation
title: Exception Handling Implementation
domain: computer-science
course: compilers
prerequisites:
- id: semantic-analysis
  type: hard
- id: code-generation
  type: hard
builds-toward:
- bytecode-and-vm-design
tags:
- exceptions
- runtime
- control-flow
stage: advanced
status: draft
---

# Exception Handling Implementation

## Core Idea
Exceptions are compiled into stack unwinding mechanisms. The compiler generates exception dispatch tables indexed by program counter ranges, inserts runtime checks that invoke the unwinder when exceptions occur, and generates finally-block code to execute during unwinding, ensuring cleanup happens correctly.

## Explainer

At the source level, exception handling looks straightforward: wrap code in a `try` block, catch specific exception types, and optionally run cleanup in a `finally` block. But from a compiler's perspective, exceptions introduce a form of **non-local control flow** that is fundamentally different from anything you have seen in normal code generation. When an exception is thrown, execution does not just jump to a nearby label — it may need to unwind through multiple stack frames, destroying local variables, running destructors, and executing finally blocks in each frame along the way, until it finds a matching catch handler. The compiler must generate code that makes all of this possible without slowing down the normal (non-exceptional) execution path.

The dominant modern approach is **table-driven exception handling**, sometimes called "zero-cost" exceptions because it adds no overhead to code that does not throw. The compiler generates an **exception table** alongside the normal code. This table maps ranges of program counter values to information about what to do if an exception occurs at that point: which catch handlers are in scope, what cleanup (destructors or finally blocks) must run, and how to unwind the stack frame. When no exception is thrown, this table is never consulted — the normal code runs at full speed with zero extra instructions. Only when an exception actually occurs does the runtime look up the current program counter in the table and begin the unwinding process.

**Stack unwinding** is the core runtime mechanism. When an exception is thrown, the runtime walks backward through the call stack, frame by frame. At each frame, it consults the exception table to determine whether a matching catch handler exists. If one is found, control transfers to it. If not, the runtime runs any registered cleanup code (destructors, finally blocks) for that frame and continues unwinding to the caller. This requires that each stack frame contain enough metadata — saved registers, frame pointer, return address — for the unwinder to reconstruct the caller's state. The compiler must emit this metadata, often in a standardized format like DWARF `.eh_frame` sections on Unix systems, so that the unwinder can traverse frames compiled by different compilers or even written in different languages.

The alternative to table-driven handling is **setjmp/longjmp-based** implementation, where `try` blocks save the current execution context (registers, stack pointer) with `setjmp`, and `throw` restores it with `longjmp`. This is simpler to implement but imposes a cost on every `try` block entry — even when no exception is thrown — because `setjmp` must execute and save state. For languages like C++ and Java where try blocks are common and exceptions are rare, the table-driven approach is strongly preferred. The compiler's job is to emit correct tables that account for every possible throw point, ensure that cleanup code runs in the right order during unwinding, and handle edge cases like exceptions thrown during stack unwinding itself (which in C++ calls `std::terminate`).
