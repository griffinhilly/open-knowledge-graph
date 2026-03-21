---
id: arithmetic-logic-unit-design-details
title: Arithmetic Logic Unit (ALU) Design and Operation Selection
domain: computer-science
course: computer-architecture
prerequisites:
- id: arithmetic-logic-unit
  type: hard
- id: carry-lookahead-adder-design
  type: soft
builds-toward:
- cpu-datapath-structural-design
tags:
- alu
- arithmetic
- logic-operations
stage: formal-systems
status: draft
---

# Arithmetic Logic Unit (ALU) Design and Operation Selection

## Core Idea
The ALU performs arithmetic (add, subtract, multiply, divide) and logic (AND, OR, XOR, NOT) operations on two operands. Control inputs select which operation to perform. Modern ALUs incorporate shifters and may use carry-lookahead or other optimization techniques. The ALU also sets condition code flags (zero, negative, overflow, carry) used by branch instructions.

## Questions

```yaml
- question: "On a given clock cycle, the control unit issues an ADD instruction to the ALU. What is the logic unit (AND/OR/XOR circuitry) doing during this cycle?"
  type: multiple-choice
  options:
    - "It is powered down to save energy since it is not needed for this instruction"
    - "It is computing logical operations on the operands in parallel with the adder; the mux selects the adder's output"
    - "It waits until the adder finishes, then computes logic operations in case a subsequent instruction needs them"
    - "It is performing input validation to confirm the operands are valid integers before the adder runs"
  answer: 1
  explanation: "All ALU functional units (adder, logic unit, shifter) compute simultaneously on every clock cycle. The multiplexer controlled by the operation select signal then routes the appropriate result — in this case, the adder's output — to the ALU result bus. The logic unit doesn't power down or wait; it just computes results that go unused on this cycle. This parallel design is simpler and faster than activating only the needed unit, since mux selection is near-instantaneous while control logic for selective activation would add complexity and delay."

- question: "What mechanism allows a conditional branch instruction (like 'jump if zero') to act on the result of a previous arithmetic operation?"
  type: multiple-choice
  options:
    - "The branch instruction reads the operand registers directly and re-executes the arithmetic to check the result"
    - "The scheduler ensures branch instructions always immediately follow the arithmetic they depend on"
    - "Condition code flags (zero, negative, overflow, carry) set by the ALU and stored in a status register"
    - "The program counter is automatically updated whenever an arithmetic result is zero"
  answer: 2
  explanation: "After every ALU operation, the ALU sets condition code flags that describe the result: Z (zero), N (negative), V (overflow), C (carry). These flags are stored in a status register. A conditional branch instruction then reads the relevant flag(s) from the status register to decide whether to jump. This is the architectural mechanism that connects arithmetic to control flow — it lets instructions be data-independent while still allowing branches to respond to computed results without re-executing the arithmetic."

- question: "Modern ALU designs implement subtraction using a dedicated subtraction circuit, separate from the adder, because subtraction and addition require fundamentally different hardware."
  type: true-false
  answer: false
  explanation: "Subtraction is implemented using the two's complement trick: complement (flip all bits of) the second operand and add one. This converts subtraction into addition, allowing the same adder hardware to handle both operations with only a small addition of a complementer circuit and an extra carry-in of 1. This design eliminates the need for a separate subtractor, saving significant chip area while maintaining correctness for both signed and unsigned arithmetic."

- question: "The zero flag (Z) in the ALU's condition code register is set when the result of the most recent arithmetic or logic operation is all zeros, enabling branch instructions to test for equality."
  type: true-false
  answer: true
  explanation: "The zero flag captures whether the ALU output is exactly zero. This is directly useful for equality testing: to check if A equals B, the CPU subtracts B from A and checks the Z flag — if Z is set, A − B = 0, meaning A = B. This is how 'branch if equal' instructions work at the hardware level. The zero flag (along with N, V, and C) connects arithmetic results to the control flow of the program, allowing the CPU to make decisions based on computed values."

- question: "Explain why the ALU uses a multiplexer approach — all functional units compute in parallel, with the mux selecting the result — rather than a design that activates only the needed unit per operation."
  type: short-answer
  answer: "The parallel-with-mux design is simpler and faster than selective activation. Determining which unit to activate requires decoding the operation code, routing control signals, and waiting for the selected unit to power on or stabilize — all of which add delay on the critical path. A multiplexer, by contrast, is a simple combinational circuit that selects among already-computed results in near-zero time once the select lines are set. Since all units are combinational logic that compute continuously as long as power is supplied, letting them all run and muxing the output adds minimal cost while avoiding the latency and complexity of selective gating."
  explanation: "This design principle — compute everything, then select — appears throughout digital logic because selection is cheap compared to computation. The cost of running the non-selected units is power consumption (all units draw current even when not selected), which is why modern processors with many execution units do gate power to unused units. But even in those designs, the basic principle within the ALU itself often remains parallel computation with mux selection, because the units are small enough that their power cost is negligible compared to the latency benefit."
```

## Explainer

From your introduction to the ALU concept, you know it is the part of the processor that performs computation. Now consider how it is actually built. An ALU is not a single circuit — it is a collection of parallel functional units (an adder, a logic unit, a shifter) whose outputs are fed into a **multiplexer** controlled by an operation select signal. When the control unit issues an ADD instruction, the select lines route the adder's output to the ALU result bus. When it issues an AND instruction, the same select lines route the logic unit's output instead. All units compute simultaneously on every cycle; the mux simply chooses which result to use.

The arithmetic section centers on an **adder circuit**, often a carry-lookahead adder for speed, as you studied previously. Subtraction is implemented by complementing the second operand (flipping all bits) and adding one — the two's complement trick that converts subtraction into addition with minimal extra hardware. Multiplication and division, when included directly in the ALU, require more complex iterative or combinational circuits and often take multiple clock cycles. The logic section is simpler: AND, OR, XOR, and NOT operations are computed independently for each bit position, since these operations have no carry propagation between bits. A **barrel shifter** handles shift and rotate operations, moving all bits simultaneously rather than shifting one position per clock cycle.

A critical output of the ALU is its **condition code flags**, also called status flags. After every operation, the ALU sets flags that describe the result: the **zero flag** (Z) indicates the result is all zeros, the **negative flag** (N) captures the most significant bit (indicating a negative result in two's complement), the **overflow flag** (V) detects when a signed operation produces a result too large for the word size, and the **carry flag** (C) captures the carry-out of the most significant bit position. These flags are stored in a status register and are read by conditional branch instructions — a "branch if zero" instruction checks the Z flag to decide whether to jump. This is the mechanism that connects arithmetic to control flow in every processor.

The **operation select** input is the interface between the ALU and the rest of the CPU. In a typical design, a 3- or 4-bit control field selects among 8 or 16 operations. This field comes from the control unit, which decodes the current instruction's opcode to determine what the ALU should do. The width of the ALU — 8-bit, 32-bit, 64-bit — determines how many bits are processed in parallel and directly affects the processor's data-handling capability. Designing an ALU means balancing the number of supported operations, the speed of the critical path (usually the adder), and the silicon area budget, since every additional operation adds hardware that must fit on the chip.
