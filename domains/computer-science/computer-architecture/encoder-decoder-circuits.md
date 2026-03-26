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

## Questions

```yaml
- question: "A 3-to-8 decoder receives the binary input 101. Which output line is activated?"
  type: multiple-choice
  options:
    - "Output line 3"
    - "Output line 4"
    - "Output line 5"
    - "Output lines 1, 3, and 5 simultaneously — one for each active input bit"
  answer: 2
  explanation: "A 3-to-8 decoder interprets its 3-bit input as a binary number and activates exactly one of 8 output lines. 101 in binary equals 5 in decimal, so output line 5 is asserted and all others are deasserted. Option D represents the key misconception: the decoder does not activate one output per set input bit. It activates the single output corresponding to the binary address. The entire point of a decoder is the translation from compact binary encoding to one-hot selection."

- question: "A computer system has 8 peripheral devices that may simultaneously generate interrupt signals. What type of circuit is needed to produce a 3-bit code identifying which interrupt to service?"
  type: multiple-choice
  options:
    - "A 3-to-8 decoder"
    - "A basic 8-to-3 encoder"
    - "A priority encoder"
    - "A multiplexer with a 3-bit select"
  answer: 2
  explanation: "A basic 8-to-3 encoder assumes exactly one input is active at a time — if multiple inputs assert simultaneously, its output is undefined or incorrect. Since multiple interrupt sources can fire at once, a priority encoder is required: it accepts multiple simultaneous inputs, selects the highest-priority active one, and outputs its 3-bit binary code along with a 'valid' signal. This is precisely the interrupt controller's job in real systems, and why priority encoders are a standard building block for interrupt handling."

- question: "A basic 4-to-2 encoder will produce incorrect output if two or more of its input lines are simultaneously asserted."
  type: true-false
  answer: true
  explanation: "True. A simple encoder is designed assuming exactly one of its 2^n input lines is active at any time. Its output lines are ORed together in ways that only produce a valid binary code for single-active-input scenarios. When two inputs are simultaneously active, their OR-combined outputs produce a code that may correspond to neither active input — it could be the code of a third, inactive input. Priority encoders solve this by using additional logic to identify and encode only the highest-priority active input."

- question: "A decoder and a demultiplexer perform identical functions and can usually be used interchangeably in digital circuit design."
  type: true-false
  answer: false
  explanation: "False. A decoder and a demultiplexer are closely related but functionally distinct. A decoder takes an n-bit binary address and asserts the corresponding one-of-2^n output line — it translates an address into a selection. A demultiplexer routes a single data input signal to one of several output lines selected by a control address. The difference is that a DEMUX carries a data value through to the selected output, while a decoder simply asserts or deasserts selection lines. A decoder can be used as a DEMUX by treating the enable pin as the data input, but they are not interchangeable in general."

- question: "Explain the complementary relationship between encoders and decoders in terms of what information each converts and to what representation, and give one practical application of each in a computer system."
  type: short-answer
  answer: "A decoder takes a compact binary code (n bits) and produces a one-hot output (exactly one of 2^n lines active) — it expands a binary address into a selection signal. An encoder does the inverse: given one active line among many, it produces the compact binary code identifying which line is active. Practical decoder application: memory address decoding — a 3-to-8 decoder selects which of 8 RAM chips responds to a given address bus value. Practical encoder application: keyboard encoding — when a key is pressed, an encoder converts the active key line into a binary scancode the CPU can process."
  explanation: "The complementary nature is fundamental to how data moves between binary-coded formats (used for compact storage and transmission) and one-hot formats (used for direct hardware selection and activation). CPU instruction decoding uses decoders to translate opcode bits into control signals that activate specific datapath components. Interrupt controllers use priority encoders to convert multiple simultaneous interrupt lines into a single prioritized interrupt number."
```

## Explainer

From your study of combinational circuit design, you know how to build circuits whose outputs depend purely on their current inputs. Encoders and decoders are among the most practically important combinational circuits in computer architecture, and they perform complementary translations between two representations of information: a **one-hot** encoding (where exactly one line among many is active) and a **binary** encoding (a compact multi-bit code).

A **decoder** takes an *n*-bit binary input and activates exactly one of 2^n output lines. Think of it as an address translator: given the binary address `01`, a 2-to-4 decoder asserts output line 1 (the second line, counting from zero) and deasserts the other three. Internally, each output line is an AND gate that checks for a specific input pattern. Output 0 is AND(A', B'), output 1 is AND(A', B), output 2 is AND(A, B'), and output 3 is AND(A, B). Decoders are everywhere in computer systems — they select which memory chip responds to a given address, they activate the correct register in a register file, and inside the CPU's control unit, they decode instruction opcodes into control signals that drive the datapath.

An **encoder** performs the inverse operation: given 2^n input lines with exactly one active, it produces the *n*-bit binary code identifying which line is active. A 4-to-2 encoder with input line 2 active outputs `10`. The practical limitation of a simple encoder is that it assumes exactly one input is active at a time. When multiple inputs can be active simultaneously — as happens in interrupt systems where several devices may request attention at once — you need a **priority encoder**. A priority encoder assigns a fixed priority ordering to the input lines (typically higher-numbered inputs have higher priority) and outputs the binary code of the highest-priority active input, along with a "valid" bit indicating that at least one input is active.

These circuits compose naturally into larger systems. A 3-to-8 decoder can be built from two 2-to-4 decoders plus an inverter, using the third input bit to enable one decoder and disable the other. Similarly, decoders with enable inputs can be cascaded to build address decoding logic for an entire memory system: a top-level decoder selects which memory bank is active, and within each bank, a lower-level decoder selects the specific word line. This hierarchical composition means you rarely need to design a massive decoder from scratch — you build it from smaller, well-understood pieces, which is a recurring pattern in digital design.
