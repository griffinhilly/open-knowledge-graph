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
status: validated
---

# Overflow and Underflow Detection

## Core Idea
Overflow occurs when an arithmetic result exceeds the maximum representable value. In two's complement, overflow is detected by comparing input and output signs—a sum of two positive numbers should not be negative.

## Questions

```yaml
- question: "In 8-bit two's complement, you add 80 + 60. The result is −116 and the carry-out bit from the MSB is 0. Which of the following best describes what happened?"
  type: multiple-choice
  options:
    - "No error occurred — the carry-out being 0 means the result is correct"
    - "Overflow occurred because two positive numbers produced a negative result"
    - "Underflow occurred because the result is negative"
    - "Overflow cannot occur with positive numbers, so this must be a hardware bug"
  answer: 1
  explanation: "The detection rule for two's complement overflow is not about the carry-out bit alone — it is about whether two operands of the same sign produced a result of the opposite sign. 80 + 60 = 140, which exceeds the 8-bit range of −128 to +127. Both inputs are positive, but the result wrapped to −116 (negative), proving overflow. Option A confuses carry-out with overflow; carry-out is one input to the overflow detection logic but is not sufficient on its own."

- question: "Which of the following additions in two's complement arithmetic can never produce an overflow, regardless of the operand values?"
  type: multiple-choice
  options:
    - "Adding two large positive numbers"
    - "Adding two large negative numbers"
    - "Adding a positive number and a negative number"
    - "Adding any number to zero"
  answer: 2
  explanation: "When adding a positive and a negative number in two's complement, the result always lies between the two operands in magnitude, so it always fits within the representable range — overflow cannot occur. By contrast, adding two positive numbers can overflow into the negative range, and adding two negative numbers can overflow into the positive range. The sign-matching rule ('same-sign inputs → overflow possible; opposite-sign inputs → overflow impossible') encodes this insight directly."

- question: "In 8-bit two's complement, adding 100 + 50 produces −106. This is an overflow, and the hardware can detect it by observing that two positive inputs produced a negative output."
  type: true-false
  answer: true
  explanation: "This is exactly the two's complement overflow detection rule. 100 + 50 = 150, which exceeds +127, the maximum 8-bit representable value. The result wraps to −106. The sign-check rule — both inputs are positive but the output is negative — is both necessary and sufficient to detect overflow in two's complement addition."

- question: "If the carry-out bit from the most significant bit position is 1 after an addition, an overflow has definitely occurred."
  type: true-false
  answer: false
  explanation: "This is a common misconception. In two's complement arithmetic, overflow is detected by comparing the carry INTO the MSB with the carry OUT of the MSB — overflow occurs only when these two carry bits differ. A carry-out of 1 can occur with no overflow (e.g., adding a positive and a large negative number may produce a carry-out without violating the representable range). Conversely, overflow can occur with a carry-out of 0 (e.g., two large positive numbers). The carry-out alone is not the overflow indicator."

- question: "Explain why adding a positive number and a negative number in two's complement can never produce an overflow."
  type: short-answer
  answer: "Because the result must lie between the two operands in magnitude. Adding a positive and a negative number moves the sum toward zero from both sides — the result is always smaller in absolute value than the larger operand. Since both operands are representable, and the result is bounded by the larger, it is always within the representable range."
  explanation: "The intuition is geometric: a positive and negative number pull in opposite directions on the number line, so the sum is always between them and cannot escape the bounds. This is why the sign-matching rule works: you only need to worry about two inputs that both push in the same direction — two positives can exceed the positive maximum, and two negatives can fall below the negative minimum. Opposite-sign inputs self-constrain."
```

## Explainer

From your study of binary arithmetic and two's complement, you know that a fixed number of bits can only represent a finite range of values. An 8-bit two's complement number, for example, spans −128 to +127. **Overflow** occurs when an arithmetic operation produces a result outside this range — the true mathematical answer exists, but it cannot be encoded in the available bits. The result wraps around to the opposite end of the number line, producing a value with the wrong sign. For instance, adding 100 + 50 in 8-bit two's complement yields 150, which exceeds +127 and wraps to −106 — a catastrophically wrong answer with no warning unless the hardware explicitly detects it.

The detection rule for addition in two's complement is elegant: **overflow occurs if and only if the two operands have the same sign but the result has a different sign**. Adding two positive numbers should produce a positive result; if the result is negative, the sum has overflowed. Adding two negative numbers should produce a negative result; if it comes out positive, underflow has occurred (the result is more negative than the representation allows). Adding a positive and a negative number can never overflow, because the result is always between the two operands in magnitude. At the hardware level, this is detected by comparing the carry into the most significant bit with the carry out of it — if they differ, overflow has occurred.

**Underflow** in integer arithmetic is conceptually the mirror image of overflow — the result is too negative to represent. In two's complement, adding −100 and −50 gives −150, which is below −128 and wraps to +106. For floating-point numbers, underflow has a different meaning: the result is too close to zero to represent as a normalized number, and precision is lost as the number enters the **denormalized** range or rounds to zero. Whether dealing with integers or floating-point, the fundamental issue is the same — finite representations have boundaries, and crossing them silently produces wrong answers.

Processors handle overflow in different ways depending on the instruction set architecture. Some architectures set a status flag (like the overflow flag in x86) that software can check after each operation. Others, like MIPS, provide both checked and unchecked arithmetic instructions — `add` traps on overflow while `addu` silently wraps. In high-level languages, this hardware behavior is often invisible; C and C++ define signed integer overflow as undefined behavior, meaning the compiler assumes it never happens. Understanding the hardware detection mechanism is essential for writing correct low-level code and for designing ALUs that faithfully report when their results cannot be trusted.
