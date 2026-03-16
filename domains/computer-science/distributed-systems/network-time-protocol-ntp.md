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

## Explainer

In a distributed system, every machine has its own clock, and those clocks drift apart. A quartz oscillator on one server might gain a few microseconds per second while another loses a few — within hours, two machines can disagree about the current time by tens of milliseconds. This matters because timestamps are used everywhere: log correlation, cache expiration, certificate validation, and ordering events across services. Without synchronized clocks, debugging a distributed failure becomes nearly impossible because you cannot tell which event happened first.

**Network Time Protocol (NTP)** solves this by organizing time sources into a hierarchy called **strata**. Stratum 0 consists of high-precision reference clocks — atomic clocks, GPS receivers — that define "true" time. Stratum 1 servers are directly connected to a stratum 0 source. Stratum 2 servers synchronize from stratum 1, and so on. Each hop adds a small amount of uncertainty, so lower stratum numbers indicate higher accuracy. A typical enterprise server synchronizes at stratum 2 or 3, achieving accuracy within a few milliseconds.

The core of NTP's measurement technique is the **round-trip delay calculation**. A client sends a request timestamped with its local clock, the server stamps arrival and departure times with its clock, and the client records when the response arrives. From these four timestamps, NTP estimates the one-way network delay (half the round trip) and the clock offset (how far the client's clock is from the server's). This is the same basic idea you would use if you mailed a letter with a timestamp and the recipient mailed it back — by measuring the total transit time, you can estimate the one-way delay and figure out how far apart your watches are.

NTP does not simply jump the clock to the correct time. Abrupt clock jumps can break applications that assume time moves forward monotonically — imagine a log file where an entry at 10:00:01 is followed by one at 9:59:58. Instead, NTP uses **clock slewing**: it slightly speeds up or slows down the local clock rate until it converges on the correct time. For small offsets, this gradual adjustment is invisible to applications. Only on initial startup or after very large drifts does NTP perform a hard step correction. This design reflects a key lesson from distributed systems modeling: even infrastructure protocols must respect the assumptions that higher-level software makes about the environment.
