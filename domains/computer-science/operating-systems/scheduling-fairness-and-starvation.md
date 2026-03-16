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

## Explainer

From your study of CPU scheduling basics, you know that the scheduler decides which ready process gets the CPU next, using algorithms like round-robin, shortest-job-first, or priority scheduling. Each algorithm optimizes for something — throughput, response time, or urgency. But optimizing for one metric can create a dangerous side effect: some processes may wait indefinitely. This indefinite postponement is called **starvation**, and preventing it is one of the central challenges in scheduler design.

Starvation most commonly occurs in **priority scheduling**. Imagine a system where high-priority processes keep arriving faster than they can complete. Every time the scheduler checks the ready queue, it finds a high-priority process waiting, so the low-priority process at the back never runs. The low-priority process is technically ready — it has everything it needs — but it starves because the scheduler always picks someone else. This is analogous to standing in a line where anyone with a VIP pass can cut in front of you: if VIPs arrive continuously, you wait forever.

The classic solution is **aging** — gradually increasing a process's priority the longer it waits. A process that has been in the ready queue for a long time eventually reaches a priority high enough to compete with newcomers. Aging converts a strict priority system into one that balances urgency with fairness. A related problem is **priority inversion**, where a high-priority process is blocked waiting for a lock held by a low-priority process, and a medium-priority process preempts the lock holder, indirectly blocking the high-priority one. **Priority inheritance** fixes this by temporarily boosting the lock holder's priority to match the highest-priority waiter, ensuring the lock is released promptly.

Beyond these fixes, some schedulers take a fundamentally different approach to fairness. **Proportional-share** (or fair-share) schedulers allocate CPU time as shares rather than strict priorities — a process with twice the shares gets roughly twice the CPU time, but no process gets zero. Linux's Completely Fair Scheduler (CFS) implements this idea using a virtual runtime metric: it always picks the process with the least accumulated virtual runtime, ensuring that over any reasonable time window, every process receives its proportional allocation. The key insight is that fairness and efficiency are not opposites — a well-designed scheduler achieves both by bounding how long any process can be neglected.
