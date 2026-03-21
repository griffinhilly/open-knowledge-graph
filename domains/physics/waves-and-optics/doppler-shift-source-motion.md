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

## Questions

```yaml
- question: "An ambulance moves toward you at 30 m/s emitting sound at 500 Hz (speed of sound = 340 m/s). A classmate says: 'The sound waves reach you faster because the source is moving toward you, which raises the frequency.' What is wrong with this explanation?"
  type: multiple-choice
  options:
    - "Nothing — the wave speed increases when the source moves toward the observer"
    - "The frequency is actually lower when the source approaches, not higher"
    - "Wave speed in air is fixed by the medium and unchanged by source motion — the higher frequency arises from compressed wavelength, not faster waves"
    - "The classmate is correct for sound but wrong for light, where the frequency shift involves time dilation instead"
  answer: 2
  explanation: "Wave speed in a medium is determined by the medium's properties (density and elasticity for sound) — not by source motion. What changes when the source approaches is the wavelength: each successive wavefront is emitted closer to the previous one, packing crests together. More crests arrive per second not because they travel faster, but because they are spaced more closely. The correct formula gives f' = 500 × 340/310 ≈ 548 Hz, but the mechanism is wavelength compression, never speed increase. Option A states the specific misconception being addressed here."

- question: "If a source moves away from a stationary observer at speed v_s, the denominator in the Doppler formula becomes (v_wave + v_s), giving a lower frequency. Which explanation correctly identifies why the denominator increases?"
  type: multiple-choice
  options:
    - "The wave speed decreases when the source moves away from the observer"
    - "The source emits wavefronts less frequently when receding"
    - "Each successive wavefront is emitted farther from the previous one, stretching the wavelength behind the source"
    - "The medium becomes less dense behind the source, which slows the waves"
  answer: 2
  explanation: "When the source recedes, it travels v_s·T away from the observer between emitting successive crests (T = 1/f is the emission period). Each new crest is launched v_s·T farther from the previous one, stretching the spacing to λ' = (v_wave + v_s)/f. The crests still propagate at v_wave, but they arrive less frequently: f' = v_wave/λ' = f·v_wave/(v_wave + v_s). The emission rate (option B) does not change — the source vibrates at its own frequency regardless of motion. Options A and D both incorrectly attribute the effect to wave speed changes."

- question: "The Doppler effect for a moving source changes the wavelength of sound as measured in the medium, but does not change the speed at which those waves travel through the medium."
  type: true-false
  answer: true
  explanation: "Wave speed in air (~340 m/s) is set by air's density and bulk modulus — properties of the medium that are unaffected by source motion. What changes is the spatial spacing of wavefronts: ahead of an approaching source the crests bunch together (shorter λ), and behind it they spread apart (longer λ). Both the compressed and stretched wavefronts still travel at the same speed v_wave. The observer measures more or fewer arrivals per second — a frequency shift — entirely because of the changed wavelength, with no change in propagation speed."

- question: "The Doppler formula f' = f·v_wave/(v_wave − v_s) applies equally to a moving source and a moving observer, as long as v_s is interpreted as the relative speed between source and observer."
  type: true-false
  answer: false
  explanation: "This is a common but incorrect shortcut. The formula f' = f·v_wave/(v_wave − v_s) applies specifically to a stationary observer with a moving source. For a moving observer approaching a stationary source, the correct formula is f' = f·(v_wave + v_obs)/v_wave — a different expression, not equivalent by substituting relative speed. The two cases differ physically: a moving source changes the wavelength deposited in the medium, while a moving observer sweeps through a fixed wavelength at a different rate. These mechanisms are distinct, and in classical wave theory 'who is moving' relative to the medium matters."

- question: "Explain the physical mechanism by which a moving source produces a higher observed frequency when approaching, without invoking any change in wave speed."
  type: short-answer
  answer: "The source emits one wavefront per period T = 1/f. When stationary, each successive crest is launched from the same position, so crests are spaced λ = v_wave·T apart. When the source moves toward the observer at speed v_s, it travels a distance v_s·T toward the observer between emitting one crest and the next. Each new crest is therefore launched v_s·T closer to the previous one, compressing the spacing to λ' = (v_wave − v_s)·T = (v_wave − v_s)/f. The crests still propagate at v_wave but arrive at the observer more frequently because they are packed together: f' = v_wave/λ' = f·v_wave/(v_wave − v_s) > f."
  explanation: "The mechanism is entirely geometric: source motion between successive emissions changes where each new crest originates, compressing or stretching wavefront spacing. Wave speed is unchanged; only the spacing — and hence the arrival rate — changes."
```

## Explainer

From acoustic wave speed, you know that sound travels through a medium at a fixed speed v_wave determined by the medium's properties — density and elasticity — not by any motion of the source or observer. When both are stationary, the observer hears exactly the frequency at which the source vibrates. The Doppler effect breaks this symmetry by changing where each successive wavefront is emitted.

Visualize the mechanism concretely. A source emits one crest every T = 1/f seconds. When the source is stationary, each crest is launched from the same location, so the crests are spaced exactly λ = v_wave/f apart in every direction. Now suppose the source moves toward you at speed v_s. In the time T between emitting one crest and the next, the source travels a distance v_s·T toward you. Each new crest is therefore emitted v_s·T closer to the previous one, compressing the spacing in front to λ' = λ − v_s·T = (v_wave − v_s)/f. Since the crests still travel at v_wave, you receive them at frequency f' = v_wave/λ' = f · v_wave/(v_wave − v_s). Because (v_wave − v_s) is smaller than v_wave, f' > f — you hear a higher pitch. When the source moves away, the spacing behind it stretches to (v_wave + v_s)/f, and the observed frequency drops to f · v_wave/(v_wave + v_s).

This is the familiar sound of a passing ambulance: higher pitch on approach, lower pitch as it recedes. The wave speed has not changed at all — what changes is the **wavelength** in the medium ahead of and behind the source. The observer's ear measures a higher rate of crest arrivals from the compressed-wavelength side and a lower rate from the stretched side. Notice that the formula breaks down if v_s ≥ v_wave: the denominator goes to zero or negative, which physically corresponds to the source catching up to or outrunning its own wavefronts — the **sonic boom** regime where the analysis requires different treatment.

This formula assumes the observer is stationary and the source moves. If the observer moves instead, the formula changes because the mechanism differs — a moving observer sweeps through crests at a different rate, rather than the crests themselves being compressed. The asymmetry between moving source and moving observer is a key distinction developed in the follow-on topic. In all cases, keep this principle in mind: wave speed in a medium is a property of the medium, not of any motion; the Doppler effect always works through wavelength changes, not speed changes.
