---
id: interpolation-filtering-image-rejection
title: Interpolation, Image Rejection, and Upsampling
domain: engineering
course: signals-and-systems
prerequisites:
- id: reconstruction-filters-post-interpolation-design
  type: hard
builds-toward: []
tags:
- interpolation
- upsampling
- image-rejection
- multirate
stage: expert
status: draft
---
# Interpolation, Image Rejection, and Upsampling

## Core Idea
Interpolation by factor L involves upsampling by inserting L-1 zeros between each sample, then filtering to remove spectral images. Unfiltered upsampling creates images at multiples of the original sampling rate. The anti-imaging filter must eliminate these images (frequencies above the original Nyquist rate) while preserving the baseband signal in the wider frequency range. Interpolation increases sample rate while maintaining signal information.

## How It's Best Learned
Upsample a discrete signal by factor 2 with and without anti-imaging filter. Observe spectral images in the unfiltered case; verify filter removes them while preserving baseband.

## Common Misconceptions
- Thinking upsampling creates new information (zeros don't add information).
- Confusing anti-imaging filter cutoff with original Nyquist frequency.
- Not recognizing that interpolation is dual of decimation.

## Questions

```yaml
- question: "A discrete signal originally sampled at 10 kHz is upsampled by factor L = 4 via zero-insertion (before any filtering). Where do the spectral images appear in the output spectrum?"
  type: multiple-choice
  options:
    - "At the new Nyquist frequency of 20 kHz only"
    - "At multiples of the original sampling rate — near 10 kHz, 20 kHz, and 30 kHz — within the new 0–20 kHz range"
    - "Images do not appear — zero-insertion only increases the sample rate without altering the spectrum"
    - "At multiples of the new sampling rate, 40 kHz apart"
  answer: 1
  explanation: "Upsampling by L=4 produces an output at 4×10 kHz = 40 kHz. The DTFT of the upsampled sequence is periodic, and zero-insertion causes the original baseband spectrum (0–5 kHz) to repeat at multiples of the original sampling frequency (10 kHz) within the new frequency range. Images appear near 10 kHz, 20 kHz, and 30 kHz — three unwanted copies of the baseband. The anti-imaging filter with cutoff at the original Nyquist (5 kHz) removes these images while preserving the baseband."

- question: "A DSP engineer upsamples a 44.1 kHz audio signal by factor 4 to produce a 176.4 kHz stream but forgets to apply the anti-imaging filter. What is the result?"
  type: multiple-choice
  options:
    - "Exactly the same audio — the filter is only needed for final analog reconstruction"
    - "Improved audio quality because the higher sample rate adds resolution between original samples"
    - "The original audio plus distortion from spectral images appearing as spurious high-frequency content aliased into the signal"
    - "Silence — the upsampled signal has no energy at the original frequencies"
  answer: 2
  explanation: "Without the anti-imaging filter, the spectral images created by zero-insertion remain in the signal. These images are copies of the original audio spectrum appearing at multiples of 44.1 kHz within the new frequency range. When the signal is subsequently processed or reconstructed, these images cause audible distortion. The upsampling itself adds no new information — zero-inserted samples contribute nothing real. The anti-imaging filter is mandatory to produce a valid higher-rate signal."

- question: "Inserting zeros between samples during upsampling creates new signal information, which is why higher sample rates can represent audio with greater accuracy."
  type: true-false
  answer: false
  explanation: "Zero insertion adds no information — the inserted zeros are mathematically inert placeholders. What upsampling creates is spectral images (artifacts), not new signal content. The anti-imaging filter then produces interpolated values between the original samples, but these are derived from the existing signal data — they represent the best estimate of what the original continuous signal was doing between samples, not new information. A student who confuses zero-insertion with information gain will misunderstand what interpolation actually achieves."

- question: "The anti-imaging filter applied after upsampling by L should have its cutoff at the original Nyquist frequency (f_s/2), not at the new Nyquist frequency (L·f_s/2)."
  type: true-false
  answer: true
  explanation: "The goal of the anti-imaging filter is to retain only the original baseband spectrum (0 to f_s/2) and suppress all spectral images at higher frequencies. If the cutoff were set at the new Nyquist (L·f_s/2), the filter would pass all the images it is supposed to remove. The original Nyquist frequency is the boundary between the true signal and the artifacts, so that is the correct cutoff. The filter gain must also be L to compensate for the energy reduction caused by inserting zero-valued samples."

- question: "Explain why upsampling by inserting zeros creates spectral images, and what role the anti-imaging filter plays in producing a valid higher-rate signal."
  type: short-answer
  answer: "The DTFT of any discrete sequence is periodic with period equal to the sampling rate. When L−1 zeros are inserted between each sample, the resulting sequence has the same baseband spectrum but now that spectral period structure repeats L−1 additional times within the wider frequency range of the higher-rate output. These repetitions — spectral images — are mathematical artifacts of the zero-insertion operation, not real signal components. The anti-imaging (lowpass) filter with cutoff at the original Nyquist frequency passes only the true baseband copy and suppresses all images. After filtering, the output contains interpolated values between the original samples (the filter effectively fills in values consistent with a bandlimited reconstruction of the original signal), producing a legitimate higher-rate representation without any spurious content."
  explanation: "This is the discrete-time analog of the continuous-time reconstruction process: just as a DAC reconstruction filter suppresses aliased copies in the continuous domain, the anti-imaging filter suppresses copies in the discrete domain after upsampling. Both are mandatory; both remove the same type of artifact from the same spectral periodicity."
```

## Explainer

To understand interpolation, start from what you know about sampling and the Nyquist theorem. When a continuous signal is sampled at rate f_s, its spectrum — the DTFT — is periodic with period f_s. That periodicity is the key: the baseband spectrum (from −f_s/2 to +f_s/2) repeats indefinitely at every integer multiple of f_s. When we reconstruct the continuous signal, an ideal reconstruction filter passes only the baseband copy and suppresses all the repetitions. Interpolation is the discrete-time version of the same idea, but between discrete sequences rather than between discrete and continuous signals.

**Upsampling by factor L** inserts L−1 zeros between every input sample, producing an output sequence at rate L·f_s. In the frequency domain, this zero-insertion has a specific spectral effect: the original baseband spectrum — occupying 0 to f_s/2 in the original sequence — now occupies 0 to f_s/2 in a wider frequency axis that extends to L·f_s/2. But the original periodicity of the DTFT also persists, creating L−1 additional copies (**spectral images**) of the baseband spectrum at intervals of f_s within the new wider range. These images are not new information — they are mathematical artifacts of the zero-insertion operation. They must be removed.

The **anti-imaging filter** (also called the interpolation filter or reconstruction filter) is a lowpass filter applied after upsampling to suppress those spectral images. Its cutoff must be at f_s/2 — the original Nyquist frequency — so it passes the true baseband signal and attenuates everything above it. The filter gain must be L to compensate for the energy reduction caused by inserting zeros (the inserted zeros contribute no energy, so the average signal energy drops by a factor of L after upsampling). After filtering, the output looks like a higher-rate version of the original signal with appropriately interpolated values between the original samples — this is digital interpolation, and it is the mechanism by which digital audio upsamples from 44.1 kHz to 192 kHz, for instance.

The duality with decimation is worth recognizing. Decimation (downsampling) reduces the sample rate by applying an **anti-aliasing** filter before discarding samples — the filter prevents high-frequency content from folding into the baseband. Interpolation increases the sample rate by inserting zeros and applying an **anti-imaging** filter after upsampling — the filter suppresses images created by the zero insertion. In both cases, filtering is mandatory: skip the filter in decimation and you get aliasing; skip it in interpolation and you get images. Both operations are lossless in principle when the signal is properly bandlimited, and both are implemented efficiently using **polyphase decompositions** that avoid computing filter outputs at discarded or zero-valued sample positions — the topic that builds directly on this one.
