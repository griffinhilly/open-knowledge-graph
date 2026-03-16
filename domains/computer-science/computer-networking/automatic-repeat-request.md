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
status: draft
---

# Automatic Repeat Request (ARQ)

## Core Idea
ARQ protocols recover from packet loss by having the receiver acknowledge correct receipt and the sender retransmit unacknowledged packets. Stop-and-wait ARQ sends one packet at a time and waits for acknowledgment, while sliding-window variants (Go-Back-N, Selective Repeat) allow multiple outstanding packets. ARQ is fundamental to reliable data transfer in networks.

## Explainer

From your study of error detection and correction, you know that checksums and CRCs can tell a receiver whether a packet arrived intact. But detection alone is not enough — once you know a packet is corrupted or missing, something must happen to recover the data. **Automatic Repeat Request (ARQ)** is the answer: a family of protocols where the receiver signals success or failure, and the sender retransmits anything that did not arrive correctly. ARQ converts an unreliable channel into a reliable one using just error detection, acknowledgments, and timeouts.

The simplest ARQ protocol is **Stop-and-Wait**. The sender transmits a single packet, starts a timer, and waits. If an acknowledgment (ACK) arrives before the timer expires, it sends the next packet. If the timer expires — meaning the packet or its ACK was lost — the sender retransmits the same packet. Sequence numbers (just 0 and 1, alternating) prevent the receiver from accepting a duplicate as a new packet. Stop-and-Wait is easy to implement but performs terribly on high-latency links because the sender sits idle during the entire round-trip time. On a satellite link with a 500 ms round trip, you can send at most two packets per second regardless of bandwidth — most of the pipe is empty.

**Go-Back-N** and **Selective Repeat** solve this by allowing the sender to have multiple packets "in flight" simultaneously using a **sliding window**. In Go-Back-N, the sender can transmit up to N packets without waiting for acknowledgments. If packet 3 is lost, the receiver discards packets 4, 5, 6 (even if they arrive intact) because they are out of order, and the sender must retransmit everything from packet 3 onward. This is simple for the receiver — it only needs to buffer one packet — but wasteful when errors are rare, since correct packets get needlessly retransmitted. **Selective Repeat** improves on this by having the receiver buffer out-of-order packets and only requesting retransmission of the specific packets that were lost. The sender retransmits only what is actually missing, but the receiver now needs buffer space and reordering logic.

The choice among these protocols is a classic engineering tradeoff. Stop-and-Wait is adequate for short, low-delay links. Go-Back-N works well when errors are rare and simplicity matters. Selective Repeat maximizes throughput on lossy or high-delay links but adds complexity. TCP, which you will study next, builds on these ARQ foundations with its own sliding window, cumulative acknowledgments, and selective acknowledgment (SACK) options — essentially a sophisticated hybrid of the principles you see here in their pure form.
