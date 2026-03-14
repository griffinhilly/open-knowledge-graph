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
