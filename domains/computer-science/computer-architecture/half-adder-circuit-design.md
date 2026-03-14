---
id: half-adder-circuit-design
title: Half Adder Circuit Design
domain: computer-science
course: computer-architecture
prerequisites:
- id: xor-equivalence-gates
  type: hard
- id: logic-gates-fundamentals
  type: hard
builds-toward:
- full-adder-circuit-design
tags:
- adder
- arithmetic-circuits
stage: formal-systems
status: draft
---

# Half Adder Circuit Design

## Core Idea
A half adder adds two single bits, producing sum (via XOR) and carry (via AND). It lacks a carry-in input, limiting use to the least significant bit of multi-bit addition.
