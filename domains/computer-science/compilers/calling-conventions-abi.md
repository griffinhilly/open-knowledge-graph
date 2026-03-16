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
status: draft
---

# Calling Conventions and ABI

## Core Idea
A calling convention specifies how functions are called: how arguments are passed (registers vs stack), where the return value goes, which registers are caller/callee-saved, and how the stack frame is organized. ABIs formalize these conventions so different compilers generate compatible code.

## How It's Best Learned
Study the ABI for your target platform (x86-64 System V ABI, ARM EABI, etc.). Implement function calls that interoperate with system libraries.

## Explainer

When your compiler emits a function call, it must answer a series of concrete questions: Where do the arguments go? Where does the return value appear? Which registers can the called function freely overwrite, and which must it preserve? How is the stack aligned? If your compiler and the C standard library disagree on any of these answers, the program crashes or silently corrupts data. A **calling convention** is the complete specification that answers all of these questions, and an **Application Binary Interface** (ABI) formalizes calling conventions along with data layout, object file format, and other low-level details into a platform-wide contract.

Consider the x86-64 System V ABI used on Linux and macOS. The first six integer arguments go in registers rdi, rsi, rdx, rcx, r8, r9 — in that exact order. Floating-point arguments go in xmm0 through xmm7. Additional arguments spill onto the stack. The return value comes back in rax (or rax:rdx for 128-bit values). Registers rax, rcx, rdx, rsi, rdi, r8, r9, r10, r11 are **caller-saved** — the called function may freely destroy them, so if the caller needs their values after the call, it must save them first. Registers rbx, rbp, r12–r15 are **callee-saved** — the called function must restore them before returning. The stack must be 16-byte aligned before the `call` instruction. Every one of these details is a potential bug if your compiler gets it wrong.

The distinction between **caller-saved** and **callee-saved** registers is a division of labor that minimizes unnecessary work. If a register is caller-saved, the callee can use it as scratch space without any overhead — no saving, no restoring. If a register is callee-saved, the caller can assume it survives the call without doing anything — but the callee pays the cost of preserving and restoring it if it wants to use it. A compiler's register allocator must be aware of these rules: it should prefer caller-saved registers for short-lived temporaries that do not span calls, and callee-saved registers for values that must survive across calls. Getting this allocation right is a significant factor in generated code performance.

Different platforms make different tradeoffs. Windows x64 uses a different convention: only four registers for integer arguments (rcx, rdx, r8, r9), and the caller must always allocate a 32-byte "shadow space" on the stack even if all arguments fit in registers. ARM uses r0–r3 for the first four arguments and has a link register (lr) instead of pushing the return address on the stack. These differences mean that a compiler targeting multiple platforms needs a clean abstraction layer for call generation. ABIs also specify **struct passing** rules — small structs may be passed in registers, large ones by hidden pointer — and **variadic function** conventions, which often differ from normal calls. When your compiled code calls `printf` from the C library, every one of these details must be exactly right, because the library was compiled with its own ABI assumptions and your code must match them perfectly.
