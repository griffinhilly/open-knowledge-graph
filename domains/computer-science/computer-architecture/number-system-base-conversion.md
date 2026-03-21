---
id: number-system-base-conversion
title: Number System Conversions
domain: computer-science
course: computer-architecture
prerequisites:
- id: binary-number-system
  type: hard
- id: hexadecimal-number-system
  type: hard
tags:
- number-systems
- conversion
stage: formal-systems
status: draft
---

# Number System Conversions

## Core Idea
Converting between binary, octal, decimal, and hexadecimal is essential in computer architecture. Binary–hex conversion is direct (4 bits per hex digit); decimal conversions require repeated division or multiplication.

## Questions

```yaml
- question: "A student needs to convert 10110100₂ to hexadecimal. What is the most efficient method?"
  type: multiple-choice
  options:
    - "Group the bits into sets of four from the right: 1011→B, 0100→4, giving B4₁₆"
    - "Convert to decimal first (180), then use repeated division by 16"
    - "Apply repeated multiplication to each individual bit"
    - "Sum the positional values (128+32+16+4) and look up the hex table"
  answer: 0
  explanation: "Binary to hex is a direct substitution because 16 = 2⁴ — each hex digit maps to exactly four binary bits. Group from the right: 1011→B, 0100→4, giving B4₁₆. No arithmetic needed. Option 1 (convert to decimal first) is needlessly complex and misses the key insight: when two bases are powers of each other, conversion is a direct digit-group substitution."

- question: "Which of the following conversions requires the repeated division algorithm?"
  type: multiple-choice
  options:
    - "Binary 110101 to hexadecimal"
    - "Decimal 179 to binary"
    - "Hexadecimal A3 to binary"
    - "Binary 1010 to octal"
  answer: 1
  explanation: "Only conversions involving decimal require algorithmic computation (repeated division for decimal→binary, or summing positional powers for binary→decimal) because base 10 is not a power of 2. Binary↔hex and binary↔octal are direct group substitutions because 16 = 2⁴ and 8 = 2³ — the bases are exact powers of 2, so the digit positions align perfectly."

- question: "Converting between binary and octal uses the same principle as binary-to-hex conversion, just with groups of three bits instead of four."
  type: true-false
  answer: true
  explanation: "True. Because 8 = 2³, each octal digit maps exactly to three binary bits — the same direct grouping principle that makes binary↔hex trivial. Only the group size differs (3 vs. 4). This direct mapping exists whenever the two bases are powers of each other."

- question: "To convert hexadecimal 2F to decimal, you group the hex digits into pairs and look up their binary equivalents."
  type: true-false
  answer: false
  explanation: "False. Hex-to-decimal conversion uses positional notation: multiply each hex digit by its power of 16 and sum. 2F₁₆ = 2×16 + 15×1 = 47₁₀. The grouping method works for hex↔binary conversion, not hex↔decimal. The mistake confuses two different conversion problems."

- question: "Why can you convert between binary and hexadecimal without any arithmetic, while converting between binary and decimal always requires an algorithm?"
  type: short-answer
  answer: "Because hexadecimal (base 16) is an exact power of 2 (2⁴), each hex digit corresponds to exactly four binary digits — the positional weights align perfectly and no arithmetic is needed. Decimal (base 10) is not a power of 2, so the positional weights in the two systems do not align, and you must compute sums of powers of 2 or perform repeated division to reconcile them."
  explanation: "The structural key is whether the two bases are powers of each other. When they are (binary/octal, binary/hex), each digit in one base maps cleanly to a fixed group of digits in the other — a pure substitution. When they aren't (decimal and any power-of-2 base), the systems are incommensurable and actual arithmetic is required."
```

## Explainer

You already understand binary and hexadecimal as number systems — now the practical skill is converting fluently between them and decimal. The key insight is that some conversions are trivial because the bases are powers of each other, while others require an algorithm because the bases are unrelated.

**Binary to hexadecimal** (and back) is the easiest conversion because 16 = 2⁴. Each hexadecimal digit maps to exactly four binary digits. To convert binary to hex, group the bits into sets of four starting from the right, pad with leading zeros if needed, and replace each group with its hex equivalent: 0000→0, 0001→1, ..., 1010→A, ..., 1111→F. For example, 11010110₂ becomes D6₁₆ (1101→D, 0110→6). Going the other direction, just expand each hex digit into four bits. **Binary to octal** works identically but with groups of three (since 8 = 2³). This direct mapping is why hex is the preferred shorthand for binary in computing — it compresses the representation without any arithmetic.

**Decimal to binary** conversion requires the **repeated division algorithm**. Divide the decimal number by 2 and record the remainder; that remainder is the least significant bit. Divide the quotient by 2 again, recording the next remainder, and continue until the quotient reaches zero. Reading the remainders from bottom to top gives the binary representation. For example, 43 ÷ 2 = 21 remainder 1, 21 ÷ 2 = 10 remainder 1, 10 ÷ 2 = 5 remainder 0, 5 ÷ 2 = 2 remainder 1, 2 ÷ 2 = 1 remainder 0, 1 ÷ 2 = 0 remainder 1 — so 43₁₀ = 101011₂. The same algorithm works for any target base: to convert decimal to hex, divide repeatedly by 16 instead.

**Binary to decimal** uses positional notation directly: multiply each bit by its positional power of 2 and sum the results. For 101011₂: 1×32 + 0×16 + 1×8 + 0×4 + 1×2 + 1×1 = 43₁₀. For fractional parts, the process mirrors: binary digits after the radix point represent negative powers of 2 (2⁻¹ = 0.5, 2⁻² = 0.25, etc.), and converting decimal fractions to binary uses **repeated multiplication by 2**, taking the integer part at each step. Mastering these mechanical procedures is essential because every aspect of computer architecture — from memory addressing to instruction encoding — involves reading and reasoning about values across these bases.
