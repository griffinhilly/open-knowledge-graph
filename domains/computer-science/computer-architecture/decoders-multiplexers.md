---
id: decoders-multiplexers
title: Decoders, Encoders, and Multiplexers
domain: computer-science
course: computer-architecture
prerequisites:
- id: universal-logic-gates
  type: hard
- id: combinational-circuit-design
  type: soft
builds-toward:
- memory-array-organization
- instruction-fetch-decode-execute
tags:
- decoders
- encoders
- multiplexers
- combinational
stage: formal-systems
status: draft
---

# Decoders, Encoders, and Multiplexers

## Core Idea
Decoders convert binary input to one-hot output (one wire high per input code), encoders do the reverse, and multiplexers select one of many inputs based on a control signal. These are fundamental selection and routing components in memory and CPU design.

## How It's Best Learned
Design 2-to-4 decoder and 4-to-1 multiplexer from gates; observe how they scale to larger widths.

## Common Misconceptions
A decoder activates exactly one output for each input. Encoders assume only one input is high at a time. Multiplexers are data routers, not logic gates.
