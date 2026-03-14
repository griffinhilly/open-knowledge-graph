---
id: network-time-protocol-ntp
title: Network Time Protocol (NTP) for Clock Synchronization
domain: computer-science
course: distributed-systems
prerequisites:
- id: distributed-system-models
  type: hard
tags:
- time
- synchronization
- protocol
stage: advanced
status: draft
---

# Network Time Protocol (NTP) for Clock Synchronization

## Core Idea
NTP is a protocol for synchronizing clocks across a network to within milliseconds. It uses a hierarchical stratum of time sources, starting with atomic clocks. By measuring round-trip latencies and correcting for clock drift and network delays, NTP enables distributed systems to maintain coordinated time. Clock synchronization is essential for ordering events and debugging.
