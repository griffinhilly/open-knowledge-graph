---
id: logical-clocks
title: Logical Clocks and Event Ordering
domain: computer-science
course: distributed-systems
prerequisites:
- id: distributed-systems-overview
  type: hard
- id: process-concept
  type: soft
builds-toward:
- lamport-timestamps
- vector-clocks
tags:
- time
- ordering
- causality
stage: advanced
status: draft
---

# Logical Clocks and Event Ordering

## Core Idea
Without synchronized physical clocks, distributed systems need logical mechanisms to order events. Logical clocks assign monotonically increasing values to events based on message passing and local execution, capturing causal relationships and enabling detection of whether one event could have influenced another.

## Explainer

In a single-threaded program on one machine, events have a natural order: whatever runs first happened first. You can look at wall-clock time and know exactly which instruction preceded which. In a distributed system, this breaks down completely. Each node has its own clock, and those clocks drift apart — sometimes by milliseconds, sometimes by seconds. If node A timestamps an event at 10:00:00.003 and node B timestamps an event at 10:00:00.001, you cannot conclude that B's event happened first. The clocks are simply not synchronized well enough to make that comparison meaningful.

**Logical clocks** solve this by abandoning wall-clock time entirely and instead tracking **causality** — the "could have influenced" relationship between events. The core insight, formalized by Leslie Lamport, is the **happens-before** relation: if event A occurs before event B on the same process, or if A is a message send and B is the corresponding receive, then A happens-before B. This relation is transitive: if A happens-before B and B happens-before C, then A happens-before C. Events with no happens-before path between them are **concurrent** — neither could have influenced the other.

A logical clock implements this by assigning each event a counter value. Every process maintains a local counter. When a process executes an event, it increments its counter. When it sends a message, it attaches the counter value. When it receives a message, it sets its counter to the maximum of its own counter and the received value, then increments. This ensures that if event A happens-before event B, then A's counter value is strictly less than B's. The converse is not necessarily true — two events may have ordered counter values yet be concurrent — which is why Lamport clocks capture a partial order rather than a total one.

Understanding logical clocks is essential because they underpin nearly every distributed algorithm you will encounter. Lamport timestamps extend this basic idea to create a total order (by breaking ties with process IDs). Vector clocks go further, giving each process its own counter dimension so you can detect concurrency precisely. But the foundation is always the same: replace unreliable physical time with a counter discipline that faithfully tracks causality through message passing.
