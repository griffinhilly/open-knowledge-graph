---
id: quadrature-modulation-iq-representation
title: Quadrature Modulation and I/Q Representation
domain: engineering
course: signals-and-systems
prerequisites:
- id: modulation-amplitude-frequency-shift-keying
  type: hard
- id: hilbert-transform-analytic-signals
  type: soft
builds-toward:
- phase-shift-keying-modulation
tags:
- modulation
- iq-modulation
- quadrature
- communication
stage: advanced
status: draft
---

# Quadrature Modulation and I/Q Representation

## Core Idea
Quadrature modulation uses two carriers in phase quadrature (90° apart) to transmit two information streams: s(t) = I(t)·cos(ωct) – Q(t)·sin(ωct). Complex notation s_c(t) = (I + jQ)·e^(jωct) simplifies analysis where s_c is the complex envelope. Demodulation by correlating with local carriers recovers I and Q components, enabling bandwidth-efficient communication.
