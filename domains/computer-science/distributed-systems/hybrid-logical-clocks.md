---
id: hybrid-logical-clocks
title: Hybrid Logical Clocks
domain: computer-science
course: distributed-systems
prerequisites:
- id: lamport-timestamps
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
status: draft
---
# Hybrid Logical Clocks

## Core Idea
Hybrid Logical Clocks (HLC) combine physical time and logical clocks: they advance with physical time (like NTP clocks) but increment logically when events are causally dependent, ensuring that if event A happens before event B in physical time, A's HLC is less than B's. This bounds the clock skew error while preserving causal ordering.

## Explainer

From Lamport timestamps, you know how to assign logical clocks that respect causality: if event A happens before event B, then A's timestamp is less than B's. But Lamport timestamps are pure logical counters with no connection to wall-clock time — timestamp 42 tells you nothing about *when* an event occurred, only its position in the causal order. Physical clocks give you real time but suffer from **clock skew** — different machines' clocks drift apart, so you can't rely on physical timestamps for ordering. **Hybrid Logical Clocks (HLC)** solve this by combining both: they stay close to physical time while guaranteeing causal ordering.

An HLC timestamp has two components: a **physical part** (the best-known physical time) and a **logical part** (a counter that breaks ties). When a node generates a local event, it sets the physical part to the maximum of its current HLC physical part and its current wall-clock time, then resets the logical part to zero (if the physical part advanced) or increments it (if wall-clock time hasn't advanced past the stored physical part). When a node receives a message, it sets the physical part to the maximum of its own physical part, the sender's physical part, and its current wall-clock time, then sets the logical counter accordingly. This "max" rule ensures the physical part never goes backward and always reflects the most recent physical time any causally connected node has observed.

The result is a timestamp that is always within the clock skew bound of real physical time (typically milliseconds with NTP), and that also satisfies the Lamport clock property: if A happens before B, then HLC(A) < HLC(B). You compare HLC timestamps by comparing the physical part first, then the logical part as a tiebreaker. This gives you something neither pure logical clocks nor pure physical clocks can offer alone — you can use HLC timestamps for causal ordering *and* for approximate real-time queries like "show me all events from the last five minutes." The physical component is meaningful in human terms; the logical component handles the edge cases where physical time alone would give ambiguous or incorrect ordering.

HLCs are particularly valuable in distributed databases that need to implement **snapshot isolation** or **causal consistency**. Systems like CockroachDB and MongoDB use HLC-style timestamps to order transactions across nodes without requiring a centralized timestamp oracle. Because the physical part stays close to real time, the system can efficiently determine that a snapshot at time T includes all events with HLC timestamps ≤ T, with bounded error. If you've studied vector clocks, note the tradeoff: vector clocks capture the full causal structure (you can tell whether two events are concurrent), but their size grows with the number of nodes. HLCs are fixed-size (just two numbers) regardless of system scale, but they only tell you "A happened before B" or "we can't determine the order" — they don't explicitly represent concurrency. For systems where compact timestamps and physical time proximity matter more than full concurrency detection, HLCs are the practical choice.
