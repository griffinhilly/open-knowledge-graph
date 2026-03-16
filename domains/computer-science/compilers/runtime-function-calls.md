---
id: runtime-function-calls
title: Runtime Function Calls and Stack Frames
domain: computer-science
course: compilers
prerequisites:
- id: code-generation
  type: hard
- id: memory-organization
  type: hard
builds-toward:
- garbage-collection-algorithms
tags:
- calling-conventions
- stack-frames
- runtime-support
stage: advanced
status: draft
---

# Runtime Function Calls and Stack Frames

## Core Idea
Function calls must maintain a call stack: each activation creates a stack frame storing return address, parameters, local variables, and saved registers. Calling conventions specify register allocation, parameter passing (registers vs. stack), and caller/callee save responsibilities. Proper calling conventions are essential for correctness and interoperability between separately compiled code.

## Explainer

When your generated code encounters a function call, the processor must do more than just jump to the function's first instruction. It needs to remember where to return, pass arguments to the callee, allocate space for local variables, and ensure that registers the caller was using are not clobbered. All of this is managed through the **call stack** — a region of memory that grows and shrinks as functions are called and return. Each active function occupies a contiguous block on this stack called a **stack frame** (or activation record).

A typical stack frame contains several regions, laid out in a specific order defined by the platform's **calling convention**. Starting from the frame's base, you typically find the saved return address (where to jump when this function finishes), saved frame pointer (so you can restore the caller's frame), space for local variables, and possibly saved registers. Arguments may live in registers, on the stack, or both — the convention dictates which. For example, the x86-64 System V ABI passes the first six integer arguments in registers (RDI, RSI, RDX, RCX, R8, R9) and any additional arguments on the stack, while the Windows x64 convention uses RCX, RDX, R8, R9 for the first four.

From your work on code generation and memory organization, you know the compiler must emit instructions for both sides of a call. The **caller** saves any registers it needs preserved (caller-saved registers), pushes arguments that do not fit in registers, and executes a `call` instruction that pushes the return address and jumps. The **callee** then sets up its own frame: it saves the old frame pointer, allocates space for locals by adjusting the stack pointer, and saves any callee-saved registers it plans to use. On return, the callee restores those registers, deallocates its frame, and executes a `ret` instruction that pops the return address and jumps back. The division of register-saving responsibility between caller and callee is a fundamental design tradeoff — more callee-saved registers reduce save/restore overhead at call sites but increase function prologue/epilogue cost.

Getting calling conventions right is not just a correctness issue — it is an **interoperability** requirement. If your compiler generates code that follows the System V convention but links against a library compiled with a different convention, the program will crash or silently corrupt data. This is why calling conventions are standardized per platform and why the compiler must faithfully implement them in its code generation phase. Recursive functions make the stack mechanism especially visible: each recursive call pushes a new frame, and the stack unwinds frame by frame as calls return, naturally preserving each invocation's local state.
