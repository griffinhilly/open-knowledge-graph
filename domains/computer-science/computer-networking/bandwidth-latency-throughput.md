---
id: bandwidth-latency-throughput
title: Bandwidth, Latency, and Throughput
domain: computer-science
course: computer-networking
prerequisites: []
builds-toward:
- ethernet-protocol
- tcp-flow-control-and-congestion-control
- qos-quality-of-service
tags:
- performance
- metrics
- link-quality
- transmission
stage: advanced
status: draft
---

# Bandwidth, Latency, and Throughput

## Core Idea
Bandwidth is the maximum data rate a link can support (measured in bits/second); latency is the time it takes for a packet to travel from source to destination; throughput is the actual data rate achieved in practice, limited by both bandwidth and latency as well as protocol overhead and congestion. Understanding these distinct metrics is essential for network design and performance optimization.

## How It's Best Learned
Use network simulation tools (e.g., ns-3, mininet) to observe how latency and bandwidth constraints affect throughput under various traffic conditions.

## Common Misconceptions
- Higher bandwidth automatically means faster networks; latency is equally important and can be the bottleneck.
- Throughput equals bandwidth; in reality throughput is always less due to overhead and contention.
- Latency is only transmission delay; it includes propagation, processing, and queuing delays.

## Explainer

Three metrics define how well a network performs, and confusing them is one of the most common mistakes in networking. Think of a highway as an analogy. **Bandwidth** is the number of lanes — it determines how many cars can pass a point per hour at maximum capacity. **Latency** is how long it takes a single car to drive from one city to another. **Throughput** is how many cars actually arrive per hour in practice, accounting for traffic jams, accidents, and speed limits. A 10-lane highway (high bandwidth) between distant cities (high latency) is very different from a 2-lane highway (low bandwidth) between nearby towns (low latency), and both can have throughput problems for completely different reasons.

**Bandwidth** (also called link capacity) is measured in bits per second (bps) — megabits, gigabits, etc. It describes the theoretical maximum rate at which data can be pushed onto a link. A 1 Gbps Ethernet connection can, at best, place one billion bits onto the wire each second. But bandwidth alone tells you nothing about when those bits arrive at the other end.

**Latency** measures the total delay a packet experiences traveling from source to destination. It has four components: **propagation delay** (time for a signal to travel the physical medium, limited by the speed of light), **transmission delay** (time to push all the packet's bits onto the wire, which depends on bandwidth), **processing delay** (time for routers to examine headers and make forwarding decisions), and **queuing delay** (time a packet waits in a router's buffer behind other packets). For a short local network, latency might be under 1 millisecond. For a transatlantic link, propagation delay alone is around 30-40 ms. Queuing delay is the most variable component and the one that spikes during congestion.

**Throughput** is the metric that actually matters to users — it is the rate at which useful data is successfully delivered. Throughput is always less than or equal to bandwidth because of protocol overhead (headers, acknowledgments, retransmissions), congestion (competing traffic), and the latency-bandwidth interaction. A particularly important concept is the **bandwidth-delay product**: the amount of data "in flight" on the link at any moment, equal to bandwidth multiplied by round-trip latency. If a protocol like TCP waits for acknowledgments before sending more data, it can only keep bandwidth × RTT bits in transit at once. On a high-bandwidth, high-latency link (like a satellite connection with 1 Gbps bandwidth and 600 ms RTT), the pipe can hold 75 megabytes of data in flight — if the protocol's window is smaller than this, throughput will be far below bandwidth regardless of the link's raw capacity.
