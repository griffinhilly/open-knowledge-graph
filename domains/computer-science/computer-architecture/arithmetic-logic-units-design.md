---
id: arithmetic-logic-units-design
title: Arithmetic-Logic Unit (ALU) Design
domain: computer-science
course: computer-architecture
prerequisites:
- id: binary-adders
  type: hard
- id: arithmetic-logic-unit
  type: soft
builds-toward:
- cpu-datapath
- instruction-fetch-decode-execute
tags:
- alu
- arithmetic
- logic
- operations
stage: formal-systems
status: draft
---

# Arithmetic-Logic Unit (ALU) Design

## Core Idea
An ALU integrates multiple arithmetic and logical operations (add, subtract, AND, OR, shift, etc.) and uses control signals to select which operation to perform. It is the computational core of every CPU's datapath.

## How It's Best Learned
Design a simple ALU with 4 operations (add, subtract, AND, OR); trace through execution with sample inputs.

## Common Misconceptions
ALUs do not store state; they are purely combinational. Operation selection requires log₂(N) control bits for N operations.
