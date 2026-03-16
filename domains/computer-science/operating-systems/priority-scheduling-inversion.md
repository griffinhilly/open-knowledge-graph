---
id: priority-scheduling-inversion
title: Priority Scheduling and Priority Inversion
domain: computer-science
course: operating-systems
prerequisites:
- id: scheduling-algorithm-analysis
  type: hard
- id: mutex-and-locks
  type: hard
builds-toward:
- critical-section-problem-formalization
tags:
- priority
- scheduling
- inversion
stage: formal-systems
status: draft
---

# Priority Scheduling and Priority Inversion

## Core Idea
Priority inversion occurs when a high-priority task waits for a low-priority task holding a lock. Solutions include priority inheritance (temporarily boost lock-holder to waiter's priority) and priority ceiling (pre-set lock priority to max priority that might acquire it).

## Explainer

From scheduling algorithms, you know that priority-based schedulers always run the highest-priority ready task. From your study of mutexes and locks, you know that a task holding a lock blocks any other task that tries to acquire the same lock. **Priority inversion** is what happens when these two mechanisms interact badly: a high-priority task ends up waiting — sometimes indefinitely — because of a low-priority task, violating the fundamental promise of priority scheduling.

Here is the classic scenario with three tasks. Task H (high priority) needs a shared resource protected by a lock. Task L (low priority) currently holds that lock. Task M (medium priority) does not need the lock at all. Because L holds the lock, H must wait for L to finish and release it. But now M becomes ready to run. The scheduler sees that M has higher priority than L, so it preempts L to run M. While M runs, L is suspended — still holding the lock — and H continues to wait. In effect, M (which has no relationship to the shared resource) is delaying H, a task with higher priority. This is **unbounded priority inversion**: any number of medium-priority tasks can preempt L and extend H's wait indefinitely.

**Priority inheritance** solves this by temporarily raising the lock-holder's priority. When H tries to acquire the lock held by L, the OS boosts L's priority to match H's. Now M cannot preempt L, because L is running at H's effective priority. L finishes its critical section quickly, releases the lock, drops back to its original priority, and H proceeds. The key property is that L runs at elevated priority only while it holds a lock that a higher-priority task is waiting for — the boost is transitive and temporary. The most famous real-world example of priority inversion was the Mars Pathfinder incident in 1997, where the Sojourner rover experienced repeated system resets caused by exactly this scenario, fixed by enabling priority inheritance in the VxWorks real-time OS.

**Priority ceiling protocol** takes a different approach: each lock is assigned a ceiling priority equal to the highest priority of any task that might ever acquire it. When a task acquires the lock, its priority is immediately raised to the ceiling, regardless of whether any higher-priority task is currently waiting. This prevents priority inversion entirely because no medium-priority task can preempt the lock holder. It also prevents deadlock in systems with multiple locks, because a task can only acquire a lock if its priority is strictly higher than the ceiling of any lock currently held by other tasks. The tradeoff is that priority ceiling requires knowing in advance which tasks will use which locks, making it less flexible but more predictable — a property that real-time systems value highly.
