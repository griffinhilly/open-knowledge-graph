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
stage: expert
status: draft
---

# Time-Series and Frequency-Domain Analysis in Seismology

## Core Idea
Seismic data are processed in time and frequency domains using filtering, deconvolution, and spectral analysis. Fourier transforms convert time-domain signals to frequency content, enabling removal of noise and geologic artifacts.

## Questions

```yaml
- question: "A seismologist wants to remove 60 Hz power-line noise from a seismic recording. In which domain is this most efficiently accomplished?"
  type: multiple-choice
  options:
    - "The time domain, by subtracting a 60 Hz sine wave from the raw seismogram"
    - "The frequency domain, by computing the Fourier transform, zeroing the 60 Hz component, then inverse transforming"
    - "The spatial domain, by combining recordings from multiple seismometers to cancel the noise"
    - "The wavelet domain, which is required for any frequency-based operation"
  answer: 1
  explanation: "The Fourier transform converts the time-domain signal to a frequency spectrum where different frequency components are separated and identifiable. Suppressing 60 Hz noise is trivial in the frequency domain — multiply the spectrum by a notch filter at 60 Hz, then inverse transform back. Doing this in the time domain requires convolving with a complex filter. The efficiency of the frequency domain for filtering operations is the central practical motivation for using the Fourier transform."

- question: "Stacking multiple seismic recordings of the same subsurface point improves signal-to-noise ratio primarily because:"
  type: multiple-choice
  options:
    - "Coherent signal adds linearly while random noise adds in quadrature, improving SNR by √N for N stacked traces"
    - "Each additional trace adds more signal power, making the total signal N times stronger while noise stays constant"
    - "Stacking applies an implicit bandpass filter above 40 Hz, removing high-frequency noise"
    - "Multiple recordings cover a wider area of the subsurface, providing more spatial information"
  answer: 0
  explanation: "The signal is coherent across traces — same arrival time and waveform shape. Random noise is incoherent — different in each trace. When N traces are summed, the coherent signal adds linearly (amplitude scales as N) while random noise adds in quadrature (amplitude scales as √N), so signal-to-noise ratio improves by N/√N = √N. This is why seismic surveys acquire many redundant recordings — each additional trace provides diminishing but real improvement."

- question: "Deconvolution improves the temporal resolution of a seismic record by removing the effect of the source wavelet from the recorded signal."
  type: true-false
  answer: true
  explanation: "A seismogram is the convolution of the source wavelet, the Earth's reflectivity series (what you want), and the instrument response. Deconvolution inverts this: because convolution in time equals multiplication in frequency, deconvolution is spectral division by the source wavelet. The result compresses the broad, ringy wavelet into a sharp spike, improving the ability to resolve closely spaced reflectors. Deconvolution is a standard step in seismic processing pipelines for this reason."

- question: "A seismic bandpass filter passing 10–40 Hz both removes low-frequency microseismic ocean noise and high-frequency power-line noise while preserving the geologically relevant signal."
  type: true-false
  answer: true
  explanation: "Ocean-generated microseismic noise dominates below ~1 Hz; power-line and cultural noise concentrate at 50–60 Hz. Crustal reflection signals often fall in the 5–40 Hz range. A 10–40 Hz bandpass filter suppresses both noise bands while passing the geologic signal — dramatically improving signal-to-noise ratio. The Fourier transform makes this selective frequency removal straightforward via multiplication by a window function in the frequency domain."

- question: "Why does the fact that convolution in the time domain equals multiplication in the frequency domain make deconvolution practical?"
  type: short-answer
  answer: "A seismogram is the convolution of wavelet, Earth reflectivity, and instrument response. Undoing convolution (deconvolution) is a difficult inverse problem in the time domain. But in the frequency domain, convolution becomes multiplication, so deconvolution becomes simple division: divide the recorded spectrum by the wavelet spectrum. This transforms a computationally hard operation into straightforward pointwise arithmetic, making it practical for large seismic datasets."
  explanation: "The convolution theorem is what makes frequency-domain processing powerful throughout signal processing and geophysics. Operations that are difficult or expensive in the time domain (deconvolution, arbitrary filtering) become trivial in the frequency domain. The tradeoff is that a forward and inverse Fourier transform must be applied, but FFT algorithms make this efficient even for large datasets."
```

## Explainer

From your study of seismic waves, you know that an earthquake or artificial source generates elastic waves that propagate through the Earth, and seismometers record the resulting ground motion as a time series — amplitude as a function of time. But a raw seismogram is a tangled mixture of signals: direct arrivals, reflections from layer boundaries, surface waves, multiple bounces, instrument noise, and cultural noise from traffic or machinery. **Seismic signal processing** is the set of mathematical techniques that disentangle this mixture to extract geologically meaningful information.

The foundational tool is the **Fourier transform**, which converts a time-domain signal into its frequency-domain representation — a spectrum showing how much energy the signal carries at each frequency. This matters because noise and signal often occupy different frequency bands. A reflection from a deep crustal boundary might contain energy primarily between 5 and 40 Hz, while cultural noise concentrates at 50 or 60 Hz (power-line frequency) and microseismic ocean noise dominates below 0.5 Hz. Applying a **bandpass filter** — which passes frequencies within a specified range and suppresses everything outside it — dramatically improves the signal-to-noise ratio with minimal distortion of the desired signal. The filter is trivial to implement in the frequency domain (multiply the spectrum by a window function) and is converted back to the time domain by the inverse Fourier transform.

**Deconvolution** addresses a more subtle problem: the seismogram is not a simple record of subsurface reflectivity but a **convolution** of three things — the source wavelet (the shape of the pulse emitted), the Earth's impulse response (the reflectivity series you want), and the instrument response. Convolution in the time domain corresponds to multiplication in the frequency domain, so deconvolution amounts to spectral division: dividing the recorded spectrum by the source wavelet spectrum to recover the reflectivity series. In practice, the source wavelet is rarely known precisely, so **predictive deconvolution** (Wiener filtering) estimates the wavelet statistically from the data itself, assuming that the reflectivity is random and white (equally energetic at all frequencies). The result is a sharpened, compressed wavelet that improves temporal resolution and suppresses reverberations.

Beyond these core techniques, seismic processing employs **stacking** (summing multiple recordings of the same subsurface point to suppress random noise by √N), **migration** (repositioning reflected energy to its true spatial location by accounting for wave propagation geometry), and **spectral analysis** for characterizing attenuation, dispersion, and source properties. Each step builds on the time-frequency duality that the Fourier transform provides. The processing sequence is designed so that each operation improves the data for the next, progressively transforming a noisy field record into an interpretable image of subsurface structure — whether that is a reflection profile for oil exploration or a tomographic velocity model for tectonic research.
