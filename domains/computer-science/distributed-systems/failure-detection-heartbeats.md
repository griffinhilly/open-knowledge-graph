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

## Questions

```yaml
- question: "A team sets their heartbeat timeout to 100ms to detect node failures as quickly as possible. Their operations team starts receiving many 'node down' alerts that resolve within seconds. What is the most likely root cause?"
  type: multiple-choice
  options:
    - "The nodes are actually crashing and recovering — 100ms is appropriate for detecting this"
    - "The timeout is too short: brief network congestion or processing spikes cause heartbeats to arrive late, triggering false positives"
    - "The heartbeat interval itself should be shortened to match the timeout"
    - "Gossip-based heartbeats would eliminate this problem entirely without any tradeoff"
  answer: 1
  explanation: "Short timeouts improve detection latency for real failures but increase the false positive rate — declaring a live node dead because a heartbeat was delayed by transient network congestion, a garbage collection pause, or a busy CPU. This is the core detection-speed vs. accuracy tradeoff. The false positive storm is a classic symptom of an overly aggressive timeout. Gossip-based approaches (option D) reduce overhead but do not eliminate the fundamental timeout tradeoff."

- question: "A node in a distributed system hasn't received a heartbeat from a peer for three times the normal interval. The network is experiencing unusual congestion. What can the observing node definitively conclude?"
  type: multiple-choice
  options:
    - "The peer has crashed and should be marked as failed immediately"
    - "The peer is experiencing a Byzantine failure and may be sending corrupt messages"
    - "Nothing definitive — in an asynchronous network, missing heartbeats cannot distinguish a crashed node from a very slow one"
    - "The peer has definitely not crashed but needs its heartbeat interval increased"
  answer: 2
  explanation: "This is the fundamental impossibility result: in an asynchronous network (no upper bound on message delivery time), no timeout value can definitively distinguish a crashed node from one that is alive but slow. The missing heartbeats could be caused by a crash, by severe congestion delaying messages, or by the peer being overloaded. A perfect failure detector — one that is both complete (detects all failures) and accurate (never makes false accusations) — is provably impossible in the asynchronous model. Real systems must accept this and design for graceful handling of both false positives and false negatives."

- question: "In a fully synchronous network where message delivery time is bounded by a known maximum delay δ, it is theoretically possible to build a perfect failure detector."
  type: true-false
  answer: true
  explanation: "True. The impossibility result applies specifically to asynchronous networks, which have no upper bound on message delay. If you know that any message will arrive within δ time units, you can set a timeout of δ + ε and be certain: if a heartbeat hasn't arrived by then, the node has truly crashed (not merely slow). The synchrony assumption is what makes the distinction between 'crashed' and 'slow' detectable. Real-world networks are asynchronous, which is why the impossibility matters in practice."

- question: "Heartbeat-based failure detection can definitively identify whether a node has crashed or is merely slow, as long as the timeout is calibrated correctly."
  type: true-false
  answer: false
  explanation: "False. No timeout calibration overcomes the fundamental impossibility in an asynchronous network. Even a perfectly tuned timeout only reduces false positives — it cannot eliminate them, because network behavior is unbounded. A node that takes 10 seconds to respond is indistinguishable from a crashed node during those 10 seconds. The impossibility result (proved by Fischer, Lynch, and Paterson for consensus, extended to failure detection) shows that in an asynchronous model, completeness and accuracy cannot both be guaranteed simultaneously."

- question: "Why do systems like Cassandra use phi accrual failure detectors rather than simple binary timeout-based heartbeats?"
  type: short-answer
  answer: "Phi accrual detectors replace the binary alive/dead verdict with a continuous suspicion score (φ) based on the statistical distribution of recent heartbeat arrival times. If heartbeats from a node normally arrive every 500ms with low variance, and the last one was 3 seconds ago, φ is very high. If the network is normally variable (high jitter), the same 3-second gap produces a lower φ. This adaptive approach avoids the fixed-threshold problem: a timeout that works under normal conditions may generate false positives during congestion or false negatives if the network slows down. Systems can then set different response thresholds for different actions — e.g., 'log a warning' at φ=5, 'route around' at φ=8, 'declare dead' at φ=12."
  explanation: "The phi accrual approach treats heartbeat arrival times as a statistical process and measures the probability that the observed gap is due to failure rather than normal variation. This makes the detector self-calibrating: it learns the typical behavior of each link and computes suspicion relative to that baseline. It reduces both false positives (during congestion) and detection latency (when failure actually occurs), at the cost of complexity."
```

## Explainer

From your study of failure models, you know that nodes in a distributed system can fail in various ways — crash failures, omission failures, Byzantine failures. But knowing that failures *can* happen is different from knowing that one *has* happened. **Failure detection** is the mechanism by which live nodes determine that another node has stopped functioning, and the heartbeat protocol is the simplest and most widely used approach.

The basic idea is almost trivially simple. Every node periodically sends a small "I'm alive" message — a **heartbeat** — to other nodes (or to a central monitor). If node A does not receive a heartbeat from node B within a specified **timeout window**, A suspects that B has failed. The elegance is in the decentralized nature: no special failure-detection server is needed, and the protocol works with any network topology. In practice, heartbeats can be direct (every node pings every other node), gossip-based (nodes randomly share heartbeat information with peers, spreading liveness knowledge epidemically), or hierarchical (nodes report to designated monitors).

The fundamental tension in heartbeat-based detection is between **detection speed** and **accuracy**. A short timeout means you detect failures quickly — but you also generate more **false positives**, declaring nodes dead when they are merely slow or when the network is temporarily congested. A long timeout reduces false positives but means genuinely crashed nodes go undetected for longer, during which time the system may be operating with stale assumptions. This tradeoff is not a tuning problem you can solve with the right constant — it is a fundamental impossibility result. In an asynchronous network (one with no upper bound on message delivery time), it is provably impossible to build a perfect failure detector that is both complete (eventually detects every failure) and accurate (never makes false accusations).

Real systems deal with this by accepting imperfection and adding sophistication. **Phi accrual failure detectors** (used in Cassandra) replace the binary alive/dead verdict with a continuous suspicion level based on the statistical distribution of recent heartbeat arrival times. If heartbeats from node B typically arrive every 500ms with a standard deviation of 50ms, and the last one was 2 seconds ago, the suspicion level is very high. **Gossip-based heartbeats** (used in Amazon's systems) reduce network overhead by having each node gossip heartbeat tables to random peers rather than directly pinging every other node, scaling O(n) per node instead of O(n²). The key practical lesson is that failure detection is always probabilistic — the system must be designed to handle both missed detections and false alarms gracefully.
