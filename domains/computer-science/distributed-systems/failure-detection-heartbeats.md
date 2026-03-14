---
id: failure-detection-heartbeats
title: Failure Detection with Heartbeats
domain: computer-science
course: distributed-systems
prerequisites:
- id: distributed-system-models
  type: hard
- id: failure-models-distributed
  type: hard
builds-toward:
- network-partition-tolerance
- hinted-handoff
- timeout-retry-strategies
tags:
- failure-detection
- monitoring
- liveness
stage: advanced
status: draft
---

# Failure Detection with Heartbeats

## Core Idea
Heartbeat-based failure detection operates by having each node periodically send 'alive' signals to other nodes. If a node fails to receive a heartbeat within a timeout window, it declares that node dead. This is a simple, decentralized approach, but it struggles with false positives due to network delays and packet loss, particularly during congestion.

## How It's Best Learned
Simulate heartbeat mechanisms with varying network delays and failure scenarios. Understand the tradeoff between detection latency and false positive rate. Study real implementations in Cassandra or Redis.

## Common Misconceptions
- Heartbeats guarantee accurate failure detection (no protocol can distinguish crash from slow network). - Heartbeat intervals should be very short for quick detection (this causes more false positives and overhead). - All nodes must use the same heartbeat interval (adaptive intervals per link are better).
