---
id: doppler-shift-observer-motion
title: Doppler Effect for Moving Observers
domain: physics
course: waves-and-optics
prerequisites:
- id: acoustic-wave-speed-properties
  type: hard
- id: doppler-shift-source-motion
  type: soft
tags:
- doppler
- sound
stage: advanced
status: validated
---

# Doppler Effect for Moving Observers

## Core Idea
When an observer moves toward a source at speed v_o, the observed frequency increases: f' = f(v_wave + v_o)/v_wave. Moving away decreases the frequency. The formula differs from source motion because the observer is moving relative to the wavefront spacing, not the wave itself. Combined source and observer motion requires adding both effects.

## Questions

```yaml
- question: "A source emits sound at 440 Hz while stationary. In scenario A, the source moves toward a stationary observer at 20 m/s. In scenario B, the source is stationary and the observer moves toward it at 20 m/s. Do both scenarios produce the same observed frequency?"
  type: multiple-choice
  options:
    - "Yes — by symmetry, the observed shift depends only on the closing speed, not which party is moving"
    - "No — equal source and observer speeds produce different observed frequencies because the mechanisms differ"
    - "Yes — the Doppler formula f' = f(v + 20)/v applies equally to both cases"
    - "No — observer motion always produces a larger frequency shift than source motion at the same speed"
  answer: 1
  explanation: "Source motion compresses the wavefronts themselves, changing the wavelength: f' = f · v_wave / (v_wave − v_s). Observer motion changes how fast the observer sweeps through fixed-wavelength wavefronts: f' = f · (v_wave + v_o) / v_wave. At 20 m/s approach and v_wave = 343 m/s, source motion gives f' = 440 × 343/323 ≈ 467 Hz; observer motion gives f' = 440 × 363/343 ≈ 466 Hz — close but not identical, and diverging as speeds increase. Option A is the classic misconception: the scenarios look symmetric but are mechanistically distinct."

- question: "What physically changes when an observer moves toward a stationary sound source?"
  type: multiple-choice
  options:
    - "The wavelength of the sound decreases as the observer approaches the source"
    - "The speed of sound through the air increases in the direction of observer motion"
    - "The observer's velocity relative to the wavefronts increases, so more pressure crests are encountered per second"
    - "The source emits higher-frequency waves in response to the approaching observer"
  answer: 2
  explanation: "The wavefronts are equally spaced — the source hasn't moved, so wavelength is unchanged. The observer's effective speed relative to the wavefronts is v_wave + v_o, meaning they sweep through more crests per second, increasing observed frequency. The speed of sound in air is determined by the medium, not relative motion (option B). Source motion (not observer motion) changes wavelength (option A). The source is unaware of the observer (option D)."

- question: "When an observer moves away from a stationary sound source, the speed of sound through the air decreases."
  type: true-false
  answer: false
  explanation: "The speed of sound is a property of the medium — temperature and density of air — and is unaffected by the motion of either source or observer. What changes is the observer's speed *relative to the wavefronts*: v_wave − v_o. This reduces the rate of crest encounters, lowering observed frequency, but the wave itself still travels through air at the same v_wave."

- question: "For equal closing speeds, a moving observer produces a different observed frequency than a moving source."
  type: true-false
  answer: true
  explanation: "The formulas are structurally different: source motion f' = f · v_wave/(v_wave − v_s); observer motion f' = f · (v_wave + v_o)/v_wave. At the same speed these yield slightly different values because source motion physically alters the spacing of wavefronts (wavelength), while observer motion leaves the wavelength intact and only changes the encounter rate. The asymmetry grows with speed."

- question: "Why does the Doppler formula for a moving observer differ structurally from the formula for a moving source, even though both change the observed frequency?"
  type: short-answer
  answer: "Because the physical mechanisms are different. Source motion compresses or stretches the spacing between wavefronts — changing the wavelength itself — before the wave even reaches the observer. Observer motion leaves the wavelength unchanged; it only alters the rate at which the observer sweeps through fixed wavefronts. These distinct mechanisms produce formulas with different mathematical structure: source motion appears in the denominator (affecting wavelength), observer motion appears in the numerator (affecting encounter rate)."
  explanation: "The key is to ask: what is actually different about the wave? For source motion, the wave pattern itself is distorted. For observer motion, the wave is identical to the stationary case — only the observer's relationship to it changes. Both produce a frequency shift, but tracing the physics to its origin reveals why the formulas look similar but are not interchangeable."
```

## Explainer

From your study of acoustic wave speed, you know that a sound wave travels through air at a fixed speed v_wave set by the medium — roughly 343 m/s in air at room temperature. The wave consists of pressure crests (compressions) spaced one wavelength apart, traveling outward from the source. When the source and observer are both stationary, the observer encounters those crests at a steady rate equal to the source frequency. The Doppler effect for a moving observer changes that encounter rate — not by altering the wave itself, but by changing how fast the observer sweeps through the crests.

Think of the crests as equally spaced mile markers on a highway. If you stand still, cars (crests) pass you at the speed the road allows. If you run toward the oncoming traffic, you pass more mile markers per second — your effective speed relative to the crests is v_wave + v_o. If you run away, fewer crests reach you per second, giving relative speed v_wave − v_o. The **observed frequency** is just how many crests you pass per second: f' = (relative speed) / (wavelength) = (v_wave ± v_o) / λ. Since λ = v_wave / f, this simplifies to f' = f(v_wave ± v_o) / v_wave — the standard formula.

The important conceptual distinction is between observer motion and source motion. When the source moves, it compresses the wavefronts ahead of it and stretches them behind, changing the wavelength itself. When the observer moves, the wavelength is unchanged — the observer simply sweeps through crests at a different rate. Both scenarios change the observed frequency, but through different physical mechanisms, so their formulas have different structure. For source motion: f' = f · v_wave / (v_wave ∓ v_s). For observer motion: f' = f · (v_wave ± v_o) / v_wave. The formulas look similar but are not symmetric — substituting equal speeds for source versus observer gives slightly different observed frequencies.

When both source and observer move simultaneously, combine both effects: f' = f · (v_wave ± v_o) / (v_wave ∓ v_s). The sign rule is always the same: use the upper sign when motion closes the gap (observer toward source, or source toward observer) and the lower sign when motion opens it. This additive structure makes physical sense — both effects independently shift how many crests per second reach the observer, so the total shift is the product of the two factors.
