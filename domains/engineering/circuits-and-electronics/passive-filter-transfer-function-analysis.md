---
id: passive-filter-transfer-function-analysis
title: Passive Filter Transfer Function Analysis
domain: engineering
course: circuits-and-electronics
prerequisites:
- id: AC-Kirchhoff-laws-phasor-domain
  type: hard
- id: series-RLC-resonance-characteristics
  type: soft
builds-toward:
- first-order-passive-filters
- second-order-passive-filters
tags:
- filters
- transfer-function
- magnitude-response
- phase-response
stage: formal-systems
status: draft
---

# Passive Filter Transfer Function Analysis

## Core Idea
A filter's transfer function H(jω) = V_out/V_in is a ratio of phasors that characterizes frequency response. The magnitude |H(jω)| and phase ∠H(jω) show which frequencies are passed or attenuated. Passive filters (built with R, L, C) have transfer functions that are ratios of polynomials in jω, leading to characteristic rolloff rates.
