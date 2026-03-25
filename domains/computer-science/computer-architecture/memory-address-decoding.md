---
id: memory-address-decoding
title: Memory Address Decoding
domain: computer-science
course: computer-architecture
prerequisites:
- id: multiplexers-and-demultiplexers
  type: hard
- id: memory-organization
  type: hard
builds-toward:
- memory-access-timing
tags:
- address-decoding
- memory-circuits
stage: formal-systems
status: validated
---

# Memory Address Decoding

## Core Idea
Address decoding selects the correct memory location from an n-bit address using decoders. 2D decoding (row/column) reduces complexity; partial and hierarchical decoding further optimize large memories.

## Questions

```yaml
- question: "A memory chip requires a 12-bit address. Compared to using a single flat 12-to-4096 decoder, two-dimensional decoding (6 row bits + 6 column bits) requires how many total decoder output lines?"
  type: multiple-choice
  options:
    - "4,096 — 2D decoding saves internal wiring but the number of output lines stays the same"
    - "128 — 64 from the row decoder plus 64 from the column decoder"
    - "2,048 — exactly half as many as the flat decoder"
    - "24 — two output lines per address bit"
  answer: 1
  explanation: "A single flat 12-to-4096 decoder needs 4,096 output lines — one per possible address. 2D decoding splits the 12-bit address into two 6-bit halves, requiring a 6-to-64 row decoder (64 outputs) and a 6-to-64 column decoder (64 outputs): 128 lines total instead of 4,096. This is the core efficiency gain of 2D decoding — the output count grows as 2 × 2^(n/2) rather than 2^n."

- question: "What is the consequence of 'partial decoding' in a memory system?"
  type: multiple-choice
  options:
    - "Memory access becomes slower because fewer address bits are checked"
    - "The same physical memory location appears at multiple addresses, called aliasing"
    - "Certain memory addresses become permanently inaccessible"
    - "Memory chips using partial decoding cannot correctly store all data patterns"
  answer: 1
  explanation: "Partial decoding ignores some address bits, meaning multiple distinct addresses map to the same physical location. For example, if bit 15 is ignored, addresses 0x0100 and 0x8100 both select the same memory cell. This 'aliasing' wastes address space but reduces hardware complexity. Early microcomputers used this tradeoff deliberately; modern systems use full decoding to avoid wasting the address space."

- question: "In a 2D decoded memory with a 10-bit address split into 5 row bits and 5 column bits, each row in the memory array contains 32 cells that share the same row-select signal."
  type: true-false
  answer: true
  explanation: "With 5 row bits, the row decoder has 2^5 = 32 output lines, one per row. Each row contains 2^5 = 32 cells (one per column). When a row line is asserted, all 32 cells in that row are electrically accessed simultaneously — this is why DRAM, which uses a similar scheme, has a separate row-access strobe (RAS) and column-address strobe (CAS) phase in its timing."

- question: "Using a single flat 10-to-1024 decoder for a 10-bit address requires fewer output wires than 2D decoding with the same address width."
  type: true-false
  answer: false
  explanation: "A flat 10-to-1024 decoder requires 1,024 output lines. 2D decoding splits the address 5+5, requiring a 5-to-32 row decoder (32 outputs) plus a 5-to-32 column decoder (32 outputs) = 64 lines total. 64 is far fewer than 1,024. This reduction — from 2^n to 2 × 2^(n/2) — is the primary motivation for 2D decoding in memory design."

- question: "Why does 2D address decoding reduce hardware complexity compared to a flat decoder, and what is the tradeoff introduced?"
  type: short-answer
  answer: "2D decoding splits the n-bit address into two halves, each decoded independently. This reduces output lines from 2^n to 2 × 2^(n/2) — a massive saving for wide addresses. The tradeoff is that memory selection now requires two signals (row and column) that must both be asserted to select a cell, introducing a two-phase access sequence rather than a single decode step. This adds slight timing complexity but is vastly cheaper in hardware."
  explanation: "The exponential-to-linear reduction in decoder outputs is what makes large memory arrays feasible. A 32-bit flat decoder would need 4 billion output lines — physically impossible. 2D decoding with 16-bit halves needs only 2 × 65,536 = 131,072 lines. Hierarchical decoding extends this further by cascading multiple levels, each operating on a subset of address bits."
```

## Explainer

You already know how decoders work: an n-input decoder activates exactly one of 2^n output lines based on the binary input. You also know that memory is organized as an array of storage locations, each holding a fixed number of bits. **Address decoding** is the bridge between these two concepts — it is the mechanism that translates a binary address from the CPU into the activation of one specific memory cell (or row of cells) within a memory chip.

Consider a simple example: a memory chip with 1,024 locations needs a 10-bit address. A straightforward approach would use a single 10-to-1024 decoder, but that decoder would have 1,024 output lines — an impractical number of wires and gates. **Two-dimensional (2D) decoding** solves this by splitting the address into two halves. The upper 5 bits select one of 32 rows, and the lower 5 bits select one of 32 columns. Now you need only a 5-to-32 row decoder and a 5-to-32 column decoder — 64 output lines total instead of 1,024. The selected memory cell sits at the intersection of the activated row and column, just like finding a seat in a theater by row letter and seat number.

Real systems take this further with **hierarchical decoding**. A computer with 4 GB of RAM doesn't have a single monolithic chip — it has many smaller memory chips organized into banks and modules. The highest-order address bits select which chip or bank is active (using a chip-select signal driven by a decoder), while the remaining bits perform the row/column decoding within that chip. **Partial decoding** is a simpler but less precise technique where not all address bits are decoded — some bits are ignored, causing the same physical memory to appear at multiple addresses (called **aliasing**). This was common in early microcomputers where simplicity mattered more than full address space utilization, but modern systems use full decoding to avoid wasting address space.
