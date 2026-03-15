---
id: hexadecimal-number-system
title: Hexadecimal Number System
domain: computer-science
course: computer-architecture
prerequisites: []
builds-toward:
- memory-organization
- assembly-language-basics
tags:
- hexadecimal
- number-systems
- representation
stage: formal-systems
status: validated
---

# Hexadecimal Number System

## Core Idea
Hexadecimal (base-16) uses digits 0–9 and letters A–F to represent values 0–15 in a single digit position. It is widely used in computing because each hex digit corresponds exactly to 4 binary bits (a nibble), making it a compact and readable shorthand for binary data. Memory addresses, color codes, and machine code are commonly expressed in hexadecimal. Converting between hex and binary is straightforward: replace each hex digit with its 4-bit binary equivalent.

## How It's Best Learned
Memorize the hex-to-binary mapping for 0–F. Practice converting byte values (8-bit = 2 hex digits) between all three bases. Read and interpret memory dumps and color codes expressed in hex.

## Common Misconceptions
- Hexadecimal is not a separate 'special' system — it is just base-16 with the same place-value logic as any positional system.
- The letters A–F are not arbitrary; they are the conventional symbols for decimal 10–15.
