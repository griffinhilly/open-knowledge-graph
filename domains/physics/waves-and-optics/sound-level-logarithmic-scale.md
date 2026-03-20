---
id: sound-level-logarithmic-scale
title: Sound Intensity Level and the Decibel Scale
domain: physics
course: waves-and-optics
prerequisites:
- id: energy-flow-rate-intensity
  type: hard
tags:
- acoustics
- sound
- logarithm
stage: advanced
status: draft
---

# Sound Intensity Level and the Decibel Scale

## Core Idea
The decibel scale L_dB = 10 log₁₀(I/I₀) quantifies sound intensity relative to a reference (I₀ = 10⁻¹² W/m²). A 10 dB increase represents a factor of 10 in intensity. This logarithmic scale compresses the huge range of audible intensities (factor of 10¹²) into a manageable range (0–140 dB). Human perception of loudness is roughly logarithmic, justifying this choice.

## Explainer

You already know that **intensity** is the power carried by a wave per unit area (W/m²) and that it decreases with distance as a wave spreads. The range of intensities audible to the human ear is extraordinary: from the threshold of hearing at 10⁻¹² W/m² to the threshold of pain at roughly 1 W/m² — a factor of one trillion (10¹²). Representing this span on a linear scale is impractical; any graph large enough to show a jet engine would make a whisper invisible. This is exactly the problem the **decibel scale** solves through logarithmic compression.

The formula L = 10 log₁₀(I / I₀) converts a ratio of intensities into a compact number, using I₀ = 10⁻¹² W/m² as the reference level (approximately the softest sound a healthy young person can detect). The key relationships to internalize: multiplying intensity by 10 adds exactly 10 dB; doubling intensity adds about 3 dB (since log₁₀(2) ≈ 0.3). The entire trillion-to-one span from threshold of hearing to threshold of pain maps cleanly onto 0–120 dB. Normal conversation sits around 60 dB; a rock concert around 110 dB; a whisper around 30 dB.

The logarithmic scale reflects how the auditory system actually works. Your ear does not perceive intensity linearly — perceived loudness tracks roughly the logarithm of intensity. An increase from 40 dB to 50 dB sounds roughly as large a step as an increase from 80 dB to 90 dB, even though both represent the same 10-fold change in intensity. **Equal perceived steps correspond to equal intensity ratios**, which is precisely what the decibel scale encodes. This same perceptual logic explains why musical pitch is organized in octaves (each doubling of frequency), why the pH scale is logarithmic, and why the Richter scale is logarithmic — whenever the response is proportional to ratio rather than absolute difference, a log scale matches perception.

A common error is to add decibels as if they were ordinary numbers. Two identical 70 dB sources do not produce 140 dB — they produce about 73 dB. Why? Because 70 dB corresponds to an intensity of I₀ × 10⁷, and two such sources double that intensity to 2 × I₀ × 10⁷. Doubling intensity adds log₁₀(2) × 10 ≈ 3 dB. Ten identical jackhammers produce only about 10 dB more than one. This counterintuitive result is the unavoidable arithmetic of the logarithmic scale, with real practical consequences for noise control and hearing protection.
