---
id: distributed-snapshots-chandy-lamport
title: Distributed Snapshots and Chandy-Lamport Algorithm
domain: computer-science
course: distributed-systems
prerequisites:
- id: happened-before-relation-causality
  type: hard
- id: vector-clocks
  type: soft
builds-toward:
- distributed-system-observability
- causal-consistency-implementation
tags:
- snapshots
- consistency
- global-state
- algorithm
stage: advanced
status: draft
---

# Distributed Snapshots and Chandy-Lamport Algorithm

## Core Idea
The Chandy-Lamport algorithm captures a consistent global snapshot of a distributed system without stopping all processes. It uses markers sent along message channels to identify which in-flight messages belong to the snapshot, ensuring the snapshot respects the happened-before relation and represents a feasible system state.

## How It's Best Learned
Trace through the algorithm by hand on a small system (3 processes, messages) and verify the snapshot is consistent. Understand why the marker must be sent immediately and why receiving the marker on all channels is necessary.

## Common Misconceptions
- Snapshots must freeze all processes; Chandy-Lamport allows processes to continue running.
- The snapshot captures the exact moment of a query; it captures a state that could have been reached through some ordering of events.

## Questions

```yaml
- question: "When a process receives a marker on a channel for the first time during a Chandy-Lamport snapshot, what actions does it take?"
  type: multiple-choice
  options:
    - "It pauses all processing until it has received markers on every incoming channel"
    - "It records its local state (if not already done), begins recording messages arriving on that channel, and sends markers on all its outgoing channels"
    - "It discards all messages received after the marker on that channel and waits for the initiator to confirm"
    - "It forwards the marker to the next process in a ring topology and records nothing until confirmed"
  answer: 1
  explanation: "Receiving a first marker triggers three actions: record own state (if not yet done), start recording incoming messages on this channel (to capture in-flight messages), and send markers on all outgoing channels to propagate the snapshot. Crucially, the process does NOT pause — it continues normal execution. Recording stops on a channel only when a subsequent marker arrives on it (signaling the channel state is complete)."

- question: "In a distributed bank system, Process A holds $100 and sends $50 to Process B before initiating a snapshot. A records its state ($50) and sends markers. The $50 message is still in transit when B receives the marker and records its balance of $200. What does the complete snapshot show?"
  type: multiple-choice
  options:
    - "A=$100, B=$200 — the snapshot reflects states before any transactions"
    - "A=$50, B=$200, with $50 recorded as in-transit in the A→B channel state"
    - "A=$50, B=$250 — the transaction completes before the snapshot is considered final"
    - "The snapshot is invalid because A and B recorded their states at different physical times"
  answer: 1
  explanation: "B received the marker before it received A's $50 message, so B starts recording incoming messages on the A→B channel after the marker. The $50 message arrives after the marker is recorded, making it part of the A→B channel state. The snapshot shows A=$50 (post-send), B=$200 (pre-receive), plus $50 in the channel — total $300, conserved. Snapshots taken at different physical times are expected and valid; what matters is consistency, not simultaneity."

- question: "A Chandy-Lamport snapshot captures the exact global state of the system at a single physical moment in time."
  type: true-false
  answer: false
  explanation: "Different processes record their states at different real-world times — the snapshot is explicitly not a simultaneous photograph. Instead, it captures a *consistent cut*: a state the system could have passed through under some valid causal ordering of events. No message appears as received without having been sent, which is the consistency guarantee. The snapshot may not correspond to any instant that actually occurred, but it represents a state reachable through some valid execution, which is sufficient for invariant checking and debugging."

- question: "A consistent Chandy-Lamport snapshot guarantees that any global invariant (such as total money conservation) that held throughout the system's execution will also hold in the captured snapshot."
  type: true-false
  answer: true
  explanation: "Because the snapshot represents a feasible past state of the system (a consistent cut), any invariant that was true at every moment of real execution must also hold in the snapshot. Every message either appears in the state of the process that received it, or in the channel state as in-transit — no message is double-counted or lost. This means quantities like total money are conserved in the snapshot, making it reliable for detecting violations of global invariants."

- question: "Why is a 'consistent cut' sufficient for practical uses of distributed snapshots, even though it may not correspond to any single moment in real time?"
  type: short-answer
  answer: "Most useful global properties — conservation of resources, absence of deadlock, invariant conditions — depend only on causal relationships, not on physical simultaneity. A consistent cut guarantees that no causal violation exists: no effect appears without its cause. If the system was in a valid state satisfying some invariant throughout its execution, any consistent cut will also satisfy that invariant. This means the snapshot can be used to verify global properties, detect deadlocks, or checkpoint state without ever needing to freeze the system or agree on a global clock."
  explanation: "This is the deeper insight: distributed systems cannot have a globally synchronized clock (per Lamport's work), so 'simultaneous' is meaningless. The happened-before relation provides a substitute — causal consistency — that is strong enough for most practical guarantees while permitting processes to keep running during the snapshot."
```

## Explainer

Consider a distributed system with multiple processes communicating over message channels. You want to answer a global question — what is the total balance across all bank accounts, or has the system reached a deadlocked state? The naive approach would be to pause everything, record the state of every process and every channel, and resume. But halting a distributed system is expensive and often impractical. The **Chandy-Lamport algorithm** solves this by capturing a **consistent global snapshot** while the system continues running normally.

The algorithm works by propagating special **marker messages** through the communication channels. One process initiates the snapshot by recording its own local state and immediately sending a marker on every outgoing channel. When a process receives a marker on a channel for the first time, it records its own state (if it hasn't already) and begins recording all messages arriving on that channel. When it receives a marker on a channel it's already recording, it stops recording that channel — the recorded messages represent the **channel state** (messages that were in flight during the snapshot). The process also sends markers on all its outgoing channels when it first records its state. The snapshot is complete when every process has recorded its state and every channel's state has been captured.

The key insight, grounded in your understanding of the happened-before relation, is that the resulting snapshot is **consistent** — it corresponds to a **consistent cut** of the system's execution. A consistent cut means that if the snapshot includes an event, it also includes all events that causally precede it. No message appears as received without also appearing as sent. This doesn't mean the snapshot reflects the system's state at any single physical instant — processes record their states at different real-world times. Instead, it represents a state the system *could have* passed through under some valid ordering of events. This is sufficient for most analyses: checking invariants, detecting deadlocks, or computing global aggregates.

A practical example helps solidify this. Imagine three bank processes: A, B, and C. A initiates the snapshot by recording its balance ($100) and sends markers to B and C. Meanwhile, B sends $20 to C. B receives A's marker, records its balance ($50), and starts recording incoming channels. The $20 message to C was sent before C received any marker, so it's captured as part of the channel state between B and C. The final snapshot shows A=$100, B=$50, C's recorded balance plus $20 in transit — the total is conserved, the snapshot is consistent, and no process ever had to stop executing. This property — capturing a meaningful global state without coordination overhead — makes Chandy-Lamport foundational for monitoring, checkpointing, and garbage collection in distributed systems.
