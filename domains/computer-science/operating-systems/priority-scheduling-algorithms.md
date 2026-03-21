---
id: priority-scheduling-algorithms
title: Priority Scheduling Algorithms
domain: computer-science
course: operating-systems
prerequisites:
- id: cpu-scheduling-basic-concepts
  type: hard
tags:
- scheduling-algorithms
- priority-based
- starvation-risk
stage: formal-systems
status: draft
---

# Priority Scheduling Algorithms

## Core Idea
Priority scheduling associates a priority with each process and runs the highest-priority process. Preemptive variants interrupt lower-priority processes when higher-priority ones arrive. However, priority scheduling can starve low-priority processes and requires careful priority assignment and aging techniques to prevent pathological behavior.

## Common Misconceptions
Higher priority always means faster execution (depends on competing processes and workload). Static priorities are always better (dynamic/adaptive priorities often prevent starvation).

## Questions

```yaml
- question: "A system uses preemptive priority scheduling. Process P1 (priority 5) is running when Process P2 (priority 8) enters the ready queue. What happens immediately?"
  type: multiple-choice
  options:
    - "P1 continues until it completes its CPU burst, then P2 runs"
    - "P1 is immediately preempted and P2 is given the CPU"
    - "P2 is added to the ready queue and P1 continues until it voluntarily blocks"
    - "The scheduler waits for the next clock tick before deciding whether to switch"
  answer: 1
  explanation: "In preemptive priority scheduling, a higher-priority process immediately interrupts whatever is currently running. P2 (priority 8) outranks P1 (priority 5), so P1 is preempted and P2 runs now. This is the defining characteristic of preemptive scheduling: the scheduler does not wait for the current process to yield or finish. Non-preemptive priority scheduling (option A) would let P1 complete its burst before switching, but the question specifies preemptive. Time-quantum waits (option D) describe round-robin scheduling."

- question: "A batch job has been waiting in the ready queue for two hours in a priority-scheduled system, repeatedly deferred by arriving interactive tasks. What is the standard mechanism to address this?"
  type: multiple-choice
  options:
    - "Assign the batch job maximum static priority at design time"
    - "Aging — the OS gradually increases the priority of processes that have waited a long time"
    - "Switch the entire system to FCFS to guarantee eventual execution"
    - "Reduce all interactive task priorities by half every 30 minutes"
  answer: 1
  explanation: "Aging is the standard solution to starvation in priority scheduling. The OS periodically increments the priority of waiting processes, so that even a low-priority process eventually reaches a high enough priority to run before newly arriving high-priority ones. This converts worst-case waiting time from potentially unbounded to bounded. Static priority changes require human intervention and don't automate protection. Switching to FCFS eliminates priority entirely, which often defeats the point. Ad-hoc priority reduction (option D) is non-standard and could destabilize the system."

- question: "In a priority scheduling system without aging, a low-priority process can remain in the ready queue indefinitely without ever receiving CPU time."
  type: true-false
  answer: true
  explanation: "This is starvation, and it is a genuine risk in priority scheduling. If the ready queue always contains at least one higher-priority process, the lower-priority process is perpetually deferred. In a system with continuous interactive workload (high priority) and a few background batch jobs (low priority), the batch jobs could wait hours or theoretically forever. This is not a theoretical edge case — it was observed in real systems before aging was introduced. Aging is the mechanism that converts 'potentially infinite wait' into 'bounded wait.'"

- question: "Static priorities (assigned once at process creation and never changed) are generally preferred over dynamic priorities in modern operating systems because they are more predictable."
  type: true-false
  answer: false
  explanation: "Modern operating systems almost universally use dynamic priorities because they better balance responsiveness and throughput. A process that behaves as I/O-bound (frequently blocking, using short CPU bursts) gets a priority boost — it's unlikely to monopolize the CPU, and boosting it keeps I/O devices busy. A CPU-bound process gets its priority reduced to prevent monopolization. Linux's Completely Fair Scheduler and Windows' multilevel feedback queue both use dynamic priority adjustment. Static priorities are simpler but require careful manual tuning and cannot adapt to changing process behavior."

- question: "Explain why aging is necessary in priority scheduling and how it prevents indefinite starvation."
  type: short-answer
  answer: "Without aging, a low-priority process can wait indefinitely if higher-priority processes continuously arrive — this is starvation. Aging prevents it by having the OS periodically increment the priority of every waiting process. After waiting long enough, even the lowest-priority process reaches a priority high enough to be selected before newly arriving higher-priority ones. This bounds the worst-case waiting time: instead of potentially infinite wait, every process is guaranteed to run within a time proportional to the priority differential divided by the aging rate."
  explanation: "The aging rate requires tuning: too slow and starvation is only marginally reduced; too fast and the priority ordering is disrupted in normal operation. In practice, aging ensures fairness as a background guarantee while preserving priority semantics during normal operation — high-priority processes still run first most of the time. The same principle motivates aging in multilevel feedback queues: processes that have been waiting a long time get promoted to higher-priority queues."
```

## Explainer

From CPU scheduling basics, you understand that the scheduler chooses which ready process runs next and that different algorithms optimize for different goals. Priority scheduling assigns each process a numerical **priority value** and always runs the highest-priority ready process. Unlike FCFS, which uses arrival order, or Shortest Job First, which uses burst time, priority scheduling uses an externally assigned importance ranking — the OS or the user decides which processes matter most. This makes it the natural choice for systems where some tasks are genuinely more urgent than others: a real-time audio driver should preempt a background file indexer, not wait behind it.

Priority scheduling comes in two flavors. In the **non-preemptive** variant, once a process starts running, it keeps the CPU until it finishes or blocks, even if a higher-priority process arrives in the meantime. In the **preemptive** variant, a newly arrived or newly unblocked process with higher priority immediately interrupts the currently running process. Preemptive priority scheduling is more responsive — a high-priority task gets the CPU as soon as it needs it — but requires more context switches. Most real operating systems use preemptive priority scheduling because responsiveness matters: when you move your mouse, the interrupt handler and input processing should preempt your background compilation, not wait for it to finish.

The critical problem with priority scheduling is **starvation**: a low-priority process may never run if higher-priority processes keep arriving. Imagine a system where interactive tasks (high priority) constantly arrive — a batch job sitting at low priority could wait hours or even indefinitely. The standard solution is **aging**: the OS gradually increases the priority of processes that have been waiting a long time. After enough time in the ready queue, even the lowest-priority process eventually reaches a priority high enough to run. Aging ensures that priority scheduling has a bounded worst-case waiting time rather than an unbounded one.

In practice, priorities can be **static** (assigned once, fixed for the process lifetime) or **dynamic** (adjusted by the OS based on behavior). Many systems use dynamic priorities to balance responsiveness and throughput: a process that has been I/O-bound (frequently blocking on I/O) gets a priority boost because it is likely to use only a small burst of CPU time before blocking again, keeping I/O devices busy. A process that has been CPU-bound gets its priority reduced to prevent it from monopolizing the CPU. Linux's Completely Fair Scheduler (CFS) and Windows' multilevel feedback queue both incorporate priority with dynamic adjustment. Understanding pure priority scheduling gives you the building block for these more sophisticated multilevel schemes, where processes move between priority bands based on their observed behavior.
