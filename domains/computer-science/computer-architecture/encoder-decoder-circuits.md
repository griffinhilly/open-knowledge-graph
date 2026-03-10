---
id: encoder-decoder-circuits
title: Encoders, Decoders, and Priority Encoders
domain: computer-science
course: computer-architecture
prerequisites:
- id: combinational-circuit-design
  type: hard
builds-toward:
- cpu-datapath
- memory-organization
tags:
- encoder
- decoder
- combinational
- address-decoding
stage: formal-systems
status: draft
---

# Encoders, Decoders, and Priority Encoders

## Core Idea
A decoder takes an n-bit input and activates exactly one of 2^n output lines — used to select memory locations or I/O devices given an address. An encoder performs the inverse, converting one active input line into an n-bit code. A priority encoder handles multiple simultaneous inputs by encoding the highest-priority active line. These circuits are fundamental in memory addressing, instruction decoding, and interrupt handling in computer systems.

## How It's Best Learned
Design a 2-to-4 decoder and a 4-to-2 encoder from truth tables. Extend to a 3-to-8 decoder and verify all 8 output combinations. Build a simple priority encoder and trace its behavior when multiple inputs are simultaneously active.

## Common Misconceptions
- A decoder and a demultiplexer are closely related but not identical; a DEMUX routes a data signal while a decoder asserts selection lines based on an address.
- Decoders do not 'decode meaning' — they simply assert the selected output line corresponding to a binary address.
