---
id: multi-stage-amplifiers
title: Multi-Stage Amplifiers
domain: engineering
course: circuits-and-electronics
prerequisites:
- id: common-emitter-amplifier
  type: hard
- id: common-collector-amplifier
  type: soft
builds-toward:
- differential-amplifier-circuits
tags:
- cascading
- coupling-capacitors
- overall-gain
- loading-effect
- bandwidth
- cascade
- cascode
stage: formal-systems
status: draft
---

# Multi-Stage Amplifiers

## Core Idea
When a single amplifier stage cannot provide sufficient gain, bandwidth, or impedance characteristics, multiple stages are cascaded in series. The overall voltage gain is the product of individual stage gains, but each stage's output impedance loads the next stage's input impedance, reducing the effective gain below the product of unloaded gains. Coupling capacitors between stages block DC to preserve each stage's independent bias point while passing the AC signal. A common design pattern pairs a high-gain CE first stage with a CC (emitter follower) output stage — the CE provides voltage amplification while the CC provides low output impedance to drive the load without gain degradation. The overall bandwidth of a multi-stage amplifier is narrower than any individual stage because each stage's roll-off compounds, reducing the combined -3 dB bandwidth by a factor that depends on the number of identical stages. Cascode (CE + CB) and Darlington (CE + CC with shared collector) are specialized two-transistor configurations that achieve specific performance targets.

## How It's Best Learned
Analyze a two-stage CE-CC cascade by first solving each stage in isolation, then connecting them and accounting for loading. Compare the overall gain calculated as a simple product of individual gains versus the gain computed with inter-stage loading to see the discrepancy. Measure bandwidth of one, two, and three identical stages to observe the progressive bandwidth shrinkage.

## Common Misconceptions
- Multiplying unloaded stage gains to get overall gain — the output impedance of each stage forms a voltage divider with the input impedance of the next, reducing the effective gain at each interface.
- Assuming coupling capacitors have no effect on performance — they introduce low-frequency poles that raise the overall low-frequency cutoff, and each additional coupling capacitor adds another pole.
- Thinking more stages always improve performance — beyond a point, added stages reduce bandwidth, increase noise, and complicate bias design with diminishing gain returns.
