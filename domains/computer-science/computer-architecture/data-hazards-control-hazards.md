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

## Questions

```yaml
- question: "Consider the sequence: ADD R1, R2, R3 followed immediately by SUB R4, R1, R5. In a 5-stage pipeline with full data forwarding, how many stall cycles does the processor insert?"
  type: multiple-choice
  options:
    - "2 stall cycles — ADD must complete write-back before SUB can read R1"
    - "1 stall cycle — the result needs one extra cycle to propagate"
    - "0 stall cycles — forwarding routes ADD's ALU output directly to SUB's ALU input"
    - "It depends on whether the operands are in cache"
  answer: 2
  explanation: "With data forwarding, the result of ADD is available at the ALU output before it is written to the register file. The hardware routes this value directly to SUB's execute stage input — eliminating the stall entirely. Without forwarding, SUB would read the stale value of R1. This is the core purpose of forwarding: converting what would be a 2-cycle stall into a 0-cycle stall for most RAW hazards."

- question: "Consider the sequence: LOAD R1, [address] followed immediately by ADD R4, R1, R5. With a full forwarding network, how many stall cycles are needed?"
  type: multiple-choice
  options:
    - "0 — forwarding eliminates all data hazards"
    - "1 — the load result is not available until after memory access, one stage later than ALU results"
    - "2 — load instructions always require two extra cycles"
    - "3 — the pipeline must fully drain before continuing"
  answer: 1
  explanation: "This is a load-use hazard. Unlike an ALU instruction whose result is available at the end of the execute stage, a LOAD instruction's result is not available until the end of the memory access stage — one cycle later. Even with forwarding, the ADD instruction would need the value before it is ready. The processor must insert one stall (bubble) cycle to let the load complete memory access before ADD can proceed. This is the one case where forwarding cannot eliminate the stall."

- question: "Not every data dependency between adjacent instructions in a pipeline causes a hazard — only dependencies where the dependent instruction needs a result before it has been written."
  type: true-false
  answer: true
  explanation: "A data dependency only becomes a hazard if the pipeline stages overlap in a way that causes the dependent instruction to read a value before the producing instruction has written it. With forwarding, many RAW dependencies are resolved without any stall. Additionally, instructions far enough apart in the sequence may naturally avoid hazards because the producer has already written back by the time the consumer reads. Not every dependency is a hazard — the stage timing determines whether a conflict actually occurs."

- question: "Data forwarding eliminates all data hazards in a pipelined processor."
  type: true-false
  answer: false
  explanation: "Forwarding eliminates most RAW (read-after-write) hazards but not all. The load-use hazard is the classic exception: a LOAD instruction's result is not available until after the memory stage, so a dependent instruction that follows immediately needs to stall for one cycle regardless of forwarding. Additionally, forwarding cannot help with structural hazards (competing for the same hardware resource simultaneously) or control hazards (branches)."

- question: "Why does a control hazard occur in a pipelined processor, and what is the fundamental difficulty in resolving it compared to data hazards?"
  type: short-answer
  answer: "A control hazard occurs because the processor fetches instructions after a branch before knowing whether the branch is taken. By the time the branch outcome is determined (at the execute stage), one or more instructions have been fetched and partially executed — if the branch is taken, those instructions are wrong and must be flushed. Unlike data hazards, where forwarding can supply the needed value, control hazards require knowing the future: which instruction to fetch next is unknown until the branch resolves. Solutions involve accepting the flush penalty, static prediction (assume not-taken), or dynamic branch prediction."
  explanation: "Data hazards are about value availability — forwarding solves them by routing data early. Control hazards are about instruction flow — there is no equivalent of 'forwarding' because the needed information (branch direction) does not exist yet when the fetch decision must be made. This is why branch prediction is a probabilistic strategy rather than a deterministic fix, and why mispredictions are expensive."
```

## Explainer

From your study of instruction pipelining, you know that a pipelined processor overlaps the execution of multiple instructions — while one instruction is being executed, the next is being decoded, and the one after that is being fetched. This overlap is what gives pipelines their throughput advantage. But it also creates a fundamental problem: what happens when one instruction depends on the result of another instruction that has not finished yet? These situations are called **hazards**, and they fall into two main categories.

**Data hazards** arise from dependencies between instructions' operands. The most common type is **read-after-write** (RAW): instruction B reads a register that instruction A writes, but A has not yet reached the write-back stage when B needs the value in the decode or execute stage. Consider `ADD R1, R2, R3` followed immediately by `SUB R4, R1, R5`. The SUB needs R1, but ADD will not write its result to the register file for two more cycles. Without intervention, SUB would read the old, stale value of R1. Two other types exist: **write-after-read** (WAR), where a later instruction writes a register before an earlier instruction reads it, and **write-after-write** (WAW), where two instructions write the same register and their order must be preserved. WAR and WAW hazards are rare in simple in-order pipelines but become significant in out-of-order execution.

The simplest solution is **stalling** (inserting pipeline bubbles) — the processor pauses the dependent instruction until its operand is available. But stalling wastes cycles. A more efficient solution is **data forwarding** (also called bypassing): the result of ADD is available at the output of the ALU before it is written to the register file, so the hardware can route it directly to SUB's ALU input through a forwarding path. This eliminates the stall entirely for many RAW hazards. However, forwarding cannot solve every case — a load instruction, for instance, does not have its result until the end of the memory access stage, so a dependent instruction may still need to stall for one cycle (a **load-use hazard**).

**Control hazards** arise from branches. When the processor fetches a conditional branch, it does not know the outcome until the branch condition is evaluated, typically in the execute stage. By that time, the pipeline has already fetched one or more instructions after the branch — but if the branch is taken, those instructions are wrong and must be flushed. This penalty — wasted cycles from fetched-then-discarded instructions — is the control hazard. Simple solutions include always stalling until the branch resolves (costly), assuming the branch is not taken and flushing if wrong, or **delayed branching** (filling the slot after the branch with a useful instruction). More advanced processors use **branch prediction** to guess the outcome and speculatively execute the predicted path, recovering if the guess is wrong.
