---
id: acoustic-resonance-strings
title: Acoustic Resonance in Strings and Tension
domain: physics
course: waves-and-optics
prerequisites:
- id: standing-waves-formation-mechanism
  type: hard
builds-toward:
- fundamental-frequency-and-overtones
tags:
- resonance
- strings
- tension
- fundamental-frequency
stage: formal-systems
status: draft
---

# Acoustic Resonance in Strings and Tension

## Core Idea
A string fixed at both ends resonates at discrete frequencies where standing waves fit: f_n = n v/(2L) = n/(2L) √(T/μ), where n = 1, 2, 3, ... (harmonics), v is wave speed, T is tension, L is length, and μ is linear mass density. The fundamental (n=1) has the longest wavelength; higher harmonics have progressively shorter wavelengths and higher frequencies.

## Questions

```yaml
- question: "A guitar string of length L resonates at fundamental frequency f₁. A guitarist frets the string at the midpoint, halving the vibrating length while keeping tension and mass density unchanged. The new fundamental frequency is..."
  type: multiple-choice
  options:
    - "2f₁ — halving the length doubles the fundamental frequency"
    - "f₁/2 — a shorter string vibrates more slowly"
    - "4f₁ — frequency scales as 1/L²"
    - "f₁√2 — frequency scales as 1/√L"
  answer: 0
  explanation: "The fundamental frequency is f₁ = (1/2L)√(T/μ). Halving L gives f = (1/(2·L/2))√(T/μ) = (1/L)√(T/μ) = 2f₁. Frequency is inversely proportional to length (not length squared or √L), so halving the length doubles the frequency — exactly one octave higher. This is the physical basis for how fretting works on stringed instruments."

- question: "Why are the resonant frequencies of a fixed string spaced at integer multiples of the fundamental (f₁, 2f₁, 3f₁, ...)?"
  type: multiple-choice
  options:
    - "Because each harmonic requires an integer number of half-wavelengths to fit between the fixed endpoints, and frequency is inversely proportional to wavelength at fixed wave speed"
    - "Because string tension increases proportionally with each successive harmonic, raising the frequency by equal steps"
    - "Because higher harmonics travel faster through the string, raising their frequency above the fundamental"
    - "Because each harmonic corresponds to a different linear mass density along the string"
  answer: 0
  explanation: "Fixed endpoints must be nodes, so the string length L must equal n·(λ/2) for integer n. This gives λₙ = 2L/n. Since f = v/λ, the resonant frequencies are fₙ = nv/(2L) = nf₁. The harmonic spacing is a direct consequence of the boundary constraint and the fixed wave speed — not changes in tension or density, which are properties of the string, not of the mode number."

- question: "Increasing the tension of a guitar string raises all of its resonant frequencies — fundamental and harmonics alike."
  type: true-false
  answer: true
  explanation: "True. The wave speed on the string is v = √(T/μ), so increasing tension T increases v. Since all resonant frequencies are fₙ = nv/(2L), every harmonic scales proportionally with v — the entire harmonic series shifts upward. A guitarist tightening a tuning peg raises the fundamental and all overtones simultaneously, maintaining the integer-multiple harmonic structure while shifting the overall pitch."

- question: "The second harmonic of a string has twice the wavelength of the fundamental."
  type: true-false
  answer: false
  explanation: "False — it has half the wavelength. The fundamental (n=1) has wavelength λ₁ = 2L: one half-wavelength fits across the string. The second harmonic (n=2) has two half-wavelengths fitting across L, so λ₂ = L = λ₁/2. The second harmonic has half the wavelength and twice the frequency of the fundamental. A common confusion is to associate 'second harmonic' with 'twice as large' — but wavelength and frequency move in opposite directions."

- question: "Explain why a string fixed at both ends cannot resonate at an arbitrary driving frequency — why only certain discrete frequencies produce standing waves."
  type: short-answer
  answer: "A string fixed at both ends must have displacement nodes (zero motion) at both endpoints, since neither end can move. A stable standing wave requires the reflected waves from each end to arrive back in phase with the original wave. This happens only when the round-trip distance (2L) equals an integer multiple of the wavelength — equivalently, when an integer number of half-wavelengths fits exactly between the endpoints: L = nλ/2. At any other driving frequency, reflections arrive out of phase and destructively interfere, preventing any sustained standing wave from building up."
  explanation: "These discrete, allowed wavelengths λₙ = 2L/n directly determine the resonant frequencies fₙ = nv/(2L). The harmonic series is not a coincidence — it is the set of frequencies whose wavelengths are compatible with the boundary conditions. This same logic applies to any resonating system with two boundaries: open or closed organ pipes, quantum mechanical particle-in-a-box, microwave cavities."
```

## Explainer

You already know from standing waves that when two identical waves travel in opposite directions along a medium, they can superimpose to form a stable pattern of **nodes** (points of zero displacement) and **antinodes** (points of maximum displacement). A string fixed at both ends has a boundary condition that forces both ends to be nodes — the string cannot move where it is attached. This constraint is what produces the discrete, quantized set of resonant frequencies.

Imagine driving the string with a vibrating source. Most driving frequencies produce a chaotic, rapidly-decaying response: the reflections from the two ends return out of phase and cancel the motion. But at certain special frequencies, the reflected wave arrives back in phase with the original — the two reinforce each other and the amplitude builds. These are the **resonant frequencies**, and they are exactly the frequencies for which a whole number of half-wavelengths fits between the endpoints. For the **fundamental** (first harmonic, n = 1), one half-wavelength spans the full length L, so λ₁ = 2L. For the **second harmonic** (first overtone, n = 2), two half-wavelengths fit, so λ₂ = L. In general, λ_n = 2L/n.

The connection to tension and mass density comes through the wave speed on the string: v = √(T/μ). This relationship has an intuitive basis — a tighter string (higher T) snaps back to equilibrium more forcefully, so disturbances travel faster. A heavier string (higher μ) has more inertia, so disturbances travel slower. Substituting v = fλ into f_n = v/λ_n gives f_n = n/(2L) · √(T/μ). So to raise all the resonant frequencies of a guitar string, you can either shorten it (decrease L), tighten it (increase T), or use a thinner string (decrease μ). Guitarists exploit all three: fretting shortens the vibrating length, tuning pegs adjust tension, and different strings have different mass densities.

The **harmonic series** f₁, 2f₁, 3f₁, ... has a deep consequence for musical timbre. When you pluck a guitar string, you excite many harmonics simultaneously. The relative amplitudes of each harmonic — not just the fundamental — determine the characteristic sound of the instrument. A violin and a flute playing the same note have the same fundamental frequency, but sound different because they excite different mixtures of harmonics. In this way, the physics of resonance on a string is the physical foundation for understanding timbre and musical acoustics.
