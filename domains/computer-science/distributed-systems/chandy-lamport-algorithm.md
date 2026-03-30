---
id: chandy-lamport-algorithm
title: Chandy-Lamport Snapshot Algorithm
domain: computer-science
course: distributed-systems
prerequisites:
- id: distributed-snapshots
  type: hard
- id: logical-clocks
  type: hard
builds-toward:
- distributed-tracing
tags:
- snapshots
- algorithm
- consistency
stage: expert
status: validated
---

# Chandy-Lamport Snapshot Algorithm

## Core Idea
The Chandy-Lamport algorithm is a protocol for capturing a consistent distributed snapshot without halting the system. An initiator sends a marker message to all outgoing channels. Upon receiving a marker, a process records its state, saves the marker, and begins buffering all messages on incoming channels. After receiving markers on all channels, the buffered messages are included in the snapshot.

## How It's Best Learned
Trace the algorithm step-by-step through a 3-4 node system with message timings. Understand why markers must propagate along every channel and how buffering captures in-flight state without global coordination.

## Common Misconceptions
- The snapshot represents a physically simultaneous state (it is a logical cut through the distributed execution). - Processes must be programmed to expect markers (the algorithm works on unmodified processes). - Markers travel instantaneously (the algorithm's complexity depends on system diameter).

## Questions

```yaml
- question: "Process A initiates a snapshot, records its state, and sends markers. Before receiving A's marker, Process B sends a $50 transfer to A. A later receives this $50 message before B's marker arrives on that channel. How should A handle this $50 message?"
  type: multiple-choice
  options:
    - "Ignore it — A has already recorded its state, so messages arriving afterward are excluded from the snapshot"
    - "Record it as part of A's channel state — it is an in-flight message that was in transit at snapshot time"
    - "Discard it — only the initiating process records in-flight messages"
    - "Include it in the snapshot unconditionally, regardless of when it was sent"
  answer: 1
  explanation: "After recording its own local state, A begins buffering messages arriving on channels from which it has not yet received a marker. The $50 transfer arrived after A took its snapshot but before B's marker arrived on that channel — meaning the transfer was logically 'in-flight' at snapshot time. FIFO guarantees that B sent this message before sending its marker, so the message is a pre-snapshot event and must be included in the channel state to produce a consistent snapshot."

- question: "Why does the Chandy-Lamport algorithm require FIFO (first-in-first-out) communication channels?"
  type: multiple-choice
  options:
    - "To ensure that the initiating process sends markers before any regular messages during the snapshot"
    - "To guarantee that all messages sent before a marker on a given channel arrive at the receiver before that marker does"
    - "To prevent any process from recording its state more than once during a single snapshot"
    - "To ensure that marker messages travel faster than regular application messages"
  answer: 1
  explanation: "FIFO is essential for correctness. When a process receives a marker on a channel, it stops recording messages on that channel — assuming all pre-snapshot messages have already arrived. This assumption is only valid if channels are FIFO: if a message sent before the marker can arrive after it, the process would miss recording that pre-snapshot message, breaking the consistency of the cut. Without FIFO, a more complex protocol is required."

- question: "The Chandy-Lamport snapshot captures the global state of a distributed system at a single physical instant in time."
  type: true-false
  answer: false
  explanation: "This is the central misconception about distributed snapshots. There is no global clock in a distributed system — 'physical simultaneity' is meaningless across separate processes. The Chandy-Lamport snapshot instead captures a consistent cut: a division of all events into 'before' and 'after' the snapshot such that no 'after' event causally precedes a 'before' event. This logical consistency is sufficient for verifying global invariants, even though different processes record their state at different physical times."

- question: "When a process receives a marker message for the first time, it immediately records its own local state before forwarding markers to its neighbors."
  type: true-false
  answer: true
  explanation: "This is a critical rule of the algorithm. The process must record its state at the moment it first receives a marker — before any other actions — to ensure that state is captured before further messages can change it. It then sends markers on all outgoing channels and begins buffering messages on channels from which it has not yet received a marker. The order matters: record state, then propagate markers."

- question: "What does 'consistent cut' mean in the Chandy-Lamport algorithm, and why is consistency sufficient for verifying global invariants even without physical simultaneity?"
  type: short-answer
  answer: "A consistent cut divides all events into 'before the snapshot' and 'after the snapshot' such that if an event is in the 'after' set, none of its causal predecessors are in the 'before' set. This means the snapshot represents a state the system could have occupied — it is causally coherent. Global invariants like 'total money is conserved' must hold at every causally consistent state, so verifying them against a consistent snapshot is valid even though different processes recorded their state at different physical moments."
  explanation: "The key insight is that consistency is a logical property, not a temporal one. In a distributed system, causal ordering is the fundamental structure, not clock time. The Chandy-Lamport snapshot respects causal ordering because the marker barriers ensure each process records its state after all causally prior events have been processed. Any invariant that holds at every reachable system state will hold at a consistent snapshot — which is precisely what makes the algorithm practically useful for debugging, checkpointing, and verification."
```

## Explainer

You know from distributed snapshots that capturing the global state of a distributed system is fundamentally difficult — there is no shared clock, and each process only sees its own local state plus the messages it sends and receives. You also know from logical clocks that events in a distributed system can be ordered without physical time synchronization. The **Chandy-Lamport algorithm** combines these insights into an elegant protocol that captures a *consistent* snapshot of the entire system while it continues to run.

The algorithm works in three phases, initiated by any single process. The **initiator** records its own local state, then sends a special **marker message** along every outgoing communication channel. When a process receives a marker on a channel for the first time, it records its own local state and immediately sends markers on all of *its* outgoing channels. It also begins recording all messages that arrive on other incoming channels (channels from which it has not yet received a marker). When a marker finally arrives on one of those other channels, the process stops recording on that channel — the recorded messages represent the **in-flight messages** that were in the channel at the time of the snapshot.

The key insight is what "consistent" means here. The snapshot does not represent a single instant in physical time — that concept is meaningless in a distributed system with no global clock. Instead, it represents a **consistent cut**: a division of all events into "before the snapshot" and "after the snapshot" such that if an event is in the "after" set, none of its causal predecessors are also in the "after" set. This is exactly the kind of causal consistency that logical clocks help reason about. The marker messages act as barriers — they propagate through the system and ensure that every process records its state at a causally consistent point.

Consider a concrete example: three bank branches (processes A, B, C) that transfer money between accounts via messages. Process A initiates a snapshot, records its balance, and sends markers to B and C. Before B receives A's marker, B sends a $50 transfer to A. When A receives this $50 message before B's marker arrives on that channel, A records it as an in-flight message — money that was "in the channel" at snapshot time. The final snapshot includes each branch's recorded balance plus all in-flight transfers, and the total money in the system is conserved. This is what makes the algorithm so valuable: you can verify global invariants (like conservation of money) from a snapshot taken without ever pausing the system.

The algorithm requires that channels are FIFO (messages arrive in the order they were sent) and reliable (no messages are lost). The FIFO requirement is essential because it ensures that once a process receives a marker on a channel, all pre-snapshot messages on that channel have already arrived. Without FIFO ordering, a pre-snapshot message could arrive after the marker, and the snapshot would miss it, breaking consistency. Understanding these assumptions clarifies both the power and the limitations of the algorithm — and motivates the more complex snapshot protocols needed for systems without FIFO guarantees.
