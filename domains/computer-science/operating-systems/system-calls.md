---
id: system-calls
title: System Calls and User/Kernel Mode
domain: computer-science
course: operating-systems
prerequisites:
- id: instruction-set-architecture
  type: hard
- id: kernel-architecture
  type: soft
builds-toward:
- process-concept
- inter-process-communication
- io-management
tags:
- system-call
- user-mode
- kernel-mode
- trap
- privilege
stage: formal-systems
status: validated
---

# System Calls and User/Kernel Mode

## Core Idea
CPUs operate in at least two privilege levels: user mode (restricted) and kernel mode (unrestricted). A system call is the controlled mechanism by which user-space programs request privileged services from the kernel, such as reading a file, spawning a process, or allocating memory. The call triggers a software interrupt or trap instruction that switches the CPU into kernel mode, executes the requested service, and returns control to user mode. The POSIX API (read, write, fork, exec, etc.) defines the standard system call interface on Unix-like systems.

## How It's Best Learned
Use strace on Linux to observe which system calls a program makes. Then inspect how a simple write() call propagates from C library through libc wrapper, into the kernel, and back.

## Common Misconceptions
- Calling a C standard library function (printf) is NOT a system call itself; it eventually wraps one (write).
- System calls are expensive relative to function calls because mode-switching flushes CPU pipeline state.

## Questions

```yaml
- question: "A C program calls printf(\"Hello\"). At what point does execution cross from user mode into kernel mode?"
  type: multiple-choice
  options:
    - "Immediately when printf() is called, since printf() is a system call"
    - "When the C standard library internally calls the write() system call to send bytes to the terminal"
    - "Never — modern CPUs execute printf() directly without involving the kernel"
    - "When the program is compiled, since the compiler inserts kernel calls at compile time"
  answer: 1
  explanation: "printf() is a library function that runs entirely in user mode. It formats the string, buffers output, and eventually calls write() — the actual system call — which triggers the trap instruction to switch into kernel mode. The user/kernel boundary is crossed at write(), not at printf(). This layering means most of the work happens in user space; the kernel is invoked only for the final privileged operation of writing bytes to the file descriptor."

- question: "Why are system calls significantly more expensive than ordinary function calls within a program?"
  type: multiple-choice
  options:
    - "System calls require network access to communicate with the OS server"
    - "The kernel must validate that the requested operation is legal before executing it"
    - "Mode-switching saves all user-mode register state, flushes CPU pipeline state, and reverses the entire process on return — multiplying the cost of a simple function call many times over"
    - "System calls use interpreted code rather than compiled machine instructions"
  answer: 2
  explanation: "A regular function call takes a few nanoseconds (push arguments, jump, return). A system call involves saving all user-mode register state, switching privilege levels, potentially flushing CPU pipeline and cache state, executing kernel code, then reversing the entire sequence. This is why well-designed programs batch small operations into fewer, larger system calls — e.g., buffering many writes into one large write() — rather than making many small calls. Option B (validation) is part of what the kernel does but is not the primary source of overhead."

- question: "Calling the C standard library function printf() is itself a system call that directly transitions the CPU into kernel mode."
  type: true-false
  answer: false
  explanation: "printf() is a user-space library function. It runs entirely in user mode, performing string formatting and output buffering, before eventually calling write() — the actual system call — which triggers the mode switch. The distinction matters architecturally: the C standard library sits between application code and the kernel, providing a higher-level interface that often batches and buffers operations before making the privileged kernel call. You can observe this layering directly with strace, which shows only the actual system calls, not library function calls."

- question: "The separation between user mode and kernel mode exists to prevent buggy or malicious programs from crashing the entire system by directly accessing hardware or modifying other processes' memory."
  type: true-false
  answer: true
  explanation: "This is the fundamental purpose of the privilege boundary. In user mode, programs can execute arithmetic and logic but cannot directly access hardware, modify page tables, or touch another process's memory. Only kernel mode has unrestricted hardware access. Without this boundary, a single buffer overflow in a web browser could corrupt the filesystem — the kernel's protection prevents any user-space bug or attack from directly harming the whole system."

- question: "What mechanism allows a user-space program to request a privileged operation from the kernel without compromising the user/kernel protection boundary, and how does the CPU ensure the transition is controlled?"
  type: short-answer
  answer: "The user-space program places the system call number and arguments into specific CPU registers, then executes a trap instruction (such as syscall on x86-64 or svc on ARM). This instruction simultaneously switches the CPU into kernel mode and jumps to a fixed, predefined entry point in the kernel — not to an arbitrary address supplied by the user program. The kernel validates the arguments, performs the privileged operation, puts the result in a register, then switches back to user mode. The key security property is that the trap always enters the kernel at a known address, so user code cannot redirect kernel execution to arbitrary locations."
  explanation: "The trap instruction is the controlled gateway that makes the boundary meaningful. If user programs could switch to kernel mode and jump anywhere, the protection would be illusory. By forcing all mode transitions through a single kernel entry point, the OS can validate every request and prevent privilege escalation. This is why system calls must pass through a predefined interface (POSIX: read, write, fork, exec, etc.) rather than calling arbitrary kernel functions directly."
```

## Explainer

From your study of instruction set architecture, you know that the CPU executes instructions one after another, and that different instructions have different privileges. The key insight behind system calls is that modern CPUs enforce a **protection boundary** between two (or more) privilege levels. In **user mode**, programs can execute normal arithmetic and logic but cannot directly access hardware, modify page tables, or touch another process's memory. In **kernel mode**, the operating system has unrestricted access to everything. This separation exists to prevent a buggy or malicious program from crashing the entire system — if your web browser could directly write to disk sectors, a single bug could corrupt your filesystem.

But user programs still need to do things that require privilege: reading files, sending network packets, creating new processes. The **system call** is the controlled gateway between these two worlds. When your program calls `read()` to get data from a file, it doesn't directly access the disk. Instead, the C library places the system call number and arguments into specific CPU registers and executes a special **trap instruction** (like `syscall` on x86-64 or `svc` on ARM). This instruction simultaneously switches the CPU into kernel mode and jumps to a predefined entry point in the kernel. The kernel examines the request, validates the arguments, performs the privileged operation, places the result in a register, and switches back to user mode. Your program resumes as if it just returned from a normal function call.

The distinction between library functions and system calls trips up many beginners. When you call `printf("hello")` in C, you're calling a library function that formats your string, buffers it, and eventually calls the `write()` system call to actually send bytes to the terminal. The library function runs entirely in user mode; only `write()` crosses into the kernel. You can observe this directly using tools like **strace** on Linux, which intercepts and logs every system call a program makes. Running `strace ls` reveals dozens of calls — `openat()`, `read()`, `write()`, `close()` — showing that even a simple directory listing involves a rich conversation between user space and kernel space.

System calls are significantly more expensive than ordinary function calls. A regular function call might take a few nanoseconds — push arguments, jump, return. A system call involves saving all user-mode register state, switching privilege levels, potentially flushing CPU pipeline and cache state, executing the kernel code, then reversing the entire process. This overhead is why well-designed programs minimize system calls — buffering many small writes into one large `write()` call, for instance, or using memory-mapped files to avoid repeated `read()` calls. The POSIX standard defines the common system call interface (`read`, `write`, `fork`, `exec`, `open`, `close`, `mmap`, etc.) that Unix-like systems implement, giving programmers a portable vocabulary for requesting kernel services.
