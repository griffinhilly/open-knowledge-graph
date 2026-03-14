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
