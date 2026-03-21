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

## Questions

```yaml
- question: "A receiver sends a TCP ACK with a window size of 0. What does this signal, and what should the sender do?"
  type: multiple-choice
  options:
    - "The connection has failed; the sender should retransmit all unacknowledged data immediately"
    - "The receiver's buffer is temporarily full; the sender should stop transmitting and send periodic probe segments to detect when the window reopens"
    - "The network is congested; the sender should reduce its congestion window by half"
    - "The receiver is requesting a permanent reduction in data rate using the slow-start algorithm"
  answer: 1
  explanation: "A zero window advertisement means the receiver's buffer is full right now — not that the connection has failed. The sender enters a persist state, sending small probe segments at intervals to check whether the receiver has advertised a nonzero window. This prevents deadlock: without probing, the sender would wait forever for a window update while the receiver waits for a probe. A zero window is a flow control signal from the receiver, entirely separate from congestion control (which responds to network conditions, not receiver buffer state)."

- question: "A client and server exchange data over a transatlantic link with RTT = 150 ms and available bandwidth of 1 Gbps. The TCP receive window is the default 64 KB. Why might observed throughput be only ~3–4 Mbps despite ample bandwidth?"
  type: multiple-choice
  options:
    - "TCP checksums are too slow to verify at 1 Gbps, creating a processing bottleneck"
    - "The 64 KB window limits unacknowledged bytes in flight; with 150 ms RTT, maximum throughput is approximately window/RTT ≈ 3.4 Mbps regardless of available bandwidth"
    - "TCP cannot pipeline packets over high-latency links because flow control disables segment batching"
    - "Zero window advertisements from the receiver slow the sender during the high-latency handshake"
  answer: 1
  explanation: "Throughput is bounded by (window size / RTT). With 64 KB = 65,536 bytes and RTT = 0.15 s: maximum throughput ≈ 65,536 / 0.15 ≈ 437 KB/s ≈ 3.5 Mbps. The sender exhausts its allowed in-flight data before the first ACK returns and must idle. This is the bandwidth-delay product problem. Window scaling (RFC 1323) was created precisely for this: by allowing effective windows in the megabytes, it enables full utilization of high-bandwidth, high-latency links."

- question: "TCP flow control and TCP congestion control both limit how much data the sender can have unacknowledged at once, but they respond to entirely different signals."
  type: true-false
  answer: true
  explanation: "Both mechanisms constrain the sender — the effective window is min(rwnd, cwnd), where rwnd is the receiver-advertised window (flow control) and cwnd is the congestion window (congestion control). But they respond to different signals: flow control responds to the receiver's available buffer space (advertised in every ACK), while congestion control responds to network congestion indicators (packet loss or ECN marks). Both are active simultaneously, and the sender transmits at the rate allowed by whichever constraint is tighter."

- question: "The TCP receive window size is negotiated once during the three-way handshake and remains fixed for the duration of the connection."
  type: true-false
  answer: false
  explanation: "The receive window (rwnd) is advertised in every segment the receiver sends and changes dynamically as the receiver's application processes data (freeing buffer space) or falls behind (filling the buffer). This dynamic adjustment IS the flow control mechanism — a static window would provide no feedback loop. What is negotiated at connection setup is only the window scale factor (RFC 1323), which sets the multiplier for interpreting subsequent window values. The actual window value changes with every ACK."

- question: "Why does increasing the TCP receive window size improve throughput on high-latency links, even when the physical bandwidth is not the bottleneck?"
  type: short-answer
  answer: "Throughput is bounded by window_size / RTT. The sender can have at most rwnd bytes unacknowledged in flight at any moment. On a high-latency link, the round-trip time is large, meaning the sender must wait a long time before ACKs return. If the window is too small, the sender exhausts its allowed in-flight data before the first ACK arrives and must idle — leaving bandwidth unused. A larger window keeps more data in flight simultaneously, filling the bandwidth-delay product and enabling continuous transmission."
  explanation: "The intuition is 'pipe filling': the link is a pipe whose volume equals RTT × bandwidth. To keep the pipe full, you need enough in-flight data to fill it. A 64 KB window and 150 ms RTT gives only ~3.5 Mbps of pipe-filling capacity regardless of physical bandwidth. Window scaling solves this by allowing windows sized to match the bandwidth-delay product — enabling the sender to keep the entire pipe filled with data in transit. This is why BDP is fundamental to network performance analysis, and why simply upgrading bandwidth without adjusting TCP parameters often produces disappointing throughput improvements."
```

## Explainer

From your study of TCP, you know it provides reliable, ordered byte-stream delivery. But reliability alone does not prevent a fast sender from overwhelming a slow receiver — if the sender blasts data faster than the receiver can process it, the receiver's buffer fills up and incoming segments get dropped. **Flow control** is TCP's mechanism for preventing this, and the **sliding window** is how it works in practice.

Every TCP segment the receiver sends back includes a field called the **receive window (rwnd)** — a 16-bit value announcing how many bytes of buffer space the receiver currently has available. The sender treats this as a hard cap: it will never have more than rwnd bytes of unacknowledged data in flight. As the receiver processes data and frees buffer space, it advertises a larger window in subsequent ACKs. As its buffer fills up, it shrinks the window. This creates a dynamic, self-regulating feedback loop — the sender continuously adjusts its transmission rate based on the receiver's latest advertisement.

Visualize it concretely. Suppose the receiver advertises a window of 4,000 bytes. The sender can transmit segments totaling 4,000 bytes and then must stop and wait. When the receiver processes 1,000 bytes and sends an ACK, that ACK advertises a new window (say 1,000 bytes of free space), which lets the sender transmit 1,000 more bytes. The "window" slides forward along the byte stream as data is acknowledged. If the receiver is temporarily swamped — perhaps the application reading from the socket is busy — it can advertise a **zero window**, telling the sender to stop completely. The sender then enters a **persist** state, periodically sending tiny probe segments to check whether the window has reopened, ensuring the connection does not deadlock.

The original TCP header allocates 16 bits for the window field, limiting it to 65,535 bytes. This was fine for early networks, but modern high-bandwidth, high-latency links (think intercontinental fiber) need much larger windows to keep the pipe full. **Window scaling** (RFC 1323) solves this by negotiating a scale factor during the three-way handshake. A scale factor of 7, for example, means the advertised window value is left-shifted by 7 bits, allowing effective windows up to gigabytes. This is essential for achieving full throughput on links where the bandwidth-delay product — the amount of data "in flight" to fill the pipe — exceeds 64 KB. Understanding this distinction between flow control (receiver-driven, preventing buffer overflow) and congestion control (network-driven, preventing router overload) is critical: TCP uses both simultaneously, and the sender transmits at the rate allowed by whichever constraint is tighter.
