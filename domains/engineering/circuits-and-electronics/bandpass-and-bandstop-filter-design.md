---
id: bandpass-and-bandstop-filter-design
title: Bandpass and Bandstop Filter Design
domain: engineering
course: circuits-and-electronics
prerequisites:
- id: first-order-passive-filters
  type: hard
- id: second-order-passive-filters
  type: hard
builds-toward:
- filter-selection-and-practical-applications
tags:
- bandpass
- bandstop
- notch
- cascade-filters
stage: formal-systems
status: draft
---

# Bandpass and Bandstop Filter Design

## Core Idea
Bandpass filters allow frequencies within a passband while rejecting others; the passband width and center frequency are set by component values. Bandstop (notch) filters do the opposite. Practical designs cascade first-order and second-order stages to achieve the desired attenuation slope and selectivity. The resonance characteristics of RLC circuits are exploited to create sharp transitions.
