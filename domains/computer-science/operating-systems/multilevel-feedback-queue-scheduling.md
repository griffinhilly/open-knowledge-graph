---
id: multilevel-feedback-queue-scheduling
title: Multilevel Feedback Queue (MLFQ) Scheduling
domain: computer-science
course: operating-systems
prerequisites:
- id: shortest-job-first-sjf-cpu-scheduling
  type: hard
- id: priority-scheduling-algorithms
  type: soft
builds-toward:
- real-time-scheduling-algorithms
tags:
- scheduling
- algorithms
- cpu
- feedback
stage: formal-systems
status: draft
---

# Multilevel Feedback Queue (MLFQ) Scheduling

## Core Idea
MLFQ uses multiple queues with different priorities and time quanta, allowing processes to move between queues based on behavior. Processes that consume their full time slice move to lower-priority queues, while I/O-bound processes stay in higher-priority queues. This design approximates SJF without requiring prior knowledge of burst times.

## How It's Best Learned
Trace through MLFQ scheduling with varying process behaviors. Experiment with different queue structures and time quantum combinations. Compare against SJF and round-robin to understand trade-offs.

## Common Misconceptions
- Thinking MLFQ requires knowing job length in advance (it adapts dynamically).
- Assuming all processes converge to the lowest queue (depends on behavior).
- Ignoring the risk of starvation in lower-priority queues.

## Questions

```yaml
- question: "A process enters the MLFQ scheduler and consistently uses its full CPU time quantum without voluntarily yielding. What happens to it over successive rounds?"
  type: multiple-choice
  options:
    - "It stays in the highest-priority queue because it clearly needs the most CPU time"
    - "It is terminated for monopolizing the CPU"
    - "It is demoted to a lower-priority queue with a larger time quantum"
    - "It is promoted to higher priority to ensure its long computation completes faster"
  answer: 2
  explanation: "A process that exhausts its full quantum is inferred to be CPU-bound (long-running). MLFQ demotes it to the next lower queue, which has a larger quantum but runs less frequently. This keeps CPU-hungry processes from starving interactive ones. The common misconception is that 'needing more CPU' should earn higher priority — but MLFQ rewards short, interactive bursts, not long ones."

- question: "Why does a text editor waiting for keystrokes typically remain in the high-priority queues of an MLFQ scheduler?"
  type: multiple-choice
  options:
    - "The scheduler detects that the process is user-facing and assigns it a static high-priority flag"
    - "I/O-bound processes receive special protection that prevents demotion"
    - "The process frequently yields the CPU before exhausting its time quantum, so the scheduler never demotes it"
    - "Text editors are given high priority by convention in most operating systems"
  answer: 2
  explanation: "MLFQ does not know the process is a text editor — it only observes behavior. Because the text editor spends most of its time waiting for keystrokes (an I/O event), it issues frequent I/O requests and voluntarily releases the CPU well before its quantum expires. The scheduler infers this is a short/interactive process and keeps it at high priority. No special flags or conventions are needed; the behavioral signal is the quantum usage pattern."

- question: "MLFQ scheduling requires the operating system to know each process's expected run time before scheduling it."
  type: true-false
  answer: false
  explanation: "This is precisely the problem MLFQ solves. SJF requires knowing burst times in advance, which is impractical. MLFQ observes behavior dynamically: processes that exhaust their quantum are inferred to be long-running and demoted; those that yield early are inferred to be short and kept at high priority. No advance knowledge is required."

- question: "Without a periodic priority boost mechanism, MLFQ scheduling can cause starvation for long-running CPU-bound processes."
  type: true-false
  answer: true
  explanation: "If interactive (high-priority) processes continuously arrive, they will always preempt lower-priority queues, leaving CPU-bound processes in the bottom queues to wait indefinitely. This is the starvation problem. The standard fix is a periodic priority boost: every fixed interval, all processes are moved back to the highest-priority queue, giving long-running processes a fresh chance to run."

- question: "How does MLFQ approximate the behavior of Shortest Job First scheduling without knowing job lengths in advance?"
  type: short-answer
  answer: "MLFQ uses observed CPU usage as a proxy for job length. New processes enter the highest-priority queue. If a process exhausts its quantum without yielding, the scheduler infers it is long/CPU-bound and demotes it. If it yields early (completing an I/O burst), it remains at high priority — inferred to be short/interactive. Short jobs naturally finish before demotion; long jobs sink to lower queues. The result is preferential treatment for short, bursty processes, mimicking SJF's behavior without requiring predictions."
  explanation: "This 'learn by observing' approach is more robust than SJF in practice because it adapts to actual behavior. A process that starts CPU-bound but later becomes interactive (e.g., a compiler that finishes compiling and starts waiting for user input) will be promoted back through the priority boost mechanism."
```

## Explainer

From your study of Shortest Job First scheduling, you know that SJF produces optimal average waiting times — but it has a fatal practical flaw: it requires knowing how long each job will run *before* it runs. In real operating systems, the kernel has no idea whether the process that just became ready will use the CPU for 2 milliseconds or 2 seconds. **Multilevel Feedback Queue (MLFQ)** scheduling solves this by *observing* process behavior and adjusting priority dynamically, effectively learning which processes are short and interactive versus long and CPU-bound.

The structure is a set of queues arranged by priority level. A new process enters the **highest-priority queue** with a small time quantum (say 8ms). If it finishes its CPU burst before the quantum expires — perhaps because it issued an I/O request — it stays at the same high priority. The system infers that this process is interactive or I/O-bound, and interactive processes need fast response times. But if the process uses its entire quantum without voluntarily yielding, the scheduler demotes it to the **next lower queue**, which has a larger time quantum (say 16ms). If it burns through that quantum too, it drops again. Eventually, long-running CPU-bound processes sink to the lowest-priority queue with the largest time quantum, where they run less frequently but get larger chunks of CPU time when they do run.

This design elegantly approximates SJF without requiring advance knowledge. Short jobs finish quickly in the high-priority queue and never get demoted. Long jobs gradually sink to lower queues where they don't interfere with interactive responsiveness. I/O-bound processes (like a text editor waiting for keystrokes) naturally stay at high priority because they frequently yield the CPU before their quantum expires. The scheduler gives preferential treatment to exactly the processes that need it: those with short, bursty CPU usage patterns that would suffer most from delayed scheduling.

The main pitfall is **starvation**: if enough high-priority processes keep arriving, the low-priority queues never get to run. The standard solution is a **priority boost** — periodically (say every second), the scheduler moves all processes back to the highest-priority queue. This gives long-running processes a fresh chance to run and also handles processes whose behavior changes over time (a computation phase might end and the process might become interactive). Another concern is **gaming**: a clever process could issue a trivial I/O request just before its quantum expires, tricking the scheduler into keeping it at high priority while monopolizing the CPU. Modern MLFQ implementations track total CPU time per priority level rather than just per-quantum behavior to prevent this. Nearly every general-purpose OS uses some variant of MLFQ — Linux's CFS and Windows' priority scheduling both incorporate feedback-based priority adjustment, because the principle of "observe and adapt" is fundamentally more robust than requiring predictions about future behavior.
