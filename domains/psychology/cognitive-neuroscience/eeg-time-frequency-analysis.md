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
stage: advanced
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

## Explainer

From your prerequisites in EEG/ERP methods, you know that EEG records voltage fluctuations from the scalp reflecting synchronized neural activity, and that event-related potentials (ERPs) are extracted by averaging across many trials. ERPs reveal activity that is **phase-locked** to a stimulus — components that occur at the same latency on each trial, so they survive averaging. But many cognitively relevant neural processes are oscillatory without being phase-locked: they fluctuate in power or phase in relation to cognitive states, but not consistently at the same latency on every trial. Averaging washes out this activity. **Time-frequency analysis** is the method that captures it.

The key mathematical tool from your Fourier analysis prerequisites is the idea that any signal can be decomposed into sine waves of different frequencies. The challenge is that Fourier analysis assumes stationarity — that frequency content doesn't change over time — which is false for brain signals. The solution is the **short-time Fourier transform (STFT)** or the more flexible **wavelet analysis**: decompose small time windows independently and track how frequency content changes across those windows. The result is a **spectrogram** — a 2D map of time × frequency with color or intensity indicating power at each moment and frequency. Wavelet analysis improves on STFT by using narrower windows at high frequencies (providing good time resolution where frequencies change quickly) and wider windows at low frequencies (providing good frequency resolution where slower dynamics matter).

Each **frequency band** has characteristic functional correlates established by decades of cognitive neuroscience research. **Theta** (4–8 Hz) is strongly linked to hippocampal-prefrontal communication during memory encoding and retrieval, and to working memory maintenance — theta power over frontal electrodes increases when people hold information in mind. **Alpha** (8–12 Hz) is associated with **cortical inhibition**: regions processing irrelevant information show alpha *increases*, while engaged regions show alpha *suppression*. This makes alpha a useful marker of selective attention — it reveals not just what is being processed, but what is being actively suppressed. **Beta** (12–30 Hz) is associated with maintaining current sensorimotor or cognitive states and decreases during motor actions or cognitive transitions. **Gamma** (30–100+ Hz) is linked to local cortical processing and feature binding during active encoding.

Beyond power, **phase** carries critical information. **Phase-amplitude coupling (PAC)** — where the phase of a slow oscillation modulates the amplitude of a fast oscillation — is thought to implement a neural multiplexing mechanism. Theta cycles organize gamma bursts in sequence, so that within one theta cycle, multiple gamma bursts can occur, each potentially representing a different item held in working memory. This hierarchical relationship between oscillations offers a mechanistic account of working memory's limited capacity: the number of gamma cycles that fit within a theta cycle constrains how many items can be maintained simultaneously. A critical caveat: high-frequency gamma can also arise from **EMG muscle artifact** conducted to scalp electrodes — careful artifact rejection is essential before interpreting gamma results, and this is among the most common sources of false positives in cognitive neuroscience.
