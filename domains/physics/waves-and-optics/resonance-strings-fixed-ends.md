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
stage: formal-systems
status: draft
---

# Resonance in Strings with Fixed Ends

## Core Idea
A string fixed at both ends resonates when its length equals an integer number of half-wavelengths: L = nλ/2. This produces standing waves with fixed nodes at the ends and resonant frequencies fₙ = nv/(2L), where n = 1,2,3... defines the harmonic number.

## Explainer

From your study of standing waves, you know that two waves of equal amplitude and frequency traveling in opposite directions combine to produce a pattern that oscillates in place — fixed nodes where displacement is always zero, and antinodes where displacement swings between maximum positive and negative. A string fixed at both ends is the physical system that forces this pattern to occur: the boundary conditions at the two fixed endpoints require nodes there, and the resonant frequencies are exactly those for which the geometry works out.

Think about what "fixed end" means physically. At a fixed endpoint, the string cannot move — the wall or bridge exerts whatever force is needed to keep displacement zero. This is a hard constraint: the standing wave must have a **node at every fixed end**. So the question becomes: for a given wave speed v on the string, which wavelengths λ produce a pattern with nodes at both ends when the string has length L? The answer is all wavelengths where exactly an integer number of half-wavelengths fits: L = nλ/2, so λₙ = 2L/n. Each allowed wavelength corresponds to a **harmonic**: n = 1 is the **fundamental** (one half-wavelength spans the string, one antinode in the middle), n = 2 is the **second harmonic** (two half-wavelengths, two antinodes), n = 3 the third, and so on. Any other wavelength would require a non-zero displacement at the fixed end, violating the boundary condition — so those frequencies simply cannot sustain a standing wave.

Converting wavelength to frequency using f = v/λ gives fₙ = nv/(2L). The fundamental frequency f₁ = v/(2L) sets the spacing: every harmonic is an integer multiple of f₁. This integer relationship — harmonics at f₁, 2f₁, 3f₁, ... — is what makes stringed instruments sound musical. The **wave speed v** on a string depends on tension T and linear mass density μ: v = √(T/μ). Tightening a guitar string (increasing T) raises v and therefore raises all harmonics equally. Using a lighter string (smaller μ) also increases v. Pressing a string down at a fret shortens L, which increases all fₙ since they depend on 1/L. Every time a guitarist tunes or plays a note, they are manipulating this formula.

In a real plucked string, the fundamental and all harmonics are excited simultaneously. The relative strength of each harmonic — called the **harmonic spectrum** or **timbre** — determines the instrument's characteristic sound. A guitar plucked near the bridge excites high harmonics strongly (bright, cutting sound); plucked near the middle, the even harmonics are suppressed (the pluck point is an antinode of odd harmonics and a node of even ones), producing a rounder tone. This is the physics behind the difference between guitar playing positions, and why bowing versus plucking a violin string produces different timbres. The resonance condition L = nλ/2 is simple; the richness comes from how many harmonics are excited and in what proportions.
