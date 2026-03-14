---
id: phase-shift-keying-modulation
title: Phase Shift Keying Modulation
domain: engineering
course: signals-and-systems
prerequisites:
- id: quadrature-modulation-iq-representation
  type: hard
tags:
- psk
- bpsk
- qpsk
- modulation
- communication
stage: advanced
status: draft
---

# Phase Shift Keying Modulation

## Core Idea
Phase Shift Keying (PSK) encodes information in carrier phase: s(t) = A·cos(ωct + φ[n]) for symbol n. BPSK uses two phases (0, π), QPSK uses four phases at π/4, 3π/4, 5π/4, 7π/4, and M-ary PSK extends to M phases. Demodulation uses phase-locked loops or matched filters matched to each constellation point.
