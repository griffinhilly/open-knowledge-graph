---
id: wave-speed-medium
title: Wave Speed and the Medium
domain: physics
course: waves-and-optics
prerequisites:
- id: wave-properties-intro
  type: hard
- id: wave-speed-equation
  type: soft
builds-toward:
- standing-waves
- doppler-effect
- refraction-intro
- snells-law
tags:
- wave speed
- medium
- tension
- elasticity
- density
stage: formal-systems
status: validated
---

# Wave Speed and the Medium

## Core Idea
Wave speed is determined by the properties of the medium, not by the frequency or amplitude of the wave. For a string, v = √(T/μ) where T is tension and μ is linear mass density. For sound in a gas, speed increases with temperature. When a wave crosses from one medium into another, frequency is preserved but wavelength and speed both change according to v = fλ.

## How It's Best Learned
Perform experiments varying string tension and mass density, measuring how wave speed changes. Then solve problems where a wave crosses a boundary and students must find the new wavelength given the new speed.

## Common Misconceptions
- Many students believe higher frequency means faster wave in the same medium — frequency changes only when the source changes, not the medium.
- Speed changing at a boundary is counterintuitive; emphasize that frequency is locked by the source, so λ must adjust.

## Explainer

From your study of wave properties, you know that a wave is characterized by frequency, wavelength, amplitude, and speed, all linked by v = fλ. But where does the speed come from? The fundamental insight is that wave speed belongs to the **medium**, not to the wave itself. The wave is a disturbance propagating through a material; how fast that disturbance travels is set by the material's physical properties. You, as the source, control the frequency — but you have no direct control over how fast the wave moves once it enters the medium.

The formula v = √(T/μ) for a transverse wave on a string captures this physically. **Tension** T is the restoring force: it pulls a displaced segment of string back toward its equilibrium position. Greater tension means stronger restoring force, so the medium snaps back faster, and the wave propagates more quickly. **Linear mass density** μ (mass per unit length) is inertia: a heavier string resists being set into motion. The wave must accelerate each segment of string as it passes through; more mass means more sluggish response, so the wave travels more slowly. Speed is the outcome of these two competing factors — the balance between how strongly the medium is pulled back and how reluctantly it moves. Sound waves in air follow an analogous competition between elasticity (the medium's springiness, related to pressure) and density; warmer air is less dense, which is why the speed of sound increases with temperature.

The most important consequence of medium-determined speed is what happens at a **boundary** where one medium meets another. When a wave crosses from medium 1 (wave speed v₁) into medium 2 (wave speed v₂), frequency cannot change. Frequency is the rate at which wave cycles arrive, which is set by the source that launched the wave — nothing at the boundary can change how often cycles are produced. But if frequency is fixed and speed changes, then wavelength must change to preserve v = fλ: the new wavelength is λ₂ = v₂/f = λ₂ = λ₁ · (v₂/v₁). A wave entering a slower medium shortens its wavelength; a wave entering a faster medium lengthens it. This wavelength adjustment at boundaries — happening at every cycle, simultaneously across the entire wavefront — causes the wave direction to bend when the wave hits the boundary at an angle. That bending is refraction, which you will study in optics, and it follows directly from the same principle: medium controls speed, source controls frequency, and wavelength adjusts accordingly.

## Questions

```yaml
- question: "A string has tension 100 N and linear mass density 0.04 kg/m. What is the wave speed on this string?"
  type: multiple-choice
  options:
    - "25 m/s"
    - "50 m/s"
    - "2500 m/s"
    - "4 m/s"
  answer: 1
  explanation: "v = √(T/μ) = √(100/0.04) = √2500 = 50 m/s. Note: doubling tension would multiply speed by √2 (not double it), because speed depends on the square root of tension."

- question: "A wave travels from a rope with wave speed 40 m/s into a second rope where wave speed is 20 m/s. The wave frequency is 10 Hz. What is the wavelength in each rope?"
  type: short-answer
  answer: "In rope 1: λ₁ = v₁/f = 40/10 = 4 m. In rope 2: λ₂ = v₂/f = 20/10 = 2 m. Frequency is unchanged (set by the source); wavelength halves because speed halves."
  explanation: "At a boundary, frequency is conserved and wavelength changes in proportion to speed. This is the key relationship v = fλ applied at the boundary: same f, different v, therefore different λ."

- question: "A student increases the frequency of a wave on a string by bowing it faster. Does the wave speed on the string change? Does the wavelength change?"
  type: short-answer
  answer: "Wave speed does not change — it is determined by the string's tension and linear mass density, which the student hasn't altered. Wavelength does change: since v = fλ and v is fixed, increasing f means λ must decrease (λ = v/f)."
  explanation: "This tests the core principle: speed belongs to the medium, frequency belongs to the source. The student controls frequency; the string controls speed. Wavelength is the dependent variable that adjusts to keep v = fλ consistent."
```
