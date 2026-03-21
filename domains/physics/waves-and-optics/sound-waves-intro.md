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
stage: formal-systems
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

## Questions

```yaml
- question: "Two tuning forks are struck simultaneously — one at 440 Hz and one at 880 Hz — from 10 meters away. Assuming the same air temperature, which reaches your ears first?"
  type: multiple-choice
  options:
    - "The 880 Hz fork, because higher frequency means more energy and faster propagation"
    - "Both arrive simultaneously, because sound speed depends on the medium, not on frequency"
    - "The 440 Hz fork, because lower frequency waves have longer wavelengths and travel faster"
    - "The 880 Hz fork, because it completes more wave cycles per second"
  answer: 1
  explanation: "Sound speed in a given medium at a given temperature is a fixed property of the medium — it does not depend on frequency or amplitude. Both forks travel at 343 m/s in the same air and arrive simultaneously. Option A represents the common misconception that 'higher frequency = higher speed.' In fact, higher frequency simply means shorter wavelength (since v = fλ and v is fixed), not faster travel."

- question: "A sound wave passes from air into water. Which of the following correctly describes what changes and what stays the same?"
  type: multiple-choice
  options:
    - "Frequency increases because water molecules vibrate faster"
    - "Speed increases and wavelength changes, but frequency remains set by the source"
    - "Amplitude increases because water is denser and transfers energy more efficiently"
    - "Frequency and speed both increase proportionally, keeping wavelength constant"
  answer: 1
  explanation: "When a wave crosses into a new medium, the source still determines how many compressions per second are emitted — frequency is fixed by the source, not the medium. Speed changes (water ~1480 m/s vs. air ~343 m/s) and, since v = fλ, wavelength changes proportionally. This is a direct application of the principle that wave speed is a medium property."

- question: "A louder sound (greater amplitude) travels faster through air than a quieter sound of the same frequency."
  type: true-false
  answer: false
  explanation: "Amplitude and speed are independent properties of a sound wave. Amplitude determines loudness (the size of pressure fluctuations), but wave speed is determined entirely by the medium's properties — temperature, density, and elastic modulus. A thunderclap and a whisper at the same temperature travel at exactly the same speed. Confusing amplitude with speed is analogous to confusing how hard you swing with how fast the ripples spread."

- question: "Sound waves cannot travel through a vacuum because they require a material medium to propagate their alternating compressions and rarefactions."
  type: true-false
  answer: true
  explanation: "Sound is a mechanical, longitudinal wave — it propagates by particles pushing their neighbors through collisions. Without a medium (no molecules to compress and rarefy), there is nothing to transmit the disturbance. This is why the classic science-fiction trope of loud space explosions is physically wrong: space is (approximately) a vacuum, so no sound can propagate. The bell-jar demonstration — evacuating the jar silences a ringing bell inside — is the canonical experimental proof."

- question: "Why does sound travel faster in steel (~5000 m/s) than in air (~343 m/s), even when produced by the same source at the same frequency?"
  type: short-answer
  answer: "Sound speed depends on the medium's elastic properties and density, not on the source. Steel has much stronger intermolecular bonds than air, so disturbances are transmitted between particles far more quickly. The restoring force in steel is enormous compared to the compressibility of air, enabling the compression-rarefaction cycle to propagate at much higher speed. The source frequency is unchanged — only the speed (and thus wavelength) differs."
  explanation: "The general formula v = √(elastic modulus / density) captures this: steel has a far higher bulk modulus (resistance to compression) relative to its density than air does. This is why dense materials with strong bonds (metals, glass, water) all conduct sound faster than gases. The key insight is that speed is a medium property, entirely separate from the frequency or amplitude that the source determines."
```

## Explainer

From transverse waves, you know that waves carry energy through a medium by having particles oscillate around equilibrium positions. Sound waves are **longitudinal waves** — the particles oscillate back and forth in the same direction the wave is traveling, rather than perpendicular to it. Imagine a row of dominoes: pushing the first creates a pulse that travels down the line as each domino pushes the next. Sound in air works similarly: a vibrating speaker cone pushes adjacent molecules together (creating a **compression**), and when it pulls back, it leaves behind a region of lower density (a **rarefaction**). This alternating compression-rarefaction pattern propagates outward at the speed of sound.

The **speed of sound** depends entirely on the medium, not on the frequency or amplitude of the wave. In air at 20°C it is approximately 343 m/s — a number worth memorizing. The formula v ≈ 331 + 0.6T shows that warmer air has faster-moving molecules that transmit disturbances more quickly, raising the speed. In denser materials with stronger intermolecular forces — water (~1480 m/s) or steel (~5000 m/s) — sound travels far faster. The key lesson from wave-speed-medium applies directly: the medium's properties set the speed, not the source.

**Frequency** and **amplitude** are the two independent variables that describe a sound. Frequency — how many compressions pass a point per second — determines **pitch**: 440 Hz is the musical note A. Amplitude — how large the pressure excursions are — determines **loudness**. These are completely independent: you can have a loud high-pitched sound (a piccolo at full volume) or a quiet low-pitched sound (a distant bass note). This independence is why audio engineers can boost bass frequencies without making everything louder.

One implication of sound being a mechanical, longitudinal wave is that it **cannot travel through a vacuum** — there are no molecules to compress and rarefy. This is why the classic film trope of deafening space explosions is physically wrong. Sound also takes time to travel: the familiar three-second delay between a lightning flash and thunder tells you the storm is roughly one kilometer away (343 m/s × 3 s ≈ 1 km). Appreciating this finite propagation speed becomes crucial when you encounter the Doppler effect.
