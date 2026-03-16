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

## Explainer

From your study of instruction set architecture, you know that the CPU executes instructions one after another, and that different instructions have different privileges. The key insight behind system calls is that modern CPUs enforce a **protection boundary** between two (or more) privilege levels. In **user mode**, programs can execute normal arithmetic and logic but cannot directly access hardware, modify page tables, or touch another process's memory. In **kernel mode**, the operating system has unrestricted access to everything. This separation exists to prevent a buggy or malicious program from crashing the entire system — if your web browser could directly write to disk sectors, a single bug could corrupt your filesystem.

But user programs still need to do things that require privilege: reading files, sending network packets, creating new processes. The **system call** is the controlled gateway between these two worlds. When your program calls `read()` to get data from a file, it doesn't directly access the disk. Instead, the C library places the system call number and arguments into specific CPU registers and executes a special **trap instruction** (like `syscall` on x86-64 or `svc` on ARM). This instruction simultaneously switches the CPU into kernel mode and jumps to a predefined entry point in the kernel. The kernel examines the request, validates the arguments, performs the privileged operation, places the result in a register, and switches back to user mode. Your program resumes as if it just returned from a normal function call.

The distinction between library functions and system calls trips up many beginners. When you call `printf("hello")` in C, you're calling a library function that formats your string, buffers it, and eventually calls the `write()` system call to actually send bytes to the terminal. The library function runs entirely in user mode; only `write()` crosses into the kernel. You can observe this directly using tools like **strace** on Linux, which intercepts and logs every system call a program makes. Running `strace ls` reveals dozens of calls — `openat()`, `read()`, `write()`, `close()` — showing that even a simple directory listing involves a rich conversation between user space and kernel space.

System calls are significantly more expensive than ordinary function calls. A regular function call might take a few nanoseconds — push arguments, jump, return. A system call involves saving all user-mode register state, switching privilege levels, potentially flushing CPU pipeline and cache state, executing the kernel code, then reversing the entire process. This overhead is why well-designed programs minimize system calls — buffering many small writes into one large `write()` call, for instance, or using memory-mapped files to avoid repeated `read()` calls. The POSIX standard defines the common system call interface (`read`, `write`, `fork`, `exec`, `open`, `close`, `mmap`, etc.) that Unix-like systems implement, giving programmers a portable vocabulary for requesting kernel services.
