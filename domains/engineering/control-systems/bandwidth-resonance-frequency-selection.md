---
id: bandwidth-resonance-frequency-selection
title: Bandwidth and Resonant Frequency Selection
domain: engineering
course: control-systems
prerequisites:
- id: frequency-response-magnitude-phase
  type: hard
- id: frequency-response-magnitude-phase-basics
  type: soft
builds-toward:
- control-loop-design-via-bode-plots
tags:
- bandwidth
- resonance
- peak
- magnitude-response
- frequency-domain-performance
stage: advanced
status: validated
---
# Bandwidth and Resonant Frequency Selection

## Core Idea
Bandwidth is the frequency at which magnitude drops to −3 dB (0.707 times the DC value). It indicates how fast a system can respond to changing reference inputs. Resonant peaks indicate underdamped modes; peak height increases as damping decreases.

## Questions

```yaml
- question: "A control engineer increases the gain of a feedback controller, moving the closed-loop poles closer to the imaginary axis. What effect does this have on the closed-loop frequency response?"
  type: multiple-choice
  options:
    - "Bandwidth decreases and the resonant peak shrinks — higher gain stabilizes the system"
    - "Bandwidth increases and the resonant peak grows — faster response comes with more oscillatory behavior"
    - "Bandwidth increases but the resonant peak is unchanged — bandwidth and damping are independent"
    - "Both bandwidth and resonant peak decrease — the system becomes slower but more stable"
  answer: 1
  explanation: "Increasing controller gain pushes closed-loop poles toward the imaginary axis. This has two simultaneous effects: the bandwidth (−3 dB frequency) increases — the system can track faster reference signals — but the poles' real part decreases, meaning less damping. Less damping produces a higher resonant peak in the frequency response and more overshoot in the step response. This is the fundamental bandwidth-resonance tradeoff: aggressive bandwidth comes at the cost of oscillatory transient behavior and, eventually, instability."

- question: "A closed-loop system's frequency response shows a resonant peak of +6 dB above its DC gain. What does this predict about the system's step response?"
  type: multiple-choice
  options:
    - "The step response will reach steady-state in exactly 6% of the natural period with no overshoot"
    - "The step response will exhibit roughly 30% overshoot"
    - "The step response will be critically damped — the +6 dB peak indicates optimal damping"
    - "The step response cannot be predicted from the frequency response alone"
  answer: 1
  explanation: "There is a direct correspondence between frequency-domain resonant peaks and time-domain overshoot. A +6 dB peak (magnitude 2× DC gain) corresponds to a damping ratio of approximately ζ ≈ 0.26, which yields about 30% overshoot on a step input. This frequency-to-time-domain mapping is why control designers work on Bode plots: specifications written in the time domain (overshoot < 15%) translate directly into frequency-domain constraints (M_p < 3–4 dB), allowing design and verification in the frequency domain before implementation."

- question: "The bandwidth of a closed-loop system is the frequency at which the magnitude response drops to half its DC gain value."
  type: true-false
  answer: false
  explanation: "This is a common confusion. Bandwidth is defined as the −3 dB frequency — the point where magnitude drops to 0.707 (1/√2) times the DC gain, not half (0.5). The −3 dB criterion is chosen because power is proportional to amplitude squared: at 0.707 amplitude, the output power has dropped to (0.707)² = 0.5, i.e., half the input power. The '−3 dB bandwidth' is therefore a half-power bandwidth. Confusing half-amplitude (−6 dB) with the standard bandwidth criterion leads to incorrect speed specifications."

- question: "A resonant peak in the closed-loop frequency response that exceeds the DC gain (i.e., M_p > 0 dB) indicates that the system is underdamped and will likely produce overshoot in the step response."
  type: true-false
  answer: true
  explanation: "A resonant peak exceeding 0 dB means the closed-loop gain at some frequency is greater than the DC gain — the system amplifies certain frequencies rather than merely attenuating them. This occurs when the closed-loop poles are underdamped (small damping ratio ζ), and it directly predicts overshoot in the time domain. Peaks above +3 to +6 dB (depending on application) indicate very underdamped behavior and often signal proximity to stability margins. This makes the resonant peak a direct design metric for transient performance."

- question: "Explain why increasing bandwidth in a closed-loop control system tends to increase overshoot in the step response, and what this implies for control design."
  type: short-answer
  answer: "Increasing bandwidth requires moving closed-loop poles to higher frequencies, which typically moves them closer to the imaginary axis (reducing their real part, hence reducing damping). Underdamped poles create a resonant peak in the frequency response and overshoot in the step response. The practical implication is a tradeoff: to track faster reference signals (high bandwidth) while maintaining acceptable transient behavior (limited overshoot), the designer must actively manage damping — for example, by using lead compensators or pole-zero cancellation to move poles along constant-damping-ratio lines rather than just closer to the imaginary axis."
  explanation: "This bandwidth-resonance tradeoff is central to classical control design. It explains why simply increasing gain to improve speed eventually leads to instability: the bandwidth rises, the resonant peak grows, overshoot increases, and eventually the system oscillates continuously. The design challenge is achieving the required bandwidth while keeping the resonant peak (and thus overshoot) within specification — which requires shaping the loop gain with a compensator, not just adjusting a single gain knob."
```

## Explainer

From your study of frequency response and Bode plots, you know how to compute and plot a system's gain and phase as a function of frequency — the magnitude plot showing |G(jω)| and the phase plot showing ∠G(jω). Bandwidth and resonance are the two most important features to read off those plots when assessing how a system will perform in closed-loop operation.

**Bandwidth** (ω_BW) is the frequency at which the closed-loop magnitude response drops to −3 dB, which corresponds to a gain of 0.707 (or 1/√2) relative to the DC value. The −3 dB criterion is not arbitrary: it is the frequency at which output power has dropped to half of its DC value (since power is proportional to amplitude squared). Below the bandwidth, the system tracks reference inputs faithfully — a sinusoidal command at frequency ω < ω_BW produces a nearly full-amplitude output. Above the bandwidth, the system cannot keep up: output amplitude shrinks and phase lag increases, meaning fast reference changes are partially or fully filtered out. Bandwidth is therefore a direct measure of **speed**: a wider bandwidth means the system can track faster-changing references. Practically, doubling the bandwidth roughly halves the rise time of the step response.

**Resonant peaks** in the frequency response appear when the system has **underdamped poles** — complex conjugate poles whose real part is small relative to their imaginary part. A second-order system with natural frequency ω_n and damping ratio ζ has a closed-loop frequency response that peaks near ω_n when ζ < 1/√2 ≈ 0.707. The peak magnitude is **M_p = 1/(2ζ√(1−ζ²))**, which grows without bound as ζ → 0. A resonant peak in the frequency response translates directly into overshoot in the step response: a system whose magnitude peaks at +6 dB will produce roughly 30% overshoot on a step input. This is the critical link between the frequency domain (where controller design happens) and the time domain (where performance specifications are written).

The **tradeoff between bandwidth and resonance** is central to control design. Increasing controller gain generally pushes the closed-loop bandwidth higher — faster tracking — but also brings the closed-loop poles closer to the imaginary axis, increasing the resonant peak and overshoot. Aggressive bandwidth comes at the cost of oscillatory transient behavior, noise sensitivity (high-frequency disturbances are amplified near the resonant peak), and eventually instability. The practical design goal is to achieve the bandwidth required by the speed specification while keeping M_p below about 3–6 dB (corresponding to ζ ≥ 0.35–0.5), ensuring acceptable damping. Resonant peaks at or above 0 dB — meaning the magnitude response exceeds DC gain at some frequency — indicate very underdamped behavior and often signal that the design is approaching instability margins.
