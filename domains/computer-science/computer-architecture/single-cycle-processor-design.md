---
id: single-cycle-processor-design
title: Single-Cycle Processor Architecture
domain: computer-science
course: computer-architecture
prerequisites:
- id: cpu-datapath
  type: hard
- id: instruction-fetch-decode-execute
  type: hard
- id: finite-state-machine-processor-design
  type: soft
builds-toward:
- multi-cycle-processor-design
- instruction-level-parallelism
tags:
- processor-design
- single-cycle
- architecture
stage: formal-systems
status: draft
---

# Single-Cycle Processor Architecture

## Core Idea
A single-cycle processor completes one instruction per clock cycle: fetch, decode, execute, memory access, and writeback all happen in a single clock period. The clock period must accommodate the longest critical path through all stages. This design is simple and has no pipeline hazards, but the slow clock limits performance.

## Explainer

You know from studying the CPU datapath that executing an instruction requires several operations: fetching the instruction from memory, decoding which operation to perform and which registers to use, executing the computation in the ALU, potentially accessing data memory, and writing the result back to a register. A **single-cycle processor** performs all of these operations in one clock cycle — signals ripple through the entire datapath from instruction memory to register write-back before the clock ticks again.

To see how this works concretely, trace an R-type instruction like `add $t0, $t1, $t2`. The **program counter** feeds an address to instruction memory, which outputs the 32-bit instruction. The decode logic extracts register specifiers and sends them to the **register file**, which outputs the values in $t1 and $t2. These values flow into the **ALU**, which computes their sum. The result travels past the data memory (unused for this instruction — controlled by MUXes you studied earlier) and arrives at the register file's write port, where it is stored in $t0. All of this — memory read, register read, ALU computation, register write — must complete within a single clock period. No intermediate values are stored; every signal propagates combinationally from input to output.

The fatal weakness of this design is the **critical path** problem. Different instructions use different parts of the datapath: an `add` never touches data memory, but a `lw` (load word) must read from data memory after the ALU computes the address. The clock period must be long enough for the *slowest* instruction to complete — typically `lw`, which traverses instruction memory, register file, ALU, data memory, and register write-back in sequence. Every other instruction, no matter how simple, must wait for this same long clock period. An `add` that could finish in 600 picoseconds is forced to wait 800 picoseconds because `lw` needs the extra time. This means the processor's clock frequency is dictated by its most complex instruction, wasting time on every simpler one.

Despite this inefficiency, the single-cycle design is valuable as a conceptual foundation. It is the simplest complete processor architecture: no pipeline registers, no hazards, no forwarding logic, no stall control. Every instruction takes exactly one cycle, so CPI (cycles per instruction) is always 1 — performance depends entirely on clock speed. Understanding its limitations motivates the multi-cycle design (which breaks execution into variable-length steps to avoid the critical-path penalty) and pipelining (which overlaps multiple instructions to reclaim the wasted time). The single-cycle processor is rarely built in practice, but it is the baseline against which all more sophisticated designs are measured.
