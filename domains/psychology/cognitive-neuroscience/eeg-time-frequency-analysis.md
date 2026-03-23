---
id: eeg-time-frequency-analysis
title: EEG Time-Frequency Analysis and Neural Oscillations
domain: psychology
course: cognitive-neuroscience
prerequisites:
- id: eeg-erp-temporal-dynamics
  type: hard
- id: frequency-oscillations-cognition
  type: hard
- id: fourier-series-lp-theory
  type: soft
- id: fourier-series-definition
  type: soft
- id: complex-numbers-intro
  type: soft
builds-toward:
- attention-switching-theta-oscillations
- working-memory-theta-gamma-coupling
tags:
- EEG
- oscillations
- theta
- alpha
- beta
- gamma
- time-frequency
stage: expert
status: draft
---

# EEG Time-Frequency Analysis and Neural Oscillations

## Core Idea
EEG recordings contain oscillatory activity across frequency bands (delta <4Hz, theta 4-8Hz, alpha 8-12Hz, beta 12-30Hz, gamma 30-100+Hz) that reflect different neural states and cognitive processes. Time-frequency decomposition reveals how the power and phase of these oscillations change during cognition, enabling inference about neural communication, attention allocation, and memory operations.

## How It's Best Learned
Begin by understanding Fourier analysis and windowed spectrograms for time-frequency decomposition. Examine published EEG time-frequency plots from different cognitive domains (attention, memory, motor control) to build intuition for characteristic oscillatory signatures.

## Common Misconceptions
- High gamma power always reflects neural spiking; gamma can arise from volume-conducted muscle artifact or EMG.
- Power increases in one frequency indicate reduced activity in others; spectral changes are interdependent.
- Oscillatory phase has no information; phase-amplitude coupling and phase-phase coupling carry cognitive significance.

## Questions

```yaml
- question: "A researcher averages 200 EEG trials time-locked to a stimulus onset and finds no consistent frontal theta power increase in the average, even though individual trials clearly show theta bursts. What is the most likely explanation?"
  type: multiple-choice
  options:
    - "Theta is too low a frequency to be reliably detected from scalp EEG recordings"
    - "The theta bursts are not phase-locked to the stimulus — they occur at variable latencies across trials, so averaging cancels them out"
    - "200 trials is statistically insufficient to detect theta power changes"
    - "Frontal theta in this context is an artifact of eye movements rather than genuine neural activity"
  answer: 1
  explanation: "This is the fundamental distinction between ERPs and time-frequency analysis. Averaging preserves only phase-locked components — those occurring at the same latency on every trial. Theta oscillations related to working memory or encoding fluctuate in power across trials but not at a consistent post-stimulus latency, so averaging cancels them. Time-frequency analysis computes power in each trial's time windows independently before averaging the spectrograms, capturing this non-phase-locked activity. This is exactly why time-frequency methods are needed beyond standard ERP analysis."

- question: "During a spatial attention task, a researcher observes alpha power increasing over right parietal cortex while subjects attend to the left visual field. What is the most accurate interpretation?"
  type: multiple-choice
  options:
    - "Right parietal cortex is working harder to process the attended left-side information"
    - "Right parietal cortex is being actively suppressed to prevent irrelevant right-side information from interfering with the attended left side"
    - "The alpha increase is an artifact; genuine neural engagement always reduces alpha power"
    - "Alpha increases reflect heightened arousal and general attentional readiness"
  answer: 1
  explanation: "Alpha is a marker of cortical inhibition, not engagement. Alpha increases over a region indicate active suppression of that region. During leftward spatial attention, right parietal cortex (which processes the right visual field) shows alpha increases because the system is inhibiting processing of irrelevant right-side input. The attended left visual field is handled by left parietal cortex, which shows alpha suppression. Option A inverts the relationship — engaged regions show alpha decreases, not increases."

- question: "High gamma power in an EEG recording reliably indicates increased local cortical spiking activity."
  type: true-false
  answer: false
  explanation: "High-frequency gamma can arise from EMG (electromyographic) muscle artifact — electrical signals from scalp and facial muscles that volume-conduct to EEG electrodes. This is one of the most common sources of false positives in cognitive EEG research. While genuine gamma can reflect local cortical processing and feature binding, the statement that high gamma reliably indicates neural spiking is false without careful artifact rejection. Gamma results must be interpreted with this confound in mind."

- question: "Alpha suppression over a brain region is evidence that the region is actively engaged in processing relevant information."
  type: true-false
  answer: true
  explanation: "Because alpha reflects cortical inhibition, a decrease in alpha (alpha suppression or desynchronization) over a region indicates that the inhibitory 'idle' state has been released and the region is actively processing. This makes alpha a dual-sided marker: increases reveal what is being suppressed; decreases reveal what is being engaged. Selective attention studies exploit this logic — attention to one location produces alpha suppression over regions processing that location and alpha increases over regions handling irrelevant locations."

- question: "What is phase-amplitude coupling (PAC), and how does it offer a mechanistic account of working memory capacity limits?"
  type: short-answer
  answer: "Phase-amplitude coupling is when the phase of a slow oscillation (e.g., theta, 4-8 Hz) modulates the amplitude of a fast oscillation (e.g., gamma, 30-100 Hz) — gamma bursts occur preferentially at specific phases of the theta cycle. This is thought to implement neural multiplexing: each gamma burst within a theta cycle can represent a different item held in working memory. The number of gamma cycles that fit within one theta cycle is finite, which constrains how many distinct items can be simultaneously maintained, providing a mechanistic explanation for working memory's limited capacity."
  explanation: "PAC operationalizes a hierarchical view of neural oscillations: slow oscillations provide temporal frames, fast oscillations encode content within those frames. The theta-gamma coupling model links a behavioral observation (capacity limits of ~4 items) to a physiological mechanism (the ratio of theta to gamma periods), generating testable predictions about how capacity limits should vary with oscillatory frequencies and cognitive load. It also connects EEG findings to hippocampal sequence coding, where theta-gamma coupling organizes spatial representations."
```

## Explainer

From your prerequisites in EEG/ERP methods, you know that EEG records voltage fluctuations from the scalp reflecting synchronized neural activity, and that event-related potentials (ERPs) are extracted by averaging across many trials. ERPs reveal activity that is **phase-locked** to a stimulus — components that occur at the same latency on each trial, so they survive averaging. But many cognitively relevant neural processes are oscillatory without being phase-locked: they fluctuate in power or phase in relation to cognitive states, but not consistently at the same latency on every trial. Averaging washes out this activity. **Time-frequency analysis** is the method that captures it.

The key mathematical tool from your Fourier analysis prerequisites is the idea that any signal can be decomposed into sine waves of different frequencies. The challenge is that Fourier analysis assumes stationarity — that frequency content doesn't change over time — which is false for brain signals. The solution is the **short-time Fourier transform (STFT)** or the more flexible **wavelet analysis**: decompose small time windows independently and track how frequency content changes across those windows. The result is a **spectrogram** — a 2D map of time × frequency with color or intensity indicating power at each moment and frequency. Wavelet analysis improves on STFT by using narrower windows at high frequencies (providing good time resolution where frequencies change quickly) and wider windows at low frequencies (providing good frequency resolution where slower dynamics matter).

Each **frequency band** has characteristic functional correlates established by decades of cognitive neuroscience research. **Theta** (4–8 Hz) is strongly linked to hippocampal-prefrontal communication during memory encoding and retrieval, and to working memory maintenance — theta power over frontal electrodes increases when people hold information in mind. **Alpha** (8–12 Hz) is associated with **cortical inhibition**: regions processing irrelevant information show alpha *increases*, while engaged regions show alpha *suppression*. This makes alpha a useful marker of selective attention — it reveals not just what is being processed, but what is being actively suppressed. **Beta** (12–30 Hz) is associated with maintaining current sensorimotor or cognitive states and decreases during motor actions or cognitive transitions. **Gamma** (30–100+ Hz) is linked to local cortical processing and feature binding during active encoding.

Beyond power, **phase** carries critical information. **Phase-amplitude coupling (PAC)** — where the phase of a slow oscillation modulates the amplitude of a fast oscillation — is thought to implement a neural multiplexing mechanism. Theta cycles organize gamma bursts in sequence, so that within one theta cycle, multiple gamma bursts can occur, each potentially representing a different item held in working memory. This hierarchical relationship between oscillations offers a mechanistic account of working memory's limited capacity: the number of gamma cycles that fit within a theta cycle constrains how many items can be maintained simultaneously. A critical caveat: high-frequency gamma can also arise from **EMG muscle artifact** conducted to scalp electrodes — careful artifact rejection is essential before interpreting gamma results, and this is among the most common sources of false positives in cognitive neuroscience.
