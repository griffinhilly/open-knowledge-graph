---
id: real-time-scheduling-algorithms
title: Real-Time Scheduling Algorithms
domain: computer-science
course: operating-systems
prerequisites:
- id: priority-scheduling-algorithms
  type: hard
- id: multilevel-feedback-queue-scheduling
  type: soft
tags:
- scheduling
- real-time
- deterministic
stage: formal-systems
status: draft
---

# Real-Time Scheduling Algorithms

## Core Idea
Real-time systems require deterministic scheduling guarantees to meet task deadlines. Rate-Monotonic Scheduling (RMS) assigns priorities inversely to task period length, while Earliest Deadline First (EDF) dynamically selects the task nearest its deadline. Both algorithms have precise schedulability conditions and are used in safety-critical applications.

## Questions

```yaml
- question: "A real-time system has three tasks with periods of 5 ms, 10 ms, and 20 ms. Under Rate-Monotonic Scheduling, which task gets the highest priority?"
  type: multiple-choice
  options:
    - "The task with period 20 ms, because it has the most slack time"
    - "The task with period 5 ms, because it runs most frequently and has the tightest constraints"
    - "They share equal priority since RMS is a dynamic algorithm"
    - "Priority depends on execution time, not period length"
  answer: 1
  explanation: "RMS assigns priority inversely proportional to period length: shorter period = higher priority. A task with a 5 ms period runs 4 times as often as the 20 ms task, meaning its deadline arrives far more frequently. RMS's insight is that frequency is a proxy for urgency. Priorities are assigned once at design time (static), not dynamically. The 5 ms task gets highest priority, 10 ms gets medium, 20 ms gets lowest."

- question: "A real-time system's total CPU utilization is 85%. Which scheduling algorithm can guarantee all deadlines are met, and which cannot?"
  type: multiple-choice
  options:
    - "Both RMS and EDF can guarantee deadlines at 85% utilization"
    - "Neither RMS nor EDF can guarantee deadlines above 69% utilization"
    - "EDF can guarantee deadlines (up to 100% utilization); RMS cannot guarantee them at 85%"
    - "RMS can guarantee deadlines; EDF cannot handle utilization above 80%"
  answer: 2
  explanation: "EDF is optimal for single-processor real-time systems — it can schedule any feasible task set up to 100% CPU utilization. At 85%, EDF guarantees all deadlines will be met. RMS, by contrast, has a schedulability bound of approximately 69% (for large numbers of tasks). At 85% utilization, RMS cannot guarantee all deadlines — some task sets at this utilization will be schedulable by EDF but will miss deadlines under RMS. The 69% bound is conservative: many specific task sets work above it with RMS, but there is no general guarantee."

- question: "EDF is preferred over RMS for safety-critical embedded systems like aircraft flight controllers because it can utilize 100% of CPU capacity."
  type: true-false
  answer: false
  explanation: "Despite EDF's theoretical optimality, safety-critical systems like avionics and medical devices typically prefer RMS. The reason is predictability under overload: when a system becomes overloaded, RMS fails gracefully — low-priority (long-period) tasks miss deadlines while high-priority (short-period) tasks continue to meet theirs. EDF under overload fails chaotically — many tasks miss deadlines unpredictably. Safety-critical systems are designed with utilization well below 69%, sacrificing CPU efficiency in exchange for analyzable, certifiable behavior."

- question: "Rate-Monotonic Scheduling is a dynamic priority algorithm that reassigns priorities whenever task periods change."
  type: true-false
  answer: false
  explanation: "RMS is a static priority algorithm — priorities are assigned once at system design time based on task periods and never change at runtime. A task with period 5 ms always has higher priority than one with period 20 ms, even if the 20 ms task is currently closer to its deadline. This static assignment is what makes RMS simple to implement and easy to analyze for certification. EDF, by contrast, is the dynamic algorithm that continuously evaluates which task has the nearest deadline and adjusts priorities accordingly."

- question: "Why do real-time systems often operate with CPU utilization well below the schedulability bound, even when they could theoretically run higher?"
  type: short-answer
  answer: "Keeping utilization well below the bound provides margin for transient overloads, measurement errors in execution times, and unanticipated tasks or interrupts. Real-world task execution times are estimates — actual execution can vary, and worst-case estimates are conservative. Operating below the bound ensures that even in adverse conditions, deadlines are still met. For safety-critical applications, the cost of a missed deadline (a plane crash, a failed drug infusion) far outweighs the cost of leaving CPU cycles unused."
  explanation: "This reflects the broader engineering principle that safety margins matter more than theoretical efficiency when failures have catastrophic consequences. The schedulability bound assumes worst-case execution times and perfectly periodic tasks — conditions that may not hold in practice. A real system running at 50% utilization with RMS has headroom to absorb reality; one running at 68% is betting that worst-case never actually occurs."
```

## Explainer

From your study of priority scheduling, you know that assigning fixed priorities to processes determines who runs when the CPU is available. Real-time scheduling takes this idea and adds a critical constraint: every task has a **deadline** that must be met, or the system fails. Think of an anti-lock braking system — if the brake controller misses its 10-millisecond window to adjust pressure, the car doesn't stop safely. Unlike general-purpose scheduling where fairness and throughput matter most, real-time scheduling is about **predictability and guarantees**.

**Rate-Monotonic Scheduling (RMS)** is the simplest approach: assign higher priority to tasks that run more frequently. A task that repeats every 5 ms gets higher priority than one repeating every 20 ms. The intuition is that frequent tasks have tighter timing constraints, so they should preempt less frequent ones. RMS is a **static priority** algorithm — priorities are assigned once at design time and never change. Its key theoretical result is the schedulability bound: if total CPU utilization stays below approximately 69% (more precisely, n(2^(1/n) − 1) for n tasks), all deadlines are guaranteed to be met. This conservative bound means RMS sometimes rejects task sets that would actually work, but it never accepts one that will fail.

**Earliest Deadline First (EDF)** takes a dynamic approach. Instead of fixed priorities, the scheduler always picks the task whose deadline is nearest. If Task A's deadline is 8 ms away and Task B's is 3 ms away, B runs first regardless of their periods. EDF is **optimal** for single-processor systems — it can schedule any task set that is theoretically schedulable, up to 100% CPU utilization. The tradeoff is implementation complexity: the scheduler must continuously re-evaluate deadlines, and when the system is overloaded, EDF's behavior becomes unpredictable because many tasks miss deadlines simultaneously.

The choice between RMS and EDF reflects a classic engineering tradeoff. RMS is simpler to implement and analyze, making it preferred in safety-critical systems like avionics and medical devices where certification demands provable behavior. EDF extracts more useful work from the processor but is harder to reason about under overload. In practice, many real-time systems use RMS with utilization well below the bound, trading CPU efficiency for the certainty that no deadline will ever be missed.
