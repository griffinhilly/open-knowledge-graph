---
id: group-delay-phase-characterization
title: Group Delay and Phase Characterization
domain: engineering
course: signals-and-systems
prerequisites:
- id: frequency-response-and-bode-plots
  type: hard
builds-toward:
- all-pass-filters-phase-shaping
tags:
- phase-response
- group-delay
- dispersion
- filters
stage: advanced
status: draft
---

# Group Delay and Phase Characterization

## Core Idea
Phase response φ(ω) = arg[H(e^jω)] describes phase shift as a function of frequency. Group delay τg(ω) = –dφ/dω represents delay of signal components at each frequency. Linear-phase filters have constant group delay, avoiding signal distortion. Non-constant group delay disperses frequency components at different rates, causing waveform degradation.
