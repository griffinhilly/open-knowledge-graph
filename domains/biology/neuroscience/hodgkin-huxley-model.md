---
id: hodgkin-huxley-model
title: The Hodgkin-Huxley Model
domain: biology
course: neuroscience
prerequisites:
- id: cable-theory-axonal-conduction
  type: hard
- id: voltage-gated-sodium-channels
  type: hard
- id: voltage-gated-potassium-channels
  type: hard
builds-toward:
- action-potential-initiation
- action-potential-repolarization
tags:
- hh-model
- conductance
- gating-variables
stage: advanced
status: draft
---

# The Hodgkin-Huxley Model

## Core Idea
The Hodgkin-Huxley model captures action potential generation using differential equations for voltage-dependent sodium and potassium conductances. Gating variables (m, h, n) describe channel opening probability: dV/dt = (gL(EL−V) + gNam³h(ENa−V) + gKn⁴(EK−V) + Iapp)/Cm. This minimal model explains threshold, regenerative firing, and refractory periods.

## How It's Best Learned
Implement HH equations numerically. Vary parameters and observe emergent behaviors like threshold-spike response.

## Common Misconceptions
HH fully explains neuronal firing. HH is a conductance-based approximation valid near rest. Different neurons require modified parameters.
