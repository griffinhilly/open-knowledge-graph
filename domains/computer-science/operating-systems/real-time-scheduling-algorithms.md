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

## Explainer

From your study of priority scheduling, you know that assigning fixed priorities to processes determines who runs when the CPU is available. Real-time scheduling takes this idea and adds a critical constraint: every task has a **deadline** that must be met, or the system fails. Think of an anti-lock braking system — if the brake controller misses its 10-millisecond window to adjust pressure, the car doesn't stop safely. Unlike general-purpose scheduling where fairness and throughput matter most, real-time scheduling is about **predictability and guarantees**.

**Rate-Monotonic Scheduling (RMS)** is the simplest approach: assign higher priority to tasks that run more frequently. A task that repeats every 5 ms gets higher priority than one repeating every 20 ms. The intuition is that frequent tasks have tighter timing constraints, so they should preempt less frequent ones. RMS is a **static priority** algorithm — priorities are assigned once at design time and never change. Its key theoretical result is the schedulability bound: if total CPU utilization stays below approximately 69% (more precisely, n(2^(1/n) − 1) for n tasks), all deadlines are guaranteed to be met. This conservative bound means RMS sometimes rejects task sets that would actually work, but it never accepts one that will fail.

**Earliest Deadline First (EDF)** takes a dynamic approach. Instead of fixed priorities, the scheduler always picks the task whose deadline is nearest. If Task A's deadline is 8 ms away and Task B's is 3 ms away, B runs first regardless of their periods. EDF is **optimal** for single-processor systems — it can schedule any task set that is theoretically schedulable, up to 100% CPU utilization. The tradeoff is implementation complexity: the scheduler must continuously re-evaluate deadlines, and when the system is overloaded, EDF's behavior becomes unpredictable because many tasks miss deadlines simultaneously.

The choice between RMS and EDF reflects a classic engineering tradeoff. RMS is simpler to implement and analyze, making it preferred in safety-critical systems like avionics and medical devices where certification demands provable behavior. EDF extracts more useful work from the processor but is harder to reason about under overload. In practice, many real-time systems use RMS with utilization well below the bound, trading CPU efficiency for the certainty that no deadline will ever be missed.
