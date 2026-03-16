---
id: bode-plot-stability-analysis
title: Bode Plot Stability Analysis
domain: engineering
course: control-systems
prerequisites:
- id: frequency-response-and-bode-plots
  type: hard
- id: transfer-functions-control
  type: hard
- id: logarithms-intro
  type: hard
- id: operations-with-complex-numbers
  type: soft
builds-toward:
- nyquist-stability-criterion
- gain-and-phase-margins
- lead-lag-compensators
tags:
- bode-plot
- crossover-frequency
- loop-gain
- open-loop
- frequency-domain
stage: advanced
status: validated
---

# Bode Plot Stability Analysis

## Core Idea
Bode plot stability analysis applies the open-loop frequency response G(jω)H(jω) to assess closed-loop stability without solving for closed-loop poles. The gain crossover frequency ωgc is where the open-loop magnitude equals 0 dB, and the phase crossover frequency ωpc is where the phase equals −180°. For minimum-phase systems in a unity feedback loop, closed-loop stability requires that the phase at ωgc exceeds −180° and the gain at ωpc is below 0 dB. These crossover relationships define the gain and phase margins, which quantify how much additional gain or phase lag the system can tolerate before becoming unstable.

## How It's Best Learned
Sketch asymptotic Bode plots for several open-loop transfer functions and identify crossover frequencies by hand. Compare with computed Bode plots to calibrate the accuracy of asymptotic approximations, especially near corners.

## Common Misconceptions
- Bode's stability criterion applies directly only to minimum-phase, single-loop systems — non-minimum-phase systems (with RHP zeros or time delays) require the Nyquist criterion.
- A large gain margin alone does not guarantee a robust design — both gain and phase margins must be adequate (typical targets: GM > 6 dB, PM > 45°).
- The Bode plot used for stability analysis is the open-loop transfer function G(jω)H(jω), not G(jω) alone when H ≠ 1.

## Explainer

Your prerequisites give you two tools: transfer functions describe how a system maps input to output in the Laplace domain, and Bode plots show the magnitude and phase of a system's frequency response. Bode plot stability analysis combines these to answer a practical question without solving for closed-loop poles directly: will a unity feedback loop with plant G(s) be stable?

The key insight is what happens when a signal travels around the feedback loop. A sinusoidal input at frequency ω gets multiplied in magnitude by |G(jω)H(jω)| and shifted in phase by ∠G(jω)H(jω) on each trip around the loop. If the loop gain equals exactly 1 (0 dB) and the phase shift equals exactly −180°, then the signal fed back is an inverted copy of itself at full strength — which, because of the subtraction in the negative feedback summing junction, actually *adds* to the input rather than subtracting. The system reinforces itself without bound: that is instability. Bode stability analysis amounts to checking how close the system comes to this critical condition.

The **gain crossover frequency** ωgc is where the open-loop magnitude first crosses 0 dB. The **phase margin** (PM) is how far the phase at ωgc is from −180°: PM = 180° + ∠G(jωgc)H(jωgc). A positive phase margin means that at the frequency where the loop gain is 1, the phase has not yet reached −180° — there is angular "room" before instability. The **phase crossover frequency** ωpc is where the phase first hits −180°. The **gain margin** (GM) is how far the magnitude at ωpc is from 0 dB, expressed in dB: GM = −20 log₁₀|G(jωpc)H(jωpc)|. A positive gain margin means the loop gain at the critical phase is below 1 — the system would need more gain before going unstable.

Reading margins off a Bode plot is fast and visual: find the 0 dB crossing and read the phase; find the −180° crossing and read the magnitude. But the interpretation requires care. Both margins must be adequate simultaneously — a large gain margin with a small phase margin (or vice versa) still produces a poorly damped, nearly unstable design. Standard targets of GM > 6 dB and PM > 45° are rules of thumb that correspond to reasonable closed-loop damping ratios. The method only applies directly to **minimum-phase** systems — those with no right-half-plane zeros and no time delays — because only those systems have phase that is uniquely determined by the magnitude response. Systems with time delays or RHP zeros need the Nyquist criterion, which Bode is a simplified version of.
