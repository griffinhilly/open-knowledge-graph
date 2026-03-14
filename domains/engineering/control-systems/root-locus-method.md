---
id: root-locus-method
title: Root Locus Method
domain: engineering
course: control-systems
prerequisites:
- id: routh-hurwitz-criterion
  type: hard
- id: complex-numbers-intro
  type: hard
- id: transfer-functions-control
  type: hard
builds-toward:
- root-locus-controller-design
- state-feedback-pole-placement
tags:
- root-locus
- pole-migration
- asymptotes
- breakaway-points
- angle-condition
stage: advanced
status: validated
---

# Root Locus Method

## Core Idea
The root locus is a graphical method showing how closed-loop poles migrate in the complex s-plane as the gain parameter K varies from 0 to ∞. Starting at the open-loop poles (K=0) and terminating at the open-loop zeros or infinity (K→∞), the locus is symmetric about the real axis and satisfies the angle condition ∠G(s)H(s) = ±180°(2k+1). Key construction rules include: number of branches equals number of open-loop poles; asymptote angles are 180°(2k+1)/(n−m); the centroid of asymptotes is (Σpoles − Σzeros)/(n−m); real-axis locus exists to the left of an odd count of open-loop poles and zeros. The root locus provides immediate visual insight into how gain affects stability and dominant transient behavior.

## How It's Best Learned
Sketch loci by hand using the construction rules before verifying with MATLAB's rlocus() or Python's control.root_locus(). Focus on understanding why the angle condition governs locus membership rather than memorizing rules in isolation.

## Common Misconceptions
- The locus exists on the real axis to the left of an odd number of open-loop poles and zeros combined, not just between adjacent poles.
- Breakaway points are found from dK/ds = 0 (or equivalently d/ds[1/G(s)H(s)] = 0), not from the angle condition alone.
- The root locus only shows the effect of scalar gain K; adding poles or zeros to the compensator reshapes the entire locus, which is the basis of compensator design.
