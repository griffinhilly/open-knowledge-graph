---
id: tcp-connection-termination-fin-rst
title: TCP Connection Termination and FIN/RST Handling
domain: computer-science
course: computer-networking
prerequisites:
- id: tcp-connection-establishment
  type: hard
- id: tcp-transmission-control-protocol
  type: hard
builds-toward:
- tcp-flow-control-and-congestion-control
tags:
- transport-layer
- tcp
- connection-management
- termination
stage: advanced
status: draft
---

# TCP Connection Termination and FIN/RST Handling

## Core Idea
TCP connection termination involves a four-way handshake: one side sends FIN, the other acknowledges and sends its own FIN, and both acknowledge the second FIN. Half-close is possible (one side closes write while reading continues). RST (Reset) abruptly terminates a connection, discarding buffered data. TIME_WAIT state persists for 2*MSL to prevent packet confusion.

## How It's Best Learned
Observe TCP connection termination using tcpdump in normal and abrupt (RST) scenarios. Measure TIME_WAIT duration and observe its impact on socket reuse. Test half-close behavior by closing write and continuing to read. Monitor TCP state transitions using netstat.

## Common Misconceptions
FIN is not the same as RST; FIN allows graceful shutdown while RST is abrupt. TIME_WAIT prevents connection confusion; reducing it can cause issues. A connection in TIME_WAIT state still occupies a socket and can prevent rapid reconnection.
