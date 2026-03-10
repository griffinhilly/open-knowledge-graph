---
id: operational-amplifier-fundamentals
title: Operational Amplifier Fundamentals
domain: engineering
course: circuits-and-electronics
prerequisites:
- id: ac-circuit-analysis-methods
  type: hard
- id: node-voltage-method
  type: hard
- id: bjt-amplifier-configurations
  type: soft
builds-toward:
- op-amp-circuit-applications
tags:
- op-amp
- ideal-op-amp
- virtual-short
- virtual-ground
- negative-feedback
- inverting-amplifier
- non-inverting-amplifier
stage: formal-systems
status: draft
---

# Operational Amplifier Fundamentals

## Core Idea
An operational amplifier is a high-gain differential voltage amplifier with two inputs (inverting − and non-inverting +) and one output. The ideal op-amp model assumes infinite open-loop gain, infinite input impedance, and zero output impedance. With negative feedback, these idealizations yield two analysis rules: (1) the differential input voltage is virtually zero — the inputs are at equal voltage (virtual short), and (2) no current enters either input terminal (virtual open). Applying these rules reduces any linear op-amp circuit to a straightforward KCL problem. The inverting amplifier has gain −R_f/R_in; the non-inverting amplifier has gain 1 + R_f/R_in.

## How It's Best Learned
Apply the virtual short and virtual open rules systematically to the inverting and non-inverting configurations before memorizing the gain formulas — the formulas follow directly from KCL. Practice identifying which op-amp terminal connects to signal ground for each topology.

## Common Misconceptions
- Applying the virtual short rule to the output terminal — it applies only between the two input terminals.
- Assuming the ideal model is always accurate — real op-amps have finite gain-bandwidth product, slew rate, offset voltage, and cannot drive the output beyond the supply rails.
- Thinking virtual short means the input terminals are physically connected — they are at the same potential, but no current passes between them.
