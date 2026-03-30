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
status: validated
---

# Nichols Chart: Magnitude-Phase Design Tool

## Core Idea
The Nichols chart plots magnitude (dB) vs phase (degrees) on a single diagram with iso-magnitude and iso-phase contours for closed-loop response. It provides direct visualization of how loop gain and phase translate to closed-loop bandwidth and peak overshoot, enabling simultaneous optimization of both performance metrics.

## Questions

```yaml
- question: "A control engineer increases loop gain by 6 dB on a Nichols chart. What happens to the open-loop curve on the chart?"
  type: multiple-choice
  options:
    - "The entire curve shifts vertically upward by 6 dB while its horizontal position is unchanged"
    - "The entire curve shifts to the right by 6 degrees, increasing the phase margin"
    - "The curve rotates clockwise around the critical point at (−180°, 0 dB)"
    - "Only the high-frequency portion shifts; the low-frequency portion is unaffected by gain changes"
  answer: 0
  explanation: "On the Nichols chart, the vertical axis is open-loop magnitude in dB. A pure gain change multiplies all magnitudes by the same factor, which is a uniform vertical shift of the entire curve. Phase is unaffected by a real gain scalar, so the horizontal position stays fixed. This property makes gain tuning visually intuitive: you can slide the curve up or down and immediately read off the new performance from the fixed closed-loop contours."

- question: "A designer reads the Nichols chart and finds the open-loop curve is tangent to the M = 4 dB closed-loop contour near crossover. This indicates:"
  type: multiple-choice
  options:
    - "The closed-loop peak magnitude is 4 dB (about 59% overshoot), which likely exceeds typical specifications"
    - "The gain margin is exactly 4 dB, meaning the system has minimal stability robustness"
    - "The phase margin equals 4 degrees, which is dangerously small"
    - "The closed-loop bandwidth is 4 rad/s, independently of the crossover frequency"
  answer: 0
  explanation: "The M-contours on a Nichols chart are loci of constant closed-loop magnitude. Where the open-loop curve is tangent to a contour, that contour value is the peak closed-loop magnitude M_p. An M_p of ~1.3 dB corresponds to about 20% overshoot; 4 dB is much larger, indicating a significant resonance peak and likely excessive overshoot. The chart lets you read this directly without computing the closed-loop transfer function."

- question: "The M-contours and N-contours on a Nichols chart should be recalculated for each new plant, since they depend on the specific open-loop transfer function."
  type: true-false
  answer: false
  explanation: "The M- and N-contours are fixed curves derived from the algebra of the unity-feedback closed-loop formula T = G/(1 + G). They are universal for any unity-feedback system and do not depend on the specific plant G(s). This is precisely the chart's power: a precomputed overlay converts open-loop magnitude-phase coordinates directly to closed-loop performance metrics for any plant."

- question: "The Nichols chart allows a designer to simultaneously read gain margin, phase margin, and closed-loop peak overshoot from a single diagram."
  type: true-false
  answer: true
  explanation: "Gain margin is the vertical distance from the open-loop curve to 0 dB at the −180° phase crossing; phase margin is the horizontal distance from the curve to −180° at the 0 dB gain crossing; and the M-contour tangent to the curve gives the closed-loop peak M_p. All three are readable simultaneously from the same Nichols plot, which is its key advantage over separate Bode plots."

- question: "Why is the Nichols chart more useful for final design verification than for initially selecting the structure or poles/zeros of a compensator?"
  type: short-answer
  answer: "Because the Nichols chart shows how the combined open-loop curve relates to closed-loop performance, but it doesn't reveal how individual compensator poles or zeros contribute to the curve's shape. Root locus and Bode plots give better insight into the frequency-domain effect of specific compensator elements during initial design. Once the structure is fixed, the Nichols chart efficiently verifies that all simultaneous specs are met."
  explanation: "The Nichols chart is a verification and tuning tool. Its strength — showing all performance metrics at once — is also a limitation: the curve's shape is the result of the entire open-loop transfer function, so it's hard to diagnose which compensator element to change. Bode magnitude and phase plots make the contribution of individual poles and zeros transparent, making them better for initial compensator design."
```

## Explainer

From your work on gain and phase margins, you know that a closed-loop system's stability and performance are governed by its open-loop frequency response. Bode plots display gain and phase on two separate aligned axes — useful for understanding each individually but requiring mental effort to combine them. The **Nichols chart** places both on a single diagram: open-loop magnitude in dB on the vertical axis, open-loop phase in degrees on the horizontal axis. As frequency sweeps from zero to infinity, the open-loop response traces a single curve winding through this magnitude-phase plane.

What makes the chart powerful is a set of **fixed closed-loop contours** overlaid on the magnitude-phase space. The M-contours (constant closed-loop magnitude loci) and N-contours (constant closed-loop phase loci) of the unity-feedback transfer function T(jω) = G(jω)/(1 + G(jω)) are precomputed curves derived from the algebra of feedback. Because these contours are fixed in the magnitude-phase plane, wherever your open-loop curve passes through the chart, you can read off the corresponding closed-loop magnitude and phase directly — no calculation required. The **critical point** at (−180°, 0 dB) corresponds to the −1 point on the Nyquist diagram; gain margin is the vertical distance from the curve to 0 dB at −180°, and phase margin is the horizontal distance from the curve to −180° at 0 dB.

The design procedure is intuitive. You want the open-loop Nichols curve to pass through regions of the chart that map to acceptable closed-loop behavior: adequate closed-loop bandwidth (the frequency where the M-contour value equals −3 dB), acceptable **closed-loop peak magnitude** M_p (an M_p of approximately 1.3 dB corresponds to about 20% overshoot in the step response), and sufficient gain and phase margin. Adding a **lead compensator** rotates and shifts the curve rightward and upward near the crossover frequency, pulling it away from the critical point and reducing M_p. Adding a **lag compensator** slides the high-frequency portion of the curve downward, reducing gain while preserving phase near crossover.

The key advantage over separate Bode plots is **simultaneity**: you can see gain margin, phase margin, closed-loop bandwidth, and closed-loop peak overshoot all at once, making it easy to check that multiple specifications are satisfied simultaneously. Adjusting loop gain vertically shifts the entire curve up or down — you can immediately see how much gain can be added before hitting an unacceptable M_p contour. The limitation is that the Nichols chart is less intuitive for understanding the effect of individual compensator poles and zeros during initial design; Bode plots and root locus are more useful for that. Nichols charts are most valuable for final design verification and for tuning systems where compensator structure is already fixed and you need to optimize gain and frequency scaling.
