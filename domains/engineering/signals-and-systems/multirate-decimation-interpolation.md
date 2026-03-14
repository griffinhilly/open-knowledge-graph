---
id: multirate-decimation-interpolation
title: Multirate Signal Processing and Filter Banks
domain: engineering
course: signals-and-systems
prerequisites:
- id: sampling-theorem-nyquist-rate
  type: hard
- id: aliasing-reconstruction-signals
  type: hard
- id: dft-and-fft-algorithms
  type: soft
tags:
- multirate
- decimation
- interpolation
- filter-banks
stage: advanced
status: draft
---

# Multirate Signal Processing and Filter Banks

## Core Idea
Decimation reduces sampling rate by integer factor M after anti-aliasing filtering; interpolation increases rate by factor L by inserting zeros and low-pass filtering. Polyphase filter structures decompose filters into parallel paths operating at reduced rates, enabling efficient implementation. Multirate systems are fundamental in audio codecs, communication systems, and signal processing applications.
