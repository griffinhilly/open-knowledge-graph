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
