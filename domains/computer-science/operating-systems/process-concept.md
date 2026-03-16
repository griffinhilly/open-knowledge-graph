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
builds-toward:
- process-states-lifecycle
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

## Explainer

From your study of instruction set architecture, you know that a CPU executes a sequence of instructions, maintaining state in registers like the program counter (which instruction to execute next) and the stack pointer. A **process** is what happens when the operating system takes a passive program — a file sitting on disk — and brings it to life as an active, running entity with its own registers, memory, and system resources.

A process is more than just code. It encompasses the **text segment** (the compiled machine instructions), the **data segment** (global and static variables), the **heap** (dynamically allocated memory that grows upward), and the **stack** (function call frames, local variables, and return addresses that grows downward). Each process also maintains CPU state: the current values of all registers, the program counter pointing to the next instruction, and the processor status word. Together, these components define the complete execution context — everything needed to pause a process and resume it later exactly where it left off.

The operating system tracks all of this in a data structure called the **Process Control Block** (PCB). Every process has one. The PCB stores the process ID (PID), current process state (running, ready, waiting), saved register values, memory management information (page tables, segment limits), I/O status (open file descriptors, pending I/O operations), and scheduling data (priority, CPU time consumed). When the OS switches the CPU from one process to another — a **context switch** — it saves the running process's register values into its PCB, then loads the next process's saved registers from its PCB. The CPU seamlessly resumes the new process as if it had never stopped. This save-and-restore cycle is what enables multitasking: dozens of processes take turns on the CPU, each unaware of the others.

The critical insight is that processes are **isolated by default**. Two processes running the same program binary have completely separate address spaces — process A's variable `x` at virtual address 0x1000 and process B's variable `x` at virtual address 0x1000 refer to different physical memory locations. Neither can read or corrupt the other's data. This isolation is enforced by the hardware memory management unit, which the OS configures separately for each process. When processes do need to communicate, they must use explicit **inter-process communication** (IPC) mechanisms — pipes, shared memory segments, message queues, or sockets — that the OS mediates and controls.
