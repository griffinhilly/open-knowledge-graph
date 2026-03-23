---
id: vibrating-string-normal-modes
title: Resonance in Strings and Normal Modes
domain: physics
course: waves-and-optics
prerequisites:
- id: standing-waves
  type: hard
- id: wavelength-frequency-speed-relation
  type: hard
builds-toward:
- fundamental-frequency-and-overtones
tags:
- resonance
- strings
- harmonics
stage: advanced
status: validated
---

# Resonance in Strings and Normal Modes

## Core Idea
A string fixed at both ends resonates at frequencies where standing waves fit exactly: f_n = nv/(2L) for n = 1, 2, 3,... (n = 1 is the fundamental, higher n are harmonics). Wave speed v = √(T/μ) depends on tension T and mass per unit length μ. Plucking excites multiple harmonics simultaneously, determining the string's timbre.

## Questions

```yaml
- question: "A guitarist presses a string against the 12th fret, exactly halving the string's effective length while tension and mass per unit length remain unchanged. What happens to the fundamental frequency?"
  type: multiple-choice
  options:
    - "It doubles — halving L means f₁ = v/(2L) doubles, raising pitch by one octave"
    - "It stays the same — the physical properties of the string (tension, mass) haven't changed"
    - "It halves — the shorter string has less distance to vibrate so it is slower"
    - "It increases by a factor of √2 — because frequency scales as the square root of length"
  answer: 0
  explanation: "Wave speed v = √(T/μ) depends only on tension and mass per unit length, both unchanged. The fundamental frequency f₁ = v/(2L). Halving L while keeping v fixed doubles f₁. This is a one-octave increase — exactly the octave, because the second harmonic of the open string (f₂ = 2f₁) equals the fundamental of the half-length string. This is why the 12th fret is exactly at the midpoint of the string, and it is why every fret has a precise mathematical location based on the twelfth root of 2."

- question: "A violinist tightens a string (increases tension T) while its length and mass per unit length remain unchanged. Which statement correctly describes the effect on the string's resonant frequencies?"
  type: multiple-choice
  options:
    - "Only the fundamental frequency increases; higher harmonics remain unchanged because they depend only on string length"
    - "All harmonic frequencies f_n = nv/(2L) increase proportionally, because v = √(T/μ) increases and all harmonics scale with wave speed"
    - "Wave speed decreases with higher tension because the string resists deformation more strongly"
    - "Timbre changes but pitch stays the same — tension affects only which harmonics are amplified, not their frequencies"
  answer: 1
  explanation: "All normal mode frequencies are f_n = nv/(2L). Since n, L are fixed, all frequencies scale directly with v = √(T/μ). Increasing T increases v, which proportionally increases every harmonic frequency. The fundamental and all overtones rise together, maintaining their integer-multiple ratios (the harmonic series is preserved). Tuning a string by tightening it raises the pitch of all its harmonics simultaneously — the string sounds higher but retains its tonal character. Option C is incorrect: higher tension increases restoring force, which increases wave speed, not decreases it."

- question: "When a guitar string is plucked, multiple normal modes are excited simultaneously, and the relative amplitudes of those harmonics — not just the fundamental — determine the timbre of the resulting sound."
  type: true-false
  answer: true
  explanation: "Plucking at a particular point on the string excites a superposition of normal modes. The fundamental determines the perceived pitch, but the relative amplitudes of the harmonics shape the tonal quality (timbre). A violin and a guitar playing the same pitch differ primarily in which harmonics are emphasized. Plucking near the bridge excites more high harmonics (brighter, harsher sound); plucking near the midpoint suppresses the second harmonic and above (warmer sound). The Fourier analysis of the initial displacement determines the harmonic content — a core reason why Fourier decomposition is so musically relevant."

- question: "A string fixed at both ends can sustain standing waves at wavelengths λₙ = L/n, where L is the string length and n = 1, 2, 3, ..., because each wavelength fits an integer number of full waves into the string."
  type: true-false
  answer: false
  explanation: "The correct condition is λₙ = 2L/n, not L/n. The fixed endpoints must be nodes (zero displacement), and the constraint is that an integer number of *half-wavelengths* must fit within L: L = nλₙ/2, giving λₙ = 2L/n. For the fundamental (n = 1), the half-wavelength equals L, so the full wavelength λ₁ = 2L is *twice* the string length. The string contains exactly half a wave at the fundamental. Stating λₙ = L/n would mean fitting full wavelengths — this would give the correct positions for nodes but would require nodes at places other than the endpoints, violating the boundary conditions for n = 1."

- question: "Explain why a string fixed at both ends can only sustain certain discrete frequencies rather than vibrating at any frequency."
  type: short-answer
  answer: "The fixed endpoints impose boundary conditions: displacement must be zero at both ends at all times (these points cannot move). A standing wave can persist only if both endpoints are nodes. This geometric constraint limits which wavelengths fit: only wavelengths λₙ = 2L/n (for integer n) place nodes at both x = 0 and x = L. All other wavelengths produce a displacement at one or both endpoints, which cannot persist — the driving and reflected waves destructively interfere and cancel. Since frequency is f = v/λ and wave speed v is fixed by the string's tension and mass, each allowed wavelength corresponds to exactly one frequency f_n = nv/(2L). The discreteness is a consequence of the boundary conditions, not of any inherent property of waves."
  explanation: "This is a physical realization of an eigenvalue problem: the boundary conditions select a discrete spectrum of allowed modes from a continuous infinity of possible waves. The same mathematics describes quantum particle in a box (infinite square well), modes of electromagnetic cavities, and acoustic resonances in organ pipes — any wave equation on a bounded domain with fixed-endpoint conditions produces a discrete spectrum of normal modes."
```

## Explainer

You've studied standing waves: two identical waves traveling in opposite directions interfere to create a pattern of **nodes** (points of zero displacement) and **antinodes** (points of maximum displacement) that appears stationary. A string fixed at both ends is a perfect physical realization of this — the fixed endpoints are forced to be nodes. The physics then constrains which standing waves are geometrically possible.

The constraint is simple: only wavelengths that fit an integer number of half-wavelengths within the string's length L are allowed. The longest possible wave — one loop with one antinode — has λ₁ = 2L. The next pattern has two loops: λ₂ = L. Then three loops: λ₃ = 2L/3. In general, λₙ = 2L/n. These are the only patterns that produce nodes at both fixed endpoints; all others cancel destructively and cannot persist. They are the **normal modes** of the string.

Now apply the wave relation v = fλ. The wave speed v = √(T/μ) depends on the physical properties of the string — tension T and mass per unit length μ — and is fixed for a given string. The allowed frequencies are f_n = v/λₙ = nv/(2L). The lowest, f₁ = v/(2L), is the **fundamental**. Higher harmonics are exact integer multiples: f₂ = 2f₁, f₃ = 3f₁, and so on. This integer relationship is what makes a vibrating string sound musical — the harmonics align into a tonal pattern the ear interprets as pitch.

When you pluck a guitar string, you excite many harmonics simultaneously. The relative amplitudes of those harmonics determine the **timbre** — the tonal quality that makes a violin sound different from a guitar even at the same pitch. Tuning uses both control variables: tightening the string (increasing T) raises v and therefore raises all f_n proportionally; pressing the string against a fret shortens the effective length L, also raising frequency. A guitarist pressing the 12th fret halves L, doubling all frequencies — raising the pitch by exactly one octave, which is the f₁ → 2f₁ interval.
