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

## Explainer

From your work with automatic repeat request (ARQ) protocols, you know the basic reliability pattern: send a packet, wait for an acknowledgment, then send the next one. This **stop-and-wait** approach is correct but painfully slow, especially on high-latency links. If the round-trip time between sender and receiver is 100 milliseconds and each packet takes 1 millisecond to transmit, the sender spends 99% of its time idle, waiting for ACKs. The sliding window protocol solves this by allowing the sender to transmit multiple packets before any acknowledgment arrives, keeping the link busy.

The core idea is a **window** — a range of sequence numbers that the sender is allowed to have "in flight" (sent but not yet acknowledged) at any given time. If the window size is 4, the sender can transmit packets 1, 2, 3, and 4 without pausing. When the ACK for packet 1 arrives, the window "slides" forward: now packets 2, 3, 4, and 5 are within the window, and packet 5 can be sent. The window always represents the boundary between what has been acknowledged (behind the window), what is in flight (inside the window), and what cannot be sent yet (ahead of the window). The receiver maintains a corresponding window tracking which sequence numbers it is prepared to accept.

The window size directly controls the tradeoff between throughput and resource consumption. A larger window allows more packets in flight, which is necessary to fill high-bandwidth, high-latency links — this product of bandwidth and delay is called the **bandwidth-delay product**, and the window must be at least that large to fully utilize the link. However, a larger window also means more data that might need retransmission if something goes wrong, and more buffer space required at both sender and receiver. Two classic variants handle loss differently within this framework: **Go-Back-N** retransmits the lost packet and everything after it (simpler but wasteful), while **Selective Repeat** retransmits only the specific lost packets (more efficient but requires the receiver to buffer out-of-order arrivals).

TCP uses a sliding window as the foundation for both **flow control** and **congestion control**. The receiver advertises its available buffer space as a receive window, telling the sender "do not send more than this many bytes beyond what I have acknowledged." This prevents a fast sender from overwhelming a slow receiver. The congestion window, managed by the sender, limits the sending rate to avoid overwhelming the network itself. The effective window at any moment is the minimum of these two values. This is why understanding sliding windows is essential before studying TCP's flow and congestion control mechanisms — they are all built on top of this single elegant idea of a movable range of permitted sequence numbers.
