---
id: processor-control-unit-design
title: Processor Control Unit Design
domain: computer-science
course: computer-architecture
prerequisites:
- id: instruction-decoding-logic
  type: hard
- id: hardwired-microprogrammed-control
  type: soft
builds-toward:
- hazard-detection-and-stalling
tags:
- control-unit
- processor-design
stage: formal-systems
status: draft
---

# Processor Control Unit Design

## Core Idea
The control unit interprets instructions and generates control signals for the datapath. In hardwired control, a decoder produces signals directly from instruction bits. In microprogrammed control, a ROM stores microcode sequences that output control signals over multiple cycles. The choice involves trade-offs: hardwired is fast but complex to modify; microprogrammed is flexible but slower.
