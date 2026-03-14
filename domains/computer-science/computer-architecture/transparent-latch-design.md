---
id: transparent-latch-design
title: Transparent Latch Design and Timing
domain: computer-science
course: computer-architecture
prerequisites:
- id: flip-flops-and-latches
  type: hard
builds-toward:
- master-slave-flipflop-design
tags:
- latch
- timing
- sequential-logic
stage: formal-systems
status: draft
---

# Transparent Latch Design and Timing

## Core Idea
A transparent latch captures data when enabled (control=1), with output following input; when disabled, it holds state. Setup and hold time constraints relative to the control signal are critical for correct operation.
