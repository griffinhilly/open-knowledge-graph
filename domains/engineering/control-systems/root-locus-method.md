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
- id: complex-plane
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

## Explainer

From the Routh-Hurwitz criterion, you can determine whether a closed-loop system is stable for a given gain. But Routh-Hurwitz gives you a yes/no answer about stability — it doesn't show you *how* the poles are moving or whether increasing gain makes the system faster, slower, or more oscillatory. The **root locus** provides the full picture: it traces every closed-loop pole position simultaneously as gain K varies from zero to infinity.

The starting logic is straightforward. For a unity-feedback loop with forward gain K·G(s), the closed-loop poles satisfy 1 + K·G(s) = 0, or equivalently G(s) = −1/K. As K → 0, the closed-loop poles approach the open-loop poles of G(s) (because small K means weak feedback and the loop barely closes). As K → ∞, the closed-loop poles must approach the open-loop zeros or escape to infinity along asymptotes (because infinite gain would force G(s) = 0 at some finite s, which occurs at zeros). Between these extremes, the poles trace continuous paths in the s-plane — one path per open-loop pole, starting at each pole and ending at each zero or at infinity. The **angle condition** ∠G(s) = ±180° is the membership test: a point s₀ is on the locus if and only if the product of angles from all open-loop zeros to s₀ minus the sum of angles from all poles to s₀ equals an odd multiple of 180°. This geometric condition is the locus's definition.

The construction rules make sketching tractable without solving high-degree polynomials. The real-axis rule — locus exists to the left of an odd count of real poles and zeros — follows directly from the angle condition on the real axis, where all angles are 0° or 180°. The asymptote angles (180°(2k+1)/(n−m) for k = 0, 1, ...) and centroid ((Σpoles − Σzeros)/(n−m)) tell you where locus branches escaping to infinity are headed, which reveals whether high gain drives the system unstable. A locus branch crossing the imaginary axis means a pair of poles is becoming purely imaginary — marginally stable. You can find the crossing gain from Routh-Hurwitz, connecting the two tools you know.

The power of the root locus for design lies in its visual directness. A glance at the locus tells you whether increasing gain stabilizes or destabilizes the system, where the dominant poles (closest to the imaginary axis) sit and therefore what the transient response looks like, and at what gain the system becomes unstable. More importantly, when a simple gain adjustment cannot place the poles where you need them, the locus reveals *why* — and adding a compensator pole or zero reshapes the entire locus, physically pulling branches toward better regions of the s-plane. The **lead compensator** (zero to the left of the dominant poles, pole further left) rotates the locus toward the left half-plane, improving speed and damping. The **lag compensator** improves steady-state error without significantly altering dynamic response. The root locus is not just an analysis tool — it is the geometric language of classical compensator design.
