---
id: udp-user-datagram-protocol
title: 'UDP: User Datagram Protocol'
domain: computer-science
course: computer-networking
prerequisites:
- id: tcp-ip-model
  type: hard
builds-toward:
- dns-domain-name-system
- port-addressing-sockets
tags:
- udp
- connectionless
- transport-layer
- unreliable
- low-overhead
stage: advanced
status: draft
---

# UDP: User Datagram Protocol

## Core Idea
UDP is a connectionless, unreliable transport layer protocol that offers minimal overhead compared to TCP. It provides port-based demultiplexing but no guarantees of delivery, ordering, or flow control, making it suitable for latency-sensitive applications like DNS, video streaming, and online gaming.

## How It's Best Learned
Write simple UDP echo client and server using socket APIs; observe that UDP provides no retransmission or ordering guarantees.

## Common Misconceptions
- UDP is always faster than TCP; UDP has lower overhead but TCP can achieve higher throughput via congestion control.
- UDP is unreliable; applications can add reliability on top (e.g., QUIC wraps UDP with reliability).

## Explainer

From the TCP/IP model, you know that the transport layer sits between the application and the network layer, providing process-to-process communication using port numbers. TCP is the transport protocol most people learn first — it provides reliable, ordered delivery through connection setup, acknowledgments, retransmissions, and flow control. UDP is the other major transport protocol, and understanding it starts with understanding what happens when you strip all of that machinery away.

A **UDP datagram** has an 8-byte header containing just four fields: source port, destination port, length, and checksum. That is the entire protocol. There is no connection setup (no three-way handshake), no sequence numbers, no acknowledgments, no retransmission, no flow control, and no congestion control. The application hands a chunk of data to UDP, UDP slaps on the header, and the network layer sends it. If the packet gets lost, duplicated, or arrives out of order, UDP does not notice and does not care. The application must handle these problems if they matter.

Why would anyone choose this over TCP? Because TCP's reliability machinery has a cost: **latency**. The three-way handshake adds a full round-trip before any data flows. Retransmission means a single lost packet can stall the entire stream (head-of-line blocking). Congestion control can throttle throughput below what the network can handle. For applications where speed matters more than perfection, these costs are unacceptable. Consider a live video call: if a video frame arrives 200 milliseconds late because TCP retransmitted it, the moment has passed — showing a stale frame is worse than dropping it. DNS queries are another example: a single request-response exchange would require two round-trips with TCP (handshake plus query) but only one with UDP.

This tradeoff explains why UDP dominates in **real-time and query-response applications**: DNS, VoIP, video streaming, online gaming, and network time synchronization (NTP). In each case, the application either tolerates loss (video skips a frame), handles reliability itself (DNS retries after a timeout), or both. The modern protocol **QUIC** — which powers HTTP/3 — takes this further by building a full reliable transport protocol on top of UDP, gaining the reliability of TCP while avoiding its head-of-line blocking and ossified middlebox behavior. QUIC demonstrates that UDP is not just for "unreliable" applications; it is a minimal foundation on which any transport behavior can be constructed in application space.
