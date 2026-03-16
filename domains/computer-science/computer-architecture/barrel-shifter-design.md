---
id: barrel-shifter-design
title: Barrel Shifter and Rotation Circuits
domain: computer-science
course: computer-architecture
prerequisites:
- id: multiplexer-circuits
  type: hard
- id: combinational-logic-implementation
  type: soft
builds-toward:
- arithmetic-logic-unit-design-details
tags:
- shifter
- rotation
- barrel-shifter
stage: formal-systems
status: draft
---

# Barrel Shifter and Rotation Circuits

## Core Idea
A barrel shifter performs multi-position shifts or rotations in a single clock cycle using cascaded multiplexers. Unlike a serial shifter that requires multiple cycles, a barrel shifter can shift by any amount (even 0) in parallel. Rotations are used in cryptographic algorithms and bit manipulation.

## Explainer

From your work with multiplexer circuits, you know that a **mux** selects one of several inputs based on a control signal. A barrel shifter is built entirely from multiplexers arranged in a clever pattern that decomposes an arbitrary shift into a sequence of power-of-two shifts, each handled by one layer of muxes — all operating in a single clock cycle with no feedback or sequential logic required.

Consider an 8-bit barrel shifter that must shift its input by any amount from 0 to 7 positions. The shift amount is a 3-bit binary number (e.g., shift by 5 = binary 101). The barrel shifter uses three stages, one for each bit of the shift amount. The first stage either shifts by 4 positions or passes the data through, controlled by bit 2 of the shift amount. The second stage either shifts by 2 or passes through, controlled by bit 1. The third stage either shifts by 1 or passes through, controlled by bit 0. A shift by 5 (101) activates the 4-shift stage and the 1-shift stage, producing a net shift of 5. Each stage is simply a row of 2-to-1 multiplexers — one per bit of the data word — where each mux chooses between the unshifted input and the shifted input for that stage.

This **logarithmic decomposition** is what makes barrel shifters fast. An n-bit shifter needs only log₂(n) stages, each adding one mux delay. A 32-bit barrel shifter uses 5 stages; a 64-bit shifter uses 6. The total delay is proportional to log₂(n) multiplexer delays rather than n clock cycles as a serial shift register would require. The tradeoff is area: the barrel shifter uses n × log₂(n) multiplexers, which is substantially more hardware than a simple shift register. But in a processor where shift and rotate instructions must complete in a single cycle, this area cost is well worth the speed.

The same structure supports **logical shifts** (fill vacated positions with zeros), **arithmetic shifts** (fill with the sign bit to preserve the sign of a two's complement number), and **rotations** (bits shifted out one end re-enter at the other). The difference is only in what value the multiplexers select for the vacated bit positions. For a logical left shift, zeros fill in from the right. For an arithmetic right shift, the sign bit (MSB) fills in from the left. For a rotation, the bits that would be shifted out wrap around to the opposite end. A single barrel shifter circuit with a few extra control signals can perform all these operations, which is why processors typically implement shifts and rotates with one shared barrel shifter inside the ALU rather than building separate circuits for each operation.
