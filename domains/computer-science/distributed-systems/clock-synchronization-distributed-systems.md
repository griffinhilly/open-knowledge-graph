---
id: clock-synchronization-distributed-systems
title: Clock Synchronization and Network Time Protocol
domain: computer-science
course: distributed-systems
prerequisites:
- id: synchronous-asynchronous-systems
  type: hard
builds-toward:
- happened-before-relation-causality
- hybrid-logical-clocks
tags:
- time
- synchronization
- ntp
- clocks
stage: advanced
status: draft
---

# Clock Synchronization and Network Time Protocol

## Core Idea
Physical clocks on different machines drift independently, and perfect synchronization is impossible. Network Time Protocol (NTP) achieves approximate synchronization by measuring network delays and adjusting local clocks, typically to within milliseconds. Understanding clock bounds is crucial for designing systems with time-based guarantees.

## How It's Best Learned
Implement a simple clock synchronization algorithm: measure RTT to a time server, estimate network delay, adjust local clock. Then examine how NTP layers complexity to handle multiple servers and stratum levels.

## Common Misconceptions
- Clocks can be perfectly synchronized; the best achievable is bounded skew (e.g., ±100ms with NTP).
- High-precision time is always available; GPS and atomic clocks are expensive and not universally accessible.

## Explainer

From your study of synchronous versus asynchronous system models, you know that distributed systems make different assumptions about timing. In a synchronous model, message delivery and clock drift have known bounds. In an asynchronous model, no such bounds exist. Real systems sit somewhere between these extremes, and **clock synchronization** is the practical problem of keeping physical clocks on different machines close enough to be useful — even though perfect agreement is impossible.

Every computer has a **physical clock** — a quartz oscillator that ticks at a rate determined by its crystal's properties. The problem is that no two crystals are identical: they drift at slightly different rates, and the drift varies with temperature, voltage, and age. A typical quartz clock drifts by 10-100 parts per million, meaning two machines that start perfectly synchronized can diverge by tens of milliseconds within minutes and by seconds within a day. Without correction, physical clocks across a cluster become progressively less useful for determining which event happened first.

**Network Time Protocol (NTP)** addresses this by periodically querying a reference time server. The client sends a request, records the send time, receives the server's timestamp, and records the receive time. From the round-trip time (RTT), NTP estimates the one-way network delay as RTT/2 and adjusts the local clock accordingly. To improve accuracy, NTP queries multiple servers organized in a hierarchy of **strata**: stratum-0 devices are atomic clocks or GPS receivers, stratum-1 servers connect directly to them, stratum-2 servers synchronize to stratum-1, and so on. By combining estimates from multiple sources and discarding outliers, NTP typically achieves synchronization within a few milliseconds on a local network and within tens of milliseconds over the internet.

The critical insight is that clock synchronization provides **bounded uncertainty**, not perfect agreement. When machine A's clock reads 10:00:00.000 and machine B's clock reads 10:00:00.003, the true time difference could be anywhere within the synchronization bound — say ±5ms. This means you cannot reliably determine the order of two events that occurred within that uncertainty window on different machines. If event X happens at A's time 10:00:00.010 and event Y happens at B's time 10:00:00.012, you cannot be sure X happened first — the clocks might be off by more than 2ms. This fundamental limitation is what motivates logical clocks (Lamport timestamps, vector clocks) and hybrid approaches, which track causal ordering without depending on physical time accuracy.
