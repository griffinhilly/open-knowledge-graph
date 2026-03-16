---
id: process-creation-fork-exec
title: 'Process Creation: fork() and exec()'
domain: computer-science
course: operating-systems
prerequisites:
- id: process-concept-in-os
  type: hard
- id: kernel-mode-and-privilege-levels
  type: soft
builds-toward:
- process-termination-and-cleanup
- process-states-and-transitions
tags:
- system-calls
- process-lifecycle
- unix-api
stage: formal-systems
status: draft
---

# Process Creation: fork() and exec()

## Core Idea
Processes are created via system calls like fork() (Unix/Linux) or CreateProcess() (Windows). fork() creates a child process as a copy of the parent; exec() replaces the current process image with a new program. Together, they enable process spawning and program execution in Unix-like systems.

## Common Misconceptions
fork() returns twice (it does: once in the parent returning the child's PID, once in the child returning 0). exec() returns on error (it never returns on success; the process image is replaced).

## Explainer

You know from the process concept that a process is a running program with its own address space, registers, and OS-managed state. But how does a new process come into existence? In Unix-like systems, the answer is surprisingly simple: every process is created by an existing process using the **fork()** system call. There is no "create process from scratch" operation — even the first user process (init or systemd) is forked by the kernel during boot. This means every process has a parent, forming a tree rooted at the init process.

When a process calls **fork()**, the kernel creates a new child process that is a near-exact copy of the parent. The child gets a duplicate of the parent's address space (code, data, heap, stack), the same open file descriptors, and the same register state — including the program counter, so the child resumes execution at the exact same point in the code as the parent. The only difference is the return value of fork(): it returns the child's process ID (PID) to the parent, and 0 to the child. This single difference lets the program branch: `if (fork() == 0) { /* child code */ } else { /* parent code */ }`. It may seem strange that one function call produces two return values, but it makes sense once you realize that after fork(), there are two independent processes running the same code — each receives its own return value.

Fork alone is only half the story. A child that is an exact copy of its parent is rarely useful — you usually want the child to run a different program. That is where **exec()** comes in. The exec family of system calls (execl, execv, execvp, etc.) replaces the current process's entire address space with a new program loaded from an executable file. The process ID stays the same, open file descriptors are preserved (unless marked close-on-exec), but the code, data, stack, and heap are replaced completely. Exec never returns on success because there is nothing to return to — the old program is gone. It only returns if loading the new program fails (e.g., file not found, permission denied).

The **fork-then-exec** pattern is the standard Unix idiom for launching programs. A shell, for example, forks a child process, and the child calls exec to run the command you typed. The parent (the shell) waits for the child to finish using **wait()** or **waitpid()**, then prints the next prompt. This two-step design is deliberate and powerful: the window between fork and exec gives the child a chance to set up its environment — redirect file descriptors (for I/O redirection like `> output.txt`), change the working directory, adjust signal handlers, or drop privileges — before the new program starts. Combining these simple primitives gives Unix its characteristic composability: pipes, background jobs, and process supervision all emerge from fork, exec, and wait.
