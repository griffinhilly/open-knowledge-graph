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

## Explainer

You already know the two workhorses of the transport layer: TCP gives you reliable, ordered byte streams but treats everything as one continuous flow, while UDP gives you fast, independent messages but with no delivery guarantees. **SCTP (Stream Control Transmission Protocol)** was designed to combine the best properties of both — reliable delivery with message boundaries and independent streams — originally for carrying telephone signaling (SS7) over IP networks, but useful wherever those properties matter.

The key innovation is **multi-streaming**. An SCTP connection (called an **association**) can carry multiple independent streams simultaneously. Within each stream, messages are delivered in order and reliably. But crucially, if a packet is lost on stream 3, only stream 3 stalls while waiting for retransmission — streams 1, 2, and 4 continue delivering data without delay. Compare this to TCP, where a single lost packet blocks delivery of everything behind it in the byte stream, even if that later data is logically unrelated. This problem, called **head-of-line blocking**, is TCP's fundamental limitation for multiplexed traffic, and it is exactly what SCTP solves.

SCTP also preserves **message boundaries**, unlike TCP. When you send a 500-byte message over TCP, the receiver might get it as two 250-byte chunks or as part of a larger read — TCP sees only a stream of bytes. SCTP delivers discrete messages intact, the way UDP does, but with TCP-like reliability. Each message arrives whole, in order within its stream, and the sender knows via acknowledgments that it was received. SCTP uses **Selective Acknowledgments (SACK)** to efficiently report which chunks have arrived, allowing the sender to retransmit only what is missing rather than resending everything from the gap forward.

Another distinctive feature is **multi-homing**: an SCTP association can bind to multiple IP addresses on each endpoint. If the primary network path fails, SCTP automatically switches to an alternate address — a built-in failover mechanism that TCP achieves only with external tooling. The protocol monitors path health through periodic **heartbeat** messages to alternate addresses. This makes SCTP particularly valuable in telecommunications and other environments where link redundancy is critical. While SCTP has not displaced TCP and UDP for general internet use — largely due to middlebox compatibility issues and lack of widespread OS support — it remains the protocol of choice for signaling in 4G/5G networks (via the Diameter and S1AP protocols) and anywhere that multi-streaming or multi-homing provides a clear architectural advantage.
