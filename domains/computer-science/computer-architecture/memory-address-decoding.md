---
id: memory-address-decoding
title: Memory Address Decoding
domain: computer-science
course: computer-architecture
prerequisites:
- id: decoders-multiplexers
  type: hard
- id: memory-organization
  type: hard
builds-toward:
- memory-access-timing
tags:
- address-decoding
- memory-circuits
stage: formal-systems
status: draft
---

# Memory Address Decoding

## Core Idea
Address decoding selects the correct memory location from an n-bit address using decoders. 2D decoding (row/column) reduces complexity; partial and hierarchical decoding further optimize large memories.

## Explainer

You already know how decoders work: an n-input decoder activates exactly one of 2^n output lines based on the binary input. You also know that memory is organized as an array of storage locations, each holding a fixed number of bits. **Address decoding** is the bridge between these two concepts — it is the mechanism that translates a binary address from the CPU into the activation of one specific memory cell (or row of cells) within a memory chip.

Consider a simple example: a memory chip with 1,024 locations needs a 10-bit address. A straightforward approach would use a single 10-to-1024 decoder, but that decoder would have 1,024 output lines — an impractical number of wires and gates. **Two-dimensional (2D) decoding** solves this by splitting the address into two halves. The upper 5 bits select one of 32 rows, and the lower 5 bits select one of 32 columns. Now you need only a 5-to-32 row decoder and a 5-to-32 column decoder — 64 output lines total instead of 1,024. The selected memory cell sits at the intersection of the activated row and column, just like finding a seat in a theater by row letter and seat number.

Real systems take this further with **hierarchical decoding**. A computer with 4 GB of RAM doesn't have a single monolithic chip — it has many smaller memory chips organized into banks and modules. The highest-order address bits select which chip or bank is active (using a chip-select signal driven by a decoder), while the remaining bits perform the row/column decoding within that chip. **Partial decoding** is a simpler but less precise technique where not all address bits are decoded — some bits are ignored, causing the same physical memory to appear at multiple addresses (called **aliasing**). This was common in early microcomputers where simplicity mattered more than full address space utilization, but modern systems use full decoding to avoid wasting address space.
