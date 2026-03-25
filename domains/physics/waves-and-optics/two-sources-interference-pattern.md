---
id: two-sources-interference-pattern
title: Interference from Two Coherent Sources
domain: physics
course: waves-and-optics
prerequisites:
- id: linear-superposition-principle
  type: hard
- id: phase-of-oscillation-initial
  type: hard
- id: beats-and-beat-frequency
  type: soft
builds-toward:
- bright-fringes-dark-fringes-spacing
- double-aperture-interference-fringe
tags:
- interference
- coherence
- patterns
stage: advanced
status: validated
---
# Interference from Two Coherent Sources

## Core Idea
Two coherent sources (same frequency, fixed phase difference) create an interference pattern of bright and dark regions. Bright fringes occur where waves arrive in phase (path difference = nλ); dark fringes where they arrive 180° out of phase (path difference = (n+½)λ). The visibility of fringes depends on the sources' coherence.

## Questions

```yaml
- question: "Two identical loudspeakers emit the same frequency, but Speaker B is connected with reversed polarity (a 180° phase shift relative to Speaker A). At a point equidistant from both speakers, what do you expect to hear?"
  type: multiple-choice
  options:
    - "Loud sound, because the path difference is zero — constructive interference occurs whenever path difference is zero"
    - "Silence, because the 180° source phase difference makes the total phase difference 180° at equal path lengths, causing destructive interference"
    - "Loud sound, because reversed polarity only affects the speaker cone direction, not the sound waves themselves"
    - "It depends on the frequency — some frequencies will constructively interfere, others destructively"
  answer: 1
  explanation: "The total phase difference at any point has two contributions: source phase difference plus path-difference phase. At equal path lengths, the path-difference phase is zero, but the 180° source phase difference remains. Total phase = 180°, so waves cancel. This is the key subtlety: constructive interference requires path difference = nλ AND the sources in phase. If sources have a built-in phase offset, the entire pattern shifts — a bright fringe location becomes dark."

- question: "Two coherent sources produce an interference pattern. The wavelength is doubled while source separation stays the same. What happens to the spacing between adjacent bright fringes?"
  type: multiple-choice
  options:
    - "Fringe spacing halves — longer wavelength means more waves fit between sources, so fringes pack tighter"
    - "Fringe spacing is unchanged — it depends only on source coherence, not wavelength"
    - "Fringe spacing doubles — fringe spacing is proportional to wavelength"
    - "The pattern disappears — changing wavelength breaks the coherence condition"
  answer: 2
  explanation: "Fringe spacing is proportional to wavelength (and inversely proportional to source separation). Longer wavelength means each successive path-difference multiple (0, λ, 2λ…) is reached at a wider angular separation, spreading the fringes apart. A common misconception is that fringe spacing depends only on coherence — coherence is a prerequisite for any stable pattern, but once satisfied, it is wavelength and geometry that determine fringe spacing."

- question: "For two coherent sources of equal amplitude, dark fringes represent total cancellation — the intensity is exactly zero at those locations."
  type: true-false
  answer: true
  explanation: "True. When two waves of equal amplitude arrive exactly 180° out of phase (path difference = (n + ½)λ with in-phase sources), they cancel completely by superposition, giving zero intensity. This complete cancellation only holds when amplitudes are equal; unequal amplitudes produce a minimum greater than zero."

- question: "Two independent light bulbs emit light at the same wavelength. If placed close together, they will produce a visible interference pattern, since both conditions — same frequency and close source separation — are met."
  type: true-false
  answer: false
  explanation: "False. Same wavelength (frequency) is necessary but not sufficient. Coherence requires a fixed phase relationship between the sources. Two independent light bulbs have randomly fluctuating phase relationships — at any instant they may be in phase, out of phase, or anywhere between, with no fixed relationship. The pattern averages to uniform intensity. Stable interference requires sources driven by the same oscillator (or the same wave split by two slits), not merely matching frequencies."

- question: "Why does creating a stable interference pattern require coherent sources? What happens to the pattern when the sources are incoherent?"
  type: short-answer
  answer: "A stable interference pattern requires that the phase difference at each fixed point in space remains constant over time. With coherent sources (fixed phase relationship), the path difference at each point is constant and so is the interference condition — producing persistent bright and dark fringes. With incoherent sources, the phase relationship fluctuates randomly; the interference condition at every point oscillates randomly between constructive and destructive on timescales faster than any detector can resolve, so the pattern time-averages to uniform intensity with no visible fringes."
  explanation: "This is the conceptual core: coherence is not a minor technical requirement but the fundamental reason a stable spatial pattern exists at all. The interference pattern is not a snapshot — it is a time-averaged structure that only persists when geometry (path difference) fully determines the phase difference, which requires a fixed source phase relationship."
```

## Explainer

The linear superposition principle you've studied tells you that when two waves overlap, their displacements add at every point in space and time. Two-source interference is what this looks like when two sources continuously radiate waves that overlap across an extended region — instead of a momentary addition, you get a stable spatial pattern of reinforcement and cancellation that persists as long as the sources keep emitting.

The essential requirement is **coherence**: the two sources must have the same frequency and a fixed phase relationship. If the phase between them fluctuates randomly (incoherent sources, like two separate light bulbs), the interference pattern averages out into uniform intensity. With coherent sources — two loudspeakers driven by the same oscillator, or two slits illuminated by the same laser — the phase difference at any fixed point in space depends only on the path difference from the two sources to that point. Because geometry doesn't change, the path difference at each point is constant, and so is the interference condition there. The result is a stable, spatially organized pattern.

Where the path difference equals a whole number of wavelengths (0, λ, 2λ, ...), waves from both sources arrive in phase and add constructively: **bright fringes** for light, loud regions for sound. Where path difference equals half-integer multiples (λ/2, 3λ/2, ...), waves arrive 180° out of phase and cancel: **dark fringes** or quiet regions. These alternating bands are laid out across the overlap zone like stripes. The spacing between adjacent bright fringes depends on the wavelength and the geometry — longer wavelength or closer-spaced sources produce wider-spaced fringes, while shorter wavelength or wider source separation produces tighter fringes.

One important subtlety: if the two sources have a built-in phase difference (one source starts half a cycle ahead of the other), the entire pattern shifts. A location that would have been a bright fringe with in-phase sources becomes a dark fringe when the sources are 180° out of phase. This is because the total phase difference at any point has two contributions: the **source phase difference** (fixed, set by the source configuration) and the **path difference phase** (varies with position). Keep these distinct in your analysis. The double-slit experiment you'll encounter next is the canonical application of this framework, and its fringe spacing formula follows directly from the geometry developed here.
