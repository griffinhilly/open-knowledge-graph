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
- id: bandwidth-latency-throughput
  type: hard
- id: sliding-window-protocol
  type: hard
builds-toward:
- qos-quality-of-service
tags:
- flow-control
- congestion-control
- window
- cwnd
- rtt
stage: advanced
status: validated
---

# TCP Flow Control and Congestion Control

## Core Idea
TCP's flow control (via a receive window) prevents the sender from overwhelming the receiver; congestion control (via a congestion window) prevents the sender from overwhelming the network. Algorithms like Reno, Cubic, and BBR adjust the congestion window based on packet loss and RTT to optimize throughput while minimizing queueing delay.

## How It's Best Learned
Use network simulation tools to observe congestion window growth and shrinkage under packet loss; test different algorithms to see their behavior.

## Common Misconceptions
- Flow control and congestion control are the same thing; flow control protects the receiver, congestion control protects the network.
- All TCP implementations use the same congestion control algorithm; modern systems use different algorithms (BBR, Cubic, Reno, etc.).

## Questions

```yaml
- question: "A server is sending data to a fast client over a congested network link. The client's receive buffer is nearly empty and rwnd is large, but packets are being dropped at an intermediate router. Which mechanism is currently limiting the transmission rate?"
  type: multiple-choice
  options:
    - "Flow control — the receive window is the bottleneck because the client is processing data slowly"
    - "Congestion control — the congestion window is limiting transmission because loss signals network congestion"
    - "Both equally — TCP always takes the maximum of rwnd and cwnd to set the sending rate"
    - "Neither — TCP retransmits dropped packets automatically without adjusting the sending rate"
  answer: 1
  explanation: "The effective sending rate is the *minimum* of rwnd and cwnd. Here, rwnd is large (fast client with empty buffer) but packets are dropping at the network — a congestion signal. TCP interprets loss as congestion and shrinks cwnd accordingly. Flow control is not the constraint because the receiver's buffer is healthy; the network is the bottleneck. Option C gets the formula backwards — TCP uses the minimum, not maximum. Option D is wrong: TCP does retransmit but *also* reduces cwnd to relieve congestion, which is precisely the point of congestion control."

- question: "Why does TCP Slow Start use exponential rather than linear window growth at the beginning of a connection?"
  type: multiple-choice
  options:
    - "Exponential growth wastes less time reaching the available bandwidth without staying cautiously slow for too long"
    - "Linear growth would immediately cause congestion by exceeding network capacity"
    - "The TCP specification requires exponential growth for historical backward-compatibility reasons"
    - "Exponential growth allows the sender to detect packet loss faster than linear growth"
  answer: 0
  explanation: "Slow Start is called 'slow' because it begins with a small cwnd (1–2 segments) rather than immediately sending at maximum. But exponential doubling quickly probes available bandwidth — within a few RTTs, cwnd reaches the available capacity. Linear growth from a small initial value would take far longer to reach a useful sending rate, wasting time. The name is somewhat misleading: Slow Start starts slowly but scales up fast. Once cwnd reaches ssthresh (the estimated capacity threshold), the algorithm switches to linear congestion avoidance to probe more cautiously."

- question: "Flow control and congestion control are redundant mechanisms — either one alone is sufficient to prevent packet loss in any real network scenario."
  type: true-false
  answer: false
  explanation: "They solve fundamentally different problems and protect different resources. Flow control protects the *receiver's buffer* using the explicitly advertised rwnd — it prevents the sender from overwhelming a slow receiver. Congestion control protects the *network* using the inferred cwnd — it prevents the sender from overwhelming intermediate routers. A fast receiver with a large buffer provides no flow control constraint, yet the network can still congest. Conversely, a slow receiver constrained by rwnd still needs congestion control on the sender's side to avoid filling router queues. Each mechanism can be the binding constraint independently."

- question: "The effective TCP sending rate is governed by the minimum of the receive window (rwnd) and the congestion window (cwnd)."
  type: true-false
  answer: true
  explanation: "This is the fundamental rule that unifies flow control and congestion control. The amount of data TCP can have unacknowledged in flight cannot exceed either limit. If rwnd = 64KB and cwnd = 32KB, the network is the bottleneck and the sender is limited to 32KB in flight. If rwnd = 16KB and cwnd = 64KB, the receiver is the bottleneck and the sender is limited to 16KB in flight. Both windows are enforced simultaneously, and whichever is smaller determines the actual sending rate. This is why both mechanisms can independently limit throughput."

- question: "Why does TCP interpret packet loss as a signal of network congestion, and why might this assumption break down in modern networks?"
  type: short-answer
  answer: "TCP was designed when networks were simple and nearly all packet loss was caused by router buffer overflow — a direct indicator of congestion. Loss-based algorithms like Reno and Cubic treat any loss event as a congestion signal and reduce cwnd. This assumption breaks down in wireless networks, where packet loss often occurs due to noise, interference, or fading rather than congestion. If TCP misinterprets wireless loss as congestion, it unnecessarily reduces its sending rate even though the network has available capacity. BBR addresses this by estimating bottleneck bandwidth and minimum RTT directly rather than inferring congestion from loss."
  explanation: "The core issue is that loss is an imperfect proxy for congestion — it was a good proxy on wired 1980s networks but not on modern heterogeneous networks. A deeper problem is that loss-based algorithms fill router queues before detecting congestion, causing high latency before any loss occurs (bufferbloat). BBR's approach of directly estimating capacity represents a more fundamental departure: instead of asking 'did anything go wrong?', it asks 'how much capacity actually exists?'"
```

## Explainer

From your understanding of TCP and connection establishment, you know that TCP provides reliable, ordered delivery by using sequence numbers, acknowledgments, and retransmissions. But reliability alone is not enough — a sender that blasts data as fast as possible can overwhelm either the receiver or the network itself. TCP solves these two distinct problems with two separate mechanisms: **flow control** protects the receiver, and **congestion control** protects the network.

**Flow control** is the simpler of the two. The receiver advertises a **receive window (rwnd)** — the amount of buffer space it currently has available — in every ACK it sends back. The sender must never have more unacknowledged data in flight than the receiver's window allows. If the receiver is slow (perhaps its application is busy processing previous data), its buffer fills up, rwnd shrinks toward zero, and the sender pauses. When the receiver catches up and frees buffer space, rwnd grows again and the sender resumes. This is a direct, end-to-end feedback mechanism: the receiver explicitly tells the sender how much it can handle.

**Congestion control** is harder because the network cannot directly tell the sender how much capacity is available — the sender must infer it. TCP maintains a **congestion window (cwnd)** that limits how much data can be in flight, independent of the receive window. The effective sending rate is governed by the minimum of rwnd and cwnd. The classic algorithm has distinct phases. **Slow start** begins with a small cwnd (typically one or two segments) and doubles it every round-trip time — exponential growth that quickly probes available bandwidth. When cwnd reaches a threshold (ssthresh) or a packet loss is detected, the algorithm switches to **congestion avoidance**, where cwnd grows by roughly one segment per RTT — linear growth that cautiously probes for more capacity. When loss occurs, the sender interprets it as a signal of congestion and cuts cwnd dramatically (halving it in Reno, or resetting to one segment after a timeout).

Different congestion control algorithms refine this basic approach. **TCP Reno** halves cwnd on triple duplicate ACKs (fast recovery) but resets to slow start on timeouts. **TCP Cubic**, the default on Linux, uses a cubic function to grow cwnd more aggressively after a loss recovery, reaching the previous cwnd faster and then probing cautiously beyond it. **BBR (Bottleneck Bandwidth and Round-trip propagation time)**, developed by Google, takes a fundamentally different approach: instead of reacting to loss, it actively estimates the bottleneck bandwidth and minimum RTT, then paces packets to match the estimated capacity. BBR performs significantly better on networks with large buffers where loss-based algorithms would fill queues before detecting congestion. The choice of algorithm profoundly affects throughput, latency, and fairness — and modern operating systems let you select or even swap algorithms per connection.
