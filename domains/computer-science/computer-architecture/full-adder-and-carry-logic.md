---
id: full-adder-and-carry-logic
title: Full Adder and Carry Propagation
domain: computer-science
course: computer-architecture
prerequisites:
- id: combinational-logic-implementation
  type: hard
- id: adder-circuits
  type: soft
builds-toward:
- carry-lookahead-adder-design
- arithmetic-logic-unit-design-details
tags:
- arithmetic
- adder
- carry-propagation
stage: formal-systems
status: draft
---

# Full Adder and Carry Propagation

## Core Idea
A full adder adds three bits (two operand bits plus carry-in) and produces a sum and carry-out. Cascading full adders creates a ripple-carry adder that adds multi-bit numbers, but the carry propagation delay grows linearly with bit width, creating a performance bottleneck in high-speed arithmetic.

## Explainer

From your work with combinational logic, you know how to build circuits that compute Boolean functions of their inputs. A **half adder** adds two single bits, producing a sum (the XOR of the inputs) and a carry (the AND of the inputs). But real multi-bit addition requires handling a carry coming in from the previous column. A **full adder** extends the half adder to accept three inputs — two operand bits (A and B) plus a **carry-in** (Cin) from the adjacent lower-order position — and produces two outputs: a sum bit and a **carry-out** (Cout).

The logic is straightforward. The sum output is 1 when an odd number of the three inputs are 1: `Sum = A XOR B XOR Cin`. The carry-out is 1 when two or more inputs are 1: `Cout = (A AND B) OR (Cin AND (A XOR B))`. You can verify this against what you know about binary addition — adding three 1-bits gives 11 in binary (decimal 3), which is sum=1 and carry=1. A common implementation chains two half adders: the first computes A+B, producing an intermediate sum and carry; the second adds that intermediate sum to Cin, producing the final sum and a second carry. The overall carry-out is the OR of the two half-adder carries.

To add multi-bit numbers, you **cascade** full adders by connecting each stage's carry-out to the next stage's carry-in. For an N-bit addition, you chain N full adders (with the least significant stage's carry-in tied to 0, making it effectively a half adder). This is called a **ripple-carry adder**, and it correctly computes the sum — but with a significant speed limitation. Each full adder must wait for the carry-out of the previous stage before it can compute its own outputs. In the worst case (adding 1111...1 + 0001, where the carry ripples through every position), the delay is proportional to N. For a 64-bit adder, that means 64 gate delays in series.

This linear delay is the motivation for faster adder designs you will encounter next, particularly the **carry-lookahead adder**. The key insight of carry-lookahead is that each full adder either **generates** a carry (both A and B are 1, so a carry-out happens regardless of carry-in) or **propagates** a carry (exactly one of A and B is 1, so the carry-out equals the carry-in). By computing all the generate and propagate signals in parallel and using them to calculate carries directly, a carry-lookahead adder reduces the delay from O(N) to O(log N) — a dramatic improvement for wide datapaths.
