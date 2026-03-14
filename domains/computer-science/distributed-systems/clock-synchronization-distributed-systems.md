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
stage: concrete-techniques
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
