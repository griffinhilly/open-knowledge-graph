---
id: distributed-snapshots
title: Distributed Snapshots and Consistent State Capture
domain: computer-science
course: distributed-systems
prerequisites:
- id: distributed-system-models
  type: hard
- id: logical-clocks
  type: hard
builds-toward:
- chandy-lamport-algorithm
- distributed-tracing
tags:
- consistency
- snapshots
- state-capture
stage: advanced
status: validated
---

# Distributed Snapshots and Consistent State Capture

## Core Idea
A distributed snapshot captures the state of every process and all in-flight messages at a single logical instant across the system. Without a global clock, achieving consistency is non-trivial: a snapshot must be mutually consistent such that replaying the captured state and messages allows the system to continue correctly. Snapshots are used for recovery, monitoring, and debugging.

## Questions

```yaml
- question: "In a distributed system, process P1 sends a $100 payment to P2 and then records its local state (balance: $900). P2 records its local state (balance: $500) before receiving the payment. The message is still in transit. What must a correct snapshot algorithm do?"
  type: multiple-choice
  options:
    - "Discard the snapshot — any snapshot where a sent message has not yet been received is inconsistent and must be retaken"
    - "Assign the in-transit $100 to P1's recorded state, showing P1 with $1,000"
    - "Record the in-transit $100 as part of the channel state, so the snapshot captures $900 + $500 + $100 in-flight = consistent total"
    - "Roll back P1's state to before the send, so both processes agree no transfer occurred"
  answer: 2
  explanation: "A consistent snapshot must account for messages that were sent before one process recorded its state but not yet received when the other process recorded its state. These in-transit messages are captured as the channel state. If we ignored the in-transit $100, the snapshot would show $1,400 in total wealth when there should be $1,500 — money would appear to have vanished. Recording the channel state preserves the invariant and ensures the captured global state could have been a valid intermediate state of the system."

- question: "In the Chandy-Lamport algorithm, when a process receives a marker on a channel for the first time, what does it do?"
  type: multiple-choice
  options:
    - "It immediately stops processing all messages until all other processes have sent their markers"
    - "It records its own local state (if it has not done so already) and begins recording all messages arriving on its other incoming channels until markers arrive on those channels too"
    - "It forwards the marker only to processes it has sent messages to recently, to minimize overhead"
    - "It requests a global coordinator to freeze the system and collect all channel states simultaneously"
  answer: 1
  explanation: "The elegance of Chandy-Lamport is that it is fully decentralized and non-blocking. Upon receiving a marker on channel C for the first time: (1) the process records its local state if it hasn't already, and (2) it begins recording incoming messages on all *other* channels (not C) — these messages were in transit and belong to the channel state. When a marker arrives on each remaining channel, the process stops recording that channel's state. The channel from which the first marker arrived has an empty state, because the process recorded its state exactly when the marker arrived, so no messages on that channel are in the 'snapshot window'."

- question: "A consistent distributed snapshot represents the exact global system state at a specific instant in wall-clock time."
  type: true-false
  answer: false
  explanation: "This is the key conceptual subtlety of distributed snapshots. Because processes run independently with no global clock, there is no 'pause button' that freezes every process simultaneously. A consistent snapshot (consistent cut) is a logically valid state that respects causal ordering — if the snapshot includes the effect of an event, it includes all causally preceding events. But this logical cut may never have existed simultaneously in real time; it is a state the system *could have passed through*, which is sufficient for recovery, deadlock detection, and invariant checking, even though it does not correspond to any single wall-clock moment."

- question: "Distributed snapshots are useful not only for fault recovery (checkpointing) but also for monitoring live system properties like invariant checking and deadlock detection."
  type: true-false
  answer: true
  explanation: "Snapshots have multiple applications beyond crash recovery. For invariant checking, you can capture the global state and verify that conserved quantities (total money, total message count) are preserved — without stopping the system. For deadlock detection, you analyze the snapshot's resource-wait graph for cycles. For debugging, you can inspect global state at a logical point without interrupting execution. None of these require the snapshot to correspond to a real-time instant — logical consistency is sufficient for all of them."

- question: "What makes a distributed snapshot 'consistent,' and why is this consistency necessary for the snapshot to be useful for purposes like fault recovery or invariant checking?"
  type: short-answer
  answer: "A consistent snapshot satisfies the condition that if it includes the effect of any event, it also includes all causally preceding events (it respects the happened-before partial order). Concretely, it means: if process P1's recorded state shows a message was sent, either P2's recorded state shows it was received, or the message is captured as in-transit in the channel state. Without this, replaying the snapshot could produce contradictions — messages received that were never sent, or resources that appear or disappear. Consistency ensures the captured state is one the system could have legitimately occupied, making it a valid starting point for recovery or analysis."
  explanation: "The happened-before relation (from Lamport clocks) defines causal order. A consistent cut is one where you can draw a line through the event history of each process such that no message crosses the line from right to left — i.e., no message is shown as 'received' in the snapshot without its corresponding 'send' also being in the snapshot (or in the channel state). This is what the marker mechanism achieves: the marker acts as the cut line for each channel, ensuring all pre-marker messages are captured and all post-marker messages are excluded."
```

## Explainer

In a single-machine system, taking a snapshot is straightforward: pause everything, save the state, resume. In a distributed system, there is no global pause button. Processes run independently, messages are in flight between them, and there is no shared clock to coordinate a simultaneous freeze. A **distributed snapshot** must capture the local state of every process and all messages currently in transit, producing a picture of the system that is internally consistent — even though no single instant in real time corresponds to this picture.

The consistency requirement is subtle. Imagine two processes, P1 and P2. P1 sends a message, then records its state. P2 records its state, then receives the message. In P2's snapshot, the message has not arrived — but P1's snapshot shows the message as sent. If the snapshot fails to account for this in-flight message, it has lost information. A **consistent snapshot** (also called a consistent cut) ensures that if the snapshot includes the effect of any event, it also includes all events that causally preceded it. From your study of Lamport timestamps, you know that happened-before relationships define causal order — a consistent snapshot respects these relationships.

The core insight behind distributed snapshot algorithms is the use of **marker messages**. A process that initiates the snapshot records its own state and sends a special marker on every outgoing channel. When a process receives a marker on a channel, it records its own state (if it hasn't already) and records the state of that channel as all the messages received on it after its own state recording but before the marker arrived. The marker essentially acts as a divider: everything before it was "in the snapshot," everything after was not. This is the foundation of the Chandy-Lamport algorithm, which you will study next.

Distributed snapshots have several practical applications. **Checkpointing** for fault tolerance: periodically snapshot the system so that after a crash, processes can roll back to the last consistent snapshot rather than restarting from scratch. **Deadlock detection**: analyze the snapshot to check for cycles in resource-wait graphs. **Monitoring and debugging**: capture the system state to verify invariants (like "total money in the system is conserved") without stopping the system. The snapshot does not correspond to any actual moment in wall-clock time, but it represents a state the system could have passed through — which is sufficient for all of these purposes.
