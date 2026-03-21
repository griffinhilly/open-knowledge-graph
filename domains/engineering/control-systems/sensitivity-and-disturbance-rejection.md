---
id: sensitivity-and-disturbance-rejection
title: Sensitivity and Disturbance Rejection
domain: engineering
course: control-systems
prerequisites:
- id: feedback-control-fundamentals
  type: hard
- id: transfer-functions-control
  type: hard
builds-toward:
- robust-control-basics
tags:
- sensitivity-function
- complementary-sensitivity
- disturbance-rejection
- noise-sensitivity
- bandwidth
- waterbed-effect
stage: advanced
status: draft
---

# Sensitivity and Disturbance Rejection

## Core Idea
The sensitivity function S(s) = 1/(1 + G(s)C(s)) and complementary sensitivity function T(s) = G(s)C(s)/(1 + G(s)C(s)) together characterize how a feedback system responds to disturbances, references, and model uncertainty, satisfying the fundamental constraint S(s) + T(s) = 1 at every frequency. S(jω) quantifies how disturbances at the plant output are attenuated by feedback: |S(jω)| < 1 means disturbance rejection, while |S(jω)| > 1 means disturbance amplification. T(jω) describes how sensor noise propagates to the output and also measures the system's sensitivity to multiplicative plant uncertainty. Good disturbance rejection requires |S(jω)| to be small at low frequencies (high loop gain), while noise rejection and robustness to uncertainty require |T(jω)| to be small at high frequencies (low loop gain). Since S + T = 1, these goals are complementary: one cannot make both small at the same frequency, establishing a fundamental design tradeoff. Bode's integral theorem (the waterbed effect) further constrains design: for systems with RHP poles or zeros, reducing |S| in one frequency band necessarily increases it in another, making the tradeoff inescapable.

## How It's Best Learned
Plot S(jω) and T(jω) for a simple feedback system as the controller gain varies, observing how increasing gain pushes |S| down at low frequencies but increases the peak of |S| near the crossover frequency. Then introduce a disturbance signal and a noise signal simultaneously and observe how the closed-loop output is affected at different frequencies, directly connecting the S and T magnitudes to physical behavior. Study the S + T = 1 constraint graphically to internalize why perfect disturbance rejection and perfect noise rejection are mutually exclusive.

## Common Misconceptions
- Making the loop gain as large as possible does not minimize sensitivity at all frequencies — it reduces |S| at low frequencies but causes |S| to peak above unity near the crossover frequency, potentially amplifying disturbances in that band.
- The sensitivity function S(s) is not the same as the closed-loop transfer function T(s) — S relates disturbances to output while T relates reference inputs to output, and they play complementary roles in the design.
- The waterbed effect is not just a theoretical curiosity — it means that control design is fundamentally about distributing sensitivity across frequency, not eliminating it, and aggressive disturbance rejection in one band always comes at the cost of amplification elsewhere.

## Questions

```yaml
- question: "An engineer increases controller gain tenfold, successfully reducing |S(jω)| from 0.3 to 0.05 at low frequencies, improving disturbance rejection there. What is the expected consequence near the crossover frequency?"
  type: multiple-choice
  options:
    - "|S(jω)| also decreases near crossover, providing uniform improvement across all frequencies"
    - "The system becomes unconditionally stable because higher gain improves phase margin"
    - "|S(jω)| peaks above 1 near the crossover frequency, meaning disturbances in that band are actually amplified by feedback"
    - "|T(jω)| decreases near crossover, providing better noise rejection at those frequencies"
  answer: 2
  explanation: "This is the S + T = 1 constraint made concrete. Reducing |S| at low frequencies by increasing gain improves disturbance rejection there, but the gain must eventually roll off at high frequencies to maintain stability. This rolloff forces |S| to peak above 1 somewhere near the crossover frequency — the region where the loop gain transitions from large to small. At those frequencies, |S| > 1 means feedback is actually amplifying disturbances rather than rejecting them. Making the loop gain very large at low frequencies therefore creates a sensitivity peak at crossover, not uniform improvement. Good design minimizes this peak (the sensitivity peak M_s) rather than ignoring it."

- question: "Bode's integral theorem — the 'waterbed effect' — states that for a stabilizable system, the integral of log|S(jω)| over all frequencies is constrained. What does this imply for control design?"
  type: multiple-choice
  options:
    - "Aggressive disturbance rejection in one frequency band necessarily creates sensitivity amplification in another band — sensitivity cannot be eliminated, only redistributed"
    - "Increasing bandwidth always increases the sensitivity peak, making high-bandwidth designs inherently dangerous for any plant"
    - "Plants with right-half-plane zeros are easier to control because they offer more design freedom in shaping the sensitivity function"
    - "The waterbed effect applies only to unstable plants; stable plants can achieve arbitrarily low sensitivity at all frequencies simultaneously"
  answer: 0
  explanation: "Bode's integral theorem formalizes the fundamental design tradeoff. For systems with sufficient high-frequency roll-off, the integral of log|S(jω)| over all frequencies equals zero (or is positive if the plant has right-half-plane poles, making the constraint even tighter). This means the 'area' under the log-sensitivity curve is fixed — pushing it down in one frequency range forces it up elsewhere, like pressing on a waterbed. The implication for design is that sensitivity cannot be eliminated; it can only be redistributed. Clever design allocates unavoidable amplification to frequency bands where it causes least harm."

- question: "Since S(s) + T(s) = 1 exactly at every frequency, a control engineer can make both |S(jω)| and |T(jω)| small simultaneously at any frequency of interest by choosing an appropriate controller."
  type: true-false
  answer: false
  explanation: "S + T = 1 is an algebraic identity that holds at every value of s — it is a constraint, not a goal. If |S(jω)| is made small at a frequency (say 0.1), then |T(jω)| must be close to 1 there, and vice versa. There is no controller that can make both magnitudes simultaneously small at the same frequency; the identity prevents it. This is why disturbance rejection (requiring small |S|) and noise rejection (requiring small |T|) are fundamentally conflicting goals at any given frequency, and why the crossover frequency — where the transition from large to small loop gain occurs — is the key design parameter."

- question: "The sensitivity function S(s) = 1/(1 + GC) measures how plant output disturbances propagate to the output: |S(jω)| < 1 means feedback reduces the disturbance, while |S(jω)| > 1 means feedback amplifies it at that frequency."
  type: true-false
  answer: true
  explanation: "|S(jω)| is the disturbance survival rate at frequency ω. If a 1 Hz disturbance enters the plant output and |S(j2π)| = 0.1, feedback reduces it to 10% of its original amplitude — 90% rejection. If |S(jω)| = 2, feedback doubles the disturbance amplitude at that frequency. This amplification occurs near the crossover frequency when gain is too aggressive at lower frequencies. The sensitivity function is therefore a frequency-resolved map of the feedback system's disturbance-handling capability, and its peak value M_s is both a disturbance amplification limit and a robustness measure."

- question: "Why does the constraint S(s) + T(s) = 1 mean that control system design is fundamentally about distributing sensitivity rather than eliminating it?"
  type: short-answer
  answer: "S + T = 1 is an algebraic identity holding at every frequency: whatever fraction of sensitivity is not in S is in T. Making |S| small at a frequency forces |T| large there, and vice versa. This means there is no controller that achieves low sensitivity simultaneously at all frequencies — the total is conserved. Control design is therefore a choice of where to place sensitivity: small |S| at low frequencies (to reject process disturbances) forces large |T| there (more noise passes through), while small |T| at high frequencies (to reject sensor noise) forces large |S| there. The waterbed effect tightens this further for plants with right-half-plane poles or zeros: even redistribution is constrained by the plant's unstable features. Good design chooses where the unavoidable sensitivity peaks are placed, not whether they exist."
  explanation: "This perspective reframes control design from 'minimize error' to 'allocate sensitivity wisely.' The crossover frequency is the primary knob: moving it up extends low-frequency disturbance rejection but brings the sensitivity peak to higher frequencies where it may interact with noise or model uncertainty. The sensitivity peak M_s is a measure of how tightly the Nyquist curve approaches the −1 point — a smaller M_s means more robustness to plant uncertainty. The design goal is a smooth, well-conditioned crossover with M_s controlled to an acceptable level, allocating the unavoidable sensitivity budget to the least harmful frequency band."
```

## Explainer

The sensitivity function emerges naturally from what you already know about feedback. Recall that in a closed-loop system the output depends on both the reference signal and any disturbances or noise that enter the plant. From your study of transfer functions and feedback fundamentals, you know that the closed-loop transfer function from reference to output is T(s) = GC/(1+GC). The **sensitivity function** S(s) = 1/(1+GC) describes something different: how disturbances injected at the plant output survive to appear at the output. If you notice that the denominator 1+GC is identical in both functions, you can immediately see why S + T = 1 — it is an algebraic identity, not an approximation, holding at every value of s.

Think of |S(jω)| as a frequency-resolved disturbance survival rate. If |S(jω)| = 0.1 at 1 Hz, a 1 Hz disturbance entering the plant is reduced to 10% of its original amplitude — feedback rejects 90% of it. If |S(jω)| = 2 at 100 Hz, feedback actually amplifies that disturbance twofold. Large loop gain GC makes |S| small: the denominator 1+GC is much larger than 1, so S ≈ 1/GC → 0. But large loop gain at all frequencies is impossible — the loop must roll off at high frequencies to prevent instability and to avoid amplifying sensor noise. The **complementary sensitivity function** T describes how measurement noise propagates to the output: large |T| means noise gets through; small |T| means noise is rejected. Since S + T = 1, whenever you push |S| down at a frequency you push |T| up there. You are never eliminating sensitivity — you are choosing where to place it.

Bode's integral theorem formalizes this into the **waterbed effect**: for a plant with sufficient high-frequency roll-off, the integral of log|S(jω)| over all frequencies is zero (or positive if the plant has right-half-plane poles). Pushing down on one part of the sensitivity curve forces another part to bulge upward. Physically, this means aggressive disturbance rejection in one frequency band creates a band where disturbances are amplified. The peak of |S| above unity — the **sensitivity peak M_s** — is also a robustness measure: a larger M_s means the closed loop is closer to instability as the plant model changes, since it corresponds geometrically to how close the Nyquist curve passes to the −1 point.

The practical design insight is to treat S and T as frequency response targets. You want |S| small in the low-frequency band where process disturbances concentrate (requiring high loop gain there) and |T| small at high frequencies where sensor noise dominates (requiring low loop gain there). The **crossover frequency** — where loop gain transitions from large to small — sets the system bandwidth. A well-designed compensator achieves a smooth crossover without an excessive M_s peak. Bode's integral theorem tells you the total "area" under log|S| is fixed by the plant's unstable poles — clever control design allocates that unavoidable sensitivity to the least harmful frequency range, rather than pretending it can be eliminated.
