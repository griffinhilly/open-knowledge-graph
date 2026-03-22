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

## Questions

```yaml
- question: "A program calls fork(). After fork() returns, how many processes are executing the instruction immediately after the fork() call?"
  type: multiple-choice
  options:
    - "One — the parent continues and the child starts from the beginning of main()"
    - "One — the child takes over execution and the parent is suspended"
    - "Two — both parent and child resume at the same point with different return values"
    - "Two — the parent continues normally; the child automatically starts a new program"
  answer: 2
  explanation: "After fork(), both the parent and child resume execution at exactly the same point — immediately after the fork() call — because the child is a copy of the parent's entire state, including the program counter. The parent receives the child's PID as the return value; the child receives 0. This is why fork() is said to 'return twice': there are now two processes running the same code, each branching based on which return value they received."

- question: "A child process calls execvp() to run a new program. The call succeeds. What happens to the child process's original code, stack, and heap?"
  type: multiple-choice
  options:
    - "They are preserved and available when the new program finishes"
    - "They are saved to disk and restored if exec() is called again"
    - "They are completely replaced by the new program's image; exec() does not return"
    - "They are shared with the parent process via copy-on-write until the child exits"
  answer: 2
  explanation: "exec() replaces the entire process image — code, data, heap, stack — with the new program loaded from the executable file. The process ID stays the same, but everything else is replaced. exec() does not return on success because there is nothing to return to: the old program no longer exists in that process. It only returns if loading the new program fails (e.g., file not found, permission denied). A common bug is writing code after exec() assuming it will run on success."

- question: "After fork() is called, the child process starts execution from the beginning of the main() function."
  type: true-false
  answer: false
  explanation: "The child does NOT start from main(). It resumes at the instruction immediately after the fork() call, because the child is a copy of the parent's state including the program counter. The return value (0 for the child, the child's PID for the parent) is the only difference between the two processes. This surprises many students who expect process creation to behave like starting a fresh program."

- question: "The fork-then-exec pattern gives the child process an opportunity to configure its environment — such as redirecting file descriptors — before the new program starts."
  type: true-false
  answer: true
  explanation: "The window between fork() and exec() is intentional and powerful. Because the child runs the same code as the parent but can execute any operations before exec(), it can redirect stdin/stdout, change the working directory, set signal handlers, or drop privileges — all before the new program takes over. This is exactly how shell I/O redirection works: the child sets up file descriptor redirections (e.g., for > output.txt), then execs the command."

- question: "Explain why it is said that fork() 'returns twice.' What does each return value mean, and how does a program use them to take different actions in the parent vs. the child?"
  type: short-answer
  answer: "After fork(), there are two processes running the same code. The parent receives the child's PID (a positive integer) as the return value; the child receives 0. The program tests this value to branch: if fork() returned 0, the current process is the child; if it returned a positive number, the current process is the parent. 'Returns twice' means one call produced two outcomes in two separate processes — each process sees its own return value."
  explanation: "The apparent paradox resolves once you understand that after fork() there are two execution paths. From each path's perspective, fork() returned exactly once — they just received different values. This is why the idiom `if (fork() == 0) { /* child */ } else { /* parent */ }` works: the condition evaluates differently in each process, allowing a single code path to implement two roles. Understanding this also clarifies why the child resumes mid-program rather than starting fresh."
```

## Explainer

You know from the process concept that a process is a running program with its own address space, registers, and OS-managed state. But how does a new process come into existence? In Unix-like systems, the answer is surprisingly simple: every process is created by an existing process using the **fork()** system call. There is no "create process from scratch" operation — even the first user process (init or systemd) is forked by the kernel during boot. This means every process has a parent, forming a tree rooted at the init process.

When a process calls **fork()**, the kernel creates a new child process that is a near-exact copy of the parent. The child gets a duplicate of the parent's address space (code, data, heap, stack), the same open file descriptors, and the same register state — including the program counter, so the child resumes execution at the exact same point in the code as the parent. The only difference is the return value of fork(): it returns the child's process ID (PID) to the parent, and 0 to the child. This single difference lets the program branch: `if (fork() == 0) { /* child code */ } else { /* parent code */ }`. It may seem strange that one function call produces two return values, but it makes sense once you realize that after fork(), there are two independent processes running the same code — each receives its own return value.

Fork alone is only half the story. A child that is an exact copy of its parent is rarely useful — you usually want the child to run a different program. That is where **exec()** comes in. The exec family of system calls (execl, execv, execvp, etc.) replaces the current process's entire address space with a new program loaded from an executable file. The process ID stays the same, open file descriptors are preserved (unless marked close-on-exec), but the code, data, stack, and heap are replaced completely. Exec never returns on success because there is nothing to return to — the old program is gone. It only returns if loading the new program fails (e.g., file not found, permission denied).

The **fork-then-exec** pattern is the standard Unix idiom for launching programs. A shell, for example, forks a child process, and the child calls exec to run the command you typed. The parent (the shell) waits for the child to finish using **wait()** or **waitpid()**, then prints the next prompt. This two-step design is deliberate and powerful: the window between fork and exec gives the child a chance to set up its environment — redirect file descriptors (for I/O redirection like `> output.txt`), change the working directory, adjust signal handlers, or drop privileges — before the new program starts. Combining these simple primitives gives Unix its characteristic composability: pipes, background jobs, and process supervision all emerge from fork, exec, and wait.
