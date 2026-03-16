---
id: multiplexer-circuits
title: Multiplexers and Demultiplexers
domain: computer-science
course: computer-architecture
prerequisites:
- id: combinational-logic-implementation
  type: hard
- id: binary-number-system
  type: soft
builds-toward:
- barrel-shifter-design
- memory-address-decoding
tags:
- multiplexing
- data-selection
- routing
stage: formal-systems
status: draft
---

# Multiplexers and Demultiplexers

## Core Idea
A multiplexer (MUX) selects one of many inputs based on control signals (select lines), while a demultiplexer routes a single input to one of many outputs. An n-to-1 multiplexer needs log₂(n) select lines. These are fundamental for routing data and are used in ALUs, memory addressing, and register selection.

## Explainer

From your work with combinational logic, you know how to build circuits that produce outputs based purely on current inputs using AND, OR, and NOT gates. A **multiplexer** (MUX) is one of the most useful combinational circuits you can build — think of it as a digitally controlled switch. Just as a railroad switch routes a train onto one of several tracks, a multiplexer routes one of several data inputs to a single output, controlled by a set of **select lines**.

A 4-to-1 multiplexer has four data inputs (D0, D1, D2, D3), two select lines (S1, S0), and one output. The binary value on the select lines determines which input passes through. If S1S0 = 10 (binary for 2), the output equals D2. Internally, each data input is ANDed with a unique combination of select signals (using the same minterm logic you learned in combinational implementation), and all the AND gate outputs are ORed together. The general pattern is that an **n-to-1 MUX** needs exactly log₂(n) select lines — a 2-to-1 needs 1, an 8-to-1 needs 3, a 16-to-1 needs 4.

A **demultiplexer** (DEMUX) does the reverse: it takes a single input and routes it to one of many outputs based on the select lines. You can think of a MUX as a funnel (many sources, one destination) and a DEMUX as a sprinkler (one source, many destinations). A DEMUX is structurally identical to a decoder with an enable input — when the enable is tied to the data input, the decoder becomes a demultiplexer.

These circuits appear everywhere in processor design. In an ALU, a multiplexer selects which operation's result to output (addition, subtraction, AND, OR) based on control signals from the instruction decoder. In a register file, multiplexers choose which register's contents to read. In memory systems, multiplexers and demultiplexers route data to and from the correct memory bank. Larger multiplexers are often built hierarchically from smaller ones — a 16-to-1 MUX can be constructed from five 4-to-1 MUXes — which makes them scalable building blocks for complex data routing throughout a computer.
