---
id: decoders-multiplexers
title: Decoders, Encoders, and Multiplexers
domain: computer-science
course: computer-architecture
prerequisites:
- id: universal-logic-gates
  type: hard
- id: combinational-circuit-design
  type: soft
builds-toward:
- memory-array-organization
- instruction-fetch-decode-execute
tags:
- decoders
- encoders
- multiplexers
- combinational
stage: formal-systems
status: draft
---

# Decoders, Encoders, and Multiplexers

## Core Idea
Decoders convert binary input to one-hot output (one wire high per input code), encoders do the reverse, and multiplexers select one of many inputs based on a control signal. These are fundamental selection and routing components in memory and CPU design.

## How It's Best Learned
Design 2-to-4 decoder and 4-to-1 multiplexer from gates; observe how they scale to larger widths.

## Common Misconceptions
A decoder activates exactly one output for each input. Encoders assume only one input is high at a time. Multiplexers are data routers, not logic gates.

## Explainer

You've built circuits from universal logic gates — AND, OR, NOT, NAND, NOR — and you understand how to combine them into useful combinational circuits. **Decoders**, **encoders**, and **multiplexers** are the next level of abstraction: standardized building blocks that route and select signals, appearing everywhere in processor and memory design. Think of them as the addressing and switching infrastructure that connects everything else together.

A **decoder** takes an n-bit binary input and activates exactly one of 2^n output lines. A 2-to-4 decoder, for example, has 2 input bits and 4 output lines. If the input is 10 (binary 2), output line 2 goes high while all others stay low. Internally, each output is just an AND gate combining the appropriate mix of true and complemented inputs. Output 2 (input = 10) is driven by A_1 AND (NOT A_0). The decoder essentially answers the question: "which number does this binary code represent?" This is exactly what happens in memory: when you supply a memory address, a decoder activates the one row or column that matches, allowing data to be read from or written to that specific location.

An **encoder** performs the reverse operation: given 2^n input lines where exactly one is active, it produces the n-bit binary code identifying which line is high. A 4-to-2 encoder takes 4 inputs and outputs 2 bits. If input line 3 is high, the output is 11. **Priority encoders** handle the case where multiple inputs might be active simultaneously — they output the code for the highest-priority (typically highest-numbered) active input and include a "valid" output indicating whether any input is active at all. Interrupt controllers in CPUs use priority encoders to determine which pending interrupt to service first.

A **multiplexer** (mux) is a data selector: it has 2^n data inputs, n select lines, and one output. The select lines choose which data input passes through to the output — like a railroad switch that connects one of several tracks to a single main line. A 4-to-1 mux has 4 data inputs (D0–D3), 2 select bits (S1, S0), and routes D_S to the output. Internally, each data input is ANDed with the appropriate select combination (using a decoder pattern), and all results are ORed together. Multiplexers are fundamental in CPU datapaths — the ALU's input mux selects whether data comes from a register, an immediate value, or memory; the register file's output uses muxes to select which register to read. A key insight is that any Boolean function of n variables can be implemented using a 2^n-to-1 mux by hardwiring the data inputs to 0 or 1, making multiplexers a universal building block in their own right.
