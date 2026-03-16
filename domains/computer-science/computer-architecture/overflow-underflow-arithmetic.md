---
id: overflow-underflow-arithmetic
title: Overflow and Underflow Detection
domain: computer-science
course: computer-architecture
prerequisites:
- id: twos-complement
  type: hard
- id: binary-arithmetic
  type: hard
tags:
- arithmetic
- error-detection
stage: formal-systems
status: draft
---

# Overflow and Underflow Detection

## Core Idea
Overflow occurs when an arithmetic result exceeds the maximum representable value. In two's complement, overflow is detected by comparing input and output signs—a sum of two positive numbers should not be negative.

## Explainer

From your study of binary arithmetic and two's complement, you know that a fixed number of bits can only represent a finite range of values. An 8-bit two's complement number, for example, spans −128 to +127. **Overflow** occurs when an arithmetic operation produces a result outside this range — the true mathematical answer exists, but it cannot be encoded in the available bits. The result wraps around to the opposite end of the number line, producing a value with the wrong sign. For instance, adding 100 + 50 in 8-bit two's complement yields 150, which exceeds +127 and wraps to −106 — a catastrophically wrong answer with no warning unless the hardware explicitly detects it.

The detection rule for addition in two's complement is elegant: **overflow occurs if and only if the two operands have the same sign but the result has a different sign**. Adding two positive numbers should produce a positive result; if the result is negative, the sum has overflowed. Adding two negative numbers should produce a negative result; if it comes out positive, underflow has occurred (the result is more negative than the representation allows). Adding a positive and a negative number can never overflow, because the result is always between the two operands in magnitude. At the hardware level, this is detected by comparing the carry into the most significant bit with the carry out of it — if they differ, overflow has occurred.

**Underflow** in integer arithmetic is conceptually the mirror image of overflow — the result is too negative to represent. In two's complement, adding −100 and −50 gives −150, which is below −128 and wraps to +106. For floating-point numbers, underflow has a different meaning: the result is too close to zero to represent as a normalized number, and precision is lost as the number enters the **denormalized** range or rounds to zero. Whether dealing with integers or floating-point, the fundamental issue is the same — finite representations have boundaries, and crossing them silently produces wrong answers.

Processors handle overflow in different ways depending on the instruction set architecture. Some architectures set a status flag (like the overflow flag in x86) that software can check after each operation. Others, like MIPS, provide both checked and unchecked arithmetic instructions — `add` traps on overflow while `addu` silently wraps. In high-level languages, this hardware behavior is often invisible; C and C++ define signed integer overflow as undefined behavior, meaning the compiler assumes it never happens. Understanding the hardware detection mechanism is essential for writing correct low-level code and for designing ALUs that faithfully report when their results cannot be trusted.
