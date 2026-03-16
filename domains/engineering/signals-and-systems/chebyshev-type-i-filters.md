---
id: chebyshev-type-i-filters
title: Chebyshev Type I Filter Design
domain: engineering
course: signals-and-systems
prerequisites:
- id: butterworth-analog-filter-design
  type: hard
- id: transfer-function-poles-zeros
  type: hard
builds-toward:
- elliptic-filter-design
- bilinear-transform-digital-filters
tags:
- filter-design
- chebyshev
- equiripple
- rolloff
stage: advanced
status: draft
---

# Chebyshev Type I Filter Design

## Core Idea
Chebyshev Type I filters achieve steeper rolloff than Butterworth by allowing equiripple magnitude response in the passband. The ripple level (typically 0.5–3 dB) is a tunable design parameter: higher ripple permits steeper rolloff. Poles lie on an ellipse in the s-plane according to Chebyshev polynomial roots, resulting in narrower transition bands for the same filter order.

## Explainer

From your study of Butterworth filters, you know that the Butterworth design achieves a **maximally flat** magnitude response in the passband — the frequency response is as flat as possible at DC and remains monotonically decreasing through the passband and into the stopband. This flatness is elegant, but it comes at a cost: the rolloff at the passband edge is relatively gradual for a given filter order, requiring higher order (more poles) to meet stringent stopband attenuation requirements. Chebyshev Type I filters make a different tradeoff — they intentionally introduce ripple in the passband to gain a steeper rolloff beyond it.

The key idea is **equiripple behavior**: the Chebyshev Type I filter's magnitude response oscillates between two bounds (1 and 1/√(1 + ε²), where ε controls the ripple level) throughout the passband, touching both bounds exactly N times for an Nth-order filter, then rolls off steeply. The ripple is "equal" in the sense that every oscillation reaches the same maximum and minimum — no part of the passband wastes allowable deviation. This is optimal in the minimax sense: among all Nth-order filters that meet the passband ripple constraint, the Chebyshev Type I has the best (steepest) rolloff. The mathematical basis is the **Chebyshev polynomial** T_N(x), which has the remarkable property of oscillating between −1 and +1 exactly N times on the interval [−1, 1] while growing faster than any other monic polynomial outside that interval.

The poles of a Chebyshev Type I filter lie on an **ellipse** in the s-plane, compared to the circle where Butterworth poles lie. The ellipse has its major axis along the imaginary axis (the poles are closer to the jω axis) and its minor axis along the real axis. Poles closer to the jω axis create a steeper, more resonant frequency response near the passband edge — which is what produces both the ripple in the passband and the steep rolloff beyond it. All poles are in the left half-plane (the filter is stable), and the filter is minimum-phase. From your knowledge of transfer function poles and zeros, you know that poles near the jω axis create peaks in the magnitude response, and the Chebyshev design precisely arranges these peaks to produce the equiripple pattern.

The design tradeoff is concrete: a 5th-order Butterworth filter with a 3 dB passband might achieve only 40 dB attenuation at twice the cutoff frequency, while a 5th-order Chebyshev Type I with 3 dB ripple can achieve 60 dB or more at the same frequency. Equivalently, to achieve a given stopband specification, Chebyshev often requires 1–2 fewer poles than Butterworth. The cost is passband ripple and nonlinear **phase response** (the Chebyshev phase response is more distorted than Butterworth's, which matters for applications sensitive to signal shape like pulse transmission). When you need steep rolloff and can tolerate some passband variation — as in many audio, RF, and anti-aliasing applications — Chebyshev Type I is often the practical choice.
