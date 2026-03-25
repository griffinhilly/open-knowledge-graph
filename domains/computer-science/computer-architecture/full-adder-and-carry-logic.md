---
id: full-adder-and-carry-logic
title: Full Adder and Carry Propagation
domain: computer-science
course: computer-architecture
prerequisites:
- id: combinational-circuit-design
  type: hard
- id: binary-adders
  type: soft
builds-toward:
- carry-lookahead-adder-design
- arithmetic-logic-unit
tags:
- arithmetic
- adder
- carry-propagation
stage: formal-systems
status: validated
---

# Full Adder and Carry Propagation

## Core Idea
A full adder adds three bits (two operand bits plus carry-in) and produces a sum and carry-out. Cascading full adders creates a ripple-carry adder that adds multi-bit numbers, but the carry propagation delay grows linearly with bit width, creating a performance bottleneck in high-speed arithmetic.

## Questions

```yaml
- question: "A ripple-carry adder is used to add the 8-bit numbers 11111111 and 00000001. How does this compare to adding 10000000 and 00000001 in terms of carry propagation delay?"
  type: multiple-choice
  options:
    - "Both take the same time, because carry propagation always traverses all 8 bits"
    - "The first addition is slower, because the carry must propagate through all 8 bit positions"
    - "The second addition is slower, because adding to a number with a 1 in the MSB is harder"
    - "Neither produces a carry, so both complete in a single gate delay"
  answer: 1
  explanation: "In 11111111 + 00000001, the carry generated at bit 0 must ripple through all 8 positions — each full adder must wait for the carry-out of the previous stage before it can finalize its sum and carry-out. This is the worst case for a ripple-carry adder. In 10000000 + 00000001, the carry is generated at bit 0 but bits 1–6 are 0 (in the first operand), so the carry stops propagating quickly — the delay is much shorter. This illustrates why ripple-carry delay is O(N) in the worst case but can be much less for some inputs."

- question: "A student describes a full adder as 'a circuit with two inputs (A and B) and two outputs (Sum and Carry-out).' What critical component is missing from this description?"
  type: multiple-choice
  options:
    - "The enable line, which gates the adder's operation"
    - "The carry-in input, which accepts the carry from the previous bit position"
    - "The overflow output, which signals when the result exceeds the bit width"
    - "The subtract input, which allows the full adder to perform subtraction"
  answer: 1
  explanation: "A full adder has three inputs — A, B, and carry-in (Cin) — not two. This is what distinguishes it from a half adder. The carry-in is essential because in multi-bit addition, each bit position receives a carry from the adjacent lower-order position. Without carry-in, you cannot cascade adders to handle multi-bit numbers correctly. The student's description is actually of a half adder, which only adds two bits and cannot be directly used in a multi-bit ripple-carry chain."

- question: "The sum output of a full adder is 1 when an odd number of its three inputs (A, B, Cin) are 1."
  type: true-false
  answer: true
  explanation: "The sum output implements XOR across all three inputs: Sum = A XOR B XOR Cin. XOR is 1 when an odd number of inputs are 1. So Sum = 1 when exactly one or all three inputs are 1 (1+0+0=1, 0+1+0=1, 0+0+1=1, 1+1+1=3 which is odd). Sum = 0 when exactly zero or two inputs are 1 (0+0+0=0, 1+1+0=2, 1+0+1=2, 0+1+1=2). This matches standard binary addition: 1+1+1 = 11 in binary (sum=1, carry=1)."

- question: "In a ripple-carry adder, all bit positions compute their final sum values simultaneously in parallel, and the only sequential step is combining the results."
  type: true-false
  answer: false
  explanation: "This is the fundamental limitation of ripple-carry adders. Each bit position cannot determine its sum until it receives the carry-out from the previous position. The computation is inherently sequential — the carry signal 'ripples' from bit 0 to bit 1 to bit 2, and so on. This creates an O(N) critical path delay where N is the bit width. The bit positions do not compute in parallel; bit position k must wait for bit position k−1 to finish. This is precisely why carry-lookahead adders were developed — to parallelize the carry computation."

- question: "Why is carry-lookahead faster than ripple-carry, and what is the key insight that makes it possible?"
  type: short-answer
  answer: "In a ripple-carry adder, each stage must wait for the previous carry-out before computing, creating O(N) sequential delay. Carry-lookahead exploits the fact that each bit position either 'generates' a carry (when both A and B are 1, regardless of carry-in) or 'propagates' a carry (when exactly one of A, B is 1, passing carry-in through to carry-out). All generate and propagate signals can be computed simultaneously from the original inputs in one gate delay. Then, using Boolean formulas that combine these signals, the carry into any position can be computed directly in O(log N) depth without waiting for carries to ripple through intermediate stages. The key insight is separating the carry computation from the sum computation and parallelizing the carry logic."
  explanation: "Carry-lookahead reduces critical path from O(N) to O(log N) by expressing each carry as a Boolean function of the original operand bits — not iteratively through previous stages. This is the foundational insight behind all fast adder designs, including carry-select and Kogge-Stone architectures."
```

## Explainer

From your work with combinational logic, you know how to build circuits that compute Boolean functions of their inputs. A **half adder** adds two single bits, producing a sum (the XOR of the inputs) and a carry (the AND of the inputs). But real multi-bit addition requires handling a carry coming in from the previous column. A **full adder** extends the half adder to accept three inputs — two operand bits (A and B) plus a **carry-in** (Cin) from the adjacent lower-order position — and produces two outputs: a sum bit and a **carry-out** (Cout).

The logic is straightforward. The sum output is 1 when an odd number of the three inputs are 1: `Sum = A XOR B XOR Cin`. The carry-out is 1 when two or more inputs are 1: `Cout = (A AND B) OR (Cin AND (A XOR B))`. You can verify this against what you know about binary addition — adding three 1-bits gives 11 in binary (decimal 3), which is sum=1 and carry=1. A common implementation chains two half adders: the first computes A+B, producing an intermediate sum and carry; the second adds that intermediate sum to Cin, producing the final sum and a second carry. The overall carry-out is the OR of the two half-adder carries.

To add multi-bit numbers, you **cascade** full adders by connecting each stage's carry-out to the next stage's carry-in. For an N-bit addition, you chain N full adders (with the least significant stage's carry-in tied to 0, making it effectively a half adder). This is called a **ripple-carry adder**, and it correctly computes the sum — but with a significant speed limitation. Each full adder must wait for the carry-out of the previous stage before it can compute its own outputs. In the worst case (adding 1111...1 + 0001, where the carry ripples through every position), the delay is proportional to N. For a 64-bit adder, that means 64 gate delays in series.

This linear delay is the motivation for faster adder designs you will encounter next, particularly the **carry-lookahead adder**. The key insight of carry-lookahead is that each full adder either **generates** a carry (both A and B are 1, so a carry-out happens regardless of carry-in) or **propagates** a carry (exactly one of A and B is 1, so the carry-out equals the carry-in). By computing all the generate and propagate signals in parallel and using them to calculate carries directly, a carry-lookahead adder reduces the delay from O(N) to O(log N) — a dramatic improvement for wide datapaths.
