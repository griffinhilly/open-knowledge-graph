---
id: binary-number-system
title: Binary Number System
domain: computer-science
course: computer-architecture
prerequisites:
- id: place-value-whole-numbers
  type: soft
builds-toward:
- hexadecimal-number-system
- binary-arithmetic
- twos-complement
tags:
- binary
- number-systems
- representation
stage: formal-systems
status: validated
---

# Binary Number System

## Core Idea
The binary number system uses only two digits (0 and 1) to represent all numbers, using powers of 2 as place values. Each digit position corresponds to 2^n for some n ≥ 0, so the binary number 1011 equals 1×8 + 0×4 + 1×2 + 1×1 = 11 in decimal. Computers use binary because electronic circuits naturally represent two states: on (1) and off (0). Converting between binary and decimal is a core skill for understanding how data is stored and processed.

## How It's Best Learned
Practice converting between binary and decimal in both directions. Start with small numbers (0–15) to build intuition about powers of 2, then extend to larger values. Use the doubling/halving method for quick conversions.

## Common Misconceptions
- Binary numbers are not just 'computer code' — they are a complete positional number system with the same arithmetic properties as decimal.
- Leading zeros do not change a binary number's value (0101 = 101) but are often written for alignment to fixed bit-widths.
