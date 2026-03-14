---
id: packet-switching-circuit-switching
title: Packet Switching vs. Circuit Switching
domain: computer-science
course: computer-networking
prerequisites:
- id: network-fundamentals
  type: hard
builds-toward:
- osi-model-layers
tags:
- switching
- packet-switching
- circuit-switching
- network-design
stage: advanced
status: draft
---

# Packet Switching vs. Circuit Switching

## Core Idea
Packet switching divides data into small packets that are independently routed across shared network links, while circuit switching establishes a dedicated end-to-end path before communication begins. Packet switching provides better utilization of shared resources and fault tolerance but introduces latency variability; circuit switching guarantees bandwidth but wastes resources if no data is being sent. Most modern networks use packet switching.
