---
id: arithmetic-logic-unit
title: Arithmetic Logic Unit (ALU)
domain: computer-science
course: computer-architecture
prerequisites:
- id: adder-circuits
  type: hard
- id: twos-complement
  type: hard
- id: boolean-algebra
  type: soft
- id: floating-point-representation
  type: soft
builds-toward:
- cpu-datapath
- cpu-control-unit
tags:
- ALU
- arithmetic
- logic-operations
- CPU
stage: formal-systems
status: validated
---
# Arithmetic Logic Unit (ALU)

## Core Idea
The Arithmetic Logic Unit (ALU) is the computational core of a CPU, performing arithmetic operations (addition, subtraction, comparison) and bitwise logic operations (AND, OR, XOR, NOT, shifts) on binary data. An n-bit ALU takes two n-bit operands and a function-select code, producing a result and status flags (zero, carry, overflow, negative). The ALU is built from a combination of adder circuits and logic gates unified by a multiplexer that selects the output based on the operation code.

## How It's Best Learned
Design a simple 1-bit ALU that supports ADD, AND, and OR, then extend to 4 bits. Implement status flags and trace how they are set by different operations. Examine an open-source CPU design to see how the ALU fits into the full datapath.

## Common Misconceptions
- The ALU does not perform multiplication and division directly in most designs; these are handled by separate units or by repeated addition in software.
- The ALU does not know what operation to perform on its own — it relies entirely on the control unit sending the correct function-select signals.

## Questions

```yaml
- question: "An ALU needs to compute A − B. Given that no subtraction circuit exists in the design, how does it perform the operation?"
  type: multiple-choice
  options:
    - "It routes the operands to a separate subtraction unit outside the ALU"
    - "It computes NOT(A) + B + 1 using the adder"
    - "It computes A + NOT(B) + 1 using the adder, exploiting two's complement negation"
    - "It cannot perform subtraction without a dedicated subtractor circuit"
  answer: 2
  explanation: "Subtraction uses the adder by exploiting two's complement: −B = NOT(B) + 1, so A − B = A + NOT(B) + 1. The ALU inverts the second operand (bitwise NOT) and sets carry-in to 1. This is why understanding two's complement is a prerequisite for the ALU — subtraction, negation, and comparison all reduce to addition with a complemented input. Option B has the operands reversed."

- question: "A high-level language statement `if (a < b)` is compiled and executed on a CPU. What does the ALU actually do to evaluate this condition?"
  type: multiple-choice
  options:
    - "It reads the values of a and b from memory and compares their addresses"
    - "It performs a − b, discards the numeric result, and checks the negative and overflow flags"
    - "It uses a dedicated comparison circuit separate from the arithmetic path"
    - "The control unit evaluates the condition directly without invoking the ALU"
  answer: 1
  explanation: "Comparison is implemented as subtraction: the ALU computes a − b, and the control unit reads the resulting status flags. For signed integers, the negative flag (MSB of result) and the overflow flag together determine whether a < b. The numeric result is discarded. This shows how the ALU's flag outputs — not just its data output — are central to the processor's ability to implement any conditional logic."

- question: "The ALU's function-select inputs determine which operation (ADD, AND, OR, etc.) is performed on the current clock cycle."
  type: true-false
  answer: true
  explanation: "The ALU simultaneously computes multiple operations on the input operands — the AND gate, OR gate, and adder all produce outputs in parallel. A multiplexer at the output selects which result to pass through based on the function-select code sent by the control unit. So the select inputs do determine which operation's result is used, though all operations run in parallel internally."

- question: "The ALU decides which arithmetic or logic operation to perform based on the instruction currently being executed."
  type: true-false
  answer: false
  explanation: "The ALU has no knowledge of the current instruction or the program being executed. It is a purely combinational circuit: it takes operands and a function-select code as inputs and produces a result. It is the *control unit* that decodes the instruction and generates the appropriate function-select signals sent to the ALU. The ALU simply executes whatever operation the control unit requests — it has no agency or instruction-awareness of its own."

- question: "Why can an ALU perform subtraction using only an adder circuit, and why does this require two's complement representation?"
  type: short-answer
  answer: "In two's complement, the negation of B is NOT(B) + 1. Therefore A − B = A + (NOT(B) + 1) = A + NOT(B) + 1, which is just an addition with the second operand bitwise-inverted and carry-in set to 1. The adder handles this naturally by inverting B's bits and enabling carry-in. This works *because* two's complement is designed so that negation is a bitwise inversion plus 1 — a property that doesn't hold for sign-magnitude or one's complement representations."
  explanation: "The key insight is that two's complement wasn't just chosen to represent negatives — it was chosen specifically because it makes subtraction free once you have an adder. This is why the ALU needs no separate subtraction hardware. The same trick extends to comparisons, which also reduce to subtraction, making the adder the computational workhorse behind arithmetic, subtraction, and branching conditions."
```

## Explainer

You already know how to build an adder circuit that takes two binary numbers and produces their sum, and you understand how two's complement represents negative numbers. The **Arithmetic Logic Unit** is the component that unifies addition, subtraction, and all the bitwise logic operations into a single circuit that can perform any of them on demand. Think of it as a Swiss Army knife for binary computation — every tool is always present, and a control signal selects which one to use.

At the simplest level, a 1-bit ALU slice contains an AND gate, an OR gate, and a full adder, all operating in parallel on the same pair of input bits. A **multiplexer** at the output selects which result to pass through, based on a 2-bit operation code. For AND, the mux selects the AND gate output. For addition, it selects the full adder output. Subtraction is handled by the same adder: inverting the second operand (bitwise NOT) and setting the carry-in to 1 gives you the two's complement negation, so A + NOT(B) + 1 = A − B. This is why understanding two's complement is essential — subtraction, comparison, and negation all reduce to addition with complemented inputs.

To build an n-bit ALU, you chain together n copies of the 1-bit slice, connecting the carry-out of each bit to the carry-in of the next (exactly like the ripple-carry adder you studied). All slices receive the same operation-select signals, so they all perform the same operation simultaneously. The result is an n-bit output plus four **status flags**. The **zero flag** is set when every output bit is 0. The **carry flag** captures the carry-out of the most significant bit. The **overflow flag** detects when a signed operation produces a result too large or too small for the representation (carry into the MSB differs from carry out of it). The **negative flag** is simply the most significant bit of the result, indicating a negative value in two's complement.

These flags are not just bookkeeping — they are how the processor implements conditional branching. A comparison like `if (a < b)` is typically executed as a subtraction `a − b` whose result is discarded; only the flags matter. The negative and overflow flags together determine whether `a` was less than `b` in signed arithmetic. The carry flag determines the same for unsigned comparison. So every conditional branch, every loop termination test, and every comparison operator in a high-level language ultimately reduces to an ALU operation followed by a flag check. The ALU does not know what program it is running — it simply takes two operands and a function code, produces a result and flags, and waits for the next instruction. The control unit orchestrates everything else.
