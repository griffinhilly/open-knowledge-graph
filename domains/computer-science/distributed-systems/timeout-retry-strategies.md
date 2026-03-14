---
id: timeout-retry-strategies
title: Timeout and Retry Strategies
domain: computer-science
course: distributed-systems
prerequisites:
- id: failure-detection-heartbeats
  type: hard
- id: network-partition-tolerance
  type: hard
builds-toward:
- idempotent-operations
tags:
- fault-tolerance
- reliability
- strategy
stage: advanced
status: draft
---

# Timeout and Retry Strategies

## Core Idea
Timeout and retry strategies determine how systems respond to transient failures. Immediate retries can amplify load during congestion; exponential backoff with jitter reduces cascading failures. Adaptive timeouts adjust based on measured latencies. Choosing timeouts is critical: too short causes false timeouts, too long degrades latency. Timeouts must be paired with idempotent operations for safe retries.
