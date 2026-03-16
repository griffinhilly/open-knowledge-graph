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

## Explainer

Consider a distributed system with multiple processes communicating over message channels. You want to answer a global question — what is the total balance across all bank accounts, or has the system reached a deadlocked state? The naive approach would be to pause everything, record the state of every process and every channel, and resume. But halting a distributed system is expensive and often impractical. The **Chandy-Lamport algorithm** solves this by capturing a **consistent global snapshot** while the system continues running normally.

The algorithm works by propagating special **marker messages** through the communication channels. One process initiates the snapshot by recording its own local state and immediately sending a marker on every outgoing channel. When a process receives a marker on a channel for the first time, it records its own state (if it hasn't already) and begins recording all messages arriving on that channel. When it receives a marker on a channel it's already recording, it stops recording that channel — the recorded messages represent the **channel state** (messages that were in flight during the snapshot). The process also sends markers on all its outgoing channels when it first records its state. The snapshot is complete when every process has recorded its state and every channel's state has been captured.

The key insight, grounded in your understanding of the happened-before relation, is that the resulting snapshot is **consistent** — it corresponds to a **consistent cut** of the system's execution. A consistent cut means that if the snapshot includes an event, it also includes all events that causally precede it. No message appears as received without also appearing as sent. This doesn't mean the snapshot reflects the system's state at any single physical instant — processes record their states at different real-world times. Instead, it represents a state the system *could have* passed through under some valid ordering of events. This is sufficient for most analyses: checking invariants, detecting deadlocks, or computing global aggregates.

A practical example helps solidify this. Imagine three bank processes: A, B, and C. A initiates the snapshot by recording its balance ($100) and sends markers to B and C. Meanwhile, B sends $20 to C. B receives A's marker, records its balance ($50), and starts recording incoming channels. The $20 message to C was sent before C received any marker, so it's captured as part of the channel state between B and C. The final snapshot shows A=$100, B=$50, C's recorded balance plus $20 in transit — the total is conserved, the snapshot is consistent, and no process ever had to stop executing. This property — capturing a meaningful global state without coordination overhead — makes Chandy-Lamport foundational for monitoring, checkpointing, and garbage collection in distributed systems.
