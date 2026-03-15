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
