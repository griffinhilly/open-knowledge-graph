---
id: activation-records-runtime
title: Activation Records and Stack Frames
domain: computer-science
course: compilers
prerequisites:
- id: memory-management-basics
  type: hard
- id: calling-conventions-abi
  type: hard
builds-toward:
- exception-handling-compilation
tags:
- runtime
- memory
- function-calls
stage: advanced
status: draft
---

# Activation Records and Stack Frames

## Core Idea
An activation record (or stack frame) stores a function's return address, parameters, local variables, saved registers, and temporary values. The compiler generates code to build these frames on function entry and dismantle them on exit, managing the runtime call stack and enabling recursion.

## How It's Best Learned
Examine assembly code for a simple recursive function, trace stack frame construction, and verify that parameters and locals are accessible at known offsets from the frame pointer.

## Explainer

From your study of calling conventions, you know that when one function calls another, there must be an agreed-upon protocol for passing arguments, returning values, and preserving registers. The **activation record** (or **stack frame**) is the concrete data structure that makes this possible at runtime. Each time a function is called, a new activation record is pushed onto the call stack; when the function returns, its record is popped. This stack-based discipline is what enables recursion — each recursive call gets its own independent frame with its own copy of parameters and local variables, even though the same function code is executing.

A typical activation record contains several regions laid out at known offsets from a reference point. The **return address** records where execution should resume after the function finishes. The **saved frame pointer** preserves the caller's frame pointer so it can be restored on return, maintaining the chain of frames. **Parameters** that did not fit in registers (or that the calling convention places on the stack) occupy a known region. **Local variables** are allocated at negative offsets from the frame pointer. **Saved registers** preserve any callee-saved registers the function intends to use, so the caller finds them unchanged on return. The compiler assigns each variable a fixed offset at compile time, so accessing a local variable compiles to a single memory load like `mov eax, [rbp-8]` — no name lookup, no search, just arithmetic on the frame pointer.

The function **prologue** and **epilogue** are the bookkeeping sequences the compiler emits at the start and end of every function. The prologue pushes the old frame pointer, sets the new frame pointer to the current stack pointer, and adjusts the stack pointer to reserve space for locals and temporaries. The epilogue reverses this: it restores the stack pointer, pops the saved frame pointer, and executes a return instruction that jumps to the saved return address. These sequences are so mechanical and predictable that debuggers use them to **walk the stack** — following the chain of saved frame pointers from the current frame back through every caller, which is how you get a stack trace when a program crashes.

Understanding activation records also illuminates why certain bugs behave the way they do. A buffer overflow in a local array can overwrite the saved return address, causing the function to "return" to an arbitrary location — this is the classic stack-smashing attack. A function that returns a pointer to a local variable hands out a dangling pointer because the local's stack memory is reclaimed when the frame is popped. And tail-call optimization, where the compiler reuses the current frame for a tail call instead of pushing a new one, becomes intuitive: if the current function has nothing left to do after the call, there is no reason to preserve its frame. The compiler simply overwrites the current activation record with the new call's data, turning recursion into iteration at the machine level.
