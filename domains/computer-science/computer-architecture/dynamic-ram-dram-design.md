---
id: dynamic-ram-dram-design
title: Dynamic RAM (DRAM) Organization and Refresh Cycles
domain: computer-science
course: computer-architecture
prerequisites:
- id: memory-array-organization
  type: hard
- id: memory-bus-interconnect
  type: soft
builds-toward:
- memory-hierarchy-design
tags:
- dram
- memory-design
- refresh
- timing
stage: formal-systems
status: validated
---

# Dynamic RAM (DRAM) Organization and Refresh Cycles

## Core Idea
A DRAM cell stores charge on a capacitor; a transistor gate controls access. DRAM is dense and cheap but must be refreshed (rewritten) periodically before charge leaks. Access is slower than SRAM and requires address multiplexing (row and column addresses on the same pins). Main memory uses DRAM; refresh cycles reduce available bandwidth.

## Questions

```yaml
- question: "A CPU performs a read operation on a DRAM row. After the data is returned to the CPU, what has happened to the charge on the capacitors in that row?"
  type: multiple-choice
  options:
    - "The capacitors retain their original charge — DRAM reads are non-destructive"
    - "The capacitors discharge during the read; sense amplifiers latch the values and the row is automatically rewritten"
    - "Only the accessed cells discharge; unaccessed cells in the same row retain their charge"
    - "The capacitors are refreshed before the read to guarantee data integrity"
  answer: 1
  explanation: "DRAM reads are destructive. When a row is activated, all cells dump their charge onto the shared bit lines — the sense amplifiers detect the tiny voltage difference, latch the values, and then immediately write them back to restore the charge. This implicit rewrite is why row activation counts as a refresh for that row. The destruction of the original charge is an unavoidable consequence of the sense amplifier architecture."

- question: "Why does DRAM use address multiplexing — sending row and column addresses in two separate cycles on the same pins — instead of sending the full address at once?"
  type: multiple-choice
  options:
    - "It reduces latency by allowing the row and column decoders to work simultaneously"
    - "It halves the number of address pins required, keeping the package compact and inexpensive"
    - "It allows the memory controller to refresh rows between address cycles"
    - "It prevents timing conflicts between read and write operations on the same row"
  answer: 1
  explanation: "Address multiplexing is a cost and packaging decision. A DRAM with 1 GB of addressable memory would need 30 address lines to send the full address at once. By sending the row address first (latched by the Row Address Strobe) and column address second (latched by the Column Address Strobe) on the same pins, the pin count is cut roughly in half. This makes DRAM chips physically smaller and cheaper — the tradeoff is the added latency of two address cycles per access."

- question: "DRAM cells must be periodically refreshed because their storage capacitors gradually lose charge and will eventually become unreadable without intervention."
  type: true-false
  answer: true
  explanation: "This is the fundamental characteristic that makes DRAM 'dynamic.' A capacitor leaks charge through the transistor and surrounding silicon even when no operation is occurring. Without refresh, stored values degrade within milliseconds. Modern DRAM must refresh every row within a 64-millisecond window. Each refresh cycle consumes memory bus bandwidth, making refresh overhead a constant performance tax."

- question: "DRAM achieves higher storage density than SRAM because it uses a more sophisticated multi-transistor cell that packs more tightly into silicon."
  type: true-false
  answer: false
  explanation: "DRAM achieves higher density because its cell is simpler, not more sophisticated. A DRAM cell uses one transistor and one capacitor (1T1C). An SRAM cell uses six transistors (6T) arranged in a feedback loop to hold state without refresh. Fewer transistors per bit means more bits per unit area — DRAM is denser because it is simpler, not despite being simpler."

- question: "Why does DRAM require periodic refresh even when no data is being read or written, and what is the performance cost of this requirement?"
  type: short-answer
  answer: "A DRAM capacitor leaks charge passively — charge dissipates through the transistor even with no active operation. Left unattended, stored values become unreadable within milliseconds. Refresh circuits must periodically activate every row in the array (reading and rewriting all cells) within a fixed window, typically 64 ms. Each refresh cycle occupies the memory bus, preventing normal read and write accesses during that time. This creates a constant bandwidth tax: some fraction of all memory cycles are consumed by refresh overhead, reducing the effective memory bandwidth available to the processor. This overhead, combined with the multi-step row/column addressing, is why DRAM latency is fundamentally higher than SRAM."
  explanation: "The refresh requirement is the defining tradeoff of DRAM design: you get 6× or more the storage density compared to SRAM, at the cost of refresh overhead and slower access. The memory hierarchy — SRAM caches close to the CPU, DRAM main memory farther away — exists precisely to hide this latency difference."
```

## Explainer

From your study of memory array organization, you know that memory is structured as a grid of rows and columns, with each intersection holding one bit. A **DRAM cell** is the simplest possible storage element: just one transistor and one tiny capacitor. The capacitor holds a charge (representing 1) or no charge (representing 0), and the transistor acts as a switch connecting the capacitor to a shared wire called the **bit line**. Compare this to an SRAM cell, which uses six transistors to hold its state in a feedback loop. DRAM's one-transistor design is why it achieves far higher density and lower cost per bit — and why virtually all main memory in computers is DRAM.

The fundamental tradeoff is that a capacitor leaks charge. Left alone, a DRAM cell will lose its stored value within milliseconds as the charge dissipates through the transistor and surrounding silicon. This means every cell must be periodically **refreshed** — read out and written back — before its charge drops below the threshold where the sense amplifier can distinguish 0 from 1. Modern DRAM refreshes every row in the array within a 64-millisecond window, typically using **distributed refresh** that spreads refresh operations across time rather than stalling the entire array at once. Each refresh cycle occupies the memory bus, stealing bandwidth from actual read and write requests. This refresh overhead is a constant tax on DRAM performance.

Accessing a DRAM cell is a multi-step process. First, the **row address** is sent and the corresponding row is activated — all cells in that row dump their charge onto the bit lines, where sense amplifiers detect and latch the values. This destructive read (the capacitors lose their charge) is why every access implicitly refreshes the row. Then the **column address** selects which bits from the activated row to output. The two-step addressing allows DRAM to share address pins between row and column signals (multiplexing), cutting the pin count in half compared to sending the full address at once. This pin reduction was a critical design decision that kept DRAM packages small and cheap, at the cost of requiring two address cycles per access.

Modern DRAM standards like DDR (Double Data Rate) build on this foundation with techniques to improve effective bandwidth: transferring data on both rising and falling clock edges, widening the internal bus, and allowing multiple banks to operate concurrently so one bank can be accessed while another refreshes. Understanding the basic cell structure and refresh requirement explains why DRAM latency is fundamentally higher than SRAM — and why the memory hierarchy you will study next uses small, fast SRAM caches in front of large, slow DRAM main memory to bridge the performance gap.
