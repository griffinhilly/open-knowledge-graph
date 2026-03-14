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
