---
id: phase-of-oscillation-initial
title: Phase and Phase Relationships Between Waves
domain: physics
course: waves-and-optics
prerequisites:
- id: harmonic-wave-time-dependence
  type: hard
builds-toward:
- path-length-difference-analysis
- interference-two-sources-interference-pattern
tags:
- waves
- phase
stage: advanced
status: draft
---

# Phase and Phase Relationships Between Waves

## Core Idea
The phase of a wave (φ = kx - ωt + φ₀) determines which part of the oscillation cycle is occurring at a given point and time. Two waves are in phase when their crests align, out of phase when crests align with troughs, and at intermediate phase differences in between. Phase relationships determine how waves add constructively or destructively.

## How It's Best Learned
Sketch two sinusoids with different phase constants and observe how shifting one by half a wavelength reverses the sign (180° phase shift).

## Common Misconceptions
Phase difference of 2π radians is NOT different from zero phase difference—they represent the same wave state.

## Explainer

From your study of harmonic wave time dependence, you know that a wave is described by a sinusoidal function: y(x, t) = A sin(kx − ωt + φ₀). The term inside the sine function is called the **phase**: φ = kx − ωt + φ₀. It's a single number, measured in radians, that tells you exactly where in the oscillation cycle a particular point of the medium is at a particular moment. Think of the phase as the "address" within a repeating cycle — just as an angle on a clock face tells you where the hand is, the phase tells you where the wave is in its up-down-up cycle.

The constant φ₀ is the **initial phase** — it shifts the entire wave pattern left or right in space (or equivalently, forward or backward in time). When φ₀ = 0, the wave starts at y = 0 at x = 0, t = 0. When φ₀ = π/2, it starts at a crest. When φ₀ = π, it starts at zero but going in the opposite direction compared to φ₀ = 0. Two waves that are identical in frequency and wavelength but differ in initial phase will be offset from each other — their crests don't line up.

The important quantity for superposition is the **phase difference** Δφ between two waves at the same location. When Δφ = 0 (or any multiple of 2π), the waves are **in phase**: crests align with crests, troughs align with troughs, and the waves reinforce each other — **constructive interference**. When Δφ = π (or any odd multiple of π), the waves are **out of phase** or **in antiphase**: crests align with troughs, they cancel — **destructive interference**. Any other phase difference gives partial interference between these extremes. The key insight is that phase difference is periodic with period 2π: a phase shift of 2π is physically indistinguishable from zero shift, because sine is a periodic function.

Phase differences arise in two distinct ways. A **spatial** phase difference comes from two waves traveling different path lengths to the same point — you'll explore this in detail with path-length difference analysis. A **temporal** phase difference comes from two sources that start oscillating at different times, or from a reflection that inverts the wave (adding a phase shift of exactly π). Understanding which type of phase difference you're dealing with is the first step in analyzing any interference or superposition problem.
