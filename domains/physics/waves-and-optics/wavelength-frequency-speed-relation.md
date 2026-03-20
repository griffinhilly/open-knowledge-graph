---
id: wavelength-frequency-speed-relation
title: Wavelength, Frequency, and Wave Speed
domain: physics
course: waves-and-optics
prerequisites:
- id: harmonic-wave-time-dependence
  type: hard
builds-toward:
- acoustic-wave-speed-properties
- diffraction-resolution-angular-separation
tags:
- waves
- kinematics
stage: advanced
status: draft
---

# Wavelength, Frequency, and Wave Speed

## Core Idea
The fundamental relation v = fλ connects wave speed (v), frequency (f), and wavelength (λ). Frequency is determined by the source, wavelength by the medium's properties (via wave speed), and the product always gives the propagation speed. This simple relation allows prediction of how waves behave when they change media.

## Explainer

From harmonic wave time-dependence, you know that a wave oscillates in time at frequency f: the displacement at any fixed point in space completes f full cycles per second, with period T = 1/f. The wave also has a spatial pattern — the displacement varies with position, forming crests and troughs. The distance between two adjacent identical points (two crests, two troughs, or two zero-crossings moving in the same direction) is the **wavelength** λ. The equation v = fλ connects the wave's spatial structure (λ) to its temporal structure (f) through the speed at which the pattern travels (v).

The physical derivation is worth carrying out mentally once. In one period T, the source completes one full oscillation and sends exactly one wavelength of disturbance down the medium. That wavefront advances a distance of one wavelength in a time T. Speed is distance divided by time, so v = λ/T = λ·f. The equation is unavoidable once you accept those two facts. There's no free parameter to choose.

The equation's most important consequence involves what happens when a wave crosses from one medium into another. The **frequency is set by the source** and does not change at the boundary — it would be physically incoherent for the medium to somehow alter the rate at which the source oscillates. What changes is the wave speed, which depends on the new medium's properties (density, elasticity for mechanical waves; permittivity, permeability for electromagnetic waves). Since v = fλ and f is fixed, a slower medium forces a shorter wavelength; a faster medium forces a longer wavelength. When light enters glass (slower medium), its frequency stays fixed, its speed drops, and its wavelength shortens. The direction change you call **refraction** is a consequence of this wavelength change at the boundary.

In practice, v = fλ solves a third of unknown given the other two. For sound in air at 20 °C, v ≈ 343 m/s; a 440 Hz musical A has wavelength 343/440 ≈ 0.78 m. For visible light in vacuum, v = 3 × 10⁸ m/s; green light at 550 nm has frequency f = 3 × 10⁸ / 550 × 10⁻⁹ ≈ 5.5 × 10¹⁴ Hz. When a problem tells you a wave passes from air into water where sound travels at 1,480 m/s, the frequency stays at 440 Hz and the wavelength becomes 1480/440 ≈ 3.4 m — more than four times longer. The same number of cycles per second now spans much more distance per cycle.
