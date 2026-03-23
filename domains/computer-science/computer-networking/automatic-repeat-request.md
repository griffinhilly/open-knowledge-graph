---
id: automatic-repeat-request
title: Automatic Repeat Request (ARQ)
domain: computer-science
course: computer-networking
prerequisites:
- id: error-detection-and-correction
  type: hard
builds-toward:
- sliding-window-protocol
- tcp-transmission-control-protocol
tags:
- arq
- retransmission
- error-recovery
- reliability
stage: advanced
status: validated
---

# Automatic Repeat Request (ARQ)

## Core Idea
ARQ protocols recover from packet loss by having the receiver acknowledge correct receipt and the sender retransmit unacknowledged packets. Stop-and-wait ARQ sends one packet at a time and waits for acknowledgment, while sliding-window variants (Go-Back-N, Selective Repeat) allow multiple outstanding packets. ARQ is fundamental to reliable data transfer in networks.

## Questions

```yaml
- question: "A sender uses Stop-and-Wait ARQ over a satellite link with 600ms round-trip time. The link bandwidth is 1 Mbps and each packet is 1,000 bits. Approximately what is the maximum achievable throughput?"
  type: multiple-choice
  options:
    - "1 Mbps — Stop-and-Wait uses the full bandwidth since only one packet is in flight at a time"
    - "500 Kbps — the protocol is exactly 50% efficient due to ACK overhead"
    - "Approximately 1.7 Kbps — one packet (1 ms transmission time) per 601 ms round trip"
    - "Approximately 2 Mbps — Stop-and-Wait doubles throughput by interleaving send and receive"
  answer: 2
  explanation: "Stop-and-Wait sends one packet and then waits for an ACK before sending the next. Sending 1,000 bits at 1 Mbps takes 1 ms, then the sender waits 600 ms for the round trip. So only 1 packet is sent per 601 ms — about 1,000 bits / 0.601 s ≈ 1,664 bps. The vast majority of the link capacity sits idle. This illustrates why Stop-and-Wait is catastrophically inefficient on high-bandwidth-delay product links."

- question: "A Go-Back-N ARQ sender has window size N=8. Packets 1 through 8 are all transmitted. Packet 4 is lost; packets 5, 6, 7, and 8 arrive intact at the receiver. What does the receiver do with packets 5–8?"
  type: multiple-choice
  options:
    - "Buffers them and sends individual ACKs, then requests only packet 4 to be retransmitted"
    - "Discards them and sends a NAK for packet 4 — Go-Back-N receivers only accept in-order packets"
    - "Acknowledges them with cumulative ACKs, signaling to the sender that no retransmission is needed"
    - "Stores only packet 5 and discards 6–8 to conserve buffer space"
  answer: 1
  explanation: "Go-Back-N receivers are intentionally simple: they only accept packets in order. Any out-of-order packet (5–8, which cannot be delivered until 4 arrives) is discarded. The sender must then retransmit packet 4 AND all subsequent packets (5–8), even though those arrived correctly. This waste of bandwidth is the key disadvantage of Go-Back-N versus Selective Repeat, which buffers out-of-order packets and only requests the specific missing one."

- question: "ARQ protocols achieve reliable delivery over an unreliable channel using error detection combined with retransmission — they do not require error correction codes."
  type: true-false
  answer: true
  explanation: "Error correction (like Hamming codes or Reed-Solomon) embeds enough redundancy to reconstruct corrupted bits without retransmission. ARQ takes a different approach: just detect that something went wrong (using a checksum or CRC), discard the bad packet, and ask for a retransmission. This is simpler to implement and wastes no bandwidth on correction redundancy when errors are rare. The tradeoff is that errors cause retransmissions (latency) rather than inline repair (complexity)."

- question: "In Selective Repeat ARQ, the receiver discards correctly received out-of-order packets to keep implementation simple, relying on the sender to retransmit the entire window from the lost packet onward."
  type: true-false
  answer: false
  explanation: "That describes Go-Back-N, not Selective Repeat. Selective Repeat receivers buffer correctly received out-of-order packets and only request retransmission of the specific missing packets. This is more complex for the receiver (requires buffer space and reordering logic) but far more efficient when errors are rare, because correct packets are never needlessly retransmitted. The naming reflects the key distinction: Go-Back-N 'goes back' to the lost packet and retransmits everything; Selective Repeat selectively retransmits only what was lost."

- question: "Why does Stop-and-Wait ARQ perform poorly on high-bandwidth, high-latency links, and what fundamental change do sliding-window protocols make to address this?"
  type: short-answer
  answer: "Stop-and-Wait lets only one packet be in flight at a time. On a high-bandwidth, high-latency link, the round-trip time is long relative to the packet transmission time, so the sender spends most of its time idle waiting for ACKs — the 'pipe' is nearly empty. Sliding-window protocols allow the sender to transmit multiple packets before receiving any acknowledgment, keeping the pipe full. The window size is chosen to match the bandwidth-delay product: window ≥ bandwidth × round-trip time."
  explanation: "The metric that captures this inefficiency is the bandwidth-delay product: if a 1 Gbps link has a 100 ms round trip, you could have 100 Mb = 12.5 MB of data in transit simultaneously. Stop-and-Wait keeps at most one packet in flight, wasting nearly all of that capacity. A window size of at least bandwidth × RTT = 1 Gbps × 0.1 s / (packet size) packets is needed to fully utilize the link. This is why TCP's window size is a critical performance parameter on intercontinental connections."
```

## Explainer

From your study of error detection and correction, you know that checksums and CRCs can tell a receiver whether a packet arrived intact. But detection alone is not enough — once you know a packet is corrupted or missing, something must happen to recover the data. **Automatic Repeat Request (ARQ)** is the answer: a family of protocols where the receiver signals success or failure, and the sender retransmits anything that did not arrive correctly. ARQ converts an unreliable channel into a reliable one using just error detection, acknowledgments, and timeouts.

The simplest ARQ protocol is **Stop-and-Wait**. The sender transmits a single packet, starts a timer, and waits. If an acknowledgment (ACK) arrives before the timer expires, it sends the next packet. If the timer expires — meaning the packet or its ACK was lost — the sender retransmits the same packet. Sequence numbers (just 0 and 1, alternating) prevent the receiver from accepting a duplicate as a new packet. Stop-and-Wait is easy to implement but performs terribly on high-latency links because the sender sits idle during the entire round-trip time. On a satellite link with a 500 ms round trip, you can send at most two packets per second regardless of bandwidth — most of the pipe is empty.

**Go-Back-N** and **Selective Repeat** solve this by allowing the sender to have multiple packets "in flight" simultaneously using a **sliding window**. In Go-Back-N, the sender can transmit up to N packets without waiting for acknowledgments. If packet 3 is lost, the receiver discards packets 4, 5, 6 (even if they arrive intact) because they are out of order, and the sender must retransmit everything from packet 3 onward. This is simple for the receiver — it only needs to buffer one packet — but wasteful when errors are rare, since correct packets get needlessly retransmitted. **Selective Repeat** improves on this by having the receiver buffer out-of-order packets and only requesting retransmission of the specific packets that were lost. The sender retransmits only what is actually missing, but the receiver now needs buffer space and reordering logic.

The choice among these protocols is a classic engineering tradeoff. Stop-and-Wait is adequate for short, low-delay links. Go-Back-N works well when errors are rare and simplicity matters. Selective Repeat maximizes throughput on lossy or high-delay links but adds complexity. TCP, which you will study next, builds on these ARQ foundations with its own sliding window, cumulative acknowledgments, and selective acknowledgment (SACK) options — essentially a sophisticated hybrid of the principles you see here in their pure form.
