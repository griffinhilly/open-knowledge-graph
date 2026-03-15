---
id: register-allocation
title: Register Allocation
domain: computer-science
course: compilers
prerequisites:
- id: live-variable-analysis
  type: hard
- id: instruction-set-architecture
  type: soft
- id: graph-coloring
  type: hard
builds-toward:
- code-generation
tags:
- register-allocation
- code-generation
- architecture
stage: advanced
status: draft
---

# Register Allocation

## Core Idea
Register allocation assigns variables to CPU registers and memory locations. A variable can use a register if its live ranges don't overlap with other variables' (no two live variables can share a register). This is modeled as a graph coloring problem: variables are nodes, edges connect interfering variables, and colors are registers. Spilling (moving to memory) is required when coloring exceeds available registers.
