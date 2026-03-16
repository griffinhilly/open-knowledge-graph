---
id: sound-waves-intro
title: Sound Waves
domain: physics
course: waves-and-optics
prerequisites:
- id: transverse-and-longitudinal-waves
  type: hard
- id: wave-speed-medium
  type: soft
builds-toward:
- sound-intensity-and-decibels
- doppler-effect
tags:
- sound
- pressure wave
- compression
- rarefaction
- speed of sound
stage: concrete-operations
status: validated
---

# Sound Waves

## Core Idea
Sound is a longitudinal mechanical wave — alternating compressions and rarefactions of a medium propagated by collisions between particles. It requires a material medium and cannot travel through a vacuum. The speed of sound in air at 20°C is approximately 343 m/s and increases with temperature (v ≈ 331 + 0.6T m/s). The frequency of a sound wave determines its pitch; amplitude determines loudness.

## How It's Best Learned
Ring a bell inside a bell jar and evacuate the jar to demonstrate that sound needs a medium. Measure the speed of sound by timing an echo from a distant wall.

## Common Misconceptions
- Sound does not travel in a vacuum — the common sci-fi trope of loud space explosions is physically wrong.
- Higher frequency (pitch) does not mean faster sound in the same medium; speed is medium-dependent, not frequency-dependent.

## Explainer

From transverse waves, you know that waves carry energy through a medium by having particles oscillate around equilibrium positions. Sound waves are **longitudinal waves** — the particles oscillate back and forth in the same direction the wave is traveling, rather than perpendicular to it. Imagine a row of dominoes: pushing the first creates a pulse that travels down the line as each domino pushes the next. Sound in air works similarly: a vibrating speaker cone pushes adjacent molecules together (creating a **compression**), and when it pulls back, it leaves behind a region of lower density (a **rarefaction**). This alternating compression-rarefaction pattern propagates outward at the speed of sound.

The **speed of sound** depends entirely on the medium, not on the frequency or amplitude of the wave. In air at 20°C it is approximately 343 m/s — a number worth memorizing. The formula v ≈ 331 + 0.6T shows that warmer air has faster-moving molecules that transmit disturbances more quickly, raising the speed. In denser materials with stronger intermolecular forces — water (~1480 m/s) or steel (~5000 m/s) — sound travels far faster. The key lesson from wave-speed-medium applies directly: the medium's properties set the speed, not the source.

**Frequency** and **amplitude** are the two independent variables that describe a sound. Frequency — how many compressions pass a point per second — determines **pitch**: 440 Hz is the musical note A. Amplitude — how large the pressure excursions are — determines **loudness**. These are completely independent: you can have a loud high-pitched sound (a piccolo at full volume) or a quiet low-pitched sound (a distant bass note). This independence is why audio engineers can boost bass frequencies without making everything louder.

One implication of sound being a mechanical, longitudinal wave is that it **cannot travel through a vacuum** — there are no molecules to compress and rarefy. This is why the classic film trope of deafening space explosions is physically wrong. Sound also takes time to travel: the familiar three-second delay between a lightning flash and thunder tells you the storm is roughly one kilometer away (343 m/s × 3 s ≈ 1 km). Appreciating this finite propagation speed becomes crucial when you encounter the Doppler effect.
