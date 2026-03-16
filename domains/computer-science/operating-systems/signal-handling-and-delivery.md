---
id: signal-handling-and-delivery
title: Signal Handling and Delivery
domain: computer-science
course: operating-systems
prerequisites:
- id: process-concept-in-os
  type: hard
- id: interrupt-exception-handling
  type: soft
tags:
- signals
- asynchronous
- events
stage: formal-systems
status: draft
---

# Signal Handling and Delivery

## Core Idea
Signals are asynchronous notifications delivered to processes, interrupting their normal execution flow. A process can install signal handlers to respond to specific signals (SIGTERM, SIGUSR1, etc.) or use default behavior (termination, ignoring, core dump). Signal delivery is not guaranteed to be immediate, and blocking signals during critical sections prevents race conditions and data corruption.

## Explainer

You already understand that a process is an isolated unit of execution managed by the OS, and you have some familiarity with how hardware interrupts disrupt the CPU's normal instruction flow. Signals are the software analog of interrupts, but delivered to *processes* rather than to the CPU itself. They are the OS's mechanism for telling a process "something happened that you need to deal with" — a user pressed Ctrl+C, a child process terminated, a timer expired, or another process explicitly sent a notification.

Each signal has a number and a symbolic name. **SIGTERM** (15) politely asks a process to shut down. **SIGKILL** (9) forcibly terminates it — the process cannot catch or ignore this one. **SIGSEGV** (11) indicates a segmentation fault. **SIGCHLD** tells a parent that a child's status changed. When a signal arrives, the process's normal execution is *interrupted* — the OS saves the current instruction pointer and register state, then transfers control to a **signal handler** if the process installed one, or applies the default action (which is often termination). After the handler finishes, execution resumes where it was interrupted, as if nothing happened. This asynchronous interruption is what makes signals both powerful and dangerous.

The danger comes from the fact that a signal can arrive at *any* point during execution — in the middle of updating a data structure, halfway through a library call, or while holding a lock. If the signal handler modifies the same data, you get a race condition. The solution is **signal masking**: a process can temporarily block specific signals during critical sections using sigprocmask(). Blocked signals are not lost — they are held **pending** and delivered as soon as the mask is lifted. This is analogous to disabling interrupts in kernel code, but at the process level. Note that standard signals are not queued: if the same signal is sent multiple times while blocked, only one delivery occurs when the mask is lifted. Real-time signals (SIGRTMIN and above) *are* queued, but standard signals are not.

To install a custom handler, a process uses the sigaction() system call (the older signal() function is less portable and has subtle pitfalls). The handler is a function that receives the signal number as an argument and must be **async-signal-safe** — it can only call a restricted set of functions (write, _exit, and a few others) because most library functions are not safe to call from an interrupted context. A common pattern is for the handler to simply set a global flag variable, and the main loop checks and clears that flag at a safe point. This keeps the handler minimal and moves complex logic back to the normal flow of control, where it is safe to use the full standard library.
