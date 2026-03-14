---
id: compensation-design-tradeoffs-cascadefeedback
title: 'Compensation Design: Cascade vs. Feedback Control Tradeoffs'
domain: engineering
course: control-systems
prerequisites:
- id: pole-placement-observer-design
  type: hard
- id: gain-phase-margin-stability-measures
  type: soft
- id: root-locus-asymptote-centroid-breakaway
  type: soft
tags:
- compensation
- cascade-control
- feedback-control
- design-tradeoffs
stage: concrete-application
status: draft
---

# Compensation Design: Cascade vs. Feedback Control Tradeoffs

## Core Idea
Cascade compensation (series controller) provides loop shaping via Bode plots; feedback compensation (unity feedback plus compensator) separates error signal. Cascade excels at disturbance rejection; feedback excels at reference tracking and model uncertainty. Most systems use both: inner feedback loop + outer cascade compensator. Design must balance speed, bandwidth, robustness, and noise sensitivity.
