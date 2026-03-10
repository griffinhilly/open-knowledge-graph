---
id: memory-organization
title: Memory Organization and Addressing
domain: computer-science
course: computer-architecture
prerequisites:
- id: binary-number-system
  type: hard
- id: hexadecimal-number-system
  type: soft
builds-toward:
- memory-hierarchy-overview
- cache-memory-design
- virtual-memory-basics
tags:
- memory
- addressing
- byte-ordering
- address-space
- endianness
stage: formal-systems
status: draft
---

# Memory Organization and Addressing

## Core Idea
Memory in a computer system is organized as an array of addressable locations, each identified by a unique binary address. The address space size is determined by the address bus width: a 32-bit address bus can address 2^32 ≈ 4 GB. Memory is typically byte-addressable, meaning each address refers to one byte even when words are larger. Byte ordering (endianness) determines whether multi-byte values store the most significant byte at the lowest address (big-endian) or highest address (little-endian), affecting data interchange and debugging.

## How It's Best Learned
Draw a memory map of a small address space and identify regions for code, data, and stack. Compare big-endian and little-endian storage of a 4-byte integer. Examine how array indexing translates to memory addresses in a low-level language like C.

## Common Misconceptions
- Memory addresses in programs are not physical hardware locations; modern systems use virtual addresses translated to physical addresses by hardware.
- Byte-addressable memory does not mean every byte is independently accessed — processors typically read and write full words at aligned addresses for efficiency.
