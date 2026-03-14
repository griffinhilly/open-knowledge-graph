---
id: interrupt-vector-dispatch
title: Interrupt Vector Tables and Dispatch
domain: computer-science
course: operating-systems
prerequisites:
- id: interrupt-exception-handling
  type: hard
- id: cpu-control-path-design
  type: soft
builds-toward:
- exception-handling-os-internals
tags:
- interrupts
- hardware
- dispatch
stage: formal-systems
status: draft
---

# Interrupt Vector Tables and Dispatch

## Core Idea
When a hardware interrupt or exception occurs, the CPU consults an interrupt vector table indexed by interrupt number to find the handler address. This enables the OS to dispatch control rapidly without querying what caused the interrupt.
