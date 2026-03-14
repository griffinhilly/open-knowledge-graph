---
id: sliding-window-protocol
title: Sliding Window Protocol
domain: computer-science
course: computer-networking
prerequisites:
- id: automatic-repeat-request
  type: hard
builds-toward:
- tcp-transmission-control-protocol
- tcp-flow-control-and-congestion-control
tags:
- sliding-window
- flow-control
- sequence-numbers
- buffering
stage: advanced
status: draft
---

# Sliding Window Protocol

## Core Idea
A sliding window allows a sender to have multiple packets in flight without waiting for acknowledgments, improving throughput by overlapping transmission and acknowledgment. The window size controls how many unacknowledged packets can exist; it slides forward as acknowledgments arrive. Both TCP and selective repeat ARQ use sliding windows to balance throughput with reliability.
