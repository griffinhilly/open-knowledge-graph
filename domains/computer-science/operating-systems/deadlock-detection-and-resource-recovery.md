---
id: deadlock-detection-and-resource-recovery
title: Deadlock Detection and Recovery
domain: computer-science
course: operating-systems
prerequisites:
- id: deadlock-conditions-and-graphs
  type: hard
tags:
- deadlock
- detection
- recovery
- resource-allocation
stage: formal-systems
status: draft
---

# Deadlock Detection and Recovery

## Core Idea
Deadlock detection uses resource allocation graphs to identify cycles, indicating deadlock. The OS periodically checks for cycles. Recovery involves terminating processes (simple but destructive) or preempting resources (complex but less disruptive). Detection-and-recovery trades off prevention overhead for acceptance of occasional deadlocks.

## Explainer

From deadlock conditions and resource allocation graphs, you know that deadlock requires four conditions — mutual exclusion, hold and wait, no preemption, and circular wait — and that a cycle in the resource allocation graph proves deadlock exists for single-instance resources. **Deadlock detection and recovery** is the strategy of letting deadlocks happen and then cleaning up, as opposed to preventing or avoiding them in advance.

The detection algorithm works by constructing and analyzing the **wait-for graph**, a simplified version of the resource allocation graph that shows only which processes are waiting for which other processes. For single-instance resource types, finding a cycle in this graph is sufficient to confirm deadlock. For multi-instance resource types, the detection algorithm is more involved: it simulates resource allocation using available resources, marking processes that could finish with what is currently free, then releasing their resources and repeating. Any process that cannot be marked by the end of this simulation is deadlocked. This is essentially the same logic as the Banker's algorithm for avoidance, but run on current state rather than projected future state.

A critical design question is how often to run the detection algorithm. Running it after every resource request catches deadlocks immediately but adds overhead to every allocation. Running it periodically (say, every few minutes) or when resource utilization drops below a threshold reduces overhead but means deadlocked processes sit idle longer. The right frequency depends on how costly deadlocks are versus how costly detection is — in a system where deadlocks are rare, periodic detection is usually sufficient.

Once a deadlock is detected, the OS must break it. **Process termination** is the blunt approach: kill one or more deadlocked processes to release their resources. The OS can terminate all deadlocked processes at once (guaranteed to break the deadlock, but maximally destructive) or terminate them one at a time, re-running detection after each kill to see if the deadlock is resolved. **Resource preemption** is gentler: forcibly take a resource from one process and give it to another, rolling back the victim process to a safe state. This requires the ability to checkpoint and restore process state, which is not always feasible. In either case, the OS must choose a victim — typically the process with the lowest priority, the least accumulated computation, or the one holding the most resources. The detection-and-recovery approach is philosophically pragmatic: rather than constraining every allocation to prevent a rare event, it lets the system run freely and pays the recovery cost only when deadlock actually occurs.
