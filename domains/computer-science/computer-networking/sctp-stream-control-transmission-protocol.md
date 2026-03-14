---
id: sctp-stream-control-transmission-protocol
title: 'SCTP: Stream Control Transmission Protocol'
domain: computer-science
course: computer-networking
prerequisites:
- id: tcp-transmission-control-protocol
  type: hard
- id: udp-user-datagram-protocol
  type: hard
- id: port-addressing-sockets
  type: soft
builds-toward:
- qos-quality-of-service
- network-standards-and-ietf
tags:
- transport-layer
- protocols
- reliable-delivery
- streaming
stage: advanced
status: draft
---

# SCTP: Stream Control Transmission Protocol

## Core Idea
SCTP combines reliability of TCP with message boundaries and multi-streaming of UDP, designed for signaling in telecommunications. It supports multiple independent streams within a single association, allowing one stream's packet loss not to block others. SCTP includes explicit congestion control, ordered/unordered delivery options per stream, and heartbeat mechanisms.

## How It's Best Learned
Compile and test SCTP using lksctp-tools on Linux. Observe SCTP associations using netstat -S and packet captures. Implement multi-stream client-server applications to understand independent stream sequencing.

## Common Misconceptions
SCTP is not a replacement for TCP/UDP but complements them for specific use cases. Message boundaries are preserved but sequencing is per-stream, not per-association. SCTP congestion control uses SACK (Selective Acknowledgment) differently than TCP does.
