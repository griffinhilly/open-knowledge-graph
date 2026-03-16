---
id: tcp-flow-control-and-congestion-control
title: TCP Flow Control and Congestion Control
domain: computer-science
course: computer-networking
prerequisites:
- id: tcp-transmission-control-protocol
  type: hard
- id: tcp-connection-establishment
  type: hard
- id: optimization-multivariable-basics
  type: soft
builds-toward:
- qos-quality-of-service
tags:
- flow-control
- congestion-control
- window
- cwnd
- rtt
stage: advanced
status: draft
---

# TCP Flow Control and Congestion Control

## Core Idea
TCP's flow control (via a receive window) prevents the sender from overwhelming the receiver; congestion control (via a congestion window) prevents the sender from overwhelming the network. Algorithms like Reno, Cubic, and BBR adjust the congestion window based on packet loss and RTT to optimize throughput while minimizing queueing delay.

## How It's Best Learned
Use network simulation tools to observe congestion window growth and shrinkage under packet loss; test different algorithms to see their behavior.

## Common Misconceptions
- Flow control and congestion control are the same thing; flow control protects the receiver, congestion control protects the network.
- All TCP implementations use the same congestion control algorithm; modern systems use different algorithms (BBR, Cubic, Reno, etc.).

## Explainer

From your understanding of TCP and connection establishment, you know that TCP provides reliable, ordered delivery by using sequence numbers, acknowledgments, and retransmissions. But reliability alone is not enough — a sender that blasts data as fast as possible can overwhelm either the receiver or the network itself. TCP solves these two distinct problems with two separate mechanisms: **flow control** protects the receiver, and **congestion control** protects the network.

**Flow control** is the simpler of the two. The receiver advertises a **receive window (rwnd)** — the amount of buffer space it currently has available — in every ACK it sends back. The sender must never have more unacknowledged data in flight than the receiver's window allows. If the receiver is slow (perhaps its application is busy processing previous data), its buffer fills up, rwnd shrinks toward zero, and the sender pauses. When the receiver catches up and frees buffer space, rwnd grows again and the sender resumes. This is a direct, end-to-end feedback mechanism: the receiver explicitly tells the sender how much it can handle.

**Congestion control** is harder because the network cannot directly tell the sender how much capacity is available — the sender must infer it. TCP maintains a **congestion window (cwnd)** that limits how much data can be in flight, independent of the receive window. The effective sending rate is governed by the minimum of rwnd and cwnd. The classic algorithm has distinct phases. **Slow start** begins with a small cwnd (typically one or two segments) and doubles it every round-trip time — exponential growth that quickly probes available bandwidth. When cwnd reaches a threshold (ssthresh) or a packet loss is detected, the algorithm switches to **congestion avoidance**, where cwnd grows by roughly one segment per RTT — linear growth that cautiously probes for more capacity. When loss occurs, the sender interprets it as a signal of congestion and cuts cwnd dramatically (halving it in Reno, or resetting to one segment after a timeout).

Different congestion control algorithms refine this basic approach. **TCP Reno** halves cwnd on triple duplicate ACKs (fast recovery) but resets to slow start on timeouts. **TCP Cubic**, the default on Linux, uses a cubic function to grow cwnd more aggressively after a loss recovery, reaching the previous cwnd faster and then probing cautiously beyond it. **BBR (Bottleneck Bandwidth and Round-trip propagation time)**, developed by Google, takes a fundamentally different approach: instead of reacting to loss, it actively estimates the bottleneck bandwidth and minimum RTT, then paces packets to match the estimated capacity. BBR performs significantly better on networks with large buffers where loss-based algorithms would fill queues before detecting congestion. The choice of algorithm profoundly affects throughput, latency, and fairness — and modern operating systems let you select or even swap algorithms per connection.
