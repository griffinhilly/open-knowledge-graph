---
id: time-domain-response-second-order
title: Second-Order System Time Response
domain: engineering
course: control-systems
prerequisites:
- id: time-domain-response-first-order
  type: hard
- id: second-order-transient-circuits
  type: soft
- id: simple-harmonic-motion
  type: soft
- id: second-order-system-damping-ratio
  type: soft
builds-toward:
- steady-state-error-analysis
- routh-hurwitz-criterion
- pid-control
tags:
- damping-ratio
- natural-frequency
- percent-overshoot
- settling-time
- second-order
stage: advanced
status: validated
---
# Second-Order System Time Response

## Core Idea
A standard second-order system has the transfer function G(s) = ωₙ²/(s² + 2ζωₙs + ωₙ²), characterized by natural frequency ωₙ and damping ratio ζ. The damping ratio determines qualitative behavior: underdamped (ζ < 1) produces oscillatory overshoot, critically damped (ζ = 1) gives the fastest non-overshooting response, and overdamped (ζ > 1) gives a sluggish monotone response. Key performance metrics — percent overshoot (%OS = e^{−πζ/√(1−ζ²)}×100), rise time, peak time Tₚ = π/ωd, and settling time Ts ≈ 4/(ζωₙ) — are analytically derivable from ζ and ωₙ. Most control design specifications are stated in terms of these metrics.

## How It's Best Learned
Plot step responses for ζ = 0.1, 0.5, 0.707, 1.0, and 2.0 to internalize how damping affects behavior. Derive the overshoot formula and settling time approximation so they become second nature — these are the most frequently used formulas in control design.

## Common Misconceptions
- Critically damped (ζ = 1) is not always the best choice — ζ ≈ 0.7 often gives a better tradeoff between speed and overshoot in practice.
- The overshoot and settling time formulas apply to the ideal second-order prototype; additional poles or zeros change these predictions significantly.
- Natural frequency ωₙ is not the oscillation frequency of the step response; the damped natural frequency ωd = ωₙ√(1−ζ²) is the actual oscillation rate.

## Questions

```yaml
- question: "A second-order system has ωₙ = 10 rad/s and ζ = 0.6. A step input is applied. At what frequency does the step response oscillate?"
  type: multiple-choice
  options:
    - "10 rad/s — that is the natural frequency of the system"
    - "6 rad/s — the product ζ × ωₙ gives the oscillation frequency"
    - "8 rad/s — the damped natural frequency ωd = ωₙ√(1 − ζ²) = 10√(1 − 0.36) ≈ 8 rad/s"
    - "The response does not oscillate because ζ = 0.6 is nearly critically damped"
  answer: 2
  explanation: "The natural frequency ωₙ is the frequency of oscillation only when there is *no damping* (ζ = 0). In an underdamped system (0 < ζ < 1), damping slows the oscillation: the actual frequency is the damped natural frequency ωd = ωₙ√(1−ζ²). For ζ = 0.6: ωd = 10√(1−0.36) = 10√0.64 = 10 × 0.8 = 8 rad/s. Confusing ωₙ with ωd is a frequent error — ωₙ appears in the transfer function and performance formulas, but ωd is what you observe in the actual oscillation. Note that ζ = 0.6 is well underdamped and will oscillate; critical damping (ζ = 1) would produce no oscillation."

- question: "A control system specification requires settling within 2 seconds and less than 5% overshoot. A designer is choosing between ζ = 1.0 (critically damped) and ζ = 0.707 (underdamped). Which choice is likely better?"
  type: multiple-choice
  options:
    - "ζ = 1.0 is always the best choice — it never overshoots and thus guarantees the <5% overshoot specification without any risk"
    - "ζ = 0.707 is likely better — it produces only ~4.3% overshoot (within spec) and typically settles faster than the critically damped case at the same ωₙ, meaning it can meet both specs simultaneously"
    - "ζ = 1.0 settles faster than ζ = 0.707 because it doesn't waste time in oscillation, so it better satisfies the settling time requirement"
    - "ζ = 0.707 cannot be used because any underdamped system violates an overshoot specification by definition"
  answer: 1
  explanation: "The common misconception is that critically damped = best. ζ = 1.0 achieves the absolute minimum overshoot (zero), but it approaches the final value asymptotically and can actually have a *longer* settling time than a lightly underdamped system. ζ ≈ 0.707 produces only ~4.3% overshoot — within the <5% spec — while the response reaches and stays within the settling band faster. The settling time formula Ts ≈ 4/(ζωₙ) shows that at the same ωₙ, ζ = 0.707 settles faster than ζ = 1.0. ζ ≈ 0.707 is the near-optimal tradeoff point for many practical specifications."

- question: "The natural frequency ωₙ is the frequency at which an underdamped second-order system actually oscillates in its step response."
  type: true-false
  answer: false
  explanation: "ωₙ is the *undamped* natural frequency — the oscillation rate only when ζ = 0 (no damping). In any real underdamped system (0 < ζ < 1), the actual oscillation frequency is the damped natural frequency ωd = ωₙ√(1−ζ²), which is always less than ωₙ. For example, at ζ = 0.5, ωd = ωₙ√(1−0.25) = 0.866ωₙ — about 13% slower than ωₙ. At ζ = 0.9, ωd = ωₙ√(1−0.81) ≈ 0.436ωₙ — dramatically slower. Only as ζ → 0 does ωd → ωₙ. The peak time formula Tₚ = π/ωd correctly uses ωd for this reason."

- question: "For a second-order system, increasing the damping ratio ζ while holding the natural frequency ωₙ constant will reduce overshoot but will generally increase the settling time."
  type: true-false
  answer: true
  explanation: "Both settling time and overshoot are functions of ζ and ωₙ, but they trade off against each other as ζ changes at fixed ωₙ. Overshoot %OS = e^(−πζ/√(1−ζ²)) × 100 strictly decreases as ζ increases — more damping means less overshoot. Settling time Ts ≈ 4/(ζωₙ) at first decreases as ζ increases from 0 (more damping helps), but for ζ > 1 the system is overdamped and settles sluggishly — the formula no longer strictly applies, but the qualitative effect is that very high ζ is slow. Near ζ ≈ 0.707, settling time is near its minimum for a given ωₙ, which is why this value represents a practical optimum balancing both specifications."

- question: "Explain why ζ ≈ 0.707 is often preferred over ζ = 1.0 (critically damped) in practical control system design, even though critical damping guarantees zero overshoot."
  type: short-answer
  answer: "Critically damped (ζ = 1.0) approaches the final value without overshooting, but does so asymptotically and slowly for the settling band. ζ ≈ 0.707 overshoots by only ~4.3% — within most engineering tolerances — but reaches and stays within the ±2% settling band faster at the same ωₙ. It represents the minimum settling time near-optimal tradeoff: fast response, acceptably small overshoot, and clean settling."
  explanation: "The numerical comparison: for a system with ωₙ = 10 rad/s, the 2% settling time at ζ = 1.0 is roughly Ts ≈ 6/ωₙ = 0.6 s (using the exact formula for critically damped), while at ζ = 0.707 it is Ts ≈ 4/(ζωₙ) = 4/(0.707×10) ≈ 0.57 s — faster. In the s-plane, ζ = 0.707 corresponds to poles at 45° from the negative real axis, which is the geometric sweet spot between poles that are too close to the imaginary axis (oscillatory) and poles that are too close to the real axis (slow). This value appears so often in control design that experienced engineers recognize it immediately."
```

## Explainer

From your study of first-order systems, you know that a single time constant τ fully describes how fast a system approaches its final value — the response is always a decaying exponential, never oscillatory. A second-order system introduces a new possibility: the system can overshoot its target and ring back and forth before settling. This happens because a second-order system has energy storage in two different elements (think of a mass with both spring and dashpot), and those elements can exchange energy with each other. The two parameters that replace τ are the **natural frequency** ωₙ and the **damping ratio** ζ.

The natural frequency ωₙ sets the intrinsic speed of the system — how fast it would oscillate if there were no damping at all (ζ = 0). Think of it as the frequency of an undamped spring-mass system from your simple harmonic motion prerequisite. The damping ratio ζ measures how aggressively the system dissipates energy relative to that natural oscillation. When ζ = 0, the system oscillates forever. When ζ = 1 (**critically damped**), dissipation exactly prevents any overshoot. When ζ > 1 (**overdamped**), the system is sluggish — imagine a door closer in thick oil. The most practically useful regime is **underdamped** (0 < ζ < 1), where the system overshoots but settles quickly. The actual oscillation frequency you observe in the step response is the **damped natural frequency** ωd = ωₙ√(1−ζ²), which is always lower than ωₙ because damping slows the oscillations.

The performance metrics follow directly from ζ and ωₙ. **Percent overshoot** depends only on ζ: %OS = e^(−πζ/√(1−ζ²)) × 100. This is a pure function of ζ — if you want less than 5% overshoot, you need ζ > 0.69. **Peak time** Tₚ = π/ωd tells you when the first overshoot peak occurs — it decreases as ωd increases, meaning a faster (higher ωₙ) or less-damped system peaks sooner. **Settling time** Ts ≈ 4/(ζωₙ) depends on both parameters: to settle faster, you need either more damping or a higher natural frequency. This is the essential design tradeoff — ζ controls the overshoot; ωₙ scales the overall speed.

The value ζ ≈ 0.707 (= 1/√2) deserves special attention. It is not critically damped, but it achieves a near-optimal compromise: the step response is fast, the overshoot is only about 4.3%, and the settling is clean. Many practical specifications target this region. In the s-plane, increasing ωₙ moves the closed-loop poles radially outward (faster), while increasing ζ rotates them toward the negative real axis (less oscillatory). When you move to designing controllers like PID, every gain adjustment is really an attempt to place those poles at the right combination of ωₙ and ζ — so internalizing the relationship between pole location and these time-domain metrics is foundational to everything that follows.
