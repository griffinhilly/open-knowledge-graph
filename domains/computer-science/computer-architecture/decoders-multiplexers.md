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
status: validated
---

# Decoders, Encoders, and Multiplexers

## Core Idea
Decoders convert binary input to one-hot output (one wire high per input code), encoders do the reverse, and multiplexers select one of many inputs based on a control signal. These are fundamental selection and routing components in memory and CPU design.

## How It's Best Learned
Design 2-to-4 decoder and 4-to-1 multiplexer from gates; observe how they scale to larger widths.

## Common Misconceptions
A decoder activates exactly one output for each input. Encoders assume only one input is high at a time. Multiplexers are data routers, not logic gates.

## Questions

```yaml
- question: "A 3-to-8 decoder receives input 101 (binary 5). Which output line goes high?"
  type: multiple-choice
  options:
    - "Output lines 1, 0, and 1 go high (matching each input bit)"
    - "Output line 5 goes high; all others remain low"
    - "Output lines 5, 4, and 1 go high (corresponding to active input bits)"
    - "All 8 output lines briefly pulse high before settling"
  answer: 1
  explanation: "A decoder produces a one-hot output — exactly one line high per input code. Input 101 (binary) equals 5, so output line 5 goes high and all 7 others stay low. This 'one line high' property is the entire point of a decoder: it answers 'which number does this binary code represent?' and activates only that line. Option A confuses the input bit pattern with multiple simultaneous outputs; option C confuses which bits are '1' in the input with which output lines activate."

- question: "How does a 4-to-1 multiplexer differ functionally from a 2-to-4 decoder?"
  type: multiple-choice
  options:
    - "A multiplexer converts binary codes to one-hot; a decoder routes one input to many outputs"
    - "A multiplexer routes one of several DATA inputs to a single output based on select lines; a decoder maps a binary code to exactly one active output line"
    - "A multiplexer is a sequential circuit; a decoder is purely combinational"
    - "A decoder requires more input lines than a multiplexer of equivalent size"
  answer: 1
  explanation: "A decoder is an address-to-one-hot converter: it takes n binary bits and activates one of 2^n output lines. A multiplexer is a data router: it has 2^n data inputs, n select lines, and steers exactly one of the data inputs through to the output. The select lines work like a decoder internally (choosing which data input to activate), but the output is the selected DATA, not a one-hot line. A decoder answers 'which one?'; a mux answers 'pass this one through.'"

- question: "A 3-to-8 decoder with input 101 activates three output lines simultaneously — one for each bit that is '1' in the input."
  type: true-false
  answer: false
  explanation: "Decoders produce one-hot output: exactly ONE output line goes high per input code, regardless of how many bits in the input are '1'. Input 101 (= 5) activates only output line 5. The internal logic of each output gate is an AND of the appropriate combination of true and complemented inputs — output 5 fires when A2=1, A1=0, A0=1 simultaneously, i.e., only for the complete input pattern 101. No other output can fire for that same input."

- question: "Any Boolean function of n inputs can be implemented using a 2^n-to-1 multiplexer by hardwiring its data inputs to 0 or 1."
  type: true-false
  answer: true
  explanation: "This is one of the most powerful properties of multiplexers. A 2^n-to-1 mux has one data input for each possible combination of the n select-line inputs. For any desired Boolean function, simply look up each row of the truth table: if the function outputs 1 for that input combination, tie that data input to 1; if 0, tie it to 0. The select lines then route the appropriate constant to the output, implementing the full truth table. This makes a large mux a universal combinational building block."

- question: "Explain how a decoder implements memory row addressing. What specific property of decoder output makes it suitable for this purpose?"
  type: short-answer
  answer: "A decoder takes the binary memory address and activates exactly one output line — the one corresponding to that address. This one-hot property ensures that only a single memory row's word line goes high, enabling read/write access to only that row while all other rows remain inactive. If multiple output lines could go high simultaneously, multiple rows would be accessed at once, corrupting data. The decoder guarantees mutual exclusion: for any n-bit address, exactly one of 2^n rows is selected."
  explanation: "Memory arrays are organized as a grid of rows and columns. The row decoder maps the upper bits of the address to a single word line; a column decoder or multiplexer handles the lower bits to select specific bit(s) within that row. The key requirement is that the address space be partitioned without overlap — exactly the property a decoder provides. Without one-hot output, any address would activate multiple rows, making targeted read/write impossible."
```

## Explainer

You've built circuits from universal logic gates — AND, OR, NOT, NAND, NOR — and you understand how to combine them into useful combinational circuits. **Decoders**, **encoders**, and **multiplexers** are the next level of abstraction: standardized building blocks that route and select signals, appearing everywhere in processor and memory design. Think of them as the addressing and switching infrastructure that connects everything else together.

A **decoder** takes an n-bit binary input and activates exactly one of 2^n output lines. A 2-to-4 decoder, for example, has 2 input bits and 4 output lines. If the input is 10 (binary 2), output line 2 goes high while all others stay low. Internally, each output is just an AND gate combining the appropriate mix of true and complemented inputs. Output 2 (input = 10) is driven by A_1 AND (NOT A_0). The decoder essentially answers the question: "which number does this binary code represent?" This is exactly what happens in memory: when you supply a memory address, a decoder activates the one row or column that matches, allowing data to be read from or written to that specific location.

An **encoder** performs the reverse operation: given 2^n input lines where exactly one is active, it produces the n-bit binary code identifying which line is high. A 4-to-2 encoder takes 4 inputs and outputs 2 bits. If input line 3 is high, the output is 11. **Priority encoders** handle the case where multiple inputs might be active simultaneously — they output the code for the highest-priority (typically highest-numbered) active input and include a "valid" output indicating whether any input is active at all. Interrupt controllers in CPUs use priority encoders to determine which pending interrupt to service first.

A **multiplexer** (mux) is a data selector: it has 2^n data inputs, n select lines, and one output. The select lines choose which data input passes through to the output — like a railroad switch that connects one of several tracks to a single main line. A 4-to-1 mux has 4 data inputs (D0–D3), 2 select bits (S1, S0), and routes D_S to the output. Internally, each data input is ANDed with the appropriate select combination (using a decoder pattern), and all results are ORed together. Multiplexers are fundamental in CPU datapaths — the ALU's input mux selects whether data comes from a register, an immediate value, or memory; the register file's output uses muxes to select which register to read. A key insight is that any Boolean function of n variables can be implemented using a 2^n-to-1 mux by hardwiring the data inputs to 0 or 1, making multiplexers a universal building block in their own right.
