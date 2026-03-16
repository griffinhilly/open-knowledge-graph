---
id: relativistic-doppler-shift
title: Relativistic Doppler Effect
domain: physics
course: modern-physics
prerequisites:
- id: special-relativity-postulates
  type: hard
- id: doppler-effect
  type: hard
tags:
- special-relativity
- waves
- doppler
stage: abstract-reasoning
status: draft
---

# Relativistic Doppler Effect

## Core Idea
The relativistic Doppler formula for light is f' = f√[(1−β)/(1+β)] for motion along the line of sight (β = v/c). Unlike the classical Doppler effect, relativistic shift includes time dilation effects and is symmetric—observers in different frames calculate the shift consistently. Transverse Doppler shift (motion perpendicular to line of sight) arises purely from time dilation.

## Explainer

You already know the classical Doppler effect: a source moving toward you compresses the wavefronts, raising the observed frequency; one moving away stretches them, lowering it. The formula depends on the velocities of both source and medium. But light has no medium, and here special relativity changes the picture fundamentally. Two effects are at play simultaneously — the geometric compression of wavefronts and **time dilation** — and both must be accounted for to get the right answer.

Consider a source moving directly toward you at speed v (β = v/c). In the source's frame, it emits waves at frequency f. But from your frame, the source's clock is time-dilated: it ticks more slowly by a factor γ = 1/√(1−β²). This slowing acts like a lower emission frequency. Simultaneously, because the source is approaching, each successive crest is emitted from a position closer to you, compressing the wavelength. These two effects combine — one tending to lower the frequency, one to raise it — and the net result is f' = f√[(1+β)/(1−β)] for an approaching source, which is always larger than the classical prediction for the same speed.

The formula becomes especially illuminating for recession: f' = f√[(1−β)/(1+β)]. This is the **cosmological redshift** formula in its pure Doppler form. When astronomers observe distant galaxies with spectral lines shifted to longer wavelengths, they're measuring β directly from this formula. Notice the deep symmetry: the formula is the same whether you think of the source as moving away from a stationary observer or the observer moving away from a stationary source. In classical Doppler, these two cases give different answers (because the medium defines a preferred frame). In special relativity they are identical — there is no preferred frame, and the physics depends only on relative velocity.

The most conceptually novel piece is **transverse Doppler shift**: when the source moves perpendicular to your line of sight, the classical formula predicts zero frequency shift (no compression or stretching of wavefronts). But relativistically, there is still a shift — a pure time-dilation redshift of f' = f/γ. The source's clock runs slow, so you receive fewer cycles per second even though it's not moving toward or away from you at the moment of emission. This effect has no classical analogue and was one of the first experimental confirmations of relativistic time dilation, observed using fast-moving atomic clocks and later by precise measurements in particle accelerators.
