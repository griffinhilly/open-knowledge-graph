---
id: scheduling-algorithms
title: CPU Scheduling Algorithms
domain: computer-science
course: operating-systems
prerequisites:
- id: cpu-scheduling-basics
  type: hard
- id: threads-and-concurrency
  type: soft
- id: disk-scheduling
  type: soft
tags:
- FCFS
- SJF
- round-robin
- priority-scheduling
- multilevel-queue
stage: formal-systems
status: validated
---
# CPU Scheduling Algorithms

## Core Idea
Classic scheduling algorithms each optimize different objectives: First-Come First-Served (FCFS) is simple but causes the convoy effect; Shortest Job First (SJF) minimizes average waiting time but requires knowing future burst lengths; Round Robin (RR) gives each process a fixed time quantum and is fair for interactive systems; Priority Scheduling assigns numeric priorities but risks starvation of low-priority processes, mitigated by aging. Multilevel Feedback Queues combine multiple algorithms into a hierarchy, promoting or demoting processes based on their observed behavior, and represent the approach used by most real operating systems.

## How It's Best Learned
Calculate average waiting time and turnaround time for the same workload under each algorithm. Then argue: for which workload would Round Robin beat SJF?

## Common Misconceptions
- SJF is theoretically optimal for minimizing average waiting time, but it is not practical because burst times must be predicted.
- A small Round Robin quantum isn't always better; too small causes excessive context switching overhead.

## Questions

```yaml
- question: "Three processes arrive simultaneously: P1 (burst 30ms), P2 (burst 2ms), P3 (burst 4ms). Under FCFS in arrival order P1, P2, P3, what is P2's waiting time?"
  type: multiple-choice
  options:
    - "0ms — P2 runs immediately after P1 without waiting"
    - "30ms — P2 waits for P1 to complete"
    - "2ms — P2 waits for its own burst time"
    - "34ms — P2 waits for both P1 and P3 to complete"
  answer: 1
  explanation: "FCFS runs processes in arrival order to completion. P1 runs first for 30ms; P2 waits the entire time. This is the convoy effect: a long CPU-bound process (P1) blocks all the short processes behind it. Under SJF, P2 would run first (burst 2ms), P3 second (4ms), P1 last — P2's waiting time would be 0ms and the average waiting time drops dramatically. The convoy effect is FCFS's critical flaw."

- question: "In a Multilevel Feedback Queue, a process that consistently uses its entire time quantum at the highest priority level will be:"
  type: multiple-choice
  options:
    - "Promoted to an even higher priority level as a reward for intensive CPU use"
    - "Demoted to a lower priority queue, because full quantum usage signals CPU-bound behavior"
    - "Kept at the same level with a longer quantum to reduce context-switching overhead"
    - "Terminated, since MLFQ assumes interactive processes should dominate"
  answer: 1
  explanation: "MLFQ interprets full quantum usage as evidence of CPU-bound behavior — the process is doing heavy computation and doesn't frequently yield for I/O. CPU-bound processes get lower priority because interactive responsiveness matters more for user-facing tasks. The process is demoted to a lower queue with a larger quantum. Conversely, a process that blocks early (suggesting interactive I/O-bound behavior) stays at high priority. MLFQ learns process behavior through observation rather than requiring advance knowledge of burst times."

- question: "Shortest Job First is the best scheduling algorithm for real operating systems because it provably minimizes average waiting time."
  type: true-false
  answer: false
  explanation: "SJF minimizes average waiting time theoretically, but it is impractical for real operating systems because burst times are unknown in advance. You cannot implement pure SJF without knowing how long each process will run — and processes don't declare their burst times. Real implementations use exponential averaging of past bursts to estimate future ones, making it an approximation. MLFQ is used by most real operating systems instead, because it adapts to observed behavior without any prediction. SJF is best understood as a theoretical benchmark, not a deployable algorithm."

- question: "Making the Round Robin time quantum very small (e.g., 1ms) always improves responsiveness because every process gets the CPU more frequently."
  type: true-false
  answer: false
  explanation: "A very small quantum does increase how frequently each process gets CPU turns, but it also dramatically increases context-switching overhead. Each context switch requires saving and restoring register state, flushing CPU caches, and updating OS data structures — all of which consume CPU time. If the quantum is smaller than context-switch overhead, the system spends more time switching than executing actual process code. The guideline is that the quantum should be large enough that roughly 80% of CPU bursts complete within a single quantum, balancing responsiveness against overhead."

- question: "Explain why MLFQ does not need to know CPU burst times in advance, and how it nonetheless approximates the goal that SJF is trying to achieve."
  type: short-answer
  answer: "MLFQ infers burst behavior by observing how processes use their time quanta. A process that uses its full quantum is inferred to be CPU-bound (long bursts) and is demoted to a lower-priority queue with a larger quantum. A process that blocks before using its quantum is inferred to be I/O-bound or interactive (short bursts) and stays at high priority. This approximates SJF's goal — running short jobs first — without any advance knowledge. Interactive processes naturally self-select into high-priority queues by blocking frequently, while batch processes settle into lower queues, achieving similar scheduling order to what SJF would produce."
  explanation: "SJF requires omniscience about future burst times. MLFQ substitutes learning: past behavior predicts future behavior well enough for scheduling purposes. The key insight is that CPU-bound vs. I/O-bound behavior is observable at runtime, making SJF's impractical requirement achievable through adaptive classification."
```

## Explainer

From CPU scheduling basics, you know that the scheduler decides which ready process gets the CPU next, and that metrics like waiting time, turnaround time, and response time measure how well it does its job. Scheduling algorithms are the specific strategies for making that decision, and each one represents a different tradeoff between fairness, efficiency, and practicality. No single algorithm is best for all workloads — understanding why requires walking through each one.

**First-Come, First-Served (FCFS)** is the simplest: processes run in arrival order, and each runs to completion (or until it blocks). It's easy to implement — just a FIFO queue — but it suffers from the **convoy effect**. If a long CPU-bound process arrives first, every short process behind it waits. Imagine a grocery store with one cashier and no express lane: one customer with 200 items holds up everyone behind them. Average waiting time can be terrible. **Shortest Job First (SJF)** fixes this by always running the process with the shortest expected CPU burst next. It provably minimizes average waiting time — it's the mathematical optimum. The catch is that you need to know burst lengths in advance, which you don't. Real implementations estimate them using exponential averaging of past bursts, making SJF more of an ideal benchmark than a practical algorithm.

**Round Robin (RR)** takes a fundamentally different approach: every process gets a fixed **time quantum** (say, 10–100 milliseconds), and if it doesn't finish in that window, it's preempted and sent to the back of the ready queue. This guarantees that no process waits more than (n−1) × quantum time before getting a turn, making it excellent for interactive systems where responsiveness matters. The tradeoff is the quantum size. Too large, and RR degenerates into FCFS. Too small, and you spend more time context-switching than computing. A good rule of thumb is that the quantum should be large enough that 80% of CPU bursts complete within a single quantum.

**Priority Scheduling** assigns each process a numeric priority, and the highest-priority process runs first. This is powerful but introduces the risk of **starvation** — low-priority processes may never run if high-priority processes keep arriving. The solution is **aging**: gradually increasing the priority of waiting processes so that even the lowest-priority process eventually runs. Most real operating systems use **Multilevel Feedback Queues (MLFQ)**, which combine several of these ideas. MLFQ maintains multiple queues at different priority levels, each with its own scheduling policy (often RR with different quantum sizes). New processes start in the highest-priority queue. If a process uses its full quantum (suggesting it's CPU-bound), it gets demoted to a lower queue. If it blocks quickly for I/O (suggesting it's interactive), it stays at high priority. This adaptive behavior means the system automatically learns the nature of each process and schedules accordingly — no advance knowledge of burst times required.
