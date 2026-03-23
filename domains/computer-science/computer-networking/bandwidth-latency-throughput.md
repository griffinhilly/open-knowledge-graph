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
status: validated
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

## Questions

```yaml
- question: "A satellite internet link has 1 Gbps bandwidth and a 600 ms round-trip latency. A TCP connection uses a 64 KB receive window. Approximately what is the maximum achievable throughput?"
  type: multiple-choice
  options:
    - "1 Gbps — the full bandwidth of the link"
    - "About 853 Kbps — because the window size divided by RTT caps how much data can be in flight"
    - "500 Mbps — latency cuts effective bandwidth in half"
    - "Determined by propagation delay alone, not bandwidth"
  answer: 1
  explanation: "TCP can only have window-size bytes in flight at once before waiting for acknowledgments. Max throughput = window / RTT = (64 × 1024 × 8 bits) / 0.6 s ≈ 873,000 bps ≈ 853 Kbps — less than 0.1% of the 1 Gbps bandwidth. This is the bandwidth-delay product problem: high bandwidth × high latency means a huge pipe that a small TCP window cannot fill. Upgrading bandwidth without fixing the window size yields no improvement."

- question: "A network engineer observes that ping times between two servers increase dramatically during business hours but the link's speed rating (bandwidth) is unchanged. Which component of latency is most likely responsible?"
  type: multiple-choice
  options:
    - "Propagation delay — more users means signals travel more slowly through the wire"
    - "Transmission delay — higher traffic increases the time to push bits onto the link"
    - "Queuing delay — packets wait longer in router buffers when traffic competes for the link"
    - "Processing delay — routers examine more packet headers when traffic increases"
  answer: 2
  explanation: "Propagation delay is fixed by physical distance and the speed of light — it doesn't change with traffic. Transmission delay is fixed by bandwidth and packet size. Queuing delay is the most variable component: when many flows compete, buffers fill and packets wait. This is why latency spikes under congestion while bandwidth (link capacity) remains unchanged."

- question: "Throughput and bandwidth refer to the same network property — the rate at which data moves across a link."
  type: true-false
  answer: false
  explanation: "Bandwidth is the theoretical maximum rate of the link (e.g., 1 Gbps). Throughput is the actual rate of useful data delivered in practice, which is always less than bandwidth due to protocol overhead (headers, ACKs), retransmissions, congestion, and the window-size/RTT interaction. A 1 Gbps link might deliver only 50 Mbps of throughput if RTT is high and the TCP window is small."

- question: "Latency is composed of more than just propagation delay — it also includes transmission delay, processing delay, and queuing delay."
  type: true-false
  answer: true
  explanation: "This is a common misconception: students identify latency with propagation delay (the speed-of-light limit). But transmission delay (time to push all bits onto the wire, = packet size / bandwidth) becomes significant for large packets on slow links. Processing delay (router decisions) is small but real. Queuing delay is the most variable and can dominate on congested networks. Optimizing only propagation delay misses the other three."

- question: "Explain what the bandwidth-delay product represents and why it matters for protocol design."
  type: short-answer
  answer: "The bandwidth-delay product (BDP = bandwidth × round-trip time) is the amount of data that can be 'in flight' on a link at any instant — the number of bits the pipe can hold simultaneously. A protocol like TCP that waits for acknowledgments before sending more can only keep BDP bits in transit if its window size equals BDP. If the window is smaller, the sender stalls waiting for ACKs and the link is underutilized. On high-bandwidth, high-latency links (satellite, transcontinental fiber), BDP can be tens of megabytes, requiring large windows to achieve full throughput."
  explanation: "The BDP insight explains why a gigabit link with 100 ms RTT needs a ~12 MB TCP window to be fully utilized (1 Gbps × 0.1 s = 100 Mb = 12.5 MB). Historic TCP defaults of 64 KB were designed for local networks — they leave high-BDP links severely underutilized."
```

## Explainer

Three metrics define how well a network performs, and confusing them is one of the most common mistakes in networking. Think of a highway as an analogy. **Bandwidth** is the number of lanes — it determines how many cars can pass a point per hour at maximum capacity. **Latency** is how long it takes a single car to drive from one city to another. **Throughput** is how many cars actually arrive per hour in practice, accounting for traffic jams, accidents, and speed limits. A 10-lane highway (high bandwidth) between distant cities (high latency) is very different from a 2-lane highway (low bandwidth) between nearby towns (low latency), and both can have throughput problems for completely different reasons.

**Bandwidth** (also called link capacity) is measured in bits per second (bps) — megabits, gigabits, etc. It describes the theoretical maximum rate at which data can be pushed onto a link. A 1 Gbps Ethernet connection can, at best, place one billion bits onto the wire each second. But bandwidth alone tells you nothing about when those bits arrive at the other end.

**Latency** measures the total delay a packet experiences traveling from source to destination. It has four components: **propagation delay** (time for a signal to travel the physical medium, limited by the speed of light), **transmission delay** (time to push all the packet's bits onto the wire, which depends on bandwidth), **processing delay** (time for routers to examine headers and make forwarding decisions), and **queuing delay** (time a packet waits in a router's buffer behind other packets). For a short local network, latency might be under 1 millisecond. For a transatlantic link, propagation delay alone is around 30-40 ms. Queuing delay is the most variable component and the one that spikes during congestion.

**Throughput** is the metric that actually matters to users — it is the rate at which useful data is successfully delivered. Throughput is always less than or equal to bandwidth because of protocol overhead (headers, acknowledgments, retransmissions), congestion (competing traffic), and the latency-bandwidth interaction. A particularly important concept is the **bandwidth-delay product**: the amount of data "in flight" on the link at any moment, equal to bandwidth multiplied by round-trip latency. If a protocol like TCP waits for acknowledgments before sending more data, it can only keep bandwidth × RTT bits in transit at once. On a high-bandwidth, high-latency link (like a satellite connection with 1 Gbps bandwidth and 600 ms RTT), the pipe can hold 75 megabytes of data in flight — if the protocol's window is smaller than this, throughput will be far below bandwidth regardless of the link's raw capacity.
