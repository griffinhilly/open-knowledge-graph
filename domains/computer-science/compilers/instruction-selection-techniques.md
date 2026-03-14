---
id: instruction-selection-techniques
title: Instruction Selection Techniques
domain: computer-science
course: compilers
prerequisites:
- id: code-generation
  type: hard
- id: procedure-inlining-optimization
  type: soft
- id: array-subscript-optimization
  type: soft
builds-toward:
- graph-coloring-register-allocation
- code-emission-target-generation
tags:
- code-generation
- backend
- instruction-selection
stage: advanced
status: draft
---

# Instruction Selection Techniques

## Core Idea
Instruction selection translates intermediate code into target machine instructions. One IR operation may correspond to many possible machine instructions, each with different costs and constraints. Pattern matching or dynamic programming finds good instruction sequences.

## How It's Best Learned
Implement pattern-based instruction selection for a real ISA subset. Write patterns as tree rules and test on realistic code.
