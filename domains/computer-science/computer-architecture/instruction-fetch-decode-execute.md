---
id: instruction-fetch-decode-execute
title: Instruction Fetch-Decode-Execute Cycle
domain: computer-science
course: computer-architecture
prerequisites:
- id: instruction-set-architecture
  type: hard
- id: cpu-datapath
  type: soft
builds-toward:
- instruction-pipeline-organization
- cpu-control-path-design
tags:
- instruction
- fetch
- decode
- execute
- cycle
stage: formal-systems
status: draft
---

# Instruction Fetch-Decode-Execute Cycle

## Core Idea
Every instruction passes through three main stages: fetching from memory, decoding to determine operation and operand addresses, and executing the operation. This cycle forms the heartbeat of the processor.

## How It's Best Learned
Trace a sample instruction (e.g., ADD R1, R2, R3) through each stage, observing which control signals activate and how data flows.

## Common Misconceptions
Different instructions may have different cycle counts in real processors. Memory fetch and execution are not always single-cycle operations.
