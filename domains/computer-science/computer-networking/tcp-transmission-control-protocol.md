---
id: tcp-transmission-control-protocol
title: 'TCP: Transmission Control Protocol'
domain: computer-science
course: computer-networking
prerequisites:
- id: tcp-ip-model
  type: hard
builds-toward:
- tcp-connection-establishment
- tcp-flow-control-and-congestion-control
tags:
- tcp
- connection-oriented
- reliable
- transport-layer
- ordered-delivery
stage: advanced
status: validated
---

# TCP: Transmission Control Protocol

## Core Idea
TCP is a connection-oriented, reliable transport protocol that guarantees in-order delivery of bytes and uses sequence numbers, acknowledgments, and retransmission to handle packet loss. TCP's three-way handshake establishes connections, and its flow control and congestion control mechanisms prevent network overload.

## How It's Best Learned
Capture TCP handshakes and data transmission using Wireshark; observe sequence numbers, acknowledgments, and retransmissions.

## Common Misconceptions
- TCP guarantees every packet arrives; TCP guarantees the byte stream is delivered in order, not that every packet survives.
- TCP is slower than UDP; TCP's congestion control often achieves higher overall throughput in congested networks.

## Questions

```yaml
- question: "What does TCP guarantee that UDP does not?"
  type: multiple-choice
  options: ["Every individual IP packet arrives intact", "The byte stream is delivered completely and in order", "Latency is minimized end-to-end", "Bandwidth is maximized for the sender"]
  answer: 1
  explanation: "TCP guarantees the application receives a complete, ordered byte stream — not that every packet survives. Packets may be dropped and retransmitted transparently. UDP makes no delivery guarantees at all."

- question: "TCP guarantees that nearly every individual IP packet it sends will arrive at the destination."
  type: true-false
  answer: false
  explanation: "TCP guarantees the byte stream is delivered in order and without gaps, not that every underlying packet survives. Lost packets are detected via missing acknowledgments and silently retransmitted — the application never sees the individual packets."

- question: "What is the purpose of sequence numbers in TCP?"
  type: short-answer
  answer: "Sequence numbers label each byte in the stream so the receiver can reassemble out-of-order segments into the correct order and identify which data is missing, allowing the sender to retransmit only what was lost."
  explanation: "Without sequence numbers, out-of-order delivery would corrupt the data stream and there would be no way to detect gaps. Sequence numbers are also used by the receiver's acknowledgment to tell the sender exactly how far delivery has progressed."
```

## Explainer

The fundamental problem TCP solves is that the internet is unreliable: IP packets can be dropped by congested routers, duplicated, or arrive out of order. Applications like web browsers and file transfers need a reliable, ordered byte stream. TCP sits at the transport layer and hides all of this unreliability from the application, making the network behave as if it were a perfect pipe.

TCP achieves reliability through three coordinated mechanisms. First, every byte sent is assigned a **sequence number**, so the receiver knows the correct order and can detect gaps. Second, the receiver sends back **acknowledgments** (ACKs) confirming how many bytes have been received in order. Third, if the sender does not receive an ACK within a timeout window, it **retransmits** the missing segment. Together, these ensure every byte eventually arrives in the right position.

Before any data flows, TCP performs a **three-way handshake**: the client sends a SYN, the server replies with SYN-ACK, and the client confirms with ACK. This exchange synchronizes sequence numbers on both sides and establishes the connection. The handshake is why TCP is described as "connection-oriented" — there is a setup phase before data transfer, unlike UDP which fires packets immediately.

TCP also includes **flow control** (the receiver advertises how much buffer space it has, preventing the sender from overwhelming it) and **congestion control** (the sender probes network capacity and backs off when it detects congestion). These mechanisms mean that in a congested network, many TCP senders cooperate to share bandwidth efficiently — which is why TCP often achieves better throughput than UDP in practice, despite UDP's reputation for speed.

The key mental model: TCP presents a simple abstraction (a reliable ordered stream) on top of a complex, lossy reality (IP packets). The application writes bytes; TCP figures out how to deliver them. What TCP does *not* do is guarantee low latency or minimum delay — those are different goals that sometimes require UDP and application-level logic instead.

