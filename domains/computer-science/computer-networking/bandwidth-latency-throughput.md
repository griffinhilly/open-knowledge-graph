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
