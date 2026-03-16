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

## Explainer

You already understand binary and hexadecimal as number systems — now the practical skill is converting fluently between them and decimal. The key insight is that some conversions are trivial because the bases are powers of each other, while others require an algorithm because the bases are unrelated.

**Binary to hexadecimal** (and back) is the easiest conversion because 16 = 2⁴. Each hexadecimal digit maps to exactly four binary digits. To convert binary to hex, group the bits into sets of four starting from the right, pad with leading zeros if needed, and replace each group with its hex equivalent: 0000→0, 0001→1, ..., 1010→A, ..., 1111→F. For example, 11010110₂ becomes D6₁₆ (1101→D, 0110→6). Going the other direction, just expand each hex digit into four bits. **Binary to octal** works identically but with groups of three (since 8 = 2³). This direct mapping is why hex is the preferred shorthand for binary in computing — it compresses the representation without any arithmetic.

**Decimal to binary** conversion requires the **repeated division algorithm**. Divide the decimal number by 2 and record the remainder; that remainder is the least significant bit. Divide the quotient by 2 again, recording the next remainder, and continue until the quotient reaches zero. Reading the remainders from bottom to top gives the binary representation. For example, 43 ÷ 2 = 21 remainder 1, 21 ÷ 2 = 10 remainder 1, 10 ÷ 2 = 5 remainder 0, 5 ÷ 2 = 2 remainder 1, 2 ÷ 2 = 1 remainder 0, 1 ÷ 2 = 0 remainder 1 — so 43₁₀ = 101011₂. The same algorithm works for any target base: to convert decimal to hex, divide repeatedly by 16 instead.

**Binary to decimal** uses positional notation directly: multiply each bit by its positional power of 2 and sum the results. For 101011₂: 1×32 + 0×16 + 1×8 + 0×4 + 1×2 + 1×1 = 43₁₀. For fractional parts, the process mirrors: binary digits after the radix point represent negative powers of 2 (2⁻¹ = 0.5, 2⁻² = 0.25, etc.), and converting decimal fractions to binary uses **repeated multiplication by 2**, taking the integer part at each step. Mastering these mechanical procedures is essential because every aspect of computer architecture — from memory addressing to instruction encoding — involves reading and reasoning about values across these bases.
