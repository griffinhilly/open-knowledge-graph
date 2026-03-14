---
id: binary-adders
title: 'Binary Adders: Half-Adders and Full-Adders'
domain: computer-science
course: computer-architecture
prerequisites:
- id: adder-circuits
  type: hard
- id: boolean-algebra-and-laws
  type: soft
builds-toward:
- arithmetic-logic-units-design
- fixed-point-number-representation
tags:
- adders
- binary
- arithmetic
stage: formal-systems
status: draft
---

# Binary Adders: Half-Adders and Full-Adders

## Core Idea
Half-adders add two bits without carry-in; full-adders add three bits (two operands plus carry-in). Cascading full-adders creates ripple-carry adders for multi-bit addition, the basis of arithmetic in processors.
