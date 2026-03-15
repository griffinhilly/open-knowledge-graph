---
id: amperes-law
title: Ampère's Law
domain: physics
course: electricity-and-magnetism
prerequisites:
- id: biot-savart-law
  type: hard
- id: dot-product
  type: hard
- id: line-integrals-vector-fields
  type: soft
- id: curl-and-divergence
  type: soft
- id: curl-and-divergence-operators
  type: hard
builds-toward:
- maxwells-equations-overview
- magnetic-flux-and-induction
tags:
- Ampere-law
- solenoid
- toroid
- symmetry
- magnetostatics
stage: formal-systems
status: validated
---

# Ampère's Law

## Core Idea
Ampère's law states that the line integral of B around any closed Amperian loop equals μ₀ times the total current enclosed: ∮ B · dl = μ₀I_enc. It is the magnetic analog of Gauss's law — mathematically equivalent to Biot-Savart for steady currents but far more powerful when symmetry is present. It is used to find B inside a solenoid (B = μ₀nI), a toroid, or near a long straight wire without integration.

## How It's Best Learned
Study the three canonical applications: infinite straight wire, infinite solenoid, and toroid. For each, identify the Amperian loop shape (circle or rectangle) that exploits symmetry to simplify ∮ B · dl before evaluating I_enc.

## Common Misconceptions
- Like Gauss's law for E, Ampère's law is always valid but only simplifies calculation when symmetry exists.
- For a solenoid, B outside is approximately zero, not because of shielding but because of field cancellation from all loops.
- Ampère's law in this form applies only to magnetostatics; Maxwell added the displacement current term to generalize it.
