---
id: signal-handling-and-delivery
title: Signal Handling and Delivery
domain: computer-science
course: operating-systems
prerequisites:
- id: process-concept
  type: hard
- id: interrupts-and-dma
  type: soft
tags:
- signals
- asynchronous
- events
stage: formal-systems
status: validated
---

# Signal Handling and Delivery

## Core Idea
Signals are asynchronous notifications delivered to processes, interrupting their normal execution flow. A process can install signal handlers to respond to specific signals (SIGTERM, SIGUSR1, etc.) or use default behavior (termination, ignoring, core dump). Signal delivery is not guaranteed to be immediate, and blocking signals during critical sections prevents race conditions and data corruption.

## Questions

```yaml
- question: "A process is in the middle of updating a doubly-linked list when SIGUSR1 arrives. The signal handler also modifies the same list. What is the most likely outcome?"
  type: multiple-choice
  options:
    - "No problem — signal handlers run in a separate thread and cannot interfere with the main process"
    - "A race condition or data corruption, because the signal interrupts execution at an arbitrary instruction"
    - "The signal is automatically queued until the linked-list update completes safely"
    - "The handler waits for the main code to finish the current operation before executing"
  answer: 1
  explanation: "Signals interrupt execution at literally any instruction — there is no implicit synchronization. If the main code is halfway through relinking nodes when the handler runs and also modifies the list, the data structure can be left corrupt (e.g., a next pointer updated but prev not yet). The correct fix is to block the signal during the critical section with sigprocmask(), or have the handler only set a flag so the actual list modification happens later in the main loop where it's safe."

- question: "A signal handler needs to trigger complex processing: writing a log file and restarting a service. What is the most correct implementation pattern?"
  type: multiple-choice
  options:
    - "Put all the complex logic directly in the handler for the fastest possible response time"
    - "Call printf() and system() from within the handler — they are standard library functions"
    - "Set a global volatile flag in the handler; check and clear it in the main loop where full library access is safe"
    - "Use a nested signal handler inside the first to process the complex work"
  answer: 2
  explanation: "Signal handlers must be async-signal-safe — they can only call a restricted POSIX list of functions (write(), _exit(), and roughly 70 others). printf() and system() are NOT async-signal-safe because they may use internal locks or non-reentrant state. If the signal interrupts the main code while it's inside printf(), and the handler also calls printf(), you get deadlock or corruption. The correct pattern: minimal handler sets a volatile flag; main loop checks the flag at a safe point and performs complex work using the full standard library."

- question: "A signal blocked via sigprocmask() is not discarded — it is held pending and delivered when the mask is lifted."
  type: true-false
  answer: true
  explanation: "Signal masking delays delivery, it does not discard signals. The OS marks a blocked signal as 'pending' and delivers it as soon as the process restores the previous mask. This makes signal masking a correct synchronization tool for protecting critical sections — you defer the interruption to a safe point. Important caveat: standard signals are not queued if the same signal arrives multiple times while blocked (only one delivery occurs); real-time signals (SIGRTMIN and above) are fully queued."

- question: "SIGKILL can be caught by installing a custom signal handler, allowing a process to perform cleanup before exiting."
  type: true-false
  answer: false
  explanation: "SIGKILL (signal 9) is deliberately unblockable and uncatchable — the OS terminates the process directly, bypassing any installed handler. This is by design: it provides a guaranteed last-resort termination that cannot be subverted by a buggy or uncooperative process. SIGTERM (signal 15) is the polite version that *can* be caught and handled, allowing graceful shutdown with cleanup. If you want to intercept shutdown, install a SIGTERM handler — not a SIGKILL handler, which is impossible."

- question: "Why must signal handlers be 'async-signal-safe,' and what does this restriction mean in practice?"
  type: short-answer
  answer: "A signal can interrupt the main process at any instruction — including in the middle of a library function like malloc() or printf() that uses internal locks or non-reentrant global state. If the handler calls those same functions, you risk deadlock (trying to acquire a lock already held by the interrupted code) or state corruption (two executions of non-reentrant code sharing data simultaneously). Async-signal-safe functions are those that can be safely re-entered or that use only atomic operations. The POSIX standard lists about 70 safe functions; most of the standard C library is excluded. In practice, this means handlers should do minimal work — set a volatile sig_atomic_t flag — and defer all complex logic to the main loop where the full library is safely available."
  explanation: "The restriction exists because signals create concurrency within a single thread of control: the handler and main code share address space and can truly execute in conflicting states. Understanding async-signal-safety is the core technical skill for writing correct signal-driven programs."
```

## Explainer

You already understand that a process is an isolated unit of execution managed by the OS, and you have some familiarity with how hardware interrupts disrupt the CPU's normal instruction flow. Signals are the software analog of interrupts, but delivered to *processes* rather than to the CPU itself. They are the OS's mechanism for telling a process "something happened that you need to deal with" — a user pressed Ctrl+C, a child process terminated, a timer expired, or another process explicitly sent a notification.

Each signal has a number and a symbolic name. **SIGTERM** (15) politely asks a process to shut down. **SIGKILL** (9) forcibly terminates it — the process cannot catch or ignore this one. **SIGSEGV** (11) indicates a segmentation fault. **SIGCHLD** tells a parent that a child's status changed. When a signal arrives, the process's normal execution is *interrupted* — the OS saves the current instruction pointer and register state, then transfers control to a **signal handler** if the process installed one, or applies the default action (which is often termination). After the handler finishes, execution resumes where it was interrupted, as if nothing happened. This asynchronous interruption is what makes signals both powerful and dangerous.

The danger comes from the fact that a signal can arrive at *any* point during execution — in the middle of updating a data structure, halfway through a library call, or while holding a lock. If the signal handler modifies the same data, you get a race condition. The solution is **signal masking**: a process can temporarily block specific signals during critical sections using sigprocmask(). Blocked signals are not lost — they are held **pending** and delivered as soon as the mask is lifted. This is analogous to disabling interrupts in kernel code, but at the process level. Note that standard signals are not queued: if the same signal is sent multiple times while blocked, only one delivery occurs when the mask is lifted. Real-time signals (SIGRTMIN and above) *are* queued, but standard signals are not.

To install a custom handler, a process uses the sigaction() system call (the older signal() function is less portable and has subtle pitfalls). The handler is a function that receives the signal number as an argument and must be **async-signal-safe** — it can only call a restricted set of functions (write, _exit, and a few others) because most library functions are not safe to call from an interrupted context. A common pattern is for the handler to simply set a global flag variable, and the main loop checks and clears that flag at a safe point. This keeps the handler minimal and moves complex logic back to the normal flow of control, where it is safe to use the full standard library.
