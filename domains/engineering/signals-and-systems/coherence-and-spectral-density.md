---
id: coherence-and-spectral-density
title: Coherence and Cross-Spectral Density
domain: engineering
course: signals-and-systems
prerequisites:
- id: power-spectral-density-estimation
  type: hard
- id: cross-correlation-signals
  type: hard
tags:
- coherence
- cross-spectral-density
- correlation
- spectral-analysis
stage: advanced
status: draft
---

# Coherence and Cross-Spectral Density

## Core Idea
Cross-spectral density Sxy(f) = FT[Rxy(τ)] describes frequency-domain correlation between signals. Coherence Cxy(f) = |Sxy(f)|²/(Sxx(f)·Syy(f)) normalizes to [0,1], indicating linear dependence strength at each frequency. Coherence 1 indicates perfect correlation; coherence 0 indicates independence. High coherence in narrow bands reveals channel coupling or shared noise sources.
