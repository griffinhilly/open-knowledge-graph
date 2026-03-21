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

## Questions

```yaml
- question: "Process B has a local Lamport counter of 3 when it receives a message from Process A stamped with timestamp 7. What value does Process B assign as its new counter?"
  type: multiple-choice
  options:
    - "3 — B keeps its own counter unchanged"
    - "7 — B adopts the sender's timestamp directly"
    - "8 — B sets its counter to max(3, 7) + 1"
    - "10 — B sums the two counter values"
  answer: 2
  explanation: "The Lamport update rule on receipt is: new_counter = max(local, received) + 1. Here max(3, 7) = 7, so the counter becomes 8. The +1 is essential — it ensures the receive event gets a strictly higher timestamp than the corresponding send event, preserving causal order. Simply adopting the sender's value (option 1) would make send and receive simultaneous, which violates the algorithm."

- question: "Event X on process P1 has Lamport timestamp 5. Event Y on process P2 has Lamport timestamp 8. A colleague concludes that X must have happened before Y. This conclusion is:"
  type: multiple-choice
  options:
    - "Always correct — smaller Lamport timestamps reliably indicate earlier causal occurrence"
    - "Always incorrect — Lamport timestamps carry no information about ordering"
    - "Possibly correct but not provable from timestamps alone — ts(X) < ts(Y) is consistent with X → Y but does not prove it"
    - "Correct specifically because X and Y are on different processes"
  answer: 2
  explanation: "Lamport's clock condition is one-directional: if A happened-before B, then ts(A) < ts(B). The converse does not hold. X and Y may be causally unrelated (concurrent) yet incidentally assigned timestamps 5 and 8 based on local counter states. The only safe inference from ts(X) < ts(Y) is that Y did not causally precede X. To distinguish 'X caused Y' from 'X and Y are concurrent,' you need vector clocks, which track per-process causal history."

- question: "In a distributed system using Lamport timestamps, if event A happened-before event B, then A's timestamp is guaranteed to be strictly less than B's timestamp."
  type: true-false
  answer: true
  explanation: "This is the Lamport clock condition and it is guaranteed by the algorithm. Every causal link — local increments and the max+1 rule on receipt — ensures effects always receive strictly higher timestamps than their causes. This one-directional guarantee makes Lamport timestamps sufficient for establishing a consistent total ordering of events across a distributed system."

- question: "If event A has a strictly lower Lamport timestamp than event B, then A must have happened before B in the distributed execution."
  type: true-false
  answer: false
  explanation: "This is the converse of the clock condition, and it does not hold. Two concurrent (causally unrelated) events on separate processes can have any timestamp relationship depending on their local counter histories. A lower timestamp eliminates the possibility that B caused A, but does not prove A caused B. This is the core limitation of Lamport timestamps — they cannot detect concurrency — and the primary motivation for vector clocks."

- question: "Explain why Lamport timestamps cannot determine whether two events are concurrent, and what structural information would need to be added to the clock mechanism to detect concurrency."
  type: short-answer
  answer: "Lamport timestamps collapse each process's causal history into a single scalar. This is enough to build a total order (sufficient for mutual exclusion or replicated state machines) but loses the structure needed to distinguish 'A happened before B' from 'A and B are concurrent with A getting a lower counter by coincidence.' To detect concurrency, vector clocks maintain a separate counter per process. Two events are concurrent precisely when neither event's vector dominates the other — no single integer comparison can capture this."
  explanation: "The fundamental limitation is information loss: a scalar cannot encode the full causal graph of a distributed execution. Vector clocks trade simplicity (one integer per event) for expressiveness (full causal comparison). The choice between them depends on whether the application needs only to order events or also to identify independent ones."
```

## Explainer

From your study of logical clocks, you know that physical clocks in a distributed system cannot be perfectly synchronized — network delays, clock drift, and relativity itself make a global "wall clock time" unreliable for ordering events. **Lamport timestamps** solve a specific, critical problem: given two events in a distributed system, can we determine whether one *must have* happened before the other? Leslie Lamport showed that a single integer counter per process, combined with a simple update rule, is enough to capture causal ordering.

The algorithm is remarkably simple. Each process maintains a local counter, starting at zero. On every **local event** (a computation step, a state change), the process increments its counter by one. When a process **sends a message**, it increments its counter and attaches the current value to the message. When a process **receives a message**, it sets its counter to `max(local_counter, received_timestamp) + 1`. That's the entire algorithm. The max operation is the key insight: it ensures that a receiving process's clock jumps forward to at least match the sender's, preserving the causal chain. If process A sends a message at timestamp 5 to process B whose local clock is at 3, B's clock jumps to 6 — correctly reflecting that B's receive event happened after A's send event.

The fundamental guarantee is the **clock condition**: if event A happened before event B (A causally precedes B), then A's timestamp is strictly less than B's timestamp. This means timestamps are consistent with causality — you will never see a cause stamped *after* its effect. However, the converse is **not** true: if A's timestamp is less than B's timestamp, A did not necessarily happen before B. Two independent events on different processes might coincidentally have timestamps where one is smaller than the other, even though they are causally unrelated (concurrent). Lamport timestamps can confirm causality in one direction but cannot distinguish "happened-before" from "happened-to-get-a-smaller-number."

This one-directional guarantee is both the strength and the limitation. It's sufficient for establishing a **total order** over all events — if two events have the same timestamp, you break ties using process IDs — which is useful for algorithms that need a consistent global ordering (such as mutual exclusion or replicated state machines). But if you need to *detect* concurrency — to know when two events are causally independent — Lamport timestamps are insufficient. That's the problem vector clocks solve, by maintaining a separate counter for each process. Lamport timestamps trade expressiveness for simplicity: one integer per event, one comparison to check ordering, and zero dependency on physical clocks.
