---
id: seismic-data-processing-and-filtering
title: Seismic Data Processing and Noise Filtering
domain: earth-and-space-sciences
course: geophysics
prerequisites:
- id: reflection-seismic-survey-design
  type: hard
builds-toward:
- seismic-migration-techniques
- seismic-interpretation-structural-mapping
tags:
- seismic
- processing
- filtering
- signal-to-noise
stage: advanced
status: validated
---

# Seismic Data Processing and Noise Filtering

## Core Idea
Raw seismic data contains noise from instrument errors, ambient vibrations, and multiples (reflections bouncing multiple times). Processing steps include denoising, gain correction, velocity analysis, normal moveout correction, and stacking. These operations enhance reflections from target interfaces while suppressing noise, producing final seismic images ready for interpretation.

## Questions

```yaml
- question: "In a common midpoint (CMP) gather, traces recorded at different source-receiver offsets show the same reflection arriving at different times. What is the shape of the arrival time curve plotted against offset?"
  type: multiple-choice
  options:
    - "A straight line with positive slope — the further the offset, the later and more uniformly delayed the arrival"
    - "A hyperbola — the travel time increases with offset in a curved relationship governed by the seismic velocity and reflector depth"
    - "A flat line — because all traces share the same reflection point, arrivals are simultaneous regardless of offset"
    - "An exponential curve — because energy loss increases non-linearly with distance traveled"
  answer: 1
  explanation: "The travel time t for a reflection at depth z with velocity v and offset x follows t² = t₀² + x²/v² (the NMO equation), which is the equation of a hyperbola. The zero-offset two-way time t₀ forms the apex of the hyperbola, and traces at larger offsets record the same reflection progressively later. This hyperbolic shape is not arbitrary — it is a direct geometric consequence of the extra path length traveled by off-center rays. Recognizing this shape is the foundation for velocity analysis: the correct seismic velocity is the one that, when applied in the NMO correction, flattens the hyperbola into a horizontal alignment across all offsets."

- question: "After applying NMO correction and stacking 50 traces from a CMP gather, by approximately what factor does the signal-to-noise ratio improve?"
  type: multiple-choice
  options:
    - "50 — because there are 50 times as many traces contributing to the signal"
    - "25 — because stacking averages out half the noise from 50 traces"
    - "7 — because signal adds coherently while random noise averages down as the square root of the number of traces"
    - "2 — because stacking mainly removes the two largest noise spikes"
  answer: 2
  explanation: "When n traces are stacked, coherent reflections add in amplitude proportional to n, while random (incoherent) noise adds in amplitude proportional to √n (since random noise has zero mean and its amplitude sums as the root of the number of samples). The signal-to-noise ratio therefore improves by n/√n = √n. For n = 50, this is √50 ≈ 7. This √n improvement is why industry seismic surveys invest heavily in recording many traces per CMP (high fold): each doubling of fold provides roughly a 40% SNR improvement. Option A would only be correct if noise were coherent and added like signal, which random noise does not."

- question: "NMO correction changes the physical content of the seismic data by adding new geological information to the traces."
  type: true-false
  answer: false
  explanation: "False. NMO correction is a purely geometric operation — it time-shifts each trace to remove the offset-dependent travel-time delay, making all traces in a CMP gather look as though they were recorded at zero offset. It does not add information; it removes a geometric artifact of the acquisition geometry. The geological information (the reflection events) was already in the original traces — NMO correction simply aligns that information so that stacking can be applied. One side effect is 'NMO stretch' at large offsets and shallow times, where the time-shifting distorts the waveform shape, but this is an artifact of the correction, not new geological data."

- question: "Velocity analysis must be performed before NMO correction can be applied, because the correct stacking velocity determines which hyperbola to flatten."
  type: true-false
  answer: true
  explanation: "True. The NMO equation requires knowledge of the seismic velocity at each depth (or equivalently, a stacking velocity function with time). Without the correct velocity, you either over-correct (flattening too much, causing NMO stretch artifacts) or under-correct (leaving residual moveout, so stacking does not optimally align reflections). Velocity analysis is done by testing a range of velocities and finding the one that produces the flattest gather — the velocity that maximizes the coherent stack amplitude is the best stacking velocity. This is why velocity analysis is a distinct processing step that precedes NMO correction in the standard processing sequence."

- question: "Explain why stacking improves the signal-to-noise ratio. What happens to the seismic reflection signal and what happens to random noise when multiple traces are averaged together?"
  type: short-answer
  answer: "Seismic reflections are coherent signals — after NMO correction, they align horizontally across the CMP gather, so they add constructively when stacked (amplitudes sum). Random noise is incoherent — it has random polarity and timing, so it partially cancels when summed (amplitudes add as √n for n traces). The result is that the signal amplitude grows as n while the noise amplitude grows as √n, improving the signal-to-noise ratio by n/√n = √n. Stacking 50 traces therefore improves SNR by approximately 7."
  explanation: "This is the fundamental principle behind all coherency-based enhancement methods in signal processing. The key prerequisite is that NMO correction has already aligned the reflections — if reflections are not aligned before stacking, they too will partially cancel, and the SNR improvement is lost. This is why accurate velocity analysis is so critical: poor velocities mean poor NMO correction, which means poor stacking, which means poor SNR."
```

## Explainer

From reflection seismic survey design, you understand how sources and receivers are arranged to record waves bouncing off subsurface interfaces. But what comes out of the field is not a clean image — it is a massive collection of wiggly traces full of noise, artifacts, and geometric distortions. Seismic data processing is the sequence of operations that transforms this raw data into an interpretable cross-section of the subsurface. Think of it as developing a photograph from a film negative: the information is in there, but it takes careful processing to reveal it.

The first steps address basic data quality. **Gain correction** compensates for the fact that seismic waves lose energy as they travel — deeper reflections arrive with much smaller amplitudes than shallow ones, so the traces are scaled to make reflections at all depths visible. **Frequency filtering** removes noise outside the useful signal band: low-frequency ground roll (surface waves generated by the source) and high-frequency random noise are attenuated using bandpass filters. Bad traces from malfunctioning receivers are identified and removed (a process called editing or trace killing).

The central processing step is **normal moveout (NMO) correction** and **stacking**. In a common midpoint (CMP) gather — all traces that share the same reflection point — the same reflection arrives at different times depending on the source-receiver offset. For a flat reflector, the travel-time curve is a hyperbola: traces at larger offsets record the reflection later because the wave travels a longer path. **Velocity analysis** determines the seismic velocity that best flattens this hyperbola. Once the correct velocity is found, NMO correction removes the offset-dependent time delay, aligning the reflection horizontally across all offsets. The corrected traces are then **stacked** — averaged together — which dramatically improves the signal-to-noise ratio because coherent reflections add constructively while random noise cancels out. A stack of 50 traces improves the signal-to-noise ratio by roughly a factor of 7.

After stacking, additional steps address remaining artifacts. **Multiple suppression** removes reflections that have bounced more than once between interfaces (such as the sea floor in marine data) — these multiples masquerade as deeper reflections and must be identified and removed. Techniques include predictive deconvolution, which uses the repetitive nature of multiples to predict and subtract them, and Radon transforms, which separate multiples from primaries based on their different moveout velocities. The final processed section — a stacked, filtered, deconvolved image — shows the subsurface as a series of reflection events positioned at the correct two-way travel time. Converting this to true depth and correctly positioning dipping reflectors requires migration, which is covered in the next topic in this sequence.
