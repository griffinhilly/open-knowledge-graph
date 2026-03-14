---
id: isentropic-efficiency-devices
title: Isentropic Efficiency of Turbines, Compressors, and Pumps
domain: engineering
course: thermodynamics-engineering
prerequisites:
- id: isentropic-process-reversible
  type: hard
tags:
- efficiency
- isentropic
- devices
stage: advanced
status: draft
---

# Isentropic Efficiency of Turbines, Compressors, and Pumps

## Core Idea
Isentropic efficiency compares actual device performance to an ideal isentropic process, quantifying the fraction of available energy extracted (turbines) or the additional work required (compressors). For a turbine, η_s = (actual work)/(isentropic work); for a pump or compressor, η_s = (isentropic work)/(actual work). Typical values range 0.75–0.95 depending on machine design and operating conditions.

## How It's Best Learned
Calculate isentropic work (assuming S = const) using property tables, then use actual outlet conditions to find actual work and efficiency. Recognize that turbine efficiency is always less than 100% (actual work less than isentropic), while compressor efficiency is also less than 100% (actual work greater than isentropic). Use typical efficiency values (0.85 for turbines, 0.80 for compressors) to estimate real performance when exact data is unavailable.

## Common Misconceptions
- Isentropic efficiency is the same for turbines and compressors; the definitions have numerator and denominator reversed.
- Improving isentropic efficiency requires only smoother passages; it also depends on Reynolds number, stage design, and multi-stage effects.
- An isentropic efficiency of 0.90 means 90% of energy is converted to useful work; it means the device extracts 90% of the maximum possible work in an ideal process.
