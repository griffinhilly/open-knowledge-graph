---
id: binary-subtraction-circuits
title: Binary Subtraction Using Two's Complement
domain: computer-science
course: computer-architecture
prerequisites:
- id: twos-complement
  type: hard
- id: full-adder-circuit-design
  type: hard
tags:
- subtraction
- arithmetic-circuits
stage: formal-systems
status: validated
---

# Binary Subtraction Using Two's Complement

## Core Idea
Subtraction is implemented by negating the subtrahend (inverting bits and adding 1) then adding. This unifies subtraction and addition in hardware, requiring only one arithmetic unit.

## Questions

```yaml
- question: "In an adder-subtractor circuit, how is the '+1' required to complete the two's complement negation of B provided?"
  type: multiple-choice
  options:
    - "A separate increment circuit adds 1 to the inverted B before it enters the adder"
    - "The carry-in of the least significant full adder is set to the SUB control signal"
    - "An extra full adder stage is dedicated exclusively to adding the +1"
    - "The XOR gates that invert B also automatically add 1 via carry propagation"
  answer: 1
  explanation: "The SUB control signal does double duty: it drives the XOR gates to invert B's bits (giving ~B), and it is simultaneously wired to the carry-in (C_in) of the least significant bit position. When SUB = 1, C_in = 1, which adds the +1 needed to convert ~B into the full two's complement −B. The result is A + ~B + 1 = A + (−B) = A − B. No extra hardware is needed — the carry-in that the adder already has serves as the mechanism for the +1. This elegance is why the design is called an adder-subtractor rather than two separate units."

- question: "In an adder-subtractor circuit with SUB = 0, what does the circuit compute?"
  type: multiple-choice
  options:
    - "A − B, because the XOR gates pass B unchanged and carry-in is 0"
    - "A + B, because the XOR gates pass B unchanged and carry-in is 0"
    - "A + (~B), because the XOR gates always invert B"
    - "−A + B, because the SUB signal acts on A rather than B"
  answer: 1
  explanation: "When SUB = 0, the XOR gate for each bit of B computes bit_B XOR 0 = bit_B — every bit of B passes through unchanged. The carry-in is also 0 (since C_in = SUB = 0). So the circuit computes A + B + 0 = A + B: standard addition. When SUB = 1, the XOR gates invert all bits of B (giving ~B) and C_in = 1, producing A + ~B + 1 = A − B. The same hardware performs both operations, switched entirely by the single SUB bit."

- question: "An adder-subtractor circuit requires two separate arithmetic units — one adder and one subtractor — to handle both operations."
  type: true-false
  answer: false
  explanation: "The key insight of the adder-subtractor design is that subtraction uses the exact same adder as addition. XOR gates controlled by the SUB signal handle the bit inversion (~B), and the SUB signal wired to carry-in provides the +1. The result is one circuit that performs A + B when SUB = 0 and A − B when SUB = 1. This unification is why processors have a single ALU for both operations rather than separate hardware — it is simpler, faster, and uses fewer transistors."

- question: "When SUB = 1, each bit of B passes through its XOR gate unchanged, so the adder receives the original B bits and adds 1 via carry-in to get B + 1."
  type: true-false
  answer: false
  explanation: "This reverses the behavior. When SUB = 1, each XOR gate computes bit_B XOR 1 = NOT(bit_B), which inverts the bit. So the adder receives ~B (all bits flipped), not B. The carry-in is also 1 (since C_in = SUB = 1), so the adder computes A + ~B + 1 = A + (−B) = A − B. When SUB = 0, bits pass through unchanged (bit_B XOR 0 = bit_B). The confusion between the two modes is the central mistake this question tests."

- question: "Explain why A − B can be computed using an adder with B's bits inverted and carry-in set to 1."
  type: short-answer
  answer: "In two's complement, the negation of B is −B = ~B + 1 (invert all bits, then add 1). Therefore A − B = A + (−B) = A + (~B + 1) = A + ~B + 1. The adder computes A + ~B, and the carry-in of 1 provides the +1, completing the two's complement negation. The entire subtraction reduces to an addition where the subtrahend's bits are inverted and an extra 1 is injected at the least significant bit position via carry-in."
  explanation: "This is why two's complement is universally used for signed integers in hardware — it is the only signed representation where negation is simply bit inversion plus 1, which maps perfectly onto the carry-in mechanism already present in any ripple-carry adder. One's complement and sign-magnitude require more complex circuits for subtraction and do not unify naturally with the adder."
```

## Explainer

From your study of two's complement, you know that negating a binary number means inverting all its bits and adding 1. And from full adder circuit design, you know how to build hardware that adds two n-bit numbers with a carry-in. Binary subtraction circuits exploit a beautiful connection between these two ideas: **A − B is the same as A + (−B)**, and since −B in two's complement is ~B + 1, subtraction becomes A + ~B + 1. This means you can perform subtraction using the same adder you already have — you just need to invert B and set the carry-in to 1.

The hardware implementation is elegant in its simplicity. Each bit of the subtrahend B passes through a **controlled inverter** — typically an XOR gate with a control signal called SUB. When SUB = 0 (addition mode), the XOR gate passes B through unchanged. When SUB = 1 (subtraction mode), the XOR gate flips every bit of B, producing ~B. The same SUB signal is wired to the carry-in of the least significant full adder, providing the +1 needed to complete the two's complement negation. The result is a single circuit — an **adder-subtractor** — that performs addition when SUB = 0 and subtraction when SUB = 1, with no additional arithmetic hardware.

This unification is why virtually every processor has a single arithmetic unit for both addition and subtraction rather than separate circuits. It also extends naturally to detecting overflow: in two's complement, overflow occurs when the carry into the most significant bit differs from the carry out of it. The adder-subtractor can check this condition with a single XOR gate on those two carry signals. Understanding this design also clarifies why two's complement is the universal choice for signed integer representation in hardware — it is the only signed number system where subtraction reduces to addition with bit inversion, keeping the circuit simple and fast.
