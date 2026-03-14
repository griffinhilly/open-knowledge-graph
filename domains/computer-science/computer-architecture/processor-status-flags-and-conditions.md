---
id: processor-status-flags-and-conditions
title: Processor Status Flags and Condition Codes
domain: computer-science
course: computer-architecture
prerequisites:
- id: arithmetic-logic-unit-design-details
  type: hard
builds-toward:
- branch-instruction-execution
- exception-handling-architecture
tags:
- status-flags
- condition-codes
- program-status-register
stage: formal-systems
status: draft
---

# Processor Status Flags and Condition Codes

## Core Idea
Condition codes (stored in the processor status register) indicate the outcome of ALU operations: zero flag (result is zero), negative flag (sign bit set), overflow flag (signed arithmetic overflow), and carry flag (unsigned overflow). Conditional branch instructions test these flags to alter control flow. Some flags are set only on certain instruction types.
