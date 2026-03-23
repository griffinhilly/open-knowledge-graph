---
id: nyquist-stability-analysis-systems
title: Nyquist Criterion for Stability Analysis
domain: engineering
course: signals-and-systems
prerequisites:
- id: bode-plot-construction-interpretation
  type: hard
- id: pole-zero-plot-stability-analysis
  type: hard
tags:
- nyquist-criterion
- stability
- feedback-systems
stage: expert
status: draft
---

# Nyquist Criterion for Stability Analysis

## Core Idea
The Nyquist criterion uses the frequency response H(jω) plotted in the complex plane to determine closed-loop stability without explicitly computing poles. Encirclements of the (-1, 0) point indicate instability; gain and phase margins measure robustness to perturbations.

## Questions

```yaml
- question: "A feedback system has a stable open-loop transfer function (P = 0). The Nyquist plot makes one clockwise encirclement of (-1, 0). What does the Nyquist criterion conclude about the closed-loop system?"
  type: multiple-choice
  options:
    - "The closed-loop system is stable — one encirclement is within tolerance for a stable open-loop system"
    - "The closed-loop system is unstable: N = Z - P gives Z = 1 + 0 = 1, meaning one unstable closed-loop pole exists"
    - "Stability cannot be determined from the Nyquist plot alone without also examining the Bode plot"
    - "The system is marginally stable — encirclements only indicate instability if the plot passes through (-1, 0)"
  answer: 1
  explanation: "For a stable open-loop system (P = 0), closed-loop stability requires N = 0: no net encirclements of (-1, 0). Any clockwise encirclement means N > 0, so Z = N + P = 1 + 0 = 1: one unstable closed-loop pole. The Nyquist criterion determines both stability and the count of unstable closed-loop poles from the encirclement number alone, with no need to compute the closed-loop transfer function or find its poles explicitly."

- question: "A Bode analysis shows a gain margin of 12 dB and phase margin of 50° — apparently robust. Under which scenario would this Bode analysis give a misleading stability conclusion?"
  type: multiple-choice
  options:
    - "When the loop gain is very high, making the system sensitive to small parameter variations"
    - "When the open-loop transfer function has right-half-plane poles, because Bode margin analysis implicitly assumes a stable minimum-phase open-loop system and cannot account for the counterclockwise encirclements needed to stabilize an open-loop unstable plant"
    - "When the system has more than two poles, since Bode plots become unreliable for higher-order systems"
    - "When both margins exceed standard thresholds, Bode analysis always correctly certifies stability"
  answer: 1
  explanation: "Bode gain and phase margins are derived under the assumption that the open-loop system is minimum-phase and stable (P = 0). For such systems, the standard Nyquist condition is N = 0 and Bode margins measure distance from the critical point. But if the open-loop system has P unstable poles, closed-loop stability requires N = -P (counterclockwise encirclements). Bode margins interpret the absence of encirclements as stability — which is wrong when encirclements are required. A conditionally stable system can fool Bode analysis entirely."

- question: "The Nyquist criterion not only determines whether a closed-loop system is stable but also specifies exactly how many unstable closed-loop poles it has."
  type: true-false
  answer: true
  explanation: "From N = Z - P, where N is the net clockwise encirclement count and P is the known number of open-loop RHP poles, Z = N + P gives the exact count of closed-loop RHP poles. This is more information than most stability tests: the Routh-Hurwitz criterion only tells you whether all poles are in the left half plane; Nyquist tells you exactly how many are not."

- question: "A feedback system with a gain margin greater than 6 dB is guaranteed to be robustly stable against all reasonable plant variations."
  type: true-false
  answer: false
  explanation: "Gain margin measures robustness along only one dimension — how much gain can increase before instability. A system can have a large gain margin but a small or negative phase margin (stable but fragile against phase delay), or vice versa. Real plant variations typically affect both gain and phase simultaneously, so neither margin alone guarantees robustness. Standard design guidelines require both: gain margin > 6 dB AND phase margin > 45°. Additionally, these margins each apply at one crossover frequency; non-minimum-phase systems can have multiple crossings requiring examination of the full Nyquist plot."

- question: "Explain why the Nyquist criterion is strictly more general than Bode analysis for determining closed-loop stability, and describe one class of systems where relying on Bode margins alone could lead to an incorrect stability conclusion."
  type: short-answer
  answer: "Bode analysis is a special case of Nyquist analysis valid only when the open-loop system is stable and minimum-phase (P = 0). In that case, N = 0 is necessary and sufficient for closed-loop stability, and Bode margins measure the geometric distance from the critical point. Nyquist handles the general case via N = Z - P. One class where Bode fails: plants with open-loop RHP poles (unstable plants being stabilized by feedback, such as an inverted pendulum or an aircraft with unstable aerodynamics). For these systems, closed-loop stability requires counterclockwise encirclements (N < 0). A Bode analysis would flag the absence of clockwise encirclements as stable, but a negative-N condition (counterclockwise encirclements present) would be wrongly interpreted as unstable. Another failure case: conditionally stable systems where the closed loop is stable only within a range of gains — Bode margins at one crossover frequency miss the second instability at higher gain."
  explanation: "The Nyquist criterion's generality comes from the argument principle, which makes no assumptions about the location of open-loop poles."
```

## Explainer

From Bode plot analysis, you know how to read gain and phase margins from frequency response graphs — those margins tell you how far the open-loop response is from the instability boundary at −1. From pole-zero analysis, you know that a closed-loop system is stable if and only if all its poles lie in the left half of the s-plane. The **Nyquist criterion** unifies these ideas, giving a rigorous test for closed-loop stability based only on the open-loop frequency response, without ever computing the closed-loop poles explicitly.

The mathematical foundation is the **argument principle** from complex analysis: if a function F(s) is analytic inside a closed contour in the s-plane, the number of times F(s) encircles the origin as s traverses the contour equals Z − P, where Z and P are the numbers of zeros and poles of F(s) inside the contour. For stability analysis, define F(s) = 1 + G(s)H(s) — the characteristic polynomial of the closed loop. The **Nyquist contour** encloses the entire right half plane (the region of instability). A closed-loop pole in the RHP is a zero of F(s) = 1 + G(s)H(s), which is equivalent to a zero of G(s)H(s) = −1. So counting encirclements of the point (−1, 0) in the G(s)H(s)-plane as s traverses the Nyquist contour gives N = Z − P, where Z is the number of unstable closed-loop poles and P is the number of unstable open-loop poles. For a stable closed loop, Z must equal zero: **N = −P** (counterclockwise encirclements equal the number of open-loop RHP poles, if any).

The practical recipe: plot G(jω)H(jω) as ω sweeps from 0 to +∞, then mirror (conjugate) to get −∞ to 0, and close the contour at infinity. Count net clockwise encirclements of (−1, 0). For a system with no open-loop RHP poles (P = 0), any clockwise encirclement means instability. For a system with P open-loop RHP poles (an unstable plant, for example), you need exactly P counterclockwise encirclements for stability. This is more powerful than Bode analysis alone: Bode margins implicitly assume a minimum-phase, stable open-loop system, while Nyquist handles non-minimum-phase plants and conditionally stable systems (where increasing gain actually stabilizes the loop) correctly.

**Gain margin** and **phase margin** have precise geometric meaning on the Nyquist plot. The gain margin is the factor by which gain can increase before the Nyquist plot crosses through (−1, 0) — equivalently, 1/|G(jω_pc)| where ω_pc is the phase crossover frequency (where phase = −180°). The phase margin is how many additional degrees of phase lag would move the unit-circle crossing of the Nyquist plot to exactly (−1, 0). Both margins measure the distance from the plot to the critical point, giving robustness to gain uncertainty and phase delay respectively. A well-designed feedback system typically targets gain margin > 6 dB and phase margin > 45°, ensuring the system can tolerate significant plant uncertainty or additional actuator lag before going unstable.
