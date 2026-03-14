---
id: bandwidth-and-cutoff-frequencies
title: Bandwidth and Frequency Domain Specifications
domain: engineering
course: control-systems
prerequisites:
- id: frequency-response-magnitude-and-phase
  type: hard
builds-toward:
- gain-phase-margins-stability-robustness
- resonance-and-peaking-response
tags:
- bandwidth
- cutoff-frequency
- frequency-domain
- specifications
stage: advanced
status: draft
---

# Bandwidth and Frequency Domain Specifications

## Core Idea
Bandwidth is the frequency range over which a system responds adequately (typically -3dB point where power is half maximum). Bandwidth directly relates to rise time (bandwidth inversely proportional to rise time) and determines the maximum rate of reference tracking. Frequency specifications complement time-domain specs: wider bandwidth enables faster tracking but increases noise sensitivity.
