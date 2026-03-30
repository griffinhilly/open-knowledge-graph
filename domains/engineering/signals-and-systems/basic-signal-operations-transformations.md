---
id: basic-signal-operations-transformations
title: Basic Signal Operations and Transformations
domain: engineering
course: signals-and-systems
prerequisites:
- id: signal-classification-continuous-discrete
  type: hard
builds-toward:
- convolution-continuous-discrete-systems
- fourier-transform-definition-properties
tags:
- signals
- operations
- transformations
stage: formal-systems
status: validated
---

# Basic Signal Operations and Transformations

## Core Idea
Signals can be scaled, shifted in time, reflected, and combined through addition and multiplication. These operations are essential for modeling system inputs and understanding how signal transformations propagate through systems.

## Questions

```yaml
- question: "A signal x(t) has a peak at t = 0. Where does the peak of y(t) = x(2t − 4) occur?"
  type: multiple-choice
  options:
    - "t = 4, because the −4 term shifts the signal right by 4"
    - "t = 2, because the argument equals zero when 2t − 4 = 0, so t = 2"
    - "t = −2, because the signal is compressed by 2 and shifted left"
    - "t = 8, because the shift is amplified by the time-scaling factor"
  answer: 1
  explanation: "The peak of x(t) occurs when its argument equals zero. For y(t) = x(2t − 4), set 2t − 4 = 0, giving t = 2. The effective shift is 4/2 = 2, not 4. This is the critical point: x(at − b) should be rewritten as x(a(t − b/a)), so the time shift is b/a, not b. Option A is the classic mistake of reading the shift directly from the expression without accounting for the time-scaling factor. Option D doubles the shift rather than dividing."

- question: "A signal x(t) represents a speech waveform. What does the transformed signal y(t) = x(0.5t) sound like compared to x(t)?"
  type: multiple-choice
  options:
    - "It sounds sped up — the speech is compressed in time and perceived as faster"
    - "It sounds slowed down — the speech is stretched in time and perceived as slower"
    - "It sounds identical but quieter — amplitude scaling does not affect timing"
    - "It sounds pitch-shifted downward without changing the playback speed"
  answer: 1
  explanation: "Time scaling with a = 0.5 (less than 1) stretches the signal: x(0.5t) takes twice as long to complete each feature, making the speech play back at half speed and sound slowed down. Compression (a > 1) would speed it up. Option A describes the a > 1 case. Option C confuses amplitude scaling with time scaling. Option D is an approximation of pitch shifting, but x(0.5t) fundamentally slows the signal, which does lower pitch as a side effect — yet describing it as 'pitch shifted without speed change' is incorrect."

- question: "In the signal x(t − t₀), a positive value of t₀ shifts the signal to the right (delay) along the time axis."
  type: true-false
  answer: true
  explanation: "A positive t₀ in x(t − t₀) delays the signal — the event that occurred at t = 0 in x(t) now occurs at t = t₀ in the shifted version. Graphically, the signal moves to the right. This direction is counterintuitive to many students because subtracting inside the function (−t₀) seems like it should shift left. The rule to remember: subtract from t to delay (shift right); add to t to advance (shift left). This is consistent with the general x(a(t − t₀)) form: t₀ is the time shift, and it is to the right when positive."

- question: "In the expression x(2t − 6), the time shift of the original signal x(t) is 6 units to the right."
  type: true-false
  answer: false
  explanation: "The shift is 3 units, not 6. To find the true shift, rewrite the expression in standard form: x(2t − 6) = x(2(t − 3)). In the form x(a(t − t₀)), the time shift t₀ = 3 and the scale factor a = 2. Reading the shift directly from the coefficient (−6 ÷ 1 = 6) without accounting for the scale factor (dividing by a = 2) is the most common error. The effective shift is always b/a when the expression is written as x(at − b)."

- question: "A signal is given as y(t) = x(3t + 6). Describe step-by-step how y(t) relates to x(t) — what transformations have been applied and in what order?"
  type: short-answer
  answer: "Rewrite: x(3t + 6) = x(3(t + 2)). This reveals two transformations: (1) time shift by −2 (since the form is t − t₀ with t₀ = −2, the signal is advanced — shifted LEFT by 2 units); (2) time compression by factor 3 (the signal runs through its pattern 3× faster). Applying in the natural order: first shift x(t) left by 2 to get x(t + 2), then compress by 3 to get x(3t + 6). The resulting signal is both earlier (shifted left) and faster (compressed)."
  explanation: "The factoring step — rewriting x(at + b) as x(a(t + b/a)) — is the key mechanical skill. Students who apply shifts and scales without factoring first will consistently get the wrong effective shift when a ≠ 1. The question also tests understanding of direction: adding inside the argument shifts left (advances), subtracting shifts right (delays)."
```

## Explainer

From signal classification, you know that a signal is simply a function — a mapping from an independent variable (usually time) to a value. The operations in this topic are the basic algebraic manipulations you can perform on that function. They seem abstract at first, but each has a concrete physical meaning that will serve you throughout systems analysis.

**Time shifting** replaces t with t − t₀, producing x(t − t₀). If t₀ > 0, the signal is delayed — the event that occurred at time 0 now occurs at time t₀. If t₀ < 0, the signal is advanced (occurs earlier). Physically, a delayed signal might represent a sound wave arriving t₀ seconds late after traveling a distance, or a sensor with processing delay. The key rule is: to delay a signal by t₀, replace t with (t − t₀) everywhere in the signal's expression. Students often get confused about direction — subtracting inside the function shifts right (later), adding shifts left (earlier).

**Time scaling** replaces t with at, producing x(at). If a > 1, the signal is **compressed** — it runs through its entire pattern in less time (higher playback speed). If 0 < a < 1, the signal is **stretched** (slower playback). If a = −1, you get **time reversal**: x(−t), the signal reflected about the time axis. In discrete time, only integer downsampling and upsampling are valid, making time scaling more constrained. **Amplitude scaling** multiplies the entire signal by a constant: A·x(t). This scales the signal's magnitude without touching its timing — amplification (A > 1) or attenuation (0 < A < 1).

The operations combine. x(at − t₀) is both scaled and shifted — but order matters. Evaluate carefully: x(at − b) = x(a(t − b/a)), so the effective time shift is b/a, not b. Getting this wrong is the most common mistake when working with transformed signals. The right mental model is: first write the transformation as x(a(t − t₀)), then you can read off the scale factor a and the time shift t₀ independently.

**Addition** and **multiplication** of signals combine two signals sample-by-sample (or instant-by-instant for continuous signals). Addition models superposition — two sound waves arriving simultaneously sum their pressures. Multiplication models **modulation** — multiplying a low-frequency message signal by a high-frequency carrier shifts the message to a new frequency band for transmission. You will use all of these operations constantly when you study convolution and the Fourier transform: convolution is built from shifts, and the Fourier transform decomposes signals into complex exponentials that are themselves the building blocks that scaling and shifting act on most cleanly.

