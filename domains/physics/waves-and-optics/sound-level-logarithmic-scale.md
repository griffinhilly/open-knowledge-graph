---
id: sound-level-logarithmic-scale
title: Sound Intensity Level and the Decibel Scale
domain: physics
course: waves-and-optics
prerequisites:
- id: energy-flow-rate-intensity
  type: hard
- id: acoustic-pressure-and-amplitude
  type: soft
tags:
- acoustics
- sound
- logarithm
stage: advanced
status: validated
---
# Sound Intensity Level and the Decibel Scale

## Core Idea
The decibel scale L_dB = 10 log₁₀(I/I₀) quantifies sound intensity relative to a reference (I₀ = 10⁻¹² W/m²). A 10 dB increase represents a factor of 10 in intensity. This logarithmic scale compresses the huge range of audible intensities (factor of 10¹²) into a manageable range (0–140 dB). Human perception of loudness is roughly logarithmic, justifying this choice.

## Questions

```yaml
- question: "Two identical loudspeakers, each producing 80 dB, are placed side by side and play simultaneously. The combined sound level is approximately:"
  type: multiple-choice
  options:
    - "160 dB — you add the decibel values of both sources"
    - "80 dB — the two sources are in phase and cancel"
    - "83 dB — doubling intensity adds approximately 3 dB"
    - "90 dB — each additional identical source adds 10 dB"
  answer: 2
  explanation: "80 dB corresponds to an intensity of I₀ × 10⁸. Two identical sources together produce 2 × I₀ × 10⁸. Applying the formula: L = 10 log₁₀(2 × 10⁸) = 10(log₁₀2 + 8) ≈ 10(0.3 + 8) = 83 dB. Decibels are logarithmic — you cannot add them linearly. The common error of adding the dB values (80 + 80 = 160) confuses the compressed logarithmic representation with the underlying intensity values."

- question: "A sound level increases from 60 dB to 90 dB. By what factor has the intensity increased?"
  type: multiple-choice
  options:
    - "1.5 times — the ratio 90/60"
    - "30 times — the difference 90 − 60"
    - "1000 times — 10^(30/10) = 10³"
    - "2 times — one additional octave of loudness"
  answer: 2
  explanation: "A difference of ΔL dB corresponds to an intensity ratio of 10^(ΔL/10). For ΔL = 30 dB: 10^(30/10) = 10³ = 1000. The tempting wrong answer is 30 (the arithmetic difference), which confuses the dB value with the intensity ratio. 'Adding 30 dB' means multiplying intensity by 1000, not adding 30 units of intensity."

- question: "A 20 dB increase in sound level corresponds to a 100-fold increase in intensity."
  type: true-false
  answer: true
  explanation: "Using the formula: ΔL = 10 log₁₀(I₂/I₁). For ΔL = 20: 20 = 10 log₁₀(ratio), so log₁₀(ratio) = 2, giving ratio = 10² = 100. Each 10 dB increase multiplies intensity by 10, so two successive 10 dB increases multiply by 10 × 10 = 100. The logarithmic scale converts multiplicative factors into additive increments."

- question: "Ten identical jackhammers produce a sound level approximately ten times higher in decibels than a single jackhammer."
  type: true-false
  answer: false
  explanation: "Ten identical sources produce 10 times the intensity of one, which corresponds to an increase of 10 log₁₀(10) = 10 dB — not 10 times the decibel value. If one jackhammer produces 100 dB, ten together produce about 110 dB, not 1000 dB. The confusion arises from treating decibel values as if they were linear quantities that scale with the number of sources. The logarithmic scale means that adding more sources has diminishing returns in perceived loudness."

- question: "Why do two identical 70 dB sound sources together produce approximately 73 dB rather than 140 dB?"
  type: short-answer
  answer: "Because decibels are a logarithmic scale encoding intensity *ratios*, not absolute intensities. Each 70 dB source has intensity I = I₀ × 10⁷. Two together produce 2I₀ × 10⁷. Converting: L = 10 log₁₀(2 × 10⁷) = 10(log₁₀2 + 7) ≈ 10(0.301 + 7) = 73 dB. Adding the sources doubles the intensity, and doubling intensity corresponds to +3 dB regardless of the starting level. The number 140 dB would require an intensity 10¹⁴ times the reference — a level that would destroy hearing instantly, which is clearly wrong for two ordinary speakers."
  explanation: "The 140 dB error comes from treating dB like a count. But dB encodes a ratio logarithmically. You must convert to intensity, add intensities, then convert back. The practical lesson: combining identical sources never more than doubles intensity, adding at most 3 dB per doubling of the number of sources — so 10 sources add only 10 dB, and 100 sources add only 20 dB."
```

## Explainer

You already know that **intensity** is the power carried by a wave per unit area (W/m²) and that it decreases with distance as a wave spreads. The range of intensities audible to the human ear is extraordinary: from the threshold of hearing at 10⁻¹² W/m² to the threshold of pain at roughly 1 W/m² — a factor of one trillion (10¹²). Representing this span on a linear scale is impractical; any graph large enough to show a jet engine would make a whisper invisible. This is exactly the problem the **decibel scale** solves through logarithmic compression.

The formula L = 10 log₁₀(I / I₀) converts a ratio of intensities into a compact number, using I₀ = 10⁻¹² W/m² as the reference level (approximately the softest sound a healthy young person can detect). The key relationships to internalize: multiplying intensity by 10 adds exactly 10 dB; doubling intensity adds about 3 dB (since log₁₀(2) ≈ 0.3). The entire trillion-to-one span from threshold of hearing to threshold of pain maps cleanly onto 0–120 dB. Normal conversation sits around 60 dB; a rock concert around 110 dB; a whisper around 30 dB.

The logarithmic scale reflects how the auditory system actually works. Your ear does not perceive intensity linearly — perceived loudness tracks roughly the logarithm of intensity. An increase from 40 dB to 50 dB sounds roughly as large a step as an increase from 80 dB to 90 dB, even though both represent the same 10-fold change in intensity. **Equal perceived steps correspond to equal intensity ratios**, which is precisely what the decibel scale encodes. This same perceptual logic explains why musical pitch is organized in octaves (each doubling of frequency), why the pH scale is logarithmic, and why the Richter scale is logarithmic — whenever the response is proportional to ratio rather than absolute difference, a log scale matches perception.

A common error is to add decibels as if they were ordinary numbers. Two identical 70 dB sources do not produce 140 dB — they produce about 73 dB. Why? Because 70 dB corresponds to an intensity of I₀ × 10⁷, and two such sources double that intensity to 2 × I₀ × 10⁷. Doubling intensity adds log₁₀(2) × 10 ≈ 3 dB. Ten identical jackhammers produce only about 10 dB more than one. This counterintuitive result is the unavoidable arithmetic of the logarithmic scale, with real practical consequences for noise control and hearing protection.
