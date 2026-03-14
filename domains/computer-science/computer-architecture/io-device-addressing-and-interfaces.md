---
id: io-device-addressing-and-interfaces
title: I/O Device Addressing and Interface Design
domain: computer-science
course: computer-architecture
prerequisites:
- id: io-systems-overview
  type: hard
- id: memory-bus-interconnect
  type: soft
builds-toward:
- io-subsystem-design
tags:
- io-interfaces
- device-addressing
- memory-mapped-io
stage: formal-systems
status: draft
---

# I/O Device Addressing and Interface Design

## Core Idea
Devices are accessed via memory-mapped I/O (addresses in the same space as RAM) or port I/O (separate address space). Memory-mapped I/O is common: writes to device addresses trigger control actions, reads from device addresses return status. Timing and handshaking protocols (ready, acknowledge signals) coordinate CPU and device. Interrupt and polling modes handle completion notification.
