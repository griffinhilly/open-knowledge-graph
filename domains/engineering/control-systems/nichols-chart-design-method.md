---
id: nichols-chart-design-method
title: 'Nichols Chart: Magnitude-Phase Design Tool'
domain: engineering
course: control-systems
prerequisites:
- id: gain-phase-margin-stability-measures
  type: hard
- id: frequency-response-magnitude-phase-basics
  type: soft
builds-toward:
- compensation-design-tradeoffs-cascadefeedback
tags:
- nichols-chart
- magnitude-phase
- closed-loop-response
- design
stage: advanced
status: draft
---

# Nichols Chart: Magnitude-Phase Design Tool

## Core Idea
The Nichols chart plots magnitude (dB) vs phase (degrees) on a single diagram with iso-magnitude and iso-phase contours for closed-loop response. It provides direct visualization of how loop gain and phase translate to closed-loop bandwidth and peak overshoot, enabling simultaneous optimization of both performance metrics.

## Explainer

From your work on gain and phase margins, you know that a closed-loop system's stability and performance are governed by its open-loop frequency response. Bode plots display gain and phase on two separate aligned axes — useful for understanding each individually but requiring mental effort to combine them. The **Nichols chart** places both on a single diagram: open-loop magnitude in dB on the vertical axis, open-loop phase in degrees on the horizontal axis. As frequency sweeps from zero to infinity, the open-loop response traces a single curve winding through this magnitude-phase plane.

What makes the chart powerful is a set of **fixed closed-loop contours** overlaid on the magnitude-phase space. The M-contours (constant closed-loop magnitude loci) and N-contours (constant closed-loop phase loci) of the unity-feedback transfer function T(jω) = G(jω)/(1 + G(jω)) are precomputed curves derived from the algebra of feedback. Because these contours are fixed in the magnitude-phase plane, wherever your open-loop curve passes through the chart, you can read off the corresponding closed-loop magnitude and phase directly — no calculation required. The **critical point** at (−180°, 0 dB) corresponds to the −1 point on the Nyquist diagram; gain margin is the vertical distance from the curve to 0 dB at −180°, and phase margin is the horizontal distance from the curve to −180° at 0 dB.

The design procedure is intuitive. You want the open-loop Nichols curve to pass through regions of the chart that map to acceptable closed-loop behavior: adequate closed-loop bandwidth (the frequency where the M-contour value equals −3 dB), acceptable **closed-loop peak magnitude** M_p (an M_p of approximately 1.3 dB corresponds to about 20% overshoot in the step response), and sufficient gain and phase margin. Adding a **lead compensator** rotates and shifts the curve rightward and upward near the crossover frequency, pulling it away from the critical point and reducing M_p. Adding a **lag compensator** slides the high-frequency portion of the curve downward, reducing gain while preserving phase near crossover.

The key advantage over separate Bode plots is **simultaneity**: you can see gain margin, phase margin, closed-loop bandwidth, and closed-loop peak overshoot all at once, making it easy to check that multiple specifications are satisfied simultaneously. Adjusting loop gain vertically shifts the entire curve up or down — you can immediately see how much gain can be added before hitting an unacceptable M_p contour. The limitation is that the Nichols chart is less intuitive for understanding the effect of individual compensator poles and zeros during initial design; Bode plots and root locus are more useful for that. Nichols charts are most valuable for final design verification and for tuning systems where compensator structure is already fixed and you need to optimize gain and frequency scaling.
