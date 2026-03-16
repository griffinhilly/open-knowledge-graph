---
id: round-robin-scheduling
title: Round-Robin (RR) Scheduling
domain: computer-science
course: operating-systems
prerequisites:
- id: cpu-scheduling-basic-concepts
  type: hard
builds-toward:
- priority-scheduling-algorithms
tags:
- scheduling-algorithms
- preemptive
- time-sharing
stage: formal-systems
status: draft
---

# Round-Robin (RR) Scheduling

## Core Idea
Round-Robin scheduling allocates each process a fixed time quantum, then moves it to the back of the ready queue. It is preemptive, providing better responsiveness and interactivity than FCFS. Performance depends heavily on quantum size: too small causes excessive context switching; too large approaches FCFS behavior.

## How It's Best Learned
Trace through RR scheduling with different time quanta to observe context switches and measure turnaround time and response time changes.

## Explainer

From your study of CPU scheduling basics, you know that the operating system must decide which ready process gets the CPU next. First-Come, First-Served (FCFS) is simple but unfair — a long-running process can monopolize the CPU while short jobs wait. **Round-Robin (RR) scheduling** solves this by giving every process a fair turn: each process runs for a fixed slice of time called a **time quantum** (or time slice), then gets preempted and sent to the back of the ready queue, regardless of whether it has finished.

Imagine a group of students sharing one computer in a lab. Under FCFS, whoever sits down first uses it until they are done — even if they need three hours and someone else needs thirty seconds. Under Round-Robin, a timer goes off every, say, ten minutes, and the current user must get up and go to the back of the line. Everyone gets regular access, and no one waits too long for their first turn. This is why RR is the foundation of **time-sharing systems** — it guarantees responsiveness by ensuring every process gets CPU time at regular intervals.

The critical design choice is the **quantum size**. If the quantum is very small (say, 1 millisecond), every process gets a turn almost immediately — response time is excellent. But each context switch costs time: the OS must save the current process's registers, update its state, load the next process's context, and flush caches. With a tiny quantum, you spend more time switching than computing. If the quantum is very large (say, 10 seconds), context switches are rare, but the system starts behaving like FCFS — a process runs for so long that others wait excessively. The sweet spot is typically 10–100 milliseconds: long enough to amortize the context-switch overhead, short enough that users perceive the system as concurrent.

Consider a concrete example: three processes P1, P2, and P3 arrive at time 0 with burst times of 24, 3, and 3 milliseconds, and the quantum is 4ms. P1 runs for 4ms, then yields. P2 runs for 3ms and finishes (it needed less than a full quantum). P3 runs for 3ms and finishes. P1 gets the CPU back and runs its remaining 20ms in five more quanta. Under FCFS, P2 and P3 would have waited 24ms and 27ms respectively. Under RR, P2 finished at 7ms and P3 at 10ms — dramatically better response times for the short jobs, at the cost of P1 taking slightly longer overall due to context switches.
