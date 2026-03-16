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

## Explainer

From your study of failure models, you know that nodes in a distributed system can fail in various ways — crash failures, omission failures, Byzantine failures. But knowing that failures *can* happen is different from knowing that one *has* happened. **Failure detection** is the mechanism by which live nodes determine that another node has stopped functioning, and the heartbeat protocol is the simplest and most widely used approach.

The basic idea is almost trivially simple. Every node periodically sends a small "I'm alive" message — a **heartbeat** — to other nodes (or to a central monitor). If node A does not receive a heartbeat from node B within a specified **timeout window**, A suspects that B has failed. The elegance is in the decentralized nature: no special failure-detection server is needed, and the protocol works with any network topology. In practice, heartbeats can be direct (every node pings every other node), gossip-based (nodes randomly share heartbeat information with peers, spreading liveness knowledge epidemically), or hierarchical (nodes report to designated monitors).

The fundamental tension in heartbeat-based detection is between **detection speed** and **accuracy**. A short timeout means you detect failures quickly — but you also generate more **false positives**, declaring nodes dead when they are merely slow or when the network is temporarily congested. A long timeout reduces false positives but means genuinely crashed nodes go undetected for longer, during which time the system may be operating with stale assumptions. This tradeoff is not a tuning problem you can solve with the right constant — it is a fundamental impossibility result. In an asynchronous network (one with no upper bound on message delivery time), it is provably impossible to build a perfect failure detector that is both complete (eventually detects every failure) and accurate (never makes false accusations).

Real systems deal with this by accepting imperfection and adding sophistication. **Phi accrual failure detectors** (used in Cassandra) replace the binary alive/dead verdict with a continuous suspicion level based on the statistical distribution of recent heartbeat arrival times. If heartbeats from node B typically arrive every 500ms with a standard deviation of 50ms, and the last one was 2 seconds ago, the suspicion level is very high. **Gossip-based heartbeats** (used in Amazon's systems) reduce network overhead by having each node gossip heartbeat tables to random peers rather than directly pinging every other node, scaling O(n) per node instead of O(n²). The key practical lesson is that failure detection is always probabilistic — the system must be designed to handle both missed detections and false alarms gracefully.
