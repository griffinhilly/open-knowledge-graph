---
id: doppler-shift-observer-motion
title: Doppler Effect for Moving Observers
domain: physics
course: waves-and-optics
prerequisites:
- id: acoustic-wave-speed-properties
  type: hard
tags:
- doppler
- sound
stage: advanced
status: draft
---

# Doppler Effect for Moving Observers

## Core Idea
When an observer moves toward a source at speed v_o, the observed frequency increases: f' = f(v_wave + v_o)/v_wave. Moving away decreases the frequency. The formula differs from source motion because the observer is moving relative to the wavefront spacing, not the wave itself. Combined source and observer motion requires adding both effects.

## Explainer

From your study of acoustic wave speed, you know that a sound wave travels through air at a fixed speed v_wave set by the medium — roughly 343 m/s in air at room temperature. The wave consists of pressure crests (compressions) spaced one wavelength apart, traveling outward from the source. When the source and observer are both stationary, the observer encounters those crests at a steady rate equal to the source frequency. The Doppler effect for a moving observer changes that encounter rate — not by altering the wave itself, but by changing how fast the observer sweeps through the crests.

Think of the crests as equally spaced mile markers on a highway. If you stand still, cars (crests) pass you at the speed the road allows. If you run toward the oncoming traffic, you pass more mile markers per second — your effective speed relative to the crests is v_wave + v_o. If you run away, fewer crests reach you per second, giving relative speed v_wave − v_o. The **observed frequency** is just how many crests you pass per second: f' = (relative speed) / (wavelength) = (v_wave ± v_o) / λ. Since λ = v_wave / f, this simplifies to f' = f(v_wave ± v_o) / v_wave — the standard formula.

The important conceptual distinction is between observer motion and source motion. When the source moves, it compresses the wavefronts ahead of it and stretches them behind, changing the wavelength itself. When the observer moves, the wavelength is unchanged — the observer simply sweeps through crests at a different rate. Both scenarios change the observed frequency, but through different physical mechanisms, so their formulas have different structure. For source motion: f' = f · v_wave / (v_wave ∓ v_s). For observer motion: f' = f · (v_wave ± v_o) / v_wave. The formulas look similar but are not symmetric — substituting equal speeds for source versus observer gives slightly different observed frequencies.

When both source and observer move simultaneously, combine both effects: f' = f · (v_wave ± v_o) / (v_wave ∓ v_s). The sign rule is always the same: use the upper sign when motion closes the gap (observer toward source, or source toward observer) and the lower sign when motion opens it. This additive structure makes physical sense — both effects independently shift how many crests per second reach the observer, so the total shift is the product of the two factors.
