---
id: process-states-and-transitions
title: Process States and State Transitions
domain: computer-science
course: operating-systems
prerequisites:
- id: process-creation-fork-exec
  type: hard
- id: process-termination-and-cleanup
  type: soft
builds-toward:
- context-switching-and-cpu-dispatch
- cpu-scheduling-basic-concepts
tags:
- process-lifecycle
- scheduling
- state-machine
stage: formal-systems
status: validated
---

# Process States and State Transitions

## Core Idea
Processes cycle through states: new (created), ready (waiting for CPU), running (executing), blocked (waiting for I/O or event), and terminated. State transitions are triggered by the scheduler, I/O completion, or system calls. Understanding the process state machine is fundamental to comprehending OS behavior and scheduling.

## Questions

```yaml
- question: "A process issues a read() system call to load data from disk. While it waits, another process runs. When the disk read completes, where does the first process go?"
  type: multiple-choice
  options:
    - "Directly back to running — it resumes from where it left off as soon as the I/O finishes"
    - "To the ready queue — the scheduler decides when it next receives CPU time"
    - "To the blocked state again until an explicit wake-up call from the user"
    - "To the terminated state because the I/O operation has completed"
  answer: 1
  explanation: "When I/O completes, an interrupt fires and the OS moves the process from blocked to ready — not directly to running. The scheduler still decides which ready process runs next; the formerly-blocked process must compete with all other ready processes for CPU time. Assuming it jumps directly to running confuses two separate mechanisms: the I/O completion interrupt (which unblocks the process) and the scheduler dispatch (which grants CPU time). These are independent events."

- question: "What causes a running process to transition to the ready state rather than the blocked state?"
  type: multiple-choice
  options:
    - "The process calls exit() to finish execution"
    - "The process issues a blocking system call (e.g., waiting for keyboard input)"
    - "A timer interrupt preempts the process at the end of its CPU time slice"
    - "The process encounters a page fault requiring a disk read"
  answer: 2
  explanation: "Preemption by timer interrupt sends the process from running back to ready — it has done nothing wrong and is still fully capable of running; the OS simply decided another process should have a turn. In contrast, a blocking system call (option B) or a page fault (option D) sends the process to blocked, because it genuinely cannot proceed until an external event occurs. The key distinction is whether the process has work it could do right now (ready) or is waiting for something it needs (blocked)."

- question: "A blocked process consumes CPU time while waiting for its I/O request to complete."
  type: true-false
  answer: false
  explanation: "False. A blocked process is parked entirely — it is not in the run queue and will not be selected by the scheduler. It consumes no CPU time. This is the efficiency gain of blocking I/O: while one process waits for slow I/O, the CPU can run other processes productively. The OS maintains a separate waiting structure (e.g., a wait queue associated with the I/O device) for blocked processes, distinct from the ready queue from which the scheduler picks."

- question: "When the event a blocked process was waiting for occurs, the OS may move it directly to the running state if no other process is using the CPU."
  type: true-false
  answer: false
  explanation: "False. When an event completes, the OS always moves the process from blocked to ready — never directly to running, even if the CPU is idle. The scheduler then selects the highest-priority ready process to run. This two-step indirection (blocked → ready → running) keeps the scheduling decision centralized in the scheduler rather than scattered across interrupt handlers. In practice, the formerly-blocked process may be dispatched almost immediately if it has high priority, but the state machine still passes through 'ready.'"

- question: "What is the fundamental difference between a process in the ready state and one in the blocked state, and why does that difference matter for the scheduler?"
  type: short-answer
  answer: "A ready process has everything it needs to execute and is simply waiting for CPU time. A blocked process is waiting for an external event (I/O completion, a timer, a signal) and cannot make progress even if given the CPU. The scheduler only considers ready processes when deciding who to run next — blocked processes are invisible to it. This matters because assigning CPU time to a blocked process would be wasted: the process would immediately suspend again. By separating these states, the OS ensures the CPU is always given to a process that can actually do useful work."
  explanation: "The distinction is not about priority or importance — it is about whether the process is 'runnable right now.' A high-priority process waiting for a network packet is blocked; a low-priority process that just needs CPU time is ready. The scheduler serves the ready queue exclusively. When blocked processes unblock (their event occurs), they join the ready queue and the scheduler can then consider them. This separation is the mechanism that allows an OS to keep the CPU busy even when some processes are stuck waiting for slow I/O."
```

## Explainer

You already know that fork() creates a new process and exec() loads a program into it. But once a process exists, it does not simply "run until done." The operating system manages potentially hundreds of processes on a handful of CPUs, and it does so by assigning each process a **state** that determines whether it is eligible for CPU time. The five classical states — new, ready, running, blocked, and terminated — form a state machine that governs every process's lifecycle.

When fork() returns successfully, the child process enters the **new** state. The OS allocates a process control block (PCB), assigns a PID, and sets up memory mappings. Once initialization is complete, the process moves to **ready**, meaning it has everything it needs to execute and is simply waiting for the scheduler to pick it. The transition from ready to **running** happens when the scheduler dispatches the process onto a CPU — the process's saved registers are loaded, and it begins (or resumes) executing instructions.

The critical insight is what pulls a process *out* of the running state. Two things can happen. First, the scheduler may **preempt** the process — its time slice expires, or a higher-priority process becomes ready — and the process returns to the ready state without having done anything wrong. Second, the process may request something that cannot complete immediately, such as reading from disk or waiting for a network packet. At that point the process enters the **blocked** state. A blocked process is not competing for CPU time at all; it is parked until the event it is waiting for occurs. When the I/O completes or the event fires, the OS moves the process back to ready — not directly to running, because the scheduler still decides who runs next.

Finally, when a process calls exit() or is killed by a signal, it enters the **terminated** state. As you learned from process termination and cleanup, the process's resources are released, but its PCB may linger as a zombie until the parent collects its exit status. The entire state machine can be drawn as a directed graph with five nodes and a handful of edges, and every transition corresponds to a concrete OS mechanism: the scheduler dispatches (ready → running), the timer interrupt preempts (running → ready), a blocking system call waits (running → blocked), an interrupt signals completion (blocked → ready), and exit or a fatal signal terminates (running → terminated). Internalizing this diagram is the foundation for understanding CPU scheduling, context switching, and everything the OS does to juggle multiple processes on limited hardware.
