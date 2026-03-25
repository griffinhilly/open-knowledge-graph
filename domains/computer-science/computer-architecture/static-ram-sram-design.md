---
id: static-ram-sram-design
title: Static RAM (SRAM) Cell Design and Arrays
domain: computer-science
course: computer-architecture
prerequisites:
- id: flip-flops-and-latches
  type: hard
- id: memory-organization
  type: soft
builds-toward:
- registers-and-register-files
- cache-memory-design
tags:
- sram
- memory-cell
- memory-design
stage: formal-systems
status: validated
---

# Static RAM (SRAM) Cell Design and Arrays

## Core Idea
An SRAM cell is a cross-coupled NOR or NAND latch that stores one bit and requires continuous power. Unlike DRAM, SRAM is fast (single-cycle access) but power-hungry and area-inefficient. SRAM arrays use row and column decoders for addressing. Register files and caches are typically built from SRAM; main memory uses DRAM.

## Questions

```yaml
- question: "A chip designer needs to implement 16 GB of main memory for a laptop. Should they use SRAM or DRAM?"
  type: multiple-choice
  options:
    - "SRAM, because it does not require refresh and is therefore more power-efficient at large scales"
    - "DRAM, because SRAM's six-transistor cell makes 16 GB impractical to fit on a chip"
    - "SRAM, because single-cycle access is required for all memory in modern processors"
    - "Either works equally well; the choice depends only on desired clock speed"
  answer: 1
  explanation: "SRAM uses six transistors per bit versus DRAM's one transistor and one capacitor. This 6× area penalty makes SRAM economically impractical for gigabyte-scale storage. Option A is the most tempting wrong answer — SRAM does avoid the power cost of refresh, but its standby power from the always-active inverters and its massive area cost make it unsuitable for main memory. DRAM's density advantage defines its role at the bottom of the memory hierarchy."

- question: "During an SRAM read, what physically happens that distinguishes it from a DRAM read?"
  type: multiple-choice
  options:
    - "The stored capacitor charge is sensed and then immediately refreshed to prevent data loss"
    - "Both bit lines are precharged high; the cross-coupled inverters pull one side slightly lower, and a sense amplifier amplifies the difference"
    - "The access transistors discharge the stored bit into the bit line, which must then be rewritten"
    - "The cross-coupled inverters are temporarily disabled to allow non-destructive voltage measurement"
  answer: 1
  explanation: "SRAM reads are non-destructive because the cross-coupled inverters actively maintain the stored value. Precharging both bit lines and letting the inverters create a small differential, then amplifying it, gives a fast single-cycle result without disturbing the cell. Options A and C describe the DRAM read cycle, which is destructive — the capacitor discharges during reading and must be refreshed. Option D is nonsensical; disabling the inverters would destroy the stored state."

- question: "SRAM cells retain their stored value indefinitely without periodic refresh because the cross-coupled inverters actively regenerate the bit as long as power is supplied."
  type: true-false
  answer: true
  explanation: "This is exactly right. The two cross-coupled inverters form a feedback loop: each inverter's output drives the other's input, locking in either a 0 or 1. As long as power is present, this feedback continuously reinforces the stored value. DRAM, by contrast, stores charge on a capacitor that leaks over time, requiring periodic refresh cycles to restore the charge before it drops below a detectable threshold."

- question: "SRAM is commonly used for main memory in modern computers because its lack of refresh overhead makes it practical for large storage capacities."
  type: true-false
  answer: false
  explanation: "This reverses the actual tradeoff. SRAM is never used for main memory because six transistors per bit consumes far too much silicon area compared to DRAM's one-transistor-one-capacitor cell. SRAM's speed and no-refresh advantages make it ideal for small, fast structures — register files and L1/L2/L3 caches — where kilobytes to megabytes are needed at single-cycle access speeds. Main memory (gigabytes) uses DRAM despite its slower access and refresh overhead."

- question: "Why does SRAM use six transistors per bit rather than a simpler design like DRAM's one-transistor-one-capacitor cell, and what consequence does this have for where SRAM appears in the memory hierarchy?"
  type: short-answer
  answer: "SRAM needs six transistors to implement cross-coupled inverters (four transistors) plus two access transistors. This feedback loop is what makes SRAM fast and self-maintaining — but it costs 6× the silicon area of a DRAM cell. The consequence is that SRAM is economically viable only for small, high-speed structures: register files (tens to hundreds of entries read every cycle) and cache memory (kilobytes to megabytes bridging CPU and main memory). DRAM's density advantage makes it the only practical choice for gigabyte-scale main memory despite its slower access and refresh requirements."
  explanation: "The six-transistor design is not over-engineering — each transistor serves a purpose. Four form the inverter pair that maintains state through feedback; two are access gates controlled by the word line. Simpler latch designs are noisier and less robust to process variation. The 6T cell is essentially the minimum reliable design for a single-bit storage element. This area cost directly determines SRAM's role: fast but small at the top of the hierarchy (caches, registers), with DRAM's density taking over for the bulk of memory."
```

## Explainer

You already understand flip-flops and latches — circuits that use feedback loops to hold a binary value indefinitely as long as power is supplied. An **SRAM cell** is essentially a miniaturized latch, stripped down to the smallest circuit that can reliably store one bit. The standard design uses **six transistors** (6T): four transistors form two cross-coupled inverters that hold the stored value, and two additional transistors act as access gates controlled by a word line. When the word line is activated, the access transistors connect the storage inverters to a pair of complementary bit lines, allowing the cell to be read or written.

Reading an SRAM cell works by precharging both bit lines to a high voltage, then asserting the word line. The cross-coupled inverters pull one bit line slightly lower than the other, depending on the stored value. A **sense amplifier** detects this small voltage difference and amplifies it into a clean digital output. The key advantage is speed: because the stored value is actively maintained by the inverter pair, there is no need to restore the cell after reading (unlike DRAM, which destructively reads its capacitor). An SRAM read completes in a single clock cycle, making it ideal for circuits that demand the fastest possible access.

Writing works by driving the bit lines to the desired values and asserting the word line. The external drivers are stronger than the internal inverters, so they overpower the stored state and force the cross-coupled pair into the new configuration. Once the word line is deasserted, the feedback loop locks in the new value. This is straightforward but requires the drivers to be carefully sized — if they are too weak, the write fails; if the cell is too weak, it becomes vulnerable to noise during reads. Balancing these competing constraints is a central challenge in SRAM design.

The tradeoff that defines SRAM's role in computer architecture is **speed versus density**. Six transistors per bit is expensive in silicon area compared to DRAM's one transistor and one capacitor per bit. This means you can fit far fewer SRAM bits on a chip, making it impractical for main memory (which needs gigabytes). But SRAM's single-cycle access time and lack of refresh requirements make it perfect for **register files** (tens to hundreds of entries that the processor reads every cycle) and **cache memory** (kilobytes to megabytes of fast storage that bridge the speed gap between the processor and main memory). Nearly every modern processor uses SRAM for its L1, L2, and often L3 caches — the memory hierarchy depends on SRAM's speed advantage at the top and DRAM's density advantage at the bottom.
