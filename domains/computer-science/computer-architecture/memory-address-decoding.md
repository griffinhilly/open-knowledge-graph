---
id: memory-address-decoding
title: Memory Address Decoding and Control
domain: computer-science
course: computer-architecture
prerequisites:
- id: memory-array-organization
  type: hard
- id: binary-number-system
  type: soft
builds-toward:
- cache-design-principles
- instruction-fetch-decode-execute
tags:
- memory
- addressing
- decoding
- control
stage: formal-systems
status: draft
---

# Memory Address Decoding and Control

## Core Idea
Address decoders map address bus bits to specific memory locations, and control signals (read, write, chip select) govern data flow. Multi-chip systems use upper address bits to select chips and lower bits to select within each chip.
