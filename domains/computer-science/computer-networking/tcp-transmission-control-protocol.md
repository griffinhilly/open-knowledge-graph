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
status: draft
---

# TCP: Transmission Control Protocol

## Core Idea
TCP is a connection-oriented, reliable transport protocol that guarantees in-order delivery of bytes and uses sequence numbers, acknowledgments, and retransmission to handle packet loss. TCP's three-way handshake establishes connections, and its flow control and congestion control mechanisms prevent network overload.

## How It's Best Learned
Capture TCP handshakes and data transmission using Wireshark; observe sequence numbers, acknowledgments, and retransmissions.

## Common Misconceptions
- TCP guarantees every packet arrives; TCP guarantees the byte stream is delivered in order, not that every packet survives.
- TCP is slower than UDP; TCP's congestion control often achieves higher overall throughput in congested networks.
