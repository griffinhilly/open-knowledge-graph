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
status: validated
---

# Multiplexers and Demultiplexers

## Core Idea
A multiplexer (MUX) selects one of many inputs based on control signals (select lines), while a demultiplexer routes a single input to one of many outputs. An n-to-1 multiplexer needs log₂(n) select lines. These are fundamental for routing data and are used in ALUs, memory addressing, and register selection.

## Questions

```yaml
- question: "How many select lines does a 16-to-1 multiplexer require?"
  type: multiple-choice
  options:
    - "2 select lines"
    - "4 select lines"
    - "8 select lines"
    - "16 select lines"
  answer: 1
  explanation: "An n-to-1 multiplexer requires log₂(n) select lines. For 16 inputs: log₂(16) = 4 select lines. These 4 lines can encode 2⁴ = 16 unique binary patterns, one for each possible input selection. A common mistake is to think you need one select line per input (16), but that would require 16 extra control signals — the whole point of the select lines is to encode the selection efficiently in binary."

- question: "An ALU outputs four operation results: ADD on wire D0, SUB on wire D1, AND on wire D2, OR on wire D3. A 4-to-1 multiplexer routes one result to the output based on a 2-bit opcode. If the opcode is 10 (binary), which operation's result appears at the output?"
  type: multiple-choice
  options:
    - "ADD (D0) — the leading bit selects the first input"
    - "SUB (D1) — binary 10 equals decimal 1"
    - "AND (D2) — binary 10 equals decimal 2"
    - "OR (D3) — the most significant bit is 1, selecting the upper half"
  answer: 2
  explanation: "The select lines form a binary number that directly indexes the data input. Binary 10 = decimal 2, so D2 (the AND result) is selected. This is exactly how ALUs use multiplexers: the instruction's opcode bits drive the MUX select lines, and the MUX routes the appropriate operation's result to the next stage. Option B is wrong because binary 10 is 2, not 1 (that would be binary 01). Option D applies faulty intuition about the MSB — you must read the full binary value."

- question: "A demultiplexer takes multiple inputs and combines them into a single output signal."
  type: true-false
  answer: false
  explanation: "This describes a multiplexer (MUX), not a demultiplexer (DEMUX). A DEMUX does the reverse: it takes a SINGLE input and routes it to ONE of many outputs based on the select lines. MUX = many-to-one (funnel); DEMUX = one-to-many (sprinkler). A DEMUX is structurally equivalent to a decoder with an enable input — when the single input drives the enable, the selected output passes the signal while all others remain low."

- question: "A 4-to-1 multiplexer can be built from three 2-to-1 multiplexers arranged in a two-level tree."
  type: true-false
  answer: true
  explanation: "Yes — hierarchical construction is a standard technique. Two 2-to-1 MUXes in the first level each select between two of the four data inputs (D0/D1 and D2/D3), controlled by the low-order select bit S0. A third 2-to-1 MUX in the second level selects between the outputs of the first two, controlled by the high-order select bit S1. This same principle scales: a 16-to-1 MUX can be built from five 4-to-1 MUXes, enabling modular, scalable data routing."

- question: "Explain why a multiplexer is described as a 'digitally controlled switch' and how the select lines determine which data input passes through to the output."
  type: short-answer
  answer: "A multiplexer acts like a multi-position switch where the 'hand' turning the switch is a binary number on the select lines instead of a physical mechanism. Internally, each data input is ANDed with a unique combination of select signals (a minterm of the select variables), so exactly one AND gate is active at any time — the one whose select pattern matches the binary value on the select lines. All AND gate outputs are ORed together, so the single active AND gate passes its data input to the output while all other inputs are blocked (ANDed with 0). The select lines thus 'point' to one input by activating exactly one minterm, and that input's value appears at the output."
  explanation: "The key insight is that the select lines don't carry data — they carry an address that specifies which data line is connected to the output. This address decoding via minterms is the same logic used throughout processor design: instruction decoders, memory address decoders, and register file read ports all use this principle of using a binary code to select one of many options."
```

## Explainer

From your work with combinational logic, you know how to build circuits that produce outputs based purely on current inputs using AND, OR, and NOT gates. A **multiplexer** (MUX) is one of the most useful combinational circuits you can build — think of it as a digitally controlled switch. Just as a railroad switch routes a train onto one of several tracks, a multiplexer routes one of several data inputs to a single output, controlled by a set of **select lines**.

A 4-to-1 multiplexer has four data inputs (D0, D1, D2, D3), two select lines (S1, S0), and one output. The binary value on the select lines determines which input passes through. If S1S0 = 10 (binary for 2), the output equals D2. Internally, each data input is ANDed with a unique combination of select signals (using the same minterm logic you learned in combinational implementation), and all the AND gate outputs are ORed together. The general pattern is that an **n-to-1 MUX** needs exactly log₂(n) select lines — a 2-to-1 needs 1, an 8-to-1 needs 3, a 16-to-1 needs 4.

A **demultiplexer** (DEMUX) does the reverse: it takes a single input and routes it to one of many outputs based on the select lines. You can think of a MUX as a funnel (many sources, one destination) and a DEMUX as a sprinkler (one source, many destinations). A DEMUX is structurally identical to a decoder with an enable input — when the enable is tied to the data input, the decoder becomes a demultiplexer.

These circuits appear everywhere in processor design. In an ALU, a multiplexer selects which operation's result to output (addition, subtraction, AND, OR) based on control signals from the instruction decoder. In a register file, multiplexers choose which register's contents to read. In memory systems, multiplexers and demultiplexers route data to and from the correct memory bank. Larger multiplexers are often built hierarchically from smaller ones — a 16-to-1 MUX can be constructed from five 4-to-1 MUXes — which makes them scalable building blocks for complex data routing throughout a computer.
