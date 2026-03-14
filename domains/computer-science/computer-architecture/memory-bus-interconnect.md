---
id: memory-bus-interconnect
title: Memory Bus Architecture and Interconnect
domain: computer-science
course: computer-architecture
prerequisites:
- id: cpu-datapath
  type: hard
- id: memory-address-decoding
  type: soft
builds-toward:
- io-architecture-system-integration
- cache-design-principles
tags:
- bus
- memory
- interconnect
- protocol
stage: formal-systems
status: draft
---

# Memory Bus Architecture and Interconnect

## Core Idea
Memory buses connect CPU, cache, memory, and I/O; they must coordinate address, data, and control signals with proper timing. Bus arbitration resolves conflicts; protocols (like AXI) standardize handshaking and flow control.
