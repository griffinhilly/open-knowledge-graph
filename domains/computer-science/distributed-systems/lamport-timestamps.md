---
id: lamport-timestamps
title: Lamport Timestamps
domain: computer-science
course: distributed-systems
prerequisites:
- id: logical-clocks
  type: hard
builds-toward:
- causal-ordering
- consensus-problem
tags:
- timestamps
- ordering
- lamport
stage: advanced
status: draft
---

# Lamport Timestamps

## Core Idea
Lamport timestamps assign scalar timestamps to events using a simple rule: each process maintains a counter that is incremented on local events and set to max(local, received) + 1 on message receipt. If event A causally precedes event B, then A's timestamp is strictly less than B's timestamp, enabling total ordering of events across the system.

## How It's Best Learned
Trace execution of multiple processes sending messages and track how timestamps evolve.

## Common Misconceptions
Lamport timestamps uniquely determine causality (they only order causally related events); they require synchronized physical clocks.

## Explainer

From your study of logical clocks, you know that physical clocks in a distributed system cannot be perfectly synchronized — network delays, clock drift, and relativity itself make a global "wall clock time" unreliable for ordering events. **Lamport timestamps** solve a specific, critical problem: given two events in a distributed system, can we determine whether one *must have* happened before the other? Leslie Lamport showed that a single integer counter per process, combined with a simple update rule, is enough to capture causal ordering.

The algorithm is remarkably simple. Each process maintains a local counter, starting at zero. On every **local event** (a computation step, a state change), the process increments its counter by one. When a process **sends a message**, it increments its counter and attaches the current value to the message. When a process **receives a message**, it sets its counter to `max(local_counter, received_timestamp) + 1`. That's the entire algorithm. The max operation is the key insight: it ensures that a receiving process's clock jumps forward to at least match the sender's, preserving the causal chain. If process A sends a message at timestamp 5 to process B whose local clock is at 3, B's clock jumps to 6 — correctly reflecting that B's receive event happened after A's send event.

The fundamental guarantee is the **clock condition**: if event A happened before event B (A causally precedes B), then A's timestamp is strictly less than B's timestamp. This means timestamps are consistent with causality — you will never see a cause stamped *after* its effect. However, the converse is **not** true: if A's timestamp is less than B's timestamp, A did not necessarily happen before B. Two independent events on different processes might coincidentally have timestamps where one is smaller than the other, even though they are causally unrelated (concurrent). Lamport timestamps can confirm causality in one direction but cannot distinguish "happened-before" from "happened-to-get-a-smaller-number."

This one-directional guarantee is both the strength and the limitation. It's sufficient for establishing a **total order** over all events — if two events have the same timestamp, you break ties using process IDs — which is useful for algorithms that need a consistent global ordering (such as mutual exclusion or replicated state machines). But if you need to *detect* concurrency — to know when two events are causally independent — Lamport timestamps are insufficient. That's the problem vector clocks solve, by maintaining a separate counter for each process. Lamport timestamps trade expressiveness for simplicity: one integer per event, one comparison to check ordering, and zero dependency on physical clocks.
