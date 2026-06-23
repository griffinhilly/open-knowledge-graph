---
id: process-concept
title: Processes and the Process Control Block
domain: computer-science
course: operating-systems
prerequisites:
- id: instruction-set-architecture
  type: hard
- id: system-calls
  type: soft
- id: assembly-language-basics
  type: soft
- id: operating-systems-introduction
  type: soft
builds-toward:
- process-states-and-transitions
- threads-and-concurrency
- inter-process-communication
- os-security-basics
tags:
- process
- PCB
- program-counter
- address-space
stage: formal-systems
status: validated
---

# Processes and the Process Control Block

## Core Idea
A process is a program in execution — an active entity that includes the program code, current activity (program counter, registers), stack, heap, and data segment. The operating system represents each process with a Process Control Block (PCB), a data structure storing process state, PID, register values, memory maps, open file descriptors, and scheduling information. Multiple processes may run the same program but maintain separate address spaces, so they do not interfere with each other's data. The PCB is saved and restored during context switches.

## How It's Best Learned
Inspect /proc/<pid>/ on Linux to see the live PCB-equivalent data. Write a fork() program and observe how parent and child diverge despite sharing the same code.

## Common Misconceptions
- A process is not the same as a program; the same program can have many simultaneous processes.
- Processes are isolated by default; sharing memory requires explicit IPC mechanisms.

## Questions

```yaml
- question: "Two users on the same Linux system both launch the same Python interpreter. User A's program sets a global variable `counter = 100`. Will User B's Python process see `counter = 100`?"
  type: multiple-choice
  options:
    - "Yes — they share the same program binary, so they share global variables"
    - "Yes — global variables in Python are shared across all instances of the interpreter"
    - "No — each process has its own isolated address space; changes in one process's memory are invisible to the other"
    - "It depends on whether both processes are running at exactly the same time"
  answer: 2
  explanation: "Two processes running the same program binary maintain completely separate address spaces. User A's `counter` and User B's `counter` may share the same virtual address, but they map to different physical memory locations managed by separate page tables. Process isolation is the default — not sharing — enforced by the hardware MMU. If processes need to share data, they must use explicit IPC mechanisms (shared memory segments, pipes, sockets, etc.)."

- question: "During a context switch from Process A to Process B, what must the operating system do?"
  type: multiple-choice
  options:
    - "Save only Process A's program counter to its PCB, since it is the only register that changes between processes"
    - "Write Process A's entire address space to disk before loading Process B"
    - "Save all of Process A's register values to its PCB, then load all of Process B's saved register values from its PCB"
    - "Restart Process B from the beginning of its program to ensure a clean execution environment"
  answer: 2
  explanation: "A context switch saves the complete CPU state of the departing process — all register values including the program counter, stack pointer, and general-purpose registers — into its PCB. Then it loads the incoming process's saved register values from its PCB. This save-restore cycle is what enables multitasking: Process B resumes exactly where it left off, as if it had never stopped. The illusion of simultaneous execution is created by switching between processes fast enough that users don't notice."

- question: "Two instances of the same program running simultaneously share the same address space, allowing each to access the other's variables."
  type: true-false
  answer: false
  explanation: "Each process has its own completely isolated address space, even when running the same program binary. The code (text segment) may come from the same file on disk, but each process's stack, heap, and data segment occupy separate physical memory locations managed by separate page tables. One process cannot read or modify another's data without explicit OS-mediated IPC. This isolation is a fundamental OS guarantee enforced by the hardware memory management unit."

- question: "The Process Control Block (PCB) contains all the information the OS needs to pause and correctly resume a process."
  type: true-false
  answer: true
  explanation: "The PCB stores the process's complete execution context: saved register values (including the program counter), process state, memory management information (page tables), open file descriptors, scheduling data, and I/O status. During a context switch, the OS saves the running process's CPU state into its PCB and loads the next process's saved state from its PCB. With this snapshot, the OS can resume the process exactly where it left off — this is the mechanism behind multitasking."

- question: "Explain the difference between a program and a process, and why two processes running the same program cannot interfere with each other's data."
  type: short-answer
  answer: "A program is a passive file on disk — compiled code waiting to be executed. A process is a program in execution: an active entity with its own CPU state (registers, program counter), memory segments (text, data, heap, stack), and OS resources. The OS gives each process its own isolated virtual address space, and the hardware MMU enforces that the same virtual address in two different processes maps to different physical memory. Neither process can read or write the other's memory without explicit OS-mediated IPC mechanisms."
  explanation: "This distinction changes how you reason about bugs and security. A memory corruption bug in one process cannot propagate to another. A crash in Process A cannot take down Process B. Two users running the same program cannot observe each other's data. Process isolation is one of the core abstractions the OS provides, and the PCB is the data structure that makes save-and-restore possible."
```

## Explainer

From your study of instruction set architecture, you know that a CPU executes a sequence of instructions, maintaining state in registers like the program counter (which instruction to execute next) and the stack pointer. A **process** is what happens when the operating system takes a passive program — a file sitting on disk — and brings it to life as an active, running entity with its own registers, memory, and system resources.

A process is more than just code. It encompasses the **text segment** (the compiled machine instructions), the **data segment** (global and static variables), the **heap** (dynamically allocated memory that grows upward), and the **stack** (function call frames, local variables, and return addresses that grows downward). Each process also maintains CPU state: the current values of all registers, the program counter pointing to the next instruction, and the processor status word. Together, these components define the complete execution context — everything needed to pause a process and resume it later exactly where it left off.

The operating system tracks all of this in a data structure called the **Process Control Block** (PCB). Every process has one. The PCB stores the process ID (PID), current process state (running, ready, waiting), saved register values, memory management information (page tables, segment limits), I/O status (open file descriptors, pending I/O operations), and scheduling data (priority, CPU time consumed). When the OS switches the CPU from one process to another — a **context switch** — it saves the running process's register values into its PCB, then loads the next process's saved registers from its PCB. The CPU seamlessly resumes the new process as if it had never stopped. This save-and-restore cycle is what enables multitasking: dozens of processes take turns on the CPU, each unaware of the others.

The critical insight is that processes are **isolated by default**. Two processes running the same program binary have completely separate address spaces — process A's variable `x` at virtual address 0x1000 and process B's variable `x` at virtual address 0x1000 refer to different physical memory locations. Neither can read or corrupt the other's data. This isolation is enforced by the hardware memory management unit, which the OS configures separately for each process. When processes do need to communicate, they must use explicit **inter-process communication** (IPC) mechanisms — pipes, shared memory segments, message queues, or sockets — that the OS mediates and controls.
