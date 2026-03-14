---
id: logical-clocks
title: Logical Clocks and Event Ordering
domain: computer-science
course: distributed-systems
prerequisites:
- id: distributed-systems-overview
  type: hard
- id: process-concept
  type: soft
builds-toward:
- lamport-timestamps
- vector-clocks
tags:
- time
- ordering
- causality
stage: advanced
status: draft
---

# Logical Clocks and Event Ordering

## Core Idea
Without synchronized physical clocks, distributed systems need logical mechanisms to order events. Logical clocks assign monotonically increasing values to events based on message passing and local execution, capturing causal relationships and enabling detection of whether one event could have influenced another.
