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
status: draft
---

# Process States and State Transitions

## Core Idea
Processes cycle through states: new (created), ready (waiting for CPU), running (executing), blocked (waiting for I/O or event), and terminated. State transitions are triggered by the scheduler, I/O completion, or system calls. Understanding the process state machine is fundamental to comprehending OS behavior and scheduling.

## Explainer

You already know that fork() creates a new process and exec() loads a program into it. But once a process exists, it does not simply "run until done." The operating system manages potentially hundreds of processes on a handful of CPUs, and it does so by assigning each process a **state** that determines whether it is eligible for CPU time. The five classical states — new, ready, running, blocked, and terminated — form a state machine that governs every process's lifecycle.

When fork() returns successfully, the child process enters the **new** state. The OS allocates a process control block (PCB), assigns a PID, and sets up memory mappings. Once initialization is complete, the process moves to **ready**, meaning it has everything it needs to execute and is simply waiting for the scheduler to pick it. The transition from ready to **running** happens when the scheduler dispatches the process onto a CPU — the process's saved registers are loaded, and it begins (or resumes) executing instructions.

The critical insight is what pulls a process *out* of the running state. Two things can happen. First, the scheduler may **preempt** the process — its time slice expires, or a higher-priority process becomes ready — and the process returns to the ready state without having done anything wrong. Second, the process may request something that cannot complete immediately, such as reading from disk or waiting for a network packet. At that point the process enters the **blocked** state. A blocked process is not competing for CPU time at all; it is parked until the event it is waiting for occurs. When the I/O completes or the event fires, the OS moves the process back to ready — not directly to running, because the scheduler still decides who runs next.

Finally, when a process calls exit() or is killed by a signal, it enters the **terminated** state. As you learned from process termination and cleanup, the process's resources are released, but its PCB may linger as a zombie until the parent collects its exit status. The entire state machine can be drawn as a directed graph with five nodes and a handful of edges, and every transition corresponds to a concrete OS mechanism: the scheduler dispatches (ready → running), the timer interrupt preempts (running → ready), a blocking system call waits (running → blocked), an interrupt signals completion (blocked → ready), and exit or a fatal signal terminates (running → terminated). Internalizing this diagram is the foundation for understanding CPU scheduling, context switching, and everything the OS does to juggle multiple processes on limited hardware.
