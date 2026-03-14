---
id: aliasing-reconstruction-signals
title: Aliasing, Anti-Aliasing Filters, and Signal Reconstruction
domain: engineering
course: signals-and-systems
prerequisites:
- id: sampling-theorem-nyquist-rate
  type: hard
builds-toward:
- digital-signal-processing-fundamentals
tags:
- aliasing
- anti-aliasing
- reconstruction
stage: advanced
status: draft
---

# Aliasing, Anti-Aliasing Filters, and Signal Reconstruction

## Core Idea
Aliasing occurs when sampling violates the Nyquist criterion, causing high-frequency components to 'fold back' into the passband as spurious low-frequency signals. Anti-aliasing filters remove high frequencies before sampling; reconstruction filters (interpolation) convert discrete signals back to continuous form while suppressing alias images.
