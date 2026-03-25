---
id: activation-records-runtime
title: Activation Records and Stack Frames
domain: computer-science
course: compilers
prerequisites:
- id: memory-management-basics
  type: hard
builds-toward:
- exception-handling-compilation
tags:
- runtime
- memory
- function-calls
stage: advanced
status: validated
---

# Activation Records and Stack Frames

## Core Idea
An activation record (or stack frame) stores a function's return address, parameters, local variables, saved registers, and temporary values. The compiler generates code to build these frames on function entry and dismantle them on exit, managing the runtime call stack and enabling recursion.

## How It's Best Learned
Examine assembly code for a simple recursive function, trace stack frame construction, and verify that parameters and locals are accessible at known offsets from the frame pointer.

## Questions

```yaml
- question: "What enables a recursive function to have independent copies of its local variables for each level of nesting, even though all levels execute the same code?"
  type: multiple-choice
  options:
    - "The compiler generates a separate copy of the function code for each recursive invocation"
    - "Each function call creates a new activation record on the call stack, giving each invocation its own independent storage for locals and parameters"
    - "Local variables are stored in a global hash table indexed by call depth"
    - "Registers are multiplied — the CPU allocates a fresh register file per call"
  answer: 1
  explanation: "The call stack is the key. Every call to a function — including a recursive call — pushes a new activation record onto the stack. Each record has its own copy of the local variables at fixed offsets from the frame pointer. Two recursive calls at the same nesting level have two completely separate frames, so their locals are independent. When a call returns, its frame is popped, revealing the caller's frame with its own locals intact."

- question: "A function allocates a local character array `char buf[8]` and an attacker writes 20 bytes into it via an unchecked input. What does activation record layout explain about the consequence?"
  type: multiple-choice
  options:
    - "Nothing; the operating system prevents writes beyond the declared array size"
    - "The extra bytes overwrite adjacent regions of the activation record — potentially including the saved return address — redirecting control flow when the function returns"
    - "The local array silently expands to accommodate the overflow"
    - "The extra bytes overwrite heap memory, not stack memory"
  answer: 1
  explanation: "In the activation record, `buf` is allocated at a fixed negative offset from the frame pointer, and the saved return address is at a known positive offset. Writing beyond the end of `buf` advances into the rest of the frame. If the overflow reaches the saved return address slot, the attacker controls where execution jumps when the function's epilogue executes its return instruction. This is the classic stack-smashing / buffer overflow attack, and the activation record layout is precisely what makes it possible."

- question: "Each function call pushes a new activation record onto the call stack, which is why recursive functions correctly maintain independent copies of local variables at every nesting level."
  type: true-false
  answer: true
  explanation: "The stack discipline is exactly what makes recursion work. Each call to a function — including recursive self-calls — gets its own frame with its own storage. The frame is only released when the function returns (epilogue pops it). Two concurrent activations of the same function have two distinct frames at two different stack addresses, so their locals never conflict. This is not a language-level abstraction — it is a direct consequence of how the compiler generates prologue and epilogue code."

- question: "Returning a pointer to a local variable is safe as long as the caller dereferences it before calling any other function, since the stack has not yet been reused."
  type: true-false
  answer: false
  explanation: "The activation record is popped the moment the function returns, reclaiming its stack memory. From that instant, the memory is logically free and will be overwritten by the prologue of any subsequent function call — regardless of timing. Accessing a local variable via a returned pointer is always undefined behavior; there is no safe window between the return and the next call, because even the act of calling another function will reuse that stack space."

- question: "Explain why tail-call optimization allows a recursive function to run in constant stack space, using the concept of activation records."
  type: short-answer
  answer: "In a tail call, the calling function has completely finished its own work and will return the callee's result directly — it has no further use for its own activation record. Rather than pushing a new frame on top of the existing one, the compiler reuses (overwrites) the current frame with the new call's data. The stack depth therefore stays constant regardless of how many recursive calls occur. Without TCO, each call would push a new frame, growing the stack linearly with call depth until a stack overflow."
  explanation: "Tail-call optimization transforms recursion into iteration at the machine level without changing the source-level semantics. It is why functional languages like Scheme guarantee TCO — unbounded recursion is the natural idiom, and without TCO it would always stack-overflow. The activation record concept makes it clear why the optimization is valid: if you don't need the current frame anymore, there is no reason to preserve it."
```

## Explainer

From your study of calling conventions, you know that when one function calls another, there must be an agreed-upon protocol for passing arguments, returning values, and preserving registers. The **activation record** (or **stack frame**) is the concrete data structure that makes this possible at runtime. Each time a function is called, a new activation record is pushed onto the call stack; when the function returns, its record is popped. This stack-based discipline is what enables recursion — each recursive call gets its own independent frame with its own copy of parameters and local variables, even though the same function code is executing.

A typical activation record contains several regions laid out at known offsets from a reference point. The **return address** records where execution should resume after the function finishes. The **saved frame pointer** preserves the caller's frame pointer so it can be restored on return, maintaining the chain of frames. **Parameters** that did not fit in registers (or that the calling convention places on the stack) occupy a known region. **Local variables** are allocated at negative offsets from the frame pointer. **Saved registers** preserve any callee-saved registers the function intends to use, so the caller finds them unchanged on return. The compiler assigns each variable a fixed offset at compile time, so accessing a local variable compiles to a single memory load like `mov eax, [rbp-8]` — no name lookup, no search, just arithmetic on the frame pointer.

The function **prologue** and **epilogue** are the bookkeeping sequences the compiler emits at the start and end of every function. The prologue pushes the old frame pointer, sets the new frame pointer to the current stack pointer, and adjusts the stack pointer to reserve space for locals and temporaries. The epilogue reverses this: it restores the stack pointer, pops the saved frame pointer, and executes a return instruction that jumps to the saved return address. These sequences are so mechanical and predictable that debuggers use them to **walk the stack** — following the chain of saved frame pointers from the current frame back through every caller, which is how you get a stack trace when a program crashes.

Understanding activation records also illuminates why certain bugs behave the way they do. A buffer overflow in a local array can overwrite the saved return address, causing the function to "return" to an arbitrary location — this is the classic stack-smashing attack. A function that returns a pointer to a local variable hands out a dangling pointer because the local's stack memory is reclaimed when the frame is popped. And tail-call optimization, where the compiler reuses the current frame for a tail call instead of pushing a new one, becomes intuitive: if the current function has nothing left to do after the call, there is no reason to preserve its frame. The compiler simply overwrites the current activation record with the new call's data, turning recursion into iteration at the machine level.
