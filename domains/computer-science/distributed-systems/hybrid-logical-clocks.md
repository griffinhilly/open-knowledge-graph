---
id: hybrid-logical-clocks
title: Hybrid Logical Clocks
domain: computer-science
course: distributed-systems
prerequisites:
- id: logical-clocks
  type: hard
- id: vector-clocks
  type: soft
builds-toward: []
tags:
- clocks
- physical-time
- logical-time
- hybrid
stage: advanced
status: validated
---
# Hybrid Logical Clocks

## Core Idea
Hybrid Logical Clocks (HLC) combine physical time and logical clocks: they advance with physical time (like NTP clocks) but increment logically when events are causally dependent, ensuring that if event A happens before event B in physical time, A's HLC is less than B's. This bounds the clock skew error while preserving causal ordering.

## Questions

```yaml
- question: "Node A sends a message to Node B. A's HLC physical part is 500ms; B's current HLC physical part before receiving the message is 300ms; B's wall clock reads 450ms. After receiving the message, what is B's new HLC physical part?"
  type: multiple-choice
  options:
    - "300ms — B keeps its own physical part to avoid jumping forward"
    - "450ms — B always uses its local wall clock for the physical part"
    - "500ms — B takes the maximum of its current physical part, A's physical part, and its wall clock"
    - "400ms — B averages A's physical part and its own wall clock to prevent large jumps"
  answer: 2
  explanation: "The HLC 'max' rule sets the physical part to the maximum of: the receiver's current HLC physical part (300ms), the sender's HLC physical part (500ms), and the receiver's local wall clock (450ms). The maximum is 500ms. This ensures the physical part never goes backward along causal chains: any event causally following A inherits A's best-known physical time, keeping the timestamp close to real time while maintaining causal monotonicity."

- question: "A distributed systems engineer needs to determine definitively whether two events A and B are concurrent (neither caused the other). Should they use HLC timestamps or vector clocks?"
  type: multiple-choice
  options:
    - "HLC, because comparing the physical part first and the logical part second directly encodes concurrency information"
    - "HLC, because its two-component structure is mathematically equivalent to a vector clock for detecting concurrency"
    - "Vector clocks, because HLC can only tell you that A happened before B or that the order is undetermined — it cannot confirm that two events are explicitly concurrent"
    - "Either works identically; HLC is simply a more compact encoding of the same causal information as vector clocks"
  answer: 2
  explanation: "HLC preserves the Lamport clock property: if A → B (A causally precedes B), then HLC(A) < HLC(B). But the converse is not guaranteed — HLC(A) < HLC(B) does not prove A caused B. When HLC timestamps are incomparable or equal, you know nothing definitive about concurrency. Vector clocks explicitly represent the causal history of each event: if neither V(A) ≤ V(B) nor V(B) ≤ V(A) component-wise, the events are definitively concurrent. This is the fundamental tradeoff: vector clocks grow O(N) in the number of nodes but provide full concurrency detection; HLCs are fixed-size (two numbers) but sacrifice explicit concurrency detection."

- question: "HLC timestamps are fixed-size (two numbers) regardless of how many nodes are in the distributed system, whereas vector clock size grows linearly with the number of nodes."
  type: true-false
  answer: true
  explanation: "A vector clock must track one counter per node in the system, so V ∈ ℤᴺ for an N-node system. An HLC timestamp is always just two values: the physical part (max observed wall-clock time) and the logical counter (a tiebreaker). This fixed size makes HLCs practical in large distributed systems — a vector clock in a 10,000-node system would be enormous per event, while an HLC remains just two integers. The cost is losing the ability to explicitly detect concurrency, but for many applications (transaction ordering, snapshot isolation) the causal ordering guarantee is sufficient."

- question: "Because the physical component of an HLC timestamp reflects the node's wall-clock time, you can use HLC timestamps to determine the exact wall-clock moment when any given event occurred, to within NTP precision."
  type: true-false
  answer: false
  explanation: "The HLC physical part is not the wall-clock time of the event itself — it is the maximum wall-clock time observed across all causally preceding events (via the 'max' rule). An event's HLC physical part may be higher than the node's actual wall clock at the moment the event occurred, because it inherited a higher physical time from a received message. The HLC timestamp is bounded within the clock skew of real physical time (typically milliseconds with NTP), but it represents the highest observed physical time along the causal path, not a precise timestamp of when the event happened."

- question: "Explain why the 'max' rule in HLC update — taking the maximum of the receiver's current physical part, the sender's physical part, and the local wall clock — is essential for both the Lamport causal ordering property and the bounded skew from real time."
  type: short-answer
  answer: "The max rule serves two goals simultaneously. For causal ordering: by inheriting the sender's physical part (or the receiver's own if higher), the physical component never decreases along causal chains. When the physical parts are equal, the logical counter increments to break the tie, ensuring HLC(cause) < HLC(effect). This gives the Lamport property. For bounded skew: because the local wall clock is always included in the max, the physical part can never fall behind real time by more than the clock drift since the last clock synchronization. Even if a causally isolated node hasn't communicated recently, its HLC physical part advances with its own wall clock, staying within the NTP skew bound of real time."
  explanation: "Without taking the max of the local wall clock, the physical part could stagnate if a node is causally isolated. Without taking the max of the sender's physical part, causal monotonicity would break when the sender has a faster clock. Both components of the max are necessary."
```

## Explainer

From Lamport timestamps, you know how to assign logical clocks that respect causality: if event A happens before event B, then A's timestamp is less than B's. But Lamport timestamps are pure logical counters with no connection to wall-clock time — timestamp 42 tells you nothing about *when* an event occurred, only its position in the causal order. Physical clocks give you real time but suffer from **clock skew** — different machines' clocks drift apart, so you can't rely on physical timestamps for ordering. **Hybrid Logical Clocks (HLC)** solve this by combining both: they stay close to physical time while guaranteeing causal ordering.

An HLC timestamp has two components: a **physical part** (the best-known physical time) and a **logical part** (a counter that breaks ties). When a node generates a local event, it sets the physical part to the maximum of its current HLC physical part and its current wall-clock time, then resets the logical part to zero (if the physical part advanced) or increments it (if wall-clock time hasn't advanced past the stored physical part). When a node receives a message, it sets the physical part to the maximum of its own physical part, the sender's physical part, and its current wall-clock time, then sets the logical counter accordingly. This "max" rule ensures the physical part never goes backward and always reflects the most recent physical time any causally connected node has observed.

The result is a timestamp that is always within the clock skew bound of real physical time (typically milliseconds with NTP), and that also satisfies the Lamport clock property: if A happens before B, then HLC(A) < HLC(B). You compare HLC timestamps by comparing the physical part first, then the logical part as a tiebreaker. This gives you something neither pure logical clocks nor pure physical clocks can offer alone — you can use HLC timestamps for causal ordering *and* for approximate real-time queries like "show me all events from the last five minutes." The physical component is meaningful in human terms; the logical component handles the edge cases where physical time alone would give ambiguous or incorrect ordering.

HLCs are particularly valuable in distributed databases that need to implement **snapshot isolation** or **causal consistency**. Systems like CockroachDB and MongoDB use HLC-style timestamps to order transactions across nodes without requiring a centralized timestamp oracle. Because the physical part stays close to real time, the system can efficiently determine that a snapshot at time T includes all events with HLC timestamps ≤ T, with bounded error. If you've studied vector clocks, note the tradeoff: vector clocks capture the full causal structure (you can tell whether two events are concurrent), but their size grows with the number of nodes. HLCs are fixed-size (just two numbers) regardless of system scale, but they only tell you "A happened before B" or "we can't determine the order" — they don't explicitly represent concurrency. For systems where compact timestamps and physical time proximity matter more than full concurrency detection, HLCs are the practical choice.
