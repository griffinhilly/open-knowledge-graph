---
id: pipelining-fundamentals
title: CPU Pipelining
domain: computer-science
course: computer-architecture
prerequisites:
- id: cpu-datapath
  type: hard
- id: instruction-set-architecture
  type: hard
- id: cpu-control-unit
  type: soft
builds-toward:
- pipeline-hazards
tags:
- pipelining
- throughput
- latency
- RISC
- stages
stage: formal-systems
status: validated
---
# CPU Pipelining

## Core Idea
Pipelining overlaps the execution of multiple instructions by dividing the CPU datapath into stages — typically Fetch, Decode, Execute, Memory, and Write-back — and processing a different instruction in each stage simultaneously. While the latency of a single instruction stays the same or increases slightly, throughput approaches one instruction completed per clock cycle (ideal CPI = 1). Pipelining is the primary reason RISC designs with uniform instruction formats are efficient; the fixed-length instruction encoding allows stage work to be balanced and pipelined cleanly.

## How It's Best Learned
Draw a pipeline timing diagram for a 5-stage pipeline executing 8 instructions. Count total cycles and compute CPI. Compare to a non-pipelined processor executing the same sequence. Identify how stage boundaries in the datapath require pipeline registers to hold intermediate values.

## Common Misconceptions
- Pipelining does not speed up individual instructions; it speeds up the throughput of many instructions executing in parallel.
- A deeper pipeline does not always mean more performance; each stage boundary adds pipeline register latency and increases exposure to hazard penalties.

## Explainer

You already understand the CPU datapath — the hardware that fetches an instruction, decodes it, executes it through the ALU, accesses memory if needed, and writes the result back to a register. In a simple non-pipelined processor, these five steps happen sequentially for each instruction: the entire datapath sits idle while one stage does its work, then the next stage takes over. Pipelining eliminates this waste by letting different instructions occupy different stages simultaneously, like an assembly line in a factory.

Imagine a laundry analogy: washing takes 30 minutes, drying takes 30 minutes, and folding takes 30 minutes. Without pipelining, you finish one load completely (90 minutes) before starting the next. With pipelining, you start washing load 2 as soon as load 1 moves to the dryer, and start washing load 3 when load 2 moves to the dryer and load 1 moves to folding. After the initial fill-up time, you complete one load every 30 minutes instead of every 90. The **throughput** triples even though each individual load still takes 90 minutes (**latency** is unchanged). This is exactly what happens in a pipelined CPU: after the pipeline fills, one instruction completes every clock cycle.

The classic **five-stage pipeline** divides execution into **Instruction Fetch (IF)**, **Instruction Decode (ID)**, **Execute (EX)**, **Memory Access (MEM)**, and **Write Back (WB)**. Between each stage, **pipeline registers** capture and hold the intermediate results — the fetched instruction bits, the decoded register values, the ALU output, the memory read data — so that each stage can work independently on its own instruction. The clock period is set by the slowest stage, not the total path length. If the longest stage takes 200 picoseconds instead of the 800-picosecond total path, the clock runs roughly four times faster, and throughput improves correspondingly.

Pipelining works best when every instruction follows the same format and takes the same stages — which is exactly the design philosophy of **RISC** (Reduced Instruction Set Computer) architectures. Fixed-length instructions mean the fetch stage always knows where the next instruction starts. Uniform instruction formats mean the decode stage always finds register specifiers in the same bit positions. This regularity keeps the pipeline stages balanced and simple. CISC architectures like x86, with variable-length instructions and complex addressing modes, must work much harder to achieve efficient pipelining, often by translating complex instructions into simpler micro-operations internally.

The ideal of one instruction per cycle is disrupted by **pipeline hazards** — situations where the next instruction cannot proceed because it depends on a result still moving through the pipeline. These hazards (data, control, and structural) are a direct consequence of overlapping execution, and managing them is the central challenge of pipelined processor design. But even with hazard penalties, pipelining delivers such dramatic throughput improvements that every modern processor uses it. The five-stage pipeline is the foundation; real processors extend it to 10, 15, or even 20+ stages to push clock speeds higher, trading increased hazard complexity for faster clocks.
