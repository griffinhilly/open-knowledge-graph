---
id: resonance-and-resonance-frequency
title: Resonance and Resonance Frequency
domain: physics
course: classical-mechanics
prerequisites:
- id: driven-harmonic-oscillator
  type: hard
- id: complex-numbers-intro
  type: soft
- id: phase-and-amplitude-forced-oscillations
  type: soft
tags:
- resonance
- oscillations
- frequency
- amplification
stage: formal-systems
status: validated
---

# Resonance and Resonance Frequency

## Core Idea
Resonance occurs when the driving frequency matches the natural frequency (or close to it), producing a large-amplitude steady-state oscillation. The sharpness and height of the resonance peak depend on damping: less damping yields a sharper, taller peak (high quality factor Q). Resonance is exploited in radio tuning and mechanical systems but must be avoided in structures (buildings, bridges) to prevent dangerous vibrations.

## Questions

```yaml
- question: "A radio receiver circuit has a very high quality factor Q. Compared to a circuit with low Q tuned to the same frequency, how does it behave when exposed to multiple nearby radio signals?"
  type: multiple-choice
  options:
    - "It responds equally strongly to all frequencies near its resonance — the high Q makes it more sensitive overall"
    - "It has a broad, low resonance peak, providing equal amplification across a wide frequency band"
    - "It has a sharp, tall resonance peak, responding strongly to its target frequency and weakly to nearby frequencies — enabling selective tuning"
    - "It resonates at a much lower frequency than a low-Q circuit, because high Q reduces the resonance frequency"
  answer: 2
  explanation: "High Q means low damping: the oscillator rings for a long time when struck and has a narrow, tall resonance peak. For a radio receiver, this means strong response at the target frequency and rapid falloff at adjacent frequencies — exactly the selectivity needed to tune to one station while ignoring others. A low-Q circuit (heavily damped) would have a broad, flat peak, responding to many nearby frequencies with roughly equal strength — good for shock absorption but terrible for frequency selection. High Q = high selectivity = sharp tuning."

- question: "A child is being pushed on a swing. Each push is timed to coincide with the swing reaching its maximum backward height. Over time, the swing's amplitude grows. Why does timing the pushes this way produce growth, while random timing does not?"
  type: multiple-choice
  options:
    - "Pushes at the maximum height add maximum potential energy, which accumulates regardless of the swing's natural frequency"
    - "Random timing averages to zero net energy, while synchronized pushing consistently adds energy in phase with the natural motion, allowing amplitude to build"
    - "The swing's natural frequency changes as amplitude grows, and timed pushes track this changing frequency"
    - "Random pushes cancel the swing's motion by sometimes pushing against it, while timed pushes prevent any cancellation at all"
  answer: 1
  explanation: "Resonance is about consistent, in-phase energy transfer. When pushes are synchronized with the natural period (pushing when the swing moves away), each push adds a fixed amount of energy to the oscillation. Over many cycles, energy accumulates and amplitude grows. With random timing, pushes sometimes add energy (in phase) and sometimes remove it (out of phase) — these effects average out, leaving amplitude roughly constant. The natural frequency ω₀ is not the frequency where you push hardest; it is the frequency at which energy addition is consistently constructive rather than partially canceling."

- question: "In an underdamped oscillator, the steady-state amplitude at the resonance peak increases as damping decreases."
  type: true-false
  answer: true
  explanation: "This is the defining behavior of resonance in damped systems. The steady-state amplitude at driving frequency ω is proportional to F₀/m divided by |ω₀² − ω² + iγω|. At resonance (ω ≈ ω₀), the first term in the denominator vanishes and the amplitude is governed by the damping term γω₀. Smaller γ (less damping) means smaller denominator, which means larger amplitude. In the limit of zero damping, the amplitude at resonance grows without bound. Damping limits the resonance peak — it is both what keeps resonance from being infinite and what determines the Q factor."

- question: "The resonance frequency of a damped oscillator is exactly equal to its natural frequency ω₀, regardless of the amount of damping present."
  type: true-false
  answer: false
  explanation: "For a damped driven oscillator, the frequency of maximum steady-state amplitude — the resonance frequency — is not exactly ω₀, but ω_res = √(ω₀² − γ²/2), which is slightly below ω₀. Damping shifts the peak downward. For light damping (high Q), this shift is negligible, and ω_res ≈ ω₀ to excellent approximation. But as damping increases, the shift becomes significant and the peak also broadens and lowers. In the limit of very heavy damping, the resonance peak disappears entirely. The approximation ω_res ≈ ω₀ is useful but not exact."

- question: "Explain why resonance can be both deliberately exploited and deliberately avoided in engineering, and give an example of each use case."
  type: short-answer
  answer: "Resonance is exploited when large-amplitude response to a small driving force is desired. In a radio receiver, a high-Q circuit resonates at one frequency to select that carrier signal from background noise. In musical instruments, air columns and strings are designed to resonate at specific frequencies to amplify sound. Resonance is avoided when large oscillations would be destructive. Bridges, buildings, and mechanical structures must have natural frequencies far from typical driving frequencies (traffic, wind, seismic activity) to prevent runaway oscillation — the Tacoma Narrows Bridge collapsed when wind drove oscillations near a structural resonance. The same principle (driving frequency matching natural frequency → large amplitude) is a tool when controlled and a hazard when not."
  explanation: "The key is that resonance itself is neither good nor bad — it is a physical phenomenon whose consequences depend on context. Whether you want to amplify a signal (radio), sustain a tone (instrument), or prevent catastrophic vibration (structure) determines whether resonance is the goal or the danger."
```

## Explainer

From driven harmonic oscillators, you know the setup: a mass-spring system (or equivalent) with natural frequency ω₀, damping coefficient γ, driven by an external periodic force F₀cos(ωt). The steady-state amplitude depends on both ω and ω₀. **Resonance** is the phenomenon that occurs when these frequencies nearly coincide — and understanding why amplitudes become large at resonance is the physical heart of the concept.

The intuition is about energy transfer. When you push a child on a swing, you push in time with the swing's natural motion. Each push adds energy to the oscillation; the amplitude grows. If you pushed randomly — sometimes with the swing, sometimes against it — energy would average out and amplitude would stay small. Resonance is the perfect synchronization of driving force and natural motion: energy pumped in from the driving force is consistently reinforced rather than periodically canceled, so amplitude grows until damping limits it. The **resonance frequency** (strictly, the frequency of maximum amplitude) is close to ω₀ — slightly shifted by damping, but approaching ω₀ as damping decreases toward zero.

The **quality factor Q** encodes the sharpness of resonance. A high-Q oscillator has low damping: it rings for a long time when struck, has a sharp resonance peak (large amplitude near ω₀, small amplitude far from it), and tunes selectively. A radio receiver circuit is a high-Q oscillator tuned to resonate at a specific carrier frequency — it responds strongly to that frequency and weakly to all others, implementing frequency selection. A low-Q oscillator (heavily damped, like a car's shock absorber) has a broad, low resonance peak; it damps vibrations across a wide frequency range rather than selectively amplifying one. Q characterizes both frequency selectivity and the duration of free oscillation: Q ≈ ω₀τ/2 where τ is the decay time.

Complex numbers illuminate resonance cleanly. A sinusoidal driving force can be written as Re[F₀e^{iωt}], and the steady-state response as Re[A(ω)e^{iωt}]. The complex amplitude A(ω) = F₀/m(ω₀² − ω² + iγω) is a rational function of ω. Its magnitude |A(ω)| is the actual oscillation amplitude; its phase gives the lag between force and response. The resonance peak is where the denominator |ω₀² − ω² + iγω| is minimized — visually, where the pole of A(ω) in the complex ω-plane is closest to the real axis. This pole structure elegantly captures both the location and width of the resonance peak.

Resonance is ubiquitous and consequential. In structural engineering it is a hazard: the Tacoma Narrows Bridge collapse (1940) involved wind-driven oscillation near a structural resonance frequency. In medical imaging, nuclear magnetic resonance (NMR/MRI) drives proton spins at their resonance frequency to generate tissue images. In lasers and optical cavities, resonance conditions determine which wavelengths are amplified. In music, resonance amplifies strings, air columns, and drum heads. The principle is always the same: when driving frequency matches natural frequency, small inputs produce large outputs — a feature to exploit or avoid depending on the application.
