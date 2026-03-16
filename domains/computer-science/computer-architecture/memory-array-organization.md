---
id: memory-array-organization
title: Memory Array Organization and Access
domain: computer-science
course: computer-architecture
prerequisites:
- id: decoders-multiplexers
  type: hard
- id: d-flip-flop-design
  type: soft
builds-toward:
- memory-address-decoding
- cache-design-principles
tags:
- memory
- arrays
- addressing
- organization
stage: formal-systems
status: draft
---

# Memory Array Organization and Access

## Core Idea
Memory arrays arrange storage cells (flip-flops or capacitors) in a 2D grid, using row and column decoders to select individual cells. Address lines are split between row and column to reduce decoder complexity.

## How It's Best Learned
Design a 4×4 bit memory array with row/column decoders; trace address-to-cell selection.

## Common Misconceptions
Both row and column decoders must be active to select one cell. Larger arrays use hierarchical decoding, not monolithic decoders.

## Explainer

You already know that decoders take an n-bit input and activate exactly one of 2^n output lines. Memory arrays use this principle at scale: thousands or millions of storage cells are arranged in a two-dimensional grid, and decoders select which cell to read or write. Understanding this organization explains why memory has the capacity, speed, and cost characteristics it does.

Consider a memory that stores 1,024 bits. You could build a single decoder with 10 address lines selecting one of 1,024 cells in a flat row — but a 10-to-1024 decoder is enormous, requiring 1,024 AND gates each with 10 inputs. Instead, the **2D organization** splits those 10 address bits into two groups: 5 bits for a **row decoder** (selecting one of 32 rows) and 5 bits for a **column decoder** (selecting one of 32 columns). Each decoder is now only 5-to-32, dramatically reducing hardware complexity. The row decoder activates an entire row of 32 cells, and the column decoder then picks the single cell you want from that activated row. This is why memory is described as having "rows" and "columns" — it is physically laid out as a grid.

Each cell in the grid stores one bit. In **SRAM** (static RAM), each cell is a cross-coupled pair of inverters — essentially two NOT gates feeding back into each other, forming the kind of bistable latch you studied with flip-flops. SRAM cells are fast but large, requiring six transistors per bit. In **DRAM** (dynamic RAM), each cell is just a single transistor and a tiny capacitor: the capacitor holds charge to represent a 1 or discharges to represent a 0. This makes DRAM cells extremely compact — roughly one-sixth the area of SRAM — but the charge leaks away in milliseconds, requiring periodic **refresh** cycles that read and rewrite every row. This fundamental tradeoff between density and complexity is why DRAM is used for main memory (cheap, dense) while SRAM is used for caches (fast, expensive).

When you read from a memory array, the process unfolds in stages. The row decoder activates a **word line**, connecting an entire row of cells to their respective **bit lines** (vertical wires). The cells drive tiny voltage differences onto the bit lines, which **sense amplifiers** detect and amplify into clean digital signals. The column decoder then selects which amplified bit(s) to route to the output. Writing reverses the flow: the column decoder steers input data to the correct bit line, and the active word line lets the new value overwrite the selected cell. In practice, modern DRAMs read an entire row into a **row buffer** at once, making subsequent accesses to the same row much faster than accesses to a different row — a phenomenon called **row buffer locality** that has profound implications for memory system performance.
