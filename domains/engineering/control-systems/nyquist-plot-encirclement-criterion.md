---
id: nyquist-plot-encirclement-criterion
title: Nyquist Plot and Encirclement Criterion
domain: engineering
course: control-systems
prerequisites:
- id: nyquist-stability-criterion
  type: hard
- id: sinusoidal-response-magnitude-phase-angle
  type: hard
builds-toward:
- gain-margin-phase-margin-stability
tags:
- nyquist-diagram
- encirclement
- stability-test
- closed-loop-poles
- frequency-response
stage: abstract-reasoning
status: draft
---

# Nyquist Plot and Encirclement Criterion

## Core Idea
The Nyquist criterion states: the closed-loop system is stable if and only if the plot of G(jω) encircles the point −1 a number of times equal to the number of RHP poles in the open-loop transfer function G(s). This elegant result connects open-loop frequency response to closed-loop stability.
