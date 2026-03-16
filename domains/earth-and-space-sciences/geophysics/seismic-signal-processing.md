---
id: seismic-signal-processing
title: Time-Series and Frequency-Domain Analysis in Seismology
domain: earth-and-space-sciences
course: geophysics
prerequisites:
- id: seismic-waves
  type: hard
builds-toward:
- seismic-reflection-surveys
tags:
- seismic
- signal
- processing
- fourier
stage: advanced
status: draft
---

# Time-Series and Frequency-Domain Analysis in Seismology

## Core Idea
Seismic data are processed in time and frequency domains using filtering, deconvolution, and spectral analysis. Fourier transforms convert time-domain signals to frequency content, enabling removal of noise and geologic artifacts.

## Explainer

From your study of seismic waves, you know that an earthquake or artificial source generates elastic waves that propagate through the Earth, and seismometers record the resulting ground motion as a time series — amplitude as a function of time. But a raw seismogram is a tangled mixture of signals: direct arrivals, reflections from layer boundaries, surface waves, multiple bounces, instrument noise, and cultural noise from traffic or machinery. **Seismic signal processing** is the set of mathematical techniques that disentangle this mixture to extract geologically meaningful information.

The foundational tool is the **Fourier transform**, which converts a time-domain signal into its frequency-domain representation — a spectrum showing how much energy the signal carries at each frequency. This matters because noise and signal often occupy different frequency bands. A reflection from a deep crustal boundary might contain energy primarily between 5 and 40 Hz, while cultural noise concentrates at 50 or 60 Hz (power-line frequency) and microseismic ocean noise dominates below 0.5 Hz. Applying a **bandpass filter** — which passes frequencies within a specified range and suppresses everything outside it — dramatically improves the signal-to-noise ratio with minimal distortion of the desired signal. The filter is trivial to implement in the frequency domain (multiply the spectrum by a window function) and is converted back to the time domain by the inverse Fourier transform.

**Deconvolution** addresses a more subtle problem: the seismogram is not a simple record of subsurface reflectivity but a **convolution** of three things — the source wavelet (the shape of the pulse emitted), the Earth's impulse response (the reflectivity series you want), and the instrument response. Convolution in the time domain corresponds to multiplication in the frequency domain, so deconvolution amounts to spectral division: dividing the recorded spectrum by the source wavelet spectrum to recover the reflectivity series. In practice, the source wavelet is rarely known precisely, so **predictive deconvolution** (Wiener filtering) estimates the wavelet statistically from the data itself, assuming that the reflectivity is random and white (equally energetic at all frequencies). The result is a sharpened, compressed wavelet that improves temporal resolution and suppresses reverberations.

Beyond these core techniques, seismic processing employs **stacking** (summing multiple recordings of the same subsurface point to suppress random noise by √N), **migration** (repositioning reflected energy to its true spatial location by accounting for wave propagation geometry), and **spectral analysis** for characterizing attenuation, dispersion, and source properties. Each step builds on the time-frequency duality that the Fourier transform provides. The processing sequence is designed so that each operation improves the data for the next, progressively transforming a noisy field record into an interpretable image of subsurface structure — whether that is a reflection profile for oil exploration or a tomographic velocity model for tectonic research.
