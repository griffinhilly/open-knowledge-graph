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
status: validated
---

# Converting Between Binary, Decimal, and Hexadecimal

## Core Idea
Conversion between bases uses positional notation: any base-b number equals sum of (digit × b^position). Binary and hexadecimal are particularly related—every 4 binary digits map to 1 hex digit. Understanding these conversions is essential for reading machine code and memory addresses.

## Questions

```yaml
- question: "What is the hexadecimal equivalent of the binary number 1011 1010?"
  type: multiple-choice
  options:
    - "0x188"
    - "0x1BA"
    - "0xBA"
    - "0x11BA"
  answer: 2
  explanation: "Group the 8 bits into two groups of four from the right: 1011 and 1010. Convert each group separately: 1011 = 8+2+1 = 11 = B in hex; 1010 = 8+2 = 10 = A in hex. Result: 0xBA. This is the key advantage of the binary↔hex relationship — no arithmetic across digit boundaries is needed. Each 4-bit group translates independently to one hex digit. Options like 0x188 or 0x1BA arise from incorrect groupings or positional calculations; 0x11BA has too many digits for 8 bits."

- question: "Why is hexadecimal preferred over binary for displaying memory addresses in debuggers and hex dumps?"
  type: multiple-choice
  options:
    - "Hexadecimal arithmetic is faster for computers to perform than binary arithmetic"
    - "Hexadecimal is a human-readable form compatible with standard decimal notation"
    - "One hex digit represents exactly four bits, so hex compresses binary by 4:1 without any arithmetic conversion"
    - "Memory addresses are stored internally as hexadecimal values, not binary"
  answer: 2
  explanation: "Computers store everything in binary — hex is purely a display convention for humans. The reason hex is preferred is the lossless 4:1 compression: one hex character represents exactly four bits, so an 8-bit byte becomes two hex characters, a 32-bit address becomes 8 hex characters. This is compact without requiring any arithmetic: the translation is a direct symbol substitution. Decimal would require arithmetic (repeated division) to recover binary, and binary itself would be an unmanageably long string of 0s and 1s."

- question: "To convert between binary and hexadecimal, you must first convert both values to decimal as an intermediate step."
  type: true-false
  answer: false
  explanation: "Binary and hex share a direct relationship because 16 = 2⁴. Every hex digit maps to exactly four binary digits, and vice versa, with no arithmetic required — you simply substitute symbols. For example, 0xA = 1010 and 0xF = 1111. Going through decimal would be slower and unnecessary. Decimal is base 10, which has no power-of-2 relationship with binary or hex, so decimal conversions genuinely do require arithmetic. But binary↔hex is a direct, table-based lookup."

- question: "In the repeated-division method for converting a decimal number to another base, the remainders are read from the last computed to the first — that is, bottom to top — to form the result."
  type: true-false
  answer: true
  explanation: "Each division step produces the next least-significant digit — the first remainder is the units digit (lowest place value), the second is the 'base¹' digit, and so on. When you read the remainders in the order they were computed (top to bottom), you get the number in reverse. Reading bottom to top gives the correct most-significant-digit-first representation. For example, converting 42 to binary: remainders are 0,1,0,1,0,1 (in order), read bottom to top: 101010."

- question: "Explain why converting between binary and hexadecimal requires no arithmetic, while converting between either of these and decimal does require calculation."
  type: short-answer
  answer: "Binary and hex are both powers of 2 (base 2¹ and base 2⁴). Because 16 = 2⁴, exactly four binary digits correspond to one hex digit — the mapping is a fixed, arithmetic-free lookup table. You group bits in fours and substitute symbols. Decimal is base 10, which shares no power-of-2 relationship with binary, so there is no digit-group correspondence. To convert to or from decimal, you must either sum positional weights (digit × base^position) or repeatedly divide by the target base — both involve arithmetic across all digit positions."
  explanation: "This distinction is practically important. Fluency with the direct binary↔hex substitution lets you read machine code and memory dumps without calculation. When you see 0xFF, you should immediately see 11111111 without computing. That immediacy comes from memorizing the 16 4-bit patterns, not from understanding base conversion in the abstract."
```

## Explainer

You already understand that hexadecimal is a base-16 system using digits 0–9 and letters A–F. The deeper skill is fluently converting between bases — not just knowing the theory, but being able to look at a hex value like `0x3F` and immediately see the binary and decimal equivalents. The foundation is **positional notation**: each digit's value is the digit itself multiplied by the base raised to the power of its position, counting from zero on the right. In decimal, 247 means 2×10² + 4×10¹ + 7×10⁰. The same principle applies to every base.

To convert **from any base to decimal**, expand each digit by its positional weight and sum. For binary 1101: 1×2³ + 1×2² + 0×2¹ + 1×2⁰ = 8 + 4 + 0 + 1 = 13. For hex 2A: 2×16¹ + 10×16⁰ = 32 + 10 = 42. To convert **from decimal to another base**, use repeated division: divide the decimal number by the target base, record the remainder (that is the least significant digit), then divide the quotient again. Continue until the quotient is zero, then read the remainders bottom to top. For example, converting 42 to binary: 42÷2=21 r0, 21÷2=10 r1, 10÷2=5 r0, 5÷2=2 r1, 2÷2=1 r0, 1÷2=0 r1 — reading remainders upward gives 101010.

The most practically important conversion is between **binary and hexadecimal**, and here the relationship is direct because 16 = 2⁴. Every single hex digit maps to exactly four binary digits: 0→0000, 1→0001, ..., 9→1001, A→1010, B→1011, ..., F→1111. To convert binary to hex, group the bits into sets of four starting from the right and translate each group. Binary 1010 1100 becomes AC in hex. To go the other direction, expand each hex digit into its four-bit equivalent. This is why hexadecimal is the preferred shorthand for binary data in computing — it compresses four bits into one character without any arithmetic.

Fluency in these conversions matters because you will encounter all three representations constantly. Memory addresses and machine code are displayed in hex because it is compact and aligns with byte boundaries (two hex digits = one byte = eight bits). Debugging requires reading hex dumps and mentally converting to binary to see individual flag bits. Understanding bit masks, bitwise operations, and memory alignment all depend on moving comfortably between representations. Practice the repeated-division method until it is mechanical, and memorize the sixteen 4-bit binary-to-hex mappings — they are as fundamental to computer architecture as the multiplication table is to arithmetic.
