---
id: distributed-snapshots
title: Distributed Snapshots and Consistent State Capture
domain: computer-science
course: distributed-systems
prerequisites:
- id: distributed-system-models
  type: hard
- id: lamport-timestamps
  type: hard
builds-toward:
- chandy-lamport-algorithm
- distributed-tracing
tags:
- consistency
- snapshots
- state-capture
stage: advanced
status: draft
---

# Distributed Snapshots and Consistent State Capture

## Core Idea
A distributed snapshot captures the state of every process and all in-flight messages at a single logical instant across the system. Without a global clock, achieving consistency is non-trivial: a snapshot must be mutually consistent such that replaying the captured state and messages allows the system to continue correctly. Snapshots are used for recovery, monitoring, and debugging.

## Explainer

In a single-machine system, taking a snapshot is straightforward: pause everything, save the state, resume. In a distributed system, there is no global pause button. Processes run independently, messages are in flight between them, and there is no shared clock to coordinate a simultaneous freeze. A **distributed snapshot** must capture the local state of every process and all messages currently in transit, producing a picture of the system that is internally consistent — even though no single instant in real time corresponds to this picture.

The consistency requirement is subtle. Imagine two processes, P1 and P2. P1 sends a message, then records its state. P2 records its state, then receives the message. In P2's snapshot, the message has not arrived — but P1's snapshot shows the message as sent. If the snapshot fails to account for this in-flight message, it has lost information. A **consistent snapshot** (also called a consistent cut) ensures that if the snapshot includes the effect of any event, it also includes all events that causally preceded it. From your study of Lamport timestamps, you know that happened-before relationships define causal order — a consistent snapshot respects these relationships.

The core insight behind distributed snapshot algorithms is the use of **marker messages**. A process that initiates the snapshot records its own state and sends a special marker on every outgoing channel. When a process receives a marker on a channel, it records its own state (if it hasn't already) and records the state of that channel as all the messages received on it after its own state recording but before the marker arrived. The marker essentially acts as a divider: everything before it was "in the snapshot," everything after was not. This is the foundation of the Chandy-Lamport algorithm, which you will study next.

Distributed snapshots have several practical applications. **Checkpointing** for fault tolerance: periodically snapshot the system so that after a crash, processes can roll back to the last consistent snapshot rather than restarting from scratch. **Deadlock detection**: analyze the snapshot to check for cycles in resource-wait graphs. **Monitoring and debugging**: capture the system state to verify invariants (like "total money in the system is conserved") without stopping the system. The snapshot does not correspond to any actual moment in wall-clock time, but it represents a state the system could have passed through — which is sufficient for all of these purposes.
