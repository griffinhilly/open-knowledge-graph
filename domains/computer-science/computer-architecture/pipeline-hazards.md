---
id: pipeline-hazards
title: Pipeline Hazards
domain: computer-science
course: computer-architecture
prerequisites:
- id: pipelining-fundamentals
  type: hard
tags:
- data-hazard
- control-hazard
- structural-hazard
- forwarding
- stall
- branch-prediction
stage: formal-systems
status: validated
---

# Pipeline Hazards

## Core Idea
Pipeline hazards are conditions that prevent the next instruction from executing in its scheduled stage, reducing throughput below ideal. Structural hazards arise when two instructions need the same hardware resource simultaneously. Data hazards occur when an instruction depends on a result not yet written back by a prior instruction. Control hazards arise from branches: the next instruction to execute is not known until the branch resolves. Solutions include pipeline stalls (bubbles), data forwarding (routing results earlier in the pipeline), branch prediction, and delayed branching.

## How It's Best Learned
Trace data hazards in a sequence like 'ADD R1,R2,R3; SUB R4,R1,R5' through a pipeline diagram and identify which cycles require stalls or forwarding. Model a branch misprediction and count the penalty cycles. Compare the CPI impact of each hazard type.

## Common Misconceptions
- Data forwarding does not eliminate all stalls — a load-use hazard (load immediately followed by use of the loaded value) still requires one stall even with full forwarding.
- Branch prediction misses are not errors; they are expected events that the pipeline handles by flushing incorrect instructions and restarting from the correct path.

## Explainer

From pipelining fundamentals, you know the core idea: break instruction execution into stages (fetch, decode, execute, memory access, write-back) and overlap them so multiple instructions are in flight simultaneously. In an ideal 5-stage pipeline, you complete one instruction per clock cycle after the pipeline fills. But this ideal throughput assumes every instruction can enter the pipeline on schedule — **pipeline hazards** are the situations where that assumption breaks down.

**Structural hazards** are the simplest to understand: two instructions need the same hardware at the same time. Imagine a pipeline where instruction fetch and data memory access both use a single shared memory port. If instruction 3 is fetching while instruction 1 is reading data from memory, they collide. The fix is usually to duplicate the resource — separate instruction and data caches (a Harvard-style memory) eliminate this particular structural hazard entirely. Where duplication is too expensive, the pipeline inserts a **stall** (also called a bubble): one instruction waits a cycle while the other uses the resource.

**Data hazards** are more subtle and more common. Consider two instructions in sequence: `ADD R1, R2, R3` followed by `SUB R4, R1, R5`. The SUB needs the value of R1, but ADD won't write its result to the register file until the write-back stage — three cycles after it produces the result in the execute stage. If SUB tries to read R1 during its decode stage, it gets the old, stale value. The simplest fix is stalling: freeze SUB for two cycles until R1 is updated. But a much better solution is **data forwarding** (also called bypassing): since the ADD's result is actually computed at the end of the execute stage, the hardware can route it directly back to the SUB's execute input, bypassing the register file entirely. Forwarding eliminates most data hazard stalls, but not all — a **load-use hazard** (where a load instruction is immediately followed by an instruction using the loaded value) still requires one stall cycle because the data isn't available until the memory access stage.

**Control hazards** arise from branches. When the pipeline fetches a conditional branch instruction, it doesn't know which instruction comes next until the branch condition is evaluated — potentially several stages later. Every cycle spent waiting is a wasted slot. **Branch prediction** addresses this by guessing the branch outcome and speculatively fetching instructions along the predicted path. If the guess is correct, the pipeline runs at full speed. If the guess is wrong, the speculatively fetched instructions must be **flushed** (discarded), and the pipeline restarts from the correct address — this penalty is typically 2-3 cycles in a simple pipeline, but can be much more in deeper pipelines. Modern processors use sophisticated predictors that achieve over 95% accuracy, making branch mispredictions relatively rare but still one of the most significant sources of lost performance.
