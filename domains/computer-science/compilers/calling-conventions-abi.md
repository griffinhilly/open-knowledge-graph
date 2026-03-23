---
id: calling-conventions-abi
title: Calling Conventions and ABI
domain: computer-science
course: compilers
prerequisites:
- id: code-emission-target-generation
  type: hard
tags:
- abi
- calling-conventions
- function-calls
stage: advanced
status: validated
---

# Calling Conventions and ABI

## Core Idea
A calling convention specifies how functions are called: how arguments are passed (registers vs stack), where the return value goes, which registers are caller/callee-saved, and how the stack frame is organized. ABIs formalize these conventions so different compilers generate compatible code.

## How It's Best Learned
Study the ABI for your target platform (x86-64 System V ABI, ARM EABI, etc.). Implement function calls that interoperate with system libraries.

## Questions

```yaml
- question: "A function compiled for x86-64 Linux uses register r12 as a scratch register without saving or restoring it. The function is called from another function that stored a live value in r12 before the call. What happens?"
  type: multiple-choice
  options:
    - "Nothing — the calling function is responsible for saving r12 before any call it makes"
    - "A compiler warning is generated, but execution is correct"
    - "The caller's r12 value is silently overwritten, causing data corruption in the calling function"
    - "The processor raises an exception because r12 is read-only during function calls"
  answer: 2
  explanation: "In the x86-64 System V ABI, r12 is a callee-saved register. This means the called function (callee) is responsible for preserving it — if the callee wants to use r12, it must push it onto the stack on entry and pop it before returning. If the callee fails to do this and uses r12 as scratch space, the caller's live value is destroyed. No processor exception occurs; the hardware doesn't enforce ABI contracts — that's a software convention. The result is silent data corruption, which is one of the most insidious bugs in low-level code."

- question: "On Windows x64, the calling convention requires the caller to allocate 32 bytes of 'shadow space' on the stack even when all arguments fit in the four parameter registers. What is the purpose of this shadow space?"
  type: multiple-choice
  options:
    - "It holds the return address, since Windows doesn't use a link register like ARM does"
    - "It provides space the callee may use to spill its register arguments for debugging or variadic function handling"
    - "It aligns the stack to a 64-byte cache line boundary for performance"
    - "It stores the caller-saved registers automatically, so the compiler doesn't need to generate save/restore instructions"
  answer: 1
  explanation: "The shadow space (also called 'home space') is a 32-byte area the caller must reserve above the return address. It is *owned by the callee* — the callee can use it to write out the register arguments (rcx, rdx, r8, r9) if needed, for example to support variadic functions (which need all arguments contiguous in memory) or for debugger inspection. The caller allocates it but doesn't use it. This differs from Linux's System V ABI, which doesn't require shadow space, making Windows and Linux incompatible in their calling conventions even on the same hardware."

- question: "On x86-64 Linux, if a caller needs the value in register rax after making a function call, it must save rax before the call."
  type: true-false
  answer: true
  explanation: "rax is a caller-saved (call-clobbered) register in the System V ABI. The called function may freely overwrite rax — it uses rax as the return value register. If the calling function has a live value in rax that it needs after the call, it is the caller's responsibility to save it (typically by pushing it to the stack) before the call and restoring it afterward. The callee gives no guarantee about the state of caller-saved registers on return, except for what it explicitly puts there (like the return value in rax)."

- question: "The distinction between caller-saved and callee-saved registers is purely a performance optimization — if every register were callee-saved, programs would still be correct."
  type: true-false
  answer: true
  explanation: "Correctness-wise, this is true: if every register were callee-saved, functions would always restore every register before returning, preserving all caller state. Programs would work correctly. The distinction exists for performance: callee-saved registers require save/restore instructions in the callee's prologue/epilogue even when the callee uses them as scratch space. Caller-saved registers can be used freely as scratch without any overhead in the callee. By mixing both, the ABI minimizes total save/restore work — short scratch values (unlikely to span calls) can use caller-saved registers, and long-lived values (likely to span calls) should use callee-saved registers that the caller need not protect."

- question: "Why does the distinction between caller-saved and callee-saved registers exist in a calling convention, and what problem would arise if this distinction were eliminated by treating all registers as freely destroyable?"
  type: short-answer
  answer: "The distinction divides responsibility for register preservation between the two parties in a function call, minimizing total overhead. If all registers were freely destroyable (all caller-saved), every function that wanted to keep any live value across a call would have to save and restore every register it uses — even unused ones would need precautionary saves. If all registers were callee-saved, every function would pay save/restore costs in its prologue/epilogue for every register it touches. The hybrid approach lets the compiler choose: use caller-saved registers for temporaries that don't span calls (no cost to callee), and callee-saved for values that must survive calls (cost paid once in the callee, not at every call site)."
  explanation: "Without this division, the compiler would face a binary choice: either callers pay heavy spill costs at every call site, or callees pay heavy save/restore costs for every register they touch. The caller/callee split allows an optimizer to match register usage to register class — a significant factor in the performance of compiled code, especially in tight inner loops with many function calls."
```

## Explainer

When your compiler emits a function call, it must answer a series of concrete questions: Where do the arguments go? Where does the return value appear? Which registers can the called function freely overwrite, and which must it preserve? How is the stack aligned? If your compiler and the C standard library disagree on any of these answers, the program crashes or silently corrupts data. A **calling convention** is the complete specification that answers all of these questions, and an **Application Binary Interface** (ABI) formalizes calling conventions along with data layout, object file format, and other low-level details into a platform-wide contract.

Consider the x86-64 System V ABI used on Linux and macOS. The first six integer arguments go in registers rdi, rsi, rdx, rcx, r8, r9 — in that exact order. Floating-point arguments go in xmm0 through xmm7. Additional arguments spill onto the stack. The return value comes back in rax (or rax:rdx for 128-bit values). Registers rax, rcx, rdx, rsi, rdi, r8, r9, r10, r11 are **caller-saved** — the called function may freely destroy them, so if the caller needs their values after the call, it must save them first. Registers rbx, rbp, r12–r15 are **callee-saved** — the called function must restore them before returning. The stack must be 16-byte aligned before the `call` instruction. Every one of these details is a potential bug if your compiler gets it wrong.

The distinction between **caller-saved** and **callee-saved** registers is a division of labor that minimizes unnecessary work. If a register is caller-saved, the callee can use it as scratch space without any overhead — no saving, no restoring. If a register is callee-saved, the caller can assume it survives the call without doing anything — but the callee pays the cost of preserving and restoring it if it wants to use it. A compiler's register allocator must be aware of these rules: it should prefer caller-saved registers for short-lived temporaries that do not span calls, and callee-saved registers for values that must survive across calls. Getting this allocation right is a significant factor in generated code performance.

Different platforms make different tradeoffs. Windows x64 uses a different convention: only four registers for integer arguments (rcx, rdx, r8, r9), and the caller must always allocate a 32-byte "shadow space" on the stack even if all arguments fit in registers. ARM uses r0–r3 for the first four arguments and has a link register (lr) instead of pushing the return address on the stack. These differences mean that a compiler targeting multiple platforms needs a clean abstraction layer for call generation. ABIs also specify **struct passing** rules — small structs may be passed in registers, large ones by hidden pointer — and **variadic function** conventions, which often differ from normal calls. When your compiled code calls `printf` from the C library, every one of these details must be exactly right, because the library was compiled with its own ABI assumptions and your code must match them perfectly.
