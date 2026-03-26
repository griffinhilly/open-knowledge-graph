---
id: fundamental-frequency-and-overtones
title: Fundamental Frequency and Overtones
domain: physics
course: waves-and-optics
prerequisites:
- id: acoustic-resonance-strings
  type: hard
- id: acoustic-resonance-pipes
  type: soft
tags:
- fundamental
- overtones
- harmonics
- timbre
stage: formal-systems
status: validated
---

# Fundamental Frequency and Overtones

## Core Idea
The fundamental frequency is the lowest resonant frequency of an object. Overtones (harmonics) are integer multiples of the fundamental. The presence and relative amplitudes of overtones determine the timbre or tone quality of an instrument: a pure tone has only the fundamental, while musical instruments produce many overtones simultaneously.

## Questions

```yaml
- question: "A violin and a flute both play A4 (440 Hz) at the same volume. A trained listener can instantly tell them apart. What physically accounts for this difference?"
  type: multiple-choice
  options:
    - "The violin's string tension causes its fundamental frequency to be slightly higher than 440 Hz"
    - "Both instruments produce identical sound waves; the difference is purely a result of the listener's expectation"
    - "The flute produces only the fundamental frequency with no overtones, while the violin adds harmonics on top"
    - "The two instruments produce different relative amplitudes of overtones above the same 440 Hz fundamental"
  answer: 3
  explanation: "Timbre — the perceived sound quality — is physically encoded in the overtone recipe: which harmonics are present and how loud each is relative to the fundamental. Both instruments produce the same fundamental (440 Hz, A4), but the violin's body and strings excite a characteristic mixture of harmonics, while the flute's cylindrical bore produces a different mixture. Option C is a common misconception — the flute does produce overtones; it simply produces fewer and quieter high harmonics than the violin, giving it a purer, breathy character compared to the violin's richness."

- question: "A clarinet behaves as a cylindrical pipe closed at the reed end and open at the bell. Which set of resonant frequencies does it support?"
  type: multiple-choice
  options:
    - "All integer multiples of the fundamental: f₁, 2f₁, 3f₁, 4f₁ ..."
    - "Only odd-numbered harmonics: f₁, 3f₁, 5f₁, 7f₁ ..."
    - "Only even-numbered harmonics: 2f₁, 4f₁, 6f₁ ..."
    - "Only the fundamental frequency f₁, with no overtones"
  answer: 1
  explanation: "A closed-open pipe must have a pressure node at the closed end and an antinode at the open end. This boundary condition is satisfied only when the pipe length equals an odd number of quarter-wavelengths (L = λ/4, 3λ/4, 5λ/4, ...), corresponding to f₁, 3f₁, 5f₁ — odd harmonics only. Open pipes and strings support all integer harmonics (L = nλ/2). This is why the clarinet sounds distinctly different from the flute: its overtone spectrum contains only the odd-harmonic ladder, producing its characteristic hollow, woody timbre."

- question: "The fundamental frequency of a vibrating object determines its perceived pitch, while the relative amplitudes of its overtones determine its timbre."
  type: true-false
  answer: true
  explanation: "This is the correct two-part picture. Pitch is our perceptual response to the fundamental (lowest resonant) frequency — a string vibrating at 440 Hz sounds like A4 regardless of what instrument plays it. Timbre is the 'tone color' that distinguishes a violin from an oboe on the same note, and it is physically encoded in the overtone recipe: which harmonics are present and at what relative amplitudes. A pure sine wave has no overtones and sounds clinical and electronic; a rich instrument tone contains many harmonics at characteristic levels."

- question: "A pure tone containing primarily the fundamental frequency has a richer, more complex timbre than a musical instrument playing the same pitch."
  type: true-false
  answer: false
  explanation: "The opposite is true. A pure sine wave (single frequency, no overtones) is the simplest possible sound — it sounds like an electronic test tone. Musical instruments sound rich and complex precisely because they excite many overtones simultaneously. The more overtones present, and the more varied their amplitudes, the more characteristically 'instrumental' the timbre. Richness comes from the presence of harmonics, not their absence."

- question: "Why does plucking a guitar string near the bridge produce a brighter, harsher sound than plucking near the midpoint of the string?"
  type: short-answer
  answer: "Plucking near the bridge excites higher harmonics at greater amplitude, adding high-frequency overtone content that the ear perceives as brightness. Plucking near the midpoint suppresses even harmonics — those harmonics require an antinode at the midpoint, and exciting the string there interferes with them — favoring the fundamental and odd harmonics and producing a darker, more hollow tone with less high-frequency content."
  explanation: "The pluck location determines which harmonics are driven most efficiently. Harmonics that have a node at the pluck point are not efficiently excited. The midpoint of the string is a node for the 2nd harmonic (and all even harmonics with nodes there), so mid-plucking suppresses them. Near the bridge, the pluck point is close to the endpoint (a node for all harmonics), so all harmonics are driven with roughly proportional efficiency, producing a full, bright spectrum. Guitarists and violinists continuously vary plucking/bowing position to alter tone color."
```

## Explainer

From your study of acoustic resonance in strings and pipes, you know that a standing wave forms when the boundary conditions force nodes at specific points — the ends of a string, the closed end of a pipe, or the open ends of a flute. Each valid standing wave pattern corresponds to a resonant frequency, and the string or air column will naturally oscillate at any of these frequencies. The lowest one — the longest wavelength that fits the geometry — is the **fundamental frequency** (f₁). It sets the perceived pitch of the note.

The higher resonant frequencies are called **overtones** or **harmonics**. For an ideal stretched string fixed at both ends, these occur at exactly 2f₁, 3f₁, 4f₁, and so on — they are **integer multiples** of the fundamental, which is why the string is called a **harmonic oscillator**. The second harmonic (2f₁) fits exactly two half-wavelengths into the string's length; the third harmonic (3f₁) fits three. Each harmonic has an additional node in the middle of the string. Open cylindrical pipes (like a flute) follow the same integer-multiple pattern; closed pipes (like a clarinet) support only odd harmonics (f₁, 3f₁, 5f₁, ...) because the closed end forces a node while the open end forces an antinode.

When you pluck a guitar string or bow a violin, you don't excite just one frequency — you excite many harmonics simultaneously. The string vibrates at f₁ and 2f₁ and 3f₁ all at once, with different amplitudes for each. This mixture is what the ear hears as a single complex tone. The recipe of which harmonics are present and how loud each one is determines the **timbre** — the characteristic sound quality that makes a violin sound different from a flute even when both play the same note at the same volume. A pure sine wave at 440 Hz sounds clinical and electronic; an oboe playing A4 sounds rich and reedy because it adds a dense stack of overtones on top of the fundamental.

Different physical objects favor different overtone mixtures. A struck marimba bar has overtones shaped by the bar's mass distribution (which is why bars are often shaved underneath to tune the overtones). A plucked string's overtone mix depends on where along its length you pluck — plucking near the center suppresses even harmonics, producing a hollow sound; plucking near the bridge emphasizes them, producing brightness. Understanding the harmonic series is the gateway to explaining why instruments have their characteristic voices, how synthesizers recreate those voices digitally, and why some combinations of notes sound consonant while others clash.
