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
