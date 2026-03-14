---
id: phase-locked-loops-synchronization
title: Phase-Locked Loops for Synchronization
domain: engineering
course: signals-and-systems
prerequisites:
- id: feedback-control-fundamentals
  type: hard
- id: phase-shift-keying-modulation
  type: soft
tags:
- pll
- frequency-synchronization
- feedback
- control
stage: advanced
status: draft
---

# Phase-Locked Loops for Synchronization

## Core Idea
A Phase-Locked Loop synchronizes a local oscillator to an incoming signal using feedback. The phase detector produces error proportional to phase difference; the loop filter shapes dynamics to control acquisition speed and tracking bandwidth; the voltage-controlled oscillator adjusts frequency in response. PLLs enable demodulation, frequency synthesis, and clock recovery in communication systems.
