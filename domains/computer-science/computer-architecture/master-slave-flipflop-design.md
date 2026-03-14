---
id: master-slave-flipflop-design
title: Master-Slave Flip-Flop Design
domain: computer-science
course: computer-architecture
prerequisites:
- id: transparent-latch-design
  type: hard
builds-toward:
- synchronous-counter-design
tags:
- flipflop
- edge-triggered
- sequential-logic
stage: formal-systems
status: draft
---

# Master-Slave Flip-Flop Design

## Core Idea
Master-slave flip-flops cascade two transparent latches: master captures on one clock edge, slave captures the master's output on the opposite edge. This provides edge-triggered behavior and eliminates race conditions.
