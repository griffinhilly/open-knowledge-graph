---
id: tcp-flow-control-windows
title: TCP Flow Control and Sliding Windows
domain: computer-science
course: computer-networking
prerequisites:
- id: tcp-transmission-control-protocol
  type: hard
- id: tcp-flow-control-and-congestion-control
  type: hard
builds-toward:
- tcp-connection-termination-fin-rst
- qos-quality-of-service
tags:
- transport-layer
- tcp
- flow-control
- window-management
stage: advanced
status: draft
---

# TCP Flow Control and Sliding Windows

## Core Idea
TCP's sliding window mechanism allows the receiver to advertise how much data it can accept, preventing buffer overflow. The sender cannot transmit beyond the receiver's advertised window size, which changes dynamically as the receiver processes data. Window sizing balances throughput against receiver buffer constraints, with larger windows enabling higher throughput over high-latency links.

## How It's Best Learned
Use tcpdump to monitor TCP window size changes during file transfers. Simulate receiver buffer constraints and observe window shrinking. Experiment with the SO_RCVBUF socket option to change buffer size and observe window scaling.

## Common Misconceptions
The window size is not fixed; it changes per ACK. Window scaling (RFC 1323) extends the window field for large-bandwidth-delay products. A zero window does not mean connection failure; it means the receiver is not ready to receive.

## Explainer

From your study of TCP, you know it provides reliable, ordered byte-stream delivery. But reliability alone does not prevent a fast sender from overwhelming a slow receiver — if the sender blasts data faster than the receiver can process it, the receiver's buffer fills up and incoming segments get dropped. **Flow control** is TCP's mechanism for preventing this, and the **sliding window** is how it works in practice.

Every TCP segment the receiver sends back includes a field called the **receive window (rwnd)** — a 16-bit value announcing how many bytes of buffer space the receiver currently has available. The sender treats this as a hard cap: it will never have more than rwnd bytes of unacknowledged data in flight. As the receiver processes data and frees buffer space, it advertises a larger window in subsequent ACKs. As its buffer fills up, it shrinks the window. This creates a dynamic, self-regulating feedback loop — the sender continuously adjusts its transmission rate based on the receiver's latest advertisement.

Visualize it concretely. Suppose the receiver advertises a window of 4,000 bytes. The sender can transmit segments totaling 4,000 bytes and then must stop and wait. When the receiver processes 1,000 bytes and sends an ACK, that ACK advertises a new window (say 1,000 bytes of free space), which lets the sender transmit 1,000 more bytes. The "window" slides forward along the byte stream as data is acknowledged. If the receiver is temporarily swamped — perhaps the application reading from the socket is busy — it can advertise a **zero window**, telling the sender to stop completely. The sender then enters a **persist** state, periodically sending tiny probe segments to check whether the window has reopened, ensuring the connection does not deadlock.

The original TCP header allocates 16 bits for the window field, limiting it to 65,535 bytes. This was fine for early networks, but modern high-bandwidth, high-latency links (think intercontinental fiber) need much larger windows to keep the pipe full. **Window scaling** (RFC 1323) solves this by negotiating a scale factor during the three-way handshake. A scale factor of 7, for example, means the advertised window value is left-shifted by 7 bits, allowing effective windows up to gigabytes. This is essential for achieving full throughput on links where the bandwidth-delay product — the amount of data "in flight" to fill the pipe — exceeds 64 KB. Understanding this distinction between flow control (receiver-driven, preventing buffer overflow) and congestion control (network-driven, preventing router overload) is critical: TCP uses both simultaneously, and the sender transmits at the rate allowed by whichever constraint is tighter.
