---
id: pole-zero-plot-stability-analysis
title: Pole-Zero Plots and Stability Analysis
domain: engineering
course: signals-and-systems
prerequisites:
- id: transfer-function-poles-zeros
  type: hard
builds-toward:
- nyquist-stability-analysis-systems
- first-order-systems-frequency-response
tags:
- pole-zero-plot
- stability
- lti-systems
stage: advanced
status: validated
---

# Pole-Zero Plots and Stability Analysis

## Core Idea
Pole locations in the s-plane determine system stability: poles in the left half-plane give stable systems, poles on the imaginary axis give marginally stable systems, and poles in the right half-plane give unstable systems. The pole-zero plot is a graphical representation of H(s) that reveals these properties immediately.

## Explainer

From your study of transfer functions, you know that a system's transfer function H(s) is a ratio of polynomials: H(s) = N(s)/D(s). The **zeros** are the values of s where N(s) = 0 (H(s) = 0), and the **poles** are the values of s where D(s) = 0 (H(s) → ∞). These are generally complex numbers, living in the **s-plane** — a two-dimensional coordinate system where the horizontal axis is the real part of s (σ) and the vertical axis is the imaginary part (jω). The pole-zero plot places all poles (marked ×) and zeros (marked ○) in this plane, creating a visual fingerprint of the system.

**Why poles determine stability.** The natural response of a system — what it does when disturbed with no ongoing input — is determined entirely by its poles. Each pole at s = σ + jω contributes a natural mode of the form e^(σt)·cos(ωt + φ). The real part σ controls whether the mode grows or decays: if σ < 0, e^(σt) → 0 and the mode dies out (stable); if σ = 0, e^(σt) = 1 and the mode oscillates forever without decay (marginal stability); if σ > 0, e^(σt) → ∞ and the mode grows without bound (unstable). This is why the left half-plane — where Re(s) < 0 — is the "stable" region. A single right-half-plane pole makes the entire system unstable, regardless of where the other poles are.

**Reading the pole-zero plot.** Look at where the poles sit. If all poles are in the left half-plane, the system is **asymptotically stable** — all natural responses decay to zero. The distance of a pole from the imaginary axis (its real part magnitude |σ|) tells you how fast it decays: poles far to the left (large negative σ) correspond to fast, highly damped modes; poles close to the imaginary axis correspond to slow, lightly damped oscillations. Complex conjugate pole pairs (which always come in conjugate pairs for systems with real coefficients) produce oscillatory responses: a pair at σ ± jω_d oscillates at frequency ω_d and decays at rate |σ|. The ratio of σ to the distance from the origin (the pole magnitude) is the **damping ratio** ζ — a pair on the imaginary axis has ζ = 0 (pure oscillation), and a pair on the negative real axis has ζ = 1 (critically damped).

**Zeros and their role.** Zeros do not affect stability — they cannot send a bounded input to ∞ — but they profoundly shape the system's frequency response and transient behavior. A zero near a pole partially "cancels" that pole's contribution to the output, reducing the visibility of that natural mode. Zeros on the imaginary axis create exact notch frequencies where the output is zero regardless of input magnitude. Right-half-plane (RHP) zeros create **non-minimum phase behavior**: the step response initially moves in the wrong direction before settling correctly (think of backing up a trailer, where turning the wheel right first moves the trailer left). RHP zeros place fundamental limits on achievable closed-loop bandwidth in control design.

**From plot to system behavior at a glance.** The pole-zero plot lets you read off stability, oscillation frequencies, damping ratios, and resonance peaks without solving differential equations. A system with poles at −1 ± j5 has a natural oscillation at 5 rad/s with moderate damping (σ/|s| = 1/√26 ≈ 0.2, so ζ ≈ 0.2). Moving those poles to −0.1 ± j5 makes the system lightly damped — nearly oscillating. Moving them to +0.1 ± j5 makes it unstable. This geometric intuition builds the foundation for root locus analysis (how poles move as a gain parameter varies) and Nyquist stability analysis (whether a feedback loop stabilizes or destabilizes a plant) — both of which reason directly in the s-plane.

## Questions

```yaml
- question: "A system has poles at s = −2 and s = 1 + j3. Is the system stable? Explain."
  type: short-answer
  answer: "No. The pole at s = 1 + j3 has a positive real part (σ = +1), placing it in the right half-plane. This contributes a growing mode e^t·cos(3t + φ), which grows without bound. A single RHP pole is sufficient to make the system unstable regardless of where other poles are."
  explanation: "Stability requires ALL poles in the open left half-plane. The pole at s = −2 contributes a decaying mode (stable), but the pole at s = 1 + j3 contributes an exponentially growing oscillation. The system's output will diverge for any nonzero initial condition or input."

- question: "Two systems have complex pole pairs: System A at −0.5 ± j10, System B at −5 ± j10. Compare their transient responses."
  type: short-answer
  answer: "Both oscillate at approximately 10 rad/s, but System A decays much more slowly (time constant 1/0.5 = 2 s) with low damping ratio ζ ≈ 0.05, showing many cycles before settling. System B decays rapidly (time constant 1/5 = 0.2 s) with ζ ≈ 0.45, settling in less than one oscillation cycle."
  explanation: "The imaginary part of the pole determines the oscillation frequency (~ω_d ≈ Im(s) for lightly damped systems). The real part magnitude |σ| is the decay rate — larger |σ| means faster decay. System A's poles are close to the imaginary axis (lightly damped resonance); System B's poles are far left (heavily damped, fast settling). In a Bode plot, System A would show a sharp resonance peak near 10 rad/s; System B would show a broad, low peak."
```
