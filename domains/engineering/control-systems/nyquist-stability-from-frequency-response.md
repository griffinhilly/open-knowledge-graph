---
id: nyquist-stability-from-frequency-response
title: Nyquist Criterion and Stability from Frequency Response
domain: engineering
course: control-systems
prerequisites:
- id: frequency-response-magnitude-phase-basics
  type: hard
- id: gain-phase-margin-stability-measures
  type: soft
builds-toward:
- compensation-design-tradeoffs-cascadefeedback
tags:
- nyquist
- stability-criterion
- encirclement
- polar-plot
stage: abstract-reasoning
status: draft
---

# Nyquist Criterion and Stability from Frequency Response

## Core Idea
The Nyquist criterion states that the number of clockwise encirclements of the (-1, 0) point in the G(jω)H(jω) polar plot equals the number of unstable closed-loop poles. A stable open-loop system with M unstable poles requires M counterclockwise encirclements for closed-loop stability. This provides both a graphical and analytical stability test.
