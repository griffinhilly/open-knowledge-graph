---
id: process-states-lifecycle
title: Process States and Lifecycle
domain: computer-science
course: operating-systems
prerequisites:
- id: process-concept
  type: hard
builds-toward:
- cpu-scheduling-basics
- threads-and-concurrency
tags:
- process-states
- new
- ready
- running
- waiting
- terminated
- context-switch
stage: formal-systems
status: validated
---

# Process States and Lifecycle

## Core Idea
A process moves through a defined set of states during its lifetime: New (being created), Ready (waiting to be assigned to a CPU), Running (instructions executing), Waiting/Blocked (waiting for an event such as I/O completion), and Terminated (finished execution). The OS maintains separate queues for ready and waiting processes, and a scheduler selects which ready process runs next. Context switching — saving one process's state and loading another's — is the mechanism that allows multitasking on a single CPU core.

## How It's Best Learned
Draw the state transition diagram and trace a concrete scenario: a process does a disk read, moves to Waiting, the I/O completes, it moves to Ready, then gets scheduled to Running.

## Common Misconceptions
- A process in Waiting state is not consuming CPU; it is blocked on an event.
- Context switches have nonzero cost — they involve saving/restoring registers and potentially flushing TLB entries.

## Explainer

You already know that a process is a running instance of a program — the OS creates it, gives it memory, and tracks it. But the OS doesn't just launch a process and forget about it. Every process moves through a series of well-defined **states**, and the transitions between those states are what allow a single CPU to juggle dozens or hundreds of processes at once. Think of it like a doctor's office: patients (processes) arrive, wait in the lobby (Ready queue), get seen by the doctor (Running on the CPU), sometimes get sent to the lab for tests (Waiting on I/O), and eventually leave (Terminated). The doctor can only see one patient at a time, but by cycling through patients efficiently, everyone gets served.

The five canonical states are **New**, **Ready**, **Running**, **Waiting** (also called Blocked), and **Terminated**. When a process is created, it enters the New state. Once the OS finishes setting up its process control block and allocating resources, the process moves to Ready — meaning it is fully prepared to execute but is waiting its turn for the CPU. When the scheduler selects it, it transitions to Running. From Running, three things can happen: the process finishes (moves to Terminated), it needs to wait for something like a disk read (moves to Waiting), or the OS preempts it because another process deserves a turn (moves back to Ready). A process in the Waiting state returns to Ready — not directly to Running — once the event it was waiting for completes.

The mechanism that makes all of this possible is the **context switch**. When the OS decides to switch from process A to process B, it saves A's entire execution context — the program counter, register values, stack pointer, and other state — into A's process control block (PCB). It then loads B's saved context from B's PCB into the CPU and resumes execution. This save-and-restore cycle is pure overhead: no useful work happens during a context switch. The CPU spends time bookkeeping instead of running your code. That's why context switch frequency is a design tradeoff — too few and interactive responsiveness suffers; too many and you waste cycles on switching instead of computing.

Understanding this lifecycle is essential because almost everything else in operating systems builds on it. CPU scheduling is the policy for choosing which Ready process runs next. Synchronization problems arise because multiple processes in the Ready and Running states share resources. Even virtual memory interacts with process states — a page fault during Running moves the process to Waiting until the page is loaded from disk. Once you can trace a process through its state diagram and explain *why* each transition happens, you have the mental model needed for everything that follows.
