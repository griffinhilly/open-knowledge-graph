---
id: shift-register-design
title: Shift Register Design and Applications
domain: computer-science
course: computer-architecture
prerequisites:
- id: flip-flops-and-latches
  type: hard
- id: sequential-circuit-design
  type: soft
builds-toward:
- state-machine-in-processor-design
tags:
- sequential-circuits
- shift-register
- serial-parallel
stage: formal-systems
status: draft
---

# Shift Register Design and Applications

## Core Idea
A shift register is a chain of flip-flops that shifts data left or right. Serial-in, parallel-out (SIPO) shift registers convert serial data to parallel; parallel-in, serial-out (PISO) do the reverse. Shift registers are used for serial communication, pattern detection, and controlling sequencing of operations.
