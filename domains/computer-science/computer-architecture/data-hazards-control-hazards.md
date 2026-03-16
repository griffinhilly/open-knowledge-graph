---
id: data-hazards-control-hazards
title: Hazards in Pipelined Processors
domain: computer-science
course: computer-architecture
prerequisites:
- id: instruction-pipeline-organization
  type: hard
- id: pipeline-hazards
  type: soft
builds-toward:
- branch-prediction-techniques
- out-of-order-execution-design
tags:
- hazards
- data
- control
- pipeline
stage: formal-systems
status: draft
---

# Hazards in Pipelined Processors

## Core Idea
Data hazards occur when an instruction depends on results not yet written (read-after-write, write-after-read, write-after-write); control hazards arise from branches. Stalling, forwarding, and speculation resolve these conflicts.

## How It's Best Learned
Identify hazards in a simple instruction sequence and trace how forwarding eliminates stalls.

## Common Misconceptions
Not all data dependencies cause hazards—only those that cross pipeline stages. Forwarding can eliminate many hazards without stalling.

## Explainer

From your study of instruction pipelining, you know that a pipelined processor overlaps the execution of multiple instructions — while one instruction is being executed, the next is being decoded, and the one after that is being fetched. This overlap is what gives pipelines their throughput advantage. But it also creates a fundamental problem: what happens when one instruction depends on the result of another instruction that has not finished yet? These situations are called **hazards**, and they fall into two main categories.

**Data hazards** arise from dependencies between instructions' operands. The most common type is **read-after-write** (RAW): instruction B reads a register that instruction A writes, but A has not yet reached the write-back stage when B needs the value in the decode or execute stage. Consider `ADD R1, R2, R3` followed immediately by `SUB R4, R1, R5`. The SUB needs R1, but ADD will not write its result to the register file for two more cycles. Without intervention, SUB would read the old, stale value of R1. Two other types exist: **write-after-read** (WAR), where a later instruction writes a register before an earlier instruction reads it, and **write-after-write** (WAW), where two instructions write the same register and their order must be preserved. WAR and WAW hazards are rare in simple in-order pipelines but become significant in out-of-order execution.

The simplest solution is **stalling** (inserting pipeline bubbles) — the processor pauses the dependent instruction until its operand is available. But stalling wastes cycles. A more efficient solution is **data forwarding** (also called bypassing): the result of ADD is available at the output of the ALU before it is written to the register file, so the hardware can route it directly to SUB's ALU input through a forwarding path. This eliminates the stall entirely for many RAW hazards. However, forwarding cannot solve every case — a load instruction, for instance, does not have its result until the end of the memory access stage, so a dependent instruction may still need to stall for one cycle (a **load-use hazard**).

**Control hazards** arise from branches. When the processor fetches a conditional branch, it does not know the outcome until the branch condition is evaluated, typically in the execute stage. By that time, the pipeline has already fetched one or more instructions after the branch — but if the branch is taken, those instructions are wrong and must be flushed. This penalty — wasted cycles from fetched-then-discarded instructions — is the control hazard. Simple solutions include always stalling until the branch resolves (costly), assuming the branch is not taken and flushing if wrong, or **delayed branching** (filling the slot after the branch with a useful instruction). More advanced processors use **branch prediction** to guess the outcome and speculatively execute the predicted path, recovering if the guess is wrong.
