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

## Questions

```yaml
- question: "A process is in the Running state and initiates a disk read. While waiting for the disk to respond, what happens to the process, and what state does it enter when the I/O completes?"
  type: multiple-choice
  options:
    - "Moves to Waiting; returns directly to Running when I/O completes"
    - "Moves to Waiting; moves to Ready when I/O completes, then waits for the scheduler"
    - "Stays in Running on a separate CPU core while the I/O is in progress"
    - "Moves to Ready immediately; the disk read happens in the background without blocking"
  answer: 1
  explanation: "When a process waits for I/O, it moves to the Waiting (Blocked) state — it is not consuming CPU. When the I/O completes, it moves to the Ready state, not directly back to Running. This is the most common misconception. The process must then wait for the scheduler to select it. Only the scheduler decides which Ready process transitions to Running; completing an event does not immediately grant CPU access."

- question: "Why is context switching considered 'pure overhead' in operating systems?"
  type: multiple-choice
  options:
    - "Context switches require the OS to terminate and restart processes from scratch"
    - "Context switches flush the disk cache, requiring slow I/O operations"
    - "During a context switch, the CPU saves and restores process state instead of executing user code"
    - "Context switches allocate new memory for each process, which is expensive"
  answer: 2
  explanation: "A context switch involves saving the current process's execution context (program counter, registers, stack pointer) into its PCB and loading the next process's context from its PCB. During this entire save-and-restore cycle, the CPU is performing bookkeeping rather than running any process's instructions — no useful computation happens. This is why context switch frequency is a design tradeoff: too frequent and you waste cycles on overhead; too infrequent and interactive responsiveness suffers."

- question: "A process in the Waiting state is consuming CPU cycles while it waits for its I/O request to complete."
  type: true-false
  answer: false
  explanation: "This is one of the core misconceptions identified in this topic. A process in the Waiting state is explicitly *not* on the CPU — it has been removed from the CPU precisely because it cannot make progress until some external event (I/O completion, a signal, a timer) occurs. This is the whole point of the Waiting state: it lets the CPU be used by other Ready processes instead of spinning uselessly. A Waiting process occupies no CPU time until the event it is blocked on completes and it transitions to Ready."

- question: "After a page fault occurs during execution, the OS moves the faulting process from the Running state to the Waiting state while the required page is loaded from disk."
  type: true-false
  answer: true
  explanation: "A page fault is an event that the running process must wait for — the OS needs to load the required memory page from disk before the process can continue. Since disk I/O is an external event the process cannot proceed without, it follows the same transition as any I/O wait: Running → Waiting. Once the page is loaded, the process moves to Ready and eventually back to Running. This is a concrete example of how virtual memory management interacts with the process state model."

- question: "Explain why a process that finishes waiting for I/O goes to the Ready state rather than directly back to Running."
  type: short-answer
  answer: "Because only one process can run on a CPU core at a time, and when the I/O-waiting process was moved to Waiting, the CPU was assigned to another process. The CPU may still be busy with that process (or another) when the I/O completes. The Ready state represents 'fully prepared to execute but waiting for CPU access' — the process has satisfied its dependency (the I/O is done) but must wait for the scheduler to select it. Jumping directly to Running would require preempting whatever is currently running, which may not be appropriate."
  explanation: "The Ready state is the OS's queue of processes that could run but haven't been assigned a CPU. The scheduler enforces policy about which process gets the CPU next — it might use priority, round-robin, or other algorithms. Allowing I/O completion to automatically preempt the currently running process would bypass scheduling policy and could starve other processes or violate fairness guarantees. The indirection through Ready lets the scheduler maintain control over CPU allocation."
```

## Explainer

You already know that a process is a running instance of a program — the OS creates it, gives it memory, and tracks it. But the OS doesn't just launch a process and forget about it. Every process moves through a series of well-defined **states**, and the transitions between those states are what allow a single CPU to juggle dozens or hundreds of processes at once. Think of it like a doctor's office: patients (processes) arrive, wait in the lobby (Ready queue), get seen by the doctor (Running on the CPU), sometimes get sent to the lab for tests (Waiting on I/O), and eventually leave (Terminated). The doctor can only see one patient at a time, but by cycling through patients efficiently, everyone gets served.

The five canonical states are **New**, **Ready**, **Running**, **Waiting** (also called Blocked), and **Terminated**. When a process is created, it enters the New state. Once the OS finishes setting up its process control block and allocating resources, the process moves to Ready — meaning it is fully prepared to execute but is waiting its turn for the CPU. When the scheduler selects it, it transitions to Running. From Running, three things can happen: the process finishes (moves to Terminated), it needs to wait for something like a disk read (moves to Waiting), or the OS preempts it because another process deserves a turn (moves back to Ready). A process in the Waiting state returns to Ready — not directly to Running — once the event it was waiting for completes.

The mechanism that makes all of this possible is the **context switch**. When the OS decides to switch from process A to process B, it saves A's entire execution context — the program counter, register values, stack pointer, and other state — into A's process control block (PCB). It then loads B's saved context from B's PCB into the CPU and resumes execution. This save-and-restore cycle is pure overhead: no useful work happens during a context switch. The CPU spends time bookkeeping instead of running your code. That's why context switch frequency is a design tradeoff — too few and interactive responsiveness suffers; too many and you waste cycles on switching instead of computing.

Understanding this lifecycle is essential because almost everything else in operating systems builds on it. CPU scheduling is the policy for choosing which Ready process runs next. Synchronization problems arise because multiple processes in the Ready and Running states share resources. Even virtual memory interacts with process states — a page fault during Running moves the process to Waiting until the page is loaded from disk. Once you can trace a process through its state diagram and explain *why* each transition happens, you have the mental model needed for everything that follows.
