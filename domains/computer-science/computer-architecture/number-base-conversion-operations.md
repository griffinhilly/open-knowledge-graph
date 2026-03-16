---
id: number-base-conversion-operations
title: Converting Between Binary, Decimal, and Hexadecimal
domain: computer-science
course: computer-architecture
prerequisites:
- id: hexadecimal-number-system
  type: hard
builds-toward:
- instruction-encoding-and-machine-code
- memory-address-representation
tags:
- number-systems
- conversion
- radix
stage: formal-systems
status: draft
---

# Converting Between Binary, Decimal, and Hexadecimal

## Core Idea
Conversion between bases uses positional notation: any base-b number equals sum of (digit × b^position). Binary and hexadecimal are particularly related—every 4 binary digits map to 1 hex digit. Understanding these conversions is essential for reading machine code and memory addresses.

## Explainer

You already understand that hexadecimal is a base-16 system using digits 0–9 and letters A–F. The deeper skill is fluently converting between bases — not just knowing the theory, but being able to look at a hex value like `0x3F` and immediately see the binary and decimal equivalents. The foundation is **positional notation**: each digit's value is the digit itself multiplied by the base raised to the power of its position, counting from zero on the right. In decimal, 247 means 2×10² + 4×10¹ + 7×10⁰. The same principle applies to every base.

To convert **from any base to decimal**, expand each digit by its positional weight and sum. For binary 1101: 1×2³ + 1×2² + 0×2¹ + 1×2⁰ = 8 + 4 + 0 + 1 = 13. For hex 2A: 2×16¹ + 10×16⁰ = 32 + 10 = 42. To convert **from decimal to another base**, use repeated division: divide the decimal number by the target base, record the remainder (that is the least significant digit), then divide the quotient again. Continue until the quotient is zero, then read the remainders bottom to top. For example, converting 42 to binary: 42÷2=21 r0, 21÷2=10 r1, 10÷2=5 r0, 5÷2=2 r1, 2÷2=1 r0, 1÷2=0 r1 — reading remainders upward gives 101010.

The most practically important conversion is between **binary and hexadecimal**, and here the relationship is direct because 16 = 2⁴. Every single hex digit maps to exactly four binary digits: 0→0000, 1→0001, ..., 9→1001, A→1010, B→1011, ..., F→1111. To convert binary to hex, group the bits into sets of four starting from the right and translate each group. Binary 1010 1100 becomes AC in hex. To go the other direction, expand each hex digit into its four-bit equivalent. This is why hexadecimal is the preferred shorthand for binary data in computing — it compresses four bits into one character without any arithmetic.

Fluency in these conversions matters because you will encounter all three representations constantly. Memory addresses and machine code are displayed in hex because it is compact and aligns with byte boundaries (two hex digits = one byte = eight bits). Debugging requires reading hex dumps and mentally converting to binary to see individual flag bits. Understanding bit masks, bitwise operations, and memory alignment all depend on moving comfortably between representations. Practice the repeated-division method until it is mechanical, and memorize the sixteen 4-bit binary-to-hex mappings — they are as fundamental to computer architecture as the multiplication table is to arithmetic.
