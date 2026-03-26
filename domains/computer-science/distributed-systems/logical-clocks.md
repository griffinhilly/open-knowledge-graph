---
id: logical-clocks
title: Logical Clocks and Event Ordering
domain: computer-science
course: distributed-systems
prerequisites:
- id: distributed-systems-introduction
  type: hard
- id: process-concept
  type: soft
builds-toward:
- vector-clocks
tags:
- time
- ordering
- causality
stage: advanced
status: validated
---

# Logical Clocks and Event Ordering

## Core Idea
Without synchronized physical clocks, distributed systems need logical mechanisms to order events. Logical clocks assign monotonically increasing values to events based on message passing and local execution, capturing causal relationships and enabling detection of whether one event could have influenced another.

## Questions

```yaml
- question: "Process A sends a message at local Lamport clock value 5, and process B receives it when its own clock reads 3. After the receive, B updates its clock. Then B executes another local event. What is B's clock value after that local event?"
  type: multiple-choice
  options:
    - "4 — B just increments from 3."
    - "6 — B sets its clock to max(3, 5) = 5, then increments to 6 after the receive, then increments again to 7... wait, the question asks after the local event following receive."
    - "7 — B sets clock to max(3, 5) + 1 = 6 on receive, then increments to 7 on the next local event."
    - "5 — B adopts the sender's timestamp to stay synchronized."
  answer: 2
  explanation: "When B receives a message carrying timestamp 5, it sets its clock to max(local, received) + 1 = max(3, 5) + 1 = 6. This is the clock value for the receive event itself. Then when B executes a subsequent local event, it increments again to 7. The rule ensures that if A's send (clock 5) happened-before B's receive, the receive's clock (6) is strictly greater than 5 — the happens-before ordering is preserved in the clock values."

- question: "Two events have Lamport clock values 10 (event X) and 15 (event Y). What can you reliably conclude about their causal relationship?"
  type: multiple-choice
  options:
    - "X happened-before Y, because 10 < 15."
    - "X and Y are concurrent, because their clock values differ by 5."
    - "If X happened-before Y, then clock(X) < clock(Y) — but clock(X) < clock(Y) does not prove X happened-before Y; they may be concurrent."
    - "Nothing can be said — Lamport clocks are unreliable for ordering events."
  answer: 2
  explanation: "Lamport clocks guarantee: if A happened-before B, then clock(A) < clock(B). But the converse does not hold: clock(A) < clock(B) does not imply A happened-before B. Two processes executing independently will have increasing clocks even with no causal connection. Clock(X) = 10 < 15 = clock(Y) tells us only that Y did not happen-before X — it is consistent with X happening-before Y OR with X and Y being concurrent. To detect concurrency precisely, you need vector clocks, which track one counter dimension per process."

- question: "If event A has a strictly smaller Lamport timestamp than event B, then A is expected to have happened-before B."
  type: true-false
  answer: false
  explanation: "This is the most important misconception about Lamport clocks. The guarantee runs only one direction: happened-before implies lower timestamp. The converse fails. Two concurrent events on separate processes will accumulate increasing timestamps independently — A's clock can be lower than B's simply because A's process has executed fewer events, not because of any causal link. Lamport timestamps can detect when events are NOT concurrent (if B's timestamp ≤ A's, then B cannot have happened-before A), but they cannot confirm causality from timestamp order alone."

- question: "Logical clocks are designed to detect and track the 'happens-before' causal relationship between distributed events, not to measure elapsed physical time."
  type: true-false
  answer: true
  explanation: "This is the central insight of logical clocks. Physical wall-clock time cannot be trusted for ordering events across distributed nodes because clocks drift and cannot be perfectly synchronized. Lamport's key insight was to replace physical time with a causal model: what matters is not when events occurred on a global clock, but whether one event could have influenced another through message passing or local execution ordering. The happens-before relation captures this precisely. Logical clocks implement a counter discipline that faithfully tracks this causal structure, regardless of physical timing."

- question: "Why is wall-clock time insufficient for ordering events in a distributed system, and what specific property do logical clocks provide instead?"
  type: short-answer
  answer: "Wall-clock time is insufficient because each node maintains its own clock and clocks inevitably drift apart — they cannot be perfectly synchronized. A timestamp on node A at 10:00:00.003 may actually refer to an event that occurred after an event timestamped 10:00:00.005 on node B, because A's clock runs fast. Logical clocks replace physical time with a causal counter discipline that tracks the happens-before relation: if event A could have causally influenced event B (because A executed before B on the same process, or A sent a message that B received), then clock(A) < clock(B). This gives a partial order consistent with causality, which is what distributed algorithms actually need."
  explanation: "The deeper point is that 'when' an event happened (in absolute physical time) is often irrelevant to correctness; what matters is 'could this event have been affected by that one?' Logical clocks answer exactly that question."
```

## Explainer

In a single-threaded program on one machine, events have a natural order: whatever runs first happened first. You can look at wall-clock time and know exactly which instruction preceded which. In a distributed system, this breaks down completely. Each node has its own clock, and those clocks drift apart — sometimes by milliseconds, sometimes by seconds. If node A timestamps an event at 10:00:00.003 and node B timestamps an event at 10:00:00.001, you cannot conclude that B's event happened first. The clocks are simply not synchronized well enough to make that comparison meaningful.

**Logical clocks** solve this by abandoning wall-clock time entirely and instead tracking **causality** — the "could have influenced" relationship between events. The core insight, formalized by Leslie Lamport, is the **happens-before** relation: if event A occurs before event B on the same process, or if A is a message send and B is the corresponding receive, then A happens-before B. This relation is transitive: if A happens-before B and B happens-before C, then A happens-before C. Events with no happens-before path between them are **concurrent** — neither could have influenced the other.

A logical clock implements this by assigning each event a counter value. Every process maintains a local counter. When a process executes an event, it increments its counter. When it sends a message, it attaches the counter value. When it receives a message, it sets its counter to the maximum of its own counter and the received value, then increments. This ensures that if event A happens-before event B, then A's counter value is strictly less than B's. The converse is not necessarily true — two events may have ordered counter values yet be concurrent — which is why Lamport clocks capture a partial order rather than a total one.

Understanding logical clocks is essential because they underpin nearly every distributed algorithm you will encounter. Lamport timestamps extend this basic idea to create a total order (by breaking ties with process IDs). Vector clocks go further, giving each process its own counter dimension so you can detect concurrency precisely. But the foundation is always the same: replace unreliable physical time with a counter discipline that faithfully tracks causality through message passing.
