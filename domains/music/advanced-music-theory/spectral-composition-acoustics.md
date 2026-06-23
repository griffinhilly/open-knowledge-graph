---
id: spectral-composition-acoustics
title: Spectral Composition and Harmonic Spectrum Derivation
domain: music
course: advanced-music-theory
prerequisites:
- id: spectral-analysis-acoustics
  type: hard
- id: extended-instrumental-techniques
  type: soft
- id: fourier-series-definition
  type: soft
- id: just-intonation-acoustics
  type: soft
builds-toward:
- timbre-frequency-domain
tags:
- spectral
- composition
- acoustics
- timbre
stage: expert
status: validated
---

# Spectral Composition and Harmonic Spectrum Derivation

## Core Idea
Spectral composition derives musical structure from the harmonic spectrum of instrumental tones or other acoustic phenomena. Composers like Grisey and Murail analyze a complex tone and orchestrate its partials, creating works where harmony emerges from acoustical truth rather than abstract harmony.

## Questions

```yaml
- question: "A spectral composer analyzes a low E trombone tone at approximately 65 Hz. The 7th partial of this tone falls at roughly 455 Hz. How does this pitch relate to equal temperament?"
  type: multiple-choice
  options:
    - "It falls exactly on a note of the equal-tempered scale, since 455 Hz is close to A4"
    - "It is approximately 31 cents flat relative to the nearest equal-tempered pitch, requiring a microtonal notation"
    - "It is inaudible because upper partials are too faint to matter compositionally"
    - "It falls exactly on a note because the harmonic series and equal temperament were designed to align"
  answer: 1
  explanation: "The 7th partial lies roughly 31 cents (about a third of a half-step) flat of the nearest equal-tempered pitch. Equal temperament is a mathematical compromise that divides the octave into 12 equal logarithmic steps; this grid does not align with the integer-ratio partial structure of the harmonic series. Spectral composers must use microtonal notation and extended instrumental techniques to notate and produce these acoustically accurate pitches. Options A and D reflect a common misconception that equal temperament and the harmonic series are the same thing."

- question: "What most fundamentally distinguishes spectral composition from twelve-tone serialism as compositional systems?"
  type: multiple-choice
  options:
    - "Spectral music uses larger orchestras and more instruments"
    - "Twelve-tone music uses all 12 pitch classes equally, while spectral music uses only a few"
    - "Spectral harmony is derived from the physical acoustics of real sounds, while twelve-tone rows are abstract permutational constructs with no acoustical basis"
    - "Spectral music uses computer analysis while serialism uses only pencil and paper"
  answer: 2
  explanation: "The fundamental distinction is the source of harmonic material. Twelve-tone rows are combinatorial: you choose an ordering of 12 pitch classes and derive its transformations (inversion, retrograde, etc.). The intervals have no acoustical justification — they are determined by the chosen row. Spectral harmony, by contrast, is derived from the measured frequency content of a real or synthesized sound. The 'justification' for a spectral chord is acoustical rather than abstract. This is what Grisey meant by 'working with sounds, not against them.'"

- question: "Because the harmonic series consists of integer multiples of a fundamental, most partials above the fundamental correspond to notes already found in Western equal temperament."
  type: true-false
  answer: false
  explanation: "The harmonic series uses integer-ratio frequency relationships, while equal temperament divides the octave into 12 equal semitones using the 12th root of 2. These two systems only coincide at the octave (2nd partial) and approximately at the fifth (3rd partial). The 7th partial is ~31 cents flat, the 11th partial ~49 cents sharp, and higher partials deviate even more significantly. This is exactly why spectral composers require microtones — notating these partials as the nearest equal-tempered pitch introduces acoustical inaccuracy."

- question: "If an orchestra performs the partials of a single low-frequency tone at the correct frequencies and amplitudes, the ear may perceive the result as a single fused pitch rather than an ensemble of separate notes."
  type: true-false
  answer: true
  explanation: "This phenomenon — spectral fusion — is central to spectral compositional aesthetics. When harmonically related partials are presented at appropriate amplitudes, the auditory system integrates them into a single perceived pitch rather than analyzing them as separate tones. This is the same process by which a single cello note is perceived as unified despite containing many partials. Spectral composers exploit the continuum between fusion and separation: by altering amplitudes, spacing, or inharmonicity, they can move a chord between 'sounds like one note' and 'sounds like many separate pitches.'"

- question: "Why do spectral composers use microtones, and what does this reveal about their underlying compositional philosophy?"
  type: short-answer
  answer: "Microtones are required because the harmonic series — the acoustic foundation of spectral harmony — does not align with equal temperament. To represent partials accurately (e.g., the 7th partial ~31 cents flat), composers must notate and perform pitches between the standard semitones. Philosophically, this reveals the spectral view that harmony should be discovered from acoustical physics rather than invented as an abstract system. Equal temperament is treated as a practical approximation that sacrifices acoustic accuracy; spectral music prioritizes fidelity to the physical reality of vibration over notational convenience."
  explanation: "This question targets the conceptual core: spectral music is not just a style choice but a philosophical stance that grounds harmonic language in physics. The use of microtones is the most audible consequence of taking acoustical accuracy seriously. Students who understand this will also understand why the harmonic series, not a scale or row, is the fundamental unit of spectral composition."
```

## Explainer

Every acoustic instrument produces not a single pure tone but a **harmonic series**: a fundamental frequency f₀ accompanied by overtones at integer multiples 2f₀, 3f₀, 4f₀, and so on. A low E on a cello at 82 Hz simultaneously produces partials at 164 Hz, 246 Hz, 328 Hz, and beyond, each with different amplitudes that shape the characteristic cello timbre. From your prerequisite in Fourier series, you know that any periodic waveform decomposes uniquely into sinusoidal components at these frequencies — the spectrum is the Fourier decomposition of the sound. Spectral composition takes this acoustical fact as its compositional starting point: rather than choosing harmonies from a theoretical system like functional tonality or twelve-tone rows, spectral composers derive harmonies directly from the spectrum of a real or imagined sound.

The method in practice begins with a **spectral analysis** of an instrumental sound. Gérard Grisey's *Partiels* (1975), the foundational work of the French spectral school, opens with the low E of a trombone (approximately 65 Hz). Grisey analyzed this spectrum, identifying the frequencies and relative amplitudes of each partial, then orchestrated those partials across the ensemble — different instruments sustaining specific pitches that correspond to the harmonics of the trombone tone. The resulting chord is not a stack of thirds or fifths from any Western scale; it is a direct sonic magnification of a single complex tone. The "music" at the opening of *Partiels* is, in a precise sense, a single note played very slowly at enormous scale.

The harmonic series is not equal-tempered: the 7th partial (7f₀) falls roughly 31 cents flat of the nearest equal-tempered pitch, and the 11th partial is about 49 cents sharp. This means spectral music routinely uses **microtones** — pitches between the keys of a standard piano — because acoustical accuracy requires them. Rather than treating equal temperament as a given, spectral composers treat it as an approximation that sacrifices some acoustic truth for practical convenience. Extended instrumental techniques from your prerequisite become essential: quarter-tone fingerings, harmonics, and special bowing produce the intermediate pitches the spectral harmonic spectrum requires. The orchestra becomes a spectrally accurate instrument rather than a twelve-pitch-class system.

What spectral composition offers conceptually is a grounding of harmonic language in physics rather than convention. Traditional harmonic systems (tonal progressions, intervallic rows) are human constructs. Spectral harmony claims to be *discovered* rather than invented — the intervals between partials are fixed by physics, not by culture. Grisey described spectral music as working "with sounds, not against them," meaning that the composition follows the acoustic logic of vibration rather than imposing abstract structure. Whether or not one accepts this philosophical stance, the compositional technique opens genuine possibilities: you can construct "chords" that function as frozen timbres, evolve harmonies by morphing from one spectrum to another (as a note decays, the relative prominence of its partials changes), and use the concept of **spectral fusion** — when partials align correctly, the ear fuses them into a single perceived pitch rather than hearing them as separate notes. Mastery of these techniques requires exactly what your prerequisites provide: the ability to analyze spectra (Fourier analysis) and to produce unusual timbres on acoustic instruments (extended techniques).
