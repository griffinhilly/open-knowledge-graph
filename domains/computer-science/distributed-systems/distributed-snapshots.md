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
