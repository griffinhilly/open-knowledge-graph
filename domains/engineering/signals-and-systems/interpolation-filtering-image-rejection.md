---
id: interpolation-filtering-image-rejection
title: Interpolation, Image Rejection, and Upsampling
domain: engineering
course: signals-and-systems
prerequisites:
- id: reconstruction-filters-post-interpolation-design
  type: hard
builds-toward:
- polyphase-filter-decomposition-multirate
tags:
- interpolation
- upsampling
- image-rejection
- multirate
stage: formal-systems
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

## Explainer

To understand interpolation, start from what you know about sampling and the Nyquist theorem. When a continuous signal is sampled at rate f_s, its spectrum — the DTFT — is periodic with period f_s. That periodicity is the key: the baseband spectrum (from −f_s/2 to +f_s/2) repeats indefinitely at every integer multiple of f_s. When we reconstruct the continuous signal, an ideal reconstruction filter passes only the baseband copy and suppresses all the repetitions. Interpolation is the discrete-time version of the same idea, but between discrete sequences rather than between discrete and continuous signals.

**Upsampling by factor L** inserts L−1 zeros between every input sample, producing an output sequence at rate L·f_s. In the frequency domain, this zero-insertion has a specific spectral effect: the original baseband spectrum — occupying 0 to f_s/2 in the original sequence — now occupies 0 to f_s/2 in a wider frequency axis that extends to L·f_s/2. But the original periodicity of the DTFT also persists, creating L−1 additional copies (**spectral images**) of the baseband spectrum at intervals of f_s within the new wider range. These images are not new information — they are mathematical artifacts of the zero-insertion operation. They must be removed.

The **anti-imaging filter** (also called the interpolation filter or reconstruction filter) is a lowpass filter applied after upsampling to suppress those spectral images. Its cutoff must be at f_s/2 — the original Nyquist frequency — so it passes the true baseband signal and attenuates everything above it. The filter gain must be L to compensate for the energy reduction caused by inserting zeros (the inserted zeros contribute no energy, so the average signal energy drops by a factor of L after upsampling). After filtering, the output looks like a higher-rate version of the original signal with appropriately interpolated values between the original samples — this is digital interpolation, and it is the mechanism by which digital audio upsamples from 44.1 kHz to 192 kHz, for instance.

The duality with decimation is worth recognizing. Decimation (downsampling) reduces the sample rate by applying an **anti-aliasing** filter before discarding samples — the filter prevents high-frequency content from folding into the baseband. Interpolation increases the sample rate by inserting zeros and applying an **anti-imaging** filter after upsampling — the filter suppresses images created by the zero insertion. In both cases, filtering is mandatory: skip the filter in decimation and you get aliasing; skip it in interpolation and you get images. Both operations are lossless in principle when the signal is properly bandlimited, and both are implemented efficiently using **polyphase decompositions** that avoid computing filter outputs at discarded or zero-valued sample positions — the topic that builds directly on this one.
