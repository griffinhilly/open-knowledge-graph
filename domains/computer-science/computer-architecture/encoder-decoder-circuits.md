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
status: validated
---

# Encoders, Decoders, and Priority Encoders

## Core Idea
A decoder takes an n-bit input and activates exactly one of 2^n output lines — used to select memory locations or I/O devices given an address. An encoder performs the inverse, converting one active input line into an n-bit code. A priority encoder handles multiple simultaneous inputs by encoding the highest-priority active line. These circuits are fundamental in memory addressing, instruction decoding, and interrupt handling in computer systems.

## How It's Best Learned
Design a 2-to-4 decoder and a 4-to-2 encoder from truth tables. Extend to a 3-to-8 decoder and verify all 8 output combinations. Build a simple priority encoder and trace its behavior when multiple inputs are simultaneously active.

## Common Misconceptions
- A decoder and a demultiplexer are closely related but not identical; a DEMUX routes a data signal while a decoder asserts selection lines based on an address.
- Decoders do not 'decode meaning' — they simply assert the selected output line corresponding to a binary address.

## Explainer

From your study of combinational circuit design, you know how to build circuits whose outputs depend purely on their current inputs. Encoders and decoders are among the most practically important combinational circuits in computer architecture, and they perform complementary translations between two representations of information: a **one-hot** encoding (where exactly one line among many is active) and a **binary** encoding (a compact multi-bit code).

A **decoder** takes an *n*-bit binary input and activates exactly one of 2^n output lines. Think of it as an address translator: given the binary address `01`, a 2-to-4 decoder asserts output line 1 (the second line, counting from zero) and deasserts the other three. Internally, each output line is an AND gate that checks for a specific input pattern. Output 0 is AND(A', B'), output 1 is AND(A', B), output 2 is AND(A, B'), and output 3 is AND(A, B). Decoders are everywhere in computer systems — they select which memory chip responds to a given address, they activate the correct register in a register file, and inside the CPU's control unit, they decode instruction opcodes into control signals that drive the datapath.

An **encoder** performs the inverse operation: given 2^n input lines with exactly one active, it produces the *n*-bit binary code identifying which line is active. A 4-to-2 encoder with input line 2 active outputs `10`. The practical limitation of a simple encoder is that it assumes exactly one input is active at a time. When multiple inputs can be active simultaneously — as happens in interrupt systems where several devices may request attention at once — you need a **priority encoder**. A priority encoder assigns a fixed priority ordering to the input lines (typically higher-numbered inputs have higher priority) and outputs the binary code of the highest-priority active input, along with a "valid" bit indicating that at least one input is active.

These circuits compose naturally into larger systems. A 3-to-8 decoder can be built from two 2-to-4 decoders plus an inverter, using the third input bit to enable one decoder and disable the other. Similarly, decoders with enable inputs can be cascaded to build address decoding logic for an entire memory system: a top-level decoder selects which memory bank is active, and within each bank, a lower-level decoder selects the specific word line. This hierarchical composition means you rarely need to design a massive decoder from scratch — you build it from smaller, well-understood pieces, which is a recurring pattern in digital design.
