---
id: resonance-strings-fixed-ends
title: Resonance in Strings with Fixed Ends
domain: physics
course: waves-and-optics
prerequisites:
- id: standing-waves
  type: hard
builds-toward:
- fundamental-frequency-and-overtones
tags:
- resonance
- standing-waves
- musical-strings
stage: advanced
status: validated
---

# Resonance in Strings with Fixed Ends

## Core Idea
A string fixed at both ends resonates when its length equals an integer number of half-wavelengths: L = nλ/2. This produces standing waves with fixed nodes at the ends and resonant frequencies fₙ = nv/(2L), where n = 1,2,3... defines the harmonic number.

## Questions

```yaml
- question: "A guitarist presses a string down at a fret, shortening the vibrating length from L to L/2 while keeping tension unchanged. What happens to the resonant frequencies?"
  type: multiple-choice
  options:
    - "Only the fundamental frequency changes; the harmonics remain the same"
    - "All resonant frequencies double, since fₙ = nv/(2L) and L is halved"
    - "All resonant frequencies halve, because less string is available to vibrate"
    - "The resonant frequencies are unchanged because the same string and tension are used"
  answer: 1
  explanation: "The resonant frequencies are fₙ = nv/(2L). Wave speed v = √(T/μ) depends on tension and string density, neither of which changes when you press a fret. Only L changes — it halves. Since fₙ is proportional to 1/L, halving L doubles every harmonic: f₁ becomes 2f₁, f₂ becomes 2f₂, and so on. This is how fretting works: all harmonics shift up by the same factor, so the entire pitch rises by one octave."

- question: "Why can only specific frequencies create standing waves on a string fixed at both ends, rather than any arbitrary frequency?"
  type: multiple-choice
  options:
    - "Most frequencies dissipate too quickly in the string material to build up amplitude"
    - "The boundary condition — zero displacement at both fixed ends — requires the string length to equal an integer number of half-wavelengths"
    - "Wave speed on the string changes with frequency, filtering out most values"
    - "The string acts as a low-pass filter that only transmits frequencies below a cutoff"
  answer: 1
  explanation: "The fixed endpoints are hard constraints: the string cannot move there. Any standing wave must therefore have a node at each end. Only wavelengths satisfying L = nλ/2 (equivalently, λₙ = 2L/n) produce a pattern with nodes at both ends simultaneously. Any other wavelength would require non-zero displacement at a fixed end — an impossibility. The resonant condition is purely geometric: it is not about damping, dispersion, or filtering, but about which spatial patterns are compatible with the boundary."

- question: "Increasing the tension in a guitar string raises the frequencies of all its harmonics by the same multiplicative factor."
  type: true-false
  answer: true
  explanation: "Wave speed v = √(T/μ) increases with tension T, and all harmonic frequencies fₙ = nv/(2L) are proportional to v. Doubling the tension multiplies v by √2, which multiplies every harmonic by the same factor √2. This is why tuning a string raises (or lowers) its pitch uniformly across all harmonics rather than distorting the harmonic relationships — the timbre (ratio of harmonics) is preserved while the pitch shifts."

- question: "A string fixed at both ends can sustain a standing wave at any frequency, provided the driving amplitude is small enough to avoid nonlinear effects."
  type: true-false
  answer: false
  explanation: "Resonance in a fixed-fixed string is not a matter of amplitude — it is a geometric constraint. Only frequencies corresponding to integer multiples of the fundamental (fₙ = nv/2L) produce standing waves, because only these frequencies yield wavelengths where exactly n half-wavelengths fit in length L, placing nodes at both fixed ends. At any other driving frequency, the reflections from the two ends interfere destructively and no standing wave builds up, regardless of how small the amplitude is."

- question: "A guitarist plucks a string near the bridge and hears a bright, cutting tone; plucking near the middle produces a rounder, warmer sound. Explain this difference in terms of the resonance condition and harmonic content."
  type: short-answer
  answer: "Plucking at a point excites harmonics whose antinodes are at or near that point, and suppresses harmonics whose nodes fall there. The middle of the string is a node for all even harmonics (n = 2, 4, 6...) and an antinode for odd harmonics (n = 1, 3, 5...). Plucking near the middle therefore strongly excites the fundamental and odd harmonics while suppressing even harmonics — producing a round, hollow tone. Plucking near the bridge, which is close to a node for all harmonics, excites higher harmonics more strongly and the fundamental less, producing a bright, cutting sound rich in high-frequency overtones."
  explanation: "This is a direct application of the resonance condition: the pluck point determines the initial displacement shape of the string, which can be decomposed into contributions from each harmonic. A point that is a node for a given harmonic contributes nothing to that harmonic's excitation. Guitar and other stringed instrument players exploit this continuously — playing position (sul tasto near the fingerboard vs. sul ponticello near the bridge) is one of the primary timbre controls available to them."
```

## Explainer

From your study of standing waves, you know that two waves of equal amplitude and frequency traveling in opposite directions combine to produce a pattern that oscillates in place — fixed nodes where displacement is always zero, and antinodes where displacement swings between maximum positive and negative. A string fixed at both ends is the physical system that forces this pattern to occur: the boundary conditions at the two fixed endpoints require nodes there, and the resonant frequencies are exactly those for which the geometry works out.

Think about what "fixed end" means physically. At a fixed endpoint, the string cannot move — the wall or bridge exerts whatever force is needed to keep displacement zero. This is a hard constraint: the standing wave must have a **node at every fixed end**. So the question becomes: for a given wave speed v on the string, which wavelengths λ produce a pattern with nodes at both ends when the string has length L? The answer is all wavelengths where exactly an integer number of half-wavelengths fits: L = nλ/2, so λₙ = 2L/n. Each allowed wavelength corresponds to a **harmonic**: n = 1 is the **fundamental** (one half-wavelength spans the string, one antinode in the middle), n = 2 is the **second harmonic** (two half-wavelengths, two antinodes), n = 3 the third, and so on. Any other wavelength would require a non-zero displacement at the fixed end, violating the boundary condition — so those frequencies simply cannot sustain a standing wave.

Converting wavelength to frequency using f = v/λ gives fₙ = nv/(2L). The fundamental frequency f₁ = v/(2L) sets the spacing: every harmonic is an integer multiple of f₁. This integer relationship — harmonics at f₁, 2f₁, 3f₁, ... — is what makes stringed instruments sound musical. The **wave speed v** on a string depends on tension T and linear mass density μ: v = √(T/μ). Tightening a guitar string (increasing T) raises v and therefore raises all harmonics equally. Using a lighter string (smaller μ) also increases v. Pressing a string down at a fret shortens L, which increases all fₙ since they depend on 1/L. Every time a guitarist tunes or plays a note, they are manipulating this formula.

In a real plucked string, the fundamental and all harmonics are excited simultaneously. The relative strength of each harmonic — called the **harmonic spectrum** or **timbre** — determines the instrument's characteristic sound. A guitar plucked near the bridge excites high harmonics strongly (bright, cutting sound); plucked near the middle, the even harmonics are suppressed (the pluck point is an antinode of odd harmonics and a node of even ones), producing a rounder tone. This is the physics behind the difference between guitar playing positions, and why bowing versus plucking a violin string produces different timbres. The resonance condition L = nλ/2 is simple; the richness comes from how many harmonics are excited and in what proportions.
