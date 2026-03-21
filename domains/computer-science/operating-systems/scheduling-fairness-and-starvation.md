---
id: scheduling-fairness-and-starvation
title: Scheduling Fairness and Starvation Prevention
domain: computer-science
course: operating-systems
prerequisites:
- id: cpu-scheduling-basics
  type: hard
builds-toward:
- multilevel-feedback-queue-scheduling
tags:
- scheduling
- fairness
- concurrency
stage: formal-systems
status: draft
---

# Scheduling Fairness and Starvation Prevention

## Core Idea
Fair scheduling ensures all processes receive a reasonable share of CPU time and prevents indefinite delay (starvation). Starvation can occur when high-priority processes continuously arrive or when low-priority lock holders block high-priority processes. Modern systems use aging, priority inheritance, and proportional-share scheduling to mitigate these problems.

## Questions

```yaml
- question: "A system uses strict priority scheduling. Low-priority process P1 has been waiting 10 hours while a continuous stream of high-priority processes arrives. According to strict priority scheduling, P1:"
  type: multiple-choice
  options:
    - "Will eventually run after all currently queued high-priority processes complete"
    - "May never run if high-priority processes continue arriving faster than they finish"
    - "Will be automatically promoted to high priority after a threshold wait time"
    - "Will run because strict priority scheduling uses round-robin as a tiebreaker between priority levels"
  answer: 1
  explanation: "This is the definition of starvation: a process that is perpetually bypassed because higher-priority processes keep arriving. Strict priority scheduling has no mechanism to help P1 — it simply always picks the highest-priority ready process. Automatic promotion (option C) is the aging solution, which addresses starvation — but it is not part of strict priority scheduling by default. Starvation is what motivates aging as an add-on."

- question: "Priority inversion occurs when:"
  type: multiple-choice
  options:
    - "A high-priority process is blocked waiting for a lock held by a low-priority process, which is then preempted by a medium-priority process — indirectly blocking the high-priority one"
    - "Two high-priority processes compete for the same CPU time slice simultaneously"
    - "A low-priority process runs before a high-priority one because aging has boosted its priority"
    - "The scheduler runs out of priority levels and demotes all processes to the same tier"
  answer: 0
  explanation: "Priority inversion is the specific scenario where a high-priority process is effectively blocked by a medium-priority one through an indirect chain: high waits for a lock held by low; medium preempts low; now high is blocked while medium runs — despite medium having lower priority than high. Priority inheritance fixes this by temporarily boosting the lock holder (low) to the priority of its highest-priority waiter, so medium cannot preempt it."

- question: "Aging prevents starvation by gradually increasing the priority of a process the longer it waits in the ready queue."
  type: true-false
  answer: true
  explanation: "Aging is the standard solution to starvation in priority-based schedulers. By incrementally raising a waiting process's priority, aging ensures that even the lowest-priority process will eventually reach a priority level high enough to be scheduled. This converts a system with potential indefinite postponement into one with bounded waiting time."

- question: "A proportional-share scheduler like Linux's CFS guarantees that every process receives exactly equal CPU time regardless of its share weight."
  type: true-false
  answer: false
  explanation: "Proportional-share schedulers allocate CPU in proportion to each process's assigned shares — a process with twice the shares gets roughly twice the CPU time, not equal time. CFS specifically tracks 'virtual runtime' and always schedules the process with the least accumulated virtual runtime, scaled by its weight. Equality is a special case when all processes have equal shares; the general guarantee is proportionality, not equality."

- question: "Explain why priority inheritance is needed to solve priority inversion, and why simply permanently raising the lock holder's priority to 'high' would be wrong."
  type: short-answer
  answer: "Priority inheritance temporarily elevates the lock holder's priority to match the highest-priority process waiting for the lock. Once the lock is released, the holder's priority reverts to normal. This ensures the lock holder is not preempted before releasing the resource, unblocking the high-priority waiter quickly. Permanently raising the low-priority process's priority would be wrong because it would change its scheduling behavior for all future work — giving it unfair CPU access even after the contested lock is released — and could itself cause starvation for other medium-priority processes."
  explanation: "The key is that the priority boost is scoped to the lock-holding period only. The goal is to eliminate the indirect blocking chain, not to fundamentally reassign priorities."
```

## Explainer

From your study of CPU scheduling basics, you know that the scheduler decides which ready process gets the CPU next, using algorithms like round-robin, shortest-job-first, or priority scheduling. Each algorithm optimizes for something — throughput, response time, or urgency. But optimizing for one metric can create a dangerous side effect: some processes may wait indefinitely. This indefinite postponement is called **starvation**, and preventing it is one of the central challenges in scheduler design.

Starvation most commonly occurs in **priority scheduling**. Imagine a system where high-priority processes keep arriving faster than they can complete. Every time the scheduler checks the ready queue, it finds a high-priority process waiting, so the low-priority process at the back never runs. The low-priority process is technically ready — it has everything it needs — but it starves because the scheduler always picks someone else. This is analogous to standing in a line where anyone with a VIP pass can cut in front of you: if VIPs arrive continuously, you wait forever.

The classic solution is **aging** — gradually increasing a process's priority the longer it waits. A process that has been in the ready queue for a long time eventually reaches a priority high enough to compete with newcomers. Aging converts a strict priority system into one that balances urgency with fairness. A related problem is **priority inversion**, where a high-priority process is blocked waiting for a lock held by a low-priority process, and a medium-priority process preempts the lock holder, indirectly blocking the high-priority one. **Priority inheritance** fixes this by temporarily boosting the lock holder's priority to match the highest-priority waiter, ensuring the lock is released promptly.

Beyond these fixes, some schedulers take a fundamentally different approach to fairness. **Proportional-share** (or fair-share) schedulers allocate CPU time as shares rather than strict priorities — a process with twice the shares gets roughly twice the CPU time, but no process gets zero. Linux's Completely Fair Scheduler (CFS) implements this idea using a virtual runtime metric: it always picks the process with the least accumulated virtual runtime, ensuring that over any reasonable time window, every process receives its proportional allocation. The key insight is that fairness and efficiency are not opposites — a well-designed scheduler achieves both by bounding how long any process can be neglected.
