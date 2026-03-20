---
id: system-call-semantics
title: System Call Semantics and ABI
domain: computer-science
course: operating-systems
prerequisites:
- id: user-kernel-mode-transitions
  type: hard
- id: calling-conventions-abi
  type: soft
builds-toward:
- interrupt-vector-dispatch
tags:
- system-calls
- abi
- interface
stage: advanced
status: draft
---

# System Call Semantics and ABI

## Core Idea
System calls are the formal interface for requesting OS services. The Application Binary Interface (ABI) specifies calling conventions: which registers hold arguments and return values, stack layout, and parameter passing. This standardization enables portable user programs.

## Explainer

You already know that the CPU operates in at least two privilege levels — user mode and kernel mode — and that a transition between them is required whenever a program needs the operating system to do something on its behalf. A **system call** is the specific mechanism that triggers this transition in a controlled, safe way. When your program calls `read()`, `write()`, or `open()`, it is not directly executing kernel code. Instead, it invokes a thin wrapper in the C library that sets up arguments according to a precise contract, places a system call number in a designated register, and then executes a special instruction (like `syscall` on x86-64 or `svc` on ARM) that traps into the kernel. The kernel inspects the system call number, validates the arguments, performs the requested operation, and returns a result.

The **Application Binary Interface (ABI)** is the contract that makes this handoff work. It specifies exactly which CPU register holds the system call number, which registers carry the first, second, and subsequent arguments, where the return value appears, and which registers the kernel promises not to clobber. On Linux x86-64, for example, `rax` holds the syscall number, `rdi`, `rsi`, `rdx`, `r10`, `r8`, and `r9` carry up to six arguments, and the return value comes back in `rax`. If you have studied calling conventions, this will feel familiar — it is essentially the same idea as a function calling convention, but across a privilege boundary instead of between two functions in the same process.

This standardization is what makes user programs portable across kernel versions. As long as the ABI is stable, a compiled binary can invoke system calls on any kernel that honors the same interface, even if the kernel's internal implementation changes completely. It also enables multiple programming languages and compilers to interoperate: a Rust program and a C program on the same system both follow the same ABI when requesting kernel services. The C library (`libc`) typically wraps each system call in a function that handles the register setup, the trap instruction, and error-code translation (converting the kernel's negative error codes into `errno` values), so most programmers interact with system calls through these wrappers rather than writing assembly directly.

Understanding system call semantics also clarifies performance. Every system call involves a **mode switch** — saving user-mode registers, switching to kernel stack, executing kernel code, then restoring state and returning. This is far cheaper than a full context switch between processes, but it is still orders of magnitude more expensive than a regular function call. This cost is why high-performance programs batch operations (reading large chunks at once rather than one byte at a time) and why mechanisms like `io_uring` exist to amortize system call overhead. The ABI is not just a technical detail — it is the boundary that defines what user-space programs can and cannot do, and how efficiently they can ask the kernel for help.
