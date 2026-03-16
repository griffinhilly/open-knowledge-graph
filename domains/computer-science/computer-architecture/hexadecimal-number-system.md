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

## Explainer

Computers operate in binary — every piece of data is ultimately a sequence of 0s and 1s. But binary is painful for humans to read. The byte value `11010110` takes eight characters, and distinguishing it from `11010100` requires careful scanning. Decimal conversion helps with small values, but it obscures the bit-level structure that programmers often care about. **Hexadecimal** (base-16) solves this by providing a compact notation that preserves perfect alignment with binary: each hex digit maps to exactly 4 bits, so one byte is always exactly two hex digits, and conversion in either direction is instant.

The mapping is straightforward: 0 through 9 represent their usual values, and then A=10, B=11, C=12, D=13, E=14, F=15. To convert the binary byte `11010110` to hex, split it into two 4-bit groups: `1101` and `0110`. Looking up each group: `1101` = D and `0110` = 6, so the byte is `D6`. To go the other way, just expand each hex digit back to 4 bits. This mechanical, digit-by-digit conversion is what makes hex so useful — unlike decimal, there is no arithmetic involved, just a lookup table you quickly memorize.

Hexadecimal appears throughout computing. **Memory addresses** are written in hex because they are long binary values (32 or 64 bits) that would be unreadable in binary and misleading in decimal — the address `0x7FFF_FFFF` immediately tells an experienced programmer this is near the top of a 32-bit signed address space, while its decimal equivalent 2,147,483,647 does not convey that structure. **Color codes** in web design use hex: `#FF8800` means full red (FF = 255), about half green (88 = 136), and no blue (00 = 0). **Machine code** and assembly language listings display instruction bytes in hex. **Debugging tools** show memory dumps in hex. In each case, hex is preferred because it maintains a direct correspondence to the underlying bits while being roughly four times more compact than binary.

The prefix `0x` (used in C, Python, Java, and most programming languages) signals that a number is hexadecimal: `0x1A` is 26 in decimal, not eighteen or one-A. Some systems use other conventions — `$1A` in 6502 assembly, `1Ah` in Intel assembly, `#1A` in some contexts. Regardless of notation, the place-value system works identically to any other base: `0x1A` = 1×16¹ + 10×16⁰ = 16 + 10 = 26. As you move into memory organization and assembly language, hex will become your default way of reading and writing binary data — it is the lingua franca between human-readable and machine-readable representations.
