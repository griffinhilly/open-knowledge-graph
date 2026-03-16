---
id: root-locus-pole-placement
title: Root Locus Method and Pole Placement Design
domain: engineering
course: control-systems
prerequisites:
- id: root-locus-method
  type: hard
- id: time-domain-performance-specifications
  type: hard
builds-toward:
- state-feedback-control-design
tags:
- root-locus
- pole-placement
- design
- controller
stage: advanced
status: draft
---

# Root Locus Method and Pole Placement Design

## Core Idea
Root locus plots closed-loop pole locations as a function of controller gain K, showing how poles move with tuning. Designer specifies desired pole locations (based on rise time, overshoot, settling time specs) and reads required gain from the locus. Root locus enables interactive design: visualizing stability boundaries, identifying achievable performance limits, and systematically trading off performance metrics.

## Explainer

From your study of the root locus method, you know that as controller gain K varies from zero to infinity, the closed-loop poles trace continuous paths in the s-plane — starting at the open-loop poles (K=0) and ending at the open-loop zeros (K→∞) or going to infinity along asymptotes. Root locus **pole placement** turns this observation into a design procedure: instead of accepting whatever poles a given K produces, you specify where you *want* the closed-loop poles to be, then determine what K (and possibly what controller structure) achieves them.

The connection to your time-domain performance specifications is direct. From that prerequisite, you know that a second-order closed-loop system with poles at σ ± jω_d has rise time ∝ 1/(ω_d), percent overshoot determined by the **damping ratio** ζ = cos(θ) where θ is the angle of the pole from the negative real axis, and settling time ∝ 1/σ. These geometric relationships transform performance specs into a target region in the s-plane. "No more than 10% overshoot" means the poles must lie within a cone defined by ζ ≥ 0.59 (angle ≤ 54° from the negative real axis). "Settling time under 2 seconds" means the real part of the poles must satisfy σ ≥ 2. The intersection of these constraints defines a **feasible region** for the desired poles.

The design question is then: does the root locus pass through (or near) that feasible region? If yes, read off the value of K where the locus crosses the region and you're done — proportional gain alone achieves the desired poles. If no, the locus misses the target region entirely, which means proportional gain is insufficient and you need to reshape the locus by adding poles or zeros via a **lead**, **lag**, or **PD controller**. Adding a zero to the open-loop transfer function attracts the locus branches toward it; adding a pole pushes branches away. The design cycle is: draw the locus, check if it hits the target region, if not add compensation to reshape the locus, repeat.

A critical insight is that root locus only controls where the **dominant poles** land — the poles closest to the imaginary axis that dominate the transient response. If other poles lie far to the left, their contribution decays so fast that the time-domain response is governed almost entirely by the dominant pair. This approximation is valid when non-dominant poles are at least 3–5 times further left than the dominant poles. If additional poles crowd near the dominant pair, the higher-order terms contribute meaningfully and the second-order approximations from your specifications will be inaccurate. Verifying the dominant-pole assumption — by simulating the full system response — is the check that closes the design loop.
