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
