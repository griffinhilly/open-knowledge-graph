---
id: static-ram-sram-design
title: Static RAM (SRAM) Cell Design and Arrays
domain: computer-science
course: computer-architecture
prerequisites:
- id: flip-flops-and-latches
  type: hard
- id: memory-array-organization
  type: soft
builds-toward:
- register-file-design
- cache-memory-design
tags:
- sram
- memory-cell
- memory-design
stage: formal-systems
status: draft
---

# Static RAM (SRAM) Cell Design and Arrays

## Core Idea
An SRAM cell is a cross-coupled NOR or NAND latch that stores one bit and requires continuous power. Unlike DRAM, SRAM is fast (single-cycle access) but power-hungry and area-inefficient. SRAM arrays use row and column decoders for addressing. Register files and caches are typically built from SRAM; main memory uses DRAM.

## Explainer

You already understand flip-flops and latches — circuits that use feedback loops to hold a binary value indefinitely as long as power is supplied. An **SRAM cell** is essentially a miniaturized latch, stripped down to the smallest circuit that can reliably store one bit. The standard design uses **six transistors** (6T): four transistors form two cross-coupled inverters that hold the stored value, and two additional transistors act as access gates controlled by a word line. When the word line is activated, the access transistors connect the storage inverters to a pair of complementary bit lines, allowing the cell to be read or written.

Reading an SRAM cell works by precharging both bit lines to a high voltage, then asserting the word line. The cross-coupled inverters pull one bit line slightly lower than the other, depending on the stored value. A **sense amplifier** detects this small voltage difference and amplifies it into a clean digital output. The key advantage is speed: because the stored value is actively maintained by the inverter pair, there is no need to restore the cell after reading (unlike DRAM, which destructively reads its capacitor). An SRAM read completes in a single clock cycle, making it ideal for circuits that demand the fastest possible access.

Writing works by driving the bit lines to the desired values and asserting the word line. The external drivers are stronger than the internal inverters, so they overpower the stored state and force the cross-coupled pair into the new configuration. Once the word line is deasserted, the feedback loop locks in the new value. This is straightforward but requires the drivers to be carefully sized — if they are too weak, the write fails; if the cell is too weak, it becomes vulnerable to noise during reads. Balancing these competing constraints is a central challenge in SRAM design.

The tradeoff that defines SRAM's role in computer architecture is **speed versus density**. Six transistors per bit is expensive in silicon area compared to DRAM's one transistor and one capacitor per bit. This means you can fit far fewer SRAM bits on a chip, making it impractical for main memory (which needs gigabytes). But SRAM's single-cycle access time and lack of refresh requirements make it perfect for **register files** (tens to hundreds of entries that the processor reads every cycle) and **cache memory** (kilobytes to megabytes of fast storage that bridge the speed gap between the processor and main memory). Nearly every modern processor uses SRAM for its L1, L2, and often L3 caches — the memory hierarchy depends on SRAM's speed advantage at the top and DRAM's density advantage at the bottom.
