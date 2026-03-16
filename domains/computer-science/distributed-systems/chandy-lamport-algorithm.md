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
stage: advanced
status: draft
---

# Chandy-Lamport Snapshot Algorithm

## Core Idea
The Chandy-Lamport algorithm is a protocol for capturing a consistent distributed snapshot without halting the system. An initiator sends a marker message to all outgoing channels. Upon receiving a marker, a process records its state, saves the marker, and begins buffering all messages on incoming channels. After receiving markers on all channels, the buffered messages are included in the snapshot.

## How It's Best Learned
Trace the algorithm step-by-step through a 3-4 node system with message timings. Understand why markers must propagate along every channel and how buffering captures in-flight state without global coordination.

## Common Misconceptions
- The snapshot represents a physically simultaneous state (it is a logical cut through the distributed execution). - Processes must be programmed to expect markers (the algorithm works on unmodified processes). - Markers travel instantaneously (the algorithm's complexity depends on system diameter).

## Explainer

You know from distributed snapshots that capturing the global state of a distributed system is fundamentally difficult — there is no shared clock, and each process only sees its own local state plus the messages it sends and receives. You also know from logical clocks that events in a distributed system can be ordered without physical time synchronization. The **Chandy-Lamport algorithm** combines these insights into an elegant protocol that captures a *consistent* snapshot of the entire system while it continues to run.

The algorithm works in three phases, initiated by any single process. The **initiator** records its own local state, then sends a special **marker message** along every outgoing communication channel. When a process receives a marker on a channel for the first time, it records its own local state and immediately sends markers on all of *its* outgoing channels. It also begins recording all messages that arrive on other incoming channels (channels from which it has not yet received a marker). When a marker finally arrives on one of those other channels, the process stops recording on that channel — the recorded messages represent the **in-flight messages** that were in the channel at the time of the snapshot.

The key insight is what "consistent" means here. The snapshot does not represent a single instant in physical time — that concept is meaningless in a distributed system with no global clock. Instead, it represents a **consistent cut**: a division of all events into "before the snapshot" and "after the snapshot" such that if an event is in the "after" set, none of its causal predecessors are also in the "after" set. This is exactly the kind of causal consistency that logical clocks help reason about. The marker messages act as barriers — they propagate through the system and ensure that every process records its state at a causally consistent point.

Consider a concrete example: three bank branches (processes A, B, C) that transfer money between accounts via messages. Process A initiates a snapshot, records its balance, and sends markers to B and C. Before B receives A's marker, B sends a $50 transfer to A. When A receives this $50 message before B's marker arrives on that channel, A records it as an in-flight message — money that was "in the channel" at snapshot time. The final snapshot includes each branch's recorded balance plus all in-flight transfers, and the total money in the system is conserved. This is what makes the algorithm so valuable: you can verify global invariants (like conservation of money) from a snapshot taken without ever pausing the system.

The algorithm requires that channels are FIFO (messages arrive in the order they were sent) and reliable (no messages are lost). The FIFO requirement is essential because it ensures that once a process receives a marker on a channel, all pre-snapshot messages on that channel have already arrived. Without FIFO ordering, a pre-snapshot message could arrive after the marker, and the snapshot would miss it, breaking consistency. Understanding these assumptions clarifies both the power and the limitations of the algorithm — and motivates the more complex snapshot protocols needed for systems without FIFO guarantees.
