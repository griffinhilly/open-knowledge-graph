---
id: deadlock-handling
title: Deadlock Handling Strategies
domain: computer-science
course: operating-systems
prerequisites:
- id: deadlock-conditions
  type: hard
tags:
- deadlock-prevention
- deadlock-avoidance
- bankers-algorithm
- deadlock-detection
- recovery
stage: formal-systems
status: validated
---

# Deadlock Handling Strategies

## Core Idea
Operating systems handle deadlock through four strategies: prevention (design the system so at least one Coffman condition cannot hold — e.g., require all resources be requested at once, eliminating hold-and-wait); avoidance (allow only safe states using algorithms like Dijkstra's Banker's Algorithm, which grants resources only if a safe execution sequence exists); detection (allow deadlocks to occur, periodically run a detection algorithm, then recover by terminating or preempting processes); or simply ignoring the problem (the ostrich algorithm, acceptable when deadlocks are rare and recovery cost is low). Most practical systems use a combination: careful API design to prevent some classes, timeout-based detection for others.

## How It's Best Learned
Trace through the Banker's Algorithm manually with a small resource table. Then debate: for a real-time embedded system versus a general-purpose desktop OS, which strategy is most appropriate and why?

## Common Misconceptions
- The Banker's Algorithm requires processes to declare their maximum resource needs upfront, which is often impractical.
- Terminating processes as deadlock recovery can cause data corruption if not done carefully.
