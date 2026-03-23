---
id: arithmetic-logic-units-design
title: Arithmetic-Logic Unit (ALU) Design
domain: computer-science
course: computer-architecture
prerequisites:
- id: binary-adders
  type: hard
- id: arithmetic-logic-unit
  type: soft
builds-toward:
- cpu-datapath
- instruction-fetch-decode-execute
tags:
- alu
- arithmetic
- logic
- operations
stage: formal-systems
status: validated
---

# Arithmetic-Logic Unit (ALU) Design

## Core Idea
An ALU integrates multiple arithmetic and logical operations (add, subtract, AND, OR, shift, etc.) and uses control signals to select which operation to perform. It is the computational core of every CPU's datapath.

## How It's Best Learned
Design a simple ALU with 4 operations (add, subtract, AND, OR); trace through execution with sample inputs.

## Common Misconceptions
ALUs do not store state; they are purely combinational. Operation selection requires log₂(N) control bits for N operations.

## Questions

```yaml
- question: "In a typical ALU design, how is subtraction (A − B) implemented without a dedicated subtracter circuit?"
  type: multiple-choice
  options:
    - "A separate subtractor circuit runs in parallel with the adder, and a multiplexer selects the result"
    - "B is inverted and the carry-in is set to 1, reusing the adder circuit to exploit the two's complement identity"
    - "The operands are swapped so B − A is computed and the sign bit is flipped"
    - "Subtraction requires a separate clock cycle using the same adder iteratively"
  answer: 1
  explanation: "Two's complement subtraction: A − B = A + (NOT B) + 1. By inverting all bits of B and setting carry-in to 1, the same adder hardware that performs addition can compute subtraction. This halves the hardware needed, since one control bit toggles between addition (B as-is, carry-in = 0) and subtraction (B inverted, carry-in = 1). Option A is wasteful and less common. Option C computes the wrong result. Option D would make the ALU sequential, violating its purely combinational nature."

- question: "An ALU needs to support 8 distinct operations. How many control bits are required to select among them?"
  type: multiple-choice
  options:
    - "8 control bits — one per operation"
    - "4 control bits — half the number of operations"
    - "3 control bits — log₂(8) = 3 enables selecting one of 8 combinations"
    - "2 control bits — sufficient for any standard ALU"
  answer: 2
  explanation: "N control bits can encode 2^N distinct states, so selecting one of 8 operations requires log₂(8) = 3 bits. With 3 bits you have 000 through 111 — exactly 8 combinations. Using one bit per operation (option A) is wasteful and also ambiguous if two bits were set simultaneously. The log₂(N) formula is fundamental to multiplexer design: a 2^k-to-1 multiplexer always requires exactly k select lines."

- question: "An ALU stores intermediate results between operations and therefore requires a clock signal to function correctly."
  type: true-false
  answer: false
  explanation: "An ALU is purely combinational — it has no internal state, no flip-flops, and no clock input. Given stable inputs and control signals, it produces stable outputs after a propagation delay. This is essential to its role in a datapath: the registers before and after the ALU hold values; the ALU simply computes. Registers are sequential (clocked) elements; the ALU is not. This combinational property allows the ALU to be composed cleanly with clocked storage elements without timing conflicts."

- question: "The zero flag in an ALU can be implemented as a single wide NOR gate applied to all result bits."
  type: true-false
  answer: true
  explanation: "The result is zero if and only if every bit of the output is 0. A NOR gate outputs 1 when all its inputs are 0, and 0 when any input is 1. Applying a wide NOR gate across all n result bits produces exactly the zero flag: it outputs 1 precisely when the result is all zeros. This costs almost nothing in hardware — a single n-input gate — but provides critical information used by branch instructions like 'branch if equal' (which subtracts and checks the zero flag)."

- question: "Why is it important that the ALU is purely combinational (stateless) rather than sequential (clocked with memory)?"
  type: short-answer
  answer: "A purely combinational ALU produces its output solely from the current inputs and control signals, with no dependence on previous operations. This allows it to fit cleanly into a synchronous datapath: registers capture inputs at the start of a clock cycle, the ALU computes during the cycle, and registers capture outputs at the end. If the ALU had internal state, it would need its own clocking logic and could produce different results for the same inputs depending on history."
  explanation: "The separation of computation (combinational) from memory (sequential/clocked) is a foundational principle of synchronous digital design. Mixing the two inside the ALU would create race conditions, complicate timing analysis, and break the clean abstraction boundary between the datapath and control unit. The processor's correctness depends on the ALU being a pure function of its inputs — the same inputs always produce the same output, making verification and pipelining tractable."
```

## Explainer

From your study of binary adders, you know how to build a circuit that takes two binary numbers and produces their sum using a chain of full adders with carry propagation. An ALU generalizes this idea: instead of a single hardwired operation, it is a combinational circuit that can perform *any one of several operations* on the same pair of inputs, selected by a set of **control signals**. Think of it as a Swiss Army knife — the inputs stay the same, but the control bits tell the ALU which blade to open.

The simplest ALU design places multiple operation circuits in parallel — an adder, a subtractor, an AND gate array, an OR gate array — all connected to the same two input buses. Each circuit computes its result simultaneously, and a **multiplexer** at the output selects which result to pass through based on the control signals. For four operations, you need a 4-to-1 multiplexer controlled by 2 bits: `00` might select AND, `01` might select OR, `10` might select addition, and `11` might select subtraction. Subtraction typically reuses the adder by inverting one input and setting the carry-in to 1, exploiting the two's complement identity `A - B = A + NOT(B) + 1`. This means the adder and subtractor share hardware, and a single control bit toggles between addition and subtraction.

Beyond the primary result, a well-designed ALU produces **condition flags** that report properties of the output: a **zero flag** (is the result all zeros?), a **negative flag** (is the sign bit set?), a **carry flag** (did the addition overflow the word width?), and an **overflow flag** (did a signed addition produce an incorrect sign?). These flags cost almost nothing to generate — a zero flag is just a wide NOR gate across all result bits — but they are essential for the processor's control logic. Branch instructions like "branch if equal" simply test the zero flag after a subtraction, which is why comparison and subtraction are really the same ALU operation.

The ALU is purely **combinational**: it has no memory, no clock input, and no internal state. You present inputs and control signals, and after a propagation delay the outputs stabilize. This is a critical property because it means the ALU fits cleanly into a clocked datapath — registers capture inputs at the start of a clock cycle, the ALU computes during the cycle, and registers capture the result at the end. When you build a full CPU datapath, the ALU sits at the center, connected to the register file on both sides, with the control unit deciding which operation to perform on each clock cycle based on the current instruction.
