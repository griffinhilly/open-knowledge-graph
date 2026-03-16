---
id: wave-interference
title: 'Wave Interference: Constructive and Destructive'
domain: physics
course: waves-and-optics
prerequisites:
- id: wave-superposition
  type: hard
builds-toward:
- youngs-double-slit
- single-slit-diffraction
- thin-film-interference
- standing-waves
- beats-and-beat-frequency
tags:
- interference
- constructive
- destructive
- path difference
- phase
stage: abstract-reasoning
status: validated
---

# Wave Interference: Constructive and Destructive

## Core Idea
Interference is the result of superposition when two coherent waves overlap. Constructive interference occurs when crests align (path difference = nλ), producing larger amplitude. Destructive interference occurs when a crest meets a trough (path difference = (n+½)λ), reducing or canceling amplitude. Coherence — constant phase relationship — is required for a stable interference pattern.

## How It's Best Learned
Begin with two speakers producing the same frequency tone and walk through the room to find nodes (quiet) and antinodes (loud). Then translate the geometric path-difference condition into the algebraic criteria for maxima and minima.

## Common Misconceptions
- Destructive interference does not destroy energy; energy is redistributed to other regions.
- Interference requires coherence; two independent light bulbs do not produce observable interference patterns because their phase relationship fluctuates randomly.

## Explainer

From wave superposition, you know that when two waves occupy the same space, their displacements add. Interference is what that addition looks like over time and space when the waves have a fixed relationship to each other. The critical new concept here is **coherence**: two sources are coherent if their phase difference stays constant over time. Coherent sources produce a stable, repeating pattern of high and low amplitude in space. Incoherent sources (like two separate light bulbs) have a randomly fluctuating phase difference, so their interference pattern averages away to uniform intensity — no pattern is visible.

**Constructive interference** occurs wherever two wave crests arrive at the same point simultaneously — or two troughs, which also add to give a large displacement. The key quantity is the **path difference**: the extra distance one wave travels compared to the other to reach the same point. When the path difference is exactly an integer multiple of the wavelength (0, λ, 2λ, 3λ, ...), the crests always align, and the amplitude at that point is the sum of the two individual amplitudes. This is where you hear the loudest sound from two speakers, or see the brightest fringes in optical setups.

**Destructive interference** occurs where a crest from one wave arrives simultaneously with a trough from the other. This happens when the path difference is a half-integer multiple of the wavelength (λ/2, 3λ/2, 5λ/2, ...). The displacements cancel, and the amplitude drops to zero — a **node**. In sound, this is the quiet spot between two speakers. In light, this is a dark fringe. The energy has not vanished; it has been redistributed to the constructive regions. This is why the bright fringes in an interference pattern are brighter than either source alone — the energy "missing" from the dark fringes has piled up into the bright ones.

Understanding path difference as the fundamental condition is the key that unlocks all subsequent wave optics. Young's double-slit, single-slit diffraction, thin-film interference, diffraction gratings, and standing waves all reduce to the same two questions: what is the path difference, and is it a whole-wavelength or half-wavelength multiple? Master those two conditions here, and every subsequent interference phenomenon is a variation on the same theme.
