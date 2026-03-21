---
id: hexadecimal-number-system
title: Hexadecimal Number System
domain: computer-science
course: computer-architecture
prerequisites: []
builds-toward:
- memory-organization
- assembly-language-basics
tags:
- hexadecimal
- number-systems
- representation
stage: formal-systems
status: validated
---

# Hexadecimal Number System

## Core Idea
Hexadecimal (base-16) uses digits 0–9 and letters A–F to represent values 0–15 in a single digit position. It is widely used in computing because each hex digit corresponds exactly to 4 binary bits (a nibble), making it a compact and readable shorthand for binary data. Memory addresses, color codes, and machine code are commonly expressed in hexadecimal. Converting between hex and binary is straightforward: replace each hex digit with its 4-bit binary equivalent.

## How It's Best Learned
Memorize the hex-to-binary mapping for 0–F. Practice converting byte values (8-bit = 2 hex digits) between all three bases. Read and interpret memory dumps and color codes expressed in hex.

## Common Misconceptions
- Hexadecimal is not a separate 'special' system — it is just base-16 with the same place-value logic as any positional system.
- The letters A–F are not arbitrary; they are the conventional symbols for decimal 10–15.

## Questions

```yaml
- question: "A programmer examining a memory dump sees the byte value 0xB3. Why is hex preferred over the decimal equivalent (179) or the binary equivalent (10110011)?"
  type: multiple-choice
  options:
    - "Hex arithmetic is faster to compute mentally than binary or decimal arithmetic"
    - "Hex directly preserves binary structure: 0xB3 splits immediately into nibbles 1011 and 0011, showing each 4-bit group"
    - "Memory addresses are stored internally as hexadecimal, so decimal conversion introduces rounding errors"
    - "Hex is preferred for historical convention, not because it offers a technical advantage over binary"
  answer: 1
  explanation: "The key advantage of hex is the exact 1:4 correspondence with binary — each hex digit maps to exactly 4 bits. Converting 0xB3 to binary is instantaneous: B = 1011, 3 = 0011, giving 10110011. This mechanical lookup reveals bit-level structure that programmers care about. Decimal (179) loses that structure — the decimal form gives no insight into bit patterns, byte boundaries, or flag positions. Hex is a compact, readable shorthand for binary; computers don't perform arithmetic in hex internally."

- question: "What is the decimal value of 0xFF?"
  type: multiple-choice
  options:
    - "15, because F = 15 and only one digit is significant"
    - "150, because F = 15 and the place value doubles it"
    - "256, because FF represents the value 2⁸"
    - "255, because 0xFF = 15 × 16 + 15 = 240 + 15"
  answer: 3
  explanation: "Hex uses place-value like any positional system. 0xFF has two hex digits: F in the 16s place and F in the 1s place. F = 15, so 0xFF = 15 × 16¹ + 15 × 16⁰ = 240 + 15 = 255. This is the maximum value of one byte (8 bits: 11111111 in binary = 255). Option C (256 = 0x100) is a common off-by-one error — 256 requires a third hex digit. Web color #FFFFFF is white because each channel (R, G, B) is at maximum intensity: 255."

- question: "Computers perform internal arithmetic in hexadecimal because it is more efficient for the hardware than binary."
  type: true-false
  answer: false
  explanation: "Computers only perform arithmetic in binary — all CPU operations are binary at the hardware level. Hexadecimal is purely a human-readable representation, not an internal computation mode. Each hex digit maps exactly to 4 binary bits, so hex notation lets programmers read and write binary data compactly without the hardware doing anything differently. The 0x prefix in source code is just a notation hint to the compiler; storage and computation remain binary."

- question: "Each hexadecimal digit corresponds to exactly 4 binary bits."
  type: true-false
  answer: true
  explanation: "This 1:4 correspondence (one hex digit = one nibble = 4 bits) is the fundamental reason hex is used as shorthand for binary. The 16 possible values of a 4-bit group (0000 through 1111, i.e., 0 through 15) map exactly to the 16 hex digits (0–9 and A–F). One byte (8 bits) is always exactly two hex digits; a 32-bit value is always 8 hex digits. Conversion between hex and binary requires only a table lookup — no arithmetic."

- question: "Explain why hexadecimal is preferred over decimal when reading memory addresses or machine code, even though both representations carry the same numeric information."
  type: short-answer
  answer: "Hex preserves binary structure; decimal obscures it. Each hex digit maps exactly to 4 binary bits, so converting between hex and binary is a mechanical, digit-by-digit lookup with no arithmetic. The address 0x7FFFFFFF immediately signals 'all bits set except the sign bit' to an experienced programmer; its decimal equivalent 2,147,483,647 conveys no bit-level structure. Memory addresses, color codes, and machine instruction bytes all have structure at the bit and byte level that hex makes visible and decimal hides."
  explanation: "Programmers develop hex fluency because it's semantically aligned with how data is organized: one byte always equals two hex digits, one 32-bit word always equals eight hex digits. The visual grouping in hex directly corresponds to byte and nibble boundaries in memory — a relationship that decimal notation simply doesn't preserve."
```

## Explainer

Computers operate in binary — every piece of data is ultimately a sequence of 0s and 1s. But binary is painful for humans to read. The byte value `11010110` takes eight characters, and distinguishing it from `11010100` requires careful scanning. Decimal conversion helps with small values, but it obscures the bit-level structure that programmers often care about. **Hexadecimal** (base-16) solves this by providing a compact notation that preserves perfect alignment with binary: each hex digit maps to exactly 4 bits, so one byte is always exactly two hex digits, and conversion in either direction is instant.

The mapping is straightforward: 0 through 9 represent their usual values, and then A=10, B=11, C=12, D=13, E=14, F=15. To convert the binary byte `11010110` to hex, split it into two 4-bit groups: `1101` and `0110`. Looking up each group: `1101` = D and `0110` = 6, so the byte is `D6`. To go the other way, just expand each hex digit back to 4 bits. This mechanical, digit-by-digit conversion is what makes hex so useful — unlike decimal, there is no arithmetic involved, just a lookup table you quickly memorize.

Hexadecimal appears throughout computing. **Memory addresses** are written in hex because they are long binary values (32 or 64 bits) that would be unreadable in binary and misleading in decimal — the address `0x7FFF_FFFF` immediately tells an experienced programmer this is near the top of a 32-bit signed address space, while its decimal equivalent 2,147,483,647 does not convey that structure. **Color codes** in web design use hex: `#FF8800` means full red (FF = 255), about half green (88 = 136), and no blue (00 = 0). **Machine code** and assembly language listings display instruction bytes in hex. **Debugging tools** show memory dumps in hex. In each case, hex is preferred because it maintains a direct correspondence to the underlying bits while being roughly four times more compact than binary.

The prefix `0x` (used in C, Python, Java, and most programming languages) signals that a number is hexadecimal: `0x1A` is 26 in decimal, not eighteen or one-A. Some systems use other conventions — `$1A` in 6502 assembly, `1Ah` in Intel assembly, `#1A` in some contexts. Regardless of notation, the place-value system works identically to any other base: `0x1A` = 1×16¹ + 10×16⁰ = 16 + 10 = 26. As you move into memory organization and assembly language, hex will become your default way of reading and writing binary data — it is the lingua franca between human-readable and machine-readable representations.
