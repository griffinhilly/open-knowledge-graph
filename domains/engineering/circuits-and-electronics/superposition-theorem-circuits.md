---
id: superposition-theorem-circuits
title: Superposition Theorem
domain: engineering
course: circuits-and-electronics
prerequisites:
- id: circuit-variables-and-elements
  type: hard
- id: node-voltage-method
  type: soft
- id: mesh-current-method
  type: soft
builds-toward:
- thevenin-norton-equivalents
tags:
- linearity
- superposition
- multiple-sources
- dependent-sources
stage: formal-systems
status: validated
---

# Superposition Theorem

## Core Idea
In any linear circuit, the voltage or current at any element due to multiple independent sources equals the algebraic sum of the responses produced by each source acting alone. To isolate one independent source, all other independent voltage sources are replaced with short circuits and all other independent current sources with open circuits. Dependent sources are never deactivated — they remain active during every sub-analysis. Superposition follows directly from the linearity of Kirchhoff's laws and is foundational to Thevenin/Norton analysis.

## How It's Best Learned
Apply superposition to circuits with two or three sources and verify by comparing with full nodal or mesh analysis. Track reference directions carefully when summing partial responses — the algebraic sign of each contribution matters.

## Common Misconceptions
- Deactivating dependent sources along with independent sources — dependent sources must remain active throughout.
- Applying superposition to power, which is quadratic and nonlinear — powers from individual source contributions do not add to give total power.
- Forgetting to restore the circuit to its full topology between sub-analyses.
