---
id: doppler-shift-source-motion
title: Doppler Effect for Moving Sources
domain: physics
course: waves-and-optics
prerequisites:
- id: acoustic-wave-speed-properties
  type: hard
builds-toward:
- doppler-shift-observer-motion
tags:
- doppler
- sound
stage: advanced
status: draft
---

# Doppler Effect for Moving Sources

## Core Idea
When a source moves toward an observer at speed v_s, the observed frequency increases: f' = f(v_wave)/(v_wave - v_s). Moving away reverses the sign in the denominator. The wavelength measured in the observer's frame decreases or increases correspondingly. The Doppler formula is derived by considering how the source's motion changes the spacing between wavefronts.

## How It's Best Learned
Derive the formula by considering the distance a moving source travels between emitting successive crests.

## Common Misconceptions
The Doppler effect does not change the wave's speed in its medium—only the observed wavelength and frequency change.

## Explainer

From acoustic wave speed, you know that sound travels through a medium at a fixed speed v_wave determined by the medium's properties — density and elasticity — not by any motion of the source or observer. When both are stationary, the observer hears exactly the frequency at which the source vibrates. The Doppler effect breaks this symmetry by changing where each successive wavefront is emitted.

Visualize the mechanism concretely. A source emits one crest every T = 1/f seconds. When the source is stationary, each crest is launched from the same location, so the crests are spaced exactly λ = v_wave/f apart in every direction. Now suppose the source moves toward you at speed v_s. In the time T between emitting one crest and the next, the source travels a distance v_s·T toward you. Each new crest is therefore emitted v_s·T closer to the previous one, compressing the spacing in front to λ' = λ − v_s·T = (v_wave − v_s)/f. Since the crests still travel at v_wave, you receive them at frequency f' = v_wave/λ' = f · v_wave/(v_wave − v_s). Because (v_wave − v_s) is smaller than v_wave, f' > f — you hear a higher pitch. When the source moves away, the spacing behind it stretches to (v_wave + v_s)/f, and the observed frequency drops to f · v_wave/(v_wave + v_s).

This is the familiar sound of a passing ambulance: higher pitch on approach, lower pitch as it recedes. The wave speed has not changed at all — what changes is the **wavelength** in the medium ahead of and behind the source. The observer's ear measures a higher rate of crest arrivals from the compressed-wavelength side and a lower rate from the stretched side. Notice that the formula breaks down if v_s ≥ v_wave: the denominator goes to zero or negative, which physically corresponds to the source catching up to or outrunning its own wavefronts — the **sonic boom** regime where the analysis requires different treatment.

This formula assumes the observer is stationary and the source moves. If the observer moves instead, the formula changes because the mechanism differs — a moving observer sweeps through crests at a different rate, rather than the crests themselves being compressed. The asymmetry between moving source and moving observer is a key distinction developed in the follow-on topic. In all cases, keep this principle in mind: wave speed in a medium is a property of the medium, not of any motion; the Doppler effect always works through wavelength changes, not speed changes.
