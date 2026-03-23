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
status: validated
---

# Runtime Function Calls and Stack Frames

## Core Idea
Function calls must maintain a call stack: each activation creates a stack frame storing return address, parameters, local variables, and saved registers. Calling conventions specify register allocation, parameter passing (registers vs. stack), and caller/callee save responsibilities. Proper calling conventions are essential for correctness and interoperability between separately compiled code.

## Questions

```yaml
- question: "A function g() stores a critical intermediate result in register R9. It then calls f(). After f() returns, R9 contains a different value, corrupting g()'s computation. Assuming the x86-64 System V ABI, what went wrong?"
  type: multiple-choice
  options:
    - "R9 is a caller-saved register, so g() was responsible for saving it before the call and failed to do so"
    - "R9 is a callee-saved register, so f() violated the ABI by not restoring it"
    - "The stack pointer was misaligned, causing register corruption"
    - "f() should have cleared R9 before returning to signal that it was not used"
  answer: 0
  explanation: "In the x86-64 System V ABI, R9 is one of the argument-passing registers (caller-saved). Caller-saved means: if the caller needs the value across a function call, *the caller* must save it (e.g., push to stack) before the call and restore it afterward. The callee (f) is free to overwrite caller-saved registers. g() violated its own responsibility by relying on R9 surviving a call. Option B would be correct if R9 were callee-saved (like RBX, R12–R15), which it is not."

- question: "What does the `ret` instruction execute when a function returns?"
  type: multiple-choice
  options:
    - "Deallocates the current stack frame by resetting the stack pointer"
    - "Pops the return address from the stack and jumps to it"
    - "Restores all callee-saved registers to their values before the function call"
    - "Adjusts the frame pointer to point to the caller's frame"
  answer: 1
  explanation: "The `ret` instruction does exactly one thing: it pops the top of the stack (which is the return address pushed by the preceding `call` instruction) and jumps to that address. Stack frame deallocation (option A) is performed beforehand by adjusting the stack pointer. Restoring callee-saved registers (option C) is the callee's responsibility in its epilogue code before ret. Restoring the frame pointer (option D) also happens before ret. The ret instruction itself is simply a 'pop PC' operation."

- question: "If a compiler generates code using one calling convention but links against a library compiled with a different calling convention, the mismatch will be detected as a compilation or link error."
  type: true-false
  answer: false
  explanation: "False. Calling convention mismatches are not detectable at compile or link time because object files contain no metadata about which convention was used — they are just sequences of machine instructions. The mismatch manifests only at runtime, typically as silent data corruption (wrong values in registers), crashes, or stack misalignment. This is precisely why calling conventions must be standardized platform-wide and why compilers must faithfully implement the ABI: correctness cannot be verified mechanically, only by convention adherence."

- question: "In a recursive function that calls itself 100 levels deep, each active invocation maintains its own stack frame with its own local variables until it returns."
  type: true-false
  answer: true
  explanation: "True. Every function call, including recursive ones, creates a new stack frame. The 100th recursive call has 100 active stack frames simultaneously — each preserving the return address, local variables, and saved registers for that invocation. This is how recursion naturally preserves state at each level: the stack structure guarantees that when the 100th call returns, execution resumes in the 99th call's frame, which still holds the 99th invocation's locals intact. This also explains why unbounded recursion causes stack overflow — frames accumulate without bound."

- question: "Why is the division of register-saving responsibility between caller and callee a fundamental design tradeoff, rather than simply assigning all responsibility to one side?"
  type: short-answer
  answer: "If all registers were callee-saved, every function would need a prologue/epilogue that saved and restored every register it used, even for short leaf functions that only use one register. If all registers were caller-saved, every call site would need to save every live register, even when the callee doesn't touch most of them. Splitting responsibility lets each side save only what it actually needs: the caller saves registers it needs to survive the call, and the callee saves registers it plans to clobber. This minimizes total save/restore overhead across the program."
  explanation: "The tradeoff is between call-site overhead (caller saves) and prologue/epilogue overhead (callee saves). Caller-saved registers are cheap for callees (they can freely overwrite them) but costly for callers that need values preserved. Callee-saved registers guarantee caller values survive, but make callees pay even if the caller doesn't need preservation. ABIs partition registers empirically based on typical usage patterns — e.g., argument registers are caller-saved because the callee overwrites them anyway, while general-purpose registers used as loop variables are callee-saved to reduce call-site overhead in loops."
```

## Explainer

When your generated code encounters a function call, the processor must do more than just jump to the function's first instruction. It needs to remember where to return, pass arguments to the callee, allocate space for local variables, and ensure that registers the caller was using are not clobbered. All of this is managed through the **call stack** — a region of memory that grows and shrinks as functions are called and return. Each active function occupies a contiguous block on this stack called a **stack frame** (or activation record).

A typical stack frame contains several regions, laid out in a specific order defined by the platform's **calling convention**. Starting from the frame's base, you typically find the saved return address (where to jump when this function finishes), saved frame pointer (so you can restore the caller's frame), space for local variables, and possibly saved registers. Arguments may live in registers, on the stack, or both — the convention dictates which. For example, the x86-64 System V ABI passes the first six integer arguments in registers (RDI, RSI, RDX, RCX, R8, R9) and any additional arguments on the stack, while the Windows x64 convention uses RCX, RDX, R8, R9 for the first four.

From your work on code generation and memory organization, you know the compiler must emit instructions for both sides of a call. The **caller** saves any registers it needs preserved (caller-saved registers), pushes arguments that do not fit in registers, and executes a `call` instruction that pushes the return address and jumps. The **callee** then sets up its own frame: it saves the old frame pointer, allocates space for locals by adjusting the stack pointer, and saves any callee-saved registers it plans to use. On return, the callee restores those registers, deallocates its frame, and executes a `ret` instruction that pops the return address and jumps back. The division of register-saving responsibility between caller and callee is a fundamental design tradeoff — more callee-saved registers reduce save/restore overhead at call sites but increase function prologue/epilogue cost.

Getting calling conventions right is not just a correctness issue — it is an **interoperability** requirement. If your compiler generates code that follows the System V convention but links against a library compiled with a different convention, the program will crash or silently corrupt data. This is why calling conventions are standardized per platform and why the compiler must faithfully implement them in its code generation phase. Recursive functions make the stack mechanism especially visible: each recursive call pushes a new frame, and the stack unwinds frame by frame as calls return, naturally preserving each invocation's local state.
