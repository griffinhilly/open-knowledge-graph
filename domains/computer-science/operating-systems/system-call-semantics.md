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
stage: formal-systems
status: draft
---

# System Call Semantics and ABI

## Core Idea
System calls are the formal interface for requesting OS services. The Application Binary Interface (ABI) specifies calling conventions: which registers hold arguments and return values, stack layout, and parameter passing. This standardization enables portable user programs.

## Questions

```yaml
- question: "On Linux x86-64, a program needs to call the `write` system call (number 1). Which of the following correctly describes the ABI contract before executing the `syscall` instruction?"
  type: multiple-choice
  options:
    - "Push the syscall number and arguments onto the stack; the kernel reads from the stack"
    - "Place syscall number in `rax`, file descriptor in `rdi`, buffer pointer in `rsi`, byte count in `rdx`"
    - "Place syscall number in `rdi`, file descriptor in `rax`, and remaining arguments in caller-saved registers"
    - "Call the kernel entry point directly as a function using the standard C calling convention"
  answer: 1
  explanation: "On Linux x86-64, `rax` holds the system call number, and the first three arguments go in `rdi`, `rsi`, `rdx` respectively. For `write(fd, buf, count)`, that's: `rax=1`, `rdi=fd`, `rsi=buf_ptr`, `rdx=count`. This is *not* the same as the user-space function calling convention (which also uses `rdi`, `rsi`, `rdx` for function arguments, but `rdi` is the first argument there — the system call convention reuses similar registers but with `rax` carrying the syscall number, not a function pointer)."

- question: "Why is a system call significantly more expensive than a regular function call, even though both transfer control to another routine?"
  type: multiple-choice
  options:
    - "System calls require copying all arguments from registers to memory before the kernel can read them"
    - "System calls invoke a mode switch: saving user-mode state, switching to the kernel stack, executing privileged code, then restoring state on return"
    - "System calls must validate argument types, while function calls assume correct types from the compiler"
    - "System calls require acquiring a global kernel lock before any operation can proceed"
  answer: 1
  explanation: "The fundamental cost of a system call is the *privilege mode transition*: the CPU must save user-mode register state, switch to the kernel stack, transfer control to a kernel entry point, execute the kernel code, then restore state and return to user mode. This involves flushing parts of the pipeline and TLB, loading kernel mappings, and executing multiple privileged instructions — typically 50–100× more expensive than a simple function call. Options A and C describe validation work that may or may not occur; option D is false (many system calls do not require a global lock)."

- question: "A compiled Rust program and a compiled C program on the same Linux system call `read()` using incompatible calling conventions, so the kernel must detect which language made the call."
  type: true-false
  answer: false
  explanation: "The ABI is language-agnostic. Both Rust and C (through their respective libc wrappers) ultimately place the syscall number in `rax` and arguments in the designated registers before issuing the `syscall` instruction. The kernel has no idea — and does not care — what language generated the trap. This language-neutrality is precisely the point of the ABI: it defines a stable binary interface that any language or runtime can target, enabling interoperability without any language-awareness in the kernel."

- question: "Keeping the system call ABI stable across kernel versions means that a binary compiled against Linux 4.x will still work correctly on Linux 6.x without recompilation."
  type: true-false
  answer: true
  explanation: "Linux maintains a strict ABI compatibility guarantee: system call numbers and their register conventions do not change between kernel versions. A binary that uses syscall number 1 for `write` on kernel 4.x will find the same interface on kernel 6.x. This is a deliberate design goal — the ABI stability is what allows long-lived binaries (and the vast ecosystem of compiled software) to run across kernel upgrades without recompilation. Internal kernel implementation can change radically as long as the ABI contract at the user/kernel boundary is preserved."

- question: "Explain why high-performance programs try to minimize the number of system calls, and give a concrete example of a technique that reduces system call overhead."
  type: short-answer
  answer: "Every system call triggers a privilege mode transition — saving/restoring registers, switching stacks, and running kernel code — which costs roughly 50–100× a normal function call. High-performance programs amortize this overhead by batching work: reading a large buffer in one `read()` call instead of one byte at a time, or using `io_uring` to submit many I/O operations in a single ring buffer submission without a syscall per operation."
  explanation: "The mode-switch cost is fixed per syscall regardless of how little work the kernel does. Reading 1 byte and reading 4096 bytes both pay the same transition cost. Batching (large reads/writes) or asynchronous I/O interfaces like `io_uring` reduce the ratio of mode-switch overhead to useful work, yielding dramatically better throughput for I/O-intensive workloads."
```

## Explainer

You already know that the CPU operates in at least two privilege levels — user mode and kernel mode — and that a transition between them is required whenever a program needs the operating system to do something on its behalf. A **system call** is the specific mechanism that triggers this transition in a controlled, safe way. When your program calls `read()`, `write()`, or `open()`, it is not directly executing kernel code. Instead, it invokes a thin wrapper in the C library that sets up arguments according to a precise contract, places a system call number in a designated register, and then executes a special instruction (like `syscall` on x86-64 or `svc` on ARM) that traps into the kernel. The kernel inspects the system call number, validates the arguments, performs the requested operation, and returns a result.

The **Application Binary Interface (ABI)** is the contract that makes this handoff work. It specifies exactly which CPU register holds the system call number, which registers carry the first, second, and subsequent arguments, where the return value appears, and which registers the kernel promises not to clobber. On Linux x86-64, for example, `rax` holds the syscall number, `rdi`, `rsi`, `rdx`, `r10`, `r8`, and `r9` carry up to six arguments, and the return value comes back in `rax`. If you have studied calling conventions, this will feel familiar — it is essentially the same idea as a function calling convention, but across a privilege boundary instead of between two functions in the same process.

This standardization is what makes user programs portable across kernel versions. As long as the ABI is stable, a compiled binary can invoke system calls on any kernel that honors the same interface, even if the kernel's internal implementation changes completely. It also enables multiple programming languages and compilers to interoperate: a Rust program and a C program on the same system both follow the same ABI when requesting kernel services. The C library (`libc`) typically wraps each system call in a function that handles the register setup, the trap instruction, and error-code translation (converting the kernel's negative error codes into `errno` values), so most programmers interact with system calls through these wrappers rather than writing assembly directly.

Understanding system call semantics also clarifies performance. Every system call involves a **mode switch** — saving user-mode registers, switching to kernel stack, executing kernel code, then restoring state and returning. This is far cheaper than a full context switch between processes, but it is still orders of magnitude more expensive than a regular function call. This cost is why high-performance programs batch operations (reading large chunks at once rather than one byte at a time) and why mechanisms like `io_uring` exist to amortize system call overhead. The ABI is not just a technical detail — it is the boundary that defines what user-space programs can and cannot do, and how efficiently they can ask the kernel for help.
