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
status: validated
---

# UDP: User Datagram Protocol

## Core Idea
UDP is a connectionless, unreliable transport layer protocol that offers minimal overhead compared to TCP. It provides port-based demultiplexing but no guarantees of delivery, ordering, or flow control, making it suitable for latency-sensitive applications like DNS, video streaming, and online gaming.

## How It's Best Learned
Write simple UDP echo client and server using socket APIs; observe that UDP provides no retransmission or ordering guarantees.

## Common Misconceptions
- UDP is always faster than TCP; UDP has lower overhead but TCP can achieve higher throughput via congestion control.
- UDP is unreliable; applications can add reliability on top (e.g., QUIC wraps UDP with reliability).

## Questions

```yaml
- question: "A live video conferencing application uses UDP. A packet containing several video frames is lost in transit. What happens next?"
  type: multiple-choice
  options:
    - "The application skips those frames — a brief visual glitch is far less disruptive than pausing the stream to wait for retransmission"
    - "UDP automatically retransmits the lost packet after detecting the loss via its checksum"
    - "The video call halts until the lost packet arrives, ensuring smooth chronological playback"
    - "The connection resets and a new UDP session is negotiated from the beginning"
  answer: 0
  explanation: "UDP provides no retransmission, acknowledgment, or error recovery — lost packets are simply gone. This is intentional for live video: a retransmitted frame arriving 200–500 ms late is useless or actively disruptive (out-of-order playback). The application skips missing frames, producing a brief glitch, which is far preferable to the latency of TCP retransmission. Options B and D describe TCP-like behaviors that UDP deliberately omits by design."

- question: "A developer argues that UDP should only be used for applications that can tolerate unreliable delivery. Which statement best challenges this claim?"
  type: multiple-choice
  options:
    - "Applications like QUIC build full reliability on top of UDP, demonstrating that UDP is a minimal foundation on which any transport behavior — including reliable delivery — can be constructed"
    - "UDP is inherently unreliable and cannot be made reliable regardless of the application layer"
    - "TCP is always faster than UDP for applications that need reliable delivery"
    - "Modern networks rarely drop packets, so UDP's unreliability is not a meaningful concern in practice"
  answer: 0
  explanation: "QUIC (used in HTTP/3) directly refutes the claim. QUIC implements reliable, ordered, multiplexed streams on top of UDP, achieving TCP-level reliability while avoiding head-of-line blocking and ossified middlebox behavior. The insight is that UDP is not 'unreliable transport' — it is minimal transport. Reliability, ordering, congestion control — any transport behavior — can be implemented in application space on top of UDP. Choosing UDP means choosing to control those mechanisms yourself, not accepting their absence."

- question: "A UDP datagram header includes sequence numbers so that receivers can detect out-of-order delivery and reassemble packets in the correct order."
  type: true-false
  answer: false
  explanation: "UDP's header is intentionally minimal: source port, destination port, length, and checksum — just 8 bytes total. There are no sequence numbers, acknowledgment numbers, flags, or flow control fields. This is not an oversight; it is the point. Sequence numbers and ordering are TCP features that add overhead and latency. If a UDP application needs ordering, it must implement that logic at the application layer. The stripped-down header is why UDP adds almost no latency beyond network transit time itself."

- question: "UDP is always faster than TCP for any given application because it has lower protocol overhead."
  type: true-false
  answer: false
  explanation: "UDP has lower per-packet overhead and no connection setup latency, but 'always faster' is incorrect. TCP's congestion control can achieve higher sustained throughput than uncontrolled UDP on congested networks, because UDP floods the network without backing off while TCP adapts to available capacity. UDP's advantages are lower latency for small exchanges and no head-of-line blocking — not universally higher throughput. The right choice depends entirely on the application's requirements."

- question: "Why is UDP particularly well-suited for DNS queries, and what does the DNS application layer do to compensate for UDP's lack of reliability guarantees?"
  type: short-answer
  answer: "DNS queries are single request-response exchanges. Using TCP would require a three-way handshake before any query, adding a full round-trip of latency to every DNS lookup — unacceptable for infrastructure that precedes nearly every network connection. UDP allows the client to send a query directly and receive a response in one round-trip. To compensate for potential packet loss, the DNS resolver implements a simple application-layer retry: if no response arrives within a timeout window, it retransmits the query. This is sufficient because DNS queries are idempotent (safe to repeat) and typically succeed on the first attempt."
  explanation: "DNS illustrates the general pattern for query-response protocols over UDP: the application implements lightweight timeout-and-retry logic, which is cheaper than TCP's full reliability machinery for short, stateless exchanges. The same pattern applies to NTP (network time synchronization), SNMP, and other protocols where queries are small, responses are expected quickly, and retrying is harmless. UDP's 8-byte header means almost no overhead per query — for a service handling billions of queries daily, this matters significantly."
```

## Explainer

From the TCP/IP model, you know that the transport layer sits between the application and the network layer, providing process-to-process communication using port numbers. TCP is the transport protocol most people learn first — it provides reliable, ordered delivery through connection setup, acknowledgments, retransmissions, and flow control. UDP is the other major transport protocol, and understanding it starts with understanding what happens when you strip all of that machinery away.

A **UDP datagram** has an 8-byte header containing just four fields: source port, destination port, length, and checksum. That is the entire protocol. There is no connection setup (no three-way handshake), no sequence numbers, no acknowledgments, no retransmission, no flow control, and no congestion control. The application hands a chunk of data to UDP, UDP slaps on the header, and the network layer sends it. If the packet gets lost, duplicated, or arrives out of order, UDP does not notice and does not care. The application must handle these problems if they matter.

Why would anyone choose this over TCP? Because TCP's reliability machinery has a cost: **latency**. The three-way handshake adds a full round-trip before any data flows. Retransmission means a single lost packet can stall the entire stream (head-of-line blocking). Congestion control can throttle throughput below what the network can handle. For applications where speed matters more than perfection, these costs are unacceptable. Consider a live video call: if a video frame arrives 200 milliseconds late because TCP retransmitted it, the moment has passed — showing a stale frame is worse than dropping it. DNS queries are another example: a single request-response exchange would require two round-trips with TCP (handshake plus query) but only one with UDP.

This tradeoff explains why UDP dominates in **real-time and query-response applications**: DNS, VoIP, video streaming, online gaming, and network time synchronization (NTP). In each case, the application either tolerates loss (video skips a frame), handles reliability itself (DNS retries after a timeout), or both. The modern protocol **QUIC** — which powers HTTP/3 — takes this further by building a full reliable transport protocol on top of UDP, gaining the reliability of TCP while avoiding its head-of-line blocking and ossified middlebox behavior. QUIC demonstrates that UDP is not just for "unreliable" applications; it is a minimal foundation on which any transport behavior can be constructed in application space.
