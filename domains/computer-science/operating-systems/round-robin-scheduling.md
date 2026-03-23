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
status: validated
---

# Round-Robin (RR) Scheduling

## Core Idea
Round-Robin scheduling allocates each process a fixed time quantum, then moves it to the back of the ready queue. It is preemptive, providing better responsiveness and interactivity than FCFS. Performance depends heavily on quantum size: too small causes excessive context switching; too large approaches FCFS behavior.

## How It's Best Learned
Trace through RR scheduling with different time quanta to observe context switches and measure turnaround time and response time changes.

## Questions

```yaml
- question: "Three processes P1 (24ms burst), P2 (3ms burst), and P3 (3ms burst) arrive simultaneously. With a quantum of 4ms, when does P2 finish?"
  type: multiple-choice
  options:
    - "At 3ms — P2 runs first and completes immediately"
    - "At 7ms — P1 runs 4ms, then P2 runs its 3ms and finishes"
    - "At 10ms — all three processes share the CPU equally before any finishes"
    - "At 4ms — P2 gets a full quantum before being preempted"
  answer: 1
  explanation: "The ready queue order at time 0 is P1, P2, P3. P1 runs for 4ms (its full quantum), then yields. P2 runs for 3ms and finishes — it needed less than a full quantum, so it completes at 4 + 3 = 7ms. Under FCFS, P2 would have waited 24ms before even starting. This illustrates Round-Robin's core advantage: short jobs get CPU time quickly rather than waiting behind long-running processes."

- question: "A system administrator reduces the Round-Robin time quantum from 50ms to 1ms. Which of the following most accurately describes the result?"
  type: multiple-choice
  options:
    - "Throughput and response time both improve because processes get CPU time more frequently"
    - "Response time improves but throughput may decrease because the system spends more time on context switching overhead"
    - "Performance is unchanged because every process still gets the same total CPU time"
    - "The system behaves more like FCFS because context switches become rare"
  answer: 1
  explanation: "With a 1ms quantum, every process gets a turn very quickly — response time (time to first CPU access) drops dramatically. But each context switch incurs overhead: saving and restoring registers, cache flushing, scheduler overhead. With a 1ms quantum, the system might spend half its CPU time on context switching rather than actual computation, reducing throughput. The quantum must be large enough to amortize context-switch cost while small enough to maintain responsiveness — typically 10–100ms in practice."

- question: "Round-Robin scheduling guarantees that every process in the ready queue will eventually receive CPU time, regardless of how long any individual process runs."
  type: true-false
  answer: true
  explanation: "This is Round-Robin's defining guarantee and why it underpins time-sharing systems. Because every process is preempted after at most one quantum and moved to the back of the ready queue, no process can monopolize the CPU indefinitely. Even a process with a 10-second burst will only hold the CPU for one quantum at a time before other processes get their turn. This prevents the starvation that can occur in priority scheduling and the convoy effect in FCFS."

- question: "Reducing the time quantum in Round-Robin always improves overall system performance."
  type: true-false
  answer: false
  explanation: "This is false and is the central design tension in Round-Robin. A smaller quantum improves response time (processes wait less for their first CPU turn) but increases the proportion of CPU time spent on context switching. If the quantum falls below the context-switch overhead, the system spends more time switching than computing — throughput collapses. Performance is not monotonically improved by reducing the quantum; there is a sweet spot that balances responsiveness against overhead."

- question: "Explain why a very large time quantum in Round-Robin degrades into FCFS-like behavior, and why this is problematic for interactive systems."
  type: short-answer
  answer: "When the quantum is very large, most processes complete their entire CPU burst within a single quantum before being preempted. This means processes effectively run to completion without interruption — exactly what FCFS does. Short jobs that arrive after a long-running process must wait the full burst time of the long process before getting any CPU time. Interactive systems require short response times: a user clicking a button expects a near-instant reaction. Under FCFS-like behavior, if a long compilation job is running, the user's UI event might wait seconds for its first CPU slice. Round-Robin's value comes precisely from its preemption of long jobs at regular intervals."
  explanation: "The ideal quantum is large enough that most short jobs complete in one quantum (avoiding unnecessary preemptions) but small enough that the wait between consecutive quanta is imperceptible to users. The classic rule of thumb is that about 80% of CPU bursts should be shorter than the quantum — this ensures that most jobs complete quickly without excessive context switching while the minority of long-running jobs are preempted fairly."
```

## Explainer

From your study of CPU scheduling basics, you know that the operating system must decide which ready process gets the CPU next. First-Come, First-Served (FCFS) is simple but unfair — a long-running process can monopolize the CPU while short jobs wait. **Round-Robin (RR) scheduling** solves this by giving every process a fair turn: each process runs for a fixed slice of time called a **time quantum** (or time slice), then gets preempted and sent to the back of the ready queue, regardless of whether it has finished.

Imagine a group of students sharing one computer in a lab. Under FCFS, whoever sits down first uses it until they are done — even if they need three hours and someone else needs thirty seconds. Under Round-Robin, a timer goes off every, say, ten minutes, and the current user must get up and go to the back of the line. Everyone gets regular access, and no one waits too long for their first turn. This is why RR is the foundation of **time-sharing systems** — it guarantees responsiveness by ensuring every process gets CPU time at regular intervals.

The critical design choice is the **quantum size**. If the quantum is very small (say, 1 millisecond), every process gets a turn almost immediately — response time is excellent. But each context switch costs time: the OS must save the current process's registers, update its state, load the next process's context, and flush caches. With a tiny quantum, you spend more time switching than computing. If the quantum is very large (say, 10 seconds), context switches are rare, but the system starts behaving like FCFS — a process runs for so long that others wait excessively. The sweet spot is typically 10–100 milliseconds: long enough to amortize the context-switch overhead, short enough that users perceive the system as concurrent.

Consider a concrete example: three processes P1, P2, and P3 arrive at time 0 with burst times of 24, 3, and 3 milliseconds, and the quantum is 4ms. P1 runs for 4ms, then yields. P2 runs for 3ms and finishes (it needed less than a full quantum). P3 runs for 3ms and finishes. P1 gets the CPU back and runs its remaining 20ms in five more quanta. Under FCFS, P2 and P3 would have waited 24ms and 27ms respectively. Under RR, P2 finished at 7ms and P3 at 10ms — dramatically better response times for the short jobs, at the cost of P1 taking slightly longer overall due to context switches.
