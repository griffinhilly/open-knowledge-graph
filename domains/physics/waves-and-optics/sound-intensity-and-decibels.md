---
id: sound-intensity-and-decibels
title: Sound Intensity and the Decibel Scale
domain: physics
course: waves-and-optics
prerequisites:
- id: sound-waves-intro
  type: hard
- id: logarithms-intro
  type: hard
- id: resonance-strings-and-pipes
  type: soft
- id: wave-energy-and-intensity
  type: soft
builds-toward:
- doppler-effect
tags:
- intensity
- decibels
- inverse square law
- sound level
- power
stage: advanced
status: validated
---
# Sound Intensity and the Decibel Scale

## Core Idea
Sound intensity I is the power per unit area (W/m²) carried by the wave. For a point source radiating uniformly, I follows an inverse-square law: I ∝ 1/r². Because the human ear responds logarithmically, the decibel scale is used: β = 10 log₁₀(I/I₀), where I₀ = 10⁻¹² W/m² is the threshold of hearing. Each 10 dB increase represents a tenfold increase in intensity.

## How It's Best Learned
Calculate the dB level for common sounds (conversation ≈ 60 dB, concert ≈ 110 dB) and verify that doubling distance reduces level by about 6 dB.

## Common Misconceptions
- A 20 dB sound is not twice as loud as a 10 dB sound; it is ten times more intense.
- Decibels are a ratio, not an absolute unit — the reference level I₀ must always be specified.

## Questions

```yaml
- question: "Two identical speakers each producing 70 dB are placed side by side and both turned on. What is the resulting sound level?"
  type: multiple-choice
  options:
    - "140 dB — doubling the number of sources doubles the decibel level"
    - "73 dB — doubling the intensity adds approximately 3 dB"
    - "70 dB — the two identical sources cancel each other out"
    - "80 dB — adding a second source always adds 10 dB"
  answer: 1
  explanation: "Doubling intensity (I₂ = 2I₁) adds 10 log₁₀(2) ≈ 3 dB — not 70 dB. The most tempting wrong answer (140 dB) treats decibels as if they add arithmetically, but the dB scale is logarithmic: it compresses intensity ratios, so equal dB steps represent equal intensity *ratios*, not equal additions. Two identical sources together double the physical intensity, which corresponds to a 3 dB increase."

- question: "A sound source measures 80 dB at 10 meters. You move to 40 meters away. What is the approximate sound level at the new distance?"
  type: multiple-choice
  options:
    - "20 dB — the level decreases proportionally with distance"
    - "74 dB — the level drops by 6 dB for every factor-of-4 increase in distance"
    - "68 dB — quadrupling the distance drops intensity by a factor of 16, reducing the level by about 12 dB"
    - "60 dB — moving twice as far reduces sound level by 20 dB"
  answer: 2
  explanation: "Moving from 10 m to 40 m quadruples the distance (×4), which equals two consecutive doublings. The inverse-square law says intensity drops by 4² = 16. Level change = –10 log₁₀(16) ≈ –12 dB, giving 80 – 12 = 68 dB. Equivalently: each doubling of distance subtracts ~6 dB, and two doublings (10→20→40 m) subtract ~12 dB. Option B incorrectly applies the 6 dB rule to a factor-of-4 distance change rather than a factor-of-2."

- question: "A sound measuring 60 dB is 10 times more intense than a sound measuring 50 dB."
  type: true-false
  answer: true
  explanation: "This follows directly from the decibel definition: each 10 dB increase corresponds to a factor of 10 in intensity. From β = 10 log₁₀(I/I₀), a difference of 10 dB means 10 = 10 log₁₀(I₂/I₁), so I₂/I₁ = 10. Students sometimes expect a smaller intensity ratio for a modest-sounding 10 dB difference, but the logarithmic scale is precisely designed so that equal dB intervals represent equal intensity ratios."

- question: "A 40 dB sound is twice as intense as a 20 dB sound."
  type: true-false
  answer: false
  explanation: "40 dB and 20 dB differ by 20 dB, which corresponds to a factor of 10²⁰/¹⁰ = 100 in intensity — not a factor of 2. 'Twice as intense' would be an increase of only 10 log₁₀(2) ≈ 3 dB. This is one of the most common misconceptions about the decibel scale: the numbers feel linear (40 is twice 20), but they represent a logarithmic relationship where the intensity ratio is 100, not 2."

- question: "Why does the decibel scale use a logarithm rather than expressing sound intensity directly in watts per square meter?"
  type: short-answer
  answer: "The human auditory system spans an intensity range of roughly 10¹² — from the threshold of hearing at 10⁻¹² W/m² to the pain threshold near 1 W/m². This makes direct W/m² values inconveniently small and hard to compare. More fundamentally, the ear responds roughly logarithmically: equal ratios of intensity produce equal perceived differences in loudness. The decibel logarithm converts multiplicative intensity relationships into additive dB steps, compressing a trillion-to-one physical range into a 0–120 dB scale that tracks how loudness is actually perceived."
  explanation: "The logarithm is not just computational convenience — it reflects the structure of human perception. The ear is a ratio detector, not a difference detector. This is why both the decibel scale and the musical frequency scale (octaves) are logarithmic: they match the perceptual architecture of the auditory system."
```

## Explainer

From wave energy, you know that intensity means power per unit area — the energy the wave delivers per second to each square meter of surface it passes through. For a point source radiating equally in all directions, the wave spreads over a sphere of area 4πr². Since the source's total power P is constant, the intensity at distance r is I = P/(4πr²). Double the distance and intensity drops by a factor of four. Triple it and intensity drops by nine. This **inverse-square law** explains why sounds fade so quickly with distance — standing twice as far from a speaker delivers one-quarter the acoustic power to your ear.

Now connect this to **logarithms**, which you've studied as a tool for compressing quantities that span enormous ranges. Human hearing is sensitive over an intensity range of roughly 10¹² — from the threshold of hearing at I₀ = 10⁻¹² W/m² to the threshold of pain near 1 W/m². Expressing everyday sounds in watts per square meter produces numbers so small (conversation ≈ 10⁻⁶ W/m²) that comparing them is inconvenient. The logarithm collapses this. The **decibel** level is defined as β = 10 log₁₀(I/I₀). A whisper at 10⁻¹⁰ W/m² gives β = 10 log₁₀(10⁻¹⁰/10⁻¹²) = 10 log₁₀(100) = 20 dB. A conversation at 10⁻⁶ W/m² gives β = 10 × 6 = 60 dB. A rock concert near 10⁻¹ W/m² gives β = 110 dB. The entire 10¹² range compresses into 0–120 dB — a scale that matches how our ears actually perceive relative loudness.

The most important arithmetic rule: **every 10 dB corresponds to a factor of 10 in intensity**. This follows directly from the definition: if I₂ = 10 I₁, then β₂ − β₁ = 10 log₁₀(10) = 10 dB. A 70 dB vacuum cleaner is ten times more intense than a 60 dB conversation; a 110 dB concert is 10,000 times more intense than conversation. Two useful derived results: doubling intensity adds 10 log₁₀(2) ≈ 3 dB, and doubling distance (reducing intensity by 4) drops the level by about 6 dB. These approximations are worth memorizing for quick estimates.

A subtle but important point: the decibel scale measures physical intensity, not perceived loudness. The ear's sensitivity varies with frequency — a 1,000 Hz tone at 60 dB sounds much louder than a 100 Hz tone at 60 dB. Audio engineers use **loudness-weighted scales** (A-weighting, phon curves) that account for this, which is why you'll see "dBA" on noise regulations. For physics problems, however, stick with the standard intensity-based definition. Also remember that decibels are always a ratio relative to a reference level: I₀ = 10⁻¹² W/m² is the standard acoustic reference, but other fields use different references (dBm in radio engineering uses 1 milliwatt). The formula is always β = 10 log₁₀(I/I_reference), and the reference must be stated for the number to have meaning.
