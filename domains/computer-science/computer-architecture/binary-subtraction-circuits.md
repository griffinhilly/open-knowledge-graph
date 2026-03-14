---
id: binary-subtraction-circuits
title: Binary Subtraction Using Two's Complement
domain: computer-science
course: computer-architecture
prerequisites:
- id: twos-complement
  type: hard
- id: full-adder-circuit-design
  type: hard
tags:
- subtraction
- arithmetic-circuits
stage: formal-systems
status: draft
---

# Binary Subtraction Using Two's Complement

## Core Idea
Subtraction is implemented by negating the subtrahend (inverting bits and adding 1) then adding. This unifies subtraction and addition in hardware, requiring only one arithmetic unit.
