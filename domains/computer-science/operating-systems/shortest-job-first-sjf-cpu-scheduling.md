---
id: shortest-job-first-sjf-cpu-scheduling
title: Shortest Job First (SJF) CPU Scheduling
domain: computer-science
course: operating-systems
prerequisites:
- id: cpu-scheduling-basics
  type: hard
builds-toward:
- multilevel-feedback-queue-scheduling
- scheduling-fairness-and-starvation
tags:
- scheduling
- algorithms
- cpu
stage: formal-systems
status: draft
---

# Shortest Job First (SJF) CPU Scheduling

## Core Idea
SJF scheduling selects the process with the shortest expected burst time to minimize average waiting time. This algorithm is provably optimal for non-preemptive scheduling but requires accurate knowledge of future burst times, which is impractical in real systems. Preemptive SJF (Shortest Remaining Time First) can outperform non-preemptive SJF but adds complexity.

## How It's Best Learned
Study the algorithm with concrete examples showing scheduling timelines. Compare average waiting times against FCFS and round-robin. Implement a simple SJF simulator to see how different burst time predictions affect scheduling.

## Common Misconceptions
- Assuming SJF is always optimal in practice (it requires future knowledge).
- Confusing preemptive and non-preemptive SJF behavior.
- Believing SJF is fair to all processes (short jobs get priority).

## Questions

```yaml
- question: "Three processes arrive simultaneously with CPU burst times of 8ms, 2ms, and 5ms. What is the average waiting time under SJF (non-preemptive)?"
  type: multiple-choice
  options:
    - "5ms — the same as the FCFS average"
    - "3ms — SJF runs them in order 2ms, 5ms, 8ms: waiting times are 0, 2, and 7"
    - "7ms — the longest job dominates the wait"
    - "0ms — all jobs start immediately under SJF"
  answer: 1
  explanation: "SJF reorders by burst time: run 2ms first, then 5ms, then 8ms. Waiting times: job with 2ms burst waits 0ms; 5ms burst waits 2ms; 8ms burst waits 2+5=7ms. Average = (0+2+7)/3 = 3ms. Under FCFS in the original order (8, 2, 5), waiting times are 0, 8, 10 — average 6ms. SJF wins because short jobs finish quickly, stopping them from contributing to the wait of everyone behind them."

- question: "Why can't a real operating system implement ideal SJF scheduling?"
  type: multiple-choice
  options:
    - "SJF requires more memory than other scheduling algorithms"
    - "SJF requires knowing each process's next CPU burst time in advance, which the OS cannot determine before the process runs"
    - "SJF is only applicable in batch systems with no interactive users"
    - "SJF violates POSIX scheduling standards used by modern operating systems"
  answer: 1
  explanation: "SJF's fundamental impracticality is that it requires knowing how long each process will use the CPU before it has used it. The OS cannot predict the future. Real systems approximate SJF by estimating burst times from historical data — typically using exponential averaging where recent bursts count more than older ones. These estimates enable approximate SJF behavior but introduce errors whenever a process's behavior changes. The algorithm is theoretically optimal but practically only realizable through approximation."

- question: "Among all non-preemptive scheduling algorithms, SJF minimizes average waiting time."
  type: true-false
  answer: true
  explanation: "This is a provable optimality result. The argument is by exchange: given any schedule that does not run the shortest available job next, swapping the shortest job earlier always reduces (or maintains) total waiting time across all processes. Repeating this argument produces the SJF order, which is therefore optimal. This is the same reasoning behind greedy sorting: always process the cheapest operation first to minimize accumulated overhead."

- question: "Preemptive SJF (Shortest Remaining Time First) is always preferable to non-preemptive SJF because it produces lower average waiting times."
  type: true-false
  answer: false
  explanation: "While SRTF achieves lower or equal average waiting time, 'always preferable' is too strong. SRTF introduces additional context-switch overhead every time a shorter job arrives. More critically, SRTF severely worsens starvation: a long process can be perpetually preempted as short jobs keep arriving, potentially never completing. In systems where fairness or guaranteed progress matters, non-preemptive SJF or other algorithms may be preferred despite the slightly higher average wait time."

- question: "Why does SJF cause starvation, and how do real operating systems address this problem?"
  type: short-answer
  answer: "SJF always favors the shortest job, so a long process can be indefinitely postponed if a steady stream of shorter jobs keeps arriving — its wait time grows without bound. Real systems address this through aging: the effective priority of a waiting process gradually increases with elapsed wait time, so a long-waiting process eventually becomes the highest-priority job regardless of burst time. Multilevel feedback queues implement a similar idea by promoting processes to higher-priority queues the longer they wait, preventing starvation while still generally favoring short jobs."
  explanation: "Starvation is the fundamental fairness failure of any priority scheme that ignores elapsed waiting time. SJF is the clearest example: pure optimality for average wait time and fairness are in direct conflict. Real schedulers always make some tradeoff between efficiency and fairness — pure SJF is a theoretical benchmark, not a deployed policy."
```

## Explainer

From CPU scheduling basics, you know the OS must choose which ready process gets the CPU next, and that different policies produce different average wait times. **Shortest Job First (SJF)** takes a greedy approach: always run the process with the shortest expected CPU burst next. The intuition is the same as choosing the fastest checkout line at a grocery store — letting the person with one item go first minimizes total waiting for everyone behind them.

To see why SJF is optimal for minimizing average waiting time, consider a simple example. Three processes arrive simultaneously with burst times of 6, 8, and 2 milliseconds. Under FCFS (in arrival order), waiting times are 0, 6, and 14 — average 6.67ms. Under SJF, the order is 2, 6, 8, giving waiting times of 0, 2, and 8 — average 3.33ms. SJF always wins because short jobs finish quickly and stop contributing to everyone else's wait. This can be proven formally: any schedule that does not run the shortest remaining job can be improved by swapping it earlier, which always reduces or maintains total waiting time.

The catch is that SJF requires knowing how long each process will run before it runs — and the OS cannot predict the future. In practice, systems **estimate** burst times using historical data: if a process's last three CPU bursts were 5ms, 6ms, and 4ms, the next is likely around 5ms. Exponential averaging is the classic technique, where recent bursts count more than older ones. These estimates are imperfect, but they make SJF approximately usable.

**Preemptive SJF**, also called **Shortest Remaining Time First (SRTF)**, goes further: if a new process arrives with a shorter burst than the time remaining on the currently running process, the OS preempts the running process immediately. This achieves even lower average waiting time but adds context-switch overhead and introduces a serious fairness problem — **starvation**. A long-running process can be perpetually pushed aside as short jobs keep arriving. This is the fundamental tradeoff: SJF is optimal for throughput and wait times but fundamentally unfair to long jobs, which is why real schedulers rarely use pure SJF and instead incorporate aging mechanisms or multi-level feedback queues to balance efficiency with fairness.
