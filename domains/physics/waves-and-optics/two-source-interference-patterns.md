---
id: two-source-interference-patterns
title: Two-Source Interference Patterns
domain: physics
course: waves-and-optics
prerequisites:
- id: interference-constructive-destructive-interference
  type: hard
- id: wavelength-frequency-speed-relationship
  type: hard
builds-toward:
- diffraction-gratings
- youngs-double-slit
tags:
- interference
- two-source
- pattern
stage: formal-systems
status: draft
---

# Two-Source Interference Patterns

## Core Idea
Two coherent sources separated by distance d create an interference pattern in space, with alternating regions of constructive and destructive interference. Bright fringes occur where the path difference equals nλ (n = 0, 1, 2, ...), and dark fringes occur where the path difference equals (n + ½)λ. The fringe spacing depends on wavelength, source separation, and observation distance.

## Explainer

You already know the core principle from constructive and destructive interference: when two waves overlap, their amplitudes add. If they arrive in phase — crest meeting crest — you get a bright spot. If they arrive half a wavelength out of phase — crest meeting trough — they cancel. Two-source interference patterns take this idea and map it across a region of space: at every point in front of the sources, the two waves travel different distances, and that **path difference** determines whether those waves arrive in phase or out of phase.

Imagine two identical speakers (or the two slits in Young's experiment, or two antennas) separated by distance d, both broadcasting the same wavelength λ. For any observation point P, draw lines from each source to P. The difference in those two distances is the path difference Δ. If Δ = 0, 1λ, 2λ, ... — any whole number of wavelengths — the waves arrive perfectly in phase and you get a **bright fringe** (constructive interference). If Δ = ½λ, 3/2λ, 5/2λ, ... — any half-integer number of wavelengths — the waves arrive exactly out of phase and you get a **dark fringe** (destructive interference). The pattern of bright and dark bands you observe on a distant screen is simply the spatial map of where these path-difference conditions are satisfied.

The geometry makes the fringe spacing predictable. For a screen at distance L >> d, the fringe spacing Δy = λL/d. Three variables control the pattern: wavelength λ (longer wavelength → wider fringes), source separation d (closer sources → wider fringes), and screen distance L (farther screen → wider fringes). These relationships are not independent of your prerequisite knowledge — **wavelength** and **frequency** are linked by v = fλ, so changing frequency changes λ, which directly rescales the entire fringe pattern.

**Coherence** is the hidden requirement that makes the pattern stable. Both sources must maintain a fixed phase relationship over time — they must be synchronized. Sunlight from two separate holes would not produce a stable pattern because the phase relationship randomly fluctuates; the bright and dark fringes would wash out into uniform brightness. This is why Young's original experiment used a single source illuminating two slits (the slits are coherent because they're both driven by the same wavefront), and why laser sources make interference experiments easy while ordinary light bulbs do not. Two-source interference is the simplest model for understanding all wave interference, and Young's double-slit result — which you'll see next — is its most famous application.
