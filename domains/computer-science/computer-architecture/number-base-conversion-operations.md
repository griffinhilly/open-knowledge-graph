---
id: number-base-conversion-operations
title: Converting Between Binary, Decimal, and Hexadecimal
domain: computer-science
course: computer-architecture
prerequisites:
- id: binary-number-system
  type: hard
- id: hexadecimal-number-system
  type: hard
builds-toward:
- instruction-encoding-and-machine-code
- memory-address-representation
tags:
- number-systems
- conversion
- radix
stage: formal-systems
status: draft
---

# Converting Between Binary, Decimal, and Hexadecimal

## Core Idea
Conversion between bases uses positional notation: any base-b number equals sum of (digit × b^position). Binary and hexadecimal are particularly related—every 4 binary digits map to 1 hex digit. Understanding these conversions is essential for reading machine code and memory addresses.
