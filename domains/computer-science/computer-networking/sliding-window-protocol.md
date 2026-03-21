---
id: sliding-window-protocol
title: Sliding Window Protocol
domain: computer-science
course: computer-networking
prerequisites:
- id: automatic-repeat-request
  type: hard
builds-toward:
- tcp-transmission-control-protocol
- tcp-flow-control-and-congestion-control
tags:
- sliding-window
- flow-control
- sequence-numbers
- buffering
stage: advanced
status: draft
---

# Sliding Window Protocol

## Core Idea
A sliding window allows a sender to have multiple packets in flight without waiting for acknowledgments, improving throughput by overlapping transmission and acknowledgment. The window size controls how many unacknowledged packets can exist; it slides forward as acknowledgments arrive. Both TCP and selective repeat ARQ use sliding windows to balance throughput with reliability.

## Questions

```yaml
- question: "A network link has 100 Mbps bandwidth and a 200 ms round-trip time. A stop-and-wait sender achieves roughly 0.05% link utilization. What window size (in 1500-byte packets) is needed to approach full utilization?"
  type: multiple-choice
  options:
    - "Approximately 1,667 packets — matching the bandwidth-delay product so the sender has enough in-flight data to keep the link busy during the full round-trip"
    - "Exactly 2 packets — one being transmitted and one in the acknowledgment pipeline is sufficient for any link speed"
    - "The window size is irrelevant; link utilization depends only on packet size and link bandwidth, not on the number of in-flight packets"
    - "Approximately 10 packets — a standard TCP initial window size that balances throughput and reliability for all link types"
  answer: 0
  explanation: "Bandwidth-delay product = 100 Mbps × 0.200 s = 20 Mbits = 2.5 MB. At 1,500 bytes per packet, that is approximately 1,667 packets. The window must be large enough to fill this 'pipe volume' — to keep new data flowing while waiting for ACKs from packets sent at the start of the round trip. Stop-and-wait is equivalent to window size 1, which fills only one packet's transmission time out of an entire RTT. This calculation reveals why high-bandwidth, high-latency links (satellite, intercontinental fiber) require window sizes in the thousands to achieve near-maximum utilization."

- question: "A sender using Go-Back-N with window size 8 transmits packets 1–8. Packet 4 is lost; packets 5–8 arrive correctly at the receiver. What does the receiver do with packets 5–8?"
  type: multiple-choice
  options:
    - "Discards them — Go-Back-N receivers do not buffer out-of-order packets, so packets 5–8 are dropped and must be retransmitted after packet 4 is recovered"
    - "Buffers packets 5–8 and sends individual SACKs (selective acknowledgments) requesting only packet 4 be retransmitted"
    - "Sends a cumulative ACK through packet 8, trusting the sender to detect the gap via timeout and retransmit only what was lost"
    - "Buffers packets 5–8 silently and delivers them in order once packet 4 is recovered, without sending any ACKs until the gap is filled"
  answer: 0
  explanation: "Go-Back-N receivers only accept packets in order — they maintain no out-of-order buffer. Since packet 4 is missing, packets 5–8 arrive out of sequence and are discarded. The receiver keeps sending duplicate ACK 3 (the last correctly received in-order packet). When the sender detects the loss, it must retransmit packet 4 *and* all subsequent packets (5, 6, 7, 8) even though many were received correctly. This wasteful retransmission is Go-Back-N's main disadvantage compared to Selective Repeat, which only retransmits the specific lost packets and buffers the out-of-order ones."

- question: "The sliding window protocol improves link utilization over stop-and-wait by allowing the sender to transmit new packets while waiting for acknowledgments of earlier ones."
  type: true-false
  answer: true
  explanation: "Stop-and-wait enforces strict alternation: send one packet, idle while waiting for its ACK, then send the next. On any link where round-trip time significantly exceeds transmission time, the sender is idle for most of the time — utilization is approximately (transmission time)/(round-trip time). The sliding window keeps the pipeline filled by permitting multiple unacknowledged packets in flight simultaneously. As long as the window size meets the bandwidth-delay product, the sender always has data to transmit immediately, approaching 100% link utilization."

- question: "In TCP, the receiver's advertised window (rwnd) directly determines the sender's congestion window (cwnd), which limits how fast the sender transmits."
  type: true-false
  answer: false
  explanation: "TCP maintains two independent window mechanisms. The receive window (rwnd) is advertised by the receiver and reflects its available buffer space — this enforces flow control, preventing a fast sender from overwhelming a slow receiver. The congestion window (cwnd) is maintained entirely by the sender based on network feedback (packet loss, delay signals) — this enforces congestion control, preventing the sender from overwhelming intermediate network links. The sender's effective limit is the *minimum* of rwnd and cwnd. Conflating these two windows is a common mistake; they address different bottlenecks and are managed by different algorithms."

- question: "What is the bandwidth-delay product, and why must a sliding window be at least this large to fully utilize a high-latency link?"
  type: short-answer
  answer: "The bandwidth-delay product (BDP) is the product of link bandwidth (bits/second) and round-trip time (seconds), giving the number of bits that can be simultaneously in transit on the link. A window smaller than the BDP means the sender exhausts its permitted in-flight data before the first ACK returns, forcing it to pause. Only when the window ≥ BDP/packet_size can the sender always have new data ready the moment link capacity is available, keeping the pipe continuously full."
  explanation: "Intuitively, the BDP is the 'pipe volume' — how many bits fit inside the network at any given moment. Stop-and-wait has a pipeline capacity of exactly one packet, which is far below the BDP on any high-latency link. A window of W packets allows W × packet_size bits in transit, and when W ≥ BDP/packet_size, the sender never has to stall. This is why satellite links (RTT ~600 ms) and transcontinental fiber links require window sizes in the thousands of packets to reach full utilization — the large RTT demands a proportionally large window to fill the pipe."
```

## Explainer

From your work with automatic repeat request (ARQ) protocols, you know the basic reliability pattern: send a packet, wait for an acknowledgment, then send the next one. This **stop-and-wait** approach is correct but painfully slow, especially on high-latency links. If the round-trip time between sender and receiver is 100 milliseconds and each packet takes 1 millisecond to transmit, the sender spends 99% of its time idle, waiting for ACKs. The sliding window protocol solves this by allowing the sender to transmit multiple packets before any acknowledgment arrives, keeping the link busy.

The core idea is a **window** — a range of sequence numbers that the sender is allowed to have "in flight" (sent but not yet acknowledged) at any given time. If the window size is 4, the sender can transmit packets 1, 2, 3, and 4 without pausing. When the ACK for packet 1 arrives, the window "slides" forward: now packets 2, 3, 4, and 5 are within the window, and packet 5 can be sent. The window always represents the boundary between what has been acknowledged (behind the window), what is in flight (inside the window), and what cannot be sent yet (ahead of the window). The receiver maintains a corresponding window tracking which sequence numbers it is prepared to accept.

The window size directly controls the tradeoff between throughput and resource consumption. A larger window allows more packets in flight, which is necessary to fill high-bandwidth, high-latency links — this product of bandwidth and delay is called the **bandwidth-delay product**, and the window must be at least that large to fully utilize the link. However, a larger window also means more data that might need retransmission if something goes wrong, and more buffer space required at both sender and receiver. Two classic variants handle loss differently within this framework: **Go-Back-N** retransmits the lost packet and everything after it (simpler but wasteful), while **Selective Repeat** retransmits only the specific lost packets (more efficient but requires the receiver to buffer out-of-order arrivals).

TCP uses a sliding window as the foundation for both **flow control** and **congestion control**. The receiver advertises its available buffer space as a receive window, telling the sender "do not send more than this many bytes beyond what I have acknowledged." This prevents a fast sender from overwhelming a slow receiver. The congestion window, managed by the sender, limits the sending rate to avoid overwhelming the network itself. The effective window at any moment is the minimum of these two values. This is why understanding sliding windows is essential before studying TCP's flow and congestion control mechanisms — they are all built on top of this single elegant idea of a movable range of permitted sequence numbers.
