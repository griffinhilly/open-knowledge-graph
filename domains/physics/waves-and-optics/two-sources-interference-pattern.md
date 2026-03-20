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
builds-toward:
- bright-fringes-dark-fringes-spacing
- double-aperture-interference-fringe
tags:
- interference
- coherence
- patterns
stage: advanced
status: draft
---

# Interference from Two Coherent Sources

## Core Idea
Two coherent sources (same frequency, fixed phase difference) create an interference pattern of bright and dark regions. Bright fringes occur where waves arrive in phase (path difference = nλ); dark fringes where they arrive 180° out of phase (path difference = (n+½)λ). The visibility of fringes depends on the sources' coherence.

## Explainer

The linear superposition principle you've studied tells you that when two waves overlap, their displacements add at every point in space and time. Two-source interference is what this looks like when two sources continuously radiate waves that overlap across an extended region — instead of a momentary addition, you get a stable spatial pattern of reinforcement and cancellation that persists as long as the sources keep emitting.

The essential requirement is **coherence**: the two sources must have the same frequency and a fixed phase relationship. If the phase between them fluctuates randomly (incoherent sources, like two separate light bulbs), the interference pattern averages out into uniform intensity. With coherent sources — two loudspeakers driven by the same oscillator, or two slits illuminated by the same laser — the phase difference at any fixed point in space depends only on the path difference from the two sources to that point. Because geometry doesn't change, the path difference at each point is constant, and so is the interference condition there. The result is a stable, spatially organized pattern.

Where the path difference equals a whole number of wavelengths (0, λ, 2λ, ...), waves from both sources arrive in phase and add constructively: **bright fringes** for light, loud regions for sound. Where path difference equals half-integer multiples (λ/2, 3λ/2, ...), waves arrive 180° out of phase and cancel: **dark fringes** or quiet regions. These alternating bands are laid out across the overlap zone like stripes. The spacing between adjacent bright fringes depends on the wavelength and the geometry — longer wavelength or closer-spaced sources produce wider-spaced fringes, while shorter wavelength or wider source separation produces tighter fringes.

One important subtlety: if the two sources have a built-in phase difference (one source starts half a cycle ahead of the other), the entire pattern shifts. A location that would have been a bright fringe with in-phase sources becomes a dark fringe when the sources are 180° out of phase. This is because the total phase difference at any point has two contributions: the **source phase difference** (fixed, set by the source configuration) and the **path difference phase** (varies with position). Keep these distinct in your analysis. The double-slit experiment you'll encounter next is the canonical application of this framework, and its fringe spacing formula follows directly from the geometry developed here.
