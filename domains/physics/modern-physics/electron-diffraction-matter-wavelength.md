---
id: electron-diffraction-matter-wavelength
title: Electron Diffraction and Matter Wave Properties
domain: physics
course: modern-physics
prerequisites:
- id: de-broglie-wavelength
  type: hard
- id: wave-particle-duality
  type: hard
- id: stern-gerlach-spin-quantization
  type: soft
builds-toward:
- davisson-germer-crystal-diffraction
tags:
- wave-particle-duality
- quantum-mechanics
- experimental
stage: advanced
status: validated
---
# Electron Diffraction and Matter Wave Properties

## Core Idea
Electrons, like photons, exhibit wave behavior with wavelength λ = h/p. When electrons pass through a small slit or reflect from a crystal, they produce diffraction patterns identical in form to those of waves with the same wavelength. This demonstrates the wave nature of matter predicted by de Broglie.

## How It's Best Learned
Calculate the de Broglie wavelength for electrons accelerated through various voltages. Compare predicted diffraction patterns with experimental observations using crystals or double slits. Use single-slit diffraction to measure the electron wavelength.

## Common Misconceptions
Electrons are not sometimes particles and sometimes waves—they have both properties (complementarity). The wavelength depends on momentum, so slower electrons have longer wavelengths and diffract more.

## Questions

```yaml
- question: "An electron is accelerated through a higher voltage in a diffraction experiment. Compared to a lower-voltage electron, how do its de Broglie wavelength and diffraction pattern change?"
  type: multiple-choice
  options:
    - "Higher voltage → longer wavelength → more spread-out diffraction pattern"
    - "Higher voltage → shorter wavelength → more tightly spaced diffraction fringes"
    - "Higher voltage → shorter wavelength → wider diffraction pattern, because faster electrons scatter more"
    - "Voltage does not affect wavelength; only the target crystal spacing determines the diffraction pattern"
  answer: 1
  explanation: "Higher voltage → greater kinetic energy → greater momentum p = √(2meV) → shorter de Broglie wavelength λ = h/p. Shorter wavelength produces diffraction maxima at smaller angles (from nλ = 2d sinθ, smaller λ means smaller θ), so the diffraction pattern is more compressed — fringes are more tightly spaced. The Common Misconceptions section notes that slower electrons have *longer* wavelengths and diffract *more*, which is the opposite of option A. Option D is wrong: crystal spacing d sets absolute angle positions, but changing λ predictably shifts the pattern."

- question: "Why were nickel crystals — rather than a pair of narrow slits — the natural choice for demonstrating electron diffraction in the Davisson-Germer experiment?"
  type: multiple-choice
  options:
    - "Nickel is magnetic, which focuses the electron beam into a coherent stream before diffraction"
    - "The nickel crystal lattice spacing (~0.2 nm) is comparable to the de Broglie wavelength of electrons accelerated through tens of volts, making it an effective diffraction grating"
    - "Double slits can deflect electrons but cannot produce interference; only crystal planes create the necessary standing waves"
    - "Nickel produces fluorescence that makes diffraction patterns directly visible to the naked eye"
  answer: 1
  explanation: "For diffraction to produce observable interference, the aperture or grating spacing must be comparable to the wavelength. Electrons accelerated through 50–100 V have de Broglie wavelengths of ~0.1–0.2 nm — precisely the scale of atomic spacings in crystal lattices. Nickel's lattice spacing of ~0.2 nm acts as a natural diffraction grating at exactly the right scale. Double slits could also demonstrate electron diffraction, but achieving nanometer-scale slit separations was technically prohibitive in 1927. The crystal also provides a large, regular, well-characterized periodic structure."

- question: "In a diffraction experiment, electrons accelerated through a lower voltage produce a more spread-out diffraction pattern than electrons at higher voltage."
  type: true-false
  answer: true
  explanation: "Lower voltage → lower kinetic energy → lower momentum p = √(2meV) → longer de Broglie wavelength λ = h/p. From the Bragg condition nλ = 2d sinθ, a longer wavelength corresponds to a larger diffraction angle θ for each order n. The diffraction peaks appear at wider angles — a more spread-out pattern. This is a direct experimental handle on the de Broglie wavelength: adjusting the accelerating voltage predictably shifts the pattern in the direction the formula demands."

- question: "In the Davisson-Germer experiment, electrons behaved as waves when reflecting from the crystal lattice but as particles when traveling through vacuum between the gun and the crystal."
  type: true-false
  answer: false
  explanation: "This is precisely the misconception that complementarity corrects. Electrons do not switch between wave and particle behavior depending on where they are in the apparatus. They always possess both properties simultaneously. Whether wave-like behavior (interference, diffraction) or particle-like behavior (localized detection) is *manifest* depends entirely on the experimental arrangement — specifically, whether conditions permit interference to be observable. The periodic crystal provides those conditions; a which-path measurement would suppress the interference pattern and reveal particle-like localization instead."

- question: "Why does measuring which crystal plane an electron reflected from destroy the diffraction pattern observed in the Davisson-Germer setup?"
  type: short-answer
  answer: "Diffraction patterns arise from interference between electron waves reflecting from many parallel crystal planes simultaneously — the electron's wave function is spread across multiple planes, and contributions from different planes add constructively at specific angles. Measuring which specific plane an electron reflected from localizes the electron to a single plane, collapsing the spatial coherence between contributions from different planes. Without interference between waves from multiple planes, there are no diffraction maxima — only a diffuse, structureless reflection. The information gained (which-path knowledge) necessarily destroys the interference."
  explanation: "This is a fundamental instance of complementarity: wave and particle information cannot be simultaneously maximized. Any measurement that determines which path an electron took destroys the interference that depends on all paths being simultaneously active. It is not a technological limitation but a structural feature of quantum mechanics. Electron diffraction was the proof that matter waves are not a metaphor — and the which-path erasure is the proof that complementarity is not a metaphor either."
```

## Explainer

De Broglie's hypothesis assigned a wavelength λ = h/p to any particle with momentum p. But a hypothesis is not confirmed until experiment tests it. The key question was: do electrons actually diffract the way waves do? If the de Broglie wavelength is real and physically meaningful, then electrons passing through an appropriate aperture or reflecting from an appropriate periodic structure should produce interference fringes — the unmistakable fingerprint of wave behavior.

The experiment that confirmed this was performed by **Clinton Davisson and Lester Germer** in 1927 (and independently by George Thomson). They directed a beam of electrons at a nickel crystal and observed that the reflected electrons arrived preferentially at specific angles — exactly the angles predicted by the Bragg diffraction condition nλ = 2d sin θ, using the de Broglie wavelength λ = h/p for the electron momentum. The crystal lattice spacing d (~0.2 nm for nickel) is comparable to the de Broglie wavelength of electrons accelerated through tens of volts (λ ~ 0.1–0.3 nm), making crystals ideal diffraction gratings for electron waves. The agreement between predicted and observed diffraction angles was quantitative and decisive.

The setup for understanding these experiments connects directly to what you know about waves: when a wave encounters a periodic structure with spacing d, constructive interference occurs at angles where the path length difference between waves from successive planes is an integer multiple of the wavelength. For electrons accelerated through voltage V, the kinetic energy is eV = p²/2m, so p = √(2meV) and λ = h/√(2meV). This lets you predict exactly where diffraction peaks should appear — and experiments confirm these predictions. Crucially, you can adjust λ by changing the accelerating voltage: lower voltage → lower momentum → longer wavelength → more spread-out diffraction pattern.

The deeper lesson is about **complementarity**: electrons do not choose to be particles in some experiments and waves in others. They always have both properties. Whether wave-like or particle-like behavior is manifest depends on the experimental arrangement. In the Davisson-Germer experiment, the periodic crystal structure creates conditions where interference is observable, and wave behavior dominates the measurement. If you instead measure which crystal plane each electron bounced from (a "which-path" measurement), the diffraction pattern disappears. Electron diffraction was the experimental proof that the de Broglie relation is not an analogy or a metaphor — matter genuinely has a wave nature, and quantum mechanics must account for it.
