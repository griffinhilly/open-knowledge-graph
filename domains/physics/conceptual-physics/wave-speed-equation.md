---
id: wave-speed-equation
title: "Wave Speed: v = fλ"
domain: physics
course: conceptual-physics
prerequisites:
- id: wave-properties-conceptual
  type: hard
- id: one-step-equations
  type: hard
- id: measuring-speed
  type: soft
builds-toward:
- wave-speed-medium
tags:
- wave-speed
- frequency
- wavelength
stage: abstract-reasoning
status: validated
---
# Wave Speed: v = fλ

## Core Idea
The speed of a wave equals its frequency times its wavelength: v = fλ. This means that for a wave traveling at a fixed speed in a given medium, increasing the frequency automatically decreases the wavelength, and vice versa. Wave speed depends on the medium (air, water, steel) rather than on the wave itself — all sounds in the same air travel at the same speed regardless of pitch.

## How It's Best Learned
Generate waves on a rope or Slinky at different frequencies and measure how the wavelength changes while the wave speed stays roughly constant. Calculate wave speed for sound in air by multiplying a known frequency (like a tuning fork) by the measured wavelength. Compare the speed of sound in different materials.

## Common Misconceptions
- Higher-pitched sounds travel faster. (In the same medium, all sound waves travel at the same speed regardless of frequency. Higher pitch means higher frequency and shorter wavelength, but the same speed.)
- Increasing frequency increases wave speed. (In a given medium, wave speed is constant. Increasing frequency decreases wavelength so that v = fλ stays the same.)
- Wave speed is the same in all materials. (Wave speed depends strongly on the medium. Sound travels about 343 m/s in air but about 1,480 m/s in water and about 5,960 m/s in steel.)
- Wavelength and frequency can be changed independently for the same wave. (For a given wave speed, they are inversely proportional — change one and the other must adjust.)

## Questions

```yaml
- question: "A wave has a frequency of 500 Hz and a wavelength of 0.68 m. What is its speed?"
  type: multiple-choice
  options: ["340 m/s", "735 m/s", "500 m/s", "0.00136 m/s"]
  answer: 0
  explanation: "v = fλ = 500 Hz × 0.68 m = 340 m/s. This is approximately the speed of sound in air."

- question: "In the same medium, a wave with a higher frequency has a shorter wavelength."
  type: true-false
  answer: true
  explanation: "Since v = fλ and v is constant in the same medium, increasing f requires λ to decrease proportionally."

- question: "Sound travels at 340 m/s in air. What is the wavelength of a 170 Hz sound wave?"
  type: short-answer
  answer: "2 meters, because λ = v/f = 340/170 = 2 m."
  explanation: "Rearranging v = fλ gives λ = v/f = 340 m/s ÷ 170 Hz = 2 m."
```

## Explainer
Speed, frequency, and wavelength are the three core measurements of any wave, and they are bound together by one elegant equation: **v = fλ** (speed equals frequency times wavelength). This single relationship lets you calculate any one of the three if you know the other two.

Think about it intuitively. Suppose a wave passes by you, and each cycle takes up 2 meters of space (wavelength = 2 m). If 5 complete cycles pass you every second (frequency = 5 Hz), then the wave must travel 2 × 5 = 10 meters every second. The wave's speed is 10 m/s. That is all the equation says: how much space each cycle occupies, multiplied by how many cycles pass per second, gives you the distance the wave covers per second.

A crucial insight is that **wave speed is determined by the medium**, not by the wave's frequency or wavelength. Sound in room-temperature air always travels at about 343 m/s, whether it is a low bass note or a high-pitched whistle. What changes between bass and treble is the frequency-wavelength pair: a bass note at 100 Hz has a wavelength of about 3.4 m, while a treble note at 10,000 Hz has a wavelength of only 3.4 cm. Both travel at the same speed because v = fλ must always hold.

This has practical consequences. When sound passes from air into water, its speed changes dramatically (from about 343 m/s to about 1,480 m/s). The frequency stays the same — a 440 Hz tone is still 440 Hz underwater. So the wavelength must increase to compensate: λ = v/f = 1,480/440 ≈ 3.4 m, compared to about 0.78 m in air. This change in wavelength when entering a new medium is closely connected to **refraction**, the bending of waves at boundaries.

The wave speed equation applies to all waves: sound, light, water waves, seismic waves, and electromagnetic waves. For light in a vacuum, the speed is always about 300,000,000 m/s. Radio waves have frequencies around millions of hertz and wavelengths of meters, while visible light has frequencies around hundreds of trillions of hertz and wavelengths of a few hundred nanometers. Vastly different numbers, but v = fλ links them all.
