---
id: overflow-underflow-arithmetic
title: Overflow and Underflow Detection
domain: computer-science
course: computer-architecture
prerequisites:
- id: twos-complement
  type: hard
- id: binary-arithmetic
  type: hard
tags:
- arithmetic
- error-detection
stage: formal-systems
status: draft
---

# Overflow and Underflow Detection

## Core Idea
Overflow occurs when an arithmetic result exceeds the maximum representable value. In two's complement, overflow is detected by comparing input and output signs—a sum of two positive numbers should not be negative.
